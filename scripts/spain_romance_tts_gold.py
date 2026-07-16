#!/usr/bin/env python3
"""Spain-Romance TTS gold set — authoring, drafting and validation tooling.

The gold set lives in ``orthography2ipa/data/gold/spain_romance_tts/<code>.tsv``
(one file per lect) and provides phonetically diverse, register-appropriate,
literature-justified sentences for validating the TTS voices of the Romance
lects of Spain — Castilian and its regional accents, Galician, Asturleonese,
Aragonese, Catalan/Valencian, Aranese Occitan, and the peripheral Romance of
the Iberian west (Fala, Extremaduran, Mirandese-adjacent Sanabrese, Ladino).
Each lect is written in its **own** orthographic convention (Galician RAG or
reintegrado, Asturian ALLA, Aragonese Academia, Catalan IEC/AVL, …), so a row
is the sentence a TTS receives; there is no separate ``raw`` column and no
diacritization-completeness check.

Subcommands
-----------
checklist <lect> [tsv]
    Derive the dialect-discriminative feature checklist for a lect and (if the
    gold TSV exists) report which axes the current sentences already exercise
    and which are still missing. Use this to author additional sentences.

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

GOLD_DIR = REPO_ROOT / "orthography2ipa" / "data" / "gold" / "spain_romance_tts"

# The Spain-Romance lect roster. `checklist` accepts any of them so sentences
# can be authored ahead of the gold file; `validate` gates only the lects that
# already have a TSV (the rest report as pending). Concurrent authors touch
# only their own family's TSVs; keep this list append-friendly.
LECTS = [
    # Castilian and its peninsular / insular accents
    "es-ES",
    "es-ES-x-andalusia-e", "es-ES-x-andalusia-w",
    "es-ES-x-canarias", "es-ES-x-cantabria", "es-ES-x-extremadura",
    "es-ES-x-medieval", "es-ES-x-murcia",
    # Galician (RAG and reintegrado registers, dialect blocks)
    "gl", "gl-x-central", "gl-x-occidental", "gl-x-oriental",
    "gl-x-reintegrado", "gl-x-eonavia",
    # Asturleonese
    "ast", "ast-ES-x-leon",
    "ast-x-leon", "ast-x-cantabrian", "ast-x-occidental", "ast-x-oriental",
    "ast-x-pasiego", "ast-x-sanabria",
    # Aragonese and its high-valley varieties
    "an", "an-x-ansotano", "an-x-belsetan", "an-x-benasques", "an-x-cheso",
    "an-x-chistabin", "an-x-occidental", "an-x-oriental", "an-x-tensino",
    # Catalan / Valencian
    "ca", "ca-x-balear", "ca-x-occidental", "ca-x-valencia", "ca-x-medieval",
    # Aranese Occitan, Fala, Extremaduran, mixed, Ladino
    "oc-x-aranes", "ext", "fax", "mxi", "lad",
    # Caribbean Spanish (Americas extension)
    "es-VE", "es-VE-x-andino", "es-VE-x-llanero", "es-VE-x-maracucho",
    "es-CU", "es-DO", "es-PR",
    # Andean Spanish (Americas extension): Peru and Ecuador
    "es-PE", "es-PE-x-lima", "es-PE-x-andino", "es-PE-x-amazonico",
    "es-EC", "es-EC-x-andino", "es-EC-x-costa",
    # Rioplatense family (Argentina / Uruguay / Paraguay)
    "es-AR", "es-AR-x-cordoba", "es-AR-x-cuyo", "es-AR-x-litoral",
    "es-AR-x-norte", "es-AR-x-patagonia", "es-UY", "es-PY",
    # American Spanish — Bolivian and Chilean varieties (own morphosyntax/lexicon)
    "es-BO", "es-BO-x-andino", "es-BO-x-camba",
    "es-CL", "es-CL-x-andino", "es-CL-x-chilote",
    # Central American and Equatoguinean Spanish (Americas/Africa extension)
    "es-GT", "es-HN", "es-SV", "es-NI", "es-CR", "es-PA", "es-GQ",
    # Latin American Spanish cover + Mexican varieties (Americas extension)
    "es-419", "es-MX", "es-MX-x-norte", "es-MX-x-yucatan", "es-MX-x-costa",
    # Colombian Spanish (Americas extension): bogotano + regional accents
    "es-CO", "es-CO-x-costa", "es-CO-x-llanero", "es-CO-x-pacifico",
    "es-CO-x-paisa", "es-CO-x-santander", "es-CO-x-valluno",
    # (The Spanish-lexified creoles cbk-zam, pap and pln are NOT Iberian
    # Romance; they moved to the unified creole harness —
    # scripts/iberian_creole_tts_gold.py — with the rest of the creole roster.)
    # Basque (mega-set): Euskara Batua + the dialect specs. Not Romance, but an
    # Iberian language sharing the harness; its rows use the eu_* feature axes.
    "eu", "eu-x-bizkaiera", "eu-x-gipuzkera", "eu-x-lapurtera",
    "eu-x-nafarra-garaia", "eu-x-nafarra-beherea", "eu-x-zuberera",
    "eu-x-erronkariera",
]
MIN_ROWS = 5
FIELDS = ["id", "sentence", "ipa", "gloss_en", "features", "notes"]

# --- orthographic helpers used by the sentence-level predicates -----------
VOWELS_ORTH = set("aeiouáàâãéèêëíïóòôõúùüAEIOUÁÀÂÃÉÈÊËÍÏÓÒÔÕÚÙÜ")
FRONT_VOWELS_ORTH = set("eiéèêëíïEIÉÈÊËÍÏ")
# grapheme onsets that trigger regressive voicing of a preceding coda /s/
VOICED_ONSET = set("bdgvzlmnrjBDGVZLMNRJ") | VOWELS_ORTH


def _words(sentence: str):
    """Sentence split into word tokens with edge punctuation stripped."""
    return [w for w in re.findall(r"[^\s]+", sentence) if re.search(r"\w", w)]


def _strip_punct(word: str) -> str:
    return word.strip(".,;:!?¿¡\"'«»()—-·").lower()


def _has_cz_grapheme(sentence: str) -> bool:
    """True if the sentence has a ⟨c⟩ before a front vowel, a ⟨z⟩ or a ⟨ç⟩ —
    the graphemes whose reflex splits distinción [θ], seseo [s] and ceceo."""
    s = sentence.lower()
    for m in re.finditer(r"c", s):
        i = m.end()
        if i < len(s) and s[i] in FRONT_VOWELS_ORTH:
            return True
    return bool(re.search(r"[zç]", s))


def _has_ll_or_lh(sentence: str) -> bool:
    """True if the sentence has a ⟨ll⟩ or ⟨lh⟩ — the graphemes realised as the
    palatal lateral [ʎ] in ll/y-distinguishing lects."""
    return bool(re.search(r"ll|lh", sentence.lower()))


def _has_ll_or_y(sentence: str) -> bool:
    """True if the sentence has a ⟨ll⟩ or a consonantal (prevocalic) ⟨y⟩ — the
    graphemes that merge to [ʝ] in yeísta lects."""
    s = sentence.lower()
    return bool(re.search(r"ll", s) or re.search(r"y[aeiouáéíóúàèìòù]", s))


def _has_initial_palatal_grapheme(sentence: str) -> bool:
    """True if a word begins with ⟨ll⟩, ⟨lh⟩, ⟨ñ⟩ or ⟨nh⟩ — the Asturleonese /
    NW-Iberian initial L-/N- palatalisation the ipa realises as [ʎ]/[ɲ]."""
    for w in _words(sentence):
        w = _strip_punct(w)
        if w.startswith(("ll", "lh", "ñ", "nh")):
            return True
    return False


def _has_gheada_grapheme(sentence: str) -> bool:
    """True if the sentence has a /g/-phoneme grapheme — ⟨g⟩ before a back
    vowel, ⟨gu⟩ before a front vowel, or ⟨g⟩ before a liquid/nasal. This is the
    /g/ that Galician gheada turns into a pharyngeal/glottal fricative (the
    ⟨ge gi⟩ [x] outcome is excluded)."""
    s = sentence.lower()
    return bool(re.search(r"g[aouáóúàò]|gu[eiéí]|g[lrn]", s))


def _coda_s_grapheme(sentence: str) -> bool:
    """True if any word has an ⟨s⟩ in coda (before a consonant or word-final) —
    the position where southern lects aspirate ([h]) or delete /s/."""
    for w in _words(sentence):
        w = _strip_punct(w)
        for m in re.finditer(r"s", w):
            i = m.end()
            if i >= len(w) or w[i] not in VOWELS_ORTH:
                return True
    return False


def _has_final_u_grapheme(sentence: str) -> bool:
    """True if a word ends in a full ⟨u⟩ vowel (preceded by a consonant, so a
    falling-diphthong glide ⟨…ou/iu⟩ does not count) — the Asturleonese atonic
    final -o>-u raising / masculine metaphony axis."""
    for w in _words(sentence):
        w = _strip_punct(w)
        if len(w) >= 2 and w[-1] == "u" and w[-2] not in VOWELS_ORTH and w[-2] not in "qg":
            return True
    return False


# IPA vowel letters (nucleus carriers) for the Iberian Romance inventory.
IPA_VOWELS = set("aeiouɛɔəɐæɪʊ")


def _onset_h_ipa(ipa: str) -> bool:
    """True if a [ħ] or [h] surfaces in *onset* position — followed by a vowel.
    This is the gheada reflex of /g/ (an onset before a vowel), distinct from
    an aspirated coda /s/ [h] which stands before a consonant or a boundary."""
    for m in re.finditer(r"[ħh]", ipa):
        j = m.end()
        while j < len(ipa) and (unicodedata.combining(ipa[j]) or ipa[j] in "ˈˌ"):
            j += 1
        if m.group() == "ħ":
            return True  # ħ is only ever the gheada reflex here
        if j < len(ipa) and ipa[j] in IPA_VOWELS:
            return True
    return False


def _coda_h_ipa(ipa: str) -> bool:
    """True if an [h] surfaces in *coda* position — followed by a consonant or
    a word/utterance boundary. This is the aspirated-/s/ reflex; an onset [h]
    before a vowel (gheada) is excluded, mirroring the coda-sibilant rule."""
    for m in re.finditer(r"h", ipa):
        j = m.end()
        while j < len(ipa) and (unicodedata.combining(ipa[j]) or ipa[j] in "ˈˌ"):
            j += 1
        if j >= len(ipa) or ipa[j] == " ":
            return True  # word-final / utterance-final
        if ipa[j] not in IPA_VOWELS:
            return True  # pre-consonantal
    return False


def _has_final_u_ipa(ipa: str) -> bool:
    """True if some word in the ipa ends in a [u] vowel (stress/combining marks
    stripped from the end) — the realised side of the final -u axis."""
    for tok in ipa.split():
        tok = tok.rstrip("ˈˌ")
        while tok and unicodedata.combining(tok[-1]):
            tok = tok[:-1]
        if tok.endswith("u"):
            return True
    return False


def _has_sandhi_junction(sentence: str) -> bool:
    """True if some word boundary is a cross-word sandhi site: a vowel-final
    word before a vowel-initial word (elision / liaison), or an /s/-final word
    before a voiced-onset word (regressive sibilant voicing)."""
    ws = [_strip_punct(w) for w in _words(sentence)]
    ws = [w for w in ws if w]
    for a, b in zip(ws, ws[1:]):
        if a[-1] in VOWELS_ORTH and b[0] in VOWELS_ORTH:
            return True
        if a[-1] in "sScC" and b[0] in VOICED_ONSET:
            return True
    return False


def _diphthong_ie_ue(sentence: str, ipa: str) -> bool:
    """True if the sentence spells a Romance rising diphthong ⟨ie ue uo⟩ AND the
    ipa realises a corresponding glide+mid sequence [je we wo] — the tonic
    Ĕ>ie / Ŏ>ue(uo) diphthongisation that splits diphthongising Romance from
    the non-diphthongising Galician-Portuguese and Catalan reflexes.

    The ⟨u⟩ of ⟨que qui gue gui⟩ is a mute orthographic marker ([k]/[ɡ]), not a
    glide, so a ⟨ue⟩ inside ``aquel``/``pequeño`` must NOT count — only a ⟨ue uo⟩
    whose ⟨u⟩ is not preceded by ⟨q g⟩, or a ⟨ie⟩, together with a realised
    glide+mid [je we wo] in the ipa."""
    return bool(re.search(r"ie|(?<![qg])u[eo]", sentence.lower())) and \
        bool(re.search(r"[jw][eo]", ipa))


# --- Basque (eu family) position-tied predicates ---------------------------
# Basque is not Romance, but it is an Iberian language and rides the same gold
# harness (the mega-set). Its diagnostic axes are the three-way coronal sibilant
# and affricate system, the palatal series, Souletin front-rounded [y] and the
# continental laryngeal [h]. Each predicate below pairs an orthographic trigger
# (Euskara Batua / dialect spelling) with the position-tied ipa reflex the engine
# emits, so a tag proves the row genuinely exercises the axis. Sibilant combining
# marks: apico-alveolar ⟨s⟩ → [s̺] (s + U+033A), lamino-alveolar ⟨z⟩ → [s̻]
# (s + U+033B), post-alveolar ⟨x⟩ → [ʃ]; affricates ⟨ts tz tx⟩ → [ts̺ ts̻ tʃ].
_S_APIC = "s̺"   # [s̺] apico-alveolar
_S_LAM = "s̻"    # [s̻] lamino-alveolar


def _eu_lone_s(sentence: str) -> bool:
    """⟨s⟩ not part of the affricate ⟨ts⟩ (and not the digraph-less ⟨x⟩)."""
    return bool(re.search(r"(?<!t)s", sentence.lower()))


def _eu_lone_z(sentence: str) -> bool:
    """⟨z⟩ not part of the affricate ⟨tz⟩."""
    return bool(re.search(r"(?<!t)z", sentence.lower()))


def _eu_apical_ipa(ipa: str) -> bool:
    """[s̺] outside an affricate (a plain apico-alveolar fricative)."""
    return bool(re.search(r"(?<!t)" + _S_APIC, ipa))


# Categorical sandhi of the negative particle ez /es̻/ before a following
# auxiliary/verb-initial consonant (ez+d→ezt, ez+z→etz, ez+n→en, ez+l→el,
# ez+b→ezp, ez+g→ezk). The predicate proves BOTH the orthographic trigger (a
# lone ⟨ez⟩ word before a d/z/n/l/b/g onset) AND that the contraction reflex
# surfaced — i.e. the un-contracted voiced sequence is absent from the ipa.
# per trigger onset, the (ez-token, next-token-prefix) reflex the rule produces:
# ez /es̻/ either keeps its sibilant while the onset devoices (d/b/g) or loses it
# to coalescence/deletion (z/n/l).
_EU_EZ_REFLEX = {
    "d": ("e" + _S_LAM, "t"), "b": ("e" + _S_LAM, "p"), "g": ("e" + _S_LAM, "k"),
    "z": ("e", "t" + _S_LAM), "n": ("e", "n"), "l": ("e", "l"),
}


def _eu_ez_sandhi(sentence: str, ipa: str) -> bool:
    """True iff a lone ⟨ez⟩ before a d/z/n/l/b/g onset surfaced with its
    contraction reflex at that exact juncture (token-aligned, so an unrelated
    ⟨z⟩-final word elsewhere cannot spoof it)."""
    ws = [_strip_punct(w).lower() for w in _words(sentence)]
    ws = [w for w in ws if w]
    toks = ipa.split()
    if len(ws) != len(toks):
        return False
    for i, (a, b) in enumerate(zip(ws, ws[1:])):
        if a != "ez" or not b or b[0] not in _EU_EZ_REFLEX:
            continue
        left, right_prefix = _EU_EZ_REFLEX[b[0]]
        if toks[i] == left and toks[i + 1].startswith(right_prefix):
            return True
    return False


def _eu_laminal_ipa(ipa: str) -> bool:
    """[s̻] outside an affricate (a plain lamino-alveolar fricative)."""
    return bool(re.search(r"(?<!t)" + _S_LAM, ipa))


def _eu_postalveolar_ipa(ipa: str) -> bool:
    """[ʃ] outside the affricate [tʃ] (a plain post-alveolar fricative)."""
    return bool(re.search(r"(?<!t)ʃ", ipa))


# --- feature tags: each predicate is computable from (sentence, ipa) -------
# "ipa" predicates demonstrate a realised reflex; "orth" predicates prove the
# sentence exercises an axis whose reflex varies across lects; "both" require an
# orthographic trigger AND the predicted (position-tied) ipa so the tag proves
# the row genuinely exercises the axis.
FEATURES = {
    # /θ ~ s/ merger axis: distinción keeps [θ], seseo merges ⟨c z⟩ to [s]
    "distincion":       ("both", lambda s, ipa: _has_cz_grapheme(s) and "θ" in ipa),
    "seseo":            ("both", lambda s, ipa: _has_cz_grapheme(s)
                                                and "θ" not in ipa and "s" in ipa),
    # ll/y contrast: [ʎ] retained (distinguishing) vs merged to [ʝ] (yeísmo)
    "lateral_palatal":  ("both", lambda s, ipa: _has_ll_or_lh(s) and "ʎ" in ipa),
    "yeismo":           ("both", lambda s, ipa: _has_ll_or_y(s)
                                                and "ʝ" in ipa and "ʎ" not in ipa),
    # palatal nasal [ɲ] (⟨ñ nh ny⟩) present
    "palatal_nasal":    ("ipa",  lambda s, ipa: "ɲ" in ipa),
    # Asturleonese initial L-/N- palatalisation (word-initial ⟨ll lh ñ nh⟩ → [ʎ ɲ])
    "palatal_initial":  ("both", lambda s, ipa: _has_initial_palatal_grapheme(s)
                                                and ("ʎ" in ipa or "ɲ" in ipa)),
    # Galician gheada: /g/ → [ħ] (onset), witnessed position-tied
    "gheada":           ("both", lambda s, ipa: _has_gheada_grapheme(s) and _onset_h_ipa(ipa)),
    # southern coda /s/ aspiration → [h] (coda), witnessed position-tied
    "coda_s_aspiration": ("both", lambda s, ipa: _coda_s_grapheme(s) and _coda_h_ipa(ipa)),
    # Romance diphthongisation ⟨ie ue uo⟩ → [je we wo]
    "diphthong_ie_ue":  ("both", _diphthong_ie_ue),
    # Asturleonese atonic final -o>-u raising / masculine metaphony
    "final_u":          ("both", lambda s, ipa: _has_final_u_grapheme(s) and _has_final_u_ipa(ipa)),
    # 7-vowel open-mid contrast (Galician / Catalan / Asturleonese)
    "open_mid":         ("ipa",  lambda s, ipa: "ɛ" in ipa or "ɔ" in ipa),
    # Eastern Andalusian vocalismo abierto: a lost/aspirated plural -s opens the
    # preceding vowel ([e o a] → [ɛ ɔ æ]), the surviving cue to the morpheme
    "vocalismo_abierto": ("both", lambda s, ipa: _coda_s_grapheme(s)
                                                 and ("æ" in ipa or "ɛ" in ipa or "ɔ" in ipa)),
    # Catalan atonic schwa reduction [ə]
    "schwa":            ("ipa",  lambda s, ipa: "ə" in ipa),
    # velar nasal [ŋ] (Galician coda -n / ⟨nh⟩, Catalan ⟨ng⟩)
    "velar_nasal":      ("ipa",  lambda s, ipa: "ŋ" in ipa),
    # voiced sibilant [z]/[ʒ] contrast (present in Catalan, absent in Galician)
    "sibilant_voicing": ("ipa",  lambda s, ipa: "z" in ipa or "ʒ" in ipa),
    # strong-R trill [r] reflex (excludes the ubiquitous tap [ɾ])
    "rhotic":           ("ipa",  lambda s, ipa: "r" in ipa),
    # cross-word sandhi site (elision / liaison / final-s voicing)
    "sandhi":           ("both", lambda s, ipa: _has_sandhi_junction(s)),
    # --- Basque (eu family) coronal, palatal, front-rounded and laryngeal axes
    # apico-alveolar ⟨s⟩ → [s̺]
    "eu_sibilant_apical":       ("both", lambda s, ipa: _eu_lone_s(s) and _eu_apical_ipa(ipa)),
    # lamino-alveolar ⟨z⟩ → [s̻] (absent in the Biscayan apical merger)
    "eu_sibilant_laminal":      ("both", lambda s, ipa: _eu_lone_z(s) and _eu_laminal_ipa(ipa)),
    # post-alveolar ⟨x⟩ → [ʃ]
    "eu_sibilant_postalveolar": ("both", lambda s, ipa: "x" in s.lower() and _eu_postalveolar_ipa(ipa)),
    # Biscayan apical/laminal neutralisation: ⟨z⟩ present yet no [s̻], only [s̺]
    "eu_sibilant_neutral":      ("both", lambda s, ipa: _eu_lone_z(s)
                                                        and _S_LAM not in ipa and _S_APIC in ipa),
    # apico-alveolar affricate ⟨ts⟩ → [ts̺]
    "eu_affricate_apical":      ("both", lambda s, ipa: "ts" in s.lower() and "t" + _S_APIC in ipa),
    # lamino-alveolar affricate ⟨tz⟩ → [ts̻]
    "eu_affricate_laminal":     ("both", lambda s, ipa: "tz" in s.lower() and "t" + _S_LAM in ipa),
    # post-alveolar affricate ⟨tx⟩ → [tʃ]
    "eu_affricate_postalveolar":("both", lambda s, ipa: "tx" in s.lower() and "tʃ" in ipa),
    # palatal plosive ⟨tt⟩ → [c] / ⟨dd⟩ → [ɟ]
    "eu_palatal_stop":          ("both", lambda s, ipa: bool(re.search(r"tt|dd", s.lower()))
                                                        and ("c" in ipa or "ɟ" in ipa)),
    # Souletin (and Roncalese) front-rounded ⟨ü⟩ → [y]
    "eu_front_rounded":         ("both", lambda s, ipa: "ü" in s.lower() and "y" in ipa),
    # laryngeal ⟨h⟩ → [h] (the continental aspiration axis)
    "eu_aspiration":            ("both", lambda s, ipa: "h" in s.lower() and "h" in ipa),
    # categorical negative-particle sandhi: ez /es̻/ contracts with a following
    # d/z/n/l/b/g onset (ezt-, etz-, en-, el-, ezp-, ezk-)
    "eu_negation_sandhi":       ("both", _eu_ez_sandhi),
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
# an optional descriptive slug. Both year-last (``hualde2005``,
# ``regueira1996``) and year-medial descriptive forms occur across the specs,
# so the trailing run allows ``_``/``-`` as well as letters.
CITE_ID = r"\b[a-z][a-z_-]*[0-9]{4}[a-z_-]*\b"
# A free-text author-year citation the id form is meant to replace, e.g.
# ``Hualde 2005``, ``Freixeiro Mato & Regueira 1996``. These escape the id
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
                    f"(hualde2005-style) from the {lect} spec sources")
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
