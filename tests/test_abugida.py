"""The abugida inherent-vowel model.

In an abugida a consonant letter carries an inherent vowel. That vowel is not
an unconditional suffix: it is *cancelled* when the next character supplies the
syllable's vowel itself (a dependent vowel sign) or suppresses it (a virama).
Only when neither follows does the inherent vowel surface.

These tests pin all three branches, the conjunct behaviour that falls out of
the virama branch, and the two script-agnosticism properties the engine relies
on so that no language-specific codepoint list is needed anywhere.
"""
from __future__ import annotations

import unicodedata

import pytest

from orthography2ipa import G2P, available_codes, get
from orthography2ipa.phonetok import PhonetokTokenizer, _is_virama


def _abugida_codes():
    return sorted(c for c in available_codes()
                  if get(c).inherent_vowel and get(c).graphemes)


# ═══════════════════════════════════════════════════════════════════════════
# The three branches of the rule
# ═══════════════════════════════════════════════════════════════════════════

def test_bare_consonant_surfaces_its_inherent_vowel():
    # क with nothing following it: the inherent vowel surfaces.
    assert G2P("hi").transcribe("क").startswith("k")
    tokens = PhonetokTokenizer(get("hi")).grapheme_tokens("क")
    assert tokens[0].ipa[0] == "kə"


def test_dependent_vowel_sign_replaces_the_inherent_vowel():
    # का = क + ा. The matra supplies "aː"; the inherent "ə" must NOT also
    # appear. Regression: this produced "kəaː" (append instead of replace).
    tokens = PhonetokTokenizer(get("hi")).grapheme_tokens("का")
    assert tokens[0].ipa[0] == "k", "inherent vowel not cancelled by the matra"
    assert G2P("hi").transcribe("का") == "kaː"


def test_virama_suppresses_the_inherent_vowel():
    # क् = क + virama: a bare consonant, and the virama is consumed.
    tokens = PhonetokTokenizer(get("hi")).grapheme_tokens("क्")
    assert len(tokens) == 1
    assert tokens[0].ipa[0] == "k"
    assert tokens[0].length == 2, "the virama must be consumed by the consonant"


def test_mark_supplying_no_vowel_leaves_the_inherent_vowel_standing():
    # Malayalam anusvara's IPA opens with a combining tilde — a diacritic that
    # modifies a vowel without supplying one, so ള keeps its inherent vowel for
    # the tilde to attach to. The pipeline emits NFD (bare "a" + combining
    # tilde U+0303), so spell the expectation with escapes.
    assert G2P("ml").transcribe("മലയാളം") == "malajaːɭãm"


# ═══════════════════════════════════════════════════════════════════════════
# Conjuncts fall out of the virama branch for free
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("lang,word,expected", [
    # C + virama + C is just a cluster once the virama suppresses the vowel.
    # க்க → a k-cluster, not kaka. Tamil's own data then states that a doubled
    # consonant is a long one (TA_GEM*, tests/test_indic_allophony.py), so the
    # cluster surfaces as [kː] — the engine's job here is only to suppress the
    # inherent vowel.
    ("ta", "வணக்கம்", "ʋaɳakːam"),
    ("kn", "ಕನ್ನಡ", "kannaɖa"),      # ನ್ನ → nn, not nana
    ("ta", "நான்", "naːn"),          # final virama: no trailing vowel
    ("ta", "தமிழ்", "t̪amiɻ"),       # matra + final virama together
])
def test_conjuncts_and_final_viramas(lang, word, expected):
    assert G2P(lang).transcribe(word) == expected


# ═══════════════════════════════════════════════════════════════════════════
# Script-agnosticism: the properties that let the engine carry no codepoint list
# ═══════════════════════════════════════════════════════════════════════════

def test_every_declared_virama_is_identified_by_its_combining_class():
    # The engine identifies a virama as combining class 9 rather than by
    # enumerating codepoints. That is only sound if it holds for every virama
    # any spec actually declares — if this fails, some script needs a different
    # test, not a longer list.
    checked = 0
    for code in _abugida_codes():
        for g in get(code).graphemes:
            if len(g) != 1:
                continue
            name = unicodedata.name(g, "")
            if "SIGN VIRAMA" in name or "SIGN HALANT" in name or "SIGN PAMAAEH" in name:
                assert _is_virama(g), f"{code}: {name} not detected as a virama"
                checked += 1
    assert checked, "no virama found in any spec — the guard would be vacuous"


def test_no_hardcoded_virama_codepoint_list_in_the_engine():
    # Guards the golden rule: the engine stays language-agnostic. A codepoint
    # list here is the smell that a script was special-cased.
    from pathlib import Path
    import orthography2ipa.phonetok as pt
    src = Path(pt.__file__).read_text()
    body = src[src.index("def _is_virama"):]
    body = body[:body.index("\ndef ", 1)]
    assert "\\u09" not in body and "\\u0B" not in body, \
        "virama detection must not enumerate codepoints"


def test_non_abugida_specs_are_untouched_by_the_inherent_vowel_rule():
    # The rule is gated on spec.inherent_vowel, so a language without one must
    # never grow a vowel. Tokens there always span exactly their grapheme.
    for code in ("pt-PT", "en", "es", "de", "ru", "el"):
        spec = get(code)
        assert spec.inherent_vowel is None
        for tok in PhonetokTokenizer(spec).grapheme_tokens("casa hello"):
            assert tok.length == len(tok.grapheme)


# ═══════════════════════════════════════════════════════════════════════════
# Word reconstruction must not drop the characters a token consumed
# ═══════════════════════════════════════════════════════════════════════════

def test_word_rebuild_preserves_viramas():
    # The engine re-tokenises the words it splits out, so a word rebuilt from
    # grapheme keys alone would silently drop every virama and resurrect the
    # inherent vowels the tokenizer had just suppressed.
    g2p = G2P("ta")
    word = "வணக்கம்"
    rebuilt = [w.surface for w in g2p._split_words(word)]
    assert rebuilt == [word], "virama lost when rebuilding the word"
