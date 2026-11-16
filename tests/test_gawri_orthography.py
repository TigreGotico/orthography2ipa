"""The Gawri (Kalam Kohistani) letter values that are not Urdu's.

The 1995 Gawri spelling committee kept maximum conformity with Urdu but
added four letters and two digraphs for sounds Urdu does not have, and
Gawri's own phoneme inventory differs from Urdu's in two ways that the
shared letter shapes hide: there are no voiced aspirates, and there is no
glottal stop. Reading Gawri text with Urdu letter values therefore gets
the retroflex and dental affricates, the lateral fricative, the retroflex
nasal, the aspirate digraphs and every hamza wrong at once.

Sources are Baart & Sagar, *The Gawri Language of Kalam and Dir Kohistan*
(§2.1.2 consonants, §2.3 script) and Baart 2004, *Tone and song in Kalam
Kohistani* (§2.2 Table 2), both cited in the ``gwc`` spec.
"""
import pytest

from orthography2ipa.g2p import G2P

GWC = G2P("gwc")


# Baart & Sagar §2.3, "Special consonants in the Gawri alphabet": the Bari
# He shape carries the dental and retroflex affricates (three nuqtas above
# for ts, as in Pashto; two vertical nuqtas below for the retroflex), Sin
# with two vertical nuqtas above is the retroflex fricative, and Laam with
# a strike-through is the lateral fricative that contrasts with l.
@pytest.mark.parametrize("word,expected", [
    ("ݭ", "ʂ"),
    ("ݪ", "ɬ"),
    ("ڄ", "ʈʂ"),
    ("څ", "t̪s"),
    ("ڄھ", "ʈʂʰ"),
    ("څھ", "t̪sʰ"),
])
def test_committee_letters_beyond_the_urdu_alphabet(word, expected):
    assert GWC.transcribe(word) == expected


# Baart & Sagar §2.1.2 Table 2: the aspirated series covers only the
# voiceless stops and affricates, so Gawri has no voiced aspirates and the
# Urdu-shaped digraphs spell plain voiced consonants and nothing else.
@pytest.mark.parametrize("word,expected", [
    ("بھ", "b"),
    ("دھ", "d̪"),
    ("ڈھ", "ɖ"),
    ("گھ", "ɡ"),
    ("جھ", "dʑ"),
    ("ڑھ", "ɽ"),
])
def test_no_voiced_aspirates(word, expected):
    assert GWC.transcribe(word) == expected
    assert "ʱ" not in GWC.transcribe(word)


# Baart & Sagar §2.3, "The retroflex nasal": ɳ is written Nun + retroflex
# Re. The parallel Nun + Gaf digraph for ŋ is an inference from §2.1.2's
# remark that ɳ and ŋ might be analysed as n+ɖ and n+ɡ — the committee
# stated a digraph only for ɳ — and it is the majority gold reading, not a
# certain one. Retroflex Re on its own stays the flap ɽ, which is what
# makes the ɳ digraph worth encoding.
@pytest.mark.parametrize("word,expected", [
    ("نڑ", "ɳ"),
    ("نگ", "ŋ"),
    ("ڑ", "ɽ"),
])
def test_nasal_digraphs(word, expected):
    assert GWC.transcribe(word) == expected


# The consonant table of both sources has no glottal stop, so the letters
# that carry one in Arabic and Urdu cannot produce one here: ain and the
# bare hamza are silent carriers, and hamza-on-ya spells the glide.
@pytest.mark.parametrize("word", ["علاقہ", "چارئی", "بوبئ", "دشئ", "ائں"])
def test_no_glottal_stop_anywhere(word):
    assert "ʔ" not in GWC.transcribe(word)


# Both sources put ⟨š č ǰ⟩ in a palatal column explicitly contrasted with
# a separate retroflex column carrying ⟨ṣ c̣⟩ (Baart & Sagar §2.1.2 Table 2;
# Baart 2004 §2.2 Table 2). The alveolo-palatal sibilants are the
# palatal-region IPA letters, so the palatal series is ɕ tɕ dʑ and stays
# distinct from the retroflex ʂ ʈʂ that the committee letters spell.
@pytest.mark.parametrize("word,expected", [
    ("ش", "ɕ"),
    ("چ", "tɕ"),
    ("ج", "dʑ"),
    ("چھ", "tɕʰ"),
])
def test_palatal_series_is_alveolo_palatal(word, expected):
    assert GWC.transcribe(word) == expected


def test_palatal_and_retroflex_sibilants_stay_distinct():
    assert GWC.transcribe("ش") != GWC.transcribe("ݭ")
    assert GWC.transcribe("چ") != GWC.transcribe("ڄ")


# Baart & Sagar §2.1.2 Table 2 puts r in the flap row, not with the
# trills: the plain Re is the dental flap ɾ and contrasts with retroflex ɽ.
def test_re_is_a_flap():
    assert GWC.transcribe("ر") == "ɾ"
    assert GWC.transcribe("بور") == "boːɾ"


# Baart & Sagar §2.3, "The writing of Gawri vowels": Pesh always
# designates the u-quality and Zer always the i-quality, so a Wau written
# without Pesh is the o-quality and a Ye written without Zer the
# e-quality; Jazm on top of either marks it short. Word-initial long aː is
# written with Alif Madda, so a bare initial Alif is a short-vowel carrier.
@pytest.mark.parametrize("word,expected", [
    ("چور", "tɕoːɾ"),
    ("بیر", "beːɾ"),
    ("وْ", "o"),
    ("یْ", "e"),
    ("ٞ", "æ"),
    ("آ", "aː"),
])
def test_committee_vowel_rules(word, expected):
    assert GWC.transcribe(word) == expected


def test_bare_initial_alif_is_not_long():
    assert GWC.transcribe("اڈ") == "aɖ"


# Word-final choti he is the vowel, as in the Urdu spelling conventions
# the committee chose to follow.
def test_final_he_is_a_vowel():
    assert GWC.transcribe("بالہ") == "baːla"
    assert GWC.transcribe("ہیریٹ") == "heːɾeːʈ"


# A glide between two vowels stays a glide rather than becoming a vowel of
# its own: the positional override has to beat the flat table both ways.
def test_intervocalic_wau_is_a_glide():
    assert GWC.transcribe("داوال") == "d̪aːwaːl"
