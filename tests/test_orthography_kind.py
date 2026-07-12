"""What kind of writing a spec's graphemes encode.

"This is how Mandarin is officially written" and "this is Arabic letters in ASCII"
are not the same claim, and a consumer must be able to tell them apart.
"""
import orthography2ipa as o2i
from orthography2ipa import G2P, OrthographyKind


def test_zh_is_a_romanization_and_says_so():
    """zh reads PINYIN. It used to declare `script: Hanzi/Pinyin` and
    `script_type: logographic` — describing a spec it is not. Nothing in it reads
    a Han character, and nothing could."""
    zh = o2i.get("zh")
    assert zh.orthography_kind is OrthographyKind.ROMANIZATION
    assert zh.script == "Latin"
    assert G2P("zh").transcribe("beijing") == "peitɕiŋ"
    # A romanization is a real orthography: it has a standards body.
    assert zh.orthography_standard is not None


def test_the_native_han_spec_is_honest_about_being_unreadable():
    """A Han character does not encode sound, so there is no grapheme->IPA rule to
    write. The empty map is the answer, not a gap — and the phonology is still
    fully known, which is the whole point of separating sounds from spelling."""
    han = o2i.get("zh-Hani")
    assert han.orthography_kind is OrthographyKind.NATIVE
    assert han.graphemes == {}          # honest, not missing
    assert han.phonemes                 # …yet the phonology is declared
    assert "dictionary" in han.notes.lower()


def test_buckwalter_is_a_transliteration_not_an_orthography():
    """Buckwalter re-encodes Arabic letters in ASCII. Nobody reads it as a
    language, and it has no standards body — that absence is the tell."""
    bw = o2i.get("ar-Latn-buckwalter")
    assert bw.orthography_kind is OrthographyKind.TRANSLITERATION
    assert bw.orthography_standard is None


def test_buckwalter_is_lossless_against_the_script_it_re_encodes():
    """A transliteration that changes the pronunciation is not a transliteration.
    Same word, two encodings, one IPA."""
    table = {'ا':'A','ب':'b','ة':'p','ت':'t','ج':'j','د':'d','ر':'r','س':'s','ك':'k',
             'ل':'l','م':'m','ن':'n','ي':'y','و':'w','ع':'E','ق':'q','ء':"'",'آ':'|',
             'َ':'a','ُ':'u','ِ':'i','ْ':'o','ّ':'~'}
    for word in ("كَتَبَ", "كِتَاب", "مَدْرَسَة", "بَيْت", "مُسْلِم", "قُرْآن"):
        buckwalter = "".join(table[ch] for ch in word)
        assert G2P("ar").transcribe(word) == G2P("ar-Latn-buckwalter").transcribe(buckwalter)


def test_buckwalter_inherits_the_abjad_limit_it_cannot_escape():
    """Re-encoding a script cannot recover information the script never wrote.
    Unvocalized Buckwalter is exactly as unreadable as unvocalized Arabic — the
    short vowels are simply absent from both."""
    vocalized = G2P("ar-Latn-buckwalter").transcribe("kataba")
    bare = G2P("ar-Latn-buckwalter").transcribe("ktb")
    assert vocalized != bare
    assert "a" not in bare          # nothing invented the vowels back
