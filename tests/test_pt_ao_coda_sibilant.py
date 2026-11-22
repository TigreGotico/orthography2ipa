"""Angolan Portuguese writes a coda sibilant as [ʃ], or [ʒ] before a voiced
consonant, and a glide [j] before a following [s].

Undolo (2014, thesis, §4.1.2.2, printed pp.216-217) treats the PA coda as the
palatal [ʃ]. It prints PA [krej'sɛr] and [dekrej'sɛr] (PE [krɨʃ'ser]) for a
coda before [s], and a second variant, PA [kreʃ'ɛr], without a preference.
The article (Undolo 2014, Revista de Filología Románica, p.184) prints desgosto
PA [deʒ'gɔʃtu]. The Portal da Língua Portuguesa Dicionário fonético, Luanda
(region lda), writes existir e.ziʃ.tˈiɾ. The Portal is the output of a
rule-based generator, so it only agrees with the sources here.
"""
import pytest

from orthography2ipa import get, transcribe

#: word, and the part of the reading that a printed form fixes. The vowel after
#: the coda and the rhotic follow the spec's own maps, not the printed symbols.
PRINTED = [
    ("desgosto", "eʒˈɡɔʃt"),    # article p.184: [deʒ'gɔʃtu]
    ("crescer", "ejˈsɛɾ"),      # thesis p.216: [krej'sɛr]
    ("decrescer", "ejˈsɛɾ"),    # thesis p.216: [dekrej'sɛr]
    ("existir", "ziʃˈtiɾ"),     # Portal, lda: e.ziʃ.tˈiɾ
]


@pytest.mark.parametrize("word, part", PRINTED)
def test_pt_ao_reads_the_coda_the_sources_print(word, part):
    assert part in transcribe(word, "pt-AO")


@pytest.mark.parametrize("word", ["crescer", "decrescer", "nascer", "piscina",
                                  "descer", "adolescente", "consciência",
                                  "desça", "nasça", "fascismo"])
def test_pt_ao_writes_no_palatal_before_s(word):
    out = transcribe(word, "pt-AO")
    assert "ʃs" not in out and "ʃˈs" not in out, out
    assert "j" in out or "ʃ" in out, out


def test_pt_ao_keeps_a_coda_before_k_palatal():
    assert transcribe("escola", "pt-AO").startswith("eʃ")


@pytest.mark.parametrize("word", ["festa", "mosca", "três", "pratos", "os livros"])
def test_pt_ao_has_no_alveolar_coda(word):
    out = transcribe(word, "pt-AO")
    assert "s" not in out, out
    assert "ʃ" in out, out


@pytest.mark.parametrize("phrase", ["luz azul", "feliz amigo"])
def test_pt_ao_voices_a_final_sibilant_before_a_vowel(phrase):
    # pt-PT sandhi behaviour, with no Angolan check: [z] before a vowel.
    first = transcribe(phrase, "pt-AO").split(" ")[0]
    assert first.endswith("z"), first
    assert transcribe(phrase, "pt-PT").split(" ")[0].endswith("z")


@pytest.mark.parametrize("word", ["festa", "livros", "três"])
def test_pt_tl_keeps_the_alveolar_coda(word):
    # Albuquerque (2010, p.277): escola [is.ˈkɔ.la] ~ [iʃ.kɔ.la], [s] first.
    out = transcribe(word, "pt-TL")
    assert "s" in out and "ʃ" not in out, out


def test_pt_ao_takes_the_pt_pt_voicing_and_deletion_rules():
    ao = {r.id: r for r in get("pt-AO").allophone_rules}
    pt = {r.id: r for r in get("pt-PT").allophone_rules}
    for rule_id in ("PT_CODA_Z_HUSH", "PT_CODA_S_VOICING_INTERNAL",
                    "PT_CODA_S_BEFORE_ZH_INTERNAL"):
        assert ao[rule_id].surface == pt[rule_id].surface, rule_id
