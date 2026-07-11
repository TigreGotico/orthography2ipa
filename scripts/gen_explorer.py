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
    codes = sorted(o2i.available_codes())
    languages = {}
    for code in codes:
        spec = o2i.get(code)
        languages[code] = _spec_to_dict(spec, bench_by_lang)

    families = sorted({d["family"] for d in languages.values() if d["family"]})
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
#detail { flex: 1; overflow-y: auto; padding: 20px 26px; }
#detail h2 { margin-top: 0; }
.badge {
  display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 0.75rem;
  margin-left: 8px; color: #08131f; font-weight: 600;
}
.badge.production { background: var(--production); }
.badge.research { background: var(--research); }
.badge.skeleton { background: var(--skeleton); }
.badge.stub { background: var(--stub); }
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
  padding: 10px 14px; white-space: pre-wrap; font-size: 0.9rem;
}
.notes-box.warn { border-color: var(--skeleton); }
ul.plain { list-style: none; padding: 0; margin: 0; }
ul.plain li { padding: 4px 0; border-bottom: 1px dashed var(--border); font-size: 0.88rem; }
.empty { color: var(--muted); font-style: italic; }
.chip { display: inline-block; background: var(--panel2); border: 1px solid var(--border);
  border-radius: 4px; padding: 2px 6px; margin: 2px; font-size: 0.8rem; }
footer { padding: 10px 20px; border-top: 1px solid var(--border); color: var(--muted); font-size: 0.8rem; background: var(--panel); }
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
<main>
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
      const hay = (d.code + " " + d.name + " " + d.family).toLowerCase();
      if (hay.indexOf(q) === -1) return false;
    }
    if (familySel.value && d.family !== familySel.value) return false;
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
      nameSpan.textContent = d.name;
      a.appendChild(dot); a.appendChild(codeSpan); a.appendChild(nameSpan);
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
      html += "<tr><td>" + esc(r.dataset) + "</td><td>" + esc(r.n) + "</td><td>" +
        esc(r.per) + "</td><td>" + ci + "</td><td>" + esc(r.exact_match) + "</td><td>" +
        esc(r.provenance) + "</td><td>" + esc(r.quality_tier) + "</td></tr>";
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
    html += "<h2>" + esc(d.name) + '<span class="badge ' + esc(d.quality) + '">' + esc(d.quality) + "</span></h2>";
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
      html += '<section><h3>Notes</h3><div class="notes-box' + (looksWarning ? " warn" : "") + '">' + esc(d.notes) + "</div></section>";
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

  searchEl.addEventListener("input", renderList);
  familySel.addEventListener("change", renderList);
  scriptSel.addEventListener("change", renderList);
  tierSel.addEventListener("change", renderList);
  window.addEventListener("hashchange", onHashChange);

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
