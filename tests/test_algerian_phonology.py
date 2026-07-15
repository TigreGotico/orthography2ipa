"""Algerian Arabic (Algiers baseline) phonology: the rules that separate an
Algiers transcription from Tunis, from Moroccan, and from MSA.

This spec (`ar-DZ`) targets the sedentary, pre-Hilalian Arabic of the old city
of Algiers, with the Bedouin/rural layer diffusing in. Its hallmarks, each cited
on a real word:

* the interdentals /θ ð ðˤ/ are MERGED to the dental stops /t d dˤ/ (Algiers),
  the isogloss against Tunis, which retains them;
* qāf ق is /q/ in old-urban Algiers, with the Bedouin/rural variant /ɡ/ current
  across the country (dual /q ~ ɡ/);
* ǧīm ج is /ʒ/ (sedentary Maghrebi fricative), with the pre-Hilalian Algiers
  affricate /dʒ/ surviving as the secondary candidate;
* heavy short-vowel syncope to schwa [ə]/∅ licenses initial clusters;
* there is NO strong imāla — long /aː/ keeps its back quality (unlike Tunis).

Sources: Boucherit (2002), *L'arabe parlé à Alger*; Marçais (1902), *Le dialecte
arabe parlé à Tlemcen* (public domain); Grand'Henry (1972), *Le parler arabe de
Cherchell*; Watson (2002) for the Maghrebi ǧīm and emphasis spreading.

Expectations carry the engine's default stress mark ˈ.
"""
import pytest

from orthography2ipa import transcribe, get


def test_is_a_maghrebi_leaf_at_research_tier():
    """`ar-DZ` hangs under the Proto-Maghrebi grouping node and is now a
    research-tier spec, citing the Algiers/Algerian primary literature."""
    spec = get("ar-DZ")
    assert spec.parent == "ar-x-maghrebi"
    assert spec.quality.value == "research"
    ids = {s.id for s in spec.sources}
    assert {"boucherit2002", "marcais1902", "grand_henry1972"} <= ids


@pytest.mark.parametrize("word,expected", [
    ("ثلاثة", "ˈtlaːta"),   # ث → /t/  'three'
    ("ذيب", "ˈdjb"),         # ذ → /d/  'wolf'
])
def test_interdentals_merge_to_stops_in_algiers(word, expected):
    """Algiers merges the interdental fricatives to the dental stops: ث → /t/,
    ذ → /d/, ظ/ض → /dˤ/ (Boucherit 2002; Marçais 1902). This is the isogloss
    against Tunis, which retains /θ ð ðˤ/."""
    assert transcribe(word, "ar-DZ") == expected
    assert get("ar-DZ").graphemes["ذ"][0] == "d"
    # contrast: the Tunis leaf keeps the fricative
    assert transcribe("ثلاثة", "ar-TN").startswith("ˈθ")


def test_no_interdental_fricative_survives():
    """Nothing in an Algiers transcription of an etymological-interdental word
    should surface as /θ/ or /ð/ (Boucherit 2002)."""
    out = transcribe("ثلاثة", "ar-DZ")
    assert "θ" not in out and "ð" not in out


def test_qaf_is_dual_q_and_g():
    """Old-urban Algiers keeps /q/ (qalb → [qlb] after syncope), while the
    Bedouin/rural /ɡ/ is current across the country: the grapheme and the
    allophone both list /q/ then /ɡ/ (Boucherit 2002; Grand'Henry 1972)."""
    assert get("ar-DZ").graphemes["ق"] == ["q", "ɡ"]
    assert get("ar-DZ").allophones["q"] == ["q", "ɡ"]
    assert transcribe("قلب", "ar-DZ") == "ˈqlb"


def test_jim_is_zh_with_the_prehilali_affricate_retained():
    """ǧīm ج is /ʒ/ (sedentary Maghrebi fricative, no occlusive onset — Watson
    2002 p.16): جَمَل → [ʒamal]. The pre-Hilalian Algiers affricate /dʒ/ survives
    as the secondary candidate (Boucherit 2002; Marçais 1902)."""
    assert transcribe("جَمَل", "ar-DZ") == "ˈʒamal"
    assert get("ar-DZ").graphemes["ج"][0] == "ʒ"
    assert "dʒ" in get("ar-DZ").graphemes["ج"]


def test_heavy_syncope_reduces_short_vowels():
    """The defining Maghrebi trait: short /a i u/ reduce to schwa [ə] or ∅ in
    weak positions, licensing word-initial clusters (Boucherit 2002; Marçais
    1902). The alternates are declared on each short vowel."""
    for v in ("a", "i", "u"):
        alts = get("ar-DZ").allophones.get(v)
        assert "ə" in alts and "" in alts, f"{v}: {alts}"
    # the reduction is visible: كتاب surfaces with an initial cluster
    assert transcribe("كتاب", "ar-DZ") == "ˈktaːb"


@pytest.mark.parametrize("word,expected", [
    ("كتاب", "ˈktaːb"),   # 'book' — long /aː/ stays back
    ("باب", "ˈbaːb"),     # 'door'
])
def test_no_imala_long_a_stays_back(word, expected):
    """Algiers has no strong imāla: in a neutral (non-emphatic) environment long
    /aː/ keeps its back quality and is not raised to [ɛː] the way the Tunis leaf
    raises it (Boucherit 2002; contrast Gibson 2009 for Tunis). This is the
    vowel isogloss between the two Maghrebi neighbours."""
    out = transcribe(word, "ar-DZ")
    assert out == expected
    assert "ɛː" not in out


@pytest.mark.parametrize("word,expected", [
    ("صابون", "ˈsˤɑːbwn"),  # emphatic /sˤ/ backs /aː/ → [ɑː]
    ("طار", "ˈtˤɑːr"),       # emphatic /tˤ/
])
def test_emphasis_backs_the_low_vowel(word, expected):
    """Emphasis spreads within the word, backing /a aː/ to [ɑ ɑː] next to an
    emphatic (inherited emphasis layer; Watson 2002). This backing, not imāla,
    is what happens to a long /aː/ in an emphatic environment in Algiers."""
    assert transcribe(word, "ar-DZ") == expected
