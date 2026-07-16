#!/usr/bin/env python3
"""Atlantic Iberian-creole TTS gold set — authoring, drafting and validation.

The gold set lives in
``orthography2ipa/data/gold/creoles_atlantic_tts/<code>.tsv`` (one file per
lect) and provides phonetically diverse, register-appropriate,
literature-justified sentences for validating the TTS voices of the
Iberian-lexified Atlantic creoles: Kabuverdianu (kea), Guinea-Bissau Kriol
(pov), Principense/Lung'ie (pre), Angolar (aoa) and Sãotomense/Forro (cri).

Each row is written in the creole's **own** community/standard orthography
(ALUPEC for kea; the Kihm/Scantamburlo convention for pov; the Gulf-of-Guinea
ALUSTP-style spelling for pre/aoa/cri), in **genuine creole register** — TMA
particles, invariant nouns with no gender agreement, creole pronoun paradigms —
NOT the Portuguese lexifier. There is no separate ``raw`` column: a row is the
sentence a TTS receives.

These creoles do NOT share the Iberian-Romance harness axes (distinción/seseo,
yeísmo, Romance ⟨ie ue⟩ diphthongisation, gheada, coda-/s/ aspiration). Those
axes are inapplicable by construction and are not modelled here. The axes that
matter for this family are its own: phonemic nasal vowels, the tx/dj affricates,
prenasalised onsets (pov/pre/aoa/cri), the labial-velar stops ⟨gb kp⟩ of the
Gulf-of-Guinea cluster, the seven-vowel open-mid contrast (cri), coda sibilants
and the kea velarised coda /l/. See docs/creoles-atlantic-tts-gold.md.

Subcommands mirror scripts/spain_romance_tts_gold.py: ``checklist <lect>``,
``draft <lect> <textfile>`` and ``validate [lect ...]``.
"""
import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

GOLD_DIR = REPO_ROOT / "orthography2ipa" / "data" / "gold" / "creoles_atlantic_tts"

# The Atlantic Iberian-creole roster. `checklist` accepts any of them so
# sentences can be authored ahead of the gold file; `validate` gates only the
# lects that already have a TSV (the rest report as pending). Keep this list
# append-friendly for concurrent authors.
LECTS = [
    "kea",  # Kabuverdianu (Cape Verdean Creole), ALUPEC
    "pov",  # Guinea-Bissau Kriol (Upper Guinea Creole)
    "pre",  # Principense / Lung'ie (Gulf of Guinea)
    "aoa",  # Angolar (Gulf of Guinea, Bantu-heavy, tonal)
    "cri",  # Sãotomense / Forro / Santome (Gulf of Guinea), ALUSTP
]
MIN_ROWS = 5
FIELDS = ["id", "sentence", "ipa", "gloss_en", "features", "notes"]

# --- orthographic helpers --------------------------------------------------
NASAL_GRAPHS = ("mb", "nd", "ng", "mp")  # word-initial prenasalised onsets (orth)


def _words(sentence: str):
    return [w for w in re.findall(r"[^\s]+", sentence) if re.search(r"\w", w)]


def _strip_punct(word: str) -> str:
    return word.strip(".,;:!?¿¡\"'«»()—-·").lower()


def _has_initial_prenasal_graph(sentence: str) -> bool:
    """True if some word begins with a ⟨mb nd ng⟩ prenasalised onset."""
    for w in _words(sentence):
        w = _strip_punct(w)
        if w.startswith(NASAL_GRAPHS):
            return True
    return False


def _has_labial_velar_graph(sentence: str) -> bool:
    """True if some word contains a ⟨gb⟩ or ⟨kp⟩ labial-velar-stop digraph."""
    s = sentence.lower()
    return "gb" in s or "kp" in s


# --- ipa-side helpers ------------------------------------------------------
IPA_VOWELS = set("aeiouɛɔ")
TILDE = "̃"


def _has_nasal_vowel(ipa: str) -> bool:
    """True if any vowel carries a combining tilde — a phonemic nasal vowel."""
    for i, ch in enumerate(ipa):
        if ch == TILDE:
            return True
    # NFC-composed forms (ã õ ũ ẽ ĩ) decompose to base+tilde under NFD
    return TILDE in unicodedata.normalize("NFD", ipa)


def _token_final_sibilant(ipa: str) -> bool:
    """True if some ipa word ends in a postalveolar sibilant [ʃ]/[ʒ] — the
    coda sibilant of kea (coda /s/ → [ʃ]) and cri (⟨x⟩ → [ʃ])."""
    for tok in ipa.split():
        tok = tok.rstrip("ˈˌ")
        while tok and unicodedata.combining(tok[-1]):
            tok = tok[:-1]
        if tok.endswith(("ʃ", "ʒ")):
            return True
    return False


# --- feature tags: each predicate is computable from (sentence, ipa) -------
# "ipa" predicates demonstrate a realised reflex; "both" require an orthographic
# trigger AND the predicted ipa so the tag proves the row exercises the axis.
FEATURES = {
    # phonemic nasal vowel (ã ẽ ĩ õ ũ) — all five lects
    "nasal_vowel":     ("ipa",  lambda s, ipa: _has_nasal_vowel(ipa)),
    # tx/dj creole affricates [tʃ]/[dʒ]
    "affricate":       ("ipa",  lambda s, ipa: "tʃ" in ipa or "dʒ" in ipa),
    # postalveolar sibilant [ʃ]/[ʒ] (x=[ʃ], j=[ʒ])
    "postalveolar":    ("ipa",  lambda s, ipa: "ʃ" in ipa or "ʒ" in ipa),
    # coda sibilant: a word ends in [ʃ]/[ʒ] (kea coda /s/, cri ⟨x⟩)
    "coda_sibilant":   ("ipa",  lambda s, ipa: _token_final_sibilant(ipa)),
    # prenasalised onset ⟨mb nd ng⟩ → [mb nd ŋɡ] (pov/pre/aoa/cri)
    "prenasal_stop":   ("both", lambda s, ipa: _has_initial_prenasal_graph(s)
                                               and ("mb" in ipa or "nd" in ipa
                                                    or "ŋɡ" in ipa or "mp" in ipa)),
    # Gulf-of-Guinea labial-velar stop ⟨gb⟩ [ɡ͡b] / ⟨kp⟩ [k͡p]
    "labial_velar":    ("both", lambda s, ipa: _has_labial_velar_graph(s)
                                               and ("ɡ͡b" in ipa or "k͡p" in ipa)),
    # seven-vowel open-mid contrast [ɛ]/[ɔ] (cri; bare ⟨e o⟩)
    "open_mid":        ("ipa",  lambda s, ipa: "ɛ" in ipa or "ɔ" in ipa),
    # palatal nasal [ɲ] (⟨nh⟩ kea)
    "palatal_nasal":   ("ipa",  lambda s, ipa: "ɲ" in ipa),
    # velar nasal [ŋ] (prenasal onsets, coda ⟨n⟩)
    "velar_nasal":     ("ipa",  lambda s, ipa: "ŋ" in ipa),
    # velarised coda /l/ → [ɫ] (kea)
    "velarized_l":     ("ipa",  lambda s, ipa: "ɫ" in ipa),
    # strong rhotic [ʀ]/[r] (kea rr/#r; pov alveolar [r]) — excludes tap [ɾ]
    "strong_rhotic":   ("ipa",  lambda s, ipa: "ʀ" in ipa or "r" in ipa),
    # alveolar tap [ɾ] (single intervocalic ⟨r⟩)
    "tap":             ("ipa",  lambda s, ipa: "ɾ" in ipa),
    # lexical stress assigned in the ipa (kea)
    "stress":          ("ipa",  lambda s, ipa: "ˈ" in ipa),
}
# Non-phonetic shape / morphosyntax tags: allowed in `features`, not
# machine-verified. `tma` (a tense-mood-aspect particle: ta/ka/na/sa/bra/ka…),
# `no_agreement` (invariant noun, no gender/number agreement) and the pronoun/
# clause-type tags document the genuine creole register of the row.
SHAPE_TAGS = {"statement", "question", "negation", "imperative",
              "tma", "no_agreement", "pronoun", "plural", "copula"}


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
        print(f"\nphonetic axes not yet exercised: {', '.join(missing)}")
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


# A source id as written in the spec `sources`: lowercase author + year with an
# optional descriptive slug (baptista2002, hagemeijermaurer_apics).
CITE_ID = r"\b[a-z][a-z_-]*[0-9]{4}[a-z_-]*\b"
# A free-text author-year citation the id form is meant to replace; rejected so
# an unresolvable prose citation cannot pass as grounding.
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
        spec = orthography2ipa.get(lect)
        src_ids = {getattr(s, "id", None) for s in (getattr(spec, "sources", None) or ())}
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
            notes = r["notes"]
            for ft in FREE_TEXT_CITE.findall(notes):
                failures.append(
                    f"{rid}: free-text citation {ft!r} in notes — use the source id "
                    f"(baptista2002-style) from the {lect} spec sources")
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
