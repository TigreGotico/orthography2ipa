"""Netherlands Dutch is one spec, keyed ``nl-NL``.

Every living spec carries an explicit region subtag, and the bare code is an
alias. A bare tag names its motherland, and for Dutch that is the
Netherlands. So ``nl``, ``nld`` (ISO 639-3) and ``dut`` (ISO 639-2/B) resolve
exactly to ``nl-NL``, the spec that holds the Dutch tables, stress block and
rules. The Dutch varieties and daughter languages take it as their parent.

The forms below follow the rules the spec cites: initial stress, the tense
vowel of an open syllable and the lax vowel of a closed one (Booij, *The
Phonology of Dutch*, 1995, ch. 2; Gussenhoven, "Dutch", *Handbook of the
IPA*, 1999), [ə] for an unstressed ⟨e⟩, the short tense high vowels of
⟨ie⟩ (same sources), the uvular [χ] of ⟨g⟩ and ⟨sch⟩ (Gussenhoven,
"Dutch", *JIPA* 22, 1992, p. 45), and final devoicing (Booij 1995, § 2.5).
"""
import json
from pathlib import Path

import pytest

from orthography2ipa import G2P, get
from orthography2ipa.registry import resolve, resolves_exactly

DATA = Path(__file__).parents[1] / "orthography2ipa" / "data"


@pytest.mark.parametrize("tag", [
    "nl", "nld", "dut", "nl-NL", "nl_NL", "nl-nl", "NL", "nl-Latn",
    "nl-Latn-NL",
])
def test_every_dutch_tag_names_the_netherlands_spec_exactly(tag):
    assert resolve(tag) == "nl-NL"
    assert resolves_exactly(tag)


@pytest.mark.parametrize("tag", ["nl-SR", "nl-AW", "nl-CW", "nl-DE"])
def test_a_dutch_region_with_no_spec_falls_to_the_standard(tag):
    assert resolve(tag) == "nl-NL"


def test_belgian_dutch_keeps_its_own_spec():
    assert resolve("nl-BE") == "nl-BE"
    assert resolve("nl-be") == "nl-BE"


@pytest.mark.parametrize("code", ["nl-BE", "af", "vls"])
def test_the_dutch_varieties_take_the_standard_as_parent(code):
    assert get(code).parent == "nl-NL"


def test_belgian_dutch_reads_the_standard_tables():
    raw = json.loads((DATA / "nl-BE.json").read_text(encoding="utf-8"))
    assert raw["graphemes_base"] == "nl-NL"
    assert raw["allophones_base"] == "nl-NL"


def test_no_spec_names_the_bare_dutch_code():
    """``nl`` is an alias. A spec that names it as parent, table base or
    ancestor would point at a key with no file."""
    named = {}
    for path in sorted(DATA.glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        refs = [raw.get(k) for k in raw if k == "parent" or k.endswith("_base")]
        refs += [a.get("code") for a in raw.get("ancestors") or ()]
        if "nl" in refs:
            named[path.stem] = refs
    assert named == {}


@pytest.mark.parametrize("word,ipa", [
    ("geven", "ˈχeːvən"),     # open ge-: tense [eː]; unstressed ⟨e⟩ [ə]
    ("water", "ˈʋaːtər"),     # open wa-: tense [aː]
    ("liegen", "ˈliχən"),     # ⟨ie⟩ tense but short [i]
    ("schip", "ˈsχɪp"),       # ⟨sch⟩ [sχ]; closed syllable: lax [ɪ]
    ("hond", "ˈɦɔnt"),        # final devoicing
])
@pytest.mark.parametrize("tag", ["nl-NL", "nl", "nld", "dut"])
def test_every_dutch_tag_reads_the_cited_standard(tag, word, ipa):
    assert G2P(tag).transcribe(word) == ipa
