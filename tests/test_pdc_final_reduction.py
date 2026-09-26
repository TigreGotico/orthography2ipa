"""Cited-rule conformance: Pennsylvania German (pdc) word-final vowel
reduction and coda-/r/ vocalisation.

The flat grapheme table already listed /ə/ as a candidate for <e> and /ɐ/
as a candidate for <r>, but nothing in the spec ever selected them: the
engine always emitted the full-quality values [ɛ] and [r], including in
unstressed word-final position, so the reduced candidates were dead
alternatives no word could reach. This is the ordinary Germanic reduction
of unstressed final syllables to schwa and vocalisation of coda /r/ to
[ɐ] (cf. Standard German unstressed final <e> = [ə] and final <-er> =
[ɐ]; Wiese (1996) *The Phonology of German*, OUP — claim is standard,
edition not consulted for a page locator), and Louden (2016)
*Pennsylvania Dutch: The Story of an American Language* documents PG's
general unstressed-vowel reduction to schwa (claim is standard, edition
not consulted for a page locator).

Checked directly against the pdc/wikipron gold: every word whose only
final <e> is the plain grapheme (not part of <ie>/<ee>) realises final
[ə] there, and every word-final <r> in the gold (Bruder, Vadder, Kinner,
der, mir, wer, ...) realises [ɐ], none stay [r].
"""
from orthography2ipa.g2p import G2P


def _t(word):
    return G2P("pdc").transcribe_word(word).lstrip("ˈ")


def test_pdc_word_final_e_reduces_to_schwa():
    """Attested throughout the pdc/wikipron gold (e.g. Aabaue -> [ɔːbaʊə],
    Aabede -> [ɔːbeːdə]): a plain <e> that is the word's own last
    grapheme is a schwa, never [ɛ]."""
    assert _t("bede") == "bɛdə"
    assert _t("aabaue").endswith("ə")


def test_pdc_non_final_e_keeps_full_quality():
    """The reduction is positional: a non-final <e> keeps [ɛ] (the first
    <e> of 'bede' above, before the reduced final one)."""
    assert _t("bede").startswith("bɛd")


def test_pdc_word_final_r_vocalises_to_turned_a():
    """Attested for every word-final <r> token in the pdc/wikipron gold
    (der -> [dɛɐ̯], mir -> [miːɐ̯], Bruder -> [bruːdɐ]): word-final <r>
    is always [ɐ], never [r]."""
    assert _t("der").endswith("ɐ")
    assert _t("mir").endswith("ɐ")


def test_pdc_non_final_r_stays_consonantal():
    """The vocalisation is positional, not a blanket rewrite of the
    grapheme: <r> before a vowel keeps its consonantal value."""
    assert _t("rot").startswith("r")
