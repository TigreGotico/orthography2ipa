"""The emitted symbol set is closed, enumerable, and free of dead rules.

A neural TTS frontend builds its embedding table from the phoneme inventory
before training. A symbol the phonemizer can emit but nobody enumerated has no
embedding, and the word carrying it is mispronounced permanently and silently.
So "what can this spec emit?" must have an exact answer, and transcription must
never step outside it.
"""
import pytest

from orthography2ipa import available_codes, get
from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import (
    dead_allophone_rules, emission_inventory, phoneme_inventory, tokenize,
)

ALL_CODES = sorted(available_codes())

#: Specs whose transcription is exercised against the closure invariant. The
#: sweep runs over every spec; these carry a lexicon worth transcribing.
SAMPLE_WORDS = {
    "ar": ["كِتَاب", "قَهْوَة", "مَدْرَسَة", "صَبْر", "الشَّمْس", "بَيْت"],
    "ar-SA-x-najd": ["كِتَاب", "قَهْوَة", "لَحْم", "قَلَم"],
    "ar-SA-x-hejaz": ["بَيْت", "قَلَم", "كِتَاب"],
    "en": ["hello", "world", "phoneme"],
    "pt": ["coelho", "palavra"],
    "es": ["hola", "mundo"],
}


# ─── the closure invariant ──────────────────────────────────────────────

@pytest.mark.parametrize("code", sorted(SAMPLE_WORDS))
def test_transcription_never_leaves_the_inventory(code):
    """Nothing transcription emits may fall outside the declared token set."""
    spec = get(code)
    tokens = phoneme_inventory(spec)
    g2p = G2P(code)

    for word in SAMPLE_WORDS[code]:
        ipa = g2p.transcribe(word)
        for token in tokenize(ipa, spec):
            assert token in tokens, (
                f"{code}: transcribing {word!r} emitted {token!r}, which is "
                f"outside the phoneme inventory"
            )


@pytest.mark.parametrize("code", ALL_CODES)
def test_inventory_is_derivable_for_every_spec(code):
    """Every spec can answer 'what can you emit?' without raising."""
    spec = get(code)
    emissions = emission_inventory(spec)
    tokens = phoneme_inventory(spec)
    assert "" not in emissions, "a deleted slot is the absence of a symbol"
    assert "" not in tokens
    # A spec with graphemes must be able to emit something.
    if spec.graphemes:
        assert emissions, f"{code} has graphemes but emits nothing"


@pytest.mark.parametrize("code", ALL_CODES)
def test_every_allophone_surface_is_in_the_inventory(code):
    """A rule's surface is a symbol the engine can emit, so it must be counted.

    This is the invariant that actually bites: an allophone rule is a *new*
    source of IPA (Najdi's [ts] exists nowhere in the grapheme table), so an
    inventory derived only from the graphemes would miss it — and a TTS trained
    on that inventory would have no embedding for the affricate it is about to
    be asked to say.
    """
    spec = get(code)
    emissions = emission_inventory(spec)
    for rule in (spec.allophone_rules or ()):
        if rule.surface:
            assert rule.surface in emissions


def test_a_rule_only_surface_is_counted():
    """Najdi's affricate comes from a rule, not the grapheme table."""
    najd = get("ar-SA-x-najd")
    assert "ts" not in {r for readings in najd.graphemes.values() for r in readings}
    assert "ts" in emission_inventory(najd)
    assert "ts" in phoneme_inventory(najd)


def test_stress_is_its_own_token():
    """Prosody is not a phoneme: ˈ modifies a syllable, not the vowel after it.

    The generic IPA segmenter treats a spacing modifier as part of the preceding
    character, which would make `ɐˈ` a "phoneme" — in no inventory, and a symbol
    a model would have to learn separately from `ɐ`.
    """
    spec = get("pt")
    tokens = tokenize(G2P("pt").transcribe("palavra"), spec)
    assert "ˈ" in tokens
    assert not any(t != "ˈ" and "ˈ" in t for t in tokens)


def test_multi_character_segments_stay_whole():
    """[ts] is one token, not t + s — the affricate is declared, so it holds."""
    assert "ts" in phoneme_inventory(get("ar-SA-x-najd"))
    assert "aː" in phoneme_inventory(get("ar"))


# ─── the dead-rule lint ─────────────────────────────────────────────────

#: Specs carrying allophone rules whose target phoneme they cannot produce, so
#: the rule can never fire. Each is a real bug — a rule written against a symbol
#: the spec does not use — and each needs a language owner to say what the rule
#: *should* target, which is not a mechanical fix. Listed rather than skipped so
#: they stay visible, and so no NEW dead rule can be added without failing here.
KNOWN_DEAD_RULES = {
    # Maltese inherits the Arabic allophone rules wholesale but emits neither
    # the long vowels they target (/aː/, /iː/, /uː/) nor their environments, so
    # the whole inherited family is unreachable there.
    "mt": {
        "AR_EMPH_BACK_AA_AFTER", "AR_EMPH_BACK_AA_BEFORE",
        "AR_GLIDE_YA_BEFORE_GEMINATE", "AR_GLIDE_YA_GEMINATE_COPY",
        "AR_GLIDE_YA_CONSONANTAL", "AR_GLIDE_WAW_CONSONANTAL",
    },
    # Targets /ɪ/, which these specs never emit.
    "pt-BR-x-pr": {"BR_RAISE_FINAL_E"},
    "pt-BR-x-sul": {"BR_RAISE_FINAL_E"},
    # Dead only because the spec inherits a grapheme table without its
    # positional readings, so the vowel the rule targets is never emitted.
    # Fixed by the positional-inheritance default in #348, which revives it.
    "da-x-copenhagen": {"DA_SHORTEN_A"},
}

#: The Dravidian gemination families target whole CV emissions (``dʒa``, ``kʂa``)
#: that no slot carries, so the whole family is unreachable. A systematic bug in
#: one rule generator rather than 45 independent ones — allowed by prefix so the
#: group is visible and so a *new* dead rule outside it still fails.
KNOWN_DEAD_PREFIXES = {"ta": ("TA_GEM",), "ml": ("TA_GEM",)}


@pytest.mark.parametrize("code", ALL_CODES)
def test_no_new_dead_allophone_rules(code):
    """A rule targeting a phoneme the spec cannot produce can never fire."""
    dead = set(dead_allophone_rules(get(code)))
    known = KNOWN_DEAD_RULES.get(code, set())
    prefixes = KNOWN_DEAD_PREFIXES.get(code, ())
    unexplained = {
        rule_id for rule_id in dead - known
        if not (prefixes and rule_id.startswith(prefixes))
    }
    assert not unexplained, (
        f"{code}: new dead allophone rules {sorted(unexplained)} — the target "
        f"phoneme is not in this spec's inventory, so the rule can never fire"
    )
