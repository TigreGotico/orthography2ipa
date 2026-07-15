#!/usr/bin/env python3
"""Portuguese-dialects TTS gold set — authoring, drafting and validation tooling.

The gold set lives in ``orthography2ipa/data/gold/portuguese_tts/<code>.tsv``
(one file per lect) and provides phonetically diverse, register-appropriate,
literature-justified sentences for validating Portuguese TTS voices per
dialect. Portuguese orthography is complete (no diacritization gap), so a row
is simply the sentence a TTS receives; there is no separate ``raw`` column and
no diacritization-completeness check.

Subcommands
-----------
checklist <lect> [tsv]
    Derive the dialect-discriminative feature checklist for a lect and (if the
    gold TSV exists) report which axes the current sentences already exercise
    and which are still missing. Use this to author additional sentences.

draft <lect> <textfile>
    First-draft pipeline for new sentences (one per line, ordinary Portuguese
    orthography): transcribe with orthography2ipa and auto-tag the machine
    verifiable feature axes. Emits TSV rows marked NEEDS-REVIEW (gloss and
    citation ids are authored by hand against the lect's spec sources).

validate [lect ...]
    CI gate over the gold TSVs: schema, per-lect row minimum, o2i transcription
    regression (``transcribe(sentence, lect) == ipa``), feature-tag
    verifiability, in-lect duplicate detection and citation-id resolution
    against the lect's spec sources. Lects with no gold file yet are reported
    as pending, not failed — this is a growing set.

Schema (TSV, tab-separated, UTF-8, header row)
----------------------------------------------
id, sentence, ipa (o2i, verified), gloss_en, features (semicolon list),
notes (corrections + citation ids)
"""
import argparse
import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

GOLD_DIR = REPO_ROOT / "orthography2ipa" / "data" / "gold" / "portuguese_tts"

# All 39 Portuguese lects in the catalogue. `checklist` accepts any of them so
# sentences can be authored ahead of the gold file; `validate` gates only the
# lects that already have a TSV (the rest report as pending).
LECTS = [
    "pt-PT", "pt-BR",
    # European mainland + insular
    "pt-PT-x-lisbon", "pt-PT-x-porto", "pt-PT-x-braga", "pt-PT-x-minho",
    "pt-PT-x-viana", "pt-PT-x-aveiro", "pt-PT-x-coimbra", "pt-PT-x-beira",
    "pt-PT-x-trasosmontes", "pt-PT-x-alentejo", "pt-PT-x-algarve",
    "pt-PT-x-alfena", "pt-PT-x-medieval",
    "pt-PT-x-acores", "pt-PT-x-sao-miguel", "pt-PT-x-terceira",
    "pt-PT-x-madeira",
    # Brazilian
    "pt-BR-x-bahia", "pt-BR-x-brasilia", "pt-BR-x-caipira", "pt-BR-x-ce",
    "pt-BR-x-fluminense", "pt-BR-x-mg", "pt-BR-x-norte", "pt-BR-x-pr",
    "pt-BR-x-recife", "pt-BR-x-rj", "pt-BR-x-sp", "pt-BR-x-sul",
    # African + Asian
    "pt-AO", "pt-CV", "pt-GW", "pt-MZ", "pt-ST", "pt-MO", "pt-TL",
    "pt-UY",
]
MIN_ROWS = 5
FIELDS = ["id", "sentence", "ipa", "gloss_en", "features", "notes"]

# --- orthographic helpers used by the sentence-level predicates -----------
VOWELS_ORTH = set("aeiouáàâãéêíóôõúüAEIOUÁÀÂÃÉÊÍÓÔÕÚÜ")
# grapheme onsets that trigger regressive voicing of a preceding coda /s z/
VOICED_ONSET = set("bdgvzlmnrjBDGVZLMNRJ") | VOWELS_ORTH


def _words(sentence: str):
    """Sentence split into word tokens with edge punctuation stripped."""
    return [w for w in re.findall(r"[^\s]+", sentence) if re.search(r"\w", w)]


def _strip_punct(word: str) -> str:
    return word.strip(".,;:!?¿¡\"'«»()—-").lower()


def _coda_sibilant_grapheme(sentence: str) -> bool:
    """True if any word has an /s z x/ in coda (before a consonant or
    word-final) — the position where EP/Fluminense realise [ʃ ʒ]."""
    for w in _words(sentence):
        w = _strip_punct(w)
        for m in re.finditer(r"[szx]", w):
            i = m.end()
            if i >= len(w):  # word-final
                return True
            if w[i] not in VOWELS_ORTH:  # pre-consonantal
                return True
    return False


def _coda_l_grapheme(sentence: str) -> bool:
    """True if any word has an /l/ in coda — the position whose reflex splits
    dark [ɫ] (EP), velar, and vocalised [w] (BR) lects."""
    for w in _words(sentence):
        w = _strip_punct(w)
        for m in re.finditer(r"l", w):
            i = m.end()
            if i < len(w) and w[i] == "h":
                continue  # `lh` digraph is palatal [ʎ], not a coda /l/
            if i >= len(w) or w[i] not in VOWELS_ORTH:
                return True
    return False


def _has_sandhi_junction(sentence: str) -> bool:
    """True if some word boundary is a cross-word sandhi site: a vowel-final
    word before a vowel-initial word (elision / liaison), or an /s z/-final
    word before a voiced-onset word (regressive sibilant voicing)."""
    ws = [_strip_punct(w) for w in _words(sentence)]
    ws = [w for w in ws if w]
    for a, b in zip(ws, ws[1:]):
        if a[-1] in VOWELS_ORTH and b[0] in VOWELS_ORTH:
            return True
        if a[-1] in "szxSZX" and b[0] in VOICED_ONSET:
            return True
    return False


# --- feature tags: each predicate is computable from (sentence, ipa) -------
# "ipa" predicates demonstrate a realised reflex; "orth" predicates prove the
# sentence exercises an axis whose reflex varies across lects (so the grapheme,
# not the transcription, is the stable witness).
FEATURES = {
    # unstressed reduction to [ɨ]/[ɐ]/[u] (EP heavy, BR light) — reflex tag
    "vowel_reduction":  ("ipa",  lambda s, ipa: "ɨ" in ipa or "ɐ" in ipa),
    # coda /s z/ → [ʃ ʒ] vs [s z]: needs a coda sibilant AND a palato-alveolar
    "coda_sibilant":    ("both", lambda s, ipa: _coda_sibilant_grapheme(s)
                                                 and re.search(r"[ʃʒ]", ipa) is not None),
    "open_mid":         ("ipa",  lambda s, ipa: "ɛ" in ipa or "ɔ" in ipa),
    "close_mid":        ("ipa",  lambda s, ipa: re.search(r"[eo]", ipa) is not None),
    "nasal_vowel":      ("ipa",  lambda s, ipa: "̃" in ipa),
    # nasal diphthong: a nasalised glide [w̃]/[j̃] (ão, ãe, õe, …)
    "nasal_diphthong":  ("ipa",  lambda s, ipa: re.search(r"[wj]̃", ipa) is not None),
    "palatal":          ("ipa",  lambda s, ipa: "ʎ" in ipa or "ɲ" in ipa),
    # strong-R reflex [ʀ ʁ r h χ] (excludes the ubiquitous tap [ɾ])
    "rhotic":           ("ipa",  lambda s, ipa: re.search(r"[ʀʁrhχ]", ipa) is not None),
    # ei/ou axis: retention (EP-south [ɐj]/[o(w)]) vs monophthong (north [e]/[o])
    "diphthong_ei_ou":  ("orth", lambda s, ipa: re.search(r"ei|ou", s.lower()) is not None),
    # coda /l/ axis: dark [ɫ] (EP) vs velar vs vocalised [w] (BR)
    "l_dark_or_velar":  ("orth", lambda s, ipa: _coda_l_grapheme(s)),
    # insular fronting of /u/ → [y] (Azores/Madeira)
    "u_fronting":       ("ipa",  lambda s, ipa: "y" in ipa),
    # cross-word sandhi site (elision / liaison / sibilant voicing)
    "sandhi":           ("both", lambda s, ipa: _has_sandhi_junction(s)),
}
# Non-phonetic shape tags: allowed in `features`, not machine-verified.
SHAPE_TAGS = {"statement", "question", "negation", "imperative", "number"}


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


# A source id as written in the spec `sources`: lowercase author + year, e.g.
# ``cruzferreira1995``, ``mateus_dandrade2000`` (optionally a trailing letter).
CITE_ID = r"\b[a-z][a-z_-]*[0-9]{4}[a-z]*\b"
# A free-text author-year citation the id form is meant to replace, e.g.
# ``Cruz-Ferreira 1995``, ``Mateus & d'Andrade 2000``. These escape the id
# regex (leading capital) and must be REJECTED so an unresolvable citation
# cannot pass as prose.
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
            # free-text author-year citations must never pass silently — the
            # gold cites by resolvable source id, not by prose author name
            for ft in FREE_TEXT_CITE.findall(notes):
                failures.append(
                    f"{rid}: free-text citation {ft!r} in notes — use the source id "
                    f"(cruzferreira1995-style) from the {lect} spec sources")
            resolvable = [c for c in re.findall(CITE_ID, notes) if c in src_ids]
            for cid in re.findall(CITE_ID, notes):
                if cid not in src_ids:
                    failures.append(f"{rid}: notes cite {cid!r}, not in {lect} spec sources")
            # every row's notes MUST carry a resolvable source id from the lect's
            # spec sources: a reflex/lexical/rule claim is grounded in the source
            # that documents it, and a pure coverage note names the source whose
            # scope covers the row's phonology.
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
