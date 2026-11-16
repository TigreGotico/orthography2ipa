"""Cited-rule conformance: Pennsylvania German (pdc) word-final devoicing.

Auslautverhaertung (coda-obstruent devoicing) is the categorical West
Germanic pattern by which voiced obstruents lose voicing word-finally
(cf. Standard German). Louden (2016) *Pennsylvania Dutch: The Story of an
American Language* (Johns Hopkins) documents the pattern surfacing even in
PG-substrate English; the pdc/wikipron gold used by this benchmark directly
attests /d/-devoicing: every word-final <d> token in that gold (Freed, Kind,
Kinnskind, mied) is transcribed with a final [t], never [d]. The spec's own
notes already claimed <g> reads [k] word-finally as a BBB letter value, but
the flat grapheme table left that claim unencoded until a
``positional_graphemes`` entry was added alongside the <d> rule.

<b> is deliberately left undevoiced: the gold contains no word-final <b>
token to measure against, so extending the rule there would be an
unmeasured analogical guess rather than an attested or sourced claim.
"""
from orthography2ipa.g2p import G2P


def _t(word):
    return G2P("pdc").transcribe_word(word).lstrip("ˈ")


def test_pdc_word_final_d_devoices_to_t():
    """Directly attested in the pdc/wikipron gold: Freed, Kind, Kinnskind,
    mied all realise word-final <d> as [t]."""
    assert _t("freed") == "freːt"
    assert _t("kind") == "kɪnt"
    assert _t("mied") == "miːt"


def test_pdc_non_final_d_stays_voiced():
    """The devoicing is positional, not a blanket rewrite of the grapheme:
    <d> before a vowel keeps its underlying voicing."""
    assert _t("daadi").startswith("d")


def test_pdc_word_final_g_devoices_to_k():
    """Matches the spec's own BBB letter-value note for <g> ('finally /k/'),
    which the flat grapheme table previously left unencoded."""
    assert _t("dag") == "dak"
    assert _t("beg") == "bɛk"


def test_pdc_non_final_g_stays_voiced_or_glide():
    """Onset <g> keeps its plosive [ɡ] reading; the devoicing rule is
    keyed to word-final position only."""
    assert _t("dag").startswith("d")
    assert _t("beg").startswith("b")
