"""The it-IT-x-* varieties read ⟨c g i u⟩ as Italian spelling does.

The central varieties (Marche, Rome, Tuscany, Umbria) write standard Italian
spelling and take the it-IT grapheme table through ``graphemes_base``. ⟨c g⟩
are [tʃ dʒ] before ⟨e i⟩ and [k ɡ] elsewhere: cielo [ˈtʃɛːlo], gelo [ˈdʒɛːlo]
(Bertinetto & Loporcaro, "The sound pattern of Standard Italian", JIPA 35(2),
2005, p. 133). ⟨i u⟩ before a vowel are the glides of the opening diphthongs
(Table 2, p. 138): pieno [ˈpjɛːno], chiave [ˈkjaːve], guida [ˈɡwiːda] (p. 139).
The other expected values are the WikiPron Italian broad transcriptions
(``ita_latn_broad.tsv``).

Abruzzese is a dialect with its own spelling. Finamore, *Vocabolario dell'uso
abruzzese* (1893), pp. 12-13, gives ⟨c⟩ as velar, "Anche palatino: 'Cèlle,
augello; Cèveze, gelso; Ducènde, dugento; Damecèlle" (§29), and ⟨g⟩ "innanzi
ad e, i, ha sempre pronunzia intensa: Ggènde, Ggesù, Ggire, Leggìteme,
Relleggióne, Luvigge" (§39).

The comparison folds what the spelling cannot show and the tests do not check:
stress, length, the open/close mid vowels, and the tie bar.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P

CENTRAL = ["it-IT-x-marche", "it-IT-x-roma", "it-IT-x-toscana",
           "it-IT-x-umbria"]

STANDARD = [
    ("città", "t͡ʃ i t t a"),      # WikiPron
    ("cena", "t͡ʃ e n a"),         # WikiPron
    ("gente", "d͡ʒ ɛ n t e"),      # WikiPron
    ("pagina", "p a d͡ʒ i n a"),   # WikiPron
    ("giro", "d͡ʒ i r o"),         # WikiPron
    ("pieno", "ˈpjɛːno"),         # Bertinetto & Loporcaro 2005, p. 139
    ("chiave", "ˈkjaːve"),        # p. 139
    ("guida", "ˈɡwiːda"),         # p. 139
]


def _fold(ipa: str) -> str:
    out = []
    for ch in ipa:
        if ch in " ˈˌː͡":
            continue
        ch = {"ɛ": "e", "ɔ": "o"}.get(ch, ch)
        if out and out[-1] == ch:
            continue
        out.append(ch)
    return "".join(out)


@pytest.mark.parametrize("lang", CENTRAL)
@pytest.mark.parametrize("word,expected", STANDARD)
def test_central_variety_reads_standard_spelling(lang, word, expected):
    assert _fold(G2P(lang).transcribe_word(word)) == _fold(expected)


def test_roman_intervocalic_s_stays_voiceless():
    # "Intervocalic /s/ is voiceless in RI, so that SI minimal pairs, such as
    # [ˈkjɛːse] 'asked.3sg' vs. [ˈkjɛːze] 'churches' (both spelled chiese),
    # are neutralised as [ˈkjɛːse] in RI" (p. 133).
    assert _fold(G2P("it-IT-x-roma").transcribe_word("chiese")) == _fold("ˈkjɛːse")


def _candidates(lang: str, word: str) -> list:
    g2p = G2P(lang, expand_allophones=True)
    return [path.ipa for path in g2p.candidates(word, beam_width=32)]


def test_tuscan_deaffrication_variant_reaches_the_affricate():
    # FI and RI "display deaffrication of intervocalic /tʃ/ (cf. pace
    # [ˈpaːʃe] 'peace' […])" (p. 135). The spec states it in its allophone
    # map, which applies only once ⟨c⟩ before ⟨e⟩ reads /tʃ/.
    paths = _candidates("it-IT-x-toscana", "pace")
    assert paths[0] == "patʃe"
    assert "paʃe" in paths


def test_roman_affricate_gemination_variant_reaches_the_affricate():
    # "In RI, by contrast, intervocalic /dʒ/ geminates ([ˈadːʒo] […])"
    # (p. 135), stated in the spec's allophone map.
    paths = _candidates("it-IT-x-roma", "agio")
    assert paths[0] == "adʒo"
    assert "adːʒo" in paths


ABRUZZESE_PALATAL = [
    ("cèveze", 0, "tʃ"),       # §29
    ("ducènde", 2, "tʃ"),      # §29
    ("damecèlle", 4, "tʃ"),    # §29
    ("ggire", 0, "dːʒ"),       # §39
    ("leggìteme", 2, "dːʒ"),   # §39
    ("luvigge", 4, "dːʒ"),     # §39
]


@pytest.mark.parametrize("word,index,expected", ABRUZZESE_PALATAL)
def test_abruzzese_c_g_before_front_vowel_are_palatal(word, index, expected):
    ipa = G2P("it-IT-x-abruzzo").transcribe_word(word)
    assert ipa[index:index + len(expected)] == expected, ipa


@pytest.mark.parametrize("word,index", [("cajòle", 0), ("lattuche", 5)])
def test_abruzzese_c_elsewhere_stays_velar(word, index):
    # §29: "Iniziale, ha suono rotondo […] Così anche mediano": Cajòle, Lattuche.
    ipa = G2P("it-IT-x-abruzzo").transcribe_word(word)
    assert ipa[index] == "k", ipa
