#!/usr/bin/env python3
"""Iberian-lexified creole TTS gold set — authoring, drafting and validation.

The gold set lives in ``orthography2ipa/data/gold/iberian_creole_tts/<code>.tsv``
(one file per lect) and provides phonetically diverse, register-appropriate,
literature-justified sentences for validating the TTS voices of the Portuguese-
and Spanish-lexified creoles traceable to the Iberian expansion — the Upper
Guinea, Gulf of Guinea, South and Southeast Asian Portuguese creoles and the
Iberian creoles of the Caribbean and the Philippines.

Each lect is written in its **own** convention — a stabilised community
orthography where one exists (Baxter's Malay-based spelling for Kristang), or
the scholarly Latin transcription the documentation uses where the community has
no stable written form (Cardoso's convention for Sri Lanka Portuguese, Clements'
transcription for Korlai). A row is therefore the string the TTS receives; there
is no separate ``raw`` column and no diacritisation-completeness check.

The sentences use genuine creole morphosyntax — preverbal TMA particles, creole
pronoun sets, reduced verb paradigms, substrate lexicon — not relexified
Portuguese/Spanish.

Subcommands
-----------
checklist <lect> [tsv]
    Derive the creole feature checklist for a lect and (if the gold TSV exists)
    report which axes the current sentences already exercise and which are still
    missing. Use this to author additional sentences.

draft <lect> <textfile>
    First-draft pipeline for new sentences (one per line, in the lect's genuine
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
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

GOLD_DIR = REPO_ROOT / "orthography2ipa" / "data" / "gold" / "iberian_creole_tts"

# The Iberian-creole lect roster. `checklist` accepts any of them so sentences
# can be authored ahead of the gold file; `validate` gates only the lects that
# already have a TSV (the rest report as pending). Concurrent authors touch
# only their own family's TSVs; keep this list append-friendly.
LECTS = [
    # South / Southeast Asian Portuguese creoles
    "mcm",  # Kristang / Papia Kristang (Malacca Creole Portuguese)
    "idb",  # Sri Lanka Portuguese Creole (Batticaloa/Trincomalee Burgher)
    "vkp",  # Korlai Indo-Portuguese ("Kristi")
    # Upper Guinea + Gulf of Guinea Portuguese creoles (Atlantic)
    "kea",  # Kabuverdianu (Cape Verdean), ALUPEC
    "pov",  # Guinea-Bissau Kriol (Upper Guinea)
    "pre",  # Principense (Lung'Ie), Gulf of Guinea
    "aoa",  # Angolar (Gulf of Guinea, Bantu-heavy, tonal)
    "cri",  # Forro / Santome (Gulf of Guinea), ALUSTP
    # Spanish-lexified Iberian creoles of the Caribbean and the Philippines
    "pap",  # Papiamento (Curaçao)
    "cbk-zam",  # Chavacano (Zamboangueno)
    "pln",  # Palenquero
]
MIN_ROWS = 5
FIELDS = ["id", "sentence", "ipa", "gloss_en", "features", "notes"]

# --- IPA-side helpers used by the feature predicates ----------------------
# Nasal consonants and stop/affricate onsets for the homorganic-cluster and
# nasal-coda predicates. These are creole-areal traits: homorganic NC clusters
# and syllabic nasals from Malay/African/South-Asian contact, and the nasal
# codas left when a Portuguese nasal vowel denasalised to oral vowel + nasal.
IPA_VOWELS = set("aeiouɛɔəæɐ")
NASAL_CONS = set("mnŋɲɳ")
STOP_AFFRIC = set("bpdtkɡʈɖ")
COMBINING_SKIP = "ˈˌ"
TILDE = "̃"  # U+0303 combining tilde (nasal vowel)
# Word-initial prenasalised onset graphemes ⟨mb nd ng mp⟩ of the Upper- and
# Gulf-of-Guinea Atlantic creoles (position-tied trigger for `prenasal_stop`).
NASAL_GRAPHS = ("mb", "nd", "ng", "mp")


def _ipa_tokens(ipa: str):
    return [t for t in ipa.split() if t.strip()]


def _base_chars(tok: str):
    """Token characters with stress marks removed, combining marks kept with
    their base (returned as a flat list preserving order)."""
    return [c for c in tok if c not in COMBINING_SKIP]


def _nasal_coda_ipa(ipa: str) -> bool:
    """True if a nasal consonant [m n ŋ ɲ ɳ] stands in coda — word-final or
    immediately before another consonant. This is the position the Portuguese
    nasal-vowel denasalisation leaves a nasal coda in (mão>mang, bom>bong), and
    the coda nasal of the homorganic clusters."""
    for tok in _ipa_tokens(ipa):
        cs = _base_chars(tok)
        for i, c in enumerate(cs):
            if c in NASAL_CONS:
                nxt = cs[i + 1] if i + 1 < len(cs) else None
                # skip a following combining mark to reach the next segment
                j = i + 1
                while j < len(cs) and unicodedata.combining(cs[j]):
                    j += 1
                nxt = cs[j] if j < len(cs) else None
                if nxt is None or (nxt not in IPA_VOWELS and not unicodedata.combining(nxt)):
                    return True
    return False


def _homorganic_nc_ipa(ipa: str) -> bool:
    """True if a nasal is immediately followed by a stop or affricate — the
    homorganic NC clusters (mb nd ŋɡ ndʒ ntʃ ɳɖ …) shared by these creoles as a
    Malay/African/South-Asian areal trait."""
    return bool(re.search(r"[mnŋɲɳ](?:tʃ|dʒ|[bpdtkɡʈɖ])", ipa))


def _syllabic_nasal_ipa(ipa: str) -> bool:
    """True if a syllabic nasal (nasal carrying the syllabicity mark U+0329, or
    a word-initial nasal directly before a consonant) is present — the Kristang
    ngua 'one', nsentu 'hundred' Malay-type syllabic onset nasals."""
    if "̩" in ipa:
        return True
    for tok in _ipa_tokens(ipa):
        cs = _base_chars(tok)
        # strip a leading stress mark already handled; look at first two segments
        if len(cs) >= 2 and cs[0] in NASAL_CONS and cs[1] in STOP_AFFRIC:
            return True
    return False


# --- orthographic / ipa helpers for the Atlantic (Guinea) creole axes ------
# The Upper- and Gulf-of-Guinea creoles add position-tied axes: word-initial
# prenasalised onsets and the ⟨gb kp⟩ labial-velar stops need an orthographic
# trigger paired with the predicted ipa, and the coda sibilant is read off the
# token-final segment.
def _words(sentence: str):
    return [w for w in re.findall(r"[^\s]+", sentence) if re.search(r"\w", w)]


def _strip_punct(word: str) -> str:
    return word.strip(".,;:!?¿¡\"'«»()—-·").lower()


def _has_initial_prenasal_graph(sentence: str) -> bool:
    """True if some word begins with a ⟨mb nd ng mp⟩ prenasalised onset."""
    for w in _words(sentence):
        if _strip_punct(w).startswith(NASAL_GRAPHS):
            return True
    return False


def _has_labial_velar_graph(sentence: str) -> bool:
    """True if some word contains a ⟨gb⟩ or ⟨kp⟩ labial-velar-stop digraph."""
    s = sentence.lower()
    return "gb" in s or "kp" in s


def _has_nasal_vowel(ipa: str) -> bool:
    """True if any vowel carries a combining tilde — a phonemic nasal vowel.
    Robust to NFC-composed forms (ã õ ũ ẽ ĩ), which decompose to base+tilde."""
    return TILDE in ipa or TILDE in unicodedata.normalize("NFD", ipa)


def _token_final_sibilant(ipa: str) -> bool:
    """True if some ipa word ends in a postalveolar sibilant [ʃ]/[ʒ] — the coda
    sibilant of kea (coda /s/ → [ʃ]) and cri (⟨x⟩ → [ʃ])."""
    for tok in ipa.split():
        tok = tok.rstrip("ˈˌ")
        while tok and unicodedata.combining(tok[-1]):
            tok = tok[:-1]
        if tok.endswith(("ʃ", "ʒ")):
            return True
    return False


# --- feature tags: each predicate is computable from (sentence, ipa) -------
# The unified creole roster spans three shelves — the South/Southeast-Asian
# Portuguese creoles (mcm idb vkp), the Upper- and Gulf-of-Guinea Atlantic
# creoles (kea pov pre aoa cri) and the Spanish-lexified Caribbean/Philippine
# creoles (pln cbk-zam pap). Most axes are witnessed directly on the realised
# IPA (kind "ipa"); the position-tied Atlantic axes (`prenasal_stop`,
# `labial_velar`) are kind "both": an orthographic trigger AND the predicted
# ipa, so a tag proves the row genuinely exercises the axis. Every tag stays
# machine-verifiable against the o2i output.
FEATURES = {
    # === South / Southeast-Asian Portuguese-creole axes (mcm idb vkp) =======
    # South-Asian retroflex series/allophones [ʈ ɖ ɳ ɭ ɽ] (Korlai stops from
    # Marathi contact; Sri Lanka [ɳ ɭ] allophones after back vowels)
    "retroflex":        ("ipa",  lambda s, ipa: any(c in ipa for c in "ʈɖɳɭɽ")),
    # aspirated / breathy-voiced stop series [pʰ tʰ ʈʰ kʰ bʱ dʱ ɡʱ] (Korlai)
    "aspirated":        ("ipa",  lambda s, ipa: "ʰ" in ipa or "ʱ" in ipa),
    # nasal coda from denasalisation / homorganic cluster coda
    "nasal_coda":       ("ipa",  lambda s, ipa: _nasal_coda_ipa(ipa)),
    # homorganic NC cluster anywhere (mb nd ŋɡ ndʒ …) — the medial/any-position
    # cluster; distinct from `prenasal_stop`, the word-initial Atlantic onset
    "prenasal_cluster": ("ipa",  lambda s, ipa: _homorganic_nc_ipa(ipa)),
    # syllabic / word-initial onset nasal (Kristang ngua, nsentu)
    "syllabic_nasal":   ("ipa",  lambda s, ipa: _syllabic_nasal_ipa(ipa)),
    # phonemic vowel length [ː] (Sri Lanka Portuguese)
    "vowel_length":     ("ipa",  lambda s, ipa: "ː" in ipa),
    # South-Asian labial approximant [ʋ] for etymological /v/ (Sri Lanka, Korlai)
    "approximant_v":    ("ipa",  lambda s, ipa: "ʋ" in ipa),
    # a surfacing glide [j w] (Kristang yo, Korlai lɔ̃j)
    "glide":            ("ipa",  lambda s, ipa: "j" in ipa or "w" in ipa),
    # === Upper- and Gulf-of-Guinea Atlantic creole axes (kea pov pre aoa cri) =
    # word-initial prenasalised onset ⟨mb nd ng mp⟩ → [mb nd ŋɡ mp] (position-
    # tied): the Gulf-of-Guinea / substrate prenasalised onset
    "prenasal_stop":    ("both", lambda s, ipa: _has_initial_prenasal_graph(s)
                                                and ("mb" in ipa or "nd" in ipa
                                                     or "ŋɡ" in ipa or "mp" in ipa)),
    # Gulf-of-Guinea labial-velar stop ⟨gb⟩ [ɡ͡b] / ⟨kp⟩ [k͡p] (position-tied)
    "labial_velar":     ("both", lambda s, ipa: _has_labial_velar_graph(s)
                                                and ("ɡ͡b" in ipa or "k͡p" in ipa)),
    # postalveolar sibilant [ʃ]/[ʒ] (⟨x⟩=[ʃ], ⟨j⟩=[ʒ]; Caribbean coda /s/→[ʃ])
    "postalveolar":     ("ipa",  lambda s, ipa: "ʃ" in ipa or "ʒ" in ipa),
    # coda sibilant: a word ends in [ʃ]/[ʒ] (kea coda /s/, cri ⟨x⟩, pap coda /s/)
    "coda_sibilant":    ("ipa",  lambda s, ipa: _token_final_sibilant(ipa)),
    # velarised coda /l/ → [ɫ] (kea)
    "velarized_l":      ("ipa",  lambda s, ipa: "ɫ" in ipa),
    # alveolar tap [ɾ] (single intervocalic ⟨r⟩)
    "tap":              ("ipa",  lambda s, ipa: "ɾ" in ipa),
    # lexical stress assigned in the ipa (kea)
    "stress":           ("ipa",  lambda s, ipa: "ˈ" in ipa),
    # === shared axes (both families; deduped to one predicate each) =========
    # phonemic nasal vowel (tilde): Korlai /ĩ ũ ɛ̃ ɔ̃/, the Atlantic ⟨ã ẽ ĩ õ ũ⟩;
    # Kristang and Sri Lanka denasalised — a discriminating axis
    "nasal_vowel":      ("ipa",  lambda s, ipa: _has_nasal_vowel(ipa)),
    # retained/creole affricates [tʃ dʒ] (⟨ch⟩ ⟨j⟩ ⟨tx dj⟩) and Korlai [ts dz]
    "affricate":        ("ipa",  lambda s, ipa: any(a in ipa for a in ("tʃ", "dʒ", "ts", "dz"))),
    # palatal nasal [ɲ] (⟨ny⟩ Kristang, ⟨nh⟩ Sri Lanka/kea, ⟨ñ⟩ Caribbean)
    "palatal_nasal":    ("ipa",  lambda s, ipa: "ɲ" in ipa),
    # velar nasal [ŋ] (⟨ng⟩; final -ng from denasalisation; prenasal onsets)
    "velar_nasal":      ("ipa",  lambda s, ipa: "ŋ" in ipa),
    # open-mid vowels [ɛ ɔ] (Sri Lanka; the cri seven-vowel contrast; pap ⟨ò⟩)
    "open_mid":         ("ipa",  lambda s, ipa: "ɛ" in ipa or "ɔ" in ipa),
    # central vowel / schwa [ə] (Korlai central vowel ⟨ï⟩)
    "schwa":            ("ipa",  lambda s, ipa: "ə" in ipa),
    # strong rhotic [ʀ]/[r] reflex (excludes the tap [ɾ]) — Kristang/Sri Lanka
    # trill, kea word-initial/⟨rr⟩ strong rhotic, pov alveolar /r/
    "strong_rhotic":    ("ipa",  lambda s, ipa: "ʀ" in ipa or "r" in ipa),
}
# Non-phonetic shape / morphosyntax tags: allowed in `features`, not
# machine-verified. The union carries the Asian set's `number` and the Atlantic
# set's creole-register tags (`tma`, `no_agreement`, `pronoun`, `plural`,
# `copula`) documenting genuine creole morphosyntax.
SHAPE_TAGS = {"statement", "question", "negation", "imperative", "number",
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
        print(f"  [{mark}] {tag:<18} ({kind})")
    for tag in sorted(SHAPE_TAGS):
        mark = "x" if tag in covered else " "
        print(f"  [{mark}] {tag:<18} (shape, not machine-verified)")
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


# A source id as written in the spec `sources`: lowercase author + year, with
# an optional descriptive slug (baxter1988, humetserdanelis2002, clements1996).
CITE_ID = r"\b[a-z][a-z_-]*[0-9]{4}[a-z_-]*\b"
# A free-text author-year citation the id form is meant to replace (``Baxter
# 1988``, ``Hume & Tserdanelis 2002``). These must be REJECTED so an
# unresolvable citation cannot pass as prose.
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
                    f"(baxter1988-style) from the {lect} spec sources")
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
