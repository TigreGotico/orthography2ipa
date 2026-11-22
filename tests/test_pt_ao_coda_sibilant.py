"""Angolan Portuguese writes a coda sibilant as in pt-PT: [ʃ], or [ʒ] before a
voiced consonant.

Undolo (2014, printed p.212) prints the Angolan reading desgosto [deʒ'gɔʃtu]
(European [dɨʒ'goʃtu]) and, in the glossary (printed p.253), infeliz
[ĩfe'liʃ]. The Portal da Língua Portuguesa Dicionário fonético, Luanda (region
lda), writes existir e.ziʃ.tˈiɾ. The Portal is the output of a rule-based
generator, so it only agrees with the thesis here and is no second source.
pt-MZ and pt-TL keep the alveolar [s]: no source read for Maputo gives the coda
sibilant, and Albuquerque (2010, p.277) gives escola [is.ˈkɔ.la] ~ [iʃ.kɔ.la]
for East Timor.
"""
import pytest

from orthography2ipa import get, transcribe

#: word, the part of the reading that the source prints for the coda sibilant.
SOURCE = [
    ("desgosto", "eʒˈɡɔʃt"),   # Undolo 2014, printed p.212: [deʒ'gɔʃtu]
    ("infeliz", "liʃ"),         # Undolo 2014, printed p.253: [ĩfe'liʃ]
    ("existir", "ziʃˈtiɾ"),     # Portal, lda: e.ziʃ.tˈiɾ
]


@pytest.mark.parametrize("word, part", SOURCE)
def test_pt_ao_reads_the_sibilant_the_sources_print(word, part):
    assert part in transcribe(word, "pt-AO")


@pytest.mark.parametrize("word", ["festa", "mosca", "três", "pratos", "os livros"])
def test_pt_ao_has_no_alveolar_coda(word):
    out = transcribe(word, "pt-AO")
    assert "s" not in out, out
    assert "ʃ" in out, out


@pytest.mark.parametrize("word", ["festa", "livros", "três"])
@pytest.mark.parametrize("lang", ["pt-MZ", "pt-TL"])
def test_pt_mz_and_pt_tl_keep_the_alveolar_coda(lang, word):
    out = transcribe(word, lang)
    assert "s" in out and "ʃ" not in out, out


def test_pt_ao_takes_the_pt_pt_coda_rules_unchanged():
    ao = {r.id: r for r in get("pt-AO").allophone_rules}
    pt = {r.id: r for r in get("pt-PT").allophone_rules}
    for rule_id in ("PT_CODA_S_HUSH", "PT_CODA_Z_HUSH",
                    "PT_CODA_S_VOICING_INTERNAL", "PT_CODA_S_BEFORE_ZH_INTERNAL"):
        assert ao[rule_id].surface == pt[rule_id].surface, rule_id
