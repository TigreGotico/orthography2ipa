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

# ─── portuguese_unified ─────────────────────────────────────────────────────
#
# TigreGotico/portuguese-unified-pronunciation-lexicon merges Infopédia,
# pt.wiktionary.org and the Portal da Língua Portuguesa lexicon. Its rows carry
# four defects that the orthography or a fetched citation settles:
#
# * a primary mark on a syllable other than the one a written acute or
#   circumflex marks (Infopédia *busílis* ``buziˈliʃ``);
# * a primary mark on an unaccented word that the Acordo Ortográfico 1990
#   accent rules place elsewhere (an unaccented -ar infinitive is oxytone: the
#   Infopédia row for *malucar* reads ``mɐˈlukar``);
# * no primary mark at all (the Portal Lisbon rows lose it on a stressed vowel
#   after [j]: *paciente* ``pɐsjẽt``);
# * a reading of another headword (*tração* rows that read *seleto*, Infopédia
#   rows of a neighbouring entry), and Maputo rows that end in mis-encoded
#   text.
#
# Each overlay row is keyed on the SOURCE row, not on an o2i language tag:
# dataset, source, region, word, POS and field, plus the reading the row
# shipped. The same rows can then be applied by any consumer of the dataset.
# A ``corrected_reading`` of ``None`` drops the source row.
#
# A corrected reading only moves, adds or removes a stress mark, or drops a
# variant or a row. It never changes a segment, except where a stray symbol
# stands in for the mark (``koitádu``, ``traveˡsejru``). A mark is placed only
# where the vowel at the new stressed position is one the stressed letter can
# spell; where it is not (Lisbon *sêxtuplo* ``sɨʃtˈuplu``: a stressed [ɨ]
# cannot spell ⟨ê⟩) the row needs a segment fix that no rule here settles, and
# it is left alone.

PT_UNIFIED_DATASET = "portuguese_unified"
PT_UNIFIED_OVERLAY = "portuguese_unified_pt"

#: Vowel symbols that can be a nucleus in the dataset's readings.
PT_NUCLEI = "aɐeɛəɨioɔuʊɪæyøœɑɒʌɜɘɯäɚ"
PT_MARKS = "ˈ'"

_AO = "Acordo Ortográfico 1990 (Portal da Língua Portuguesa text)"
PT_AUTHORITY = {
    "accent": (
        _AO + ", Bases VIII, IX and XI: the acute and the circumflex are written "
        "on the stressed vowel, e.g. Base XI 1.º a 'árabe, cáustico, Cleópatra, "
        "esquálido, exército, hidráulico, líquido, míope' and 2.º a 'cânfora, "
        "cômputo, dinâmico, lâmpada'. The written ⟨{letter}⟩ is the stressed vowel"
    ),
    "oxy_r": (
        _AO + ", Base IX 2.º a and 3.º a: a paroxytone that ends in -l, -n, -r "
        "or -x takes an accent ('amável, Aníbal, dócil'; 'Almodôvar, aljôfar, "
        "âmbar'). An unaccented word with one of these endings is oxytone"
    ),
    "oxy_ao": (
        _AO + ", Base IX 2.º b: a paroxytone that ends in -ã(s), -ão(s), "
        "-ei(s), -i(s), -um, -uns or -us takes an accent ('órfão, órgão, "
        "sótão'). An unaccented word with one of these endings is oxytone"
    ),
    "paroxy": (
        _AO + ", Base IX 1.º: 'As palavras paroxítonas não são em geral "
        "acentuadas graficamente: enjoo, grave, homem, mesa'; Base VIII 1.º a "
        "and c accent an oxytone in -a, -e, -o and a multisyllable oxytone in "
        "-em, -ens ('acém, detém, harém, também'); Base XI accents every "
        "proparoxytone. An unaccented word that ends in -a, -e, -o (-s), -em or "
        "-ens is paroxytone"
    ),
}

#: Portal da Língua Portuguesa readings fetched for these corrections
#: (portaldalinguaportuguesa.org, ``action=fonetica``, exact headword match),
#: keyed on ``(word, Portal region code)``.
PT_PORTAL_QUOTES = {
    ("enfezar", "lbx"): "en·fe·zar [verbo] ẽ.fɛ.zˈaɾ",
    ("malucar", "lbx"): "ma·lu·car [verbo] mɐ.lu.kˈaɾ",
    ("unir", "lbx"): "u·nir [verbo] u.nˈiɾ",
    ("almargem", "lbx"): "al·mar·gem [nome masculino] aɫ.mˈaɾ.ʒɐ̃j",
    ("miopia", "lbx"): "mi·o·pi·a [nome feminino] mju.pˈi.ɐ",
    ("apartadamente", "lbx"): "a·par·ta·da·men·te [advérbio] ɐ.pɐɾ.tɐ.dɐ.mˈẽ.tɨ",
    ("desgraçar", "rjx"): "des·gra·çar [verbo] deʒ.gɾa.sˈaɾ",
    ("abalroa", "rjx"): "a·bal·ro·a [nome feminino] a.baw.ɦˈo.ɐ",
    ("telegrafista", "rjx"): "te·le·gra·fis·ta [nome masculino] te.le.gɾa.fˈiʃ.tɐ",
    ("delegacia", "rjx"): "de·le·ga·ci·a [nome feminino] de.le.ga.sˈi.ɐ",
    ("halo", "rjx"): "ha·lo [nome masculino] ˈa.lʊ",
    ("psicadélico", "rjx"): "psi·ca·dé·li·co [adjetivo] psi.ka.dˈɛ.li.kʊ",
    ("boticário", "rjx"): "bo·ti·cá·ri·o [nome masculino] bo.tʃi.kˈa.ɾjʊ",
    ("pseudoetimologia", "rjx"): (
        "pseu·do·e·ti·mo·lo·gi·a [nome feminino] psew.dɔ.e.tʃĩ.mo.lo.ʒˈi.ɐ"),
    ("tração", "lbx"): "tra·ção tɾɐ.sˈɐ̃w",
    ("tração", "rjx"): "tra·ção tɾa.sˈɐ̃w",
    ("tração", "spx"): "tra·ção tɾa.sˈə̃w",
    ("tração", "lda"): "tra·ção tɾa.sˈɐ̃w",
    ("tração", "mpx"): "tra·ção tra.sˈãw",
    ("tração", "dli"): "tra·ção tɾək.sˈə̃w",
    ("microfarad", "lbx"): "mi·cro·fa·rad [nome masculino] mi.kɾɔ.",
    ("microvolt", "spx"): "mi·cro·volt [nome masculino] mi.kɾo.",
}

#: Dataset region -> Portal region code, for the quote lookup. The pt-BR and
#: pt-PT Wiktionary rows are checked against the Rio and Lisbon Portal entries.
PT_PORTAL_REGION = {
    "pt-PT": "lbx", "pt-PT-x-lisboa": "lbx", "pt-BR": "rjx",
    "pt-BR-x-riodejaneiro": "rjx", "pt-BR-x-saopaulo": "spx", "pt-AO": "lda",
    "pt-MZ-x-maputo": "mpx", "pt-TL-x-dili": "dli",
}

PT_MOJIBAKE_REASON = (
    "the reading carries mis-encoded text, not a transcription; the row is "
    "dropped"
)
PT_MOJIBAKE_AUTHORITY = (
    "the reading itself: 'Ã' is not an IPA symbol. It is the first byte of a "
    "two-byte UTF-8 character such as 'ã' (C3 A3) read as Latin-1"
)
PT_MOJIBAKE_NOTE_AUTHORITY = PT_MOJIBAKE_AUTHORITY + (
    ". The reading ends in the note 'çollins-nÃ£o-tem', with 'não' read that "
    "way, and the Portal da Língua Portuguesa serves the same string, fonetica "
    "region mpx: 'a·ben·cer·ra·gem ɐ.bẽ.se.rˈa.ʒẽçollins-nÃ£o-tem'"
)
PT_IE_REASON = (
    "the reading has no primary stress mark; the stressed vowel is the e of "
    "⟨ie⟩ or ⟨ee⟩, read as [e] after the glide [j] or [w], and the mark is "
    "written before it"
)

#: Hand-checked corrections of the ``ipa_narrow`` field:
#: ``(word, region, source, original, corrected, kind, basis)``. ``corrected``
#: ``None`` drops the source row. ``basis`` is a written accent letter, a key
#: of :data:`PT_AUTHORITY`, or, for ``wrong_headword``, what the reading
#: transcribes instead. ``scripts/build_gold_corrections.py`` checks every entry
#: against the upstream file and stops on one that matches no row.
PT_UNIFIED_DECISIONS: Tuple[Tuple[str, str, str, str, Optional[str], str, str], ...] = (
    ("Blátidas", "pt-PT", "infopedia", "blaˈtidɐʃ", "ˈblatidɐʃ", "accent_contradiction", "á"),
    ("abígeo", "pt-PT", "infopedia", "ɐbiˈʒju", "ɐˈbiʒju", "accent_contradiction", "í"),
    ("acridídeo", "pt-PT", "infopedia", "ɐkridiˈdju", "ɐkriˈdidju", "accent_contradiction", "í"),
    ("amanaié", "pt-PT", "infopedia", "ɐmmɐˈnajɛ", "ɐmmɐnaˈjɛ", "accent_contradiction", "é"),
    ("amaxofóbico", "pt-PT", "infopedia", "ɐmɐˈksufɔbiku", "ɐmɐksuˈfɔbiku", "accent_contradiction", "ó"),
    ("anídrido", "pt-PT", "infopedia", "aniˈdridu", "aˈnidridu", "accent_contradiction", "í"),
    ("atlântico", "pt-PT", "infopedia+wiktionary", "ɐtlɐ̃ˈtiku", "ɐˈtlɐ̃tiku", "accent_contradiction", "â"),
    ("atlântida", "pt-PT", "infopedia", "ɐtlɐ̃ˈtidɐ", "ɐˈtlɐ̃tidɐ", "accent_contradiction", "â"),
    ("aviónica", "pt-PT", "infopedia", "ˈɐvjɔnikɐ", "ɐˈvjɔnikɐ", "accent_contradiction", "ó"),
    ("babaçuê", "pt-PT", "infopedia", "babaˈsuwe", "babasuˈwe", "accent_contradiction", "ê"),
    ("boticário", "pt-BR", "wiktionary", "boʧikaˈɾju", "boʧiˈkaɾju", "accent_contradiction", "á"),
    ("busílis", "pt-PT", "infopedia+wiktionary", "buziˈliʃ", "buˈziliʃ", "accent_contradiction", "í"),
    ("báratro", "pt-BR", "wiktionary", "baˈɾatɾu", "ˈbaɾatɾu", "accent_contradiction", "á"),
    ("clímax", "pt-AO", "portal", "klimˈaks", "klˈimaks", "accent_contradiction", "í"),
    ("clímax", "pt-BR-x-riodejaneiro", "portal", "klĩmˈaks", "klˈĩmaks", "accent_contradiction", "í"),
    ("clímax", "pt-BR-x-saopaulo", "portal", "klimˈaks", "klˈimaks", "accent_contradiction", "í"),
    ("clímax", "pt-BR-x-saopaulo", "portal", "kɽimˈaks", "kɽˈimaks", "accent_contradiction", "í"),
    ("clímax", "pt-MZ-x-maputo", "portal", "klimˈaks", "klˈimaks", "accent_contradiction", "í"),
    ("clímax", "pt-MZ-x-maputo", "portal", "klĩmˈaks", "klˈĩmaks", "accent_contradiction", "í"),
    ("clímax", "pt-PT-x-lisboa", "portal", "klimˈaks", "klˈimaks", "accent_contradiction", "í"),
    ("clímax", "pt-TL-x-dili", "portal", "klimˈaks", "klˈimaks", "accent_contradiction", "í"),
    ("daimió", "pt-PT", "infopedia", "ˈdajmjɔ", "dajˈmjɔ", "accent_contradiction", "ó"),
    ("efípio", "pt-PT", "infopedia", "ɛfiˈpju", "ɛˈfipju", "accent_contradiction", "í"),
    ("egagrópilo", "pt-PT", "infopedia", "ɛɡɐɡrɔˈpilu", "ɛɡɐˈɡrɔpilu", "accent_contradiction", "ó"),
    ("enteógeno", "pt-PT", "infopedia", "ˈẽtjɔʒənu", "ẽˈtjɔʒənu", "accent_contradiction", "ó"),
    ("estrogénico", "pt-PT", "infopedia", "iʃtrɔʒɛˈniku", "iʃtrɔˈʒɛniku", "accent_contradiction", "é"),
    ("farmacológico", "pt-PT", "wiktionary", "fɐɾ'mɐkulɔʒiku", "fɐɾmɐku'lɔʒiku", "accent_contradiction", "ó"),
    ("fitóftora", "pt-PT", "infopedia", "fitɔfˈtɔrɐ", "fiˈtɔftɔrɐ", "accent_contradiction", "ó"),
    ("flamívomo", "pt-PT", "infopedia", "flɐmiˈvumu", "flɐˈmivumu", "accent_contradiction", "í"),
    ("frângão", "pt-PT", "infopedia", "frɐ̃ˈɡɐ̃w̃", "ˈfrɐ̃ɡɐ̃w̃", "accent_contradiction", "â"),
    ("gastrícola", "pt-PT", "infopedia", "ɡɐʃtriˈkulɐ", "ɡɐʃˈtrikulɐ", "accent_contradiction", "í"),
    ("gonocórico", "pt-PT", "infopedia", "ɡɔnɔkɔˈriku", "ɡɔnɔˈkɔriku", "accent_contradiction", "ó"),
    ("heteroftálmico", "pt-PT", "infopedia", "ɛtərɔftaɫˈmiku", "ɛtərɔfˈtaɫmiku", "accent_contradiction", "á"),
    ("héctica", "pt-PT", "infopedia", "ɛˈktikɐ", "ˈɛktikɐ", "accent_contradiction", "é"),
    ("imodéstia", "pt-PT", "infopedia", "imudɛʃˈtjɐ", "imuˈdɛʃtjɐ", "accent_contradiction", "é"),
    ("indochinês", "pt-PT", "infopedia", "ĩdɔˈʃineʃ", "ĩdɔʃiˈneʃ", "accent_contradiction", "ê"),
    ("irrelevância", "pt-PT", "infopedia", "iʀələvɐ̃ˈsjɐ", "iʀələˈvɐ̃sjɐ", "accent_contradiction", "â"),
    ("judô", "pt-PT", "infopedia", "ˈʒudo", "ʒuˈdo", "accent_contradiction", "ô"),
    ("locustídeo", "pt-PT", "infopedia", "lukuʃtiˈdju", "lukuʃˈtidju", "accent_contradiction", "í"),
    ("lupuié", "pt-PT", "infopedia", "luˈpujɛ", "lupuˈjɛ", "accent_contradiction", "é"),
    ("lâmpão", "pt-PT", "infopedia", "lɐ̃ˈpɐ̃w̃", "ˈlɐ̃pɐ̃w̃", "accent_contradiction", "â"),
    ("macrolíngua", "pt", "wiktionary", "ˈmakrolĩɡwa", "makroˈlĩɡwa", "accent_contradiction", "í"),
    ("macrósporo", "pt-PT", "infopedia", "mɐkrɔʃˈpuru", "mɐˈkrɔʃpuru", "accent_contradiction", "ó"),
    ("melífluo", "pt-PT", "infopedia", "məliˈflwu", "məˈliflwu", "accent_contradiction", "í"),
    ("melífluo", "pt-PT", "wiktionary", "mɨliˈflwu", "mɨˈliflwu", "accent_contradiction", "í"),
    ("monóxeno", "pt-PT", "infopedia", "mɔnɔˈksənu", "mɔˈnɔksənu", "accent_contradiction", "ó"),
    ("ofídio", "pt-PT", "infopedia", "ɔfiˈdju,uˈfidju", "ɔˈfidju,uˈfidju", "accent_contradiction", "í"),
    ("pagauê", "pt-PT", "infopedia", "paˈɡawe", "paɡaˈwe", "accent_contradiction", "ê"),
    ("precariíssimo", "pt-BR", "wiktionary", "pɾe'kaɾjisɪmu", "pɾekaɾ'jisɪmu", "accent_contradiction", "í"),
    ("profícuo", "pt-PT", "infopedia+wiktionary", "prufiˈkwu", "pruˈfikwu", "accent_contradiction", "í"),
    ("pêntodo", "pt-PT", "infopedia", "pẽˈtudu", "ˈpẽtudu", "accent_contradiction", "ê"),
    ("raticídio", "pt-PT", "infopedia", "ʀɐtisiˈdju", "ʀɐtiˈsidju", "accent_contradiction", "í"),
    ("subsêxtuplo", "pt-AO", "portal", "subseʃtˈuplʊ", "subsˈeʃtuplʊ", "accent_contradiction", "ê"),
    ("subsêxtuplo", "pt-BR-x-riodejaneiro", "portal", "subseʃtˈuplʊ", "subsˈeʃtuplʊ", "accent_contradiction", "ê"),
    ("subsêxtuplo", "pt-BR-x-riodejaneiro", "portal", "sʊbseʃtˈuplʊ", "sʊbsˈeʃtuplʊ", "accent_contradiction", "ê"),
    ("subsêxtuplo", "pt-BR-x-saopaulo", "portal", "subsestˈuplʊ", "subsˈestuplʊ", "accent_contradiction", "ê"),
    ("subsêxtuplo", "pt-BR-x-saopaulo", "portal", "subsestˈupɽʊ", "subsˈestupɽʊ", "accent_contradiction", "ê"),
    ("subsêxtuplo", "pt-MZ-x-maputo", "portal", "subsɛʃtˈuplu", "subsˈɛʃtuplu", "accent_contradiction", "ê"),
    ("subsêxtuplo", "pt-MZ-x-maputo", "portal", "sʊbsɛʃθˈuplʊ", "sʊbsˈɛʃθuplʊ", "accent_contradiction", "ê"),
    ("sudorífico", "pt-PT", "infopedia", "suduriˈfiku", "suduˈrifiku", "accent_contradiction", "í"),
    ("sânscrito", "pt-AO", "portal", "sɐ̃ʃkɾˈitʊ", "sˈɐ̃ʃkɾitʊ", "accent_contradiction", "â"),
    ("sânscrito", "pt-BR-x-riodejaneiro", "portal", "sɐ̃ʃkɾˈitʊ", "sˈɐ̃ʃkɾitʊ", "accent_contradiction", "â"),
    ("sânscrito", "pt-BR-x-saopaulo", "portal", "sə̃skɽˈitʊ", "sˈə̃skɽitʊ", "accent_contradiction", "â"),
    ("sânscrito", "pt-BR-x-saopaulo", "portal", "sə̃skɾˈitʊ", "sˈə̃skɾitʊ", "accent_contradiction", "â"),
    ("sânscrito", "pt-MZ-x-maputo", "portal", "saʃkrˈitʰʊ", "sˈaʃkritʰʊ", "accent_contradiction", "â"),
    ("sânscrito", "pt-MZ-x-maputo", "portal", "sãʃkrˈitu", "sˈãʃkritu", "accent_contradiction", "â"),
    ("sânscrito", "pt-PT-x-lisboa", "portal", "sɐ̃ʃkɾˈitu", "sˈɐ̃ʃkɾitu", "accent_contradiction", "â"),
    ("sânscrito", "pt-TL-x-dili", "portal", "sãʃkɾˈitʊ", "sˈãʃkɾitʊ", "accent_contradiction", "â"),
    ("sêxtuplo", "pt-AO", "portal", "seʃtˈuplʊ", "sˈeʃtuplʊ", "accent_contradiction", "ê"),
    ("sêxtuplo", "pt-BR-x-riodejaneiro", "portal", "seʃtˈuplʊ", "sˈeʃtuplʊ", "accent_contradiction", "ê"),
    ("sêxtuplo", "pt-BR-x-saopaulo", "portal", "sestˈuplʊ", "sˈestuplʊ", "accent_contradiction", "ê"),
    ("sêxtuplo", "pt-BR-x-saopaulo", "portal", "sestˈupɽʊ", "sˈestupɽʊ", "accent_contradiction", "ê"),
    ("sêxtuplo", "pt-MZ-x-maputo", "portal", "sɛʃtˈuplu", "sˈɛʃtuplu", "accent_contradiction", "ê"),
    ("sêxtuplo", "pt-MZ-x-maputo", "portal", "sɛʃθˈuplʊ", "sˈɛʃθuplʊ", "accent_contradiction", "ê"),
    ("táurida", "pt-PT", "infopedia", "tawˈridɐ", "ˈtawridɐ", "accent_contradiction", "á"),
    ("vagínula", "pt-PT", "infopedia", "vɐʒiˈnulɐ", "vɐˈʒinulɐ", "accent_contradiction", "í"),
    ("álefe", "pt-PT", "infopedia", "aˈlɛf", "ˈalɛf", "accent_contradiction", "á"),
    ("álefe", "pt-PT", "infopedia", "aˈlɛfə", "ˈalɛfə", "accent_contradiction", "á"),
    ("ógea", "pt-PT", "infopedia", "ɔˈʒjɐ", "ˈɔʒjɐ", "accent_contradiction", "ó"),
    ("Albertina", "pt-BR", "wiktionary", "awbertʃinɐ", "awberˈtʃinɐ", "missing_mark", "paroxy"),
    ("Ari", "pt-BR", "wiktionary", "aɾi", "aˈɾi", "missing_mark", "oxy_ao"),
    ("Ari", "pt-PT", "wiktionary", "ɐɾi", "ɐˈɾi", "missing_mark", "oxy_ao"),
    ("Cirilo", "pt-BR", "wiktionary", "siɾilu", "siˈɾilu", "missing_mark", "paroxy"),
    ("Ciríaca", "pt-BR", "wiktionary", "siɾiakɐ", "siˈɾiakɐ", "missing_mark", "í"),
    ("Geni", "pt-BR", "wiktionary", "ʒeni", "ʒeˈni", "missing_mark", "oxy_ao"),
    ("Itacir", "pt-BR", "wiktionary", "itasiʁ", "itaˈsiʁ", "missing_mark", "oxy_r"),
    ("Olavo", "pt-BR", "wiktionary", "olavu", "oˈlavu", "missing_mark", "paroxy"),
    ("Onofre", "pt-BR", "wiktionary", "onɔfɾi", "oˈnɔfɾi", "missing_mark", "paroxy"),
    ("Onofre", "pt-PT", "wiktionary", "ɔnɔfɾɨ", "ɔˈnɔfɾɨ", "missing_mark", "paroxy"),
    ("Rafa", "pt-BR", "wiktionary", "ʀafɐ", "ˈʀafɐ", "missing_mark", "paroxy"),
    ("reexperiência", "pt-PT-x-lisboa", "portal", "ʀɨiʃpɨɾjẽsjɐ", "ʀɨiʃpɨɾjˈẽsjɐ", "missing_mark", "ê"),
    ("circum-ambiente", "pt-PT-x-lisboa", "portal", "siɾkũɐ̃bjẽt", "siɾkũɐ̃bjˈẽt", "missing_mark", "paroxy"),
    ("circum-ambiente", "pt-PT-x-lisboa", "portal", "siɾkũɐ̃bjẽtɨ", "siɾkũɐ̃bjˈẽtɨ", "missing_mark", "paroxy"),
    ("pré-consciente", "pt-PT-x-lisboa", "portal", "pɾɛkõʃsjẽt", "pɾɛkõʃsjˈẽt", "missing_mark", "paroxy"),
    ("pré-consciente", "pt-PT-x-lisboa", "portal", "pɾɛkõʃsjẽtɨ", "pɾɛkõʃsjˈẽtɨ", "missing_mark", "paroxy"),
    ("semi-inconsciente", "pt-PT-x-lisboa", "portal", "sɨmɨĩkõʃsjẽt", "sɨmɨĩkõʃsjˈẽt", "missing_mark", "paroxy"),
    ("semi-inconsciente", "pt-PT-x-lisboa", "portal", "sɨmɨĩkõʃsjẽtɨ", "sɨmɨĩkõʃsjˈẽtɨ", "missing_mark", "paroxy"),
    ("Violeta", "pt-BR", "wiktionary", "vjuletɐ", "vjuˈletɐ", "missing_mark", "paroxy"),
    ("abada", "pt-PT", "infopedia", "ɐbadɐ", "ɐˈbadɐ", "missing_mark", "paroxy"),
    ("abecásio", "pt-PT", "infopedia", "abekazju", "abeˈkazju", "missing_mark", "á"),
    ("acontraltado", "pt-PT", "infopedia", "ɐkõtrɐɫtadu", "ɐkõtrɐɫˈtadu", "missing_mark", "paroxy"),
    ("acá", "pt-PT", "infopedia", "ɐka", "ɐˈka", "missing_mark", "á"),
    ("aftoso", "pt-BR-x-riodejaneiro", "portal", "afətozʊ", "afətˈozʊ", "missing_mark", "paroxy"),
    ("aftoso", "pt-BR-x-saopaulo", "portal", "afətozʊ", "afətˈozʊ", "missing_mark", "paroxy"),
    ("alimentar", "pt-BR", "wiktionary", "aˌlimẽtaχ", "aˌlimẽˈtaχ", "missing_mark", "oxy_r"),
    ("ana", "pt-PT", "infopedia", "ɐnɐ", "ˈɐnɐ", "missing_mark", "paroxy"),
    ("antagonista", "pt-BR", "wiktionary", "ɐ̃tagoniʃtɐ", "ɐ̃tagoˈniʃtɐ", "missing_mark", "paroxy"),
    ("antevieiro", "pt-PT", "infopedia", "ɐ̃təvjɐjru", "ɐ̃təˈvjɐjru", "missing_mark", "paroxy"),
    ("antidiftérico", "pt-BR-x-riodejaneiro", "portal", "ɐ̃tʃidʒifitɛrikʊ", "ɐ̃tʃidʒifitˈɛrikʊ", "missing_mark", "é"),
    ("antidiftérico", "pt-BR-x-saopaulo", "portal", "ə̃tidifitɛrikʊ", "ə̃tidifitˈɛrikʊ", "missing_mark", "é"),
    ("antidiftérico", "pt-BR-x-saopaulo", "portal", "ə̃tʃidʒifitɛrikʊ", "ə̃tʃidʒifitˈɛrikʊ", "missing_mark", "é"),
    ("avintense", "pt-PT", "infopedia", "ɐvĩtẽs", "ɐvĩˈtẽs", "missing_mark", "paroxy"),
    ("avintense", "pt-PT", "infopedia", "ɐvĩtẽsə", "ɐvĩˈtẽsə", "missing_mark", "paroxy"),
    ("azar", "pt-BR", "wiktionary", "ɐzaɾ", "ɐˈzaɾ", "missing_mark", "oxy_r"),
    ("banza", "pt-BR", "wiktionary", "bɐ̃zɐ", "ˈbɐ̃zɐ", "missing_mark", "paroxy"),
    ("bime", "pt-AO", "portal", "bimɨ", "bˈimɨ", "missing_mark", "paroxy"),
    ("bime", "pt-BR-x-riodejaneiro", "portal", "bimɪ", "bˈimɪ", "missing_mark", "paroxy"),
    ("bime", "pt-BR-x-saopaulo", "portal", "bimi", "bˈimi", "missing_mark", "paroxy"),
    ("bime", "pt-MZ-x-maputo", "portal", "bimɨ", "bˈimɨ", "missing_mark", "paroxy"),
    ("bime", "pt-PT-x-lisboa", "portal", "bimɨ", "bˈimɨ", "missing_mark", "paroxy"),
    ("bime", "pt-TL-x-dili", "portal", "bimɨ", "bˈimɨ", "missing_mark", "paroxy"),
    ("bora", "pt-PT", "infopedia", "bɔrɐ", "ˈbɔrɐ", "missing_mark", "paroxy"),
    ("breque", "pt-PT", "infopedia", "brɛk", "ˈbrɛk", "missing_mark", "paroxy"),
    ("breque", "pt-PT", "infopedia", "brɛkə", "ˈbrɛkə", "missing_mark", "paroxy"),
    ("bunda", "pt-BR", "wiktionary", "bũw̃dɐ", "ˈbũw̃dɐ", "missing_mark", "paroxy"),
    ("bênção", "pt-BR", "wiktionary", "bẽsɐ̃w̃", "ˈbẽsɐ̃w̃", "missing_mark", "ê"),
    ("catacumba", "pt-BR", "wiktionary", "katakũba", "kataˈkũba", "missing_mark", "paroxy"),
    ("cocorote", "pt", "wiktionary", "kokoɾɔti", "kokoˈɾɔti", "missing_mark", "paroxy"),
    ("coitado", "pt-PT", "wiktionary", "koitádu", "koiˈtadu", "missing_mark", "paroxy"),
    ("competição", "pt-BR", "wiktionary", "kõpeʧisɐ̃w", "kõpeʧiˈsɐ̃w", "missing_mark", "oxy_ao"),
    ("câmbio", "pt-PT", "wiktionary", "kɐ̃bju", "ˈkɐ̃bju", "missing_mark", "â"),
    ("dicotomia", "pt-BR", "wiktionary", "dʒikotomia", "dʒikotoˈmia", "missing_mark", "paroxy"),
    ("dormitório", "pt-BR", "wiktionary", "doɾmitɔɾiu", "doɾmiˈtɔɾiu", "missing_mark", "ó"),
    ("elfo", "pt", "wiktionary", "ewfʊ", "ˈewfʊ", "missing_mark", "paroxy"),
    ("encravo", "pt", "wiktionary", "ẽkɾavʊ", "ẽˈkɾavʊ", "missing_mark", "paroxy"),
    ("excrementoso", "pt-PT", "infopedia", "ɐjʃkrəmẽˈtozu,iʃkrəmẽtozu", "ɐjʃkrəmẽˈtozu,iʃkrəmẽˈtozu", "missing_mark", "paroxy"),
    ("excrementoso", "pt-PT", "infopedia", "ɐjʃkrəmẽˈtozu,ʃkrəmẽtozu", "ɐjʃkrəmẽˈtozu,ʃkrəmẽˈtozu", "missing_mark", "paroxy"),
    ("extrapor", "pt-AO", "portal", "ɨʃtɾapoɾ", "ɨʃtɾapˈoɾ", "missing_mark", "oxy_r"),
    ("extrapor", "pt-BR-x-riodejaneiro", "portal", "eʃtɾapoɾ", "eʃtɾapˈoɾ", "missing_mark", "oxy_r"),
    ("extrapor", "pt-BR-x-saopaulo", "portal", "estɽapo", "estɽapˈo", "missing_mark", "oxy_r"),
    ("extrapor", "pt-BR-x-saopaulo", "portal", "estɾapoɾ", "estɾapˈoɾ", "missing_mark", "oxy_r"),
    ("extrapor", "pt-MZ-x-maputo", "portal", "eʃtrɐpoɾ", "eʃtrɐpˈoɾ", "missing_mark", "oxy_r"),
    ("extrapor", "pt-MZ-x-maputo", "portal", "ɛʃθrɐpoɾ", "ɛʃθrɐpˈoɾ", "missing_mark", "oxy_r"),
    ("extrapor", "pt-TL-x-dili", "portal", "ʃtɾapoɾ", "ʃtɾapˈoɾ", "missing_mark", "oxy_r"),
    ("faroense", "pt-PT", "infopedia", "fɐrwẽs", "fɐˈrwẽs", "missing_mark", "paroxy"),
    ("faroense", "pt-PT", "infopedia", "fɐrwẽsə", "fɐˈrwẽsə", "missing_mark", "paroxy"),
    ("filode", "pt-AO", "portal", "filɔdɨ", "filˈɔdɨ", "missing_mark", "paroxy"),
    ("filode", "pt-BR-x-riodejaneiro", "portal", "filodʒɪ", "filˈodʒɪ", "missing_mark", "paroxy"),
    ("filode", "pt-BR-x-saopaulo", "portal", "filodi", "filˈodi", "missing_mark", "paroxy"),
    ("filode", "pt-BR-x-saopaulo", "portal", "filodʒi", "filˈodʒi", "missing_mark", "paroxy"),
    ("filode", "pt-MZ-x-maputo", "portal", "filɔdɨ", "filˈɔdɨ", "missing_mark", "paroxy"),
    ("filode", "pt-PT-x-lisboa", "portal", "filɔdɨ", "filˈɔdɨ", "missing_mark", "paroxy"),
    ("filode", "pt-TL-x-dili", "portal", "filɔdɨ", "filˈɔdɨ", "missing_mark", "paroxy"),
    ("galveense", "pt-PT", "infopedia", "ɡaɫvjẽs", "ɡaɫˈvjẽs", "missing_mark", "paroxy"),
    ("galveense", "pt-PT", "infopedia", "ɡaɫvjẽsə", "ɡaɫˈvjẽsə", "missing_mark", "paroxy"),
    ("iatismo", "pt-BR", "wiktionary", "jat͡ʃizmʊ", "jaˈt͡ʃizmʊ", "missing_mark", "paroxy"),
    ("inadimplência", "pt-BR", "wiktionary", "ɪnɐdĩplẽⁿsjɐ", "ɪnɐdĩˈplẽⁿsjɐ", "missing_mark", "ê"),
    ("indenização", "pt-BR", "wiktionary", "ĩjdenizasãw", "ĩjdenizaˈsãw", "missing_mark", "oxy_ao"),
    ("indo", "pt-AO", "portal", "ĩdʊ", "ˈĩdʊ", "missing_mark", "paroxy"),
    ("indo", "pt-BR-x-riodejaneiro", "portal", "ĩdʊ", "ˈĩdʊ", "missing_mark", "paroxy"),
    ("indo", "pt-BR-x-saopaulo", "portal", "ĩdʊ", "ˈĩdʊ", "missing_mark", "paroxy"),
    ("indo", "pt-MZ-x-maputo", "portal", "ĩdu", "ˈĩdu", "missing_mark", "paroxy"),
    ("indo", "pt-MZ-x-maputo", "portal", "ĩdʊ", "ˈĩdʊ", "missing_mark", "paroxy"),
    ("indo", "pt-PT-x-lisboa", "portal", "ĩdu", "ˈĩdu", "missing_mark", "paroxy"),
    ("indo", "pt-TL-x-dili", "portal", "ĩdʊ", "ˈĩdʊ", "missing_mark", "paroxy"),
    ("iídiche", "pt-BR", "wiktionary", "jidʒiʃe", "ˈjidʒiʃe", "missing_mark", "í"),
    ("jequitibá", "pt-BR", "wiktionary", "ʒekitʃiba", "ʒekitʃiˈba", "missing_mark", "á"),
    ("liana", "pt", "wiktionary", "liɐ̃nɐ", "liˈɐ̃nɐ", "missing_mark", "paroxy"),
    ("manquitolar", "pt-PT", "infopedia", "mɐ̃kitɔlar", "mɐ̃kitɔˈlar", "missing_mark", "oxy_r"),
    ("maxite", "pt-AO", "portal", "maksitɨ", "maksˈitɨ", "missing_mark", "paroxy"),
    ("maxite", "pt-BR-x-riodejaneiro", "portal", "maksitʃɪ", "maksˈitʃɪ", "missing_mark", "paroxy"),
    ("maxite", "pt-BR-x-saopaulo", "portal", "makisiti", "makisˈiti", "missing_mark", "paroxy"),
    ("maxite", "pt-BR-x-saopaulo", "portal", "makisitʃi", "makisˈitʃi", "missing_mark", "paroxy"),
    ("maxite", "pt-MZ-x-maputo", "portal", "maksitɨ", "maksˈitɨ", "missing_mark", "paroxy"),
    ("maxite", "pt-PT-x-lisboa", "portal", "mɐksitɨ", "mɐksˈitɨ", "missing_mark", "paroxy"),
    ("maxite", "pt-TL-x-dili", "portal", "məksitɨ", "məksˈitɨ", "missing_mark", "paroxy"),
    ("moucarrice", "pt-PT", "infopedia", "mokɐʀis", "mokɐˈʀis", "missing_mark", "paroxy"),
    ("moucarrice", "pt-PT", "infopedia", "mowkɐʀisə", "mowkɐˈʀisə", "missing_mark", "paroxy"),
    ("oba", "pt-AO", "portal", "ɔbɐ", "ˈɔbɐ", "missing_mark", "paroxy"),
    ("oba", "pt-BR-x-riodejaneiro", "portal", "obɐ", "ˈobɐ", "missing_mark", "paroxy"),
    ("oba", "pt-BR-x-saopaulo", "portal", "obə", "ˈobə", "missing_mark", "paroxy"),
    ("oba", "pt-MZ-x-maputo", "portal", "ɔbɐ", "ˈɔbɐ", "missing_mark", "paroxy"),
    ("oba", "pt-PT-x-lisboa", "portal", "ɔbɐ", "ˈɔbɐ", "missing_mark", "paroxy"),
    ("oba", "pt-TL-x-dili", "portal", "ɔbə", "ˈɔbə", "missing_mark", "paroxy"),
    ("oftálmica", "pt-BR-x-riodejaneiro", "portal", "ofətaɫmikɐ", "ofətˈaɫmikɐ", "missing_mark", "á"),
    ("oftálmica", "pt-BR-x-saopaulo", "portal", "ofətaɫmikə", "ofətˈaɫmikə", "missing_mark", "á"),
    ("oftálmico", "pt-BR-x-riodejaneiro", "portal", "ofətaɫmikʊ", "ofətˈaɫmikʊ", "missing_mark", "á"),
    ("oftálmico", "pt-BR-x-saopaulo", "portal", "ofətaɫmikʊ", "ofətˈaɫmikʊ", "missing_mark", "á"),
    ("parafusar", "pt", "wiktionary", "paɾafuzaɾ", "paɾafuˈzaɾ", "missing_mark", "oxy_r"),
    ("parecerista", "pt-BR", "wiktionary", "paɾeseɾistɐ", "paɾeseˈɾistɐ", "missing_mark", "paroxy"),
    ("poldra", "pt-PT", "infopedia", "poɫdrɐ", "ˈpoɫdrɐ", "missing_mark", "paroxy"),
    ("reda", "pt-AO", "portal", "χedɐ", "χˈedɐ", "missing_mark", "paroxy"),
    ("reda", "pt-BR-x-riodejaneiro", "portal", "ɦedɐ", "ɦˈedɐ", "missing_mark", "paroxy"),
    ("reda", "pt-BR-x-saopaulo", "portal", "xedə", "xˈedə", "missing_mark", "paroxy"),
    ("reda", "pt-BR-x-saopaulo", "portal", "ʁedə", "ʁˈedə", "missing_mark", "paroxy"),
    ("reda", "pt-MZ-x-maputo", "portal", "redɐ", "rˈedɐ", "missing_mark", "paroxy"),
    ("sanduicheria", "pt-BR", "wiktionary", "sɐ̃ɴduiʃeɾiɐ", "sɐ̃ɴduiʃeˈɾiɐ", "missing_mark", "paroxy"),
    ("semisse", "pt-AO", "portal", "semisɨ", "semˈisɨ", "missing_mark", "paroxy"),
    ("semisse", "pt-BR-x-riodejaneiro", "portal", "sẽmisɪ", "sẽmˈisɪ", "missing_mark", "paroxy"),
    ("semisse", "pt-BR-x-saopaulo", "portal", "semisi", "semˈisi", "missing_mark", "paroxy"),
    ("semisse", "pt-MZ-x-maputo", "portal", "semisɨ", "semˈisɨ", "missing_mark", "paroxy"),
    ("semisse", "pt-MZ-x-maputo", "portal", "sẽmisɨ", "sẽmˈisɨ", "missing_mark", "paroxy"),
    ("semisse", "pt-PT-x-lisboa", "portal", "sɨmisɨ", "sɨmˈisɨ", "missing_mark", "paroxy"),
    ("semisse", "pt-TL-x-dili", "portal", "sɨmisɨ", "sɨmˈisɨ", "missing_mark", "paroxy"),
    ("superpor", "pt-AO", "portal", "supɛrpoɾ", "supɛrpˈoɾ", "missing_mark", "oxy_r"),
    ("superpor", "pt-BR-x-riodejaneiro", "portal", "superpoɾ", "superpˈoɾ", "missing_mark", "oxy_r"),
    ("superpor", "pt-BR-x-riodejaneiro", "portal", "sʊperpoɾ", "sʊperpˈoɾ", "missing_mark", "oxy_r"),
    ("superpor", "pt-BR-x-saopaulo", "portal", "superpo", "superpˈo", "missing_mark", "oxy_r"),
    ("superpor", "pt-BR-x-saopaulo", "portal", "superpoɾ", "superpˈoɾ", "missing_mark", "oxy_r"),
    ("superpor", "pt-MZ-x-maputo", "portal", "supɛrpoɾ", "supɛrpˈoɾ", "missing_mark", "oxy_r"),
    ("superpor", "pt-MZ-x-maputo", "portal", "sʊpɛrpoɾ", "sʊpɛrpˈoɾ", "missing_mark", "oxy_r"),
    ("superpor", "pt-TL-x-dili", "portal", "supɛrpoɾ", "supɛrpˈoɾ", "missing_mark", "oxy_r"),
    ("texugueira", "pt", "wiktionary", "teʃugeɾa", "teʃuˈgeɾa", "missing_mark", "paroxy"),
    ("travesseiro", "pt-BR", "wiktionary", "traveˡsejru", "traveˈsejru", "missing_mark", "paroxy"),
    ("tágico", "pt-PT", "infopedia", "taʒiku", "ˈtaʒiku", "missing_mark", "á"),
    ("vexilologia", "pt-BR", "wiktionary", "veksiloloʒiɐ", "veksiloloˈʒiɐ", "missing_mark", "paroxy"),
    ("íbis", "pt-BR", "wiktionary", "ibiʃ", "ˈibiʃ", "missing_mark", "í"),
    ("abalroa", "pt-BR", "wiktionary", "abawxoˈa", "abawˈxoa", "unaccented_stress", "paroxy"),
    ("sagui", "pt-AO", "portal", "sˈagwi", "sagwˈi", "unaccented_stress", "oxy_ao"),
    ("sagui", "pt-BR-x-riodejaneiro", "portal", "sˈagwɪ", "sagwˈɪ", "unaccented_stress", "oxy_ao"),
    ("sagui", "pt-BR-x-saopaulo", "portal", "sˈagwi", "sagwˈi", "unaccented_stress", "oxy_ao"),
    ("sagui", "pt-MZ-x-maputo", "portal", "sˈagwi", "sagwˈi", "unaccented_stress", "oxy_ao"),
    ("sagui", "pt-PT-x-lisboa", "portal", "sˈagwi", "sagwˈi", "unaccented_stress", "oxy_ao"),
    ("sagui", "pt-TL-x-dili", "portal", "sˈagwi", "sagwˈi", "unaccented_stress", "oxy_ao"),
    ("almargem", "pt-PT", "infopedia", "aɫmarˈʒɐ̃j̃", "aɫˈmarʒɐ̃j̃", "unaccented_stress", "paroxy"),
    ("arrinconar", "pt-PT", "infopedia", "ɐʀĩˈkunar", "ɐʀĩkuˈnar", "unaccented_stress", "oxy_r"),
    ("açougagem", "pt-PT", "infopedia", "ɐsowɡaˈʒɐ̃j̃", "ɐsowˈɡaʒɐ̃j̃", "unaccented_stress", "paroxy"),
    ("açougagem", "pt-PT", "infopedia", "ɐsoɡaˈʒɐ̃j̃", "ɐsoˈɡaʒɐ̃j̃", "unaccented_stress", "paroxy"),
    ("desgraçar", "pt-BR", "wiktionary", "deʒˈgɾasax", "deʒgɾaˈsax", "unaccented_stress", "oxy_r"),
    ("enfezar", "pt-PT", "infopedia", "ẽˈfɛzar", "ẽfɛˈzar", "unaccented_stress", "oxy_r"),
    ("enfezar", "pt-PT", "wiktionary", "ẽˈfɛzaɾ", "ẽfɛˈzaɾ", "unaccented_stress", "oxy_r"),
    ("espajegar", "pt-PT", "infopedia", "iʃpɐˈʒəɡar", "iʃpɐʒəˈɡar", "unaccented_stress", "oxy_r"),
    ("espajegar", "pt-PT", "infopedia", "ʃpɐˈʒəɡar", "ʃpɐʒəˈɡar", "unaccented_stress", "oxy_r"),
    ("fogagem", "pt-PT", "infopedia", "fuɡaˈʒɐ̃j̃", "fuˈɡaʒɐ̃j̃", "unaccented_stress", "paroxy"),
    ("malucar", "pt-PT", "infopedia", "mɐˈlukar", "mɐluˈkar", "unaccented_stress", "oxy_r"),
    ("marrafão", "pt-PT", "infopedia", "mɐˈʀɐfɐ̃w̃", "mɐʀɐˈfɐ̃w̃", "unaccented_stress", "oxy_ao"),
    ("minerval", "pt-PT", "infopedia", "miˈnərvaɫ", "minərˈvaɫ", "unaccented_stress", "oxy_r"),
    ("miopia", "pt-PT", "wiktionary", "ˈmjupiɐ", "mjuˈpiɐ", "unaccented_stress", "paroxy"),
    ("pseudoetimologia", "pt-BR", "wiktionary", "ˌpsewdoˌɛt͡ʃiˌmɔˈlɔʒiɐ", "ˌpsewdoˌɛt͡ʃiˌmɔlɔˈʒiɐ", "unaccented_stress", "paroxy"),
    ("telegrafista", "pt-BR", "wiktionary", "ˌtɛˈlɛɡɾafistɐ", "ˌtɛlɛɡɾaˈfistɐ", "unaccented_stress", "paroxy"),
    ("unir", "pt-PT", "wiktionary", "ˈuniɾ", "uˈniɾ", "unaccented_stress", "oxy_r"),
    ("abstrusamente", "pt-PT", "infopedia", "ɐbʃtruzɐ", None, "wrong_headword", "abstrusa: the reading stops before -mente"),
    ("acometar", "pt-PT", "infopedia", "kuˈmetɐ", None, "wrong_headword", "cometa: the reading has no initial a- and no final -r"),
    ("acridídeos", "pt-PT", "infopedia", "ɐkridiˈdju", None, "wrong_headword", "the singular acridídeo: no reading of the final -s"),
    ("adelgado", "pt-PT", "infopedia", "ɐdɛɫɡɐˈdar", None, "wrong_headword", "adelgadar: the reading ends in -ar, the word in -o"),
    ("algemamento", "pt-PT", "infopedia", "aɫʒəˈmaʒɐ̃j̃", None, "wrong_headword", "a word in -gem: the reading ends in -ʒɐ̃j̃, the word in -mento"),
    ("amanaiés", "pt-PT", "infopedia", "ɐmmɐˈnajɛ", None, "wrong_headword", "the singular amanaié: no reading of the final -s"),
    ("anarrópico", "pt-PT", "infopedia", "ɐnɐʀuˈpiɐ", None, "wrong_headword", "anarropia: the reading ends in -ia, the word in -ico"),
    ("apartadamente", "pt-PT", "infopedia", "ɐpɐrˈtadɐ", None, "wrong_headword", "apartada: the reading stops before -mente"),
    ("artrológico", "pt-PT", "infopedia", "ɐrtruluˈʒiɐ", None, "wrong_headword", "artrologia: the reading ends in -ia, the word in -ico"),
    ("avela", "pt-PT", "infopedia", "ɐvəˈlar", None, "wrong_headword", "avelar: the reading ends in -ar, the word in -a"),
    ("bioplastia", "pt-PT", "infopedia", "bju", None, "wrong_headword", "the reading [bju] covers only bio-"),
    ("brasileiro", "pt-BR", "wiktionary", "l", None, "wrong_headword", "the reading is the single segment [l]"),
    ("dataria", "pt-PT", "infopedia", "dɐˈtar", None, "wrong_headword", "datar: the reading ends in -ar, the word in -ia"),
    ("delegacia", "pt-BR", "wiktionary", "deleˈgadu", None, "wrong_headword", "delegado: the reading ends in -du, the word in -cia"),
    ("emetólogo", "pt-PT", "infopedia", "ɛmɛtuluˈʒiʃtɐ", None, "wrong_headword", "emetologista: the reading ends in -ista, the word in -ogo"),
    ("esculhambo", "pt-PT", "infopedia", "iʃkuʎɐ̃bɐˈsɐ̃w̃", None, "wrong_headword", "esculhambação: the reading ends in -ção, the word in -o"),
    ("esculhambo", "pt-PT", "infopedia", "ʃkuʎɐ̃bɐˈsɐ̃w̃", None, "wrong_headword", "esculhambação: the reading ends in -ção, the word in -o"),
    ("hacker", "pt", "portal", "ou", None, "wrong_headword", "the reading is [ou], the conjunction ou"),
    ("halo", "pt-BR", "wiktionary", "'heɪloʊ", None, "wrong_headword", "the English word halo: [eɪ] and [oʊ] are not Portuguese"),
    ("locustídeos", "pt-PT", "infopedia", "lukuʃtiˈdju", None, "wrong_headword", "the singular locustídeo: no reading of the final -s"),
    ("matutagem", "pt-PT", "infopedia", "mɐtutɐˈsɐ̃w̃", None, "wrong_headword", "matutação: the reading ends in -ção, the word in -gem"),
    ("microfarad", "pt-AO", "portal", "mikɾɔ", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microfarad", "pt-BR-x-riodejaneiro", "portal", "mikɾo", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microfarad", "pt-BR-x-saopaulo", "portal", "mikɽo", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microfarad", "pt-BR-x-saopaulo", "portal", "mikɾo", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microfarad", "pt-MZ-x-maputo", "portal", "mikrɔ", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microfarad", "pt-PT-x-lisboa", "portal", "mikɾɔ", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microfarad", "pt-TL-x-dili", "portal", "mikɾɔ", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microvolt", "pt-AO", "portal", "mikɾɔ", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microvolt", "pt-BR-x-riodejaneiro", "portal", "mikɾo", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microvolt", "pt-BR-x-saopaulo", "portal", "mikɽo", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microvolt", "pt-BR-x-saopaulo", "portal", "mikɾo", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microvolt", "pt-MZ-x-maputo", "portal", "mikrɔ", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microvolt", "pt-PT-x-lisboa", "portal", "mikɾɔ", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("microvolt", "pt-TL-x-dili", "portal", "mikɾɔ", None, "wrong_headword", "micro: the reading stops after micro-"),
    ("nanomédico", "pt-PT", "infopedia", "nɐnɔməˈliɐ", None, "wrong_headword", "a word in -melia: the reading ends in -ia, the word in -dico"),
    ("patrónimo", "pt-PT", "infopedia", "pɐtruˈnimiku", None, "wrong_headword", "patronímico: the reading ends in -ico, the word in -imo"),
    ("peruíce", "pt-PT", "infopedia", "pɐrˈvwis", None, "wrong_headword", "parvoíce: the reading has [v] and no [e] of pe-ru"),
    ("peruíce", "pt-PT", "infopedia", "pɐrˈvwisə", None, "wrong_headword", "parvoíce: the reading has [v] and no [e] of pe-ru"),
    ("proxenético", "pt-PT", "infopedia", "prɔksəˈnɛtiku,prɔʃə", "prɔksəˈnɛtiku", "wrong_headword", "the second variant [prɔʃə] covers only proxe-"),
    ("psicadélico", "pt-BR", "wiktionary", "psɪkɐdeˈliɐ", None, "wrong_headword", "psicadelia: the reading ends in -ia, the word in -ico"),
    ("tração", "pt-AO", "portal", "selˈɛtʊ", None, "wrong_headword", "seleto: three syllables se-le-to; the Portal lists only the reading of tra·ção"),
    ("tração", "pt-BR-x-riodejaneiro", "portal", "selˈɛtʊ", None, "wrong_headword", "seleto: three syllables se-le-to; the Portal lists only the reading of tra·ção"),
    ("tração", "pt-BR-x-saopaulo", "portal", "selˈɛtʊ", None, "wrong_headword", "seleto: three syllables se-le-to; the Portal lists only the reading of tra·ção"),
    ("tração", "pt-MZ-x-maputo", "portal", "selˈetu", None, "wrong_headword", "seleto: three syllables se-le-to; the Portal lists only the reading of tra·ção"),
    ("tração", "pt-MZ-x-maputo", "portal", "selˈɛːkθʊ", None, "wrong_headword", "seleto: three syllables se-le-to; the Portal lists only the reading of tra·ção"),
    ("tração", "pt-PT-x-lisboa", "portal", "sɨlˈɛtu", None, "wrong_headword", "seleto: three syllables se-le-to; the Portal lists only the reading of tra·ção"),
    ("tração", "pt-TL-x-dili", "portal", "sɨlˈɛktʊ", None, "wrong_headword", "seleto: three syllables se-le-to; the Portal lists only the reading of tra·ção"),
)


#: Hand-checked ``ipa_broad`` corrections where the narrow correction changes
#: more than a mark (a variant, or a stray symbol in place of the mark), so
#: the broad one cannot be derived from it. Same layout as
#: :data:`PT_UNIFIED_DECISIONS`, with ``original`` the broad reading.
PT_UNIFIED_BROAD_DECISIONS: Tuple[Tuple[str, str, str, str, Optional[str], str, str], ...] = (
    ("coitado", "pt-PT", "wiktionary", "koitádu", "koiˈtadu", "missing_mark", "paroxy"),
    ("excrementoso", "pt-PT", "infopedia", "ajʃkrəmẽˈtozu,iʃkrəmẽtozu",
     "ajʃkrəmẽˈtozu,iʃkrəmẽˈtozu", "missing_mark", "paroxy"),
    ("excrementoso", "pt-PT", "infopedia", "ajʃkrəmẽˈtozu,ʃkrəmẽtozu",
     "ajʃkrəmẽˈtozu,ʃkrəmẽˈtozu", "missing_mark", "paroxy"),
    ("ofídio", "pt-PT", "infopedia", "ɔfiˈdju,uˈfidju", "ɔˈfidju,uˈfidju",
     "accent_contradiction", "í"),
    ("proxenético", "pt-PT", "infopedia", "prɔksəˈnɛtiku,prɔʃə", "prɔksəˈnɛtiku",
     "wrong_headword", "the second variant [prɔʃə] covers only proxe-"),
    ("travesseiro", "pt-BR", "wiktionary", "traveˡsejru", "traveˈsejru",
     "missing_mark", "paroxy"),
)


def _pt_nuclei(reading: str) -> List[Tuple[int, int]]:
    """``(start, end)`` of each vowel of an NFD *reading*, combining marks
    included. Each vowel counts on its own, so a mark between two vowels (a
    hiatus, *liana* ``liˈɐ̃nɐ``) keeps its place."""
    spans, i = [], 0
    while i < len(reading):
        if reading[i] in PT_NUCLEI:
            j = i + 1
            while j < len(reading) and unicodedata.combining(reading[j]):
                j += 1
            spans.append((i, j))
            i = j
        else:
            i += 1
    return spans


def _pt_strip_marks(reading: str) -> str:
    return "".join(c for c in reading if c not in PT_MARKS)


def _pt_same_form(reading: str, like: str) -> str:
    """*reading* written in the characters of *like*.

    The dataset stores some readings decomposed (Infopédia nasal vowels), some
    composed, and a few mixed. When the two differ only in their stress marks,
    the marks of *reading* are placed among the characters of *like*, so the
    segments of the upstream row stay byte-identical. Otherwise *reading* is
    returned composed.
    """
    norm = unicodedata.normalize
    bare = _pt_strip_marks(like)
    if norm("NFD", bare) != norm("NFD", _pt_strip_marks(reading)):
        return norm("NFC", reading)
    target, out, ti, li = norm("NFD", reading), [], 0, 0
    while ti < len(target):
        if target[ti] in PT_MARKS:
            out.append(target[ti])
            ti += 1
            continue
        out.append(bare[li])
        ti += len(norm("NFD", bare[li]))
        li += 1
    return "".join(out)


def _pt_stressed_nucleus(reading: str) -> Optional[int]:
    """Index of the nucleus after the single primary mark, else ``None``."""
    reading = unicodedata.normalize("NFD", reading)
    marks = [i for i, c in enumerate(reading) if c in PT_MARKS]
    if len(marks) != 1:
        return None
    for k, (start, _) in enumerate(_pt_nuclei(_pt_strip_marks(reading))):
        if start >= marks[0]:
            return k
    return None


def _pt_onset_start(reading: str, start: int) -> int:
    """Where the onset of the nucleus at *start* begins in an NFD *reading*:
    a glide with the consonant before it, one consonant, an obstruent + liquid
    cluster, or an affricate. Infopédia and Wiktionary write the mark before
    the onset."""
    i = start

    def consonant(at):
        return (at >= 0 and reading[at] not in PT_NUCLEI + "jwˌ,"
                and not unicodedata.combining(reading[at]))

    if i > 0 and reading[i - 1] in "jw":
        i -= 1
        return i - 1 if consonant(i - 1) else i
    if consonant(i - 1):
        i -= 1
        if i > 0 and reading[i] in "ɾrlɫ" and reading[i - 1] in "pbtdkɡgfv":
            i -= 1
        elif i > 0 and reading[i] in "ʃʒ" and reading[i - 1] in "td":
            i -= 1
        elif i > 1 and reading[i - 1] == "\u0361":
            i -= 2
    return i


def pt_broad_from_narrow(broad: str, narrow: str, source: str) -> Optional[str]:
    """The ``ipa_broad`` correction that matches a corrected ``ipa_narrow``.

    The mark goes on the broad nucleus with the same index, before the vowel
    in a Portal reading and before the onset elsewhere, as each source writes
    it. ``None`` when the broad reading already has the mark there, or when
    its nuclei do not line up with the narrow reading's.
    """
    k = _pt_stressed_nucleus(narrow)
    bare = _pt_strip_marks(unicodedata.normalize("NFD", broad))
    spans = _pt_nuclei(bare)
    narrow_bare = _pt_strip_marks(unicodedata.normalize("NFD", narrow))
    if k is None or len(spans) != len(_pt_nuclei(narrow_bare)):
        return None
    if _pt_stressed_nucleus(broad) == k:
        return None
    start = spans[k][0]
    at = start if source == "portal" else _pt_onset_start(bare, start)
    mark = "'" if "'" in broad else "ˈ"
    return _pt_same_form(bare[:at] + mark + bare[at:], broad)


def pt_ie_stressed(word: str) -> bool:
    """Whether the spelling puts the stress on the e of its one ⟨ie⟩/⟨ee⟩.

    True when that e is ⟨ê⟩, or when the word has no other accent, ends in
    -a, -e, -o (-s), -em or -ens (so it is paroxytone), and the ⟨ie⟩/⟨ee⟩ is
    its next-to-last vowel group, as in *pa·ci·en·te*, *fri·e·za*,
    *gui·ne·en·se*.
    """
    w = word.lower()
    if " " in w or "-" in w or len(re.findall("[ie][eê]", w)) != 1:
        return False
    if any(c in "áéíóúâôãõ" for c in w):
        return False
    if "iê" in w or "eê" in w:
        return True
    groups = re.findall("[aeiouáéíóúâêôãõ]+", w)
    return (re.search("([aeo]s?|em|ens)$", w) is not None
            and len(groups) >= 2 and groups[-2] in ("ie", "ee"))


def pt_ie_mark(reading: str) -> Optional[str]:
    """Insert the primary mark before the one e-vowel that follows [j] or [w]
    in an unmarked reading; ``None`` when there is not exactly one."""
    if any(c in PT_MARKS for c in reading) or "$" in reading or "," in reading:
        return None
    nfd = unicodedata.normalize("NFD", reading)
    hits = list(re.finditer("[jw](?=[eɛ])", nfd))
    if len(hits) != 1 or len(_pt_nuclei(nfd)) < 2:
        return None
    at = hits[0].end()
    return _pt_same_form(nfd[:at] + "ˈ" + nfd[at:], reading)


def _pt_authority(kind: str, basis: str, word: str, region: str) -> str:
    if kind == "wrong_headword":
        text = f"the orthography of ⟨{word}⟩ against the reading"
    elif basis in PT_AUTHORITY:
        text = PT_AUTHORITY[basis]
    else:
        text = PT_AUTHORITY["accent"].format(letter=basis)
    quote = PT_PORTAL_QUOTES.get((word, PT_PORTAL_REGION.get(region, "")))
    if quote:
        text += ("; Portal da Língua Portuguesa, fonetica, region "
                 f"{PT_PORTAL_REGION[region]}: '{quote}'")
    return text


def _pt_reason(kind: str, basis: str, original: str, corrected: Optional[str]) -> str:
    if kind == "wrong_headword":
        what = "the row is dropped" if corrected is None else "that variant is dropped"
        return f"the reading transcribes another headword, {basis}; {what}"
    if kind == "missing_mark":
        return "the reading has no primary stress mark; the mark is added"
    if kind == "unaccented_stress":
        return "the primary stress mark is on a syllable the spelling does not stress"
    return "the primary stress mark contradicts the written accent"


def build_pt_unified_rows(rows: List[Dict]) -> Tuple[List[Dict], Dict[str, int]]:
    """Overlay rows for the unified Portuguese gold, plus the counts.

    *rows* are the dataset's JSONL rows in file order. Three sources of
    correction run over them: the hand-checked :data:`PT_UNIFIED_DECISIONS`,
    the drop of every row whose reading ends in mis-encoded text, and the
    ⟨ie⟩/⟨ee⟩ mark on Portal rows with no primary mark. Each corrected
    ``ipa_narrow`` brings a matching ``ipa_broad`` correction where the broad
    reading shows the same defect. A decision that matches no row raises:
    a silent no-op would ship a ledger that claims a correction it never made.
    """
    from benchmark import pt_unified_source  # the source rule only

    index: Dict[Tuple[str, str, str, str], List[Dict]] = {}
    for row in rows:
        key = (row["word"], row["region"], pt_unified_source(row),
               unicodedata.normalize("NFC", row["ipa_narrow"]))
        index.setdefault(key, []).append(row)
    out: List[Dict] = []
    stats = {"rows_in": len(rows)}
    seen = set()

    def emit(row, field, original, corrected, kind, reason, authority):
        key = (row["word"], row["region"], pt_unified_source(row), row["pos"], field, original)
        if key in seen:
            return
        seen.add(key)
        out.append({
            "dataset": PT_UNIFIED_DATASET, "source": key[2], "region": key[1],
            "word": key[0], "pos": key[3], "field": field,
            "original_reading": original, "corrected_reading": corrected,
            "kind": kind, "reason": reason, "authority": authority,
        })
        stats[kind] = stats.get(kind, 0) + 1

    def emit_with_broad(row, corrected, kind, reason, authority):
        if corrected is not None:
            corrected = _pt_same_form(corrected, row["ipa_narrow"])
        emit(row, "ipa_narrow", row["ipa_narrow"], corrected, kind, reason, authority)
        if (corrected is None or "," in row["ipa_narrow"] or not row["ipa_broad"]
                or _pt_strip_marks(corrected) != _pt_strip_marks(row["ipa_narrow"])):
            return
        broad = pt_broad_from_narrow(row["ipa_broad"], corrected, pt_unified_source(row))
        if broad is not None:
            emit(row, "ipa_broad", row["ipa_broad"], broad, kind, reason, authority)

    for word, region, source, original, corrected, kind, basis in PT_UNIFIED_DECISIONS:
        matches = index.get((word, region, source,
                             unicodedata.normalize("NFC", original)))
        if not matches:
            raise ValueError(f"decision matches no upstream row: {word} {region} "
                             f"{source} {original}")
        for row in matches:
            emit_with_broad(row, corrected, kind,
                            _pt_reason(kind, basis, original, corrected),
                            _pt_authority(kind, basis, word, region))
    broad_index: Dict[Tuple[str, str, str, str], List[Dict]] = {}
    for row in rows:
        key = (row["word"], row["region"], pt_unified_source(row),
               unicodedata.normalize("NFC", row["ipa_broad"]))
        broad_index.setdefault(key, []).append(row)
    for word, region, source, original, corrected, kind, basis in PT_UNIFIED_BROAD_DECISIONS:
        matches = broad_index.get((word, region, source,
                                   unicodedata.normalize("NFC", original)))
        if not matches:
            raise ValueError(f"broad decision matches no upstream row: {word} "
                             f"{region} {source} {original}")
        for row in matches:
            emit(row, "ipa_broad", row["ipa_broad"],
                 _pt_same_form(corrected, row["ipa_broad"]), kind,
                 _pt_reason(kind, basis, original, corrected),
                 _pt_authority(kind, basis, word, region))
    for row in rows:
        if "Ã" in row["ipa_narrow"]:
            authority = (PT_MOJIBAKE_NOTE_AUTHORITY if "nÃ£o" in row["ipa_narrow"]
                         else PT_MOJIBAKE_AUTHORITY)
            emit(row, "ipa_narrow", row["ipa_narrow"], None, "mojibake",
                 PT_MOJIBAKE_REASON, authority)
    for row in rows:
        if pt_unified_source(row) != "portal" or not pt_ie_stressed(row["word"]):
            continue
        basis = "accent" if re.search("[ie]ê", row["word"].lower()) else "paroxy"
        authority = (PT_AUTHORITY["accent"].format(letter="ê") if basis == "accent"
                     else PT_AUTHORITY["paroxy"])
        for field in ("ipa_narrow", "ipa_broad"):
            fixed = pt_ie_mark(row[field])
            if fixed is not None:
                emit(row, field, row[field], fixed, "missing_mark", PT_IE_REASON, authority)
    out.sort(key=lambda r: (r["word"], r["region"], r["source"], r["pos"],
                            r["field"], r["original_reading"]))
    stats["overlay_rows"] = len(out)
    return out, stats


def main_portuguese_unified() -> None:
    import benchmark  # the BASE gold file only; never the o2i engine

    text = benchmark._fetch(benchmark._PT_UNIFIED_URL,
                            "portuguese_pronunciation_lexicon.jsonl")
    rows = [json.loads(line) for line in text.splitlines() if line.strip()]
    overlay, stats = build_pt_unified_rows(rows)
    path = write_overlay(PT_UNIFIED_OVERLAY, overlay)
    for key, value in sorted(stats.items()):
        print(f"  {key}: {value}")
    print(f"wrote {len(overlay)} rows to {os.path.relpath(path, os.getcwd())}")


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
    main_portuguese_unified()


if __name__ == "__main__":
    main()
