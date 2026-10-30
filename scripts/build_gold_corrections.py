#!/usr/bin/env python3
"""Regenerate the committed gold-correction overlays.

An OVERLAY is a small, separately committed file that repairs a defect in an
upstream gold set without touching the upstream file: one row per corrected
gold entry, recording the spelling, the reading the upstream gold shipped, the
reading the overlay substitutes, the reason, and the authority the correction
rests on. ``scripts/benchmark.py`` registers the overlaid gold as its OWN
dataset, so the original row and the corrected row both stay on the board and
the correction's effect is visible as the difference between them.

THE RULE THAT MAKES AN OVERLAY HONEST: a correction may be derived ONLY from
the orthography of the word or from a fetched citation. It may NEVER be derived
from what orthography2ipa itself outputs. A gold repaired with this project's
own answers would score beautifully and measure nothing. Nothing in this file
names an orthography2ipa module, and nothing in it may start. A test parses the
source for every way of naming one, but note what that can and cannot promise:
``main`` imports ``benchmark`` for the base gold loader, so the engine IS in
``sys.modules`` while the build runs. The derivation stays honest because
each builder takes only ``(spelling, reading)`` pairs and reads the spelling —
not because the engine is out of reach.

Two overlays:

``vox_communis`` / ``vi`` — the upstream phone tier merges two contrastive
Vietnamese tones. It writes the identical Chao tone letter ˨˨ for both *ngang*
(A1, the unmarked tone) and *huyền* (A2). Kirby (2011: 386) tabulates them as
separate categories on the minimal pair ⟨ma⟩ 'ghost' (ngang, "level") versus
⟨mà⟩ 'but, yet' (huyền, "mid falling"); the two are the classic Vietnamese
tone minimal pair, so a gold that spells them alike has lost a phonemic
contrast, not chosen a notation.

The repair is derivable from spelling alone because Vietnamese orthography
writes huyền with a COMBINING GRAVE ACCENT (U+0300) over the syllable nucleus —
à è ì ò ù ỳ and their circumflex/breve/horn variants — and writes ngang with no
tone mark at all. Which of the two merged tones a syllable carries is therefore
recoverable from the Unicode combining marks of the spelling, with no
phonological model in the loop. ``vi_tone_from_spelling`` below reads exactly
those marks.

The substituted value is ˧˩. Kirby prints tone letters rather than Chao
digits, and labels huyền "mid falling" against hỏi's "low falling"
(2011: 386), so huyền must start above hỏi's register: ˧ (mid) falling to ˩.
The upstream gold's own ngang is ˨˨ and its hỏi is ˨˩˨, so ˧˩ is distinct from
every tone-letter sequence already in the file.

    Kirby, James P. (2011). Vietnamese (Hanoi Vietnamese). Journal of the
    International Phonetic Association 41(3): 381-392.
    https://doi.org/10.1017/S0025100311000181

``ipadict`` / ``pt-BR`` — the upstream ``pt_BR.txt`` writes one primary stress
on a hyphenated word, and on many of them it puts that stress on the wrong
syllable. In enclisis it stresses the penultimate syllable of host and clitic
written as one string (*acusa-o* ``a.ku.ˈza.ʊ``), but an enclitic pronoun is
unstressed and the host keeps its own stress: Toneli (2011: 2) gives host plus
enclitic, as in *fala-se*, as one prosodic word with one primary accent.
In a compound it stresses the first element (*pós-ditadura*), but the last
element of a Portuguese compound carries the main stress: each radical keeps
its stress, "sendo o último o mais forte" (Bechara, *Moderna Gramática
Portuguesa*, p. 340, as quoted in Ciberdúvidas resposta 28042), and the main
prominence of a compound prosodic word "será sempre o elemento mais à direita"
(Toneli 2011: 2).

The repair is derivable from spelling alone. The Acordo Ortográfico 1990 puts
a written accent on exactly the words that break the default stress rule
(Bases VIII, IX, X), so the stressed syllable of each element is read off the
spelling by ``pt_stress_from_end`` and mapped onto the gold's own dotted
syllables. Only the stress mark moves; every segment is kept. A spelling that
the rule cannot map onto the gold's syllables is skipped and counted.

    Toneli, Priscila Marques (2011). O comportamento prosódico de palavras
    compostas no Português Brasileiro. I Congresso Nacional de Estudos
    Linguísticos, Vitória-ES.

    Ciberdúvidas da Língua Portuguesa, resposta 28042, "Composição por
    aglutinação e composição por justaposição, novamente".
    https://ciberduvidas.iscte-iul.pt/consultorio/perguntas/x/28042

Usage::

    PYTHONPATH=. python scripts/build_gold_corrections.py

Rewrites every file under ``orthography2ipa/data/gold/corrections/``. The build
is deterministic: rerunning it on an unchanged upstream cache reproduces the
committed bytes.
"""
import json
import os
import re
import sys
import unicodedata
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CORRECTIONS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..",
    "orthography2ipa", "data", "gold", "corrections",
)

#: The five Vietnamese tone marks, as Unicode combining characters, mapped to
#: the traditional tone names. An unmarked syllable is *ngang*. These are the
#: ONLY diacritics that carry tone: the circumflex (U+0302), breve (U+0306) and
#: horn (U+031B) of ⟨â ê ô ă ơ ư⟩ are vowel-quality marks and are ignored here.
VI_TONE_MARKS = {
    "̀": "huyen",   # grave       à
    "̉": "hoi",     # hook above  ả
    "̃": "nga",     # tilde       ã
    "́": "sac",     # acute       á
    "̣": "nang",    # dot below   ạ
}

#: Chao tone letters and the glottalisation/creak marks that ride with them,
#: as used by the VoxCommunis Vietnamese phone tier.
TONE_LETTERS = re.compile("[˥-˩̰̃ˀʼ]+")

VI_NGANG_READING = "˨˨"     # ˨˨ — what the upstream gold writes
VI_HUYEN_READING = "˧˩"     # ˧˩ — Kirby 2011:386, "mid falling"

VI_TONE_REASON = (
    "upstream phone tier writes the ngang tone letter ˨˨ on a "
    "syllable spelled with the huyen grave accent, merging two contrastive "
    "tones; replaced with the huyen tone letters ˧˩"
)
VI_TONE_AUTHORITY = (
    "Vietnamese orthography (huyen is written U+0300 COMBINING GRAVE ACCENT) "
    "+ Kirby, James P. (2011), Vietnamese (Hanoi Vietnamese), JIPA 41(3): "
    "381-392, tone table p. 386 (ngang A1 'level' ma vs huyen A2 "
    "'mid falling' mà), https://doi.org/10.1017/S0025100311000181"
)


def vi_tone_from_spelling(word: str) -> Optional[str]:
    """The tone of a Vietnamese syllable, read off its combining marks.

    Returns a name from :data:`VI_TONE_MARKS`, ``"ngang"`` for an unmarked
    syllable, or ``None`` when the spelling carries more than one tone mark —
    a multi-syllable token, where no single tone can be assigned and the row
    must be left uncorrected.

    Orthography only. No phonology, no lexicon, and above all no o2i.
    """
    marks = [VI_TONE_MARKS[c] for c in unicodedata.normalize("NFD", word)
             if c in VI_TONE_MARKS]
    if not marks:
        return "ngang"
    if len(marks) == 1:
        return marks[0]
    return None


def build_vi_tone_rows(pairs: List[Tuple[str, str]]) -> Tuple[List[Dict], Dict[str, int]]:
    """Overlay rows for the VoxCommunis Vietnamese tone merge, plus the counts
    of everything deliberately left alone.

    A row is corrected only when BOTH of these hold, and skipped and counted
    otherwise:

    * the spelling carries exactly one tone mark and it is the huyen grave;
    * the gold reading's tone-letter sequence is exactly ˨˨, i.e. it is a
      single-syllable reading that actually shows the merge.

    A grave-accented spelling whose reading is NOT ˨˨ is not evidence of the
    merge and gets no correction, whatever it is. This is the negative-result
    bucket and it is reported, never silently dropped.
    """
    rows: List[Dict] = []
    stats = {
        "corrected": 0,
        "huyen_reading_not_ngang": 0,
        "tone_undeterminable": 0,
        "not_huyen": 0,
    }
    for word, reading in pairs:
        tone = vi_tone_from_spelling(word)
        if tone is None:
            stats["tone_undeterminable"] += 1
            continue
        if tone != "huyen":
            stats["not_huyen"] += 1
            continue
        if "".join(TONE_LETTERS.findall(reading)) != VI_NGANG_READING:
            stats["huyen_reading_not_ngang"] += 1
            continue
        rows.append({
            "dataset": "vox_communis",
            "lang": "vi",
            "spelling": word,
            "original_reading": reading,
            "corrected_reading": reading.replace(
                VI_NGANG_READING, VI_HUYEN_READING),
            "reason": VI_TONE_REASON,
            "authority": VI_TONE_AUTHORITY,
        })
        stats["corrected"] += 1
    rows.sort(key=lambda r: (r["spelling"], r["original_reading"]))
    return rows, stats


#: Unstressed object pronouns that Portuguese writes after a hyphen in
#: enclisis (Acordo Ortográfico 1990, Base XVII, 1.º: amá-lo, dá-se,
#: deixa-o, partir-lhe), including the contracted forms. Each is one syllable.
PT_CLITICS = frozenset(
    "me te se vos lhe lhes o a os as lo la los las no na nos nas "
    "mo ma mos mas to ta tos tas lho lha lhos lhas".split())

#: The -lo/-la forms follow a verb whose final -r, -s or -z was assimilated,
#: and the host then ends in its tonic vowel, written á, ê or ô after a, e, o
#: (Base VIII, 1.º b and 2.º b: adorá-lo, detê-lo, compô-la). A host ending in
#: an unaccented a, e or o before one of these is misspelt.
PT_LO_CLITICS = frozenset({"lo", "la", "los", "las"})

#: Future and conditional endings that follow the clitic in mesoclisis
#: (amá-lo-ei, fá-lo-á). Those rows are left alone.
PT_MESOCLITIC_ENDINGS = frozenset(
    "ei ás á emos eis ão ia ias íamos íeis iam".split())

_PT_VOWELS = frozenset("aeiouyáéíóúâêôãõàü")
_PT_STRESS_ACCENTS = frozenset("áéíóúâêô")
_PT_TILDE = frozenset("ãõ")
_PT_LETTERS = re.compile("^[a-zçáéíóúâêôãõàü]+$")
_PT_PAROXYTONE_ENDINGS = ("a", "e", "o", "as", "es", "os", "am", "em", "ens")
_PT_OXYTONE_FINALS = frozenset("iuylrzxnm")

PT_STRESS_MARK = "ˈ"

PT_ENCLITIC_REASON = (
    "the gold puts the primary stress on the penultimate syllable of the "
    "host and clitic written as one string; an enclitic pronoun is "
    "unstressed and does not move the stress of its host, so the primary "
    "is moved to the host's stressed syllable"
)
PT_COMPOUND_REASON = (
    "the gold puts the only primary stress of a hyphenated compound on an "
    "element other than the last; the last element of a Portuguese compound "
    "carries the main stress, so the primary is moved to the stressed "
    "syllable of the last element"
)
PT_AUTHORITY_ORTHOGRAPHY = (
    "stressed syllable read from the spelling by the Acordo Ortográfico 1990 "
    "accent rules (Bases VIII, IX, X: a written acute or circumflex marks it; "
    "otherwise -a/-e/-o(s), -am, -em/-ens are paroxytone and other endings "
    "oxytone)"
)
PT_ENCLITIC_AUTHORITY = (
    PT_AUTHORITY_ORTHOGRAPHY + " + Acordo Ortográfico 1990, Base VIII, 1.º b "
    "and 2.º b (adorá-lo from adorar-lo: the host keeps its tonic vowel "
    "before the clitic) + Toneli, Priscila Marques (2011), O comportamento "
    "prosódico de palavras compostas no Português Brasileiro, I Congresso "
    "Nacional de Estudos Linguísticos, p. 2: host plus enclitic, as in "
    "fala-se, is a minimal prosodic word with one primary accent"
)
PT_COMPOUND_AUTHORITY = (
    PT_AUTHORITY_ORTHOGRAPHY + " + Bechara, Moderna Gramática Portuguesa, "
    "p. 340, quoted in Ciberdúvidas da Língua Portuguesa, resposta 28042: "
    "each radical keeps its stress, 'sendo o último o mais forte' + Toneli "
    "(2011), p. 2: in a compound prosodic word the main prominence 'será "
    "sempre o elemento mais à direita'"
)

PT_REASONS = {"enclitic": PT_ENCLITIC_REASON, "compound": PT_COMPOUND_REASON}
PT_AUTHORITIES = {"enclitic": PT_ENCLITIC_AUTHORITY,
                  "compound": PT_COMPOUND_AUTHORITY}


def _pt_hiatus_before(word: str, i: int) -> bool:
    """Whether the unaccented i/u at ``word[i]`` stays a syllable of its own
    after a vowel. Base X, 2.º writes no acute on that tonic i/u before
    ⟨nh⟩ or before an l, m, n, r, z that closes its syllable (rainha, ainda,
    juiz, ruim, Raul), so those spellings are hiatuses without a mark."""
    rest = word[i + 1:]
    if rest.startswith("nh"):
        return True
    if rest[:1] in ("l", "m", "n", "r", "z"):
        return len(rest) == 1 or rest[1] not in _PT_VOWELS
    return False


def pt_nuclei(element: str) -> List[str]:
    """The syllable nuclei of one hyphen-free Portuguese element, in order,
    read from the spelling.

    A falling diphthong (a vowel then an unaccented i or u: pai, meu, muito)
    and a nasal diphthong (ão, ãe, ãi, õe) are one nucleus. Every other pair
    of vowels is a hiatus. The u of ⟨qu gu⟩ before a vowel is silent or a
    glide and is never a nucleus.
    """
    word = unicodedata.normalize("NFC", element.lower())
    nuclei: List[str] = []
    i = 0
    while i < len(word):
        ch = word[i]
        if ch not in _PT_VOWELS:
            i += 1
            continue
        if (ch in "uü" and i > 0 and word[i - 1] in "qg"
                and i + 1 < len(word) and word[i + 1] in _PT_VOWELS):
            i += 1
            continue
        nucleus = ch
        nxt = word[i + 1] if i + 1 < len(word) else ""
        if ch in _PT_TILDE and nxt in "oei":
            nucleus += nxt
        elif (nxt in "iuy" and nxt != ch
              and not _pt_hiatus_before(word, i + 1)):
            nucleus += nxt
        nuclei.append(nucleus)
        i += len(nucleus)
    return nuclei


def pt_stress_from_end(element: str) -> Optional[int]:
    """The stressed syllable of one element, counted from the end (1 = the
    last), by the Acordo Ortográfico 1990 accent rules; ``None`` when the
    spelling does not determine it.

    A written acute or circumflex marks the stressed syllable. Without one, a
    tilde in the last syllable makes it oxytone (irmão, maçã). Otherwise a
    word ending in -a, -e, -o, -as, -es, -os, -am, -em or -ens is paroxytone,
    and a word ending in -i, -u, -l, -r, -z, -x, -n, -m (other than -am/-em)
    or in one of those plus -s is oxytone: Bases VIII and IX write an accent
    on exactly the words that break this default.
    """
    word = unicodedata.normalize("NFC", element.lower())
    if not _PT_LETTERS.match(word):
        return None
    nuclei = pt_nuclei(word)
    if not nuclei:
        return None
    accented = [k for k, n in enumerate(nuclei)
                if any(c in _PT_STRESS_ACCENTS for c in n)]
    if len(accented) > 1:
        return None
    if accented:
        return len(nuclei) - accented[0]
    if len(nuclei) == 1:
        return 1
    if any(c in _PT_TILDE for c in nuclei[-1]):
        return 1
    if word.endswith(_PT_PAROXYTONE_ENDINGS):
        return 2
    final = word[:-1] if word.endswith("s") else word
    if final[-1:] in _PT_OXYTONE_FINALS:
        return 1
    return None


def _gold_syllables(reading: str) -> Tuple[List[str], Optional[int]]:
    """The gold's own dotted syllables with the stress mark removed, and the
    index of the syllable that carried the one primary mark."""
    syllables = reading.split(".")
    marked = [k for k, s in enumerate(syllables) if PT_STRESS_MARK in s]
    if len(marked) != 1 or not syllables[marked[0]].startswith(PT_STRESS_MARK):
        return syllables, None
    return [s.replace(PT_STRESS_MARK, "") for s in syllables], marked[0]


def _classify_pt_hyphenated(word: str) -> Tuple[str, Optional[int], Optional[str]]:
    """``(kind, element index carrying the primary, skip reason)`` for one
    hyphenated spelling. ``kind`` is ``enclitic`` or ``compound``."""
    elements = word.split("-")
    if any(not e for e in elements):
        return "", None, "empty_element"
    host = max((k for k, e in enumerate(elements) if e not in PT_CLITICS),
               default=None)
    if host is None:
        return "", None, "no_host"
    if (host == len(elements) - 1 and host > 0
            and elements[host] in PT_MESOCLITIC_ENDINGS
            and elements[host - 1] in PT_CLITICS):
        return "", None, "mesoclisis"
    if host < len(elements) - 1:
        hostword = elements[host]
        if (elements[host + 1] in PT_LO_CLITICS
                and hostword[-1] in "aeorsz"):
            return "enclitic", host, "misspelling"
        return "enclitic", host, None
    return "compound", host, None


def build_pt_stress_rows(
    pairs: List[Tuple[str, str]], upstream_file: str,
) -> Tuple[List[Dict], Dict[str, int]]:
    """Overlay rows that move the one primary stress of a hyphenated
    ipa-dict pt-BR gold to the syllable the spelling stresses, plus the
    counts of everything left alone.

    Only hyphenated spellings are read. The target syllable is the host's
    stressed syllable in enclisis and the last element's stressed syllable in
    a compound, read from the spelling by :func:`pt_stress_from_end` and
    mapped onto the gold's own dotted syllables by counting from the end of
    that element, plus the nuclei of the clitics after it.

    A row is corrected only when all of these hold, and skipped and counted
    otherwise:

    * the nuclei the spelling gives the elements add up to exactly the gold's
      syllable count. The gold marks no element boundary, so the
      per-element agreement is checked through that sum;
    * the gold shows the defect the reason names: in enclisis its primary is
      on the penultimate syllable of the whole string, in a compound it is on
      an element before the last;
    * the spelling is not a misspelt -lo/-la enclisis (ajuda-lo for
      ajudá-lo) and not a mesoclisis.

    Every segment stays as it was; only the stress mark moves. The gold
    writes no secondary stress anywhere, so none is added.
    """
    rows: List[Dict] = []
    stats = {"corrected_enclitic": 0, "corrected_compound": 0,
             "already_correct": 0, "misspelling": 0, "empty_element": 0,
             "no_host": 0, "mesoclisis": 0, "gold_stress_unreadable": 0,
             "gold_stress_other_shape": 0,
             "stress_undeterminable": 0, "nucleus_count_mismatch": 0}
    for word, reading in pairs:
        if "-" not in word:
            continue
        kind, host, skip = _classify_pt_hyphenated(word)
        if skip:
            stats[skip] += 1
            continue
        syllables, gold_index = _gold_syllables(reading)
        if gold_index is None:
            stats["gold_stress_unreadable"] += 1
            continue
        elements = word.split("-")
        stress = pt_stress_from_end(elements[host])
        if stress is None:
            stats["stress_undeterminable"] += 1
            continue
        if sum(len(pt_nuclei(e)) for e in elements) != len(syllables):
            stats["nucleus_count_mismatch"] += 1
            continue
        clitic_syllables = sum(len(pt_nuclei(e)) for e in elements[host + 1:])
        target = len(syllables) - clitic_syllables - stress
        if target == gold_index:
            stats["already_correct"] += 1
            continue
        if kind == "enclitic":
            shows_defect = gold_index == len(syllables) - 2
        else:
            shows_defect = (gold_index
                            < len(syllables) - len(pt_nuclei(elements[-1])))
        if not shows_defect:
            stats["gold_stress_other_shape"] += 1
            continue
        syllables[target] = PT_STRESS_MARK + syllables[target]
        rows.append({
            "dataset": "ipadict",
            "lang": "pt-BR",
            "upstream_file": upstream_file,
            "spelling": word,
            "original_reading": reading,
            "corrected_reading": ".".join(syllables),
            "kind": kind,
            "reason": PT_REASONS[kind],
            "authority": PT_AUTHORITIES[kind],
        })
        stats[f"corrected_{kind}"] += 1
    rows.sort(key=lambda r: (r["spelling"], r["original_reading"]))
    return rows, stats


def write_overlay(name: str, rows: List[Dict]) -> str:
    os.makedirs(CORRECTIONS_DIR, exist_ok=True)
    path = os.path.join(CORRECTIONS_DIR, f"{name}.jsonl")
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    return path


def main() -> None:
    import benchmark  # the BASE gold loader only; never the o2i engine

    upstream_file = benchmark._IPADICT_FILES["pt-BR"]
    builds = [
        ("vox_communis_vi", benchmark.load_vox_communis("vi", sys.maxsize),
         build_vi_tone_rows),
        ("ipadict_pt_BR", benchmark.load_ipadict("pt-BR", sys.maxsize),
         lambda pairs: build_pt_stress_rows(pairs, upstream_file)),
    ]
    for name, pairs, build in builds:
        rows, stats = build(pairs)
        path = write_overlay(name, rows)
        print(f"{name}: read {len(pairs)} upstream pairs")
        for key, value in sorted(stats.items()):
            print(f"  {key}: {value}")
        print(f"wrote {len(rows)} rows to {os.path.relpath(path, os.getcwd())}")


if __name__ == "__main__":
    main()
