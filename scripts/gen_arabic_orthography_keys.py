#!/usr/bin/env python3
"""Generate the systematic Arabic connected-speech orthography keys.

Vocalized Arabic sentence orthography encodes several obligatory
connected-speech processes that single-letter grapheme keys cannot express.
This script derives them as maximal-munch multi-character grapheme keys and
writes them into the spec JSONs (pure data — the engine stays
language-agnostic):

1. **Sun-letter assimilation** (Ryding 2005 §2.9; Watson 2002 §2): the /l/ of
   the definite article assimilates to a following coronal, written in
   vocalized text as shadda on the sun letter (``السَّلام`` → /assalaːm/).
   Keys ``ال<S>ّ`` (and clitic + article combinations) are generated **per
   lect from that lect's own effective letter values**, so a dialect that
   shifts a sun letter (e.g. Egyptian ث → /t, s/, Badawi & Hinds 1986)
   assimilates to its own reflex. A dialect spec only receives entries that
   differ from what it inherits from Classical Arabic (arb).
2. **Proclitics + article** (Ryding 2005 §2.11): ``وَال`` /wal/, ``فَال``
   /fal/, ``بِال`` /bil/, ``كَال`` /kal/, ``لِل`` /lil/ — the hamzat-wasl alif
   of the article is silent after the clitic vowel.
3. **Tā marbūṭa liaison** (Ryding 2005 §2.5): ``ة`` followed by a vowel sign
   or tanwīn is /at .../ (``المَدْرَسَةِ`` → /almadrasati/); bare final ``ة``
   keeps the pausal /a/ (existing key).
4. **Tanwīn fatḥ + silent alif/ʼalif maqṣūra** (Ryding 2005 §2.4): the alif
   written after ً is a spelling seat, not /aː/ — ``جِدًّا`` → /dʒiddan/.
5. Fix reversed vowel-letter digraphs in arb: ``يَ`` is /ja/ (consonant +
   fatḥa), not the diphthong /aj/ (that is ``َي``); likewise ``وَ`` /wa/,
   ``يِ`` /ji/, ``وُ`` /wu/, ``اَ`` (wasl alif + fatḥa) /a/. Adds the
   glide-preserving keys ``ِيَ`` /ija/, ``ِيّ`` /ijj/, ``ُوَ`` /uwa/,
   ``ُوّ`` /uww/ so intervocalic glides survive maximal munch
   (``صَافِيَة`` → /sˤaːfija(t)/).
6. **Sandhi repairs** (arb, inherited): the hamzat-wasl elision rule deleted
   the *left* vowel instead of the article's /a/ — rewritten with
   ``right_transform``; the pausal-tanwīn rule (right context ``$``) matched
   before *every* word, deleting every final /n/ — removed (the gold style
   keeps full tanwīn); the cross-word sun-assimilation rule could only ever
   fire on a real /l/-final word before a coronal-initial word, which MSA
   does not assimilate — removed (assimilation is word-internal, handled by
   the keys above).

Idempotent: re-running produces the same specs. Run after changing any
Arabic letter mapping so the derived keys stay in sync.
"""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
DATA = REPO_ROOT / "orthography2ipa" / "data"

LECTS = [
    "arb", "ar",
    "ar-EG", "ar-IQ", "ar-IQ-x-qeltu", "ar-SD", "ar-TD", "ar-NG",
    "ar-SY", "ar-LB", "ar-JO", "ar-PS",
    "ar-AE", "ar-BH", "ar-KW", "ar-QA", "ar-OM",
    "ar-SA-x-najd", "ar-SA-x-hejaz", "ar-YE",
    "ar-MA", "ar-TN", "ar-DZ", "ar-LY", "ar-MR",
    # abstract ancestors: keys placed here benefit every descendant
    "ar-x-mashriqi", "ar-x-maghrebi", "ar-x-peninsular", "ar-x-levantine", "ar-x-gulf",
]

SUN = "تثدذرزسشصضطظلن"
SHADDA = "ّ"
# clitic orthography -> clitic IPA (invariant across lects in vocalized text)
CLITICS = {"وَ": "wa", "فَ": "fa", "بِ": "bi", "كَ": "ka", "وِ": "wi"}

ARB_FIXES = {
    "يَ": ["ja"], "وَ": ["wa"], "يِ": ["ji"], "وُ": ["wu"], "اَ": ["a"],
}
ARB_ADDITIONS = {
    "اَل": ["al"],
    # hamza seats with baked vowels (أ→ʔa, إ→ʔi) double the vowel when the
    # text is fully vocalized (أَ = seat + explicit fatha) — vocalized digraphs
    "أَ": ["ʔa"], "أُ": ["ʔu"], "إِ": ["ʔi"],
    "ِيَ": ["ija"], "ُوَ": ["uwa"],
    # geminate glides: the tokenizer pre-expands shadda to a doubled letter
    # (phonetok "Gemination" transform), so the keys target the doubled form
    "ِيي": ["ijj"], "ُوو": ["uww"],
    # doubled glides from the shadda expansion in other vowel contexts, and
    # final /aːj/ (e.g. شاي); fatha + final ta marbuta = /a/ (no doubling)
    "وو": ["ww"], "يي": ["jj"], "َوو": ["aww"], "َيي": ["ajj"],
    "َاي": ["aːj"], "ُوي": ["uːj"], "ُوَا": ["uwaː"], "ِيَا": ["ijaː"],
    # vocalized glide onsets: fatha + glide + vowel is /aCV/, not a diphthong
    # (the diphthong keys َو/َي only apply when the glide closes the syllable)
    "َوَ": ["awa"], "َوِ": ["awi"], "َوُ": ["awu"], "َوَا": ["awaː"],
    "َيَ": ["aja"], "َيِ": ["aji"], "َيُ": ["aju"], "َيَا": ["ajaː"],
    "َة": ["a"],
    # silent alif al-fasila after the plural waw (كتبوا = /katabuː/)
    "ُوا": ["uː"],
    # the colloquial article اِلْ (Cairene /il/, Badawi & Hinds 1986)
    "اِل": ["il"],
    # ta marbuta + vowel/tanwin = /t/ + vowel: the vowel of the preceding
    # syllable is written on the preceding letter (Ryding 2005 §2.5)
    "ةَ": ["ta"], "ةُ": ["tu"], "ةِ": ["ti"],
    "ةً": ["tan"], "ةٌ": ["tun"], "ةٍ": ["tin"],
    "ًا": ["an"], "ًى": ["an"], "اً": ["an"],
    "وَال": ["wal"], "فَال": ["fal"], "بِال": ["bil"], "كَال": ["kal"], "لِل": ["lil"], "وِال": ["wil"],
}

SANDHI = [
    {
        "id": "AR_HAMZAT_WASL_ARTICLE",
        "name": "hamzat-al-wasl (article) elision",
        "left_context": "[aiueoɑæə]ː?$",
        "right_context": "^[aɑ](?=[^aeiouɑɐæɪʊəɛɔː])",
        "transform": None,
        "right_transform": "",
        "obligatory": True,
        "notes": "The hamzat-wasl /a/ of a word-initial definite article elides after a "
                 "vowel-final word: fiː albajti → fiː lbajti; fiː aʃʃamsi → fiː ʃʃamsi "
                 "(Ryding 2005 §2.10). Only the article's seat vowel is deleted "
                 "(right_transform) — hamzat qatʕ words start /ʔ/ and are untouched.",
    },
]


VOWELS = {"\u064e": "a", "\u064f": "u", "\u0650": "i"}


def sun_keys(letter_ipa):
    """Assimilated-article keys for one effective letter mapping.

    The tokenizer's Arabic gemination transform rewrites consonant+shadda to
    a doubled consonant before trie matching, so the keys are generated on
    the doubled-letter form ("السس" etc.)."""
    out = {}
    prefixes = {"ال": "a", "اَل": "a", "اِل": "i", "لِل": "li"}
    for cl_orth, cl_ipa in CLITICS.items():
        prefixes[cl_orth + "ال"] = cl_ipa
    for s in SUN:
        alts = letter_ipa.get(s)
        if not alts:
            continue
        gem = [a + a for a in alts]
        for p_orth, p_ipa in prefixes.items():
            # the tokenizer pre-expands shadda into a doubled letter, so the
            # assimilated article is seen as e.g. "السس" — key the doubled form
            out[p_orth + s + s] = [p_ipa + g for g in gem]
    return out


def main():
    import orthography2ipa

    # effective single-letter values per lect (inheritance resolved)
    effective = {}
    for code in LECTS:
        g = orthography2ipa.get(code).graphemes
        effective[code] = {s: list(g[s]) for s in SUN if s in g}

    # arb gets the full derived set + fixes; descendants only get entries
    # whose effective letter values differ from their nearest patched ancestor.
    def ancestors_of(code, spec_cache={}):
        import orthography2ipa
        spec = orthography2ipa.get(code)
        chain = []
        cur = spec
        while getattr(cur, "parent", None):
            chain.append(cur.parent)
            try:
                cur = orthography2ipa.get(cur.parent)
            except Exception:
                break
        return chain

    changed = []
    for code in LECTS:
        path = DATA / f"{code}.json"
        spec = json.loads(path.read_text(encoding="utf-8"))
        graphemes = spec.get("graphemes") or {}
        before = json.dumps(graphemes, sort_keys=True, ensure_ascii=False)

        if code == "arb":
            graphemes.update(ARB_FIXES)
            graphemes.update(ARB_ADDITIONS)
            graphemes.update(sun_keys(effective["arb"]))
            spec["sandhi_rules"] = SANDHI
        else:
            # letters whose effective value differs from the nearest ancestor
            # in LECTS (falling back to arb) need their own derived keys
            anc = next((a for a in ancestors_of(code) if a in effective), "arb")
            diff = {s: v for s, v in effective[code].items()
                    if v != effective.get(anc, {}).get(s)}
            if diff:
                graphemes.update(sun_keys(diff))

        spec["graphemes"] = graphemes
        after = json.dumps(spec.get("graphemes"), sort_keys=True, ensure_ascii=False)
        if before != after or code == "arb":
            path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
            changed.append(code)
    print("updated:", ", ".join(changed))


if __name__ == "__main__":
    main()
