"""The pluggable steps, and who gets to select one.

    The transcription is a function of the SPEC, the INPUT, and the CALLER'S
    EXPLICIT CONFIG. Never of what happens to be installed.

The danger was never "a plugin changed the output". It was "*pip install* changed
the output". An explicit choice — by the spec, or by the caller in code — is a
declaration anyone can read. Discovery alone is never allowed to decide.
"""
import pytest

from orthography2ipa import get, registry
from orthography2ipa.g2p import G2P
from orthography2ipa.plugins import (
    NormalizePlugin, OUTPUT_CHANGING_STAGES, STAGES, SandhiPlugin,
)
from orthography2ipa.registry import MissingPlugin


class _Diacritizer(NormalizePlugin):
    """Stands in for text2tashkeel: puts the vowels back before anything reads."""

    def normalize(self, text, lang):
        return {"كتب": "كَتَبَ"}.get(text, text)

    @property
    def language_codes(self):
        return ["ar"]


class _NunAssimilation(SandhiPlugin):
    """Stands in for arbtok's cross-word layer: min + rabbihim -> mir rabbihim."""

    def apply(self, words, surfaces, pausal, lang):
        out = list(words)
        for i, ipa in enumerate(out[:-1]):
            if ipa.endswith("n") and out[i + 1][:1] == "r":
                out[i] = ipa[:-1] + "r"
        return out

    @property
    def language_codes(self):
        return ["ar"]


@pytest.fixture
def registered(monkeypatch):
    """Install the plugins — WITHOUT declaring them."""
    monkeypatch.setitem(registry._declared, "normalize", {"diacritizer": _Diacritizer()})
    monkeypatch.setitem(registry._declared, "sandhi", {"nun": _NunAssimilation()})


# ─── installed is not selected ──────────────────────────────────────────

def test_installing_a_plugin_does_not_select_it(registered):
    """The safeguard. An output-changing plugin runs because something NAMED it."""
    assert G2P("ar").transcribe("كتب") == "ˈktb"   # undiacritized: no vowels to read


# ─── the caller names it — how a downstream engine works ────────────────

def test_the_caller_can_name_it(registered):
    """arbtok does not edit this library's shipped ar.json to say it wants a
    diacritizer. It passes one, because IT is the thing that decided."""
    engine = G2P("ar", plugins={"normalize": "diacritizer"})
    assert engine.transcribe("كتب") == "ˈkataba"


def test_a_downstream_engine_composes_several_stages(registered):
    """A rich engine picks the steps it wants: diacritize, then cross-word."""
    engine = G2P("ar", plugins={"normalize": "diacritizer", "sandhi": "nun"})
    assert engine.transcribe("كتب") == "ˈkataba"
    assert engine.plugins["normalize"] == ("diacritizer",)
    assert engine.plugins["sandhi"] == ("nun",)


# ─── a named plugin that is missing is FATAL ────────────────────────────

def test_a_named_plugin_that_is_missing_is_fatal():
    """Never a quiet fallback. A quiet fallback is how you get two transcriptions
    for one word and no way to know which one you got."""
    with pytest.raises(MissingPlugin, match="not installed"):
        G2P("ar", plugins={"normalize": "nope"}).transcribe("كتب")


def test_the_error_says_what_it_wanted_and_what_it_found(registered):
    with pytest.raises(MissingPlugin) as exc:
        G2P("ar", plugins={"normalize": "nope"}).transcribe("كتب")
    assert "nope" in str(exc.value)
    assert "diacritizer" in str(exc.value)   # what IS installed


# ─── the taxonomy itself ────────────────────────────────────────────────

def test_syllabify_is_the_only_undeclared_stage():
    """Because it is the only one that must not change the transcription."""
    assert set(STAGES) - set(OUTPUT_CHANGING_STAGES) == {"syllabify"}


def test_no_shipped_spec_names_a_plugin():
    """orthography2ipa transcribes on its own. A spec should only name a plugin
    when the language is not transcribable without it — and the `ar` spec must NOT
    name a diacritizer, because this library's input contract IS diacritized text
    and it ships no weights. The engine decides the pipeline; the spec describes
    the language."""
    from orthography2ipa import available_codes
    named = [c for c in available_codes() if get(c).plugins]
    assert named == []


# ─── the pause has to be HANDED to the plugin ───────────────────────────

class _PausalDropsTheEnding(SandhiPlugin):
    """A word at a pause loses its case ending. It cannot find the pause itself."""

    seen: list = []

    def apply(self, words, surfaces, pausal, lang):
        type(self).seen = list(pausal)
        return [
            w[:-2] if at_pause and w.endswith("un") else w
            for w, at_pause in zip(words, pausal)
        ]

    @property
    def language_codes(self):
        return ["ar"]


def test_a_sandhi_plugin_is_told_where_the_pause_is(monkeypatch):
    """Punctuation is stripped during word splitting, so by the time a plugin sees
    the words the pause is GONE from the input — and a pause is exactly what
    removes a case ending. It has to be handed over, not inferred.

    Found by the first real consumer: arbtok's cross-word layer silently did
    nothing, because it could not tell that the utterance had ended.
    """
    monkeypatch.setitem(
        registry._declared, "sandhi", {"pausal": _PausalDropsTheEnding()})

    engine = G2P("ar", plugins={"sandhi": "pausal"})
    out = engine.transcribe("قَلَمٌ")

    assert _PausalDropsTheEnding.seen == [True]     # the last word IS at a pause
    assert out.endswith("qalam")                    # …so the ending goes
