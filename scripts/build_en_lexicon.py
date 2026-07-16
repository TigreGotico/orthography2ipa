#!/usr/bin/env python3
"""Build an English lexicon TSV (``word<TAB>ipa``) for callers to register.

The library bundles no lexicon. Write the file wherever you like and point
``orthography2ipa.register_lexicon("en-GB", <path>)`` at it (or drop it in a
directory and use ``set_lexicon_dir()`` / ``$ORTHOGRAPHY2IPA_LEXICON_DIR``).

The E3 lexicon-overlay mechanism (see ``orthography2ipa/lexicon.py`` and
``docs/data_model.md``) reads an optional per-language sidecar
a ``{code}.tsv`` (``word<TAB>ipa``) the caller registers, folded into the
engine's ``word_exceptions`` override pathway. This script regenerates the
one bundled pilot lexicon that proves the mechanism end-to-end.

Provenance (see ``docs/bibliography.md``):

- **Pronunciations** — the CMU Pronouncing Dictionary (``cmudict``), a
  hand-curated public-domain / BSD-style ARPABET lexicon of North American
  English. Each entry's ARPABET is converted to a **broad, non-rhotic
  (RP-leaning) IPA** approximation with the small deterministic map below,
  so it speaks roughly the same IPA convention as the ``en-GB`` rule spec.
  CMUdict is General American, so this pilot most helps the General-American
  ("en") evaluation; a full RP / en-GB lexicon belongs downstream (this is a
  ~5k-entry pilot, not a production lexicon — see ``docs/adding_a_language.md``).
- **Frequency ordering / entry selection** — the ``google-10000-english``
  frequency list (Google Web Trillion Word Corpus, MIT-licensed), used ONLY
  to pick which ~5k words to include (the highest-frequency ones). None of
  its content ships; only the CMU-derived IPA does.

Run from a checkout::

    python scripts/build_en_lexicon.py

It writes a UTF-8, NFC, sorted, first-entry-wins TSV. Re-running is
deterministic. The produced file is validated by ``tests/test_lexicon_overlay.py``
(the data-quality guard) and by ``orthography2ipa.lexicon.validate_lexicon_text``.
"""
from __future__ import annotations

import os
import sys
import unicodedata
import urllib.request
from typing import Dict, List

CMUDICT_URL = (
    "https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict"
)
FREQ_URL = (
    "https://raw.githubusercontent.com/first20hours/google-10000-english/"
    "master/google-10000-english.txt"
)
MAX_ENTRIES = 5000

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#: Default output. NOT inside the package — a lexicon is a corpus, not payload.
OUT_PATH = os.environ.get("O2I_LEXICON_OUT", os.path.join(REPO_ROOT, "en-GB.tsv"))

# ARPABET (2-letter phone, stress digit stripped) → broad non-rhotic IPA.
# Vowels lean RP/broad; consonants are the standard 1:1 map. ``ɡ`` is
# U+0261 (IPA script g) to match the en-GB spec's phoneme inventory.
_ARPA_VOWEL: Dict[str, str] = {
    "AA": "ɑː", "AE": "æ", "AO": "ɔː", "AW": "aʊ", "AY": "aɪ",
    "EH": "ɛ", "EY": "eɪ", "IH": "ɪ", "IY": "iː", "OW": "əʊ",
    "OY": "ɔɪ", "UH": "ʊ", "UW": "uː",
    # stress-sensitive vowels are handled in _arpa_to_ipa
}
_ARPA_CONS: Dict[str, str] = {
    "B": "b", "CH": "tʃ", "D": "d", "DH": "ð", "F": "f", "G": "ɡ",
    "HH": "h", "JH": "dʒ", "K": "k", "L": "l", "M": "m", "N": "n",
    "NG": "ŋ", "P": "p", "R": "ɹ", "S": "s", "SH": "ʃ", "T": "t",
    "TH": "θ", "V": "v", "W": "w", "Y": "j", "Z": "z", "ZH": "ʒ",
}
_VOWEL_IPA = set("aeiouɑæɔəɛɪʊʌɜ")


def _arpa_to_ipa(arpa: str) -> str:
    """Convert a space-separated ARPABET string to broad non-rhotic IPA.

    Rhoticity: coda ``ɹ`` (an ``R`` not immediately before a vowel phone) is
    dropped, and the rhotic vowels ``ER``/``AH`` map to their non-rhotic /
    reduced RP values, so e.g. ``K AA1 R`` → ``kɑː`` (RP "car"), ``B ER1 D``
    → ``bɜːd`` (RP "bird").
    """
    phones = arpa.split()
    ipa_tokens: List[str] = []
    is_vowel: List[bool] = []
    for ph in phones:
        base = ph.rstrip("0123456789")
        stress = ph[len(base):]
        if base == "ER":
            sym = "ɜː" if stress in ("1", "2") else "ə"
            vowel = True
        elif base == "AH":
            sym = "ə" if stress == "0" else "ʌ"
            vowel = True
        elif base in _ARPA_VOWEL:
            sym = _ARPA_VOWEL[base]
            vowel = True
        elif base in _ARPA_CONS:
            sym = _ARPA_CONS[base]
            vowel = False
        else:
            return ""  # unknown phone → skip whole entry
        ipa_tokens.append(sym)
        is_vowel.append(vowel)

    # drop coda ɹ (not immediately followed by a vowel phone) — non-rhoticity
    out: List[str] = []
    for i, tok in enumerate(ipa_tokens):
        if tok == "ɹ":
            nxt = is_vowel[i + 1] if i + 1 < len(ipa_tokens) else False
            if not nxt:
                continue
        out.append(tok)
    return "".join(out)


def _fetch(url: str) -> str:
    with urllib.request.urlopen(url) as resp:  # noqa: S310 — trusted raw URLs
        return resp.read().decode("utf-8", errors="replace")


def build() -> List[str]:
    cmu_text = _fetch(CMUDICT_URL)
    freq_text = _fetch(FREQ_URL)

    # CMU: first pronunciation per word wins (skip ``word(2)`` variants).
    cmu: Dict[str, str] = {}
    for line in cmu_text.splitlines():
        line = line.strip()
        if not line or line.startswith(";;;"):
            continue
        parts = line.split()
        word = parts[0].lower()
        if "(" in word or len(parts) < 2 or not word.isalpha():
            continue
        if word in cmu:
            continue
        ipa = _arpa_to_ipa(" ".join(parts[1:]))
        if ipa:
            cmu[word] = unicodedata.normalize("NFC", ipa)

    freq_order = [w.strip().lower() for w in freq_text.splitlines() if w.strip()]
    rows: Dict[str, str] = {}
    for word in freq_order:
        if len(rows) >= MAX_ENTRIES:
            break
        if word.isalpha() and word in cmu and word not in rows:
            rows[word] = cmu[word]

    lines = [f"{w}\t{rows[w]}" for w in sorted(rows)]
    return lines


def main() -> None:
    lines = build()
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines))
        fh.write("\n")
    print(f"wrote {len(lines)} entries to "
          f"{os.path.relpath(OUT_PATH, REPO_ROOT)}", file=sys.stderr)


if __name__ == "__main__":
    main()
