"""Cited-claim tests for ``dz`` — Dzongkha, written in the Tibetan script.

Tibetan spelling is historical: the syllable is prefix + superscript + ROOT +
subjoined + vowel + suffix + post-suffix, and most of those letters are not
pronounced. Each test below takes ONE claim the ``dz`` spec makes, quotes it,
and proves it on a word van Driem (1998) or Mazaudon & Michailovsky (1988)
cite themselves — not on a WikiPron gold row — so the rules are validated
against the literature rather than fitted to the 230-row benchmark.

Two engine facts the Tibetan script is the first spec to exercise are tested
in ``tests/test_abugida_conjunct_inherent_vowel.py``.
"""
from __future__ import annotations

import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P


def ipa(word: str) -> str:
    return G2P("dz").transcribe_word(word)


def segments(word: str) -> str:
    """The transcription with the register-tone marks removed."""
    return ipa(word).replace("˥", "").replace("˩", "")


# ═══════════════════════════════════════════════════════════════════════════
# The stack: superscribed, subjoined and prefixed letters
# ═══════════════════════════════════════════════════════════════════════════

def test_subjoined_ya_gives_an_alveolo_palatal_affricate():
    """'⟨ཁྱ⟩ = /t͡ɕʰ/' (dz notes; van Driem 1998 ch. 2)

    ⟨ཁྱོད⟩ 'you' is van Driem's own example of ya-btags: the written velar
    ⟨ཁ⟩ plus subjoined ⟨ྱ⟩ is one alveolo-palatal onset, never *[kʰj].
    """
    assert segments("ཁྱོད").startswith("t͡ɕʰ")


def test_subjoined_ra_gives_a_retroflex():
    """'⟨ཁྲ⟩ = /ʈʰ/' (dz notes; van Driem 1998 ch. 2)

    ⟨ཁྲག⟩ 'blood': ra-btags retroflexes the onset, it is not a cluster.
    """
    assert segments("ཁྲག").startswith("ʈʰ")


def test_subjoined_la_gives_plain_l():
    """'a subjoined letter … maps to a single onset' (dz notes;
    van Driem 1998 ch. 2)

    ⟨ཀླད⟩ 'brain': la-btags leaves only [l] — the written ⟨ཀ⟩ is not read.
    """
    assert segments("ཀླད").startswith("l")


def test_subjoined_ha_under_la_gives_a_lateral_fricative():
    """'⟨ལྷ⟩ = /ɬ/' (dz notes; van Driem 1998 ch. 2)

    ⟨ལྷ⟩ 'deity', the standard example of the voiceless lateral.
    """
    assert segments("ལྷ").startswith("ɬ")


def test_prefixed_letter_is_silent():
    """'PREFIXED letters ⟨ག ད བ མ འ⟩ are silent' (dz notes;
    van Driem 1998 ch. 2)

    ⟨གསུམ⟩ 'three' is [sum]: the written ⟨ག⟩ contributes neither a consonant
    nor a vowel of its own.
    """
    assert segments("གསུམ") == "sum"


def test_silent_prefix_carries_no_inherent_vowel():
    """'Being silent they carry no inherent vowel either.' (dz notes)

    ⟨གཅིག⟩ 'one' is [t͡ɕik]. If the silent ⟨ག⟩ kept the inherent vowel, that
    phantom nucleus would make the ROOT ⟨ཅ⟩ look like a coda and the word
    would lose its own vowel.
    """
    assert segments("གཅིག") == "t͡ɕik"


def test_ga_ya_digraph_is_a_glide_onset():
    """'⟨གཡ⟩ and ⟨དབ⟩ are the two fixed digraphs of the same kind'
    (dz notes; van Driem 1998 ch. 2)

    ⟨གཡག⟩ 'yak' is [jɑk] — the ⟨ག⟩ is a silent prefix, the ⟨ཡ⟩ the root.
    """
    assert segments("གཡག") == "jɑk"


# ═══════════════════════════════════════════════════════════════════════════
# The tsheg
# ═══════════════════════════════════════════════════════════════════════════

def test_tsheg_is_mapped_and_silent():
    """'The TSHEG ⟨་⟩ is a mapped grapheme with an empty realisation.'
    (dz notes)

    ⟨ཐིམ་ཕུ⟩ 'Thimphu' is [tʰimpʰu]: the delimiter adds no segment.
    """
    assert segments("ཐིམ་ཕུ") == "tʰimpʰu"


def test_tsheg_blocks_a_suffix_rule_from_crossing_a_syllable():
    """'mapping it keeps every positional and allophonic context
    syllable-local' (dz notes)

    In ⟨ཨུ་རུ་སུ⟩ 'Russia' each ⟨ར⟩/⟨ས⟩ opens its own syllable. Without the
    tsheg in the grapheme table they would be read as the PRECEDING
    syllable's suffix and deleted, leaving *[uːuːu].
    """
    assert "r" in segments("ཨུ་རུ་སུ") and "s" in segments("ཨུ་རུ་སུ")


# ═══════════════════════════════════════════════════════════════════════════
# Suffixes: umlaut, length, deletion
# ═══════════════════════════════════════════════════════════════════════════

def test_suffix_da_umlauts_and_lengthens_o():
    """'SUFFIXES ⟨ས ད ལ ར⟩ are not realised after a nucleus; they umlaut and
    lengthen it instead (⟨ཁྱོད⟩ [t͡ɕʰøː])' (dz notes; van Driem 1998 ch. 3)
    """
    assert segments("ཁྱོད") == "t͡ɕʰøː"


def test_suffix_sa_lengthens_and_is_deleted():
    """'⟨གཉིས⟩ [ɲiː]' (dz notes; van Driem 1998 ch. 3)

    ⟨གཉིས⟩ 'two': silent prefix ⟨ག⟩, root ⟨ཉ⟩, and the suffix ⟨ས⟩ leaves only
    length behind — no [s] in the output.
    """
    assert segments("གཉིས") == "ɲiː"


def test_suffix_ra_lengthens_the_nucleus():
    """'they umlaut and lengthen it instead' (dz notes; van Driem 1998 ch. 3)

    ⟨གསེར⟩ 'gold' is [seː]: prefix silent, suffix ⟨ར⟩ gone, vowel long.
    """
    assert segments("གསེར") == "seː"


def test_pronounced_codas_survive():
    """'⟨ག ང ན མ བ⟩ stay as codas.' (dz notes; van Driem 1998 ch. 3)"""
    assert segments("གདོང").endswith("oŋ")


def test_post_suffix_sa_is_never_pronounced():
    """'the post-suffix ⟨ས⟩ is never pronounced' (dz notes;
    van Driem 1998 ch. 2)

    ⟨གཟུགས⟩ 'body' has suffix ⟨ག⟩ AND post-suffix ⟨ས⟩; only the ⟨ག⟩ can be
    heard, and the ⟨ས⟩ must not surface as a syllable of its own.
    """
    assert not segments("གཟུགས").endswith("s")


def test_suffix_rule_does_not_reach_a_syllable_initial_letter():
    """Counter-case for the suffix rules: a ⟨ར⟩ that OPENS a syllable is an
    onset, not a suffix. ⟨ཆ་རོགས⟩ 'friend' keeps its [r].
    """
    assert "r" in segments("ཆ་རོགས")


def test_suffix_rule_does_not_reach_a_word_initial_letter():
    """Counter-case: ⟨ལག⟩ 'hand' is [lɑk] — the ⟨ལ⟩ is the root with its
    inherent vowel, and the ⟨ག⟩ its coda. Neither is a suffix to delete.
    """
    assert segments("ལག") == "lɑk"


# ═══════════════════════════════════════════════════════════════════════════
# Register tone
# ═══════════════════════════════════════════════════════════════════════════

def test_voiceless_root_takes_the_high_register():
    """'voiceless root = high ˥' (dz notes; Mazaudon & Michailovsky 1988)

    ⟨ཁ⟩ 'mouth': the root ⟨ཁ⟩ is historically voiceless.
    """
    assert ipa("ཁ") == "kʰɑ˥"


def test_voiced_root_takes_the_low_register():
    """'voiced root = low ˩' (dz notes; Mazaudon & Michailovsky 1988)

    ⟨གཞུང⟩ 'government': the root ⟨ཞ⟩ is historically voiced, so the syllable
    is low even though the ⟨ག⟩ before it is silent.
    """
    assert "˩" in ipa("གཞུང")


def test_tone_is_written_on_the_nucleus():
    """'The register is written on the syllable nucleus' (dz notes)"""
    out = ipa("ཁོ")
    assert out.endswith("˥") and out.index("o") == out.index("˥") - 1


def test_sonorant_root_under_a_superscript_is_high():
    """'A sonorant root under a superscript or a prefix is voiceless and takes
    the high register.' (dz notes; van Driem 1998 §2.4)

    ⟨སྣ⟩ 'nose': a bare ⟨ན⟩ would be low, the superscribed ⟨ས⟩ makes it high.
    """
    assert "˥" in ipa("སྣ") and "˩" in ipa("ན")


def test_register_is_a_two_way_contrast_only():
    """'TONE is a two-way register contrast' (dz notes) — nothing else is
    emitted, in particular no stress mark: Dzongkha is not stress-accented.
    """
    out = "".join(ipa(w) for w in ("ཁ", "གཞུང", "ཁྱོད", "གསུམ"))
    assert set("˥˩") >= {c for c in out if c in "˥˩˦˧˨ˈˌ"}


# ═══════════════════════════════════════════════════════════════════════════
# Consonant series
# ═══════════════════════════════════════════════════════════════════════════

def test_voiced_letters_are_plain_stops_not_voiced_ones():
    """'⟨ག ད བ ཛ⟩ … are phonetically PLAIN (unaspirated) stops in Standard
    Dzongkha' (dz notes; van Driem 1998 §2.2)
    """
    assert segments("གདོང").startswith("t")


def test_the_fricative_letters_keep_their_voicing():
    """'the fricatives ⟨ཞ ཟ⟩ keep their voicing (/ʑ z/)' (dz notes;
    van Driem 1998 §2.2)
    """
    assert segments("གཞུང").startswith("ʑ")
    assert segments("གཟི").startswith("z")


# ═══════════════════════════════════════════════════════════════════════════
# The documented ceiling
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.xfail(strict=True, reason=(
    "dz notes, KNOWN CEILING: a two-letter syllable with no written vowel is "
    "structurally ambiguous — ⟨དང⟩ is root+suffix [tɑŋ] but is read as "
    "prefix+root, because the engine resolves letters left to right and cannot "
    "look at the whole syllable first"
))
def test_two_letter_syllable_is_read_as_root_plus_suffix():
    """'⟨དང⟩ is root+suffix [tɑŋ]' (dz notes; van Driem 1998 ch. 2)"""
    assert segments("དང") == "tɑŋ"


# ═══════════════════════════════════════════════════════════════════════════
# Spec hygiene
# ═══════════════════════════════════════════════════════════════════════════

def test_no_grapheme_key_carries_a_dotted_circle():
    """U+25CC is a rendering placeholder shown around a combining mark in
    print, never a character of the text. A key spelt with one can never
    match, which is how the four Tibetan vowel signs were silently dead.
    """
    assert not [k for k in get("dz").graphemes if "◌" in k]


def test_every_allophone_rule_cites_a_source():
    for rule in get("dz").allophone_rules:
        assert rule.notes, rule.id
        assert ("van Driem" in rule.notes
                or "Mazaudon" in rule.notes), rule.id
