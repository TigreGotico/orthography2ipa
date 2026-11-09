#!/usr/bin/env python3
"""Generate the language atlas: the generated blocks of the language pages and
the four atlas indexes.

A language page under ``docs/languages/`` that holds atlas markers is an atlas
page. Its file name is its spec code (``es-ES.md``). Each generated block sits
between two markers and is rewritten from the data on every run::

    <!-- atlas:header begin -->
    ...
    <!-- atlas:header end -->

Every other line of the page is hand-written and is never touched. The blocks
come in a fixed order, so that a reader learns the page once:

``summary``, ``header``, then the hand-written prose, then ``lects``,
``sources``, ``datasets``, ``inventory``, ``spelling``, ``rules``, ``examples`` and
``related``.

The ``examples`` marker can name the words to transcribe, separated by ``|``::

    <!-- atlas:examples begin words="cabra|la boca" -->

The data comes from four places, all in the repository: the resolved specs,
``benchmarks/results.json`` (read, never written), the summary table of
``docs/evaluation/datasets.md`` for the dataset links and licences, and
``scripts/atlas_snapshot.json``. The snapshot holds the Glottolog macroarea and
countries of each languoid, the ISO 639-3 reference names and the CLDR country
names. ``--refresh-snapshot`` rebuilds it over the network. The other modes
never touch the network, so ``--check`` gives the same answer in CI.

The four indexes are ``by-family.md``, ``by-region.md``, ``by-script.md`` and
``a-z.md``. Each one links every atlas page and every registered spec. A spec
with no page links to its entry in the data explorer.

Usage::

    PYTHONPATH=$PWD python scripts/gen_language_atlas.py --write
    PYTHONPATH=$PWD python scripts/gen_language_atlas.py --check
    PYTHONPATH=$PWD python scripts/gen_language_atlas.py --scaffold fi
    PYTHONPATH=$PWD python scripts/gen_language_atlas.py --refresh-snapshot

``--check`` writes nothing and exits 1 when a block or an index is stale, or
when an atlas page breaks the template.
"""

from __future__ import annotations

import argparse
import csv
import dataclasses
import glob
import importlib.util
import io
import json
import os
import re
import sys
import unicodedata
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import orthography2ipa  # noqa: E402
from orthography2ipa import registry  # noqa: E402
from orthography2ipa.inventory import STRESS_MARKS, phoneme_inventory  # noqa: E402

DATA_DIR = os.path.join(REPO_ROOT, "orthography2ipa", "data")
LANG_DIR = os.path.join(REPO_ROOT, "docs", "languages")
RESULTS = os.path.join(REPO_ROOT, "benchmarks", "results.json")
DATASETS_PAGE = os.path.join(REPO_ROOT, "docs", "evaluation", "datasets.md")
PRIMARY_ROWS = os.path.join(DATA_DIR, "gold", "primary_sources", "rows.jsonl")
PRIMARY_SOURCES = os.path.join(DATA_DIR, "gold", "primary_sources", "sources.json")
SNAPSHOT = os.path.join(REPO_ROOT, "scripts", "atlas_snapshot.json")

EXPLORER = "https://tigregotico.github.io/orthography2ipa/"
INDEXES = {
    "by-family.md": "Languages by family",
    "by-region.md": "Languages by region",
    "by-script.md": "Languages by script",
    "a-z.md": "Languages from A to Z",
}

BLOCKS = ("summary", "header", "lects", "sources", "datasets", "inventory",
          "spelling", "rules", "examples", "related")
_BLOCK = re.compile(
    r"<!-- atlas:(?P<name>\w+) begin(?P<attrs>[^>]*?)-->\n.*?<!-- atlas:(?P=name) end -->",
    re.S)
_ATTR = re.compile(r'(\w+)="([^"]*)"')
_REGION = re.compile(r"^[a-z]{2,3}(?:-[A-Z][a-z]{3})?-(?P<region>[A-Z]{2}|\d{3})(?:-|$)")

#: The coarse class of each reliability tier, in the order of
#: ``RELIABILITY_TIERS`` in ``scripts/benchmark.py``.
TIER_CLASS = {
    "expert-human": "gold",
    "lexicon-derived": "gold",
    "crowd-scraped": "gold",
    "machine-generated": "generated",
    "espeak-derived": "generated",
    "epitran-derived": "generated",
    "lupo-derived": "generated",
    "llm-corrected": "silver",
    "llm-generated": "silver",
}

#: Active members of the ISO 639-3 macrolanguage ``ara``, from the SIL
#: macrolanguage table, and Hassaniya ``mey``: the set arbtok accepts.
_ARABIC_ISO = frozenset(
    "ara aao abh abv acm acq acw acx acy adf aeb aec afb apc apd arb arq ars "
    "ary arz auz avl ayh ayl ayn ayp pga shu ssh mey".split())

#: Downstream repositories that build on the specs. ``covers`` takes the spec
#: and its lineage (the spec code first, then its ``parent`` chain) and says
#: whether the repository handles that spec.
RELATED = (
    ("tugaphone", "https://github.com/TigreGotico/tugaphone",
     "A dialect-aware Portuguese phonemizer. Each dialect is an "
     "orthography2ipa lect spec.",
     lambda spec, lineage: spec.code.split("-")[0] == "pt"),
    ("arbtok", "https://github.com/TigreGotico/arbtok",
     "Arabic text to IPA, with tashkeel restoration that knows the dialect.",
     lambda spec, lineage: _lineage_iso(lineage) in _ARABIC_ISO),
    ("euskaphone", "https://github.com/TigreGotico/euskaphone",
     "A dialect-aware Basque phonemizer over the orthography2ipa lattice.",
     lambda spec, lineage: spec.code.split("-")[0] == "eu"),
    ("o2i-lexicons", "https://github.com/TigreGotico/o2i-lexicons",
     "The residual lexicon for this spec: only the words its rules cannot "
     "reach.",
     lambda spec, lineage: spec.code in {"en-GB", "pt-BR", "pt-PT"}),
    ("silabificador", "https://github.com/TigreGotico/silabificador",
     "The Portuguese syllabifier and stress plugin of the engine.",
     lambda spec, lineage: spec.code.split("-")[0] == "pt"),
)


def _lineage_iso(lineage: Sequence) -> Optional[str]:
    for spec in lineage:
        if spec.iso639_3:
            return spec.iso639_3
    return None


# --------------------------------------------------------------------------
# Inputs


def _docs_nav():
    path = os.path.join(REPO_ROOT, "scripts", "docs_nav.py")
    spec = importlib.util.spec_from_file_location("docs_nav", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Atlas:
    """Everything the pages and the indexes are built from."""

    def __init__(self) -> None:
        self.raw: Dict[str, dict] = {}
        for path in sorted(glob.glob(os.path.join(DATA_DIR, "*.json"))):
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
            self.raw[data["code"]] = data
        self.codes = sorted(registry.available_codes())
        self.children: Dict[str, List[str]] = defaultdict(list)
        for code in self.codes:
            parent = self.raw.get(code, {}).get("parent")
            if parent:
                self.children[parent].append(code)
        self.aliases: Dict[str, List[str]] = defaultdict(list)
        for alias in registry._ALIASES:
            target = registry.resolve(alias)
            if alias != target and "x-clade" not in target:
                self.aliases[target].append(alias)
        with open(RESULTS, encoding="utf-8") as fh:
            self.board = json.load(fh)
        self.board_by_code: Dict[str, List[dict]] = defaultdict(list)
        for row in self.board:
            # A row tag that names no spec is not attributed to the nearest
            # one: its score was measured on another spec.
            if registry.resolves_exactly(row["lang"]):
                self.board_by_code[registry.resolve(row["lang"])].append(row)
        self.datasets = _dataset_table()
        with open(SNAPSHOT, encoding="utf-8") as fh:
            self.snapshot = json.load(fh)
        self.country_area = _country_areas(self.snapshot["geography"])
        self.primary_rows: Dict[str, List[dict]] = defaultdict(list)
        with open(PRIMARY_ROWS, encoding="utf-8") as fh:
            for line in fh:
                row = json.loads(line)
                if row.get("lang"):
                    self.primary_rows[row["lang"]].append(row)
        with open(PRIMARY_SOURCES, encoding="utf-8") as fh:
            self.primary_sources = json.load(fh)
        self.pages = {os.path.basename(p)[:-3]
                      for p in glob.glob(os.path.join(LANG_DIR, "*.md"))
                      if "<!-- atlas:header begin" in _read(p)}

    def spec(self, code: str):
        return orthography2ipa.get(code)

    def lineage(self, code: str) -> list:
        return [self.spec(c) for c in [code] + registry.ancestry_chain(code)
                if c in self.raw]

    def link(self, code: str, here: str = "") -> str:
        """A link to the page of *code*, or to its explorer entry."""
        if code in self.pages:
            return f"{here}{code}.md"
        return EXPLORER + "#" + urllib.parse.quote(code, safe="")

    def geography(self, code: str) -> Tuple[List[str], List[str]]:
        """The macroareas and the countries of *code*.

        A region subtag in the code names the country, and the macroarea is
        the one that most Glottolog languoids of that country fall in.
        Otherwise the countries are those of the spec's own Glottolog
        languoid. A spec with neither takes no country from an ancestor,
        because a dialect is not spoken in every country of its language.
        The macroarea then comes from the nearest spec on the lineage that
        has a languoid. A family languoid can span several macroareas.
        """
        macroarea, countries = "", []
        for depth, spec in enumerate(self.lineage(code)):
            entry = self.snapshot["geography"].get(spec.glottolog_code or "")
            if entry:
                macroarea, _, listed = entry.partition("|")
                if depth == 0:
                    countries = listed.split()
                break
        match = _REGION.match(code)
        if match and match.group("region") in self.snapshot["countries"]:
            countries = [match.group("region")]
            macroarea = self.country_area.get(countries[0], macroarea)
        return [a for a in macroarea.split(";") if a], countries

    def country(self, iso: str) -> str:
        return self.snapshot["countries"].get(iso, iso)


def _country_areas(geography: Dict[str, str]) -> Dict[str, str]:
    """The macroarea that most single-macroarea languoids of a country have."""
    counts: Dict[str, Counter] = defaultdict(Counter)
    for entry in geography.values():
        area, _, listed = entry.partition("|")
        if area and ";" not in area:
            for country in listed.split():
                counts[country][area] += 1
    return {country: c.most_common(1)[0][0] for country, c in counts.items()}


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _dataset_table() -> Dict[str, dict]:
    """The summary table of ``docs/evaluation/datasets.md``, keyed by dataset."""
    table = {}
    for line in _read(DATASETS_PAGE).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6 or not cells[0].startswith("`"):
            continue
        key = cells[0].strip("`")
        link = re.search(r"\[([^\]]+)\]\((https?://[^)]+)\)", cells[3])
        table[key] = {
            "source": link.group(1) if link else None,
            "url": link.group(2) if link else None,
            "licence": "" if cells[4] in ("-", "") else cells[4],
        }
    return table


# --------------------------------------------------------------------------
# Text helpers


def _clean(text) -> str:
    """Make free text from a spec safe in a table cell and in the prose lint."""
    text = " ".join(str(text).split())
    text = re.sub(r"\s*[—–]\s*", ", ", text)
    text = text.replace(";", ",").replace("|", "/")
    return text


def _slug(heading: str) -> str:
    """The anchor GitHub and most site generators give a heading."""
    text = unicodedata.normalize("NFKC", heading).lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def _ipa(segments: Iterable[str]) -> str:
    return " ".join(f"[{s}]" if s else "∅" for s in segments)


def _article(word: str) -> str:
    return "an" if word[:1].lower() in "aeiou" else "a"


def _join(items: Sequence[str]) -> str:
    items = list(items)
    if len(items) <= 1:
        return "".join(items)
    return ", ".join(items[:-1]) + " and " + items[-1]


def _value(enum_or_str) -> str:
    return getattr(enum_or_str, "value", enum_or_str) or ""


# --------------------------------------------------------------------------
# Page blocks


def block_summary(atlas: Atlas, spec) -> str:
    family = spec.family.split(" > ") if spec.family else []
    branch = family[-1] if family else "unclassified"
    kind = "variety" if "-x-" in spec.code else "language"
    macroarea, countries = atlas.geography(spec.code)
    names = sorted(atlas.country(c) for c in countries)
    if _REGION.match(spec.code) and len(countries) == 1:
        where = f" Its code names {names[0]}."
    elif 1 <= len(names) <= 4:
        where = f" Glottolog places it in {_join(names)}."
    elif names:
        where = f" Glottolog places it in {len(names)} countries."
    elif len(macroarea) == 1:
        where = f" Glottolog places it in the {macroarea[0]} macroarea."
    elif macroarea:
        where = f" Glottolog places it in the {_join(macroarea)} macroareas."
    else:
        where = ""
    sources = len(spec.sources or ())
    datasets = len(atlas.board_by_code.get(spec.code, ()))
    return (
        f"{spec.name} is {_article(branch)} {branch} {kind}, written in the "
        f"{spec.script} script.{where} The `{spec.code}` spec is at the "
        f"{_value(spec.quality)} tier. It cites {sources} "
        f"{'source' if sources == 1 else 'sources'} and has "
        f"{datasets} scored {'dataset' if datasets == 1 else 'datasets'}.")


def _family_cell(spec) -> str:
    if not spec.family:
        return "unclassified"
    parts = spec.family.split(" > ")
    top = f"[{parts[0]}](by-family.md#{_slug(parts[0])})"
    if len(parts) == 1:
        return top
    rest = " > ".join(parts[1:])
    return f"{top} > [{rest}](by-family.md#{_slug(spec.family)})"


def _area_group(macroareas: Sequence[str]) -> str:
    """The heading of the region index that a list of macroareas falls under."""
    if not macroareas:
        return "No macroarea"
    return macroareas[0] if len(macroareas) == 1 else "Several macroareas"


def block_header(atlas: Atlas, spec) -> str:
    rows = [("Code", f"`{spec.code}`")]
    aliases = sorted(atlas.aliases.get(spec.code, ()))
    if aliases:
        rows.append(("Aliases", ", ".join(f"`{a}`" for a in aliases)))
    if spec.iso639_3:
        name = atlas.snapshot["iso639_3"].get(spec.iso639_3)
        cell = (f"[{spec.iso639_3}](https://iso639-3.sil.org/code/"
                f"{spec.iso639_3})")
        rows.append(("ISO 639-3", f"{cell}, {name}" if name else cell))
    if spec.glottolog_code:
        name = atlas.snapshot["glottolog_names"].get(spec.glottolog_code)
        cell = (f"[{spec.glottolog_code}](https://glottolog.org/resource/"
                f"languoid/id/{spec.glottolog_code})")
        rows.append(("Glottolog", f"{cell}, {name}" if name else cell))
    if spec.wikidata_qid:
        rows.append(("Wikidata", f"[{spec.wikidata_qid}](https://www.wikidata"
                                 f".org/wiki/{spec.wikidata_qid})"))
    wiki = _wikipedia(spec)
    if wiki:
        title = urllib.parse.unquote(wiki.rsplit("/", 1)[-1]).replace("_", " ")
        rows.append(("Wikipedia", f"[{title}]({wiki})"))
    rows.append(("Family", _family_cell(spec)))
    macroarea, countries = atlas.geography(spec.code)
    if macroarea or countries:
        names = ", ".join(
            f"[{name}](by-region.md#{_slug(name)})"
            for name in sorted(atlas.country(c) for c in countries)[:8])
        if len(countries) > 8:
            names += f" and {len(countries) - 8} more"
        area = ", ".join(f"[{a}](by-region.md#{_slug(_area_group(macroarea))})"
                         for a in macroarea)
        rows.append(("Region", " > ".join(x for x in (area, names) if x)))
    script = f"[{spec.script}](by-script.md#{_slug(spec.script)})"
    rows.append(("Script", f"{script} ({_value(spec.script_type)})"))
    rows.append(("Tier", f"[{_value(spec.quality)}](../specs/quality_tiers.md"
                         f"#{_value(spec.quality)})"))
    if spec.timespan:
        end = spec.timespan.end_year
        rows.append(("Attested", f"from {spec.timespan.start_year}"
                     + (f" to {end}" if end is not None else ", living")))
    if spec.parent and spec.parent in atlas.raw:
        parent = atlas.raw[spec.parent]
        historical = (parent.get("timespan") or {}).get("end_year") is not None
        rows.append(("Ancestor" if historical else "Parent",
                     f"[{parent['name']}]({atlas.link(spec.parent)})"
                     f" `{spec.parent}`"))
    children = _child_lects(atlas, spec.code)
    if children:
        rows.append(("Child lects",
                     f"{len(children)}, see [Related lects](#related-lects)"))
    rows.append(("Explorer", f"[`{spec.code}` in the data explorer]"
                             f"({EXPLORER}#{urllib.parse.quote(spec.code, safe='')})"))
    rows.append(("Spec file", f"[`{spec.code}.json`](../../orthography2ipa/data/"
                              f"{spec.code}.json)"))
    lines = ["| Field | Value |", "|:--|:--|"]
    lines += [f"| {k} | {v} |" for k, v in rows]
    return "\n".join(lines)


def _wikipedia(spec) -> Optional[str]:
    pages = [u for u in (spec.wikipedia or ()) if "#" not in u]
    english = [u for u in pages if u.startswith("https://en.wikipedia.org/")]
    return (english or pages or [None])[0]


def _source_line(source) -> str:
    parts = [f"{_clean(source.author)} ({source.year}). *{_clean(source.title)}*."]
    if source.publisher:
        parts.append(_clean(source.publisher).rstrip(".") + ".")
    if source.pages:
        parts.append("Cited: " + _clean(source.pages).rstrip(".") + ".")
    links = []
    if source.doi:
        links.append(f"DOI [{source.doi}](https://doi.org/{source.doi})")
    if source.url and not (source.doi and source.doi in source.url):
        host = urllib.parse.urlparse(source.url).netloc.removeprefix("www.")
        links.append(f"[{host}]({source.url})")
    if links:
        parts.append(" · ".join(links))
    return " ".join(parts)


def block_sources(atlas: Atlas, spec) -> str:
    lines = ["## Sources", ""]
    sources = list(spec.sources or ())
    if not sources:
        return "\n".join(lines + ["The spec cites no source."])
    linked = sum(1 for s in sources if s.doi or s.url)
    lines += [f"The spec cites {len(sources)} works. {linked} of them have a "
              "DOI or a URL. The spec file holds a note on what each work "
              "supports.", ""]
    for n, source in enumerate(sources, 1):
        lines.append(f"{n}. <a id=\"src-{source.id}\"></a>{_source_line(source)}")
    return "\n".join(lines)


def block_datasets(atlas: Atlas, spec) -> str:
    rows = sorted(atlas.board_by_code.get(spec.code, ()),
                  key=lambda r: (list(TIER_CLASS).index(r.get("provenance", "llm-generated"))
                                 if r.get("provenance") in TIER_CLASS else 99,
                                 r["dataset"], r["lang"]))
    lines = ["## Datasets", ""]
    if not rows:
        return "\n".join(lines + [
            "No dataset on the board scores this spec. See the "
            "[dataset catalogue](../evaluation/datasets.md)."])
    lines += [
        "Every row of the board that scores this spec. PER is the phoneme "
        "error rate against the dataset. A gold row is human work, a silver "
        "row is a language model's label, and a generated row is the output "
        "of another tool. Only a row marked as gating can promote or block "
        "the spec. The [dataset catalogue](../evaluation/datasets.md) "
        "describes each set.", "",
        "| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |",
        "|:--|:--|:--|:--|:--|--:|--:|:--|"]
    for row in rows:
        meta = atlas.datasets.get(row["dataset"], {})
        name = f"`{row['dataset']}`"
        if meta.get("url"):
            name += f" ([{meta['source']}]({meta['url']}))"
        provenance = row.get("provenance") or "unknown"
        lines.append(
            f"| {name} | `{row['lang']}` | {TIER_CLASS.get(provenance, '-')} | "
            f"{provenance} | {meta.get('licence') or '-'} | {row['n']} | "
            f"{row['per']:.4f} | {'yes' if row.get('gating') else 'no'} |")
    return "\n".join(lines)


# The IPA pulmonic consonant chart, by base symbol.
_PLACES = ("bilabial", "labiodental", "dental", "alveolar", "postalveolar",
           "retroflex", "palatal", "velar", "uvular", "pharyngeal", "glottal")
_MANNERS = ("plosive", "affricate", "nasal", "trill", "tap", "fricative",
            "lateral fricative", "approximant", "lateral approximant")
_CONSONANTS = {}
for _manner, _row in {
    "plosive": "p:bilabial b:bilabial t:alveolar d:alveolar ʈ:retroflex "
               "ɖ:retroflex c:palatal ɟ:palatal k:velar ɡ:velar g:velar "
               "q:uvular ɢ:uvular ʔ:glottal",
    "affricate": "pf:labiodental ts:alveolar dz:alveolar tʃ:postalveolar "
                 "dʒ:postalveolar ʈʂ:retroflex ɖʐ:retroflex tɕ:palatal "
                 "dʑ:palatal tθ:dental dð:dental tɬ:alveolar dɮ:alveolar "
                 "kx:velar",
    "nasal": "m:bilabial ɱ:labiodental n:alveolar ɳ:retroflex ɲ:palatal "
             "ŋ:velar ɴ:uvular",
    "trill": "ʙ:bilabial r:alveolar ʀ:uvular",
    "tap": "ⱱ:labiodental ɾ:alveolar ɽ:retroflex",
    "fricative": "ɸ:bilabial β:bilabial f:labiodental v:labiodental "
                 "θ:dental ð:dental s:alveolar z:alveolar ʃ:postalveolar "
                 "ʒ:postalveolar ʂ:retroflex ʐ:retroflex ç:palatal ʝ:palatal "
                 "ɕ:palatal ʑ:palatal x:velar ɣ:velar χ:uvular ʁ:uvular "
                 "ħ:pharyngeal ʕ:pharyngeal h:glottal ɦ:glottal",
    "lateral fricative": "ɬ:alveolar ɮ:alveolar",
    "approximant": "ʋ:labiodental ɹ:alveolar ɻ:retroflex j:palatal ɰ:velar",
    "lateral approximant": "l:alveolar ɫ:alveolar ɭ:retroflex ʎ:palatal ʟ:velar",
}.items():
    for _cell in _row.split():
        _sym, _place = _cell.split(":")
        _CONSONANTS[_sym] = (_manner, _place)

_VOWEL_ROWS = ("close", "near-close", "close-mid", "mid", "open-mid",
               "near-open", "open")
_VOWEL_COLS = ("front", "central", "back")
_VOWELS = {}
for _height, _row in {
    "close": "i:front y:front ɨ:central ʉ:central ɯ:back u:back",
    "near-close": "ɪ:front ʏ:front ʊ:back",
    "close-mid": "e:front ø:front ɘ:central ɵ:central ɤ:back o:back",
    "mid": "ə:central",
    "open-mid": "ɛ:front œ:front ɜ:central ɞ:central ʌ:back ɔ:back",
    "near-open": "æ:front ɐ:central",
    "open": "a:front ɶ:front ɑ:back ɒ:back",
}.items():
    for _cell in _row.split():
        _sym, _col = _cell.split(":")
        _VOWELS[_sym] = (_height, _col)

_MODIFIERS = "ʰʷʲˠˤʼːˑ˞ⁿˡ"


def _base(segment: str) -> str:
    """A segment without its diacritics, modifier letters and tie bar.

    Combining marks are stripped from the composed form first, so that ⟨ç⟩
    stays the palatal fricative. Only a symbol the charts do not know is
    decomposed, which turns ⟨ẽ⟩ into ⟨e⟩.
    """
    def strip(text: str) -> str:
        return "".join(ch for ch in text if not unicodedata.combining(ch)
                       and ch not in _MODIFIERS and ch != "\u0361")

    composed = strip(unicodedata.normalize("NFC", segment))
    if composed in _CONSONANTS or composed in _VOWELS:
        return composed
    return unicodedata.normalize("NFC", strip(unicodedata.normalize("NFD", segment)))


def _chart(cells: Dict[Tuple[str, str], List[str]], rows: Sequence[str],
           cols: Sequence[str], corner: str) -> List[str]:
    used_rows = [r for r in rows if any((r, c) in cells for c in cols)]
    used_cols = [c for c in cols if any((r, c) in cells for r in rows)]
    if not used_rows:
        return []
    lines = ["| " + corner + " | " + " | ".join(c.capitalize() for c in used_cols) + " |",
             "|:--|" + ":-:|" * len(used_cols)]
    for r in used_rows:
        lines.append("| " + r.capitalize() + " | " + " | ".join(
            " ".join(sorted(cells.get((r, c), ()))) for c in used_cols) + " |")
    return lines


def block_inventory(atlas: Atlas, spec) -> str:
    # The whole-word exceptions are left out: a listed word is one emission,
    # and its transcription is not a segment.
    tokens = sorted(t for t in phoneme_inventory(
                        dataclasses.replace(spec, word_exceptions={}))
                    if t and t not in STRESS_MARKS and not t.isspace())
    consonants: Dict[Tuple[str, str], List[str]] = defaultdict(list)
    vowels: Dict[Tuple[str, str], List[str]] = defaultdict(list)
    other: List[str] = []
    for token in tokens:
        base = _base(token)
        if base in _CONSONANTS:
            manner, place = _CONSONANTS[base]
            consonants[(manner, place)].append(token)
        elif base in _VOWELS:
            height, col = _VOWELS[base]
            vowels[(height, col)].append(token)
        else:
            other.append(token)
    lines = ["## Inventory", "",
             f"The spec can emit {len(tokens)} segments. They come from the "
             "letter table, the positional readings, the allophones and the "
             "rules, so the charts show what the spec can write, not a "
             "phonemic analysis. A segment with a diacritic sits "
             "in the cell of its base symbol."]
    chart = _chart(consonants, _MANNERS, _PLACES, "Consonants")
    if chart:
        lines += [""] + chart
    chart = _chart(vowels, _VOWEL_ROWS, _VOWEL_COLS, "Vowels")
    if chart:
        lines += [""] + chart
    if other:
        shown = " ".join(f"[{t}]" for t in other[:40])
        more = f", and {len(other) - 40} more" if len(other) > 40 else ""
        lines += ["", f"Sequences that the spec writes as one unit: {shown}{more}."]
    if spec.tone_inventory:
        lines += ["", "Tones: " + ", ".join(
            f"[{mark}] {label}" for mark, label in spec.tone_inventory.items()) + "."]
    return "\n".join(lines)


def _readings(values) -> List[str]:
    if values is None:
        return []
    if isinstance(values, dict):
        values = values.get("ipa", ())
    return [v for v in values if v is not None]


def _stress_line(spec) -> List[str]:
    stress = spec.stress
    if not stress:
        return ["The spec declares no stress rule."]
    position = {-1: "the last syllable", -2: "the penult",
                -3: "the antepenult", -4: "the fourth syllable from the end",
                1: "the first syllable", 2: "the second syllable"}.get(
        stress.default_position, f"syllable {stress.default_position}")
    out = [f"Stress falls on {position} by default."]
    if stress.marked_vowels:
        out.append("A written " + " ".join(f"⟨{v}⟩" for v in stress.marked_vowels)
                   + " marks the stressed vowel.")
    if stress.final_stress_endings:
        out.append("These endings take final stress: " + " ".join(
            f"⟨-{e}⟩" for e in stress.final_stress_endings) + ".")
    if stress.penult_stress_endings:
        out.append("These endings take the penult: " + " ".join(
            f"⟨-{e}⟩" for e in stress.penult_stress_endings) + ".")
    if stress.quantity_sensitive:
        out.append("Stress is sensitive to syllable weight.")
    return [" ".join(out)]


def block_spelling(atlas: Atlas, spec) -> str:
    positional = spec.positional_graphemes or {}
    lines = ["## Spelling", "",
             "Each letter or letter group of the spec with its readings. The "
             "first reading is the default, and the others stay in the lattice "
             "as lower-ranked candidates. The last column gives the readings "
             "that depend on the position in the word.", "",
             "| Spelling | Readings | By position |", "|:--|:--|:--|"]
    for grapheme in sorted(spec.graphemes, key=lambda g: (g.lower(), g)):
        readings = _readings(spec.graphemes[grapheme])
        if not readings and grapheme not in positional:
            continue
        by_position = " · ".join(
            f"{_value(pos).replace('_', ' ')} {_ipa(vals)}"
            for pos, vals in sorted(positional.get(grapheme, {}).items(),
                                    key=lambda kv: _value(kv[0])))
        lines.append(f"| ⟨{grapheme}⟩ | {_ipa(readings) or '∅'} | {by_position} |")
    lines += [""] + _stress_line(spec)
    if spec.word_exceptions:
        words = sorted(spec.word_exceptions.items())
        shown = ", ".join(f"⟨{w}⟩ [{ipa}]" for w, ipa in words[:30])
        more = f", and {len(words) - 30} more in the spec file" if len(words) > 30 else ""
        lines += ["", f"Whole-word exceptions ({len(words)}): {shown}{more}."]
    if spec.grammatical_endings:
        endings = ", ".join(
            f"⟨-{e}⟩ " + (_ipa(v) if isinstance(v, (list, tuple)) else f"[{v}]")
            for e, v in sorted(spec.grammatical_endings.items()))
        lines += ["", f"Grammatical endings: {endings}."]
    return "\n".join(lines)


_CLASSES = {
    "consonant_cluster": "a consonant cluster", "coda_nasal": "a coda nasal",
    "front_vowel": "a front vowel", "back_vowel": "a back vowel",
    "emphatic": "an emphatic consonant", "word_boundary": "a word boundary",
    "vowel": "a vowel", "consonant": "a consonant", "coda": "a coda",
    "palatal": "a palatal", "any": "any letter",
}


def _segments(values: Sequence[str], limit: int = 8) -> str:
    values = list(values)
    text = " ".join(f"[{v}]" for v in values[:limit])
    return text + (f" and {len(values) - limit} more" if len(values) > limit else "")


def _change(rule) -> str:
    target = "/" + " ".join(rule.phonemes) + "/"
    if rule.append:
        head = f"insert [{rule.append}] after {target}"
    else:
        head = f"{target} → " + (f"[{rule.surface}]" if rule.surface else "∅")
    where = []
    for field, yes, no in (("word_initial", "word-initially", "not word-initially"),
                           ("word_final", "word-finally", "not word-finally")):
        value = getattr(rule, field)
        if value is not None:
            where.append(yes if value else no)
    if rule.stress:
        where.append(f"{rule.stress}")
    if rule.syllable_position:
        where.append(f"in the {rule.syllable_position}")
    if rule.preceded_by:
        where.append("after " + _CLASSES.get(rule.preceded_by, rule.preceded_by))
    if rule.followed_by:
        where.append("before " + _CLASSES.get(rule.followed_by, rule.followed_by))
    if rule.preceded_by_phoneme:
        where.append("after " + _segments(rule.preceded_by_phoneme))
    if rule.followed_by_phoneme:
        where.append("before " + _segments(rule.followed_by_phoneme))
    if rule.grapheme:
        where.append("spelled " + " ".join(f"⟨{g}⟩" for g in rule.grapheme))
    if rule.preceded_by_grapheme:
        where.append("after " + " ".join(f"⟨{g}⟩" for g in rule.preceded_by_grapheme))
    if rule.followed_by_grapheme:
        where.append("before " + " ".join(f"⟨{g}⟩" for g in rule.followed_by_grapheme))
    if rule.word:
        where.append(f"in {len(rule.word)} listed words")
    rest = [f.name for f in dataclasses.fields(rule)
            if f.name in ("preceded_by_2", "followed_by_2", "preceded_by_3",
                          "followed_by_3", "preceded_by_phoneme_2",
                          "followed_by_phoneme_2", "preceded_by_surface_phoneme_2",
                          "requires_other_nucleus", "followed_by_nucleus",
                          "followed_by_grapheme_not", "word_contains_grapheme",
                          "word_contains_grapheme_not", "mutates_neighbor")
            and getattr(rule, f.name) not in (None, (), "")]
    if rest:
        where.append("with more context in the spec")
    return head + (", " + ", ".join(where) if where else "")


_EXAMPLE = (
    re.compile(r"((?:[^\s\[\]()/,:;«»\"“”→]+ ){0,3}[^\s\[\]()/,:;«»\"“”→]+) → \[([^\]]+)\]"),
    re.compile(r"⟨([^⟩]+)⟩ (?:is |as |= )?\[([^\]]+)\]"),
    re.compile(r"((?:[^\W\d_][^\s\[\]()/,:;«»\"“”]* ){0,3}[^\W\d_][^\s\[\]()/,:;«»\"“”]*) \[([^\]]+)\]"),
    re.compile(r"([^\W\d_][^\s\[\]()/,:;«»\"“”]*) /([^/\s][^/]*)/"),
)
#: English words that stand before a bracketed segment in a note without
#: being the example word: "surfacing as [m]", "nasal [ẽ]".
_NOT_EXAMPLES = frozenset(
    "a an as is the to of in on at by or and before after between gives give "
    "nasal vowel consonant stop glide spirant becomes surfacing reads read "
    "written write yields yield than long short".split())
_CITE = re.compile(
    r"([A-Z][\w'’\-]+(?: (?:de |da |del |van |von |d')?[A-Z][\w'’\-]+)?"
    r"(?: (?:&|and) [A-Za-z][\w'’\-]+)?(?: et al\.)?),? \(?((?:1[5-9]|20)\d\d)\b")


def _examples(notes: str):
    """Every worked example in a rule note, as (spelling, IPA), in note order.

    The spelling keeps as many words as the transcription has, so that
    "the voiced apical: asno [ˈaz̺nu]" gives ⟨asno⟩ and not ⟨apical: asno⟩.
    A one-segment bracket after a description ("surfacing as [m]") is not an
    example.
    """
    for pattern in _EXAMPLE:
        for match in pattern.finditer(notes or ""):
            ipa = match.group(2).strip()
            words = match.group(1).split()[-len(ipa.split()):]
            spelled = " ".join(words)
            bare = "".join(ch for ch in ipa if not unicodedata.combining(ch)
                           and ch not in "ˈˌː")
            if ("..." in ipa or "…" in ipa or len(bare) < 2
                    or len(ipa) < len(spelled) / 2
                    or words[-1].lower().strip("⟨⟩") in _NOT_EXAMPLES
                    or spelled.startswith(("-", "/"))):
                continue
            yield spelled.strip("⟨⟩"), ipa


def _show(example) -> str:
    return f"⟨{_clean(example[0])}⟩ [{_clean(example[1])}]" if example else ""


def _example(notes: str, output: str = "") -> str:
    """The first example of the note whose transcription holds *output*.

    A note that three rules share must not give the labial example to the
    velar rule, so an example that does not show the rule's output is skipped.
    """
    return _show(next((e for e in _examples(notes) if output in e[1]), None))


def _sandhi_example(rule, output: str) -> str:
    """The first example of the note where two adjacent words meet the rule.

    The end of one word must match the left context and the start of the next
    the right context, and the side the rule rewrites must carry its output.
    """
    def fits(ipa: str) -> bool:
        words = ipa.split()
        for left, right in zip(words, words[1:]):
            try:
                if not (re.search(rule.left_context, left)
                        or (rule.transform is not None and output
                            and left.endswith(output))):
                    continue
                if not re.search(rule.right_context, right) and not (
                        rule.right_transform is not None
                        and right.lstrip("ˈˌ").startswith(output)):
                    continue
            except re.error:
                return False
            if rule.transform is not None and output and not left.endswith(output):
                continue
            if (rule.right_transform is not None and output
                    and not right.lstrip("ˈˌ").startswith(output)):
                continue
            return True
        return False

    return _show(next((e for e in _examples(rule.notes) if fits(e[1])), None))


def _cites(name: str, year: int, notes: str) -> bool:
    """Whether *notes* cites *name* with *year* in the same breath."""
    return bool(re.search(re.escape(name) + r"[^;\[]{0,40}?\b" + str(year) + r"\b",
                          notes))


def _citations(spec, notes: str) -> str:
    """The works a rule note cites, linked to the spec's sources when they match.

    A source matches when the note names its author, or the first two words
    of its title, and gives its year within a few words. Any other
    "Name (year)" in the note is listed as written, without a link.
    """
    notes = notes or ""
    found, matched = [], []
    for source in spec.sources or ():
        surname = re.split(r"[,&]", source.author)[0].strip().split(" ")[0]
        title = " ".join(source.title.split()[:2])
        if len(surname) >= 4 and _cites(surname[:6], source.year, notes):
            label = surname
        elif _cites(title, source.year, notes):
            label = title
        else:
            continue
        if source.id not in {m.id for m in matched}:
            matched.append(source)
            found.append(f"[{_clean(label)} {source.year}](#src-{source.id})")
    for name, year in _CITE.findall(notes):
        if name.startswith(("The ", "In ", "See ", "A ", "An ")):
            continue
        same = any(m.year == int(year) and (
            re.split(r"[,&]", m.author)[0].strip().split(" ")[0][:6] in name
            or " ".join(m.title.split()[:2]) in name) for m in matched)
        text = f"{_clean(name)} {year}"
        if not same and text not in found:
            found.append(text)
    return ", ".join(found[:3])


def block_rules(atlas: Atlas, spec) -> str:
    rules = list(spec.allophone_rules or ())
    active = [r for r in rules if r.phonemes]
    off = [r for r in rules if not r.phonemes]
    sandhi = list(spec.sandhi_rules or ())
    lines = ["## Rules", ""]
    if not active and not sandhi:
        lines.append("The spec has no allophone rule and no cross-word rule.")
    if active:
        lines += [
            f"The spec applies {len(active)} allophone rules after the letters "
            "are read. The change column is built from the rule's conditions. "
            "The example and the citation are quoted from the rule's note in "
            "the spec file. A dash means that the note holds no worked example "
            "or no dated citation.", "",
            "| Rule | Change | Example | Cited |", "|:--|:--|:--|:--|"]
        for rule in active:
            lines.append(f"| `{rule.id}` | {_change(rule)} | "
                         f"{_example(rule.notes, rule.surface or rule.append) or '-'} | "
                         f"{_citations(spec, rule.notes) or '-'} |")
    if sandhi:
        lines += ["", f"The spec applies {len(sandhi)} rules across a word "
                  "boundary. The contexts are regular expressions on the IPA "
                  "of the two words.", "",
                  "| Rule | End of word | Start of next word | Change | Example | Cited |",
                  "|:--|:--|:--|:--|:--|:--|"]
        for rule in sandhi:
            change, output = [], ""
            for side, value in (("left", rule.transform),
                                ("right", rule.right_transform)):
                if value is None:
                    continue
                # A replacement may restore a captured stress mark (\1).
                value = re.sub(r"\\\d|\\g<\w+>", "", value)
                output = output or value
                change.append(f"{side} [{value}]" if value else f"{side} ∅")
            # GitHub splits a table cell at a pipe, even inside a code span.
            left, right = (c.replace("|", "\\|")
                           for c in (rule.left_context, rule.right_context))
            lines.append(
                f"| `{rule.id}` | `{left}` | `{right}` | "
                f"{', '.join(change) or 'none'} | {_sandhi_example(rule, output) or '-'} | "
                f"{_citations(spec, rule.notes) or '-'} |")
    if off:
        lines += ["", f"The spec switches off {len(off)} inherited rules: "
                  + ", ".join(f"`{r.id}`" for r in off) + "."]
    return "\n".join(lines)


def block_examples(atlas: Atlas, spec, words: Sequence[str]) -> str:
    lines = ["## Examples", "",
             "The engine wrote every transcription in this section with "
             f"`orthography2ipa.transcribe(text, \"{spec.code}\")`. They are "
             "engine output, not reference transcriptions."]
    if words:
        lines += ["", "| Spelling | Engine output |", "|:--|:--|"]
        for word in words:
            lines.append(f"| {word} | [{orthography2ipa.transcribe(word, spec.code)}] |")
    # A source that prints a transcription with no spelling gives nothing
    # to transcribe.
    rows = [r for r in atlas.primary_rows.get(spec.code, ())
            if r.get("orthography_vocalized") or r.get("orthography")]
    if len(rows) > 12:
        step = len(rows) / 12
        rows = [rows[int(n * step)] for n in range(12)]
    if rows:
        lines += ["", "The next table sets the engine output against worked "
                  "examples printed in a cited source, from the "
                  "[primary-source gold](../evaluation/datasets.md"
                  "#primary-source-gold-primary_sources). The rows are spread "
                  "evenly over that set. The last column says whether the two "
                  "transcriptions are the same string.", "",
                  "| Spelling | Printed in the source | Engine output | Source, page | Same |",
                  "|:--|:--|:--|:--|:--|"]
        cited = []
        for row in rows:
            text = row.get("orthography_vocalized") or row["orthography"]
            source = atlas.primary_sources.get(row["source"], {})
            surname = re.split(r"[,&]", source.get("authors", row["source"]))[0]
            engine = orthography2ipa.transcribe(text, spec.code)
            printed = row["source_notation"]
            same = printed.strip("/[] ") == engine
            lines.append(
                f"| {text} | {_clean(printed)} | [{engine}] | "
                f"{_clean(surname)} {source.get('year', '')}, p. {row['page']} | "
                f"{'yes' if same else 'no'} |")
            if row["source"] not in cited:
                cited.append(row["source"])
        refs = []
        for key in cited:
            source = atlas.primary_sources.get(key, {})
            ref = (f"{_clean(source.get('authors', key))} ({source.get('year', '')}). "
                   f"*{_clean(source.get('title', ''))}*. {_clean(source.get('venue', ''))}.")
            if source.get("url"):
                host = urllib.parse.urlparse(source["url"]).netloc.removeprefix("www.")
                ref += f" [{host}]({source['url']})"
            refs.append(ref)
        lines += [""] + [f"Source: {ref}" for ref in refs]
    if not words and not rows:
        lines += ["", "No example words are chosen for this page yet."]
    return "\n".join(lines)


def _child_lects(atlas: Atlas, code: str) -> List[str]:
    return [c for c in sorted(atlas.children.get(code, ()))
            if not atlas.raw[c].get("clade")]


def block_lects(atlas: Atlas, spec) -> str:
    children = _child_lects(atlas, spec.code)
    lines = ["## Related lects", ""]
    if not children:
        return "\n".join(lines + [f"No spec names `{spec.code}` as its parent."])
    lines += [f"These specs name `{spec.code}` as their parent. They are "
              "sorted by country, and a lect with no recorded country "
              "comes last.", ""]

    def place(code: str) -> str:
        countries = atlas.geography(code)[1]
        return ", ".join(sorted(atlas.country(c) for c in countries))

    for code in sorted(children, key=lambda c: (not place(c), place(c), c)):
        where = place(code)
        quality = atlas.raw[code].get("quality", "research")
        lines.append(f"- [{_clean(atlas.raw[code]['name'])}]({atlas.link(code)}) "
                     f"`{code}`: {where + ', ' if where else ''}{quality} tier")
    return "\n".join(lines)


def block_related(atlas: Atlas, spec) -> str:
    lineage = atlas.lineage(spec.code)
    found = [(name, url, what) for name, url, what, covers in RELATED
             if covers(spec, lineage)]
    lines = ["## Related repositories", ""]
    if not found:
        return "\n".join(lines + [
            "No downstream repository of the TigreGotico organisation covers "
            "this spec. The [o2i-lexicons](https://github.com/TigreGotico/"
            "o2i-lexicons) package ships no lexicon for it."])
    lines += ["| Repository | What it does with this spec |", "|:--|:--|"]
    lines += [f"| [{name}]({url}) | {what} |" for name, url, what in found]
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Pages


class TemplateError(ValueError):
    pass


def render_page(atlas: Atlas, code: str, text: str) -> str:
    """The page *text* with every generated block rebuilt from the data."""
    spec = atlas.spec(code)
    names = [m.group("name") for m in _BLOCK.finditer(text)]
    if names != list(BLOCKS):
        raise TemplateError(
            f"{code}.md: the atlas blocks are {names}, the template needs "
            f"{list(BLOCKS)} in that order")
    if sum(1 for line in text.splitlines() if line.startswith("# ")) != 1:
        raise TemplateError(f"{code}.md: a page has exactly one H1")

    def fill(match: re.Match) -> str:
        name, attrs = match.group("name"), match.group("attrs")
        if name == "examples":
            words = dict(_ATTR.findall(attrs)).get("words", "")
            body = block_examples(atlas, spec,
                                  [w.strip() for w in words.split("|") if w.strip()])
        else:
            body = globals()["block_" + name](atlas, spec)
        return f"<!-- atlas:{name} begin{attrs}-->\n{body}\n<!-- atlas:{name} end -->"

    text = re.sub(r"\A# .*", f"# {spec.name} (`{code}`)", text)
    return _BLOCK.sub(fill, text)


def scaffold(atlas: Atlas, code: str) -> str:
    """A new page for *code*: every block, and the two hand-written sections."""
    order = BLOCKS[:2]
    parts = [f"# {code}", ""]
    for name in order:
        parts += [f"<!-- atlas:{name} begin -->", f"<!-- atlas:{name} end -->", ""]
    parts += ["## Overview", "", "What is distinctive about this spec.", "",
              "## Weak points", "", "Where this spec is weak.", ""]
    for name in BLOCKS[2:]:
        parts += [f"<!-- atlas:{name} begin -->", f"<!-- atlas:{name} end -->", ""]
    return render_page(atlas, code, "\n".join(parts))


# --------------------------------------------------------------------------
# Indexes


def _entry(atlas: Atlas, code: str) -> str:
    name = atlas.raw[code]["name"]
    return f"[{_clean(name)}]({atlas.link(code)})"


def _index_head(title: str, intro: str) -> List[str]:
    return [f"# {title}", "", intro, "",
            "A stub has a name, a code and a place in the family tree, but no "
            "phonology yet. The tables list every spec above the stub tier. "
            "The stubs follow each table by name and code. To open a stub, "
            f"put its code after the `#` of an [explorer]({EXPLORER}) link, "
            f"as in the [entry for `mwl`]({EXPLORER}#mwl).", "",
            "`scripts/gen_language_atlas.py` writes this page. Do not edit it "
            "by hand.", ""]


def _listed(atlas: Atlas) -> List[str]:
    return [c for c in atlas.codes if not atlas.raw[c].get("clade")]


def _group_lines(atlas: Atlas, codes: Sequence[str], extra) -> List[str]:
    """A table of the specs above stub, then one line of the stubs."""
    full = [c for c in codes if c in atlas.pages
            or atlas.raw[c].get("quality", "research") != "stub"]
    stubs = [c for c in codes if c not in full]
    lines = []
    if full:
        lines += ["| Spec | Code | Tier | " + extra[0] + " |", "|:--|:--|:--|:--|"]
        for c in full:
            page = " (page)" if c in atlas.pages else ""
            lines.append(f"| {_entry(atlas, c)}{page} | `{c}` | "
                         f"{atlas.raw[c].get('quality', 'research')} | {extra[1](c)} |")
    if stubs:
        if lines:
            lines.append("")
        lines.append(f"Stubs ({len(stubs)}): " + ", ".join(
            f"{_clean(atlas.raw[c]['name'])} `{c}`" for c in stubs) + ".")
    return lines


def index_family(atlas: Atlas) -> str:
    groups: Dict[str, Dict[str, List[str]]] = defaultdict(lambda: defaultdict(list))
    for code in _listed(atlas):
        family = atlas.spec(code).family or "Unclassified"
        top = family.split(" > ")[0]
        groups[top][family].append(code)
    lines = _index_head(
        INDEXES["by-family.md"],
        "Every spec, grouped by its family path. A spec with a page links to "
        "the page, and every other spec links to its entry in the data "
        "explorer. Each family path has its own heading, so a page can link "
        "the exact branch.")
    lines += ["| Family | Specs |", "|:--|--:|"]
    for top in sorted(groups):
        count = sum(len(v) for v in groups[top].values())
        lines.append(f"| [{top}](#{_slug(top)}) | {count} |")
    for top in sorted(groups):
        lines += ["", f"## {top}"]
        for path in sorted(groups[top]):
            if path != top:
                lines += ["", f"### {path}"]
            lines += [""] + _group_lines(
                atlas, groups[top][path],
                ("Script", lambda c: atlas.raw[c].get("script", "")))
    return "\n".join(lines)


def index_region(atlas: Atlas) -> str:
    groups: Dict[str, Dict[str, List[str]]] = defaultdict(lambda: defaultdict(list))
    for code in _listed(atlas):
        macroarea, countries = atlas.geography(code)
        for country in countries or [None]:
            name = atlas.country(country) if country else "Country not recorded"
            groups[_area_group(macroarea)][name].append(code)
    lines = _index_head(
        INDEXES["by-region.md"],
        "Every spec, grouped by its Glottolog macroarea and then by country. "
        "A region subtag in the code names the country. Otherwise the "
        "countries are those Glottolog gives for the spec's own languoid. A "
        "spec spoken in several countries appears under each of them. A "
        "dialect with no languoid and no region subtag sits under its "
        "macroarea, with no country.")
    lines += ["| Macroarea | Countries |", "|:--|--:|"]
    for area in sorted(groups):
        lines.append(f"| [{area}](#{_slug(area)}) | {len(groups[area])} |")
    for area in sorted(groups):
        lines += ["", f"## {area}"]
        for country in sorted(groups[area]):
            lines += ["", f"### {country}", ""] + _group_lines(
                atlas, groups[area][country],
                ("Family", lambda c: atlas.spec(c).family or ""))
    return "\n".join(lines)


def index_script(atlas: Atlas) -> str:
    groups: Dict[str, List[str]] = defaultdict(list)
    for code in _listed(atlas):
        groups[atlas.raw[code].get("script") or "Unknown"].append(code)
    lines = _index_head(
        INDEXES["by-script.md"],
        "Every spec, grouped by the script it reads.")
    lines += ["| Script | Specs |", "|:--|--:|"]
    for script in sorted(groups):
        lines.append(f"| [{script}](#{_slug(script)}) | {len(groups[script])} |")
    for script in sorted(groups):
        lines += ["", f"## {script}", ""] + _group_lines(
            atlas, groups[script],
            ("Family", lambda c: atlas.spec(c).family or ""))
    return "\n".join(lines)


def index_az(atlas: Atlas) -> str:
    groups: Dict[str, List[str]] = defaultdict(list)
    for code in _listed(atlas):
        initial = unicodedata.normalize("NFD", atlas.raw[code]["name"])[:1].upper()
        groups[initial if "A" <= initial <= "Z" else "Other"].append(code)
    lines = _index_head(
        INDEXES["a-z.md"],
        "Every spec by name. The pages come first in the list below. Use the "
        "letters to jump.")
    pages = sorted(atlas.pages, key=lambda c: atlas.raw[c]["name"])
    lines += ["## Pages", "", "| Page | Code | Tier | Family |", "|:--|:--|:--|:--|"]
    lines += [f"| {_entry(atlas, c)} | `{c}` | {atlas.raw[c].get('quality')} | "
              f"{atlas.spec(c).family or ''} |" for c in pages]
    lines += ["", " · ".join(f"[{k}](#{_slug(k)})" for k in sorted(groups))]
    for initial in sorted(groups):
        codes = sorted(groups[initial], key=lambda c: (atlas.raw[c]["name"], c))
        lines += ["", f"## {initial}", ""] + _group_lines(
            atlas, codes, ("Family", lambda c: atlas.spec(c).family or ""))
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Snapshot


def refresh_snapshot() -> None:
    """Rebuild ``scripts/atlas_snapshot.json`` from Glottolog, SIL and CLDR."""
    def fetch(url: str) -> str:
        request = urllib.request.Request(url, headers={
            "User-Agent": "orthography2ipa-gen-language-atlas "
                          "(https://github.com/TigreGotico/orthography2ipa)"})
        with urllib.request.urlopen(request, timeout=120) as response:
            return response.read().decode("utf-8")

    specs = []
    for path in sorted(glob.glob(os.path.join(DATA_DIR, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            specs.append(json.load(fh))
    glottocodes = {s.get("glottolog_code") for s in specs} - {None}
    named = {s.get("glottolog_code") for s in specs
             if s.get("quality", "research") != "stub"} - {None}
    iso_codes = {s.get("iso639_3") for s in specs
                 if s.get("quality", "research") != "stub"} - {None}

    geography, glottolog_names = {}, {}
    reader = csv.DictReader(io.StringIO(fetch(
        "https://raw.githubusercontent.com/glottolog/glottolog-cldf/master/"
        "cldf/languages.csv")))
    for row in reader:
        code = row["Glottocode"]
        if code in glottocodes:
            countries = sorted(c for c in row["Countries"].split(";") if c)
            geography[code] = f"{row['Macroarea']}|{' '.join(countries)}"
        if code in named:
            glottolog_names[code] = row["Name"]
    iso = {}
    for line in fetch("https://iso639-3.sil.org/sites/iso639-3/files/downloads/"
                      "iso-639-3.tab").splitlines()[1:]:
        cells = line.split("\t")
        if cells[0] in iso_codes:
            iso[cells[0]] = cells[6]
    territories = json.loads(fetch(
        "https://raw.githubusercontent.com/unicode-org/cldr-json/main/cldr-json/"
        "cldr-localenames-full/main/en/territories.json"))
    names = territories["main"]["en"]["localeDisplayNames"]["territories"]
    countries = {k: v for k, v in names.items() if re.fullmatch(r"[A-Z]{2}", k)}
    sections = {
        "about": "Glottolog macroareas, countries and names, ISO 639-3 "
                 "reference names and CLDR country names for the language "
                 "atlas. A geography value is 'macroarea|countries'. Rebuild "
                 "with scripts/gen_language_atlas.py --refresh-snapshot.",
        "geography": geography,
        "glottolog_names": glottolog_names,
        "iso639_3": iso,
        "countries": countries,
    }
    lines = ["{"]
    for n, (key, value) in enumerate(sections.items()):
        comma = "," if n < len(sections) - 1 else ""
        if isinstance(value, str):
            lines.append(f"{json.dumps(key)}: {json.dumps(value)}{comma}")
            continue
        lines.append(f"{json.dumps(key)}: {{")
        items = sorted(value.items())
        lines += [f"{json.dumps(k, ensure_ascii=False)}: "
                  f"{json.dumps(v, ensure_ascii=False)}"
                  + ("," if i < len(items) - 1 else "")
                  for i, (k, v) in enumerate(items)]
        lines.append("}" + comma)
    lines.append("}")
    with open(SNAPSHOT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"snapshot: {len(geography)} languoids, {len(glottolog_names)} "
          f"languoid names, {len(iso)} ISO names, {len(countries)} countries")


# --------------------------------------------------------------------------
# Driver


def outputs(atlas: Atlas) -> Dict[str, str]:
    """Every file the atlas owns, as path relative to the repository root."""
    indexes = {"by-family.md": index_family(atlas),
               "by-region.md": index_region(atlas),
               "by-script.md": index_script(atlas),
               "a-z.md": index_az(atlas)}
    # The reading order lists the atlas pages from the A to Z index, so it
    # is read off the index about to be written, not the one on disk.
    nav = _docs_nav()
    order = nav.reading_order(az_text=indexes["a-z.md"])
    out = {}
    for code in sorted(atlas.pages):
        rel = f"languages/{code}.md"
        page = render_page(atlas, code, _read(os.path.join(LANG_DIR, f"{code}.md")))
        out["docs/" + rel] = nav.with_footer(page, rel, order)
    for name, body in indexes.items():
        rel = f"languages/{name}"
        footer = nav.footer(rel, order) if rel in order else "\n"
        out["docs/" + rel] = body.rstrip() + footer
    return out


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write the files")
    mode.add_argument("--check", action="store_true",
                      help="exit 1 when a file differs from what the data says")
    mode.add_argument("--scaffold", metavar="CODE",
                      help="create the page for CODE from the template")
    mode.add_argument("--refresh-snapshot", action="store_true",
                      help="rebuild scripts/atlas_snapshot.json over the network")
    args = ap.parse_args(argv)

    if args.refresh_snapshot:
        refresh_snapshot()
        return 0
    atlas = Atlas()
    if args.scaffold:
        code = registry.resolve(args.scaffold)
        path = os.path.join(LANG_DIR, f"{code}.md")
        if os.path.exists(path):
            print(f"{path} exists")
            return 1
        atlas.pages.add(code)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(scaffold(atlas, code))
        print(f"wrote {os.path.relpath(path, REPO_ROOT)}. Run --write to list "
              "it in the indexes, then scripts/docs_nav.py --write and "
              "scripts/gen_reference_docs.py --write.")
        return 0

    try:
        wanted = outputs(atlas)
    except TemplateError as exc:
        print(exc)
        return 1
    stale = []
    for rel, text in wanted.items():
        path = os.path.join(REPO_ROOT, rel)
        current = _read(path) if os.path.exists(path) else None
        if current == text:
            continue
        stale.append(rel)
        if args.write:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
    if not stale:
        print(f"atlas up to date: {len(atlas.pages)} pages, {len(INDEXES)} indexes")
        return 0
    if args.write:
        print("wrote " + ", ".join(stale))
        return 0
    print("stale: " + ", ".join(stale)
          + "\nRun: PYTHONPATH=$PWD python scripts/gen_language_atlas.py --write")
    return 1


if __name__ == "__main__":
    sys.exit(main())
