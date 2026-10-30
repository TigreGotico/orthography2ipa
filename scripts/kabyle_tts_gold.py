#!/usr/bin/env python3
"""Kabyle (kab) TTS gold set — authoring, drafting and validation tooling.

The gold set lives in ``orthography2ipa/data/gold/kabyle_tts/<code>.tsv`` (one
file per lect) and provides phonetically diverse, register-appropriate,
literature-justified Kabyle sentences for validating Kabyle TTS voices
(synthesize each sentence, ASR/listen, compare against the gold IPA) and for
regression-pinning sentence-level o2i behaviour.

INPUT CONTRACT. Sentences are written in the standardised Berber LATIN alphabet
(the tamaziɣt/INALCO orthography of the Kabyle Wikipedia and Naït-Zerrad's
teaching grammars) — the same contract the ``kab`` spec expects. Tifinagh is a
secondary script and is not covered; a Tifinagh text would be transliterated to
this Latin orthography first. Kabyle orthography is complete (there is no
Arabic-style diacritization gap), so a row is simply the sentence a TTS
receives; there is no separate ``raw`` column and no diacritization check.

Subcommands
-----------
checklist <lect> [tsv]
    Derive the Kabyle-discriminative feature checklist and (if the gold TSV
    exists) report which phonological axes the current sentences already
    exercise and which are still missing. Use this to author more sentences.

draft <lect> <textfile>
    First-draft pipeline for new sentences (one Kabyle sentence per line):
    transcribe with orthography2ipa and auto-tag the machine-verifiable feature
    axes. Emits TSV rows marked NEEDS-REVIEW (gloss and citation ids are
    authored by hand against the lect's spec sources).

validate [lect ...]
    CI gate over the gold TSVs: schema, per-lect row minimum, o2i transcription
    regression (``transcribe(sentence, lect) == ipa``), feature-tag
    verifiability, in-lect duplicate detection and citation-id resolution
    against the lect's spec sources. Lects with no gold file yet report as
    pending, not failed — this is a growing set.

Schema (TSV, tab-separated, UTF-8, header row)
----------------------------------------------
id, sentence, ipa (o2i, verified), gloss_en, features (semicolon list),
notes (corrections + citation ids from the spec sources)
"""
import argparse
import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

GOLD_DIR = REPO_ROOT / "orthography2ipa" / "data" / "gold" / "kabyle_tts"

# Kabyle lects in the catalogue. `checklist` accepts any of them so sentences
# can be authored ahead of the gold file; `validate` gates only the lects that
# already have a TSV (the rest report as pending).
LECTS = ["kab"]
MIN_ROWS = 20
FIELDS = ["id", "sentence", "ipa", "gloss_en", "features", "notes"]


def _words(sentence: str):
    """Sentence split into word tokens with edge punctuation stripped."""
    return [w for w in re.findall(r"[^\s]+", sentence) if re.search(r"\w", w)]


# --- machine-verifiable Kabyle feature axes -------------------------------
# A tag is verified either from the orthography ("orth"), the IPA ("ipa") or
# both. The phonological reflexes (spirantization, gemination, emphasis, …) are
# read off the IPA; the post-nasal-hardening axis needs both, because the point
# is that a written nasal+stop cluster surfaces as a STOP, not a fricative.
def _postnasal_stop(s: str, ipa: str) -> bool:
    """A written homorganic nasal+lax-stop cluster (⟨nt nd nb⟩) that surfaces
    with the stop retained ([nt] [nd] [mb]) — the spirantization block modelled
    by the KAB_POSTNASAL_HARD_* rules."""
    if not re.search(r"n[tdb]", s.lower()):
        return False
    return bool(re.search(r"n[td]|mb", ipa))


FEATURES = {
    # Spirantization of lax stops → fricatives [β ð θ ç ʝ ðˤ] (the signature
    # Kabyle feature). ðˤ contains the ð glyph, so the class catches it too.
    "spirantization":    ("ipa",  lambda s, ipa: re.search(r"[βðθçʝ]", ipa) is not None),
    # Tense (geminate) stop / long consonant retained as a stop — any length mark.
    "geminate":          ("ipa",  lambda s, ipa: "ː" in ipa),
    # Emphatic (pharyngealized) consonant [rˤ sˤ dˤ tˤ zˤ].
    "emphatic":          ("ipa",  lambda s, ipa: "ˤ" in ipa),
    # Pharyngeal / from the Arabic-integrated series [ħ ʕ].
    "pharyngeal":        ("ipa",  lambda s, ipa: re.search(r"[ħʕ]", ipa) is not None),
    # Affricate ⟨č ǧ⟩ → [t͡ʃ d͡ʒ].
    "affricate":         ("ipa",  lambda s, ipa: "t͡ʃ" in ipa or "d͡ʒ" in ipa),
    # Uvular: stop [q] or voiceless fricative ⟨x⟩ [χ].
    "uvular":            ("ipa",  lambda s, ipa: "q" in ipa or "χ" in ipa),
    # Voiced velar/uvular fricative ⟨ɣ⟩. The spec realizes it as the uvular
    # [ʁ] in every position and keeps the broad [ɣ] as a documented variant,
    # so the tag accepts either realization of the one phoneme.
    "velar_fricative":   ("ipa",  lambda s, ipa: "ɣ" in ipa or "ʁ" in ipa),
    # Epenthetic schwa ⟨e⟩ [ə].
    "schwa":             ("ipa",  lambda s, ipa: "ə" in ipa),
    # Glide [j w] (⟨y w⟩, and the many affixal semivowels).
    "glide":             ("ipa",  lambda s, ipa: "j" in ipa or "w" in ipa),
    # Post-nasal hardening: ⟨nt nd nb⟩ keeps the stop (spirantization blocked).
    "postnasal_stop":    ("both", _postnasal_stop),
    # Nasal place assimilation to a velar [ŋ] before a dorsal.
    "velar_nasal":       ("ipa",  lambda s, ipa: "ŋ" in ipa),
}
# Non-phonetic shape tags: allowed in `features`, not machine-verified.
SHAPE_TAGS = {"statement", "question", "negation", "imperative", "greeting"}


def _load(lect):
    p = GOLD_DIR / f"{lect}.tsv"
    if not p.is_file():
        return None
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _spec_summary(lect):
    import orthography2ipa
    spec = orthography2ipa.get(lect)
    srcs = getattr(spec, "sources", None) or []
    return spec, srcs


def cmd_checklist(args):
    lect = args.lect
    spec, srcs = _spec_summary(lect)
    print(f"# {lect} — {getattr(spec, 'name', '?')}")
    print(f"sources: {', '.join(getattr(s, 'id', '?') for s in srcs) if srcs else '(none)'}")
    rows = _load(lect)
    covered = set()
    if rows:
        for r in rows:
            covered |= {t for t in r["features"].split(";") if t}
    print("\nfeature checklist (tag  verified-by  covered?):")
    for tag, (kind, _) in FEATURES.items():
        mark = "x" if tag in covered else " "
        print(f"  [{mark}] {tag:<16} ({kind})")
    for tag in sorted(SHAPE_TAGS):
        mark = "x" if tag in covered else " "
        print(f"  [{mark}] {tag:<16} (shape, not machine-verified)")
    missing = [t for t in FEATURES if t not in covered]
    if rows is None:
        print(f"\nno gold file yet: {GOLD_DIR / (lect + '.tsv')}")
    elif missing:
        print(f"\nMISSING phonetic coverage: {', '.join(missing)}")
    else:
        print("\nfull phonetic coverage.")


def cmd_draft(args):
    lect = args.lect
    import orthography2ipa
    lines = [l.strip() for l in Path(args.textfile).read_text(encoding="utf-8").splitlines() if l.strip()]
    w = csv.writer(sys.stdout, delimiter="\t")
    w.writerow(FIELDS)
    for i, line in enumerate(lines, 1):
        ipa = orthography2ipa.transcribe(line, lect)
        feats = ";".join(tag for tag, (_, pred) in FEATURES.items() if pred(line, ipa))
        w.writerow([f"{lect}-{i:03d}", line, ipa, "", feats,
                    "NEEDS-REVIEW: author gloss + citation id from spec sources"])


# A source id as written in the spec `sources`: lowercase author + year, with an
# optional descriptive slug (``kossmann_stroomer1997``, ``naitzerrad2001``,
# ``karaoui2024_fricatives``). The trailing run allows ``_``/``-`` as well.
CITE_ID = r"\b[a-z][a-z_-]*[0-9]{4}[a-z_-]*\b"
# A free-text author-year citation the id form is meant to replace, e.g.
# ``Kossmann & Stroomer 1997``. These escape the id regex (leading capital) and
# must be REJECTED so an unresolvable citation cannot pass as prose.
FREE_TEXT_CITE = re.compile(
    r"\b[A-Z][a-zA-Z]+(?:[-'][A-Z]?[a-zA-Z]+)*"
    r"(?:\s*(?:&|and|,)\s*[A-Z][a-zA-Z]+)*\s+(?:18|19|20)[0-9]{2}[a-z]?\b")


def cmd_validate(args):
    lects = args.lects or LECTS
    import orthography2ipa
    failures = []
    total = 0
    pending = 0
    for lect in lects:
        rows = _load(lect)
        if rows is None:
            pending += 1
            continue
        if len(rows) < MIN_ROWS:
            failures.append(f"{lect}: only {len(rows)} rows (< {MIN_ROWS})")
        seen = set()
        for r in rows:
            total += 1
            rid = r.get("id", "?")
            if list(r) != FIELDS and set(FIELDS) - set(r):
                failures.append(f"{rid}: bad columns {list(r)}")
                continue
            if not all(r[f] for f in ("id", "sentence", "ipa", "gloss_en", "features")):
                failures.append(f"{rid}: empty required field")
            if r["sentence"] in seen:
                failures.append(f"{rid}: duplicate sentence within {lect}")
            seen.add(r["sentence"])
            got = orthography2ipa.transcribe(r["sentence"], lect)
            if got != r["ipa"]:
                failures.append(f"{rid}: o2i regression\n    stored: {r['ipa']}\n    got:    {got}")
            for tag in [t for t in r["features"].split(";") if t]:
                if tag in SHAPE_TAGS:
                    continue
                if tag not in FEATURES:
                    failures.append(f"{rid}: unknown feature tag {tag!r}")
                elif not FEATURES[tag][1](r["sentence"], r["ipa"]):
                    failures.append(f"{rid}: feature {tag!r} not verifiable in row")
            spec = orthography2ipa.get(lect)
            src_ids = {getattr(s, "id", None) for s in (getattr(spec, "sources", None) or ())}
            notes = r["notes"]
            for ft in FREE_TEXT_CITE.findall(notes):
                failures.append(
                    f"{rid}: free-text citation {ft!r} in notes — use the source id "
                    f"(kossmann_stroomer1997-style) from the {lect} spec sources")
            resolvable = [c for c in re.findall(CITE_ID, notes) if c in src_ids]
            for cid in re.findall(CITE_ID, notes):
                if cid not in src_ids:
                    failures.append(f"{rid}: notes cite {cid!r}, not in {lect} spec sources")
            if not resolvable and not FREE_TEXT_CITE.search(notes):
                failures.append(f"{rid}: notes carry no resolvable source id "
                                f"(cite a {lect} spec source, or reword to a "
                                f"coverage note that names one)")
    print(f"validated {total} rows across {len(lects) - pending} lects ({pending} pending)")
    if failures:
        print(f"\n{len(failures)} FAILURE(S):")
        for f in failures:
            print("  -", f)
        return 1
    print("all green")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("checklist"); p.add_argument("lect"); p.set_defaults(fn=cmd_checklist)
    p = sub.add_parser("draft"); p.add_argument("lect"); p.add_argument("textfile"); p.set_defaults(fn=cmd_draft)
    p = sub.add_parser("validate"); p.add_argument("lects", nargs="*"); p.set_defaults(fn=cmd_validate)
    args = ap.parse_args()
    rc = args.fn(args)
    sys.exit(rc or 0)


if __name__ == "__main__":
    main()
