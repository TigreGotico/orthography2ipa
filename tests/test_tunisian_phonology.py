"""Tunisian Arabic (Tunis baseline) phonology: the rules that separate a Tunis
transcription from Moroccan/Algiers Maghrebi and from MSA.

This spec (`ar-TN`) targets the sedentary, pre-Hilalian Arabic of the Medina of
Tunis. Its four hallmarks, each cited on a real word:

* the interdentals /θ ð ðˤ/ are RETAINED (Tunis), where sedentary
  Moroccan/Algiers merge them to /t d dˤ/;
* qāf ق is /q/ (urban sedentary), with a cited Bedouin/rural variant /ɡ/;
* strong imāla raises long /aː/ to [ɛː], blocked next to an emphatic or a back
  consonant /q χ ʁ ħ ʕ r/;
* the inherited diphthongs /aj aw/ are monophthongised to [iː uː] in Tunis
  (the Sahel — Sūsa, Mahdia — retains them).

Sources: Singer (1984), *Grammatik der arabischen Mundart der Medina von Tunis*;
Gibson (2009), 'Tunis Arabic', *Encyclopedia of Arabic Language and Linguistics*
vol. 4; Talmoudi (1980), *The Arabic Dialect of Sūsa*; La Rosa (2021),
*Languages* 6:145 (open-access Sahel data); Watson (2002) for the Maghrebi ǧīm.

Expectations carry the engine's default stress mark ˈ; the quantity-sensitive
Arabic stress rule is inherited unchanged and is not what these tests probe.
"""
import pytest

from orthography2ipa import transcribe, get


def test_is_a_maghrebi_leaf_at_research_tier():
    """`ar-TN` hangs under the Proto-Maghrebi grouping node and is now a
    research-tier spec, with the Tunis primary literature cited."""
    spec = get("ar-TN")
    assert spec.parent == "ar-x-maghrebi"
    assert spec.quality.value == "research"
    ids = {s.id for s in spec.sources}
    assert {"singer1984", "gibson2009", "talmoudi1980"} <= ids


def test_interdentals_are_retained_in_tunis():
    """Tunis keeps the interdental fricatives (Gibson 2009; Singer 1984;
    Turki et al. 2024): ثلاثة 'three' → [θlɛːθa], not the Moroccan/Algiers
    merged [tlaːta]. This is the isogloss against sedentary Morocco/Algiers."""
    assert transcribe("ثلاثة", "ar-TN") == "ˈθlɛːθa"
    assert get("ar-TN").graphemes["ث"][0] == "θ"
    assert get("ar-TN").graphemes["ذ"][0] == "ð"
    # contrast: the merging sedentary Maghrebi neighbours
    assert transcribe("ثلاثة", "ar-MA") == "ˈtlaːta"


def test_qaf_is_uvular_q_with_a_cited_bedouin_g_variant():
    """Urban Tunis retains the voiceless uvular /q/ (Singer 1984; La Rosa 2021
    p.9): قاعة 'hall' → [qaːʕa]. The rural/Bedouin variant /ɡ/ is listed as the
    second candidate on both the grapheme and the allophone (gālū lī)."""
    assert transcribe("قاعة", "ar-TN") == "ˈqaːʕa"
    assert get("ar-TN").graphemes["ق"] == ["q", "ɡ"]
    assert get("ar-TN").allophones["q"] == ["q", "ɡ"]


def test_jim_is_the_sedentary_maghrebi_fricative():
    """ǧīm ج is the voiced post-alveolar fricative /ʒ/ with no occlusive onset —
    the sedentary Maghrebi reflex (Watson 2002 p.16; Singer 1984): جبل 'mountain'
    → [ʒbl]. Inherited from the Maghrebi grouping node, /ʒ/ is the primary
    candidate (the affricate /dʒ/ trails as the secondary Bedouin/eastern one)."""
    assert get("ar-TN").graphemes["ج"][0] == "ʒ"
    assert transcribe("جبل", "ar-TN") == "ˈʒbl"


@pytest.mark.parametrize("word,expected", [
    ("باب", "ˈbɛːb"),      # 'door' — bare /aː/ raises
    ("كتاب", "ˈktɛːb"),    # 'book'
    ("ثلاثة", "ˈθlɛːθa"),  # 'three'
])
def test_strong_imala_raises_long_a_to_open_front(word, expected):
    """Strong Tunis imāla: long /aː/ → [ɛː] in a neutral environment (Singer
    1984; Gibson 2009). This is the vowel that most audibly marks Tunis off from
    both MSA [aː] and Moroccan [aː]/[æː]."""
    assert transcribe(word, "ar-TN") == expected


@pytest.mark.parametrize("word,expected", [
    ("دار", "ˈdaːr"),      # /r/ blocks → stays [aː]
    ("مفتاح", "ˈmftaːħ"),  # pharyngeal /ħ/ blocks
    ("قاعة", "ˈqaːʕa"),    # uvular /q/ and pharyngeal /ʕ/ block
])
def test_imala_is_blocked_next_to_a_back_or_pharyngeal_consonant(word, expected):
    """Imāla does not apply when /aː/ is adjacent to a back consonant
    /q χ ʁ ħ ʕ r/; the vowel keeps its back [aː] quality (Singer 1984; Gibson
    2009). دار 'house' is [daːr], not *[dɛːr]."""
    assert transcribe(word, "ar-TN") == expected


@pytest.mark.parametrize("word,expected", [
    ("صابون", "ˈsˤɑːbwn"),  # emphatic /sˤ/ backs /aː/ → [ɑː] (inherited layer)
    ("طار", "ˈtˤɑːr"),       # emphatic /tˤ/
])
def test_emphatic_environment_backs_rather_than_raises(word, expected):
    """Next to an emphatic, the long vowel is backed to [ɑː] by the inherited
    emphasis-spreading layer, so imāla never reaches it — the opposite pole from
    the [ɛː] raising (Singer 1984; cf. Watson 2002 on emphasis)."""
    assert transcribe(word, "ar-TN") == expected


@pytest.mark.parametrize("word,expected", [
    ("بَيْت", "ˈbiːt"),   # /aj/ → [iː]  'room/house'
    ("لَوْن", "ˈluːn"),   # /aw/ → [uː]  'colour'
])
def test_diphthongs_monophthongise_in_tunis(word, expected):
    """Sedentary Tunis monophthongised the inherited diphthongs: /aj/ → [iː],
    /aw/ → [uː] (Gibson 2009; Singer 1984). The Sahel (Talmoudi 1980; La Rosa
    2021, lūn [lɔːn]) keeps the diphthong — a split this Tunis-baseline leaf
    deliberately does not model."""
    assert transcribe(word, "ar-TN") == expected
