"""grammatical_endings — morpheme-aware word-ending realisations.

Two phenomena motivate the mechanism:

* **French mute ⟨-er⟩ / ⟨-ez⟩.** Word-final ⟨-er⟩ of the infinitive and of
  agent nouns is [e] (``parler``, ``boulanger``), and ⟨-ez⟩ of the 2pl is
  likewise [e] (``mangez``, and the frozen ``nez``/``chez``/``assez``).
  The mute reading belongs to the *grammatical ending*, not to the letter
  sequence — ⟨er⟩ inside a word (``personne``, ``version``) is untouched,
  and the closed set of nouns that keep /ɛʁ/ (``mer``, ``hiver``) stays in
  ``word_exceptions`` (Fouché 1959; Tranel 1987 §3 on final-consonant
  elision in grammatical endings).
* **English suffix palatalization.** ⟨-tion⟩ → /ʃən/, ⟨-cious⟩ → /ʃəs/,
  ⟨-tial⟩ → /ʃəl/ (Chomsky & Halle 1968 on palatalization before the
  ``-ion`` suffix; Wells 2008 LPD for the surface values).

The non-regression half of this file is the point: the previous attempt at
these facts used grapheme digraph keys and broke word-*internal* material
(``personne``, ``terre``, ``house``). Endings only ever touch the word's
effective end.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def fr():
    return G2P("fr-FR")


@pytest.fixture(scope="module")
def en():
    return G2P("en")


@pytest.fixture(scope="module")
def en_us():
    return G2P("en-US")


# ── French: mute -er / -ez ────────────────────────────────────────────
@pytest.mark.parametrize("word,expected", [
    ("parler", "paʁle"),
    ("manger", "mɑ̃ʒe"),
    ("boulanger", "bulɑ̃ʒe"),
    # plural of an agent noun: the ending is still word-final modulo the
    # transparent grammatical ⟨s⟩ (Tranel 1987 §3)
    ("boulangers", "bulɑ̃ʒe"),
    ("mangez", "mɑ̃ʒe"),
    ("nez", "ne"),
    ("chez", "ʃe"),
    ("assez", "ase"),
])
def test_fr_mute_endings(fr, word, expected):
    assert fr.transcribe(word) == expected


@pytest.mark.parametrize("word,expected", [
    # ⟨er⟩ word-INTERNAL: intervocalic ⟨s⟩ must stay voiceless, ⟨rr⟩ must
    # stay degeminated — the two regressions the digraph attempt caused.
    ("personne", "pɛʁsɔn"),
    ("version", "vɛʁsjɔ̃"),
    ("terre", "təʁ"),
    ("pierre", "pjəʁ"),
    # ⟨er⟩ here matches grammatical_endings just like it does in
    # ``boulangers``; ``vers`` keeps /vɛʁ/ because its word_exceptions
    # entry outranks the ending, not because the matcher declines to match
    ("vers", "vɛʁ"),
    # word_exceptions outrank grammatical_endings
    ("mer", "mɛʁ"),
    ("hiver", "ivɛʁ"),
    # transparent-suffix machinery untouched
    ("vies", "vi"),
])
def test_fr_no_regression(fr, word, expected):
    assert fr.transcribe(word) == expected


# ── English: suffix palatalization ────────────────────────────────────
@pytest.mark.parametrize("word,expected", [
    ("nation", "næʃən"),
    ("station", "stæʃən"),
    ("motion", "mɒʃən"),
    ("mission", "mɪʃən"),
    ("special", "spɛʃəl"),
    ("gracious", "ɡɹæʃəs"),
    ("martial", "mɑːɹʃəl"),
    # longest match wins: ⟨-stion⟩ keeps the /t/ as the affricate onset
    ("question", "kwɛstʃən"),
    # same for ⟨-stial⟩/⟨-stious⟩: the ⟨t⟩ after ⟨s⟩ is not palatalized to
    # [ʃ] alone, since a bare [sʃ] cluster is phonotactically impossible
    # (Chomsky & Halle 1968; Wells 2008 LPD)
    ("celestial", "sɛlɛstʃəl"),
    ("bestial", "bɛstʃəl"),
])
def test_en_palatalized_suffixes(en, word, expected):
    assert en.transcribe(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("house", "haʊz"),
    ("mouse", "maʊz"),
    ("louse", "laʊz"),
    ("rouse", "ɹaʊz"),
])
def test_en_ous_words_unchanged(en, word, expected):
    """The #808 breakage class: ⟨-ous⟩/⟨-ouse⟩ words share letters with
    ⟨-cious⟩ but no suffix, so nothing may fire."""
    assert en.transcribe(word) == expected
    assert "ʃ" not in en.transcribe(word)


def test_en_us_inherits_endings(en_us):
    assert en_us.transcribe("nation") == "næʃən"
    assert "ʃ" not in en_us.transcribe("house")


# ── mechanism ─────────────────────────────────────────────────────────
def test_ending_never_consumes_the_whole_word(en):
    """An ending needs a head: a word that IS the ending is left alone."""
    assert G2P("fr-FR").transcribe("ez") != "e"


def test_precedence_word_exceptions_beat_endings(fr):
    assert "mer" in (fr.spec.word_exceptions or {})
    assert fr.transcribe("mer") == fr.spec.word_exceptions["mer"]


# ── Ambiguous endings: exposed in the lattice, decided downstream ─────
#
# French verbal ⟨-ent⟩ is mute (*ils parlent* [paʁl]); nominal/adjectival
# ⟨-ent⟩ is [ɑ̃] (*vent*, *moment*). Nothing orthographic separates them —
# it is a part-of-speech fact (Fouché 1959; Tranel 1987 §3; Divay & Vitale
# 1997), and o2i neither ships a tagger nor accepts a tag as an input.
#
# What it owes instead is that the reading it cannot choose still EXISTS,
# so a downstream rescorer that HAS the tag can select it. Before ⟨-ent⟩
# was declared as a deferring candidate list, [paʁl] was in no beam at any
# width: a coverage hole, which no downstream can repair, rather than a
# ranking error, which any downstream can.

@pytest.mark.parametrize("word,mute", [
    ("parlent", "paʁl"),
    ("munissent", "mynis"),
    ("chantent", "ʃɑ̃t"),
    ("rétablissent", "ʁetablis"),
    # ⟨-ment⟩ is NOT shielded off ⟨-ent⟩: it is the same ambiguity, and
    # verb stems ending in ⟨m⟩ are mute exactly like the rest.
    ("dorment", "dɔʁm"),
])
def test_fr_mute_ent_reading_is_reachable(fr, word, mute):
    """The defect this feature exists for: the mute reading must be IN the
    lattice, near enough the top that a rescorer sees it."""
    assert mute in fr.word_candidates(word, k=10)


@pytest.mark.parametrize("word,expected", [
    # nominal/adjectival ⟨-ent⟩ — rank 1 is the nasal reading, untouched
    ("vent", "vɑ̃"),
    ("dent", "dɑ̃"),
    ("cent", "sɑ̃"),
    ("argent", "aʁʒɑ̃"),
    ("moment", "mɔmɑ̃"),
    ("comment", "kɔmɑ̃"),
    ("absent", "absɑ̃"),
    # and the verbs too: o2i does NOT decide, so 1-best stays nasal
    ("parlent", "paʁlɑ̃"),
    ("dorment", "dɔʁmɑ̃"),
])
def test_fr_ent_one_best_unmoved(fr, word, expected):
    """A deferring list contributes candidates and nothing else. 1-best is
    byte-identical to what nasal ⟨en⟩ + silent ⟨t⟩ already produced —
    verified over a 2000-word wikipron/fr sweep, of which these are the
    named members."""
    assert fr.transcribe(word) == expected
    assert fr.word_candidates(word, k=10)[0] == expected


def test_fr_mute_reading_never_outranks(fr):
    """The mute reading is licit, not preferred: it may never be rank 1,
    for a verb or for anything else."""
    for word in ("parlent", "vent", "moment", "comment", "dorment"):
        assert fr.word_candidates(word, k=10)[0] != \
            fr.transcribe(word).replace("ɑ̃", "")


def test_fr_rewriting_endings_unaffected(fr):
    """⟨-er⟩/⟨-ez⟩ keep the plain-string rewrite semantics: one reading,
    the whole tail replaced."""
    assert fr.word_candidates("parler", k=10) == ["paʁle"]
    assert fr.word_candidates("mangez", k=10) == ["mɑ̃ʒe", "mɑ̃ɡe"]


def test_en_endings_have_no_alternatives(en):
    """English endings are plain strings, so nothing about them changes:
    one reading of the tail, no added candidates."""
    for word in ("nation", "question", "gracious"):
        assert all("ʃ" in c or "stʃ" in c for c in en.word_candidates(word, k=10))
    assert en.word_candidates("nation", k=10)[0] == "næʃən"


# ── value-shape semantics ─────────────────────────────────────────────
def test_normalize_ending_value_shapes():
    from orthography2ipa.positional import normalize_ending_value

    # a string and a one-element list of that string are the same thing
    assert normalize_ending_value("ʃən") == ("ʃən", ())
    assert normalize_ending_value(["ʃən"]) == ("ʃən", ())
    # null in element 0 = "rank 1 comes from the grapheme tables"
    assert normalize_ending_value([None, ""]) == (None, ("",))
    # a bare [null] declares an UNambiguous ending: no rewrite, no
    # alternatives — its only effect is longest-match shielding
    assert normalize_ending_value([None]) == (None, ())
    # an explicit rank 1 plus alternatives
    assert normalize_ending_value(["ɑ̃", ""]) == ("ɑ̃", ("",))


@pytest.mark.parametrize("bad", [[], ["a", None], [1], 7, [None, None]])
def test_normalize_ending_value_rejects(bad):
    """`null` is only meaningful as element 0. As an alternative it would
    have to mean "and this ending may also be silent", which is `""`."""
    from orthography2ipa.positional import normalize_ending_value
    with pytest.raises(ValueError):
        normalize_ending_value(bad)


def test_alternatives_are_rank_costed_and_ordered():
    """An explicit rank 1 rewrites the tail exactly as a string value does,
    and the alternatives take the same rank cost an ordered grapheme list
    takes (``weights.candidate_base_costs``) — so they follow declared
    order and can never undercut rank 1."""
    import dataclasses

    g = G2P("fr-FR")
    # A fresh spec object; the shared registry instance is not touched.
    g.spec = dataclasses.replace(
        g.spec,
        grammatical_endings={**g.spec.grammatical_endings,
                             "ent": ["\u0251\u0303", "", "\u025bnt"]})
    cands = g.word_candidates("parlent", k=10)
    assert cands[0] == "pa\u0281l\u0251\u0303"
    assert cands.index("pa\u0281l") < cands.index("pa\u0281l\u025bnt")


def test_loader_rejects_malformed_ending_value(tmp_path):
    from orthography2ipa.schema import LanguageSpecModel
    import pydantic

    with pytest.raises(pydantic.ValidationError):
        LanguageSpecModel(code="xx-XX", name="X", script="Latin",
                          grammatical_endings={"ent": []})


# ── shipped-data gates ────────────────────────────────────────────────
#
# `grammatical_endings` is the one sanctioned way morphology reaches the
# lattice, which makes it exactly the shape a lexicon or a paradigm table
# would take if one were smuggled in. AGENTS.md's lattice-ambiguity gate
# asks a reviewer to check three things by hand; these tests make two of
# them mechanical, so enumeration creep hits a tripwire instead of
# accreting one plausible entry at a time.

import glob
import json
import os
import re

import pytest

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "orthography2ipa", "data")

#: Ceiling on list-valued (ambiguous) endings in ONE spec. Ambiguous
#: endings are meant to be rare and individually argued: French ships
#: one. A spec that wants a sixth is enumerating a paradigm — the exact
#: failure this cap exists to catch — so RAISING THIS NUMBER REQUIRES AN
#: AMENDMENT TO AGENTS.md's lattice-ambiguity gate, argued there first.
#: Do not raise it to make a data PR green.
MAX_AMBIGUOUS_ENDINGS_PER_SPEC = 5


def _specs_with_endings():
    """(code, raw_json) for every shipped spec that DECLARES endings.

    Declares, not inherits: a spec that picks endings up through
    ``grammatical_endings_base`` inherits their citations with them, and
    asking it to restate them would just duplicate prose."""
    out = []
    for path in sorted(glob.glob(os.path.join(DATA_DIR, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            raw = json.load(fh)
        if raw.get("grammatical_endings"):
            out.append((os.path.basename(path)[:-len(".json")], raw))
    return out


def _mentions(notes: str, ending: str):
    """Character offsets where *notes* names *ending* as an ending.

    Bounded by non-letters on both sides, so ⟨-tion⟩, "tion" and -tion
    all count while `palatalization` and `questions` do not."""
    return [m.start() for m in
            re.finditer(rf"(?<![a-z]){re.escape(ending)}(?![a-z])",
                        notes.lower())]


def _citations(raw):
    """``(surname, year)`` pairs for every source the spec declares.

    A citation is recognised by its SURNAME. A bare year is not a
    citation and must never certify anything: prose is full of incidental
    four-digit numbers, and "a corpus sample of 1987 types" self-certifies
    against a spec that happens to cite Tranel 1987. The surname carries
    the attribution; the year only disambiguates which work by that
    author, so it is required ADJACENT to the surname rather than
    anywhere in the passage."""
    out = []
    for src in raw.get("sources") or []:
        year = src.get("year")
        if not year:
            continue
        for name in re.split(r"[,&]| and ", src.get("author") or ""):
            name = name.strip().rstrip(".")
            # Skip initials ("J.C.", "P.") — they are not attributions.
            if len(name) > 2 and not re.fullmatch(r"[A-Z.]+", name):
                out.append((name.lower(), str(year)))
    return out


#: How far a year may sit from its surname and still read as one
#: citation. Covers "Chomsky & Halle 1968", "Fouché (1959)", "Wells
#: (2008) Longman Pronunciation Dictionary" — and not a surname in one
#: clause with an unrelated year in the next.
_CITATION_SPAN = 40


def _cited_by(passage: str, citations) -> list:
    """The ``(surname, year)`` citations that appear, joined, in
    *passage* — surname first, its own year within
    :data:`_CITATION_SPAN` characters."""
    low = passage.lower()
    return [(surname, year) for surname, year in citations
            if re.search(rf"{re.escape(surname)}.{{0,{_CITATION_SPAN}}}?"
                         rf"{re.escape(year)}", low, re.S)]


#: The required shape of an ending's coverage passage in `notes`:
#:
#:     ENDING "ent" ... (Fouché 1959; Tranel 1987 §3)
#:
#: An EXPLICIT key phrase, not proximity. Proximity was the first
#: attempt and it does not work: a `notes` blob runs several thousand
#: characters and is dense with citations, so on any window wide enough
#: to hold a real explanation, most positions in the text sit near SOME
#: source token. An uncited ending a sentence away from an unrelated
#: `Tranel 1987` passed. The key phrase makes the claim explicit and
#: attributable — the author has to write down which source covers which
#: ending — and it is the same mechanical form the lattice-hole gate
#: already uses (`LATTICE-HOLE EVIDENCE for "ent"`).
_COVERAGE_PHRASE = 'ENDING "{ending}"'


def _coverage_passage(notes: str, ending: str):
    """The `ENDING "x" ... ` sentence for *ending*, or ``None``.

    Ends at the first sentence terminator that is not part of the
    citation itself, so the citation must sit in the SAME sentence as the
    coverage claim — a citation in the next sentence, or elsewhere in the
    blob, does not count."""
    marker = _COVERAGE_PHRASE.format(ending=ending)
    start = notes.find(marker)
    if start < 0:
        return None
    end = notes.find(". ", start + len(marker))
    return notes[start:] if end < 0 else notes[start:end + 1]


@pytest.mark.parametrize("code,raw", _specs_with_endings(),
                         ids=lambda v: v if isinstance(v, str) else "")
def test_every_ending_is_documented_and_cited(code, raw):
    """Every ending — single-valued or list-valued — is a cited claim
    about a suffix's realisation, never a PER-chasing pattern.

    An ending earns its place from a published source that states how the
    suffix is realised, exactly like every other rule in the spec, and
    exactly as n-grams are kept out of `graphemes`. Corpus frequency
    supports a list value's ORDERING; a frequency count alone is not a
    citation.

    The required form is explicit, so nothing is inferred from where the
    prose happens to sit::

        ENDING "ent" is [...] (Fouché 1959; Tranel 1987 §3)

    A SURNAME from this spec's own `sources`, with its year beside it,
    must stand in the same sentence as the coverage claim."""
    notes = raw.get("notes") or ""
    citations = _citations(raw)
    assert citations, (
        f"{code}: declares grammatical_endings but has no citable `sources` "
        f"(author + year); an ending is a cited linguistic claim, not a "
        f"pattern")
    for ending in raw["grammatical_endings"]:
        passage = _coverage_passage(notes, ending)
        assert passage is not None, (
            f"{code}: grammatical_endings key {ending!r} has no "
            f"{_COVERAGE_PHRASE.format(ending=ending)!r} passage in the "
            f"spec's `notes`. Say what the suffix is, how it is realised, "
            f"and cite it; see AGENTS.md's lattice-ambiguity gate.")
        assert _cited_by(passage, citations), (
            f"{code}: {_COVERAGE_PHRASE.format(ending=ending)} is documented "
            f"but not cited in the same sentence. Name an AUTHOR from this "
            f"spec's `sources` with the year beside it — a bare year is not "
            f"a citation, a frequency count is not a citation, and an ending "
            f"must never be hammered in to chase PER. Passage was: "
            f"{passage[:160]!r}")


@pytest.mark.parametrize("code,raw", _specs_with_endings(),
                         ids=lambda v: v if isinstance(v, str) else "")
def test_ambiguous_endings_carry_lattice_hole_evidence(code, raw):
    """A LIST-valued ending injects a reading into the beam, so it owes
    the extra evidence SCHEMA.md's admissibility bar asks for: the
    0-in-top-k lattice-hole measurement on gold, and the basis for the
    ordering. Both live in the spec's `notes`, beside the ending."""
    notes = raw.get("notes") or ""
    for ending, value in raw["grammatical_endings"].items():
        if not isinstance(value, list):
            continue
        for spot, label in ((f'lattice-hole evidence for "{ending}"',
                             "the 0-in-top-k measurement on gold"),
                            (f'ordering basis for "{ending}"',
                             "why rank 1 is where it is")):
            assert spot.lower() in notes.lower(), (
                f"{code}: ambiguous (list-valued) ending {ending!r} has no "
                f"{spot!r} passage in `notes`. A list value is admissible "
                f"ONLY where the missing reading is a PROVEN lattice hole; "
                f"state {label}. See AGENTS.md's lattice-ambiguity gate.")


@pytest.mark.parametrize("code,raw", _specs_with_endings(),
                         ids=lambda v: v if isinstance(v, str) else "")
def test_no_spec_enumerates_a_paradigm(code, raw):
    """No spec's ending keys may grow into a conjugation or declension
    table.

    A list value states the attested realisations of ONE spelled ending.
    Enumerating the cells of a paradigm — `ons`, `ez`, `ent`, `ais`,
    `ait`, `aient`, `èrent` … — is a morphological lexicon written in the
    schema's notation, forbidden by the same AGENTS.md clause that
    forbids morpheme chunks as grapheme keys. Each cell would match
    orthographically, so nothing else catches it: this cap is the
    tripwire."""
    ambiguous = [k for k, v in raw["grammatical_endings"].items()
                 if isinstance(v, list)]
    assert len(ambiguous) <= MAX_AMBIGUOUS_ENDINGS_PER_SPEC, (
        f"{code}: {len(ambiguous)} list-valued endings {sorted(ambiguous)} "
        f"exceeds the cap of {MAX_AMBIGUOUS_ENDINGS_PER_SPEC}. This reads as "
        f"paradigm enumeration. Raising the cap requires an amendment to "
        f"AGENTS.md's lattice-ambiguity gate, argued there first — do not "
        f"raise it to make a data PR green.")


# ── the measurement convention ────────────────────────────────────────
def test_exposure_can_be_turned_off_and_restores_the_dev_beam():
    """`expose_ambiguous_endings=False` removes the injected readings and
    nothing else.

    This is what lets the published scoreboard keep `PER - Oracle@k`
    readable as RANKING error: an injected alternative lowers an oracle
    by construction, so the board scores the beam the engine ranks. The
    engine's own default is ON, because exposing the reading it cannot
    choose is the entire point of declaring the ending ambiguous."""
    on = G2P("fr-FR")
    off = G2P("fr-FR", expose_ambiguous_endings=False)
    assert on.expose_ambiguous_endings is True
    for word, mute in (("parlent", "paʁl"), ("vent", "v"), ("moment", "mɔm")):
        exposed = on.word_candidates(word, k=10)
        plain = off.word_candidates(word, k=10)
        assert mute in exposed and mute not in plain
        # Everything else is untouched, in order: the exposed list is the
        # plain one with the injected reading spliced in at its cost.
        # Compared as a prefix, because inserting a reading at a fixed k
        # pushes the cheapest one off the end.
        without = [c for c in exposed if c != mute]
        assert without == plain[:len(without)]
        # 1-best cannot depend on the flag — an alternative never reaches
        # rank 1, which is why the PER columns are convention-independent.
        assert exposed[0] == plain[0] == off.transcribe(word) \
            == on.transcribe(word)


def _benchmark_module():
    """The benchmark harness, imported the way its own tests do."""
    import importlib
    import sys
    scripts = os.path.join(os.path.dirname(DATA_DIR), "..", "scripts")
    scripts = os.path.abspath(scripts)
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    return importlib.import_module("benchmark")


def test_board_scores_without_injected_alternatives_by_default():
    """The board's measurement convention is locked at the signature.

    `PER - Oracle@k` is published as RANKING error, so the scoring run
    must not see injected alternatives. Flipping this default silently
    republishes them into the headroom, and every downstream check still
    passes because the numbers stay internally consistent — nothing else
    in the suite notices. So the default itself is the assertion."""
    import inspect

    bench = _benchmark_module()
    for fn in (bench.evaluate_words_oracle, bench.build_scoreboard):
        default = inspect.signature(fn).parameters[
            "expose_ambiguous_endings"].default
        assert default is False, (
            f"{fn.__name__}'s expose_ambiguous_endings default is "
            f"{default!r}, not False. The published oracle columns must be "
            f"measured on the beam the engine RANKS; see docs/benchmarks.md, "
            f"'Injected alternatives do not count as ranking error'.")


def test_injected_alternatives_field_follows_the_flag_not_the_spec():
    """`oracle_injected_alternatives` is a claim about the MEASUREMENT —
    "these readings are not in these numbers" — not about the spec.

    Derived from the spec alone, it kept asserting an exclusion after the
    scoring flag was flipped, which is precisely the failure a provenance
    field exists to prevent. Scored with exposure ON there is nothing to
    claim, so the list must be empty."""
    bench = _benchmark_module()
    assert bench._injected_alternatives("fr", False) == ["fr-FR ent"]
    assert bench._injected_alternatives("fr", True) == []
    assert bench._injected_alternatives("nl", False) == []


def test_scoreboard_row_records_excluded_injections():
    """A board row whose language declares injected alternatives names
    them, so the exclusion travels with the numbers instead of living
    only in prose a later reader may not find."""
    rows = json.load(open(os.path.join(
        os.path.dirname(DATA_DIR), "..", "benchmarks", "results.json"),
        encoding="utf-8"))
    fr = [r for r in rows
          if r["lang"] == "fr" and r["dataset"] == "wikipron"][0]
    assert fr.get("oracle_injected_alternatives") == ["fr-FR ent"]
