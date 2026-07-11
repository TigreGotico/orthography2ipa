#!/usr/bin/env python3
"""Generate the self-contained language-data explorer static page.

Enumerates every registered language spec (fully resolved, so inherited
fields are populated), joins per-language benchmark rows from
``benchmarks/results.json``, and emits ONE self-contained HTML file
(``docs/explorer.html``) with the data embedded as a minified JSON blob.

No network access, no timestamps, no randomness: given the same specs
and the same results file, the output is byte-identical across runs.

Usage::

    python scripts/gen_explorer.py
"""
from __future__ import annotations

import json
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

import orthography2ipa as o2i  # noqa: E402

RESULTS_PATH = os.path.join(_ROOT, "benchmarks", "results.json")
OUTPUT_PATH = os.path.join(_ROOT, "docs", "explorer.html")


def _load_benchmarks():
    """Return {code: [row, ...]} keyed by benchmark 'lang' code."""
    if not os.path.exists(RESULTS_PATH):
        return {}
    with open(RESULTS_PATH, "r", encoding="utf-8") as fh:
        rows = json.load(fh)
    by_lang = {}
    for row in rows:
        by_lang.setdefault(row["lang"], []).append(row)
    for code in by_lang:
        by_lang[code].sort(key=lambda r: (r.get("dataset", ""), r.get("n", 0)))
    return by_lang


def _spec_to_dict(spec, bench_by_lang):
    ancestors = [
        {"code": a.code, "role": a.role.value, "weight": a.weight, "notes": a.notes}
        for a in (spec.ancestors or ())
    ]
    sources = [
        {
            "id": s.id,
            "author": s.author,
            "year": s.year,
            "title": s.title,
            "publisher": s.publisher,
            "url": s.url,
            "wikipedia_url": s.wikipedia_url,
            "pages": s.pages,
            "notes": s.notes,
        }
        for s in (spec.sources or ())
    ]

    positional = {}
    for grapheme, pos_map in (spec.positional_graphemes or {}).items():
        positional[grapheme] = {
            (pos.value if hasattr(pos, "value") else str(pos)): list(ipas)
            for pos, ipas in pos_map.items()
        }

    allophone_rules = [
        {
            "id": r.id,
            "phonemes": list(r.phonemes),
            "surface": r.surface,
            "word_initial": r.word_initial,
            "word_final": r.word_final,
            "stress": r.stress,
            "syllable_position": r.syllable_position,
            "preceded_by": r.preceded_by,
            "followed_by": r.followed_by,
            "preceded_by_phoneme": list(r.preceded_by_phoneme),
            "followed_by_phoneme": list(r.followed_by_phoneme),
            "notes": r.notes,
        }
        for r in (spec.allophone_rules or ())
    ]

    sandhi_rules = [
        {
            "id": r.id,
            "name": r.name,
            "left_context": r.left_context,
            "right_context": r.right_context,
            "transform": r.transform,
            "obligatory": r.obligatory,
            "notes": r.notes,
        }
        for r in (spec.sandhi_rules or ())
    ]

    timespan = None
    if spec.timespan is not None:
        timespan = {"start_year": spec.timespan.start_year, "end_year": spec.timespan.end_year}

    return {
        "code": spec.code,
        "name": spec.name,
        "family": spec.family,
        "family_path": list(spec.family_path),
        "clade": spec.clade,
        "script": spec.script,
        "script_type": spec.script_type.value if spec.script_type else None,
        "quality": spec.quality.value if spec.quality else None,
        "parent": spec.parent,
        "ancestors": ancestors,
        "glottolog_code": spec.glottolog_code,
        "iso639_3": spec.iso639_3,
        "graphemes": dict(sorted((spec.graphemes or {}).items())),
        "allophones": dict(sorted((spec.allophones or {}).items())),
        "positional_graphemes": dict(sorted(positional.items())),
        "allophone_rules": allophone_rules,
        "sandhi_rules": sandhi_rules,
        "tone_inventory": spec.tone_inventory,
        "sources": sources,
        "wikipedia": list(spec.wikipedia or ()),
        "notes": spec.notes or "",
        "timespan": timespan,
        "benchmarks": bench_by_lang.get(spec.code, []),
    }


def build_data():
    bench_by_lang = _load_benchmarks()
    # Clade nodes are included: they are the backbone of the ancestry tree
    # the explorer renders, and the source of every language's family path.
    codes = sorted(o2i.available_codes(include_clades=True))
    languages = {}
    for code in codes:
        spec = o2i.get(code)
        languages[code] = _spec_to_dict(spec, bench_by_lang)

    # Structural family/proto flag: a node used as someone's genetic parent
    # whose timespan has ENDED is an ancestry grouping (Galaico-Portuguese
    # 1100–1400, Medieval Portuguese 1200–1500, Hispanic Latin 200–900), not a
    # living variety. Still-spoken languages that also parent a sub-variety
    # (gl, es-ES, pt-PT) have an open-ended timespan, so they are NOT flagged —
    # this avoids mislabelling a modern language whose gold is keyed under a
    # bare code (es vs es-ES).
    parent_set = {d["parent"] for d in languages.values() if d["parent"]}
    for code, d in languages.items():
        ts = d["timespan"]
        ended = bool(ts and ts.get("end_year") is not None)
        # A grouping is a genetic parent that is either a closed historical
        # stage (ended timespan: Galaico-Portuguese, Medieval Portuguese) or a
        # pure ancestry stub carrying no data of its own ("… (family node)",
        # proto-language nodes) — those have tier `stub` and often no timespan.
        d["is_family"] = bool(d["clade"] or (code in parent_set
                                            and (ended or d["quality"] == "stub")))

    # Every step of every classification path is selectable, so the filter
    # offers both "Romance" and "Ibero-Romance".
    families = sorted({f for d in languages.values() for f in d["family_path"]}
                      | {d["family"] for d in languages.values()
                         if d["family"] and not d["family_path"]})
    scripts = sorted({d["script"] for d in languages.values() if d["script"]})
    tiers = ["production", "research", "skeleton", "stub"]
    counts = {t: 0 for t in tiers}
    for d in languages.values():
        q = d["quality"]
        if q in counts:
            counts[q] += 1

    return {
        "codes": codes,
        "languages": languages,
        "families": families,
        "scripts": scripts,
        "tiers": tiers,
        "counts": counts,
    }


PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>orthography2ipa — language data explorer</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root {
  --bg: #0b0f14;
  --panel: #121821;
  --panel2: #161d28;
  --border: #26303d;
  --text: #e4e9f0;
  --muted: #93a1b5;
  --accent: #5ec2ff;
  --production: #37d67a;
  --research: #5ec2ff;
  --skeleton: #f5c344;
  --stub: #b0b8c4;
  font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
}
@media (prefers-color-scheme: light) {
  :root {
    --bg: #f6f8fb;
    --panel: #ffffff;
    --panel2: #eef1f6;
    --border: #d8dee6;
    --text: #1a2027;
    --muted: #5a6779;
    --accent: #0b6ec2;
  }
}
:root[data-theme="dark"] {
  --bg: #0b0f14; --panel: #121821; --panel2: #161d28; --border: #26303d;
  --text: #e4e9f0; --muted: #93a1b5; --accent: #5ec2ff;
}
:root[data-theme="light"] {
  --bg: #f6f8fb; --panel: #ffffff; --panel2: #eef1f6; --border: #d8dee6;
  --text: #1a2027; --muted: #5a6779; --accent: #0b6ec2;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--bg); color: var(--text); height: 100%; }
body { display: flex; flex-direction: column; min-height: 100vh; }
a { color: var(--accent); }
header {
  padding: 14px 20px; border-bottom: 1px solid var(--border); background: var(--panel);
}
header h1 { margin: 0 0 4px 0; font-size: 1.3rem; }
header .tagline { color: var(--muted); font-size: 0.9rem; margin-bottom: 8px; }
.legend { display: flex; flex-wrap: wrap; gap: 14px; align-items: center; font-size: 0.82rem; color: var(--muted); }
.legend .dot { display: inline-block; width: 9px; height: 9px; border-radius: 50%; margin-right: 5px; vertical-align: middle; }
.dot.production { background: var(--production); }
.dot.research { background: var(--research); }
.dot.skeleton { background: var(--skeleton); }
.dot.stub { background: var(--stub); }
.caveat { margin-top: 6px; font-size: 0.8rem; color: var(--muted); }
.counts { margin-top: 6px; font-size: 0.82rem; color: var(--muted); }
main { flex: 1; display: flex; min-height: 0; }
#sidebar {
  width: 320px; min-width: 260px; border-right: 1px solid var(--border);
  display: flex; flex-direction: column; background: var(--panel);
}
#sidebar .controls { padding: 10px; border-bottom: 1px solid var(--border); display: flex; flex-direction: column; gap: 6px; }
#sidebar input[type="text"], #sidebar select {
  width: 100%; padding: 6px 8px; background: var(--panel2); color: var(--text);
  border: 1px solid var(--border); border-radius: 4px; font-size: 0.85rem;
}
#lang-list { flex: 1; overflow-y: auto; }
#lang-list ul { list-style: none; margin: 0; padding: 0; }
#lang-list li a {
  display: flex; align-items: center; gap: 8px; padding: 6px 12px; text-decoration: none;
  color: var(--text); font-size: 0.85rem; border-bottom: 1px solid var(--border);
}
#lang-list li a:hover, #lang-list li a.active { background: var(--panel2); }
#lang-list li a .code { color: var(--muted); font-family: monospace; min-width: 4.5em; }
#lang-list li a .name { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
#lang-list li a .tier-pill { font-size: 0.6rem; padding: 1px 6px; flex-shrink: 0; }
#detail { flex: 1; overflow-y: auto; padding: 20px 26px; }
#detail h2 { margin-top: 0; }
.badge {
  display: inline-block; padding: 3px 10px; border-radius: 10px; font-size: 0.8rem;
  margin-left: 8px; color: #08131f; font-weight: 700; letter-spacing: 0.03em;
  text-transform: uppercase; vertical-align: middle;
}
.badge.production { background: var(--production); }
.badge.research { background: var(--research); }
.badge.skeleton { background: var(--skeleton); }
.badge.stub { background: var(--stub); }
/* Tier pill reused inside tables/lists — no left margin, tighter. */
.tier-pill {
  display: inline-block; padding: 2px 8px; border-radius: 9px; font-size: 0.72rem;
  color: #08131f; font-weight: 700; letter-spacing: 0.02em; text-transform: uppercase;
}
.tier-pill.production { background: var(--production); }
.tier-pill.research { background: var(--research); }
.tier-pill.skeleton { background: var(--skeleton); }
.tier-pill.stub { background: var(--stub); }
/* Coloured left rail on the detail header, keyed to the tier. */
.tier-rail { border-left: 5px solid var(--border); padding-left: 12px; margin-bottom: 12px; }
.tier-rail.production { border-left-color: var(--production); }
.tier-rail.research { border-left-color: var(--research); }
.tier-rail.skeleton { border-left-color: var(--skeleton); }
.tier-rail.stub { border-left-color: var(--stub); }
.tier-rail h2 { margin: 0; }
.tier-desc { color: var(--muted); font-size: 0.82rem; margin-top: 4px; }
.meta-line { color: var(--muted); margin-bottom: 16px; }
section { margin-bottom: 26px; }
section h3 { border-bottom: 1px solid var(--border); padding-bottom: 4px; }
.table-wrap { overflow-x: auto; border: 1px solid var(--border); border-radius: 6px; }
table { border-collapse: collapse; width: 100%; font-size: 0.85rem; }
th, td { text-align: left; padding: 6px 10px; border-bottom: 1px solid var(--border); white-space: nowrap; }
th { background: var(--panel2); position: sticky; top: 0; }
td.wrap, th.wrap { white-space: normal; }
.notes-box {
  background: var(--panel2); border: 1px solid var(--border); border-radius: 6px;
  padding: 2px 16px; font-size: 0.9rem; line-height: 1.55;
}
.notes-box p { margin: 12px 0; }
.notes-box p strong { color: var(--text); font-weight: 700; }
.notes-box.warn { border-color: var(--skeleton); border-left-width: 4px; }
ul.plain { list-style: none; padding: 0; margin: 0; }
ul.plain li { padding: 4px 0; border-bottom: 1px dashed var(--border); font-size: 0.88rem; }
.empty { color: var(--muted); font-style: italic; }
.chip { display: inline-block; background: var(--panel2); border: 1px solid var(--border);
  border-radius: 4px; padding: 2px 6px; margin: 2px; font-size: 0.8rem; }
footer { padding: 10px 20px; border-top: 1px solid var(--border); color: var(--muted); font-size: 0.8rem; background: var(--panel); }

/* ── Lineage view tokens (complement the existing blue accent) ──────────── */
:root {
  --edge-parent: #5aa89d; --edge-adstrate: #dca94e;
  --edge-substrate: #c76a6a; --edge-superstrate: #8593c4;
}
@media (prefers-color-scheme: light) {
  :root { --edge-parent: #3e7c74; --edge-adstrate: #c0872d; --edge-substrate: #9a3b3b; --edge-superstrate: #4c5b8a; }
}
:root[data-theme="dark"] { --edge-parent: #5aa89d; --edge-adstrate: #dca94e; --edge-substrate: #c76a6a; --edge-superstrate: #8593c4; }
:root[data-theme="light"] { --edge-parent: #3e7c74; --edge-adstrate: #c0872d; --edge-substrate: #9a3b3b; --edge-superstrate: #4c5b8a; }

/* View switcher */
.viewnav { display: flex; gap: 4px; padding: 8px 20px 0; background: var(--panel); }
.viewnav button {
  font: inherit; font-size: 0.85rem; font-weight: 600; color: var(--muted);
  background: transparent; border: 1px solid transparent; border-bottom: none;
  padding: 8px 16px; border-radius: 7px 7px 0 0; cursor: pointer;
}
.viewnav button[aria-selected="true"] { color: var(--text); background: var(--bg); border-color: var(--border); }
.viewnav button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.view { flex: 1; min-height: 0; }
.view[hidden] { display: none !important; }
#view-browse { display: flex; min-height: 0; }

/* Family tree */
#view-tree, #view-graph { overflow: auto; padding: 18px 24px; }
.tree-toolbar { display: flex; gap: 8px; align-items: center; margin-bottom: 14px; flex-wrap: wrap; }
.tree-toolbar button { font: inherit; font-size: 0.8rem; color: var(--text); background: var(--panel2);
  border: 1px solid var(--border); border-radius: 5px; padding: 5px 10px; cursor: pointer; }
.tree-toolbar .hint { color: var(--muted); font-size: 0.8rem; }
.tree, .tree ul { list-style: none; margin: 0; padding: 0; }
.tree ul { padding-left: 22px; position: relative; }
.tree ul ul::before { content: ""; position: absolute; left: 9px; top: 0; bottom: 13px; width: 1px; background: var(--border); }
.tree li { position: relative; }
.trow { display: flex; align-items: center; gap: 8px; padding: 3px 8px; border-radius: 6px; }
.trow:hover { background: var(--panel2); }
.trow.toggle { cursor: pointer; }
.trow .tw { width: 13px; font-size: 0.65rem; color: var(--muted); flex: none; transition: transform 0.12s; text-align: center; }
.collapsed > .trow .tw { transform: rotate(-90deg); }
.collapsed > ul { display: none; }
.trow .tdot { width: 9px; height: 9px; border-radius: 50%; flex: none; }
.trow .tdot.production { background: var(--production); } .trow .tdot.research { background: var(--research); }
.trow .tdot.skeleton { background: var(--skeleton); } .trow .tdot.stub { background: var(--stub); }
.trow .tname { color: var(--text); text-decoration: none; }
.trow .tname:hover { text-decoration: underline; }
.trow.fam .tname { font-style: italic; font-weight: 600; }
.trow.fam .tdot { background: transparent; border: 1.5px dashed var(--muted); }
.trow .tcode { font-family: monospace; font-size: 0.74rem; color: var(--muted); }
.trow .fam-tag { font-family: monospace; font-size: 0.6rem; text-transform: uppercase; letter-spacing: 0.04em;
  color: var(--edge-parent); border: 1px solid var(--edge-parent); border-radius: 10px; padding: 0 6px; }
.trow.sel { background: color-mix(in srgb, var(--accent) 16%, transparent); box-shadow: inset 0 0 0 1px var(--accent); }

/* Contact graph */
.graph-head { display: flex; gap: 10px; align-items: baseline; flex-wrap: wrap; margin-bottom: 6px; }
.graph-head h2 { margin: 0; font-size: 1.15rem; }
.graph-head .sub { color: var(--muted); font-size: 0.85rem; }
.graph-legend { display: flex; gap: 16px; flex-wrap: wrap; font-size: 0.8rem; color: var(--muted); margin: 8px 0 12px; }
.graph-legend span { display: inline-flex; align-items: center; gap: 6px; }
.graph-legend i { width: 22px; height: 0; display: inline-block; }
.lg-parent { border-top: 2.5px solid var(--edge-parent); }
.lg-adstrate { border-top: 2.5px dashed var(--edge-adstrate); }
.lg-substrate { border-top: 2.5px dotted var(--edge-substrate); }
.lg-superstrate { border-top: 2.5px dashed var(--edge-superstrate); }
#graph-svg { width: 100%; max-width: 760px; height: auto; display: block; }
#graph-svg text { font-family: monospace; fill: var(--text); }
#graph-svg .gnode { cursor: pointer; }
#graph-svg .gnode circle { transition: r 0.1s; }
.graph-empty { color: var(--muted); font-style: italic; }
</style>
</head>
<body>
<header>
  <h1>orthography2ipa — language data explorer</h1>
  <div class="tagline">Every registered orthography → IPA spec, with its cited academic sources, in one browsable page.</div>
  <div class="legend">
    <span><span class="dot production"></span>production — full coverage, regression-tested, cited sources</span>
    <span><span class="dot research"></span>research — validated against published phonology; positional rules present</span>
    <span><span class="dot skeleton"></span>skeleton — auto-generated graphemes/allophones, unvalidated</span>
    <span><span class="dot stub"></span>stub — code + name + family + script only</span>
  </div>
  <div class="caveat">Gold benchmark data is a grain of salt — PER is directional, not a certification. See
    <a href="benchmarks.md">docs/benchmarks.md</a> and <a href="scoreboard.md">docs/scoreboard.md</a>.</div>
  <div class="counts" id="counts-line"></div>
</header>
<nav class="viewnav" role="tablist" aria-label="Explorer views">
  <button role="tab" id="vb-browse" aria-selected="true" aria-controls="view-browse">Browse</button>
  <button role="tab" id="vb-tree" aria-selected="false" aria-controls="view-tree">Family tree</button>
  <button role="tab" id="vb-graph" aria-selected="false" aria-controls="view-graph">Contact graph</button>
</nav>
<main>
  <div class="view" id="view-browse" role="tabpanel" aria-labelledby="vb-browse">
    <div id="sidebar">
      <div class="controls">
        <input type="text" id="search" placeholder="Search code, name, family...">
        <select id="filter-family"><option value="">All families</option></select>
        <select id="filter-script"><option value="">All scripts</option></select>
        <select id="filter-tier"><option value="">All tiers</option></select>
      </div>
      <div id="lang-list"><ul id="lang-ul"></ul></div>
    </div>
    <div id="detail"><p class="empty">Select a language from the list.</p></div>
  </div>
  <div class="view" id="view-tree" hidden role="tabpanel" aria-labelledby="vb-tree">
    <div class="tree-toolbar">
      <button id="tree-expand">Expand all</button>
      <button id="tree-collapse">Collapse all</button>
      <span class="hint">Genetic descent from each spec's <code>parent</code>. Dashed rings are ancestry groupings (proto-languages, medieval stages) with no gold of their own. Click a name to open it.</span>
    </div>
    <ul class="tree" id="tree-root"></ul>
  </div>
  <div class="view" id="view-graph" hidden role="tabpanel" aria-labelledby="vb-graph">
    <div class="graph-head">
      <h2 id="graph-title">Contact graph</h2>
      <span class="sub" id="graph-sub"></span>
    </div>
    <div class="graph-legend">
      <span><i class="lg-parent"></i>parent (descent)</span>
      <span><i class="lg-adstrate"></i>adstrate</span>
      <span><i class="lg-substrate"></i>substrate</span>
      <span><i class="lg-superstrate"></i>superstrate</span>
    </div>
    <div id="graph-holder"><p class="graph-empty">Select a language (from Browse or the tree) to see its lineage &amp; contact neighbourhood.</p></div>
  </div>
</main>
<footer>orthography2ipa · static, offline, no network requests · data generated from the registry</footer>
<script>
const DATA = __DATA_JSON__;
(function () {
  "use strict";

  function esc(s) {
    if (s === null || s === undefined) return "";
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  const TIER_DESC = {
    production: "full coverage, regression-tested, cited sources",
    research: "validated against published phonology; positional rules present",
    skeleton: "auto-generated graphemes/allophones, unvalidated",
    stub: "code + name + family + script only"
  };

  // Turn a single run-on notes string into readable paragraphs. Splits on
  // explicit newlines, on parenthesised enumerators "(1)"/"(a)", and before
  // ALL-CAPS section labels ending in a colon or dash; a leading CAPS label
  // is then bolded. Escaping happens per-segment so no markup leaks.
  function renderNotes(text) {
    const SEP = "\\u0001";
    const segments = [];
    String(text).split(/\\n+/).forEach(function (block) {
      let b = block.trim();
      if (!b) return;
      // Break before "(1) " / "(a) " enumerators.
      b = b.replace(/\\s+(?=\\((?:\\d+|[a-z])\\)\\s)/g, SEP);
      // Break before an ALL-CAPS section label (>=3 chars) that ends in
      // ":" or a dash, when it follows sentence punctuation.
      b = b.replace(
        /([.;:])\\s+(?=[A-Z][A-Z0-9 \\/’'&()-]{2,}[:—-])/g, "$1" + SEP);
      b.split(SEP).forEach(function (seg) {
        seg = seg.trim();
        if (seg) segments.push(seg);
      });
    });
    if (!segments.length) segments.push(String(text).trim());
    return segments.map(function (seg) {
      let e = esc(seg);
      // Bold a leading ALL-CAPS section label (after an optional "(n)"
      // enumerator) up to and including its terminating colon or em-dash.
      e = e.replace(
        /^(\\((?:\\d+|[a-z])\\)\\s+)?([A-Z0-9][A-Z0-9 \\/’'&()-]{2,}?(?::|\\s—))/,
        function (m, en, lbl) { return (en || "") + "<strong>" + lbl + "</strong>"; });
      return "<p>" + e + "</p>";
    }).join("");
  }

  const countsEl = document.getElementById("counts-line");
  countsEl.textContent =
    DATA.counts.production + " production · " +
    DATA.counts.research + " research · " +
    DATA.counts.skeleton + " skeleton · " +
    DATA.counts.stub + " stub";

  const familySel = document.getElementById("filter-family");
  DATA.families.forEach(function (f) {
    const o = document.createElement("option"); o.value = f; o.textContent = f;
    familySel.appendChild(o);
  });
  const scriptSel = document.getElementById("filter-script");
  DATA.scripts.forEach(function (s) {
    const o = document.createElement("option"); o.value = s; o.textContent = s;
    scriptSel.appendChild(o);
  });
  const tierSel = document.getElementById("filter-tier");
  DATA.tiers.forEach(function (t) {
    const o = document.createElement("option"); o.value = t; o.textContent = t;
    tierSel.appendChild(o);
  });

  const listEl = document.getElementById("lang-ul");
  const searchEl = document.getElementById("search");

  function matchesFilters(d) {
    const q = searchEl.value.trim().toLowerCase();
    if (q) {
      const hay = (d.code + " " + d.name + " " + d.family + " "
                   + (d.family_path || []).join(" ")).toLowerCase();
      if (hay.indexOf(q) === -1) return false;
    }
    if (familySel.value && !(d.family_path || []).includes(familySel.value)
        && d.family !== familySel.value) return false;
    if (scriptSel.value && d.script !== scriptSel.value) return false;
    if (tierSel.value && d.quality !== tierSel.value) return false;
    return true;
  }

  function renderList() {
    listEl.innerHTML = "";
    const frag = document.createDocumentFragment();
    DATA.codes.forEach(function (code) {
      const d = DATA.languages[code];
      if (!matchesFilters(d)) return;
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = "#" + encodeURIComponent(code);
      a.dataset.code = code;
      const dot = document.createElement("span");
      dot.className = "dot " + esc(d.quality);
      const codeSpan = document.createElement("span");
      codeSpan.className = "code"; codeSpan.textContent = code;
      const nameSpan = document.createElement("span");
      nameSpan.className = "name"; nameSpan.textContent = d.name;
      const tierTag = document.createElement("span");
      tierTag.className = "tier-pill " + esc(d.quality);
      tierTag.textContent = d.quality;
      a.appendChild(dot); a.appendChild(codeSpan); a.appendChild(nameSpan);
      a.appendChild(tierTag);
      li.appendChild(a);
      frag.appendChild(li);
    });
    listEl.appendChild(frag);
    highlightActive();
  }

  function highlightActive() {
    const current = currentCode();
    Array.prototype.forEach.call(listEl.querySelectorAll("a"), function (a) {
      a.classList.toggle("active", a.dataset.code === current);
    });
  }

  function currentCode() {
    return decodeURIComponent(location.hash.replace(/^#/, ""));
  }

  function goTo(code) {
    location.hash = "#" + encodeURIComponent(code);
  }

  function renderBenchTable(rows) {
    if (!rows || !rows.length) return "";
    let html = '<div class="table-wrap"><table><thead><tr>' +
      "<th>dataset</th><th>n</th><th>PER</th><th>95% CI</th><th>exact match</th>" +
      "<th>provenance</th><th>quality tier</th></tr></thead><tbody>";
    rows.forEach(function (r) {
      const ci = (r.per_ci_low !== undefined && r.per_ci_high !== undefined)
        ? esc(r.per_ci_low) + "–" + esc(r.per_ci_high) : "";
      const tier = esc(r.quality_tier);
      const tierCell = tier
        ? '<span class="tier-pill ' + tier + '">' + tier + "</span>" : "";
      html += "<tr><td>" + esc(r.dataset) + "</td><td>" + esc(r.n) + "</td><td>" +
        esc(r.per) + "</td><td>" + ci + "</td><td>" + esc(r.exact_match) + "</td><td>" +
        esc(r.provenance) + "</td><td>" + tierCell + "</td></tr>";
    });
    html += "</tbody></table></div>";
    return html;
  }

  function ancestorLink(code) {
    const d = DATA.languages[code];
    const label = d ? (code + " — " + esc(d.name)) : esc(code);
    if (!d) return '<span class="chip">' + esc(code) + " (unregistered)</span>";
    return '<a class="chip" href="#' + encodeURIComponent(code) + '">' + label + "</a>";
  }

  function renderAncestry(d) {
    let html = "";
    if (d.parent) {
      html += "<p>Parent: " + ancestorLink(d.parent) + "</p>";
    }
    if (d.ancestors && d.ancestors.length) {
      html += '<div class="table-wrap"><table><thead><tr><th>ancestor</th><th>role</th><th>weight</th><th class="wrap">notes</th></tr></thead><tbody>';
      d.ancestors.forEach(function (a) {
        html += "<tr><td>" + ancestorLink(a.code) + "</td><td>" + esc(a.role) +
          "</td><td>" + esc(a.weight) + "</td><td class=\\"wrap\\">" + esc(a.notes) + "</td></tr>";
      });
      html += "</tbody></table></div>";
    }
    if (!html) html = '<p class="empty">No ancestry recorded.</p>';
    return html;
  }

  function renderGraphemes(map) {
    const keys = Object.keys(map || {});
    if (!keys.length) return '<p class="empty">No grapheme mappings.</p>';
    let html = '<div class="table-wrap"><table><thead><tr><th>grapheme</th><th>IPA candidates</th></tr></thead><tbody>';
    keys.forEach(function (g) {
      html += "<tr><td><code>" + esc(g) + "</code></td><td>" + esc((map[g] || []).join(", ")) + "</td></tr>";
    });
    html += "</tbody></table></div>";
    return html;
  }

  function renderAllophones(map) {
    const keys = Object.keys(map || {});
    if (!keys.length) return '<p class="empty">No allophone data.</p>';
    let html = '<div class="table-wrap"><table><thead><tr><th>phoneme</th><th>surface realisations</th></tr></thead><tbody>';
    keys.forEach(function (p) {
      html += "<tr><td><code>" + esc(p) + "</code></td><td>" + esc((map[p] || []).join(", ")) + "</td></tr>";
    });
    html += "</tbody></table></div>";
    return html;
  }

  function renderPositional(map) {
    const keys = Object.keys(map || {});
    if (!keys.length) return "";
    let html = '<div class="table-wrap"><table><thead><tr><th>grapheme</th><th>position</th><th>IPA candidates</th></tr></thead><tbody>';
    keys.forEach(function (g) {
      const posMap = map[g];
      Object.keys(posMap).forEach(function (pos) {
        html += "<tr><td><code>" + esc(g) + "</code></td><td>" + esc(pos) + "</td><td>" +
          esc((posMap[pos] || []).join(", ")) + "</td></tr>";
      });
    });
    html += "</tbody></table></div>";
    return html;
  }

  function renderAllophoneRules(rules) {
    if (!rules || !rules.length) return "";
    let html = '<div class="table-wrap"><table><thead><tr><th>id</th><th>phonemes</th><th>surface</th><th class="wrap">conditions</th></tr></thead><tbody>';
    rules.forEach(function (r) {
      const conds = [];
      if (r.word_initial !== null && r.word_initial !== undefined) conds.push("word_initial=" + r.word_initial);
      if (r.word_final !== null && r.word_final !== undefined) conds.push("word_final=" + r.word_final);
      if (r.stress) conds.push("stress=" + r.stress);
      if (r.syllable_position) conds.push("syllable_position=" + r.syllable_position);
      if (r.preceded_by) conds.push("preceded_by=" + r.preceded_by);
      if (r.followed_by) conds.push("followed_by=" + r.followed_by);
      if (r.preceded_by_phoneme && r.preceded_by_phoneme.length) conds.push("preceded_by_phoneme=" + r.preceded_by_phoneme.join("/"));
      if (r.followed_by_phoneme && r.followed_by_phoneme.length) conds.push("followed_by_phoneme=" + r.followed_by_phoneme.join("/"));
      if (r.notes) conds.push(r.notes);
      html += "<tr><td><code>" + esc(r.id) + "</code></td><td>" + esc(r.phonemes.join(", ")) +
        "</td><td>" + esc(r.surface) + "</td><td class=\\"wrap\\">" + esc(conds.join("; ")) + "</td></tr>";
    });
    html += "</tbody></table></div>";
    return html;
  }

  function renderSources(sources) {
    if (!sources || !sources.length) return '<p class="empty">No cited sources.</p>';
    let html = '<ul class="plain">';
    sources.forEach(function (s) {
      let line = esc(s.author) + " (" + esc(s.year) + "). <em>" + esc(s.title) + "</em>";
      if (s.publisher) line += ". " + esc(s.publisher);
      if (s.pages) line += ", " + esc(s.pages);
      line += ".";
      if (s.url) line += ' <a href="' + esc(s.url) + '" target="_blank" rel="noopener">source</a>';
      if (s.wikipedia_url) line += ' <a href="' + esc(s.wikipedia_url) + '" target="_blank" rel="noopener">wikipedia</a>';
      if (s.notes) line += "<br><span style=\\"color:var(--muted)\\">" + esc(s.notes) + "</span>";
      html += "<li>" + line + "</li>";
    });
    html += "</ul>";
    return html;
  }

  function render(code) {
    const detail = document.getElementById("detail");
    const d = DATA.languages[code];
    if (!d) {
      detail.innerHTML = '<p class="empty">Language "' + esc(code) + '" not found.</p>';
      return;
    }
    let html = "";
    const tier = esc(d.quality);
    const tierDesc = TIER_DESC[d.quality] || "";
    html += '<div class="tier-rail ' + tier + '">' +
      "<h2>" + esc(d.name) + '<span class="badge ' + tier + '">' + tier + "</span></h2>" +
      (tierDesc ? '<div class="tier-desc"><strong>' + tier + "</strong> — " + esc(tierDesc) + "</div>" : "") +
      "</div>";
    html += '<div class="meta-line">code <code>' + esc(d.code) + "</code> · family " + esc(d.family) +
      " · script " + esc(d.script) + (d.script_type ? " (" + esc(d.script_type) + ")" : "") + "</div>";

    if (d.benchmarks && d.benchmarks.length) {
      html += "<section><h3>Gold benchmark results</h3>" + renderBenchTable(d.benchmarks) + "</section>";
    }

    html += "<section><h3>Ancestry</h3>" + renderAncestry(d) + "</section>";
    html += "<section><h3>Graphemes</h3>" + renderGraphemes(d.graphemes) + "</section>";
    html += "<section><h3>Allophones</h3>" + renderAllophones(d.allophones) + "</section>";

    const posHtml = renderPositional(d.positional_graphemes);
    if (posHtml) html += "<section><h3>Positional graphemes</h3>" + posHtml + "</section>";

    const ruleHtml = renderAllophoneRules(d.allophone_rules);
    if (ruleHtml) html += "<section><h3>Allophone rules</h3>" + ruleHtml + "</section>";

    html += "<section><h3>Sources</h3>" + renderSources(d.sources) + "</section>";

    if (d.notes) {
      const looksWarning = /\\b(warning|caution|contract|pinyin|jamo|tashkeel|requires|must be)\\b/i.test(d.notes);
      html += '<section><h3>Notes</h3><div class="notes-box' + (looksWarning ? " warn" : "") + '">' + renderNotes(d.notes) + "</div></section>";
    }

    if (d.wikipedia && d.wikipedia.length) {
      html += "<section><h3>Wikipedia</h3><ul class=\\"plain\\">";
      d.wikipedia.forEach(function (u) {
        html += '<li><a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(u) + "</a></li>";
      });
      html += "</ul></section>";
    }

    detail.innerHTML = html;
  }

  function onHashChange() {
    const code = currentCode();
    if (code && DATA.languages[code]) {
      render(code);
    } else if (!code) {
      document.getElementById("detail").innerHTML = '<p class="empty">Select a language from the list.</p>';
    }
    highlightActive();
  }

  // ── View switching ────────────────────────────────────────────────────
  const VIEWS = { "vb-browse": "view-browse", "vb-tree": "view-tree", "vb-graph": "view-graph" };
  let activeView = "vb-browse";
  function switchView(btnId) {
    activeView = btnId;
    Object.keys(VIEWS).forEach(function (b) {
      const on = b === btnId;
      const btn = document.getElementById(b);
      btn.setAttribute("aria-selected", on ? "true" : "false");
      document.getElementById(VIEWS[b]).hidden = !on;
    });
    if (btnId === "vb-tree") { renderTree(); markTreeSelection(); }
    if (btnId === "vb-graph") renderGraph(currentCode());
  }
  const viewBtnIds = Object.keys(VIEWS);
  viewBtnIds.forEach(function (b) {
    const btn = document.getElementById(b);
    btn.addEventListener("click", function () { switchView(b); });
    btn.addEventListener("keydown", function (e) {
      const i = viewBtnIds.indexOf(b);
      let j = -1;
      if (e.key === "ArrowRight") j = (i + 1) % viewBtnIds.length;
      else if (e.key === "ArrowLeft") j = (i - 1 + viewBtnIds.length) % viewBtnIds.length;
      if (j >= 0) { e.preventDefault(); const nb = document.getElementById(viewBtnIds[j]); nb.focus(); switchView(viewBtnIds[j]); }
    });
  });

  // ── Family tree (genetic descent from parent pointers) ────────────────
  let FOREST = null;
  function buildForest() {
    const children = {};
    const hasParent = {};
    DATA.codes.forEach(function (code) {
      const p = DATA.languages[code].parent;
      if (p && DATA.languages[p]) {
        (children[p] = children[p] || []).push(code);
        hasParent[code] = true;
      }
    });
    Object.keys(children).forEach(function (p) {
      children[p].sort(function (a, b) {
        return DATA.languages[a].name.localeCompare(DATA.languages[b].name);
      });
    });
    const roots = DATA.codes.filter(function (c) { return !hasParent[c]; })
      .sort(function (a, b) { return DATA.languages[a].name.localeCompare(DATA.languages[b].name); });
    return { children: children, roots: roots };
  }

  function treeNode(code, depth) {
    const d = DATA.languages[code];
    const kids = (FOREST.children[code] || []);
    const li = document.createElement("li");
    li.dataset.code = code;
    const row = document.createElement("div");
    row.className = "trow" + (kids.length ? " toggle" : "") + (d.is_family ? " fam" : "");
    const tw = document.createElement("span");
    tw.className = "tw"; tw.textContent = kids.length ? "▾" : "";
    const dot = document.createElement("span");
    dot.className = "tdot " + esc(d.quality);
    const name = document.createElement("a");
    name.className = "tname"; name.href = "#" + encodeURIComponent(code); name.textContent = d.name;
    name.addEventListener("click", function (e) { e.stopPropagation(); });
    const codeEl = document.createElement("span");
    codeEl.className = "tcode"; codeEl.textContent = code;
    row.appendChild(tw); row.appendChild(dot); row.appendChild(name); row.appendChild(codeEl);
    if (d.is_family) {
      const tag = document.createElement("span");
      tag.className = "fam-tag"; tag.textContent = "family";
      row.appendChild(tag);
    }
    li.appendChild(row);
    if (kids.length) {
      const ul = document.createElement("ul");
      kids.forEach(function (k) { ul.appendChild(treeNode(k, depth + 1)); });
      li.appendChild(ul);
      if (depth >= 1) li.classList.add("collapsed");
      row.addEventListener("click", function () { li.classList.toggle("collapsed"); });
      row.setAttribute("tabindex", "0"); row.setAttribute("role", "button");
      row.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); li.classList.toggle("collapsed"); }
      });
    }
    return li;
  }

  let treeBuilt = false;
  function renderTree() {
    if (treeBuilt) return;
    FOREST = FOREST || buildForest();
    const root = document.getElementById("tree-root");
    const frag = document.createDocumentFragment();
    FOREST.roots.forEach(function (r) { frag.appendChild(treeNode(r, 0)); });
    root.appendChild(frag);
    treeBuilt = true;
    document.getElementById("tree-expand").addEventListener("click", function () {
      root.querySelectorAll("li.collapsed").forEach(function (li) { li.classList.remove("collapsed"); });
    });
    document.getElementById("tree-collapse").addEventListener("click", function () {
      root.querySelectorAll("li > ul").forEach(function (ul) { ul.parentElement.classList.add("collapsed"); });
    });
  }

  function markTreeSelection() {
    const cur = currentCode();
    const root = document.getElementById("tree-root");
    if (!root) return;
    root.querySelectorAll(".trow.sel").forEach(function (r) { r.classList.remove("sel"); });
    const li = root.querySelector('li[data-code="' + (window.CSS && CSS.escape ? CSS.escape(cur) : cur) + '"]');
    if (li) {
      li.querySelector(".trow").classList.add("sel");
      // reveal ancestors
      let p = li.parentElement;
      while (p && p.id !== "tree-root") {
        if (p.tagName === "LI") p.classList.remove("collapsed");
        p = p.parentElement;
      }
      li.scrollIntoView({ block: "center" });
    }
  }

  // ── Contact graph (radial lineage + contact neighbourhood) ────────────
  const EDGE = {
    parent:      { color: "var(--edge-parent)",      dash: "" },
    adstrate:    { color: "var(--edge-adstrate)",    dash: "7 5" },
    substrate:   { color: "var(--edge-substrate)",   dash: "1.5 6" },
    superstrate: { color: "var(--edge-superstrate)", dash: "9 4 2 4" }
  };
  function renderGraph(code) {
    const holder = document.getElementById("graph-holder");
    const title = document.getElementById("graph-title");
    const sub = document.getElementById("graph-sub");
    const d = code ? DATA.languages[code] : null;
    if (!d) {
      title.textContent = "Contact graph";
      sub.textContent = "";
      holder.innerHTML = '<p class="graph-empty">Select a language (from Browse or the tree) to see its lineage &amp; contact neighbourhood.</p>';
      return;
    }
    title.textContent = d.name;
    sub.textContent = code + " — parent (descent) plus substrate / superstrate / adstrate contact";
    const seen = {};
    const nbrs = [];
    if (d.parent && DATA.languages[d.parent]) { nbrs.push({ code: d.parent, role: "parent", weight: null }); seen[d.parent] = true; }
    (d.ancestors || []).forEach(function (a) {
      if (seen[a.code]) return; seen[a.code] = true;
      nbrs.push({ code: a.code, role: a.role, weight: a.weight });
    });
    if (!nbrs.length) {
      holder.innerHTML = '<p class="graph-empty">No lineage or contact edges recorded for ' + esc(code) + '.</p>';
      return;
    }
    const W = 760, H = Math.max(360, 220 + nbrs.length * 26), cx = W / 2, cy = H / 2, R = Math.min(cx, cy) - 70;
    let edges = "", nodes = "";
    nbrs.forEach(function (nb, i) {
      const ang = (-Math.PI / 2) + (2 * Math.PI * i / nbrs.length);
      const x = cx + R * Math.cos(ang), y = cy + R * Math.sin(ang);
      const e = EDGE[nb.role] || EDGE.parent;
      const w = 1.6 + (nb.weight ? Math.min(2.4, nb.weight * 3) : 1);
      edges += '<line x1="' + cx + '" y1="' + cy + '" x2="' + x + '" y2="' + y +
        '" stroke="' + e.color + '" stroke-width="' + w.toFixed(1) + '" stroke-linecap="round"' +
        (e.dash ? ' stroke-dasharray="' + e.dash + '"' : "") + '></line>';
      const known = !!DATA.languages[nb.code];
      const r = 20;
      nodes += '<g class="gnode" data-code="' + esc(nb.code) + '" transform="translate(' + x.toFixed(1) + ',' + y.toFixed(1) + ')">' +
        '<circle r="' + r + '" fill="var(--panel2)" stroke="' + e.color + '" stroke-width="2"' + (known ? "" : ' stroke-dasharray="3 3"') + '></circle>' +
        '<text text-anchor="middle" dy="-1" font-size="10">' + esc(nb.code.length > 11 ? nb.code.slice(0, 10) + "…" : nb.code) + '</text>' +
        '<text text-anchor="middle" dy="11" font-size="7.5" fill="var(--muted)">' + esc(nb.role) + '</text>' +
        '</g>';
    });
    const center = '<g transform="translate(' + cx + ',' + cy + ')">' +
      '<circle r="30" fill="var(--accent)"></circle>' +
      '<text text-anchor="middle" dy="3" font-size="11" fill="var(--bg)">' + esc(code.length > 12 ? code.slice(0, 11) + "…" : code) + '</text></g>';
    holder.innerHTML = '<svg id="graph-svg" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="Lineage and contact graph for ' + esc(d.name) + '">' +
      '<g fill="none">' + edges + '</g>' + nodes + center + '</svg>';
    holder.querySelectorAll(".gnode").forEach(function (g) {
      g.addEventListener("click", function () { const c = g.dataset.code; if (DATA.languages[c]) goTo(c); });
    });
  }

  searchEl.addEventListener("input", renderList);
  familySel.addEventListener("change", renderList);
  scriptSel.addEventListener("change", renderList);
  tierSel.addEventListener("change", renderList);
  window.addEventListener("hashchange", function () {
    onHashChange();
    if (activeView === "vb-graph") renderGraph(currentCode());
    if (activeView === "vb-tree") markTreeSelection();
  });

  renderList();
  onHashChange();
})();
</script>
</body>
</html>
"""


def render_html(data: dict) -> str:
    data_json = json.dumps(data, separators=(",", ":"), ensure_ascii=False, sort_keys=True)
    return PAGE_TEMPLATE.replace("__DATA_JSON__", data_json)


def main() -> None:
    data = build_data()
    html = render_html(data)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"wrote {OUTPUT_PATH} ({len(html)} bytes, {len(data['codes'])} languages)")


if __name__ == "__main__":
    main()
