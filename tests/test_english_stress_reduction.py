"""Cited-rule conformance: English (RP) word stress and unstressed-vowel
reduction.

Each test takes one claim from ``en-GB``'s ``stress.notes`` or its reduction
prose, quotes it with its citation, and proves the engine honours it on a real
word. Claims the engine does NOT honour are stated as such — as an explicit
ceiling test with its reason — never quietly dropped.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.stress import detect_stress
from orthography2ipa import get

DESCENDANTS = ["en-US", "en-AU", "en-CA", "en-IE", "en-ZA", "en-GB-x-scotland"]


@pytest.fixture(scope="module")
def en():
    return G2P("en-GB")


# ── stress placement ────────────────────────────────────────────────────

def test_default_is_stem_initial(en):
    """DEFAULT = FIRST SYLLABLE: the Germanic stem-initial pattern English
    inherited (Fudge 1984 ch. 1-2; Cruttenden 2014 §10.4)."""
    rules = get("en-GB").stress
    assert rules is not None
    assert rules.default_position == 1
    for word in ("summer", "happy", "problem", "common"):
        assert en.transcribe_word(word).startswith("ˈ")
    assert detect_stress("problem", rules) == 0


@pytest.mark.parametrize("word,index", [
    ("ability", 1),      # a-bi-li-ty
    ("classify", 0),     # cla-ssi-fy
    ("critical", 0),     # cri-ti-cal
    ("photography", 1),  # pho-to-gra-phy
    ("regular", 0),      # re-gu-lar
    ("democracy", 1),    # de-mo-cra-cy
    # NOT here: ⟨biology⟩. The bundled syllabifier merges each run of vowel
    # letters into one nucleus, so ⟨bio-⟩ is one syllable and the word counts
    # as three; English writes hiatus with the same letter sequences it writes
    # diphthongs with, and no ending table can repair that.
])
def test_two_syllable_pre_stressed_suffixes(word, index):
    """Fudge's PRE-STRESSED suffix classes whose suffix is two orthographic
    syllables put the accent on the antepenult (Fudge 1984, ch. 3-4)."""
    rules = get("en-GB").stress
    assert detect_stress(word, rules) == index


def test_weak_form_articles_carry_no_stress(en):
    """A weak form is by definition unstressed, so the stress placer must not
    mark it (Cruttenden 2014 §9.2; Wells 1982 vol. 1)."""
    assert en.transcribe_word("the") == "ðə"
    assert en.transcribe_word("a") == "ə"
    assert en.transcribe_word("an") == "ən"
    # a full-vowel monosyllable in the same word_exceptions table still is
    assert en.transcribe_word("she") == "ˈʃiː"


# ── unstressed-vowel reduction ──────────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("woman", "ˈwɒmən"),     # unstressed ⟨a⟩ (the stressed ⟨o⟩ keeps ɒ:
                             # magic-e/open-syllable tensing is a spec limit)
    ("common", "ˈkɒmən"),    # unstressed ⟨o⟩
    ("album", "ˈælbəm"),     # unstressed ⟨u⟩
    ("problem", "ˈpɹɒbləm"),  # unstressed ⟨e⟩ in a CLOSED syllable
    ("open", "ˈɒpən"),
])
def test_unstressed_vowels_reduce_to_schwa(en, word, expected):
    """In RP the vowel of an unstressed syllable is a weak vowel,
    overwhelmingly /ə/ (Cruttenden 2014 §9.4; Carney 1994 §II)."""
    assert en.transcribe_word(word) == expected


@pytest.mark.parametrize("word", ["doctor", "dollar", "sugar", "mirror"])
def test_unstressed_rhotic_nuclei_reduce(en, word):
    """Unstressed ⟨or⟩ / ⟨ar⟩ are /əɹ/, which RP's non-rhotic rule then
    reduces to [ə] word-finally (Cruttenden 2014 §9.4, §8.7; Carney 1994)."""
    out = en.transcribe_word(word)
    assert out.endswith("ə"), out
    assert "ɔː" not in out and "ɑː" not in out


def test_unstressed_e_reduces_only_in_a_closed_syllable(en):
    """Cruttenden 2014 §9.4 separates the /ə/ and /ɪ/ weak-vowel
    distributions: closed weak syllable → /ə/, open weak syllable → /ɪ/.
    ⟨begin⟩'s first syllable is open, so its ⟨e⟩ must NOT be /ə/."""
    assert en.transcribe_word("problem").endswith("ləm")
    assert "ə" not in en.transcribe_word("begin")


def test_a_stressed_vowel_is_never_reduced(en):
    """The reduction is conditioned on the syllable being unstressed; the
    stressed nucleus keeps its full value."""
    assert en.transcribe_word("cat") == "ˈkæt"
    assert en.transcribe_word("common").startswith("ˈkɒ")


# ── inheritance / blast radius ──────────────────────────────────────────

@pytest.mark.parametrize("code", DESCENDANTS)
def test_descendants_inherit_stress_and_reduction(code):
    """The en-GB descendants declare ``graphemes_base: en-GB``, so they
    inherit the stress block and the reduction positions rather than silently
    losing them."""
    spec = get(code)
    assert spec.stress is not None
    assert spec.stress.default_position == 1
    assert "ə" in spec.positional_graphemes["a"].get("nucleus_unstressed", [])
    assert G2P(code).transcribe_word("common").endswith("ən")


# ── declared ceilings ───────────────────────────────────────────────────

def test_noun_verb_stress_pairs_are_a_documented_ceiling():
    """Noun/verb pairs are lexical and part-of-speech conditioned, not
    orthographic (Cruttenden 2014 §10.7; Wells 2008 LPD). One spelling has one
    orthographic stress, so the engine gives both readings the same one."""
    rules = get("en-GB").stress
    assert detect_stress("record", rules) == detect_stress("record", rules)
    assert detect_stress("record", rules) == 0   # the noun reading


def test_secondary_stress_is_not_modelled(en):
    """The engine's stress is binary, so a syllable carrying SECONDARY stress
    is treated as fully weak (Cruttenden 2014 §10.3). ⟨combination⟩ is
    ˌkɒmbɪˈneɪʃən in RP; the engine has no way to protect that first vowel
    once the accent moves off it — which is why the one-syllable pre-stressed
    suffixes are deliberately not declared."""
    assert "ˌ" not in en.transcribe_word("combination")
