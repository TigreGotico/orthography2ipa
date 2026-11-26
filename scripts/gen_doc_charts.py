#!/usr/bin/env python3
"""Generate the SVG charts of the evaluation docs from the committed board.

Each chart is written twice, as ``<name>.light.svg`` and ``<name>.dark.svg`` in
``docs/evaluation/charts/``, so that a page can pick one with a ``<picture>``
element. The generator uses the standard library only and writes the SVG text
by hand. The output depends on the board files alone: the same data gives the
same bytes.

The charts:

``per-distribution``
    The share of rows in each PER bin, one panel per quality tier, from
    ``benchmarks/results.json``.
``o2i-vs-espeak``
    Lexicon-free o2i PER against rules-only espeak-ng PER, from
    ``benchmarks/comparison.json``. Rows whose gold is the output of either
    engine are left out, and so is every lexicon-backed column.
``coverage``
    Board rows per gold dataset, from ``benchmarks/results.json``.
``espeak-agreement``
    Segmental agreement of o2i with espeak-ng per language, from
    ``benchmarks/espeak_agreement.json``.

Usage::

    PYTHONPATH=$PWD python scripts/gen_doc_charts.py --write
    PYTHONPATH=$PWD python scripts/gen_doc_charts.py --check

``--check`` writes nothing and exits 1 when a file differs from the data.
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
from collections import Counter
from typing import Dict, List, Optional, Sequence, Tuple

from compare_systems import fair_pairs

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHART_DIR = os.path.join("docs", "evaluation", "charts")

# Series colours, text, grid and axis colours of each GitHub surface.
MODES = {
    "light": {"series": "#2a78d6", "text": "#0b0b0b", "muted": "#52514e",
              "grid": "#e3e6ea", "axis": "#b4bac1"},
    "dark": {"series": "#3987e5", "text": "#f0efec", "muted": "#c3c2b7",
             "grid": "#262c33", "axis": "#4a5159"},
}
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
TIERS = ("production", "research", "stub", "skeleton")


def num(v: float) -> str:
    """A fixed-format number: two decimals, no trailing zeros."""
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("", "-0") else s


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x: float, y: float, s: str, c: Dict[str, str], size: int = 12,
         anchor: str = "start", muted: bool = False, weight: str = "normal",
         rotate: bool = False) -> str:
    fill = c["muted"] if muted else c["text"]
    turn = f' transform="rotate(-90 {num(x)} {num(y)})"' if rotate else ""
    return (f'<text x="{num(x)}" y="{num(y)}"{turn} font-size="{size}" '
            f'text-anchor="{anchor}" font-weight="{weight}" fill="{fill}">'
            f'{esc(s)}</text>')


def line(x1: float, y1: float, x2: float, y2: float, color: str,
         dash: Optional[str] = None) -> str:
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{num(x1)}" y1="{num(y1)}" x2="{num(x2)}" y2="{num(y2)}" '
            f'stroke="{color}" stroke-width="1"{d}/>')


def bar(x: float, y: float, w: float, h: float, fill: str, end: str) -> str:
    """A bar whose data end ('top' or 'right') has 4 px rounded corners."""
    r = min(4.0, h / 2 if end == "right" else w / 2, w if end == "top" else h)
    if end == "top":
        d = (f"M{num(x)} {num(y + h)}V{num(y + r)}Q{num(x)} {num(y)} {num(x + r)} {num(y)}"
             f"H{num(x + w - r)}Q{num(x + w)} {num(y)} {num(x + w)} {num(y + r)}V{num(y + h)}Z")
    else:
        d = (f"M{num(x)} {num(y)}H{num(x + w - r)}Q{num(x + w)} {num(y)} {num(x + w)} {num(y + r)}"
             f"V{num(y + h - r)}Q{num(x + w)} {num(y + h)} {num(x + w - r)} {num(y + h)}"
             f"H{num(x)}Z")
    return f'<path d="{d}" fill="{fill}"/>'


def svg(width: int, height: int, title: str, desc: str, body: List[str]) -> str:
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" font-family="{FONT}">'
            f'<title>{esc(title)}</title><desc>{esc(desc)}</desc>')
    return head + "\n" + "\n".join(body) + "\n</svg>\n"


def load(name: str) -> list:
    with open(os.path.join(REPO_ROOT, "benchmarks", name), encoding="utf-8") as fh:
        return json.load(fh)


def per_distribution(rows: list, c: Dict[str, str]) -> str:
    bins, step = 16, 0.05
    panels = {t: sorted(r["per"] for r in rows if r["quality_tier"] == t) for t in TIERS}
    shares = {}
    for t, vals in panels.items():
        counts = Counter(min(int(round(v / step, 9)), bins - 1) for v in vals)
        shares[t] = [100 * counts[i] / len(vals) for i in range(bins)]
    ymax = 10 * (int((max(max(s) for s in shares.values()) + 12) // 10) + 1)

    pw, ph, left, top = 290, 130, 62, 74
    gapx, gapy = 52, 62
    width, height = left + 2 * pw + gapx + 20, top + 2 * ph + gapy + 50
    body = [text(20, 26, "Rows by PER, per quality tier", c, 16, weight="bold"),
            text(20, 46, f"Share of the rows of a tier in each 0.05-wide PER bin. "
                         f"{len(rows)} board rows.", c, 12, muted=True)]
    for i, t in enumerate(TIERS):
        ox = left + (i % 2) * (pw + gapx)
        oy = top + (i // 2) * (ph + gapy)
        body.append(text(ox, oy - 10, f"{t} ({len(panels[t])} rows)", c, 13, weight="bold"))
        for g in range(0, ymax + 1, 10):
            gy = oy + ph - ph * g / ymax
            body.append(line(ox, gy, ox + pw, gy, c["grid"]))
            if i % 2 == 0:
                body.append(text(ox - 6, gy + 4, f"{g}%", c, 11, "end", muted=True))
        if i % 2 == 0:
            body.append(text(18, oy + ph / 2, "share of rows", c, 11, "middle",
                             muted=True, rotate=True))
        bw = pw / bins
        for b, s in enumerate(shares[t]):
            if s:
                h = ph * s / ymax
                body.append(bar(ox + b * bw + 1, oy + ph - h, bw - 2, h, c["series"], "top"))
        body.append(line(ox, oy + ph, ox + pw, oy + ph, c["axis"]))
        for v in (0, 0.2, 0.4, 0.6, 0.8):
            tx = ox + pw * v / (bins * step)
            body.append(text(tx, oy + ph + 15, num(v), c, 11, "middle", muted=True))
        med = statistics.median(panels[t])
        mx = ox + pw * med / (bins * step)
        body.append(line(mx, oy, mx, oy + ph, c["text"], "4 3"))
        right = mx > ox + pw * 0.6
        body.append(text(mx + (-5 if right else 5), oy + 12, f"median {med:.3f}",
                         c, 11, "end" if right else "start"))
        if i >= 2:
            body.append(text(ox + pw / 2, oy + ph + 33, "PER (phoneme error rate, 0 = perfect)",
                             c, 11, "middle", muted=True))
    title = "Per-row PER by quality tier"
    desc = "; ".join(f"{t}: median {statistics.median(v):.3f} over {len(v)} rows"
                     for t, v in panels.items())
    return svg(width, height, title, desc, body)


def o2i_vs_espeak(comparison: list, c: Dict[str, str]) -> str:
    pairs = fair_pairs(comparison)
    lower = sum(1 for o, e in pairs if o < e)
    top = 0.1 * (int(max(max(o, e) for o, e in pairs) / 0.1) + 1)
    size, left, bottom = 440, 68, 56
    x0, y0 = left, 80
    width, height = left + size + 30, y0 + size + bottom

    def px(v: float) -> float:
        return x0 + size * v / top

    def py(v: float) -> float:
        return y0 + size - size * v / top

    body = [text(20, 26, f"o2i lower on {lower} of {len(pairs)} rows", c, 16, weight="bold"),
            text(20, 46, f"PER on the {len(pairs)} board rows with gold-tier references, "
                         "where both engines", c, 12, muted=True),
            text(20, 62, "have a lexicon-free score; one dot per row.", c, 12, muted=True)]
    ticks = [i / 10 for i in range(0, int(round(top * 10)) + 1, 2)]
    for v in ticks:
        body.append(line(px(0), py(v), px(top), py(v), c["grid"]))
        body.append(line(px(v), py(0), px(v), py(top), c["grid"]))
        body.append(text(x0 - 6, py(v) + 4, num(v), c, 11, "end", muted=True))
        body.append(text(px(v), y0 + size + 16, num(v), c, 11, "middle", muted=True))
    body.append(line(px(0), py(0), px(top), py(0), c["axis"]))
    body.append(line(px(0), py(0), px(0), py(top), c["axis"]))
    body.append(line(px(0), py(0), px(top), py(top), c["muted"], "5 4"))
    for o, e in sorted(pairs):
        body.append(f'<circle cx="{num(px(o))}" cy="{num(py(e))}" r="4.5" '
                    f'fill="{c["series"]}" fill-opacity="0.8" stroke="{c["series"]}"/>')
    body.append(text(px(top) - 8, py(0) - 22, "o2i lower: dots above the dashed line",
                     c, 11, "end"))
    body.append(text(px(top) - 8, py(0) - 8, "dashed line: equal PER", c, 11, "end", muted=True))
    body.append(text(x0 + size / 2, y0 + size + 38, "o2i PER, lexicon-free (0 = perfect)",
                     c, 12, "middle"))
    body.append(text(16, y0 + size / 2, "espeak-ng PER, rules only (0 = perfect)", c, 12,
                     "middle", rotate=True))
    desc = (f"Scatter of {len(pairs)} gold-tier rows. o2i has the lower PER on {lower} of them.")
    return svg(width, height, f"o2i lower on {lower} of {len(pairs)} rows", desc, body)


def coverage(rows: list, c: Dict[str, str]) -> str:
    counts = sorted(Counter(r["dataset"] for r in rows).items(), key=lambda kv: (-kv[1], kv[0]))
    left, right, top, step, bh = 190, 56, 62, 18, 16
    pw = 520
    width, height = left + pw + right, top + step * len(counts) + 30
    peak = counts[0][1]
    body = [text(20, 26, f"Board rows per gold dataset ({len(rows)} rows, {len(counts)} datasets)",
                 c, 16, weight="bold"),
            text(20, 46, "One row is one language scored on one dataset.", c, 12, muted=True)]
    for g in range(0, peak + 1, 50):
        gx = left + pw * g / peak
        body.append(line(gx, top - 4, gx, top + step * len(counts), c["grid"]))
        body.append(text(gx, top + step * len(counts) + 14, str(g), c, 11, "middle", muted=True))
    for i, (name, n) in enumerate(counts):
        y = top + i * step
        w = pw * n / peak
        body.append(text(left - 8, y + 12, name, c, 12, "end"))
        body.append(bar(left, y, w, bh, c["series"], "right"))
        body.append(text(left + w + 6, y + 12, str(n), c, 11, muted=True))
    body.append(line(left, top - 4, left, top + step * len(counts), c["axis"]))
    desc = ", ".join(f"{name} {n}" for name, n in counts[:5]) + ", and more"
    return svg(width, height, "Board rows per gold dataset", desc, body)


def espeak_agreement(rows: list, c: Dict[str, str]) -> str:
    scored = sorted(((r["lang"], r["segmental"]) for r in rows), key=lambda kv: (-kv[1], kv[0]))
    left, right, top, step, bh = 30 + 7 * max(len(lang) for lang, _ in scored), 56, 62, 18, 16
    pw = 520
    width, height = left + pw + right, top + step * len(scored) + 30
    body = [text(20, 26, f"Segmental agreement with espeak-ng ({len(scored)} languages)",
                 c, 16, weight="bold"),
            text(20, 46, "Share of segments where o2i and espeak-ng give the same phone (1 = all).",
                 c, 12, muted=True)]
    for g in (0.0, 0.25, 0.5, 0.75, 1.0):
        gx = left + pw * g
        body.append(line(gx, top - 4, gx, top + step * len(scored), c["grid"]))
        body.append(text(gx, top + step * len(scored) + 14, num(g), c, 11, "middle", muted=True))
    for i, (lang, v) in enumerate(scored):
        y = top + i * step
        body.append(text(left - 8, y + 12, lang, c, 12, "end"))
        body.append(bar(left, y, pw * v, bh, c["series"], "right"))
        body.append(text(left + pw * v + 6, y + 12, num(v), c, 11, muted=True))
    body.append(line(left, top - 4, left, top + step * len(scored), c["axis"]))
    hi, lo = scored[0], scored[-1]
    desc = (f"Highest {hi[0]} {num(hi[1])}, lowest {lo[0]} {num(lo[1])}, "
            f"over {len(scored)} languages.")
    return svg(width, height, "Segmental agreement with espeak-ng", desc, body)


def outputs() -> Dict[str, str]:
    results, comparison = load("results.json"), load("comparison.json")
    agreement = load("espeak_agreement.json")
    charts = {"per-distribution": lambda c: per_distribution(results, c),
              "o2i-vs-espeak": lambda c: o2i_vs_espeak(comparison, c),
              "coverage": lambda c: coverage(results, c),
              "espeak-agreement": lambda c: espeak_agreement(agreement, c)}
    return {os.path.join(CHART_DIR, f"{name}.{mode}.svg"): draw(colors)
            for name, draw in charts.items() for mode, colors in MODES.items()}


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write the files")
    mode.add_argument("--check", action="store_true",
                      help="exit 1 when a file differs from what the data says")
    args = ap.parse_args(argv)

    wanted = outputs()
    stale = []
    for rel, svg_text in wanted.items():
        path = os.path.join(REPO_ROOT, rel)
        current = None
        if os.path.exists(path):
            with open(path, encoding="utf-8", newline="") as fh:
                current = fh.read()
        if current == svg_text:
            continue
        stale.append(rel)
        if args.write:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as fh:
                fh.write(svg_text)
    chart_dir = os.path.join(REPO_ROOT, CHART_DIR)
    known = {os.path.basename(rel) for rel in wanted}
    extra = sorted(f for f in os.listdir(chart_dir) if f.endswith(".svg") and f not in known) \
        if os.path.isdir(chart_dir) else []
    stale += [os.path.join(CHART_DIR, f) for f in extra if args.check]
    if not stale:
        print("charts up to date")
        return 0
    if args.write:
        print("wrote " + ", ".join(stale))
        return 0
    print("stale: " + ", ".join(stale)
          + "\nRun: PYTHONPATH=$PWD python scripts/gen_doc_charts.py --write")
    return 1


if __name__ == "__main__":
    sys.exit(main())
