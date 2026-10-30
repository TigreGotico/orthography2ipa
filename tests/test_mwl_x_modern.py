"""mwl-x-modern: the readings of the Convenção Ortográfica da Língua
Mirandesa (1999) and Ferreira et al. (SLTU 2014) where they disagree with
Leite de Vasconcellos (Estudos de Philologia Mirandesa I, 1900).

Every expected string is written by hand from the Convenção examples (page
numbers are those of the PDF) or from the phone set of Ferreira et al. §3.4.
Where the source gives no value, the spec keeps the LdV value of mwl, and a
test says so.
"""
import json
import unicodedata
from pathlib import Path

import pytest

from orthography2ipa import G2P

S = "s̺"
DATA = Path(__file__).resolve().parent.parent / "orthography2ipa" / "data"


def nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def modern(text: str) -> str:
    return nfc(G2P("mwl-x-modern").transcribe(text))


def spec_json(code: str) -> dict:
    return json.loads((DATA / f"{code}.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("word, expected", [
    ("buono", "ˈbwonu"),             # Convenção O: "uô e uôn (puôrta, fuônte)"
    ("puôrta", "ˈpwoɾtɐ"),
    ("fuonte", "ˈfwõntɨ"),           # nasal [wõ] (Ferreira et al. "won")
])
def test_uo_is_the_diphthong_wo(word, expected):
    assert modern(word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("tierra", "ˈtjerɐ"),            # Convenção, Grafia dos ditongos: "tiêrra" [je]
    ("tiêrra", "ˈtjerɐ"),
    ("bien", "ˈbjẽ"),                # Ferreira et al. "jen"
    ("quien", "ˈkjẽ"),
    ("siempre", f"ˈ{S}jẽmpɾɨ"),
])
def test_ie_is_the_diphthong_je(word, expected):
    assert modern(word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("pé", "ˈpɛ"),                   # Convenção, Acento: the acute marks "qualidade relativamente aberta"
    ("sés", f"ˈ{S}ɛ{S}"),            # "(yá, sés, nó)"
    ("nó", "ˈnɔ"),
    ("abó", "ɐˈβɔ"),                 # Convenção O: "[ɔ] aberto ... (abó, bóbida)"
    ("chapéu", "tʃɐˈpɛw"),           # Convenção, diphthong éu: "chapéu, piléu"
])
def test_the_accented_e_and_o_are_open(word, expected):
    assert modern(word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("yá", "ˈja"),                   # Convenção Y: "yê, you, yá, yêuga, yêrba e yêrbo"
    ("yê", "ˈje"),
    ("yêrba", "ˈjeɾβɐ"),
])
def test_y_is_the_glide(word, expected):
    assert modern(word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("son", f"ˈ{S}õ"),               # Convenção N: "indica a nasalidade da vogal em fim de vocábulo"
    ("coraçon", "kuɾɐˈsõ"),          # Convenção, Nasalidade: "(coraçon, melon, freijon)"
    ("melon", "mɨˈlõ"),
    ("freijon", "fɾejˈʒõ"),
    ("lhion", "ˈʎjõ"),               # Convenção N: "(lhion)"
])
def test_final_on_is_the_nasal_vowel(word, expected):
    assert modern(word) == nfc(expected)


@pytest.mark.parametrize("word, expected", [
    ("era", "ˈeɾɐ"),                 # no accent: the Convenção does not open the vowel
    ("ber", "ˈbeɾ"),
    ("probe", "ˈpɾoβɨ"),
])
def test_the_plain_e_and_o_stay_mid(word, expected):
    assert modern(word) == nfc(expected)


@pytest.mark.parametrize("word", [
    "ambos", "santo", "pongo", "lindo", "dedo", "tarde", "berde", "silba",
    "orbelhaca", "touro", "pouco", "pan",
    "ũa", "tie", "fazie", "lhargo",
])
def test_every_other_value_is_the_one_of_mwl(word):
    # no later source gives a different value, or none states it: the nasal
    # consonant before a stop (no source says it is absent), d and b (the
    # Convenção agrees with LdV), ou, the final -ie, the velar nasal
    assert modern(word) == nfc(G2P("mwl").transcribe(word))


def test_the_nasal_consonant_is_kept_before_a_stop():
    assert modern("santo") == nfc(f"ˈ{S}ɐ̃ntu")
    assert modern("pongo") == "ˈpõŋɡu"


def test_the_velar_nasal_stands_between_a_nasal_vowel_and_a_vowel():
    assert modern("bien alto") == nfc("ˈbjẽ ˈŋaɫtu")


def test_the_lax_readings_stay_as_second_candidates():
    candidates = {w: [nfc(c).replace("ˈ", "") for c in G2P("mwl-x-modern").word_candidates(w, k=10)]
                  for w in ("buono", "tierra", "pé", "you")}
    assert "bʊnu" in candidates["buono"]
    assert "tjɪrɐ" in candidates["tierra"]
    assert "pe" in candidates["pé"]
    assert "ʝɵw" in candidates["you"]


def test_only_the_disagreement_rows_are_overridden():
    spec = spec_json("mwl-x-modern")
    assert set(spec["graphemes"]) == {"y", "ie", "iê", "uo", "uô", "é", "ó", "éu"}
    assert set(spec["grammatical_endings"]) == {"on", "ion"}
    assert set(spec["word_exceptions"]) == {"quien"}
    assert "allophone_rules" not in spec and "sandhi_rules" not in spec
    assert spec["parent"] == "mwl"


@pytest.mark.parametrize("fragment", [
    "os ditongos uô e uôn (puôrta, fuônte)",
    "Muitas vezes, na fala de algumas localidades, estes ditongos reduzem-se à vogal média [o] ou nasal [õ]",
    "O ditongo [je] escreve-se yê",
    "marca também a qualidade relativamente aberta das vogais a, e e o (yá, sés, nó)",
    "Quando representa [ɔ] aberto em sílaba tónica de palavras agudas e esdrúxulas, recebe acento agudo (abó, bóbida)",
    "a semivogal anterior [j] (por vezes levemente fricatizada) nos vocábulos yê, you, yá, yêuga, yêrba e yêrbo",
    "indica a nasalidade da vogal em fim de vocábulo (lhion)",
    "Em fim de palavra adopta-se a escrita Vogal + n (coraçon, melon, freijon)",
    "Ferreira et al. (2014, §3.4) list wo and won",
    "Ferreira et al. (2014, §3.4) list je and jen",
    "no modern source says that the consonant is absent",
    "uma fricativa se está, por exemplo, entre vogais (bida) ou depois de r (berde)",
])
def test_each_override_quotes_its_source(fragment):
    assert fragment in spec_json("mwl-x-modern")["notes"]
