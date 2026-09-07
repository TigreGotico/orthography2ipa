"""Running an engine on a caller's own spec, and exporting ``syllabify_ipa``.

A downstream whose spec is a variation on a shipped one — a
``dataclasses.replace`` copy that teaches the stress rules one more written
accent — needs the engine built on that copy, not on the registry's. The
copy must stay the caller's: the registry's object is shared by every other
caller in the process, and a transcription that moves because an unrelated
engine was constructed first is a wrong number that looks fine.
"""
from dataclasses import replace

import orthography2ipa
from orthography2ipa import G2P, get

#: U+0301, the accent Cyrillic stress annotation writes after the vowel.
COMBINING_ACUTE = "́"


def _acute_aware(spec):
    """*spec* with the combining acute added to its written stress marks."""
    return replace(spec, stress=replace(
        spec.stress,
        marked_vowels=tuple(spec.stress.marked_vowels) + (COMBINING_ACUTE,)))


class TestSpecOverride:
    def test_the_engine_runs_on_the_spec_it_was_given(self):
        spec = _acute_aware(get("uk"))
        assert G2P("uk", spec=spec).spec is spec

    def test_the_given_spec_moves_the_transcription(self):
        """Ukrainian declares no written stress marks, so an annotated word
        is stressed by rule; teaching the spec the acute honours the page."""
        word = "молоко" + COMBINING_ACUTE
        assert G2P("uk").transcribe(word) == "mɔˈɫɔkɔ"
        assert G2P("uk", spec=_acute_aware(get("uk"))).transcribe(word) == (
            "mɔɫɔˈkɔ")

    def test_it_reaches_what_construction_derives(self):
        """The sandhi engine is compiled from the spec during construction,
        which is why the spec has to arrive as an argument."""
        no_sandhi = replace(get("pt-PT"), sandhi_rules=())
        assert G2P("pt-PT").transcribe("os amigos") == "oz ɐˈmiɡuʃ"
        assert G2P("pt-PT", spec=no_sandhi).transcribe("os amigos") == (
            "oʃ ɐˈmiɡuʃ")

    def test_lang_still_names_the_language(self):
        spec = _acute_aware(get("uk"))
        assert G2P("ukr", spec=spec).lang == "uk"

    def test_omitting_it_uses_the_registry(self):
        assert G2P("uk").spec is get("uk")


class TestTheRegistryIsUntouched:
    def test_the_shared_spec_never_learns_the_acute(self):
        before = tuple(get("uk").stress.marked_vowels)
        G2P("uk", spec=_acute_aware(get("uk"))).transcribe(
            "молоко" + COMBINING_ACUTE)
        assert tuple(get("uk").stress.marked_vowels) == before == ()

    def test_a_bare_engine_transcribes_identically_afterwards(self):
        word = "молоко" + COMBINING_ACUTE
        before = G2P("uk").transcribe(word)
        G2P("uk", spec=_acute_aware(get("uk"))).transcribe(word)
        assert G2P("uk").transcribe(word) == before

    def test_the_two_engines_do_not_share_a_spec(self):
        plain = G2P("uk")
        stressed = G2P("uk", spec=_acute_aware(get("uk")))
        assert plain.spec is not stressed.spec
        assert COMBINING_ACUTE not in plain.spec.stress.marked_vowels


class TestSyllabifyIpaIsPublic:
    def test_it_imports_from_the_package_root(self):
        from orthography2ipa import syllabify_ipa

        assert syllabify_ipa("mɔɫɔkɔ") == [
            "mɔ", "ɫɔ", "kɔ"]

    def test_it_is_exported(self):
        assert "syllabify_ipa" in orthography2ipa.__all__

    def test_it_is_the_implementation(self):
        from orthography2ipa.stress import syllabify_ipa

        assert orthography2ipa.syllabify_ipa is syllabify_ipa
