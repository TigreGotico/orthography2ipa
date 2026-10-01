"""An unknown private-use variant is refused, and the region fallback stays.

Before this, ``G2P("ar-BH-x-baharna")`` answered with the Bahraini Sunni spec —
261 graphemes, confident Arabic output — and nothing in the result said a
substitution had happened. A reviewer read a complete baseline column from the
wrong spec. The same path answers any invented lect: ``ar-XX-x-nonsense`` gets
MSA, ``pt-BR-x-nothing`` gets Brazilian Portuguese, each with one DEBUG line
nobody sees.

Ruled 2026-09-25, decision ``o2i-resolver-fallback``: refuse by default, with
``fallback=True`` as the opt-in, and expose the substitution when a caller opts
in.

The boundary is the one the audit drew. A region tag the registry does not
carry is ordinary BCP-47 matching within one language, and a caller can want it:
``ar-ZZ`` → ``ar`` and ``en-NZ`` → ``en-GB`` stay. A private-use ``-x-`` subtag
is a claim that a named lect exists, so answering it with a sibling is
answering a different question.
"""
import pytest

from orthography2ipa import G2P, get, resolve, resolves_exactly
from orthography2ipa.exceptions import UnknownLanguageVariantError


class TestAnInventedLectIsRefused:

    @pytest.mark.parametrize("tag", [
        "ar-XX-x-nonsense",
        "pt-BR-x-nothing",
        "ar-x-nothing",
    ])
    def test_get_refuses(self, tag):
        with pytest.raises(UnknownLanguageVariantError):
            get(tag)

    @pytest.mark.parametrize("tag", [
        "ar-XX-x-nonsense",
        "pt-BR-x-nothing",
    ])
    def test_resolve_refuses(self, tag):
        with pytest.raises(UnknownLanguageVariantError):
            resolve(tag)

    def test_the_engine_refuses(self):
        with pytest.raises(UnknownLanguageVariantError):
            G2P("ar-XX-x-nonsense")

    def test_the_error_names_what_was_asked_and_what_was_offered(self):
        """A caller has to be able to act on it: the message says the variant
        is unknown, and names the spec that would have answered."""
        with pytest.raises(UnknownLanguageVariantError) as ctx:
            get("ar-XX-x-nonsense")
        err = ctx.value
        assert err.requested == "ar-XX-x-nonsense"
        assert err.substitute == "ar"
        assert "fallback=True" in str(err)
        assert "ar-XX-x-nonsense" in str(err)

    def test_it_is_catchable_as_a_key_error(self):
        """Every caller that already catches KeyError from get() keeps
        working, because that is what get() raised for an unknown language."""
        with pytest.raises(KeyError):
            get("ar-XX-x-nonsense")


class TestTheRegionFallbackIsKept:
    """The control. If these moved, the change would have removed BCP-47
    matching rather than the silent lect substitution."""

    @pytest.mark.parametrize("tag,expected", [
        ("ar-ZZ", "ar"),
        ("en-NZ", "en-GB"),
    ])
    def test_an_unregistered_region_still_resolves(self, tag, expected):
        assert resolve(tag) == expected
        assert get(tag).graphemes

    def test_the_engine_still_builds_on_one(self):
        g2p = G2P("ar-ZZ")
        assert g2p.lang == "ar"
        assert g2p.substituted is False

    @pytest.mark.parametrize("tag", [
        "ar-EG",            # exact
        "arz",              # alias
        "AR-eg",            # case folding
        "ar-SA",            # curated region default
        "ar-BH-x-baharna",  # a registered private-use lect
    ])
    def test_a_deliberate_resolution_is_untouched(self, tag):
        """Aliases, case folding and the curated defaults name a spec
        deliberately. Only the guess is refused."""
        assert resolves_exactly(tag)
        assert get(tag).graphemes


class TestADeclaredIsoCodeIsNotAGuess:
    """A spec's own ISO 639-3 declaration crosses the primary subtag by design.

    ``ar-TN`` declares ``aeb`` and ``tl`` declares ``tgl``. The distance match
    has to cross languages to get there, but the spec itself says that code
    names the language it describes, so it is as deliberate as an alias. This
    was a real defect in the first cut of the refusal: three declared codes
    started raising.
    """

    @pytest.mark.parametrize("iso,spec_code", [
        ("aeb", "ar-TN"),
        ("arq", "ar-DZ"),
        ("tgl", "tl"),
    ])
    def test_a_declared_iso_code_still_reaches_its_spec(self, iso, spec_code):
        assert resolve(iso) == spec_code
        assert get(iso).code == spec_code

    def test_an_undeclared_three_letter_code_is_still_unknown(self):
        """The control: the exemption reads the spec's declaration, it does not
        wave through anything that happens to be three letters."""
        with pytest.raises(KeyError):
            get("zzz")


class TestOptingIn:

    def test_fallback_true_restores_the_substitution(self):
        spec = get("ar-XX-x-nonsense", fallback=True)
        assert spec.code == "ar"
        assert spec.graphemes

    def test_the_engine_exposes_what_it_substituted(self):
        """The second half of the ruling: when a caller opts in, the result
        says a substitution happened rather than hiding it in a DEBUG line."""
        g2p = G2P("ar-XX-x-nonsense", fallback=True)
        assert g2p.requested == "ar-XX-x-nonsense"
        assert g2p.lang == "ar"
        assert g2p.substituted is True

    def test_an_opted_in_engine_still_transcribes(self):
        g2p = G2P("ar-XX-x-nonsense", fallback=True)
        assert g2p.transcribe("كتاب")

    def test_opting_in_does_not_invent_a_language(self):
        """fallback=True is not "answer anything": an unknown primary subtag
        has nothing to fall back to and still raises."""
        with pytest.raises(KeyError):
            get("zz-ZZ", fallback=True)
