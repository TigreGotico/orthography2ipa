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
  item 2   nasal consonant kept before a stop  pp. 187-188
  item 3   ⟨uo⟩ = [ʊ]                          pp. 177, 180, 182, 226
  item 4   ⟨ie⟩ = [jɪ]                         pp. 173, 180, 182, 220
  item 5   ⟨é⟩, ⟨ó⟩ = [e], [o]                 §22, pp. 197-198
  item 8   d spirant                           p. 188
  item 9   b, v and g spirants                 pp. 187, 192
  item 12  ⟨ou⟩ = [ɵw]                         pp. 174, 183
  item 13  final -on = [ɵ̃w̃]                    §110, p. 257
  item 16  [ŋ] between a nasal vowel and a vowel   p. 192
  item 17  ⟨y⟩ = [ʝ]                           p. 191
  item 18  final -ie, -ue in two syllables     pp. 174, 177, 185, 225
  items 19 and 20  Sendinês lh and -ien        pp. 185, 220, 226, 259
  final -uo, final y, b and d after a vowel    pp. 177, 187, 188, 191, 200
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
    # ⟨y⟩ [ʝ] (p. 191) + ⟨ê⟩ [e], one syllable
    assert ipa(dialect, "yê") == "ˈʝe"


def test_yerba_keeps_its_nucleus(dialect):
    # [ʝ] [e] [ɾ] [β] [ɐ]: the tap after e is p. 191 (chorar), the spirant
    # after r is p. 187 ("depois de consoante sonora")
    assert ipa(dialect, "yêrba") == "ˈʝeɾβɐ"


def test_yeuga_keeps_its_nucleus(dialect):
    # stress is not asserted: no source gives it
    out = ipa(dialect, "yêuga").replace("ˈ", "")
    assert out == "ʝeuɣɐ"


# item 6 ----------------------------------------------------------------------

def test_initial_l_is_l_in_a_loan(dialect):
    # p. 188: l is "Como em português na palavra lapa"; tr is t + tap (p. 191)
    assert ipa(dialect, "litro") == "ˈlitɾu"


def test_initial_l_before_nasal_vowel(dialect):
    # p. 188 "lĩ-ndo": the l is [l] and the n is kept before the d
    assert ipa(dialect, "lindo") == "ˈlĩndu"


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
    ("envidar", "ɨ̃mbiˈðaɾ"),           # after a nasal: stop, with the kept nasal (p. 187); d between vowels: p. 188
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
    # p. 180 "drento", "pongo", with the nasal consonant kept (p. 188)
    assert ipa("mwl", "drento") == "ˈdɾẽntu"
    assert ipa("mwl", "pongo") == "ˈpõŋɡu"


def test_new_rules_cite_ldv_with_a_page():
    spec = spec_json("mwl")
    rules = {r["id"]: r for r in spec["allophone_rules"]}
    sandhi = {r["id"]: r for r in spec["sandhi_rules"]}
    for rule in [*rules.values(), *sandhi.values()]:
        if rule["id"].startswith(("MWL_S_VOICING", "MWL_FINAL_S_VOICING", "MWL_FINAL_C_VOICING",
                                  "MWL_L_VELAR", "MWL_ARTICLE_L_VELAR")):
            assert "Vasconcellos" in rule["notes"] and "p. 1" in rule["notes"], rule["id"]


# ---------------------------------------------------------------------------
# The expected strings below are written from the LdV pages. Where the spec
# keeps a convention of its own (ɐ̃ for the nasal a, p. 180 and p. 201; [o], [e]
# and [u], [ɨ] for the unstressed vowels, p. 200), the comment says so.
# ---------------------------------------------------------------------------

# item 2 ----------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("ambos", f"ˈɐ̃mbu{S}"),         # p. 187 "ã-mbos"
    ("campo", "ˈkɐ̃mpu"),            # p. 187, m before p
    ("santo", f"ˈ{S}ɐ̃ntu"),         # p. 188 "sã-nto"
    ("lindo", "ˈlĩndu"),             # p. 188 "lĩ-ndo"
    ("mundo", "ˈmũndu"),             # p. 180 "mundo", p. 188 n before d
    ("pongo", "ˈpõŋɡu"),             # p. 188 "põ-ŋgo"
    ("cinco", "ˈsĩŋku"),             # p. 180 "cinco", p. 188 "mõ-ŋcas"
])
def test_the_nasal_consonant_is_kept_before_a_stop(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_the_nasal_consonant_is_kept_before_a_stop_after_a_lax_diphthong():
    # p. 187 "sĩẹ̌-mpre"
    assert ipa("mwl", "siempre") == nfc(f"ˈ{S}jɪ̃mpɾɨ")
    assert ipa("mwl-x-sendim", "siempre") == nfc(f"ˈ{S}ĩmpɾɨ")


@pytest.mark.parametrize("word, expected", [
    ("pan", "ˈpɐ̃"),                 # p. 257 "pane > pã"
    ("fin", "ˈfĩ"),                  # p. 257 "fine > fĩ"
    ("comun", "kuˈmũ"),              # p. 257 "commune > comũ"
])
def test_a_word_final_nasal_consonant_is_absorbed(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_a_nasal_before_a_fricative_is_still_absorbed():
    # No LdV example: pins that the kept nasal does not widen beyond the stops
    assert ipa("mwl", "honra") == "ˈõɾɐ"


# item 3 ----------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("buono", "ˈbʊnu"),                # p. 182 "bọ̌no"
    ("cuosta", f"ˈkʊ{S}tɐ"),           # p. 182 "cọ̌sta"
    ("fuogo", "ˈfʊɣu"),                # p. 182 "fọ̌go"
    ("puorta", "ˈpʊɾtɐ"),              # p. 226 "pọ̌rta"
    ("nuobo", "ˈnʊβu"),                # p. 226 "nọ̌bo"
    ("uolho", "ˈʊʎu"),                 # p. 226 "ọ̌lho"
    ("fuonte", "ˈfʊ̃ntɨ"),             # p. 180 "fọ̌nte"
    ("puôrta", "ˈpʊɾtɐ"),              # Convenção spelling of the same word
])
def test_uo_is_the_lax_vowel(word, expected):
    for dialect in ("mwl", "mwl-x-ifanes"):
        assert ipa(dialect, word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("buono", "ˈbunu"),                # p. 226 "buno"
    ("puorta", "ˈpuɾtɐ"),              # p. 226 "purta"
    ("uolho", "ˈuʎu"),                 # p. 226 "ulho"
    ("fuonte", "ˈfũntɨ"),              # p. 226 "funte"
])
def test_sendines_uo_is_u(word, expected):
    assert ipa("mwl-x-sendim", word) == nfc(expected)


# item 4 ----------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("tierra", "ˈtjɪrɐ"),              # p. 173 "tiẹ̌rra"
    ("tiêrra", "ˈtjɪrɐ"),              # Convenção spelling of the same word
    ("fierro", "ˈfjɪru"),              # p. 220 "fĩẹ̌rro"
    ("bien", "ˈbjɪ̃"),                  # p. 180 "bĩẹ̌̃"
    ("quien", "ˈkjɪ̃"),                 # p. 220 "quĩẹ̌̃"
    ("cien", "ˈsjɪ̃"),                  # p. 220 "cĩẹ̌̃"
])
def test_ie_is_the_lax_vowel(word, expected):
    for dialect in ("mwl", "mwl-x-ifanes"):
        assert ipa(dialect, word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("tierra", "ˈtirɐ"),               # p. 219 "firro"
    ("fierro", "ˈfiru"),               # p. 219 "firro"
    # p. 220 "bíẽ", stress on the i; the footnote reads the ẽ as ẹ̌̃ or ẽ̥ and
    # p. 185 Obs. 4 as ḙ̃ or ẽ̥, so the vowel both pages give is ẽ̥ [ɨ̃]
    ("bien", "ˈbiɨ̃"),
    ("quien", "ˈkiɨ̃"),                 # p. 220 "quíẽ", p. 185 "kíẽ̥"
    ("cien", f"ˈ{S[0]}iɨ̃"),            # p. 220 "cíẽ"
])
def test_sendines_ie_is_i(word, expected):
    assert ipa("mwl-x-sendim", word) == nfc(expected)


@pytest.mark.parametrize("text, expected", [
    # p. 220 Obs. 2: "quĩ foi, cĩ pessoas, bĩ feito", proclitic, with no accent
    ("bien feito", "bĩ ˈfejtu"),
    ("quien foi", "kĩ ˈfoj"),
])
def test_sendines_proclitic_ien_reduces_to_i_nasal(text, expected):
    assert ipa("mwl-x-sendim", text) == nfc(expected)


def test_sendines_proclitic_cien():
    # p. 220 Obs. 2 "cĩ pessoas"
    assert first_word("mwl-x-sendim", "cien pessonas") == "sĩ"


def test_sendines_ien_before_a_pause_is_not_proclitic():
    assert first_word("mwl-x-sendim", "bien, alto") == nfc("ˈbiɨ̃")


@pytest.mark.parametrize("dialect", ["mwl", "mwl-x-ifanes"])
def test_central_ien_is_not_reduced_before_a_word(dialect):
    # Obs. 2 is a Sendinês rule; central bien is bĩẹ̌̃ (p. 180)
    assert ipa(dialect, "bien feito") == nfc("ˈbjɪ̃ ˈfejtu")


# item 5 ----------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("pé", "ˈpe"),                     # §22 pp. 197-198: no Portuguese é
    ("pés", f"ˈpe{S}"),                # p. 197 "pés"
    ("pós", f"ˈpo{S}"),                # p. 197 "pós"
    ("dó", "ˈdo"),                     # p. 197 "dó"
    ("chapéu", "tʃɐˈpew"),             # p. 183 "chapeu"
])
def test_the_accented_e_and_o_are_the_spanish_mid_vowels(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("ber", "ˈbeɾ"),                   # p. 173 "ber"
    ("certo", "ˈseɾtu"),               # p. 173 "certo"
    ("probe", "ˈpɾoβɨ"),               # p. 174 "probe"; b between vowels: p. 187
])
def test_the_stressed_e_and_o_have_no_open_candidate(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)
    assert not any(c in "ɛɔ" for cand in G2P(dialect).word_candidates(word, k=10) for c in cand)


# item 8 ----------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("dedo", "ˈdeðu"),                 # p. 188 "ls dedos"
    ("tarde", "ˈtaɾðɨ"),               # p. 188 "tarde"
    ("berde", "ˈbeɾðɨ"),               # p. 188 "depois de ... r"
    ("cudiçoso", f"kuðiˈsoz̺u"),        # p. 188 "codiçoso"
])
def test_d_is_a_spirant_between_vowels_and_after_s_z_r(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("mundo", "ˈmũndu"),               # p. 188 "depois de nasal"
    ("caldo", "ˈkaɫdu"),               # p. 188 "depois de ... l"
    ("dou", "ˈdɵw"),                   # p. 188 "döu": initial d is a stop
])
def test_d_is_a_stop_after_a_nasal_or_l_and_at_the_start(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_initial_d_after_s_and_ç_is_a_spirant_across_words(dialect):
    # p. 188 "ls dedos", "lhuç dẹ̥l ci̊ẹ̌lo": dẹ̥l has the "e surdo" [ɨ] and no stress
    assert ipa(dialect, "ls dedos").split(" ")[1] == "ˈðeðu" + S
    assert ipa(dialect, "lhuç del cielo").split(" ")[1] == "ðɨɫ"


@pytest.mark.parametrize("text, expected", [
    ("la bida", "lɐ ˈβiðɐ"),           # p. 187: the initial stop only "depois de pausa ou de nasal"
    ("de dous", f"dɨ ˈðɵw{S}"),        # p. 188: the initial stop only "depois de pausa, de nasal e de l"
])
def test_initial_b_and_d_after_a_vowel_are_spirants_across_words(dialect, text, expected):
    assert ipa(dialect, text) == nfc(expected)


@pytest.mark.parametrize("text, expected", [
    ("un bino", "ˈũ ˈbinu"),           # p. 187 "depois de ... nasal"
    ("un dedo", "ˈũ ˈdeðu"),           # p. 188 "depois de ... nasal"
    ("la gata", "lɐ ˈɡatɐ"),           # p. 192 gives g as "Medial e inicial" with no context
])
def test_initial_stops_after_a_nasal_and_g_after_a_vowel_stay_stops(dialect, text, expected):
    assert ipa(dialect, text) == nfc(expected)


def test_initial_b_after_a_pause_stays_a_stop(dialect):
    # p. 187 "depois de pausa"
    assert ipa(dialect, "casa, bida").split(" ")[1] == "ˈbiðɐ"


def test_initial_d_after_l_stays_a_stop_across_words(dialect):
    # p. 188 "depois de pausa, de nasal e de l"
    assert ipa(dialect, "el dedo").split(" ")[1] == "ˈdeðu"
    assert ipa(dialect, "un dedo").split(" ")[1] == "ˈdeðu"


# item 9 ----------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("silba", f"ˈ{S}iɫβɐ"),            # p. 187 "silƀa"
    ("orbelhaca", f"uɾβɨˈʎakɐ"),       # Convenção B "orbelhaca"
    ("servir", f"{S}ɨɾˈβiɾ"),          # §14 p. 193: v is b, so it is a spirant after r
    ("algo", "ˈaɫɣu"),                 # p. 192
    ("esgrimir", f"ɨ{Z}ɣɾiˈmiɾ"),      # p. 192, after s
])
def test_b_v_and_g_are_spirants_after_a_voiced_consonant(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_g_is_a_spirant_after_r_in_lhargo():
    # p. 192 "depois de s, l, r"; Sendinês has [l] for the initial lh (p. 259)
    assert ipa("mwl", "lhargo") == "ˈʎaɾɣu"
    assert ipa("mwl-x-ifanes", "lhargo") == "ˈʎaɾɣu"
    assert ipa("mwl-x-sendim", "lhargo") == "ˈlaɾɣu"


@pytest.mark.parametrize("word, expected", [
    ("ambos", f"ˈɐ̃mbu{S}"),            # p. 187 "depois de nasal"
    ("pongo", "ˈpõŋɡu"),               # Convenção G "depois de vogal nasal (pongo)"
    ("bibal", "biˈβaɫ"),               # initial b is a stop, the second is between vowels
])
def test_b_and_g_stay_stops_after_a_nasal_and_at_the_start(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_initial_b_and_g_are_spirants_after_s_and_l_across_words(dialect):
    # p. 187 "ls bọnos", p. 192 "depois de s, l, r"
    assert ipa(dialect, "ls buonos").split(" ")[1].startswith("ˈβ")
    assert ipa(dialect, "l gato") == "ɫ ˈɣatu"


# item 12 ---------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("touro", "ˈtɵwɾu"),               # p. 174 "töuro"
    ("tou", "ˈtɵw"),                   # p. 183 "töu"
    ("pouco", "ˈpɵwku"),               # p. 174 "öu"
])
def test_ou_has_the_base_vowel_o_umlaut(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_eu_is_unchanged(dialect):
    assert ipa(dialect, "seu") == nfc(f"ˈ{S}ew")   # p. 183 "chapeu"


# item 13 ---------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("son", f"ˈ{S}ɵ̃w̃"),                # p. 183 "söũ"
    ("coraçon", "kuɾɐˈsɵ̃w̃"),          # §110 p. 257, -ONE > -öũ
    ("perdigon", "pɨɾðiˈɣɵ̃w̃"),        # p. 257 "perdigöũ"
    ("lhion", "ˈʎjɵ̃w̃"),               # §110, -ONE after i
    ("non", "ˈno"),                    # §110 a, p. 257 "non > nó"
])
def test_final_on_is_the_nasal_diphthong(word, expected):
    for dialect in ("mwl", "mwl-x-ifanes"):
        assert ipa(dialect, word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("son", f"ˈ{S}ɐ̃w̃"),                # p. 257 note: "em sendinês ... -ão"
    ("coraçon", "kuɾɐˈsɐ̃w̃"),
])
def test_sendines_final_on_is_ao(word, expected):
    assert ipa("mwl-x-sendim", word) == nfc(expected)


def test_final_un_and_in_are_unchanged(dialect):
    assert ipa(dialect, "comun") == "kuˈmũ"        # p. 257 "comũ"


# item 16 ---------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("ũa", "ˈũŋɐ"),                    # p. 192 "ũŋa"
    ("algũa", "ɐɫˈɣũŋɐ"),              # p. 180 "algũ", p. 192
])
def test_a_velar_nasal_stands_between_a_nasal_vowel_and_a_vowel(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


def test_the_velar_nasal_is_inserted_across_words():
    # p. 192 "bĩẹ̌̃ ŋ alto"
    assert ipa("mwl", "bien alto") == nfc("ˈbjɪ̃ ˈŋaɫtu")
    assert ipa("mwl-x-sendim", "bien alto") == nfc("bĩ ˈŋaɫtu")


def test_the_velar_nasal_is_not_inserted_before_a_consonant_or_a_pause():
    assert ipa("mwl", "bien dito").split(" ")[1].startswith("ˈd")
    # p. 192, footnote 1: doubtful before a pause
    assert ipa("mwl", "bien, alto").split(" ")[1] == "ˈaɫtu"


# item 17 ---------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("you", "ˈʝɵw"),                   # p. 191 "yöu"
    ("yá", "ˈʝa"),
    ("yêrba", "ˈʝeɾβɐ"),
])
def test_y_is_the_spanish_palatal(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("rey", "ˈrej"),                   # p. 191 y is "Inicial ou medial", so a final y is the glide
])
def test_final_y_is_the_glide(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


# item 18 ---------------------------------------------------------------------

# ì = [ɪ] (p. 174), ù = [ʊ] (p. 177), ệ = [ə] (p. 178)
@pytest.mark.parametrize("word, expected", [
    ("tie", "ˈtɪə"),                   # p. 185 "tìệ"
    ("die", "ˈdɪə"),                   # p. 225 "dìệ"
    ("mie", "ˈmɪə"),                   # p. 174 "mìệ"
    ("frie", "ˈfɾɪə"),                 # p. 225 "frìệ"
    ("tue", "ˈtʊə"),                   # p. 185 "tùệ"
    ("sue", f"ˈ{S}ʊə"),                # p. 177 "sùệ"
    ("rue", "ˈrʊə"),                   # p. 232 "rùệ"
])
def test_final_ie_and_ue_are_two_syllables(word, expected):
    for dialect in ("mwl", "mwl-x-ifanes"):
        assert ipa(dialect, word) == nfc(expected)


def test_pie_is_one_syllable_with_the_diphthong():
    # p. 219: pĕde > "pi̊ẹ̌" in central Mirandese, "pi" in Sendinês
    for dialect in ("mwl", "mwl-x-ifanes"):
        assert ipa(dialect, "pie") == "ˈpjɪ"
    assert ipa("mwl-x-sendim", "pie") == "ˈpi"


@pytest.mark.parametrize("word, expected", [
    ("tue", "ˈtʊə"),                   # p. 185 "tùệ"; LdV gives no Sendinês form
    ("sue", f"ˈ{S}ʊə"),                # p. 177 "sùệ"
    ("rue", "ˈru"),                    # p. 232 "e em send. ru"
])
def test_sendines_final_ue(word, expected):
    assert ipa("mwl-x-sendim", word) == nfc(expected)


# the stress is on the i; the vowels before it are pretonic and reduce (p. 200:
# atonic a [ɐ], e [ɨ], o and u [u]), exactly as in fazer [fɐˈzeɾ]
@pytest.mark.parametrize("word, expected", [
    ("fazie", "fɐˈzɪə"),               # p. 185 "fazie"
    ("pudie", "puˈðɪə"),               # p. 185 "pudie"; d between vowels, p. 188
    ("tenie", "tɨˈnɪə"),               # p. 185 "tenie"
    ("comie", "kuˈmɪə"),
    ("habie", "ɐˈβɪə"),                # b between vowels, p. 187
    ("sabie", f"{S}ɐˈβɪə"),
    ("Marie", "mɐˈɾɪə"),               # Convenção 2.1.2.1 "Marie, die, não são acentuadas"
])
def test_a_longer_word_in_ie_has_the_stress_on_the_i(word, expected):
    for dialect in ("mwl", "mwl-x-ifanes"):
        assert ipa(dialect, word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("fazie", "fɐˈzi"),                # p. 225 "ti": the i keeps the stress
    ("tenie", "tɨˈni"),
])
def test_sendines_longer_word_in_ie_has_the_stress_on_the_i(word, expected):
    assert ipa("mwl-x-sendim", word) == nfc(expected)


@pytest.mark.parametrize("word, stressed", [
    ("série", f"ˈ{S}eɾ"),              # é = [e], p. 198
    ("superfície", f"{S}upɨɾˈfis"),
    ("cárie", "ˈkaɾ"),
])
def test_a_written_accent_keeps_the_stress_before_final_ie(dialect, word, stressed):
    out = ipa(dialect, word)
    assert out.startswith(nfc(stressed)) and out.count("ˈ") == 1


@pytest.mark.parametrize("word, expected", [
    ("tie", "ˈti"),                    # p. 225 "em sendinês ti"
    ("frie", "ˈfɾi"),                  # p. 225 "em sendinês fri"
    ("die", "ˈdi"),                    # p. 225 "dìệ e di"
])
def test_sendines_final_ie_is_i(word, expected):
    assert ipa("mwl-x-sendim", word) == nfc(expected)


def test_qu_e_is_not_a_final_ue(dialect):
    assert ipa(dialect, "que") == "kɨ"


# final unstressed -uo: ọ̌ is only tonic (p. 177), atonic u and o are [u] (p. 200)
@pytest.mark.parametrize("word, expected", [
    ("mútuo", "ˈmutuu"),
    ("indibíduo", "ĩndiˈβiðuu"),       # nasal + stop kept, p. 188; b and d between vowels
])
def test_final_unstressed_uo_keeps_its_syllable(dialect, word, expected):
    assert ipa(dialect, word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("buono", "ˈbʊnu"),                # p. 182 Obs. 2, tonic ọ̌
    ("fuonte", "ˈfʊ̃ntɨ"),              # p. 180 "fọ̌nte"
])
def test_stressed_uo_is_still_the_lax_vowel(word, expected):
    for dialect in ("mwl", "mwl-x-ifanes"):
        assert ipa(dialect, word) == nfc(expected)


# item 19 ---------------------------------------------------------------------

@pytest.mark.parametrize("word, expected", [
    ("uolho", "ˈuʎu"),                 # p. 226 "ulho"
    ("filho", "ˈfiʎu"),                # p. 191, medial lh
    ("lhado", "ˈlaðu"),                # p. 259 "lado"
])
def test_sendines_medial_lh_is_kept_and_the_initial_one_is_l(word, expected):
    assert ipa("mwl-x-sendim", word) == nfc(expected)


# the spec notes quote LdV with a page and the modern source that disagrees ----

@pytest.mark.parametrize("fragment", [
    # LdV, with the page in the same sentence or the one before it
    "Como o y castelhano normal em yo",
    "Não deve differir muito do i das palavras inglesas fill, fit, little",
    "Muito semelhante ao u do inglês full, butcher",
    "O ditongo ùọ̌ não é normal na falla mirandesa",
    "não existem na pronúncia normal mirandesa",
    "ã-mbos", "põ-ŋgo",
    "Intervocalico, e depois de s, ç (ʒ) e r",
    "no meio, depois de nasal ou de consoante que não seja s, ʒ ou r",
    "entre o i do port. viu (na pronúncia de Lisboa) e o ê do port. cêrca",
    "pĕde > \"pi̊ẹ̌\"",
    "A raia sêcca mirandesa é constituida pelas seguintes aldeias: Paradella, Ifanez, Constantim, Cicouro e S. Martinho de Angueira",
    "não são ditongos propriamente ditos, mas verdadeiros dissyllabos",
    # the modern sources, quoted
    "a semivogal anterior [j] (por vezes levemente fricatizada)",
    "Muitas vezes, na fala de algumas localidades, estes ditongos reduzem-se à vogal média [o] ou nasal [õ]",
    "dos ditongos uô e uôn (puôrta, fuônte)",
    "O ditongo [je] escreve-se yê na 3ª pessoa do singular do presente do indicativo do verbo ser e em palavras como yêrba, yêrbo, yêuga.",
    "sendo o aparecimento de [wo] menos frequente que o de [je]",
    "noutras, como Duas Igrejas e Constantim, [wo] é esporádico",
    "contextual intervocalic velar nasal [ŋ] after a stressed nasal /u/ preceding a vowel",
    "onde u nasal é seguido de a, quer em hiato quer com uma transição nasal velar",
    "marca também a qualidade relativamente aberta das vogais a, e e o (yá, sés, nó)",
    "Quando representa [ɔ] aberto em sílaba tónica de palavras agudas e esdrúxulas, recebe acento agudo (abó, bóbida)",
    "indica a nasalidade da vogal em fim de vocábulo (lhion)",
    "quer hiato [ie] (Duas Igrejas), quer ditongo [je] (Malhadas), quer monotongação em [e] (Ifanes), quer monotongação em [i] (Sendim)",
    "Ferreira et al. (2014, §3.4) list je, jen, wo and won",
    "The gold alone is not a citation",
])
def test_the_mwl_notes_quote_both_sides_of_each_disagreement(fragment):
    spec = spec_json("mwl")
    haystack = " ".join([spec["notes"], *(r["notes"] for r in spec["allophone_rules"]),
                         *(r["notes"] for r in spec["sandhi_rules"])])
    assert fragment in haystack


def all_notes(code: str) -> str:
    spec = spec_json(code)
    return " ".join([spec["notes"], spec["stress"]["notes"],
                     *(r["notes"] for r in spec.get("allophone_rules", [])),
                     *(r["notes"] for r in spec.get("sandhi_rules", []))])


@pytest.mark.parametrize("code", DIALECTS)
@pytest.mark.parametrize("fragment", [
    # misquotes of the page images
    "o é do port. cérca", "s, ç ou r", "ç (z)", "\"os ditongos uô", "O ditongo [je] escreve-se yê\"",
    # edit history in the notes
    "run after", "moved to LdV", "lost their open candidate",
    # a self-contradicting disagreement
    "so it agrees",
])
def test_the_notes_have_no_misquote_or_edit_history(code, fragment):
    assert fragment not in all_notes(code)


def test_malhadas_is_a_named_locality_in_mwl_and_not_in_ifanes():
    # LdV vol. II, p. 28: Malhadas is not one of the raia sêcca villages
    assert "Malhadas" not in spec_json("mwl-x-ifanes")["notes"]
    assert "Disagreement, named locality: Malhadas" in spec_json("mwl")["notes"]


@pytest.mark.parametrize("rule_id", [
    "AST_NASAL_ABSORB", "MWL_NASAL_ABSORB_FINAL", "MWL_SPIRANT_D",
    "MWL_SPIRANT_B_AFTER_CONSONANT", "MWL_SPIRANT_G", "MWL_NASAL_DIPHTHONG_JI",
    "MWL_NASAL_DIPHTHONG_JE", "MWL_NASAL_U_LAX", "MWL_NASAL_DIPHTHONG_WO",
])
def test_each_new_allophone_rule_cites_ldv_with_a_page(rule_id):
    notes = mwl_rules()[rule_id]["notes"]
    assert "Vasconcellos" in notes and ("p. 1" in notes or "p. 2" in notes)


def test_the_sendines_notes_cite_the_aditamento_disagreement_and_the_page():
    notes = spec_json("mwl-x-sendim")["notes"]
    assert "p. 226" in notes and "p. 259" in notes and "p. 220" in notes
    assert "Disagreement" in notes


def test_the_ifanes_notes_quote_the_convencao_footnote():
    notes = spec_json("mwl-x-ifanes")["notes"]
    assert "verifica-se a redução de [je] para [e]" in notes
    assert "não offerece differenças phoneticas em relação á do centro" in notes


def test_ifanes_keeps_the_central_values():
    # LdV vol. II: the raiano speech has no phonetic difference from the centre
    for word in ("tierra", "buono", "bien", "fuonte", "pé", "ũa"):
        assert ipa("mwl-x-ifanes", word) == ipa("mwl", word)


# the second candidates admitted by the 0-in-top-k test ------------------------

@pytest.mark.parametrize("word, modern", [
    ("buono", "bwonu"), ("puôrta", "pwoɾtɐ"), ("fuonte", "fwõntɨ"),
    ("tierra", "tjerɐ"), ("bien", "bjẽ"),
    ("pé", "pɛ"), ("pós", f"pɔ{S}"),
    ("you", "jɵw"), ("son", f"{S}õ"),
])
def test_the_modern_reading_is_a_lower_candidate(word, modern):
    candidates = [nfc(c).replace("ˈ", "") for c in G2P("mwl").word_candidates(word, k=10)]
    assert candidates[0] != nfc(modern)
    assert nfc(modern) in candidates
