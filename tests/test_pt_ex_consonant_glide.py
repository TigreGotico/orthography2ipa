"""European Portuguese ⟨e⟩ + ⟨x⟩ + consonant takes the palatal glide: [ɐjʃ].

The evidence is the Infopédia (Porto Editora) pt-PT transcription of each word.
Lisbon keeps the glide in word-initial ⟨ex⟩ only. Its medial reading is the
Lisbon dictionary of the Portal da Língua Portuguesa (tugalex lbx data):
texto tˈɐʃ·tu, contexto kõ·tˈɐʃ·tu, pretexto pɾɨ·tˈɐʃ·tu, sexta sˈɐʃ·tɐ; its
initial reading is explicar ɐjʃ·pli·kˈaɾ, excelente ɐjʃ·sɨ·lˈẽt and exterior
ɐjʃ·tɨ·ɾjˈoɾ.

Each expected form is the Infopédia string with its notation folded to the
spec's: [r] -> [ɾ], [ə] -> [ɨ], and the [rj] of exterior written [ɾi].
"""
import pytest

from orthography2ipa import transcribe

INFOPEDIA_PT = [
    ("texto", "ˈtɐjʃtu"),
    ("contexto", "kõˈtɐjʃtu"),
    ("pretexto", "pɾɨˈtɐjʃtu"),
    ("sexta", "ˈsɐjʃtɐ"),
    ("extra", "ˈɐjʃtɾɐ"),
    ("explicar", "ɐjʃpliˈkaɾ"),
    ("excelente", "ɐjʃsɨˈlẽtɨ"),
    ("exterior", "ɐjʃtɨɾiˈoɾ"),
]

LISBON_INITIAL = ["explicar", "excelente", "exterior"]
LISBON_MEDIAL = [
    ("texto", "ˈtɐʃtu"),
    ("contexto", "kõˈtɐʃtu"),
    ("pretexto", "pɾɨˈtɐʃtu"),
    ("sexta", "ˈsɐʃtɐ"),
]


@pytest.mark.parametrize("word, ipa", INFOPEDIA_PT)
def test_pt_pt_ex_consonant_has_the_glide(word, ipa):
    assert transcribe(word, "pt-PT") == ipa


@pytest.mark.parametrize("word, ipa", INFOPEDIA_PT)
def test_pt_pt_dialects_without_their_own_vowel_inherit_it(word, ipa):
    assert transcribe(word, "pt-PT-x-coimbra") == ipa


@pytest.mark.parametrize("word, ipa", LISBON_MEDIAL)
def test_lisbon_medial_ex_has_no_glide(word, ipa):
    assert transcribe(word, "pt-PT-x-lisbon") == ipa


@pytest.mark.parametrize("word", LISBON_INITIAL)
def test_lisbon_initial_ex_agrees_with_pt_pt(word):
    ipa = dict(INFOPEDIA_PT)[word]
    assert transcribe(word, "pt-PT-x-lisbon") == ipa


# The glide needs a consonant after ⟨x⟩. These readings are the ones the spec
# gave before the rule, and the rule leaves them as they were.
UNCHANGED = [
    ("pt-PT", "exame", "eˈʃɐmɨ"),
    ("pt-PT", "exato", "eˈʃatu"),
    ("pt-PT", "exemplo", "eˈʃẽplu"),
    ("pt-PT", "exalar", "eʃɐˈlaɾ"),
    ("pt-PT", "duplex", "duˈplɛʃ"),
    ("pt-PT", "luxo", "ˈluʃu"),
    ("pt-PT", "táxi", "ˈtaʃi"),
    ("pt-PT-x-lisbon", "exame", "ɐˈʃɐmɨ"),
    ("pt-PT-x-lisbon", "exato", "ɐˈʃatu"),
    ("pt-PT-x-lisbon", "exemplo", "ɐˈʃẽplu"),
    ("pt-PT-x-lisbon", "exalar", "ɐʃɐˈlaɾ"),
    ("pt-PT-x-lisbon", "duplex", "duˈplɐʃ"),
    ("pt-PT-x-lisbon", "luxo", "ˈluʃu"),
    ("pt-PT-x-lisbon", "táxi", "ˈtaʃi"),
]


@pytest.mark.parametrize("lang, word, ipa", UNCHANGED)
def test_x_without_a_following_consonant_is_unchanged(lang, word, ipa):
    assert transcribe(word, lang) == ipa


@pytest.mark.parametrize("lang, word, ipa", [
    ("pt-AO", "texto", "ˈtɛʃtʊ"),
    ("pt-PT-x-porto", "texto", "ˈtjɛʃtu"),
    ("pt-PT-x-braga", "texto", "ˈtjɛʃtu"),
    ("pt-PT-x-terceira", "explicar", "eʃpliˈkaɾ"),
    ("pt-PT-x-algarve", "texto", "ˈtɛʃtu"),
    ("pt-PT-x-aveiro", "explicar", "eʃpliˈkaɾ"),
    ("pt-PT-x-minho", "texto", "ˈtɛʃtu"),
    ("ext-PT-x-barranco", "explicar", "eʃˈplikɐ"),
    ("kea", "texto", "ˈteʃto"),
])
def test_varieties_without_a_source_keep_their_reading(lang, word, ipa):
    assert transcribe(word, lang) == ipa
