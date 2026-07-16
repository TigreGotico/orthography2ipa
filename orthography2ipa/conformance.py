"""What a plugin is allowed to change — and the kit that proves it doesn't.

A plugin exists so an external tool can **improve one language by improving one
clearly-defined step**. Not by forking the engine, not by wrapping it — by
answering *one question* better than the built-in answer.

Everything hard about the plugin system follows from one sentence:

    **A plugin refines an answer. It must not redefine the question.**

That sounds obvious. It was not enforced, and the consequence was live in this
library:

    coelho, with a syllabifier plugin installed:  ˈkuɐʎu
            without one:                          ˈkoɐʎu

The same word, the same spec, two transcriptions — decided by whether an optional
package happened to be in the environment. The plugin returned a *better*
syllabification, which changed the syllable **count**, which moved the **stress**,
which changed the **vowel reduction** that stress conditions.

Every one of those steps was working as designed. The bug was that nothing said a
plugin may not do that.

## The contract

1. **Round-trip.** A syllabifier splits a word; it does not rewrite it.
   ``"".join(syllabify(word)) == word``, always.
2. **Language claim.** A plugin speaks only for the codes it claims.
3. **Downstream neutrality.** *Installing a plugin must not change any stage the
   plugin does not own.* Transcribe a corpus with the plugin and without it: the
   output must be identical.

Rule 3 is the one that was missing, and it is the one that matters. Note what it
implies, because it is not a restriction on plugins so much as a demand on the
library:

    **If a better syllabification moves the stress, the syllable count is
    load-bearing for stress — and that is a bug in the BUILT-IN answer, not a
    feature of the plugin.**

A plugin that cannot pass rule 3 is not a bad plugin. It is a plugin telling you
that the built-in answer is wrong. Fix the built-in answer; the plugin should then
pass unchanged. (That is exactly how the ``coelho`` case was resolved: ``pt-PT``
now declares its diphthongs, the bundled syllabifier separates the hiatus itself,
and the plugin — still better at drawing boundaries — no longer moves anything.)

## Using it

A plugin author runs this in their own CI, against their own plugin::

    from orthography2ipa.conformance import assert_syllabifier_conforms

    def test_conforms():
        assert_syllabifier_conforms(MySyllabifier())

It will tell them, in words, which rule they broke and what it means.
"""

from __future__ import annotations

from typing import List, Optional, Sequence

from orthography2ipa import registry
from orthography2ipa.g2p import G2P
from orthography2ipa.syllabifier_plugin import SyllabifierPlugin

__all__ = [
    "assert_syllabifier_conforms",
    "ConformanceError",
    "DEFAULT_PROBE_WORDS",
]


class ConformanceError(AssertionError):
    """A plugin broke the contract. The message says which rule, and why it matters."""


#: Words used when the caller supplies none. Deliberately awkward: hiatus, real
#: diphthongs, written accents, a long word, a clitic-looking one. A plugin that
#: only ever sees ``casa`` proves nothing.
DEFAULT_PROBE_WORDS: List[str] = [
    "coelho", "viagem", "moeda", "poeta", "saudade", "ciência",
    "mãe", "pão", "coisa", "hoje", "paralelepípedo", "água",
]


def _check_round_trip(plugin: SyllabifierPlugin, words: Sequence[str]) -> None:
    for word in words:
        syllables = plugin.syllabify(word)
        if "".join(syllables) != word:
            raise ConformanceError(
                f"round-trip: syllabifying {word!r} gave {syllables!r}, which joins "
                f"back to {''.join(syllables)!r}.\n\n"
                f"A syllabifier SPLITS a word. It does not rewrite it — normalising, "
                f"stripping an accent or fixing a spelling here means every stage "
                f"downstream is working on a different word than the caller passed."
            )


def _check_language_claim(plugin: SyllabifierPlugin) -> None:
    codes = list(plugin.language_codes)
    if not codes:
        raise ConformanceError(
            "language claim: the plugin claims no language codes, so discovery can "
            "never route anything to it. It would be installed and never called."
        )


def _check_downstream_neutrality(
    plugin: SyllabifierPlugin,
    words: Sequence[str],
    lang: str,
) -> None:
    """The rule that matters: installing the plugin must not move the answer."""
    saved = registry._syllabifiers

    try:
        # Register under the claimed codes AND the code under test: a plugin that
        # claims `pt-PT` is meant to serve `pt-PT-x-lisbon` too, and the check is
        # about the plugin's effect, not about code resolution.
        codes = {*plugin.language_codes, lang}
        registry._syllabifiers = {code: plugin for code in codes}
        with_plugin = {w: G2P(lang).transcribe_word(w) for w in words}

        registry._syllabifiers = {}
        without_plugin = {w: G2P(lang).transcribe_word(w) for w in words}
    finally:
        registry._syllabifiers = saved

    moved = {
        w: (without_plugin[w], with_plugin[w])
        for w in words
        if without_plugin[w] != with_plugin[w]
    }
    if not moved:
        return

    detail = "\n".join(
        f"    {w}:  without the plugin {before!r}   with it {after!r}"
        for w, (before, after) in sorted(moved.items())
    )
    raise ConformanceError(
        f"downstream neutrality: installing this plugin CHANGES THE TRANSCRIPTION "
        f"for {lang}:\n\n{detail}\n\n"
        f"A plugin may answer a question better. It may not change what the question "
        f"was. If a better syllabification moves the stress, then the syllable count "
        f"is load-bearing for stress — and that is a bug in the BUILT-IN answer, not "
        f"a feature of this plugin.\n\n"
        f"So this is probably not your bug. It is orthography2ipa telling you that "
        f"its own syllabifier is wrong for {lang} and that the spec is leaning on it. "
        f"Fix the spec (a missing `diphthongs` list is the usual cause — see pt-PT), "
        f"and this plugin should pass unchanged."
    )


def assert_syllabifier_conforms(
    plugin: SyllabifierPlugin,
    words: Optional[Sequence[str]] = None,
    lang: Optional[str] = None,
) -> None:
    """Assert *plugin* keeps the syllabifier contract, or explain what it broke.

    Args:
        plugin: the syllabifier to check.
        words: probe words. Defaults to :data:`DEFAULT_PROBE_WORDS`; a plugin
            author should pass their own language's awkward cases — hiatus, real
            diphthongs, written accents.
        lang: the code to transcribe under. Defaults to the plugin's first claim.
    """
    words = list(words or DEFAULT_PROBE_WORDS)
    lang = lang or next(iter(plugin.language_codes), None)
    if lang is None:
        raise ConformanceError("the plugin claims no language codes")

    _check_language_claim(plugin)
    _check_round_trip(plugin, words)
    _check_downstream_neutrality(plugin, words, lang)


# ═══════════════════════════════════════════════════════════════════════════
# Rescorer plugins — a different contract, because they have a different job
# ═══════════════════════════════════════════════════════════════════════════
#
# A syllabifier must NOT change the transcription. A rescorer exists to change
# it. So the neutrality rule is inverted, and what remains to enforce is the
# damage a rescorer can do that nobody would notice:
#
#   * speaking for a language it did not claim;
#   * emitting a symbol the spec never declared — invisible in a diff, fatal in a
#     TTS embedding table, where an unenumerated symbol has no vector and the word
#     carrying it is mispronounced permanently and silently;
#   * being non-deterministic, which is not a transcription at all.


def assert_rescorer_conforms(
    plugin,
    words: Optional[Sequence[str]] = None,
    lang: Optional[str] = None,
) -> None:
    """Assert a rescorer plugin keeps its contract.

    It MAY change the transcription — that is what it is for. It may not invent a
    symbol, wander into another language, or answer differently twice.
    """
    from orthography2ipa import get
    from orthography2ipa.inventory import phoneme_inventory, tokenize

    lang = lang or next(iter(plugin.language_codes), None)
    if lang is None:
        raise ConformanceError("the plugin claims no language codes")
    words = list(words or DEFAULT_PROBE_WORDS)

    spec = get(lang)
    declared = phoneme_inventory(spec)

    # Declared, not discovered. A rescorer changes the transcription, so it only
    # ever runs because something NAMED it — here, the caller, which is exactly how
    # a downstream engine composes its own pipeline.
    saved = registry._declared.get("rescore")
    try:
        registry._declared["rescore"] = {"__conformance__": plugin}
        engine = G2P(lang, plugins={"rescore": "__conformance__"})
        first = {w: engine.transcribe_word(w) for w in words}
        second = {
            w: G2P(lang, plugins={"rescore": "__conformance__"}).transcribe_word(w)
            for w in words
        }
    finally:
        if saved is None:
            registry._declared.pop("rescore", None)
        else:
            registry._declared["rescore"] = saved

    unstable = {w: (first[w], second[w]) for w in words if first[w] != second[w]}
    if unstable:
        raise ConformanceError(
            f"determinism: this rescorer gives different answers for the same word "
            f"on two runs — {unstable!r}. A transcription that varies run to run is "
            f"not a transcription."
        )

    escaped = {}
    for word, ipa in first.items():
        outside = [t for t in tokenize(ipa, spec) if t not in declared]
        if outside:
            escaped[word] = outside
    if escaped:
        raise ConformanceError(
            f"inventory: this rescorer emits symbols the {lang} spec never "
            f"declares — {escaped!r}.\n\n"
            f"That is invisible in a diff and fatal downstream: a TTS frontend "
            f"builds its embedding table from the declared inventory BEFORE "
            f"training, so a symbol that appears only at inference has no vector, "
            f"and every word carrying it is mispronounced permanently and silently.\n\n"
            f"A new symbol is a claim about the phonology. Declare it in the spec, "
            f"where it can be read, cited and diffed — not at runtime."
        )
