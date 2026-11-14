"""Dongxiang / Santa (`sce`) — the post-velar series a Pinyin reading loses.

Santa is a Mongolic language of Gansu, written here in the experimental
Pinyin-based romanization of A Yibulaheimai and A Shelefu (2001). Most of its
letters do take Pinyin values, which is why the spec reads as a Pinyin table;
the part that is not Pinyin is the post-velar series. Kim's chapter lists the
consonants by place as 'the velars k g h ng (k g x ng), and the post-velars
(uvulars and glottals) kh gh hh (q gh h)', and names the spelling of the
spirant realisation directly: 'some sources claim that Santa actually has two
kinds of postvelar gh, one of which is a stop, while the other is a spirant
(orthographically gv)' (Kim 2003, in Janhunen ed., The Mongolic Languages,
pp. 349-350).

Expected strings are written from that description, never read back from the
engine.
"""
import pytest

import orthography2ipa as o2i


@pytest.fixture(scope="module")
def sce():
    return o2i.G2P("sce")


def strip_stress(s):
    return s.replace("ˈ", "").replace("ˌ", "")


@pytest.mark.parametrize("spelling,segment", [
    ("gh", "q"),
    ("kh", "qʰ"),
    ("hh", "h"),
])
def test_the_post_velar_series_is_not_read_as_pinyin(sce, spelling, segment):
    """⟨gh kh hh⟩ are uvular and glottal, not the velar-plus-h clusters a
    Pinyin reading of the letters would give."""
    assert strip_stress(sce.transcribe_word(spelling)) == segment


def test_gv_is_the_spirant_realisation_of_gh(sce):
    """⟨gv⟩ is ʁ. Without the key ⟨v⟩ has no reading at all and is deleted in
    silence; it occurs 21 times in the shipped gold and only ever in ⟨gv⟩."""
    assert strip_stress(sce.transcribe_word("bagva")) == "pɑʁɑ"


def test_v_never_stands_alone(sce):
    """The letter has no reading of its own — it is only ever the second half
    of ⟨gv⟩ — so a bare ⟨v⟩ must not silently vanish from a word that has one."""
    assert "ʁ" in sce.transcribe_word("gv")


@pytest.mark.parametrize("spelling,expected", [
    ("dangao", "tɑnkɑw"),
    ("miengu", "mjənku"),
])
def test_ng_before_a_vowel_is_a_coda_n_plus_an_onset_g(sce, spelling, expected):
    """⟨ng⟩ occurs only syllable-finally (Kim 2003: 350), so before a vowel the
    two letters belong to different syllables and are not the velar nasal."""
    assert strip_stress(sce.transcribe_word(spelling)) == expected


@pytest.mark.parametrize("spelling,expected", [
    ("ao", "ɑw"),
    ("ou", "əw"),
    ("ei", "əj"),
    ("ai", "ɑj"),
    ("ie", "jə"),
    ("ia", "jɑ"),
    ("iu", "ju"),
    ("ua", "wɑ"),
    ("ui", "wəj"),
    ("uai", "wɑj"),
])
def test_the_glide_combinations_are_the_closed_set_kim_lists(sce, spelling, expected):
    """'The possible combinations of vowels with medial and final glides are
    (orthographically): ai ei ao ou ui ua uai iu ie ia io iao' (Kim 2003: 351).
    Read letter by letter these would end in a full vowel instead of a glide."""
    assert strip_stress(sce.transcribe_word(spelling)) == expected


def test_i_is_backed_after_a_uvular(sce):
    """'The quality [ɯ] occurs mainly after the uvular consonants kh gh in
    complementary distribution with i' (Kim 2003: 348), which is what
    ⟨ghimusun⟩ writes."""
    out = strip_stress(sce.transcribe_word("ghigva"))
    assert out == "qɯʁɑ"


def test_i_stays_front_after_a_non_uvular(sce):
    """The backing is conditioned, not general: ⟨bi⟩ keeps i."""
    assert strip_stress(sce.transcribe_word("bi")) == "pi"


def test_r_is_the_liquid_not_the_retroflex_fricative(sce):
    """⟨r⟩ heads the retroflex series as a liquid (Kim 2003: 349). The gold
    writes r in 25 occurrences against ʐ in 3."""
    assert strip_stress(sce.transcribe_word("boro")) == "poro"


def test_low_vowel_is_back(sce):
    """The gold writes ɑ in 113 segments against a in 1."""
    assert strip_stress(sce.transcribe_word("aba")) == "ɑpɑ"


@pytest.mark.parametrize("letter", ["ê", "ü"])
def test_pinyin_only_vowel_letters_are_not_mapped(sce, letter):
    """Santa's vowels are a e i o u, with ɯ an allophone of i (Kim 2003: 348).
    Neither Pinyin letter has a Santa phoneme behind it."""
    assert letter not in sce.spec.graphemes
