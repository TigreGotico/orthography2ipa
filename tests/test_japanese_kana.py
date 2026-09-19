"""Japanese kana → IPA.

Full-transcription pins for Standard Tokyo Japanese. Every expectation is a
whole word, so a rule that fixes one segment and breaks another cannot pass.

The two archiphonemes carry the interesting phonology. The moraic nasal /N/
(ん/ン) has no place of its own and copies the place of a following stop,
affricate or nasal; before a fricative, a glide, a vowel, or at the end of a
word there is no oral closure to copy and it stays uvular. The moraic
obstruent /Q/ (っ/ッ) is likewise placeless and surfaces as the closure half
of a geminate. Both descriptions are standard (Vance 2008; Labrune 2012) and
are recorded on the rules themselves in ``data/ja.json``.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def ja():
    return G2P("ja")


@pytest.mark.parametrize("word,ipa", [
    # /N/ takes labial place before a labial stop or nasal
    ("しんぶん", "ɕimbɯɴ"),
    ("さんぽ", "sampo"),
    ("あんまり", "ammaɾi"),
    # coronal before a coronal stop, affricate or nasal
    ("あんない", "annai"),
    ("かんたん", "kantaɴ"),
    ("かんじ", "kaɲdʑi"),
    # palatal before a palatal affricate or nasal
    ("こんにちは", "koɲɲitɕiha"),
    # velar before a velar stop
    ("てんき", "teŋki"),
    ("にほんご", "ɲihoŋɡo"),
    ("かんこく", "kaŋkokɯ"),
    # no oral closure to copy: fricative, glide, vowel, word end
    ("はんそく", "haɴsokɯ"),
    ("ほんや", "hoɴja"),
    ("せんえん", "seɴeɴ"),
    ("にほん", "ɲihoɴ"),
])
def test_moraic_nasal_place(ja, word, ipa):
    assert ja.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("がっこう", "ɡakkoɯ"),
    ("にっぽん", "ɲippoɴ"),
    ("まった", "matta"),
    ("いっしょ", "iɕɕo"),
    ("いっさい", "issai"),
    ("バッグ", "baɡɡɯ"),
    # affricates geminate on their stop portion
    ("まっちゃ", "mattɕa"),
    ("みっつ", "mittsɯ"),
    # nothing follows: an abrupt glottal closure
    ("あっ", "aʔ"),
])
def test_moraic_obstruent_gemination(ja, word, ipa):
    assert ja.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    # katakana rows must agree with their hiragana twins
    ("リャク", "ɾʲakɯ"),
    ("ヒャク", "çakɯ"),
    ("ひゃく", "çakɯ"),
    ("りゃく", "ɾʲakɯ"),
])
def test_katakana_matches_hiragana(ja, word, ipa):
    assert ja.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("ファン", "ɸaɴ"),
    ("フィルム", "ɸiɾɯmɯ"),
    ("フォーク", "ɸoːkɯ"),
    ("パーティー", "paːtiː"),
    ("ディスク", "disɯkɯ"),
    ("チェック", "tɕekkɯ"),
    ("ジェット", "dʑetto"),
    ("シェフ", "ɕeɸɯ"),
    ("ウィーン", "wiːɴ"),
    ("ウォーター", "woːtaː"),
    ("ヴァイオリン", "vaioɾiɴ"),
    ("ツァー", "tsaː"),
    ("クォーツ", "kwoːtsɯ"),
])
def test_gairaigo_digraphs(ja, word, ipa):
    """Loanword spellings write sounds the native kana grid cannot. Without
    these rows the small kana is dropped and the preceding full kana keeps
    its dictionary vowel — フォーク comes out with /ɯ/ where the spelling
    says /o/."""
    assert ja.transcribe_word(word) == ipa


def test_no_archiphoneme_leaks(ja):
    """``N`` and ``Q`` are spec-internal archiphoneme labels, not IPA. No
    transcription may contain them."""
    for word in (
        "しんぶん", "がっこう", "あっ", "ん", "っ", "ンッンー",
        "んん", "っっ", "ンン", "あっっさ",
    ):
        out = ja.transcribe_word(word)
        assert "N" not in out and "Q" not in out, (word, out)


def test_particle_ha_is_transcribed_from_its_kana(ja):
    """は is /wa/ only as a topic particle, which cannot be identified from
    a word in isolation. The spec transcribes the kana value; this pin exists
    so the convention mismatch stays a decision rather than drift."""
    assert ja.transcribe_word("は") == "ha"
    assert ja.transcribe_word("はな") == "hana"


def test_long_vowel_only_where_written(ja):
    """ー is the only length mark the orthography writes. The おう and えい
    spellings are transcribed as the vowel sequences their kana spell; golds
    that monophthongise them to /oː eː/ disagree by convention, not by fact."""
    assert ja.transcribe_word("ケーキ") == "keːki"
    assert ja.transcribe_word("とうきょう") == "toɯkʲoɯ"
    assert ja.transcribe_word("えいが") == "eiɡa"
