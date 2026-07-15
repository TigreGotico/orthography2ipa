"""The modern Arabic varieties read MSA orthography the way ``ar`` does.

Every modern spoken variety in the data set is *written* in MSA orthography, so
its grapheme layer must carry the ``ar`` leaf's orthographic readings — the
onset-glide digraphs, the hamza carriers, the word-final matres, pausal tāʾ
marbūṭa. Its own tables then override the *phonology* (qāf reflex, interdentals,
affrication) on top.

Two mechanisms make that true, and both are asserted here:

* the three proto nodes (``ar-x-peninsular`` / ``ar-x-mashriqi`` /
  ``ar-x-maghrebi``) take their grapheme layer from ``ar``, not from Classical
  ``arb``, which has none of those readings;
* a spec that declares ``graphemes_base`` but no ``positional_graphemes_base``
  inherits the positional table through the same edge — positional entries
  refine the grapheme table they belong to, so inheriting one without the other
  yields half a table.
"""
import pytest

from orthography2ipa import get

#: Every modern spoken variety written in Arabic script.
DIALECTS = [
    "ar-x-peninsular", "ar-x-mashriqi", "ar-x-maghrebi", "ar-x-gulf",
    "ar-x-levantine", "ar-SA-x-najd", "ar-SA-x-hejaz", "ar-EG", "ar-IQ",
    "ar-SY", "ar-LB", "ar-JO", "ar-PS", "ar-MA", "ar-DZ", "ar-TN", "ar-LY",
    "ar-AE", "ar-BH", "ar-KW", "ar-QA", "ar-OM", "ar-YE", "ar-SD",
]

#: The positional graphemes the ``ar`` leaf declares; these are the readings a
#: variety silently lost when its chain bottomed out at Classical ``arb``.
AR_POSITIONAL = {"أ", "إ", "ي", "و", "ا", "ة"}


@pytest.mark.parametrize("code", DIALECTS)
def test_dialect_inherits_positional_graphemes(code):
    """A dialect resolves the ar leaf's positional table, not an empty one."""
    positional = get(code).positional_graphemes or {}
    assert AR_POSITIONAL <= set(positional), (
        f"{code} is missing positional readings {AR_POSITIONAL - set(positional)}"
    )


@pytest.mark.parametrize("code", DIALECTS)
def test_dialect_inherits_onset_glide_digraphs(code):
    """The ⟨يَ⟩/⟨وَ⟩ onset digraphs (/ja/, /wa/) reach every dialect.

    Without them a fatḥa-bearing yāʾ is read as the diphthong /aj/, so
    يَوْم surfaces as ``ajwm`` rather than ``jawm``.
    """
    graphemes = get(code).graphemes
    assert {"يَ", "وَ"} <= set(graphemes)


def test_classical_does_not_carry_the_msa_readings():
    """Guards the premise: ``arb`` is the layer that lacks them."""
    # Classical carries exactly the tāʾ marbūṭa positional pair — [at] when a
    # vowel follows (inflected context), [a] pre-pausally — which is Classical
    # grammar (Wright I §297), not an MSA-only reading. Nothing else.
    assert set((get("arb").positional_graphemes or {})) <= {"ة", "َة"}


@pytest.mark.parametrize("code,expected_qaf", [
    ("ar", "q"),                # MSA keeps the uvular stop
    ("ar-SA-x-najd", "ɡ"),      # Najdi: qāf → /ɡ/ (Ingham 1994)
    ("ar-SA-x-hejaz", "ɡ"),     # Hejazi: qāf → /ɡ/ (Omar 1975)
    ("ar-x-gulf", "ɡ"),         # Gulf: Old Arabic *q → [ɡ]
])
def test_dialect_phonology_still_overrides_the_inherited_layer(code, expected_qaf):
    """Inheriting ar's orthography must not overwrite a variety's own reflexes.

    ``ar`` reads ⟨ق⟩ as /q/. A variety that declares a /ɡ/ reflex keeps it — its
    own table sits *above* the inherited orthographic layer, so pulling the
    grapheme base up from Classical to MSA must not flip the reflex back.
    """
    qaf = get(code).graphemes["ق"]
    assert qaf[0] == expected_qaf
