"""⟨e⟩ before ⟨x⟩ and a consonant takes the diphthong of that spec's ⟨ei⟩.

pt-PT writes ⟨ei⟩ as [ej], so texto is [ˈtejʃtu] and explicar [ejʃpliˈkaɾ]. Lisbon writes
⟨ei⟩ as [ɐj], so texto is [ˈtɐjʃtu] in every position. The ⟨ei⟩ value is the project ruling
that [ɐj] is Lisbon and [ej] is standard pt-PT, and that a dictionary reading such as
Infopédia's does not settle the pt-PT norm. Infopédia (Porto Editora) carries the glide in
542 of its 549 ⟨ex⟩ + consonant headwords, with its Lisbon vowel: texto [ˈtɐjʃtu].

Cruz-Ferreira (1999, Handbook of the IPA, p. 128): "In some words the offglide has been
altogether lost, as in the pronunciation of the word /pɐiʃɯ/ peixe 'fish (n)' as [pɐʃ]." The
Lisbon rows of the Portal da Língua Portuguesa are LUPo generator output and the human
clup_dialect gold has a bare [ʃ] for some initial ⟨ex⟩, so neither fixes the Lisbon value.
"""
import pytest

from orthography2ipa import G2P, transcribe

PT_PT = [
    ("texto", "ˈtejʃtu"),
    ("contexto", "kõˈtejʃtu"),
    ("pretexto", "pɾɨˈtejʃtu"),
    ("sexta", "ˈsejʃtɐ"),
    ("extra", "ˈejʃtɾɐ"),
    ("explicar", "ejʃpliˈkaɾ"),
    ("excelente", "ejʃsɨˈlẽtɨ"),
    ("exterior", "ejʃtɨɾiˈoɾ"),
]
LISBON = [
    ("texto", "ˈtɐjʃtu"),
    ("contexto", "kõˈtɐjʃtu"),
    ("pretexto", "pɾɨˈtɐjʃtu"),
    ("sexta", "ˈsɐjʃtɐ"),
    ("extra", "ˈɐjʃtɾɐ"),
    ("explicar", "ɐjʃpliˈkaɾ"),
    ("excelente", "ɐjʃsɨˈlẽtɨ"),
    ("exterior", "ɐjʃtɨɾiˈoɾ"),
]
EI_WORDS = ["deixar", "peixe", "primeiro"]
EX_WORDS = [word for word, _ in PT_PT] + ["textura", "exportar", "experiência"]


@pytest.mark.parametrize("word, ipa", PT_PT)
def test_pt_pt_ex_consonant_is_ej(word, ipa):
    assert transcribe(word, "pt-PT") == ipa


@pytest.mark.parametrize("lang", [
    "pt-PT-x-coimbra", "pt-PT-x-alfena", "pt-PT-x-minho", "pt-PT-x-tras-os-montes",
    "pt-PT-x-viana"])
@pytest.mark.parametrize("word, ipa", PT_PT)
def test_varieties_with_ei_ej_inherit_the_rule(lang, word, ipa):
    assert transcribe(word, lang).replace("\u033a", "") == ipa


@pytest.mark.parametrize("word, ipa", LISBON)
def test_lisbon_ex_consonant_is_aj_in_every_position(word, ipa):
    assert transcribe(word, "pt-PT-x-lisbon") == ipa


@pytest.mark.parametrize("lang, diphthong", [
    ("pt-PT", "ej"), ("pt-PT-x-coimbra", "ej"), ("pt-PT-x-lisbon", "ɐj")])
def test_ex_takes_the_diphthong_of_ei(lang, diphthong):
    for word in EI_WORDS:
        assert diphthong in transcribe(word, lang)
    for word in EX_WORDS:
        assert diphthong + "ʃ" in transcribe(word, lang)


# ⟨x⟩ before a vowel, word-final ⟨x⟩ and ⟨exh⟩, ⟨exy⟩ take no glide. Infopédia reads some of
# them [z] or [ks], so only the glide is asserted absent, not the whole string.
NO_GLIDE = ["exame", "exato", "exemplo", "exalar", "exhalar", "duplex", "luxo", "táxi", "sexy"]


@pytest.mark.parametrize("lang", ["pt-PT", "pt-PT-x-coimbra", "pt-PT-x-lisbon"])
@pytest.mark.parametrize("word", NO_GLIDE)
def test_x_without_a_pronounced_consonant_after_it_takes_no_glide(lang, word):
    assert "j" not in transcribe(word, lang)


def test_the_reduced_candidate_survives_in_the_e_slot():
    slot = G2P("pt-PT").ipa_lattice("explicar")[0]
    assert [c.ipa for c in slot.candidates] == ["ej", "i", "ej", "ej"]
    assert "iʃpliˈkaɾ" in G2P("pt-PT").word_candidates("explicar", k=8)


# One disabled spec per family (African, Asian, creole, regional dialect), and the specs whose own ⟨e⟩ reading the rule would replace.
DISABLED = [
    ("pt-AO", "texto", "ˈtɛʃtʊ"),
    ("pt-MZ", "explicar", "eʃpliˈkaɾ"),
    ("pt-TL", "texto", "ˈtɛʃto"),
    ("pt-MO", "texto", "ˈtɛʃtu"),
    ("kea", "texto", "ˈteʃto"),
    ("pt-PT-x-acores", "explicar", "eʃpliˈkaɾ"),
    ("pt-PT-x-terceira", "explicar", "eʃpliˈkaɾ"),
    ("pt-PT-x-algarve", "texto", "ˈtɛʃtu"),
    ("pt-PT-x-aveiro", "explicar", "eʃpliˈkaɾ"),
    ("pt-PT-x-porto", "texto", "ˈtjɛʃtu"),
    ("pt-PT-x-porto", "explicar", "eʃpliˈkaɾ"),
    ("pt-PT-x-braga", "texto", "ˈtjɛʃtu"),
    ("pt-PT-x-braga", "explicar", "eʃpliˈkaɾ"),
    ("ext-PT-x-barranco", "explicar", "eʃˈplikɐ"),
]


@pytest.mark.parametrize("lang, word, ipa", DISABLED)
def test_disabled_varieties_keep_their_reading(lang, word, ipa):
    assert transcribe(word, lang) == ipa
