"""Abugida dependent-vowel predicates for the Tai scripts (Lao, Thai).

Two gaps in the abugida inherent-vowel model (see ``tests/test_abugida.py``)
that Devanagari and friends never exercise, because they never occur there:

1. ``_supplies_vowel`` gates on Unicode general category Mn/Mc (combining
   mark) to decide whether a dependent vowel sign follows a consonant. Thai
   and Lao's SPACING dependent vowel signs (⟨า⟩/⟨າ⟩, ⟨ะ⟩/⟨ະ⟩ and kin) are
   Unicode category Lo — plain spacing letters — so the category gate
   misses them and the inherent vowel wrongly surfaces on top:
   ⟨กา⟩ -> *[kao] instead of [kaː]. ``LanguageSpec.dependent_vowels`` is the
   data-driven escape hatch (see its docstring in ``types.py``).

2. Thai/Lao write some dependent vowels BEFORE the consonant they attach to,
   but pronounce them after: ⟨เก⟩ = /keː/, not */eːk/.
   ``LanguageSpec.preposed_vowels`` names the graphemes this applies to; the
   tokenizer folds the vowel's reading into the following consonant's IPA
   and leaves the vowel token silent, so token list order (and therefore
   every position-dependent consumer downstream — surface reconstruction,
   stress, span reporting) stays in TEXT order. See the preposed-vowel
   branch of ``PhonetokTokenizer.tokenize``.

A known, separate, OUT-OF-SCOPE gap these tests do not attempt to fix: a
bare word-final consonant with nothing after it (no dependent vowel, no
virama) still gets the inherent vowel from the general abugida rule, which
is correct for Devanagari/Tamil/Kannada's schwa but wrong for Thai/Lao's
unmarked closed-syllable convention (⟨ลาว⟩ 'Laos' -> "laːwo" rather than
"laːw": the coda ⟨ว⟩ gets a spurious inherent vowel). Devanagari-style
abugidas mark a "dead" final consonant with an explicit virama; Thai/Lao do
not write one for an ordinary closed monosyllable, so nothing in the
inherent-vowel test (which only ever looks at the *next* character) can
tell "coda of this syllable" from "bare consonant, fresh syllable" without
a third, syllable-boundary-aware mechanism. That is a real, further defect
but a different one from the two this module fixes; it is not silently
worked around here.
"""
from __future__ import annotations

import unicodedata

import pytest

from orthography2ipa import G2P, get
from orthography2ipa.phonetok import PhonetokTokenizer


# ═══════════════════════════════════════════════════════════════════════════
# 1. dependent_vowels: category-Lo dependent vowel signs
# ═══════════════════════════════════════════════════════════════════════════

def test_thai_postposed_sign_is_category_lo_not_a_combining_mark():
    # The whole point of the escape hatch: prove the codepoint really is
    # outside Mn/Mc, so the category gate genuinely needed a bypass.
    assert unicodedata.category("า") == "Lo"
    assert unicodedata.category("າ") == "Lo"


def test_lo_declares_dependent_vowels_covering_its_lo_category_signs():
    spec = get("th")
    assert "า" in spec.dependent_vowels
    spec_lo = get("lo")
    assert "າ" in spec_lo.dependent_vowels


def test_postposed_dependent_vowel_cancels_the_inherent_vowel_thai():
    # กา = ก + า. Without the fix ก keeps its inherent /o/: *[kao].
    tokens = PhonetokTokenizer(get("th")).grapheme_tokens("กา")
    assert tokens[0].ipa[0] == "k", "inherent vowel not cancelled by ⟨า⟩"
    assert G2P("th").transcribe("กา") == "kaː"


def test_postposed_dependent_vowel_cancels_the_inherent_vowel_lao():
    # ລາ = ລ + າ.
    tokens = PhonetokTokenizer(get("lo")).grapheme_tokens("ລາ")
    assert tokens[0].ipa[0] == "l", "inherent vowel not cancelled by ⟨າ⟩"
    assert G2P("lo").transcribe("ລາ") == "laː"


def test_mn_category_thai_lao_vowel_signs_already_worked_without_the_list():
    # ⟨ิ⟩/⟨ິ⟩ etc. are Mn already — the pre-existing category gate handles
    # them. dependent_vowels only needed to cover the Lo-category signs.
    assert unicodedata.category("ิ") == "Mn"
    assert G2P("th").transcribe("กิ") == "ki"


# ═══════════════════════════════════════════════════════════════════════════
# 2. preposed_vowels: written before the consonant, read after it
# ═══════════════════════════════════════════════════════════════════════════

def test_thai_lao_declare_preposed_vowels():
    assert set(get("th").preposed_vowels) == {"เ", "แ", "โ", "ใ", "ไ"}
    assert set(get("lo").preposed_vowels) == {"ເ", "ແ", "ໂ", "ໃ", "ໄ"}


def test_preposed_vowel_token_is_silent_and_stays_in_text_order():
    # Token LIST order must stay text order (vowel token first, at its true
    # position) — only the IPA content moves. This is what keeps surface
    # reconstruction (g2p._group_words) and every other position-dependent
    # consumer working unmodified.
    tokens = PhonetokTokenizer(get("th")).tokenize("เก")
    g_tokens = [t for t in tokens if t.grapheme]
    assert [t.grapheme for t in g_tokens] == ["เ", "ก"]
    assert g_tokens[0].ipa == (), "the preposed vowel token must be silent"
    assert g_tokens[0].position == 0
    assert g_tokens[1].position == 1
    assert g_tokens[1].ipa[0] == "keː", (
        "the consonant's IPA must carry the vowel's reading AFTER its own"
    )


@pytest.mark.parametrize("lang,word,expected", [
    ("th", "เก", "keː"),
    ("th", "เด", "deː"),
    ("lo", "ເມ", "meː"),
])
def test_preposed_vowel_reads_consonant_before_vowel(lang, word, expected):
    assert G2P(lang).transcribe(word) == expected


def test_word_rebuild_preserves_preposed_vowel_order():
    # The engine re-tokenises the words it splits out (see
    # test_abugida.test_word_rebuild_preserves_viramas for the Indic
    # analogue); the surface must round-trip exactly even though the vowel
    # is written before the consonant it modifies.
    g2p = G2P("th")
    word = "เก"
    rebuilt = [w.surface for w in g2p._split_words(word)]
    assert rebuilt == [word], "preposed vowel order lost when rebuilding the word"


def test_preposed_vowel_with_nothing_following_falls_back_to_its_own_reading():
    # Two preposed vowels or a preposed vowel at the very end of input: no
    # consonant to fold into, so it reads as itself rather than vanishing.
    tokens = PhonetokTokenizer(get("th")).grapheme_tokens("เ")
    assert tokens[0].ipa[0] == "eː"


# ═══════════════════════════════════════════════════════════════════════════
# Circumfix vowels: preposed + postposed halves are ONE phonemic unit
# ═══════════════════════════════════════════════════════════════════════════

def test_lao_circumfix_vowel_is_one_orthographic_unit():
    # ເສືອ 'tiger' = ເ (preposed half) + ສ (consonant) + ືອ (postposed
    # half). Together ເ...ືອ spell /ɯa/ as ONE vowel (Enfield 2007); ⟨ືອ⟩
    # is declared as a genuine multigraph (real circumfix vowel, sanctioned
    # by the repo's three-test rule), not a C×V enumeration product — it
    # supplies the WHOLE nucleus, and the preposed ⟨ເ⟩ contributes nothing
    # of its own so the vowel is not doubled (*/seːɯa/).
    tokens = PhonetokTokenizer(get("lo")).tokenize("ເສືອ")
    g_tokens = [t for t in tokens if t.grapheme]
    assert [t.grapheme for t in g_tokens] == ["ເ", "ສ", "ືອ"]
    assert g_tokens[0].ipa == (), "preposed half of a circumfix must be silent"
    assert g_tokens[1].ipa[0] == "s"
    assert g_tokens[2].ipa[0] == "ɯa"
    assert G2P("lo").transcribe("ເສືອ") == "sɯa"


# ═══════════════════════════════════════════════════════════════════════════
# Non-regression: Devanagari and friends are untouched
# ═══════════════════════════════════════════════════════════════════════════

def test_devanagari_matra_cancellation_unaffected_by_the_lo_category_escape_hatch():
    # का already worked (Mn matra) before dependent_vowels existed; an
    # escape hatch that no Indic spec declares must not change its result.
    spec = get("hi")
    assert spec.dependent_vowels == ()
    assert spec.preposed_vowels == ()
    tokens = PhonetokTokenizer(spec).grapheme_tokens("का")
    assert tokens[0].ipa[0] == "k"
    assert G2P("hi").transcribe("का") == "kaː"


def test_vocalic_r_nucleus_regression_guard_kr1shna():
    # The exact regression pinned in test_abugida.py's docstring history:
    # कृष्ण must stay kr̩ʂɳ-ish, not gain a spurious inherent vowel via any
    # side effect of the new escape hatches.
    assert G2P("hi").transcribe("कृष्ण") == "kɾɪʂɳ"


def test_non_thai_lao_specs_declare_no_dependent_or_preposed_vowels():
    for code in ("hi", "ta", "kn", "ml", "pt-PT", "en"):
        spec = get(code)
        assert spec.dependent_vowels == ()
        assert spec.preposed_vowels == ()


class TestSilentSlotLatticeContract:
    """The lattice contract reserves empty candidates for deletion: a
    silenced preposed vowel must be omitted from the public lattice, so
    ``slot.top`` stays total and confidence never zeroes on the words the
    mechanism fixes (adversarial-review regression pins)."""

    def test_no_empty_candidate_slots_in_lattice(self):
        from orthography2ipa import G2P
        for lang, word in (("th", "เก"), ("lo", "ເສືອ"), ("th", "แมว")):
            for slot in G2P(lang).ipa_lattice(word):
                assert slot.candidates, (lang, word, slot.grapheme)
                assert slot.top.ipa  # .top must never raise

    def test_word_confidence_positive_for_preposed_words(self):
        from orthography2ipa import G2P
        assert G2P("th").word_confidence("เก") > 0.0
        assert G2P("lo").word_confidence("ເສືອ") > 0.0

    def test_tokenizer_lattice_matches_contract_too(self):
        from orthography2ipa import get
        from orthography2ipa.phonetok import PhonetokTokenizer
        tok = PhonetokTokenizer(get("th"))
        lat = tok.ipa_lattice("เก")
        assert all(s.candidates for s in lat)
        assert "".join(s.top.ipa for s in lat) == "keː"
