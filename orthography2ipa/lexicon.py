"""Optional per-language IPA lexicon overlay (Workstream E3).

A **lexicon** is a convention-based sidecar file
``orthography2ipa/data/lexicons/{code}.tsv`` — one ``word<TAB>ipa`` pair per
line, UTF-8, NFC-normalised, sorted, first-entry-wins. It is the unblocker
for deep-orthography languages (English, Danish, Irish) whose rule systems
cannot reach production accuracy from grapheme rules alone: a lexicon lets a
spec ship a finite list of known whole-word pronunciations *without* inflating
the JSON ``word_exceptions`` block, and without any new ``LanguageSpec`` field.

Design contract
---------------

- **Lazy.** Importing :mod:`orthography2ipa` (and even loading a
  :class:`~orthography2ipa.types.LanguageSpec`) reads **no** lexicon file. A
  language's TSV is read once, on the first :func:`get_lexicon` call for that
  code (i.e. the first time a word is transcribed for it), and cached via
  :func:`functools.lru_cache` for the process lifetime.
- **Same pathway as ``word_exceptions``.** :class:`~orthography2ipa.g2p.G2P`
  folds a lexicon hit into the *exact* override path that
  ``spec.word_exceptions`` uses — so a lexicon entry still routes through
  stress-mark insertion and cross-word sandhi, and is reported with the same
  ``confidence == 1.0`` (a certain answer).
- **Precedence.** inline ``spec.word_exceptions`` > lexicon > rules. An inline
  exception always wins over the sidecar; the sidecar always wins over the
  grapheme/positional beam.
- **Absent lexicon → byte-identical.** A language with no ``{code}.tsv`` gets
  an empty mapping and behaves exactly as it did before this module existed.

The shipped pilot is ``en-GB.tsv`` (CMUdict-derived; see
``scripts/build_en_lexicon.py`` and ``docs/bibliography.md``).
"""
from __future__ import annotations

import unicodedata
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Tuple

__all__ = [
    "LEXICON_DIR",
    "get_lexicon",
    "available_lexicon_codes",
    "lexicon_path",
    "parse_lexicon_text",
    "validate_lexicon_text",
    "is_ipa_string",
]

LEXICON_DIR = Path(__file__).parent / "data" / "lexicons"

# Non-letter IPA symbols allowed in a transcription: length/stress/tone marks,
# spacing modifiers (aspiration, palatalisation …), tie bars and the affricate
# ties, plus combining diacritics (voiceless ring, dental bridge, no-audible-
# release …). Base *letters* are validated separately by Unicode category.
_IPA_MODIFIERS = frozenset(
    "ːˑ"          # length
    "ˈˌ"          # primary / secondary stress
    "ʰʷʲˠˤʼⁿ"     # release / secondary-articulation / ejective / nasal-release
    "‿͜͡"          # linking / tie bars
    ".|‖"         # syllable / prosodic boundaries (tolerated, not required)
    "˥˦˧˨˩"        # tone letters
)


def _is_ipa_char(ch: str) -> bool:
    if ch in _IPA_MODIFIERS:
        return True
    cat = unicodedata.category(ch)
    # Combining marks (IPA diacritics) and letters (Latin + IPA Extensions,
    # e.g. ɡ ʃ ð ŋ ɐ ɹ ʊ) are the phonetic-symbol classes.
    if cat.startswith("M") or cat.startswith("L"):
        return True
    return False


def is_ipa_string(ipa: str) -> bool:
    """Return ``True`` when *ipa* is NFC and contains only IPA characters.

    "IPA characters" = phonetic letters (Latin + IPA-Extensions letters),
    combining diacritics, and the length/stress/tie/tone modifiers used in
    broad and narrow transcription. Whitespace, digits and ASCII punctuation
    (other than the tolerated prosodic boundaries) are rejected. An empty
    string is not a valid transcription.
    """
    if not ipa:
        return False
    if unicodedata.normalize("NFC", ipa) != ipa:
        return False
    return all(_is_ipa_char(ch) for ch in ipa)


def lexicon_path(code: str) -> Path:
    """Path to the sidecar TSV for *code* (whether or not it exists)."""
    return LEXICON_DIR / f"{code}.tsv"


def available_lexicon_codes() -> List[str]:
    """Sorted list of language codes that ship a ``{code}.tsv`` lexicon."""
    if not LEXICON_DIR.is_dir():
        return []
    return sorted(p.stem for p in LEXICON_DIR.glob("*.tsv"))


def parse_lexicon_text(text: str) -> Dict[str, str]:
    """Parse TSV *text* into a ``{word: ipa}`` map, first entry winning.

    Blank lines are skipped. Each non-blank line must be ``word<TAB>ipa``;
    the word is NFC-normalised (keys are stored as-authored, i.e. already
    lowercase in a well-formed file — see :func:`validate_lexicon_text`).
    A duplicate word keeps the FIRST occurrence (sorted files make "first"
    deterministic).
    """
    out: Dict[str, str] = {}
    for line in text.split("\n"):
        if not line or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        word = unicodedata.normalize("NFC", parts[0])
        ipa = unicodedata.normalize("NFC", parts[1])
        if word and ipa and word not in out:
            out[word] = ipa
    return out


def validate_lexicon_text(text: str) -> List[Tuple[int, str]]:
    """Validate a lexicon TSV body; return a list of ``(line_no, reason)``.

    An empty list means the file is clean. Checks, per non-blank line:

    - exactly one TAB (``word<TAB>ipa`` shape);
    - word and IPA both non-empty;
    - word is NFC and lowercase (``word == word.lower()``);
    - IPA is NFC and contains only IPA characters (:func:`is_ipa_string`);
    - the word is not a duplicate of an earlier line.

    This is the data-quality guard the shipped-TSV test runs over every
    ``data/lexicons/*.tsv``.
    """
    problems: List[Tuple[int, str]] = []
    seen: set = set()
    for i, line in enumerate(text.split("\n"), start=1):
        if not line or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != 2:
            problems.append((i, f"expected 'word<TAB>ipa', got {len(parts)} fields"))
            continue
        word, ipa = parts
        if not word or not ipa:
            problems.append((i, "empty word or IPA"))
            continue
        if unicodedata.normalize("NFC", word) != word:
            problems.append((i, f"word not NFC-normalised: {word!r}"))
        if word != word.lower():
            problems.append((i, f"word not lowercase: {word!r}"))
        if not is_ipa_string(ipa):
            problems.append((i, f"IPA not NFC / not IPA-only: {ipa!r}"))
        if word in seen:
            problems.append((i, f"duplicate word: {word!r}"))
        seen.add(word)
    return problems


@lru_cache(maxsize=None)
def get_lexicon(code: str) -> Dict[str, str]:
    """Return the ``{word: ipa}`` overlay for *code*, or ``{}`` if none ships.

    Lazily reads ``data/lexicons/{code}.tsv`` on first call for *code* and
    caches the result. Never raises for a missing file — an absent lexicon
    is the common case and yields an empty (falsy) mapping, keeping the
    engine byte-identical for that language.

    *code* must be the resolved, registered language code (e.g. ``"en-GB"``),
    exactly as :attr:`orthography2ipa.g2p.G2P.lang` holds it, so lookups line
    up with the JSON spec file of the same name.
    """
    path = lexicon_path(code)
    if not path.is_file():
        return {}
    return parse_lexicon_text(path.read_text(encoding="utf-8"))
