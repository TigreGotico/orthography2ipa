"""Quantity-sensitive stress: placement by syllable weight, not by spelling.

The end-anchored systems (Portuguese, Spanish, Italian) pick the stressed
syllable from an orthographic ending. Arabic and Latin do not: stress falls on a
syllable because that syllable is **heavy**, and weight is a property of the
transcription — a long vowel, a coda — not of the spelling. No ending table can
express it, which is exactly why the Arabic spec used to declare no stress at
all.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import phoneme_atoms
from orthography2ipa.stress import (
    HEAVY, LIGHT, SUPERHEAVY, detect_stress_by_weight, syllabify_ipa,
    syllable_weight,
)
from orthography2ipa.types import StressRules

ARABIC = StressRules(
    default_position=-3,
    quantity_sensitive=True,
    superheavy_final_attracts=True,
    max_onset=1,
)


# ─── the syllabifier: weight depends on where the boundary falls ────────

@pytest.mark.parametrize("ipa,expected", [
    ("kitaːb", ["ki", "taːb"]),
    # The load-bearing case. Onset-maximising gives mu-da-rris, whose penult is
    # LIGHT, and the stress would land on the antepenult. Arabic takes exactly
    # one consonant as an onset, so the cluster splits: mu-dar-ris, the penult
    # is heavy, and the stress lands there.
    ("mudarris", ["mu", "dar", "ris"]),
    ("madrasa", ["mad", "ra", "sa"]),
    ("qahwa", ["qah", "wa"]),
    ("kataba", ["ka", "ta", "ba"]),
])
def test_syllabify_ipa_divides_clusters_by_onset_limit(ipa, expected):
    assert syllabify_ipa(ipa, max_onset=1) == expected


def test_onset_limit_changes_the_division():
    """A larger onset limit hands the whole cluster forward, emptying the coda.

    With both consonants of ⟨rr⟩ allowed as an onset the penult keeps no coda
    and is light — which is precisely the mis-division that would put Arabic's
    stress on the wrong syllable.
    """
    assert syllabify_ipa("mudarris", max_onset=2) == ["mu", "da", "rris"]
    assert syllable_weight("da") == LIGHT


# ─── weight ─────────────────────────────────────────────────────────────

@pytest.mark.parametrize("syllable,weight", [
    ("ki", LIGHT),          # CV
    ("taː", HEAVY),         # CVː
    ("dar", HEAVY),         # CVC
    ("taːb", SUPERHEAVY),   # CVːC
    ("bint", SUPERHEAVY),   # CVCC
    ("bajt", SUPERHEAVY),   # diphthong + coda
])
def test_syllable_weight(syllable, weight):
    assert syllable_weight(syllable) == weight


# ─── the cascade ────────────────────────────────────────────────────────

@pytest.mark.parametrize("ipa,index,why", [
    ("kitaːb", -1, "superheavy final takes the stress"),
    ("mudarris", -2, "heavy penult takes it when the final is not superheavy"),
    ("madrasa", -3, "otherwise the antepenult"),
    ("kataba", -3, "all light → antepenult"),
    ("qahwa", -2, "two syllables: the heavy penult is also the first"),
])
def test_detect_stress_by_weight(ipa, index, why):
    assert detect_stress_by_weight(ipa, ARABIC) == index, why


def test_a_language_that_never_stresses_the_final_syllable():
    """Latin's rule: a superheavy final does NOT attract stress."""
    latin = StressRules(
        default_position=-3, quantity_sensitive=True,
        superheavy_final_attracts=False, max_onset=1,
    )
    assert detect_stress_by_weight("kitaːb", latin) == -2
    assert detect_stress_by_weight("kitaːb", ARABIC) == -1


def test_monosyllable():
    assert detect_stress_by_weight("bajt", ARABIC) == -1


# ─── end to end, through the G2P ────────────────────────────────────────

@pytest.mark.parametrize("word,expected,why", [
    ("كِتَاب", "kiˈtaːb", "superheavy final CVːC"),
    ("مُدَرِّس", "muˈdarris", "heavy penult CVC"),
    ("مَدْرَسَة", "ˈmadrasa", "all-light tail → antepenult"),
    ("قَهْوَة", "ˈqahwa", "heavy penult, two syllables"),
    ("كَتَبَ", "ˈkataba", "all light → antepenult"),
])
def test_arabic_is_stressed_end_to_end(word, expected, why):
    """The system this was built for, through the real shipped spec."""
    assert G2P("ar").transcribe(word) == expected, why


@pytest.mark.parametrize("lang", ["ars-SA", "acw-SA", "arz-EG"])
def test_the_varieties_are_stressed_too(lang):
    assert G2P(lang).transcribe("كِتَاب").endswith("ˈtaːb")


def test_end_anchored_languages_are_untouched():
    """The existing systems must not move."""
    assert G2P("pt").transcribe("palavra") == "pɐˈlavɾɐ"
    assert not get("pt").stress.quantity_sensitive


def test_the_arabic_specs_opt_in():
    """Arabic is the system this was built for, and it now declares the block."""
    import json as _json
    import os as _os

    import orthography2ipa as _o2i
    from orthography2ipa import available_codes

    opted_in = {
        code for code in available_codes()
        if (get(code).stress and get(code).stress.quantity_sensitive)
    }
    assert {"ar", "arb", "ars-SA", "acw-SA", "arz-EG"} <= opted_in

    # Stress rides the graphemes edge, so the set entitled to inherit the block is
    # computed from that edge rather than listed: every spec whose ``graphemes_base``
    # chain ends at ``arb``. A variety that keeps only a genetic ``parent`` while
    # authoring its own orthography — mt Maltese, acy Cypriot Arabic — falls outside
    # it, correctly. A test on the code name would be wrong in both directions: this
    # repo ships arc Aramaic, arn Mapudungun, arp Arapaho, arr Karo, arv Arbore and
    # arw Arawak, none of them Arabic, while ar-TD-x-babalia Babalia Creole and sqr Siculo are
    # Arabic and look like neither.
    _data = _os.path.join(_os.path.dirname(_o2i.__file__), "data")

    def _graphemes_root(code):
        seen = set()
        while code not in seen:
            seen.add(code)
            path = _os.path.join(_data, code + ".json")
            if not _os.path.exists(path):
                return code
            with open(path, encoding="utf-8") as fh:
                base = _json.load(fh).get("graphemes_base")
            if not base:
                return code
            code = base
        return code

    inherits_from_arabic = {c for c in available_codes() if _graphemes_root(c) == "arb"}
    assert {"ar-TD-x-babalia", "sqr", "xaa"} <= inherits_from_arabic
    assert not {"mt", "acy"} & inherits_from_arabic, (
        "a genetic parent is not a graphemes base")

    # What remains is editorial, and only three specs need deciding by hand:
    # languages outside the Arabic grapheme lineage whose stress is cited as
    # quantity-sensitive in its own right. idb Sri Lanka Portuguese takes stress on
    # the long-vowel syllable and otherwise initially (Cardoso, APiCS 41); cic
    # Chickasaw puts the primary accent on the rightmost heavy CVV/CVC syllable
    # (Munro & Willmond 1994, *Chickasaw: An Analytical Dictionary*); and
    # ar-Latn-x-buckwalt is Arabic transliterated into Latin, so it declares the
    # block without sharing an Arabic grapheme table to inherit it from.
    _cited_outside_the_lineage = {"idb", "cic", "ar-Latn-x-buckwalt"}
    assert opted_in <= inherits_from_arabic | _cited_outside_the_lineage, sorted(
        opted_in - inherits_from_arabic - _cited_outside_the_lineage)


# ─── weight is counted in SEGMENTS, not characters ──────────────────────
#
# A modifier letter (pharyngealization ˤ, aspiration ʰ, length ː) rides on the
# consonant it modifies, and an affricate is one consonant, not a cluster.
# Counting characters made a CVC coda look like CVCC, called the syllable
# superheavy and pulled the stress onto it: /ɣalatˤ/ came out ɣaˈlɑtˤ and
# /xaradʒ/ xaˈradʒ, both wrong.

@pytest.mark.parametrize("syllable,weight,why", [
    ("latˤ", HEAVY, "tˤ is ONE pharyngealized consonant — CVC, not CVCC"),
    ("radʒ", HEAVY, "dʒ is ONE affricate — CVC"),
    ("lidz", HEAVY, "so is the Najdi affricate dz"),
    ("lit͡s", HEAVY, "tie-barred spelling likewise"),
    ("bakʰt", SUPERHEAVY, "a real two-consonant coda is still superheavy"),
])
def test_syllable_weight_counts_segments(syllable, weight, why):
    assert syllable_weight(syllable) == weight, why


@pytest.mark.parametrize("ipa,index,why", [
    ("ɣalatˤ", -2, "final CVC is only heavy, so it does not attract"),
    ("xaradʒ", -2, "same, with an affricate coda"),
    ("saːlidz", -2, "heavy penult saː keeps the stress"),
])
def test_detect_stress_by_weight_counts_segments(ipa, index, why):
    assert detect_stress_by_weight(ipa, ARABIC) == index, why


def test_an_affricate_is_never_split_across_a_syllable_boundary():
    assert syllabify_ipa("katsib", max_onset=1) == ["ka", "tsib"]
    assert syllabify_ipa("matˤɑr", max_onset=1) == ["ma", "tˤɑr"]


# A spec's phoneme list is in inventory order, not longest-first: es-ES lists
# /t/ before /tʃ/, and zh lists /t/ before /tɕ/ before /tɕʰ/. Passed as atoms,
# the longest phoneme must still win, or the affricate splits across the
# syllable boundary and its syllable counts a two-consonant coda.
@pytest.mark.parametrize("lang,affricate,prefixes,ipa,syllables", [
    ("es-ES", "tʃ", ("t",), "atʃa", ["a", "tʃa"]),
    ("zh", "tɕʰ", ("t", "tɕ"), "atɕʰa", ["a", "tɕʰa"]),
])
def test_spec_phonemes_as_atoms_keep_the_affricate_whole(
        lang, affricate, prefixes, ipa, syllables):
    atoms = list(get(lang).phonemes)
    assert all(atoms.index(p) < atoms.index(affricate) for p in prefixes), (
        "the case only bites while a prefix of the affricate is listed first")
    assert syllabify_ipa(ipa, max_onset=1, atoms=atoms) == syllables
    assert syllable_weight("a" + affricate, atoms) == HEAVY, "CVC, one coda consonant"


# A spec may declare a diphthong as one phoneme. Passed as an atom it becomes
# one segment, but it is still a branching nucleus, so the syllable is heavy.
@pytest.mark.parametrize("lang,diphthong,syllable", [
    ("nb", "æʉ", "æʉ"),
    ("diq", "ai", "ai"),
    ("diq", "au", "au"),
    ("shk", "aɪ", "aɪ"),
    ("sah", "ɯa", "ɯa"),
    ("inh", "oa", "joa"),
])
def test_a_diphthong_declared_as_one_phoneme_is_heavy(lang, diphthong, syllable):
    atoms = list(get(lang).phonemes)
    assert diphthong in atoms, "the case only bites while the spec declares the diphthong"
    assert syllable_weight(syllable, atoms) == HEAVY
    assert syllable_weight(syllable + "n", atoms) == SUPERHEAVY, "branching nucleus + coda"
    assert syllable_weight(syllable[:-1], atoms) == LIGHT, "one vowel alone stays light"


@pytest.mark.parametrize("syllable,weight,why", [
    ("aɪ̯", HEAVY, "a falling diphthong with a non-syllabic mark is two vocoids"),
    ("ɐ̃", LIGHT, "the nasal tilde is a mark on one vowel, not a second vowel"),
    ("ɛ̯", LIGHT, "the non-syllabic mark alone is not a second vowel"),
    ("amo", LIGHT, "two vowels with a consonant between them are no diphthong"),
])
def test_one_atom_nucleus_branches_only_on_adjacent_vowels(syllable, weight, why):
    assert syllable_weight(syllable, [syllable]) == weight, why


@pytest.mark.parametrize("lang,diphthong,syllable", [
    ("nn", "œʏ", "œʏ"), ("wym", "ɔʏ", "ɔʏ"), ("sxu", "ɞʏ̯", "ɞʏ̯"),
])
def test_a_declared_diphthong_ending_in_y_is_heavy(lang, diphthong, syllable):
    # ʏ is not in the IPA vowel table; the feature table holds it as a vowel.
    atoms = list(get(lang).phonemes)
    assert diphthong in atoms, "the case only bites while the spec declares the diphthong"
    assert syllable_weight(syllable, atoms) == HEAVY
    assert syllable_weight(syllable + "n", atoms) == SUPERHEAVY, "branching nucleus + coda"


@pytest.mark.parametrize("lang,diphthong,syllable", [
    ("es-ES", "aj", "paj"), ("es-ES", "aw", "kaw"), ("ar", "aj", "bajt"),
    ("pt-PT", "ɐ̃w̃", "mɐ̃w̃"), ("de-DE", "ɔʏ", "nɔʏ"), ("nl-NL", "œʏ", "œʏ"),
])
def test_a_diphthong_atom_weighs_as_its_letters_do_without_the_atom(lang, diphthong, syllable):
    # Without the atom the glide or ʏ is a second segment and the syllable is
    # heavy; the atom must not make the same syllable lighter.
    atoms = phoneme_atoms(get(lang))
    assert diphthong in atoms, "the case only bites while the spec emits the diphthong"
    assert syllable_weight(syllable, atoms) == syllable_weight(syllable)
    assert syllable_weight(syllable, atoms) in (HEAVY, SUPERHEAVY)


@pytest.mark.parametrize("syllable,weight,why", [
    ("aj", HEAVY, "a vowel and a glide letter are a falling diphthong"),
    ("aw", HEAVY, "a vowel and a glide letter are a falling diphthong"),
    ("ɐ̃w̃", HEAVY, "the nasal tilde on the glide does not hide it"),
    ("aja", LIGHT, "a glide before a vowel opens that vowel, it does not close the first"),
    ("ja", LIGHT, "a glide before the only vowel is an onset"),
    ("aʲ", LIGHT, "a palatalisation mark is not a glide letter"),
])
def test_a_glide_letter_branches_the_nucleus_only_after_a_vowel(syllable, weight, why):
    assert syllable_weight(syllable, [syllable]) == weight, why


def test_the_stress_mark_never_lands_inside_a_long_vowel():
    """The mark is placed against the weight syllabifier's own division.

    The naive `syllabify` cuts `saːliq` as sa|ːliq, so marking the final
    syllable there produced `saˈːliq` — a stress mark inside a long vowel,
    which is not well-formed IPA.
    """
    from orthography2ipa.stress import apply_stress_mark
    marked = apply_stress_mark(
        "saːliq", ARABIC, -1,
        ipa_syllables=syllabify_ipa("saːliq", ARABIC.max_onset),
    )
    assert marked == "saːˈliq"
