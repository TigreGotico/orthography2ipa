"""Mirandese values taken from Leite de Vasconcellos, Estudos de Philologia
Mirandesa I (1900), and from the Convenção Ortografica da Lingua Mirandesa
(1999) where it is named.

Each expected string is written by hand from the source, not copied from the
engine. The spec writes broad symbols, so LdV's mid e and o are [e] and [o], his
"a surdo" is [ɐ], his "e surdo" is [ɨ], and his tonic and atonic o is [o] and
[u] (p. 200). A test marked "unchanged" holds a neighbour on which a rule must
not fire.

  item 1   ⟨ê⟩ = [e]                          Convenção, letter table E (PDF p. 9)
  item 6   initial ⟨l⟩ = [l]                   p. 188 "lĩ-ndo", "Como em português na palavra lapa"
  item 7   ⟨v⟩ = ⟨b⟩                           §14, p. 193
  item 14  apical s voiced before voiced C     p. 190
  item 15  coda l and article l = [ɫ]          p. 188
  item 21  final ç voiced before voiced C      p. 190
  item 22  medieval notes                      §14 p. 193, p. 200
"""
import json
import unicodedata
from pathlib import Path

import pytest

from orthography2ipa import G2P

DIALECTS = ["mwl", "mwl-x-sendim", "mwl-x-ifanes"]
S = "s̺"
Z = "z̺"
DATA = Path(__file__).resolve().parent.parent / "orthography2ipa" / "data"


def nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def ipa(dialect: str, text: str) -> str:
    return nfc(G2P(dialect).transcribe(text))


def first_word(dialect: str, text: str) -> str:
    return ipa(dialect, text).split(" ")[0]


@pytest.fixture(scope="module", params=DIALECTS)
def dialect(request):
    return request.param


# item 1 ----------------------------------------------------------------------

def test_ye_keeps_its_nucleus(dialect):
    # ⟨y⟩ [j] + ⟨ê⟩ [e], one syllable
    assert ipa(dialect, "yê") == "ˈje"


def test_yerba_keeps_its_nucleus(dialect):
    # [j] [e] [ɾ] ... [ɐ]: the tap after e is p. 191 (chorar); the b/β after r
    # belongs to another rule and is not asserted
    out = ipa(dialect, "yêrba")
    assert out.startswith("ˈjeɾ") and out.endswith("ɐ")


def test_yeuga_keeps_its_nucleus(dialect):
    # stress is not asserted: no source gives it
    out = ipa(dialect, "yêuga").replace("ˈ", "")
    assert out == "jeuɣɐ"


# item 6 ----------------------------------------------------------------------

def test_initial_l_is_l_in_a_loan(dialect):
    # p. 188: l is "Como em português na palavra lapa"; tr is t + tap (p. 191)
    assert ipa(dialect, "litro") == "ˈlitɾu"


def test_initial_l_before_nasal_vowel(dialect):
    # p. 188 "lĩ-ndo". The nasal consonant that LdV keeps is outside this rule,
    # so any [n] is removed before the comparison.
    assert ipa(dialect, "lindo").replace("n", "") == "ˈlĩdu"


def test_initial_lh_stays_palatal():
    # p. 191: lh as in Portuguese. Sendinês has [l], by its own rule.
    assert ipa("mwl", "lhargo").startswith("ˈʎaɾ")
    assert ipa("mwl-x-ifanes", "lhargo").startswith("ˈʎaɾ")


def test_medial_l_in_onset_is_unchanged(dialect):
    # p. 188 "bolar"
    assert ipa(dialect, "bolar") == "buˈlaɾ"


# item 7 ----------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("vaca", "ˈbakɐ"),                  # initial: stop
    ("uva", "ˈuβɐ"),                    # between vowels: spirant, p. 187
    ("vocabulário", "bukɐβuˈlaɾiu"),    # initial stop, then b between vowels
    ("envidar", "ɨ̃biˈdaɾ"),            # after a nasal: stop
])
def test_v_is_b(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_v_after_a_nasal_across_words(dialect):
    # a word starting after a nasal vowel keeps the stop (p. 187)
    assert ipa(dialect, "un vaco") == "ˈũ ˈbaku"


def test_b_and_v_give_the_same_word(dialect):
    # §14 p. 193: "não existe differença entre b e v"
    for v_word, b_word in [("vaca", "baca"), ("uva", "uba"), ("envidar", "enbidar")]:
        assert ipa(dialect, v_word) == ipa(dialect, b_word)


def test_v_is_not_in_the_phoneme_inventory(dialect):
    assert "v" not in G2P(dialect).spec.allophones


def test_f_is_unchanged(dialect):
    assert ipa(dialect, "fame") == "ˈfamɨ"


# item 14 ---------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("asno", f"ˈa{Z}nu"),       # p. 190 "asno"
    ("mesmo", f"ˈme{Z}mu"),     # Convenção S "mesmo"
    ("cismar", f"si{Z}ˈmaɾ"),   # Convenção S "cismar"
])
def test_apical_s_is_voiced_before_a_voiced_consonant_in_a_word(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("pasta", f"ˈpa{S}tɐ"),     # voiceless t
    ("casca", f"ˈka{S}kɐ"),     # voiceless k
    ("rosa", f"ˈro{Z}ɐ"),       # between vowels: voiced already, p. 190 "rosa"
])
def test_apical_s_is_unchanged_elsewhere_in_a_word(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_final_apical_s_is_voiced_before_a_voiced_consonant(dialect):
    # p. 190 "final de palavra antes de consoante sonora": ls nius
    assert nfc(f"ˈma{Z}") == first_word(dialect, "mas bonos")
    assert first_word(dialect, "ls nius").endswith(Z)


def test_final_apical_s_is_voiced_before_the_plural_article(dialect):
    # ls starts with the voiced consonant [ɫ] (p. 188)
    assert first_word(dialect, "mas ls pais") == nfc(f"ˈma{Z}")


@pytest.mark.parametrize("text", ["mas pai", "mas", "mas amigos"])
def test_final_apical_s_is_unchanged_before_a_voiceless_consonant_or_pause(dialect, text):
    assert first_word(dialect, text) == nfc(f"ˈma{S}")


def test_final_apical_s_is_not_voiced_across_a_comma(dialect):
    assert first_word(dialect, "mas, bonos").rstrip(",") == nfc(f"ˈma{S}")


# item 15 ---------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("caldo", "ˈkaɫdu"),         # p. 188 "caldo"
    ("sol", f"ˈ{S}oɫ"),          # p. 188 "sol"
    ("alto", "ˈaɫtu"),           # l closes the first syllable
])
def test_coda_l_is_velarised(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_article_l_before_a_consonant_is_velarised(dialect):
    # p. 188 "l pai"
    assert ipa(dialect, "l pai") == "ɫ ˈpaj"


def test_article_l_before_a_vowel_is_unchanged(dialect):
    # p. 188 names the article only "antes de consoante"
    assert first_word(dialect, "l amigo") == "l"


def test_plural_article_is_velarised(dialect):
    # p. 188 "ls dedos"; the s is voiceless before p and voiced before d
    assert ipa(dialect, "ls pais").split(" ")[0] == nfc(f"ɫ{S}")
    assert ipa(dialect, "ls dedos").split(" ")[0] == nfc(f"ɫ{Z}")


@pytest.mark.parametrize("word, expected", [
    ("lapa", "ˈlapɐ"),           # p. 188: onset l
    ("plano", "ˈplanu"),         # l in an onset cluster
    ("bolar", "buˈlaɾ"),
])
def test_onset_l_is_unchanged(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_lh_is_not_velarised():
    assert ipa("mwl", "alho") == "ˈaʎu"


# item 21 ---------------------------------------------------------------------

@pytest.mark.parametrize("dialect, text, expected", [
    ("mwl", "lhuç del cielo", "ˈʎuz"),             # p. 190 "lhuç del cielo"
    ("mwl-x-ifanes", "lhuç del cielo", "ˈʎuz"),
    ("mwl-x-sendim", "lhuç del cielo", "ˈluz"),    # Sendinês lh = [l]
    ("mwl", "paç de la tiêrra", "ˈpaz"),           # Convenção Ç
])
def test_final_c_cedilla_is_voiced_before_a_voiced_consonant(dialect, text, expected):
    assert first_word(dialect, text) == expected


@pytest.mark.parametrize("text", ["lhuç pai", "lhuç", "lhuç amigos"])
def test_final_c_cedilla_is_unchanged_before_a_voiceless_consonant_vowel_or_pause(text):
    assert first_word("mwl", text) == "ˈʎus"


def test_final_c_cedilla_is_not_voiced_across_a_comma():
    assert first_word("mwl", "lhuç, del cielo").rstrip(",") == "ˈʎus"


def test_final_z_is_unchanged_before_a_voiced_consonant():
    # z already has the voiced value of the Porto z (p. 190)
    assert first_word("mwl", "paz del") == "ˈpaz"


# item 22 and the cited rules ---------------------------------------------------

def spec_json(code: str) -> dict:
    return json.loads((DATA / f"{code}.json").read_text(encoding="utf-8"))


def test_medieval_notes_do_not_claim_a_distinct_v_or_no_reduction_in_modern_mirandese():
    notes = spec_json("ast-PT-x-medieval")["notes"]
    assert "this persists in modern Mirandese" not in notes
    assert "NO VOWEL REDUCTION" not in notes
    assert "Na pronúncia normal mirandesa não existe differença entre b e v" in notes
    assert "a surdo port." in notes


def mwl_rules() -> dict:
    return {r["id"]: r for r in spec_json("mwl")["allophone_rules"]}


@pytest.mark.parametrize("rule_id", ["AST_NASAL_e", "AST_NASAL_o", "MWL_NASAL_E_OPEN"])
def test_nasal_mid_vowel_rules_cite_ldv_pages_180_and_201(rule_id):
    notes = mwl_rules()[rule_id]["notes"]
    assert "Tão aberto como em" in notes and "p. 180" in notes
    assert "p. 201" in notes
    assert "Mateus" not in notes


def test_nasal_mid_vowel_values_are_kept():
    rules = mwl_rules()
    assert (rules["AST_NASAL_e"]["surface"], rules["AST_NASAL_o"]["surface"],
            rules["MWL_NASAL_E_OPEN"]["surface"]) == ("ẽ", "õ", "ẽ")
    # p. 180 "drento", "pongo"; the nasal consonant LdV keeps is outside these rules
    assert ipa("mwl", "drento").replace("n", "") == "ˈdɾẽtu"
    assert ipa("mwl", "pongo").replace("ŋ", "").replace("n", "") == "ˈpõɡu"


def test_new_rules_cite_ldv_with_a_page():
    spec = spec_json("mwl")
    rules = {r["id"]: r for r in spec["allophone_rules"]}
    sandhi = {r["id"]: r for r in spec["sandhi_rules"]}
    for rule in [*rules.values(), *sandhi.values()]:
        if rule["id"].startswith(("MWL_S_VOICING", "MWL_FINAL_S_VOICING", "MWL_FINAL_C_VOICING",
                                  "MWL_L_VELAR", "MWL_ARTICLE_L_VELAR")):
            assert "Vasconcellos" in rule["notes"] and "p. 1" in rule["notes"], rule["id"]
