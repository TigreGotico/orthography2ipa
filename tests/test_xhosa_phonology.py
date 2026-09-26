"""Behaviour tests for the Xhosa (``xh``) spec.

The click table, the implosive/plosive ⟨b⟩–⟨bh⟩ split, post-nasal hardening,
the lateral obstruents and penultimate lengthening are all cited in the
spec's ``notes``; the sources are listed in its ``sources`` block.
"""
import pytest

from orthography2ipa import get, transcribe
from orthography2ipa.types import QualityTier


def tr(word):
    return transcribe(word, "xh")


def test_quality_and_sources():
    spec = get("xh")
    assert spec.quality is QualityTier.RESEARCH
    ids = {s.id for s in spec.sources}
    assert {"jessen2002_acoustic", "hyman2013_penult", "jessen_roux2002"} <= ids


# --- clicks -----------------------------------------------------------------
# Three click types x six series. Every click carries a rear velar closure, so
# the segment is the two-symbol sequence kǀ / ŋǀ, not a bare click letter.

@pytest.mark.parametrize("grapheme,ipa", [
    ("c", "kǀ"), ("ch", "kǀʰ"), ("gc", "ɡǀ"),
    ("nc", "ŋǀ"), ("ngc", "ŋǀ"), ("nkc", "ŋkǀ"),
    ("x", "kǁ"), ("xh", "kǁʰ"), ("gx", "ɡǁ"),
    ("nx", "ŋǁ"), ("ngx", "ŋǁ"), ("nkx", "ŋkǁ"),
    ("q", "kǃ"), ("qh", "kǃʰ"), ("gq", "ɡǃ"),
    ("nq", "ŋǃ"), ("ngq", "ŋǃ"), ("nkq", "ŋkǃ"),
])
def test_click_table_is_complete(grapheme, ipa):
    assert get("xh").graphemes[grapheme][0] == ipa


def test_plain_click_carries_its_velar_closure():
    """⟨caca⟩ is [kǀaːkǀa] — a bare ǀ would drop the rear articulation."""
    assert tr("caca") == "kǀaːkǀa"


def test_breathy_nasal_click_is_not_ng_plus_click():
    """⟨ingca⟩ is [iːŋǀa]: ⟨ngc⟩ is one nasal click, not ⟨ng⟩ + ⟨c⟩."""
    assert tr("ingca") == "iːŋǀa"


def test_nasal_velar_click_series():
    assert tr("nkqo") == "ŋkǃo"


# --- stops ------------------------------------------------------------------

def test_b_is_implosive_and_bh_is_the_plosive():
    assert tr("abo") == "aːɓo"
    assert tr("ibhasi") == "ibaːsi"


def test_v_is_transcribed():
    """⟨v⟩ was absent from the grapheme table and silently vanished."""
    assert tr("isilevu") == "isileːvu"
    assert "v" in tr("imvubu")


# --- palatals, laterals, dorsals -------------------------------------------

def test_palatal_stops():
    assert tr("tya") == "ca"
    assert tr("ukutya") == "ukuːca"
    assert tr("indyebo") == "iɲɟeːɓo"


def test_lateral_obstruents():
    assert tr("ihlathi") == "iɬaːtʰi"
    assert tr("indlu") == "iːndɮu"
    assert tr("intloko") == "intɬoːko"


def test_rh_is_a_velar_fricative_and_kr_a_velar_affricate():
    assert tr("urhulumente") == "uxulumeːnte"
    assert tr("ukrebe") == "ukxeːɓe"


def test_post_nasal_hardening_of_z():
    assert tr("amanzi") == "amaːndzi"


def test_nasal_is_homorganic_before_a_palatal():
    assert tr("intshonalanga") == "iɲtʃonalaːŋɡa"
    assert tr("njalo") == "ɲdʒaːlo"
    assert tr("injongo") == "iɲdʒoːŋɡo"


def test_hh_is_the_breathy_glottal():
    assert get("xh").graphemes["hh"][0] == "ɦ"
    assert get("xh").graphemes["h"][0] == "h"


# --- prosody ----------------------------------------------------------------

def test_penultimate_vowel_is_long():
    assert tr("molo") == "moːlo"
    assert tr("thina") == "tʰiːna"
    assert tr("kancinci") == "kaŋǀiːŋǀi"


def test_monosyllables_are_not_lengthened():
    """Penultimate lengthening needs a penult; ⟨fa⟩ and ⟨lo⟩ have none."""
    assert tr("fa") == "fa"
    assert tr("lo") == "lo"


@pytest.mark.parametrize("word,ipa", [
    ("moya", "moːja"),
    ("ikhaya", "ikʰaːja"),
    ("hayi", "haːji"),
    ("fuya", "fuːja"),
    ("leyo", "leːjo"),
    ("isithunywa", "isitʰuːɲʷa"),
    ("loo", "loːo"),
])
def test_length_lands_on_the_penult_across_a_glide(word, ipa):
    """⟨y⟩ and ⟨w⟩ are consonants: they open a syllable, they are not part of
    the nucleus. Counting them as vowels merges ⟨oya⟩ into one nucleus and the
    length lands on the wrong vowel, or on two at once."""
    assert tr(word) == ipa


def test_no_word_ends_in_a_long_vowel():
    """The penult is never the last syllable."""
    for word in ["molo", "moya", "loo", "hayi", "fa", "isithunywa", "caca"]:
        assert not tr(word).endswith("ː"), word


def test_no_word_carries_two_length_marks():
    for word in ["moya", "ikhaya", "loo", "isithunywa", "kancinci"]:
        assert tr(word).count("ː") <= 1, word


def test_vowel_letters_is_declared():
    assert get("xh").stress.vowel_letters == ("a", "e", "i", "o", "u")


def test_w_after_a_consonant_is_labialisation():
    assert tr("incwadi") == "iŋǀʷaːdi"


# --- the syllabic nasal and the prenasalised series --------------------------
# The class 1/3 prefix ⟨um-⟩ carries a syllabic nasal; the class 9/10 prefix
# ⟨im-⟩ carries a plain prenasalisation. They are spelled alike, so the spec
# keys on the word-initial ⟨u⟩. See XH_SYLLABIC_M and the XH_UM_PREFIX_* rules.

def test_choti_source_is_declared():
    assert "choti2015" in {s.id for s in get("xh").sources}


@pytest.mark.parametrize("word,ipa", [
    ("umbala", "um̩ɓaːla"),
    ("umfana", "um̩faːna"),
    ("umzi", "uːm̩zi"),
    ("umthi", "uːm̩tʰi"),
    ("umphathi", "um̩pʰaːtʰi"),
    ("umvuzo", "um̩vuːzo"),
    ("umfi", "uːm̩fi"),
    ("umpu", "uːm̩pu"),
])
def test_class_1_um_prefix_nasal_is_syllabic(word, ipa):
    """Disyllabic ⟨um-⟩ words (⟨umfi⟩, ⟨umpu⟩) carry penultimate lengthening
    on the ⟨u⟩ itself, which used to make the syllabic-prefix rules miss —
    they keyed on the ⟨u⟩ PHONEME, and by the time they ran it had already
    become ``uː``. The rules now key on the ⟨u⟩ GRAPHEME instead, which
    penultimate lengthening never touches."""
    assert tr(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("impala", "impaːla"),
    ("imbali", "imbaːli"),
    ("impilo", "impiːlo"),
    ("ikampu", "ikaːmpu"),
])
def test_class_9_im_prefix_nasal_is_not_syllabic(word, ipa):
    """Only a word-initial ⟨u⟩ licenses the syllabic reading, so ⟨im-⟩ and a
    word-internal ⟨mp⟩ stay plain prenasalisation."""
    assert tr(word) == ipa


@pytest.mark.parametrize("grapheme,ipa", [
    ("mp", "mp"), ("mph", "mpʰ"), ("mbh", "mb"),
])
def test_prenasalised_labial_stops_are_single_graphemes(grapheme, ipa):
    """⟨mb nd ng nk nt nz nj⟩ were in the table but the labial stop members
    were not, so ⟨mp⟩ was read as two segments and ⟨mbh⟩ stranded its ⟨h⟩."""
    assert get("xh").graphemes[grapheme][0] == ipa


def test_mbh_is_the_prenasalised_plain_plosive():
    """⟨bh⟩ is the plain [b] against implosive ⟨b⟩ [ɓ], and ⟨mbh⟩ inherits it."""
    assert tr("umbhobho") == "um̩boːbo"


@pytest.mark.parametrize("grapheme,ipa", [
    ("mh", "m"), ("nh", "n"), ("nyh", "ɲ"), ("ngh", "ŋ"),
])
def test_slack_voice_nasal_digraphs_are_read(grapheme, ipa):
    """⟨mh nh nyh ngh⟩ are the depressor nasals [m̤ n̤ n̠̤ʲ ŋ̤] (xhosa_wiki).
    This spec does not transcribe depressor voice quality, so they surface as
    the plain nasal — but they must be READ, or the ⟨h⟩ is emitted literally."""
    assert get("xh").graphemes[grapheme][0] == ipa


@pytest.mark.parametrize("word,ipa", [
    ("umhlaba", "um̩ɬaːɓa"),
    ("umhleli", "um̩ɬeːli"),
])
def test_hl_after_a_nasal_is_the_lateral_fricative(word, ipa):
    """⟨mhl⟩ is ⟨m⟩ + ⟨hl⟩, not the depressor digraph ⟨mh⟩ plus a stray ⟨l⟩."""
    assert tr(word) == ipa


def test_ng_apostrophe_is_the_plain_velar_nasal():
    """⟨ngʼ⟩ is [ŋ] against ⟨ng⟩ [ŋɡ] (xhosa_wiki)."""
    assert tr("ing'ang'ane") == "iŋaŋaːne"


@pytest.mark.parametrize("word,ipa", [
    ("imfene", "iɱpfeːne"),
    ("imvula", "iɱbvuːla"),
])
def test_prenasalised_labiodental_fricatives_affricate(word, ipa):
    """"Fricatives become affricated and, if voiceless, they become ejectives
    as well: mf is pronounced [ɱp̪fʼ]" (xhosa_wiki). The class 1/3 syllabic
    nasal is not a prenasalisation, so ⟨umfana⟩ keeps its plain [f]."""
    assert tr(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("umfula", "um̩fuːla"),
    ("umfi", "uːm̩fi"),
    ("umfo", "uːm̩fo"),
    ("umpha", "uːm̩pʰa"),
])
def test_the_um_prefix_blocks_affrication(word, ipa):
    """⟨umfi⟩/⟨umfo⟩ are disyllabic, so the ⟨u⟩ carries the penultimate
    length; the class 1/3 rule must still see through it to the ⟨u⟩
    grapheme and block the class 9/10 affrication."""
    assert tr(word) == ipa


# --- prenasalised series stays digraphs, never superscript modifiers --------
# The Kaikki gold writes prenasalisation with a non-syllabic superscript
# nasal (e.g. ⟨impala⟩ [íᵐpaːlá]); this spec instead writes the class 9/10
# prenasalised series as plain digraphs (⟨mp⟩ → "mp", ⟨nt⟩ → "nt"...). That
# matters beyond notation: ``allophony._is_modifier`` treats any Lm-category
# character — which the superscript nasals ᵐⁿᵑᶮ are — as attaching to the
# PRECEDING base rather than starting its own segment, so a spec that ever
# emitted them would have its prenasalised stops silently absorbed into the
# vowel before them by ``segment_ipa``. Locking the digraph convention here
# keeps the spec on the side of that engine limitation that does not bite.
@pytest.mark.parametrize("word", [
    "impala", "into", "indaba", "ubuntu", "intaba", "impi", "impilo",
    "intloko", "indlovu", "indlu", "umntwana", "umlungu", "umlenze",
])
def test_prenasalised_series_never_emits_a_superscript_modifier(word):
    ipa = tr(word)
    for ch in "ᵐⁿᵑᶬᶮ":
        assert ch not in ipa, (
            f"{word!r} -> {ipa!r} contains the superscript prenasal "
            f"{ch!r}; prenasalisation must stay a plain digraph, see the "
            "module docstring above")
