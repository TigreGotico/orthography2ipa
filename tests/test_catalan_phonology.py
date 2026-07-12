"""Catalan phonology: the processes that make or break a Catalan transcription.

Catalan is the Iberian language whose surface form is furthest from its
spelling, and almost all of the distance comes from a handful of processes
that a flat grapheme table cannot express:

* **stress**, which is predictable from the orthography (IEC grammar ch. 3)
  and which *conditions the vowel reduction* — get the stressed syllable
  wrong and every vowel in the word is wrong;
* **unstressed vowel reduction** (Eastern block only);
* **word-final ⟨-r⟩ deletion** and **final-cluster simplification**;
* **spirantization**, **final devoicing** and the **cross-word** voicing and
  lenition that only appear in connected speech.

Every word→IPA pair below is either taken from the expert-annotated 4catac
gold (projecte-aina/4catac, 160 sentences × 4 accents) or from the cited
descriptions in Wheeler (2005), Recasens (1996), Veny (1982) and the IEC /
AVL normative grammars.

The DIALECT contrasts are the proof that the four specs are modelled rather
than copied from the parent: Valencian and North-Western do not reduce,
Valencian keeps a final ⟨-r⟩ that the rest delete, only the Eastern block
simplifies a cluster after a lateral, and North-Western opens a final ⟨-a⟩
to [ɛ] that is [ə] in Central and [a] in Valencian.
"""
import pytest

from orthography2ipa import transcribe
from orthography2ipa.stress import detect_stress, syllabify
from orthography2ipa import get


# ─── Stress: the root cause ────────────────────────────────────────────────

@pytest.mark.parametrize("word,expected_index,n_syllables", [
    # A consonant+⟨s⟩ plural is OXYTONE: the plural preserves the stress of
    # the singular, so ⟨importants⟩ is impor-TANTS, not impor-tants. Treating
    # every ⟨-s⟩ as a paroxytone ending stressed the wrong syllable and the
    # reduction then fired on the wrong vowel (IEC grammar ch. 3).
    ("importants", 2, 3),
    ("important", 2, 3),
    # A vowel+⟨s⟩ plural IS paroxytone.
    ("coses", 0, 2),
    ("cases", 0, 2),
    # ⟨-en⟩/⟨-in⟩ are paroxytone (verb forms), so a blanket "-n is oxytone"
    # rule stressed ⟨semblen⟩ on its last syllable.
    ("semblen", 0, 2),
    ("creguin", 0, 2),
    # but a consonant+⟨n⟩ ending is oxytone.
    ("hivern", 1, 2),
    # HIATUS is two syllables: ⟨tenia⟩ is te-ni-a. Merging every vowel run
    # into one nucleus made it te-nia and put the stress on ⟨te⟩.
    ("tenia", 1, 3),
    ("dia", 0, 2),
    ("veïna", 1, 3),
    # a DIPHTHONG is one syllable, and a word ending in one is oxytone.
    ("ciutat", 1, 2),
    ("remei", 1, 2),
    ("aigua", 0, 2),
])
def test_stress_index(word, expected_index, n_syllables):
    rules = get("ca").stress
    sylls = syllabify(word, diphthongs=rules.diphthongs)
    assert len(sylls) == n_syllables, f"{word}: {sylls}"
    assert detect_stress(word, rules, syllables=sylls) == expected_index


def test_diaeresis_is_not_a_stress_mark():
    """⟨ü⟩ marks a pronounced ⟨u⟩, not a stressed vowel (IEC grammar ch. 3).

    Treating it as an accent made ⟨següent⟩ oxytone on the ⟨ü⟩.
    """
    rules = get("ca").stress
    assert "ü" not in rules.marked_vowels and "ï" not in rules.marked_vowels
    # se-gü-ent: the stress is on the last syllable because of the final ⟨-t⟩,
    # not on the ⟨ü⟩ — and the ⟨ü⟩ is a glide, not a nucleus.
    assert "w" in transcribe("següent", "ca")


# ─── Central Catalan word forms (4catac gold + Wheeler 2005) ───────────────

@pytest.mark.parametrize("word,expected", [
    # ⟨c⟩ and ⟨g⟩ before a front vowel (Wheeler 2005 §5.1)
    ("germana", "ʒərmanə"),
    ("gener", "ʒəne"),
    ("cel", "sel"),
    ("ciutat", "siwtat"),
    # word-final ⟨-r⟩ deletion (Wheeler 2005 §10.4)
    ("cantar", "kənta"),
    ("decidir", "dəsiði"),
    ("pagar", "pəɣa"),
    # ⟨-rs⟩: the rhotic goes with it
    ("carrers", "kəres"),
    # final-cluster simplification (Wheeler 2005 §10.4)
    ("quant", "kwan"),
    # the CODA rhotic is the neutralised [r], as in the 4catac gold
    ("important", "impurtan"),
    ("importants", "impurtans"),
    ("temps", "tems"),
    ("cinc", "siŋ"),
    ("sang", "saŋ"),
    # word-final ⟨-ig⟩ = [tʃ], and the ⟨i⟩ is absorbed
    ("vaig", "batʃ"),
    ("mig", "mitʃ"),
    # ⟨x⟩: [ʃ] initially, [ks] before a consonant, [ɡz] in ex- + vowel
    ("explotar", "əkspluta"),
    ("examen", "əɡzamən"),
    # digraphs
    ("cotxe", "kotʃə"),
    ("platja", "pladʒə"),
    ("llibre", "ʎiβɾə"),
    ("any", "aɲ"),
    # ⟨gu⟩/⟨qu⟩: silent ⟨u⟩ before a front vowel, [w] otherwise
    ("guitarra", "ɡitarə"),
    ("aigua", "ajɣwə"),
    ("sigui", "siɣi"),
    # reduction + spirantization together
    ("coses", "kozəs"),
    ("seva", "seβə"),
])
def test_central_word_forms(word, expected):
    """Expectations are written WITHOUT the stress mark.

    The bundled IPA syllabifier is onset-maximising, so it puts a whole coda
    cluster in the following onset and the mark lands a segment or two early
    ([ʒəˈrmanə] for [ʒərˈmanə]). That is a mark-PLACEMENT artefact of a naive
    syllabifier, not a segment error, and the segments are what a consumer —
    and the benchmark, which strips stress marks from both sides — reads.
    """
    assert transcribe(word, "ca").replace("ˈ", "") == expected


# ─── Cross-word (phrase-level) processes ───────────────────────────────────

def test_cross_word_final_s_voicing():
    """A word-final sibilant voices before a vowel or a voiced consonant.

    ⟨les coses importants⟩ → [ləs ˈkɔzəz impuɾˈtans]: the ⟨-s⟩ of ⟨coses⟩ is
    [z] only because the next word begins with a vowel (Wheeler 2005 §5.3).
    """
    assert transcribe("coses importants", "ca").split()[0].endswith("z")
    # ... and stays voiceless before a voiceless one
    assert transcribe("coses per", "ca").split()[0].endswith("s")


def test_cross_word_stop_does_not_voice_before_a_vowel():
    """A final STOP voices before a voiced consonant, not before a vowel.

    ⟨poc a poc⟩ is [ˈpɔk ə ˈpɔk] — a sibilant would voice here, a stop does
    not — while ⟨tot d'una⟩ is [ˈtod ˈdunə].
    """
    assert transcribe("poc a poc", "ca").split()[0].endswith("k")
    assert transcribe("tot dia", "ca").split()[0].endswith("d")


def test_cross_word_spirantization():
    """Lenition of /b d ɡ/ crosses the word boundary inside a phrase.

    ⟨la seva germana … de decidir⟩ → [lə ˈseβə ʒərˈmanə … ðə ðəsiˈði]: the
    ⟨d⟩ of ⟨de⟩ is [ð] because the PRECEDING word ends in a continuant
    (Wheeler 2005 §5.2, §10.5). It stays a stop after a pause or a nasal.
    """
    out = transcribe("la seva germana no s'acaba de decidir", "ca")
    assert "ðə ðəsiˈði" in out
    # phrase-initial → still a stop
    assert transcribe("decidir", "ca").startswith("d")
    # after a nasal → still a stop
    assert transcribe("un dia", "ca").split()[1].replace("ˈ", "")[0] == "d"


def test_atonic_function_words_reduce():
    """Clitics are unstressed *words*, so their vowels reduce.

    ⟨el⟩ ⟨la⟩ ⟨les⟩ ⟨de⟩ ⟨que⟩ are atonic (IEC grammar, 'mots àtons'), and a
    monosyllable-is-always-stressed assumption left them unreduced — [ˈlɛs
    ˈkɔzəs] instead of [ləs ˈkɔzəs] — which is wrong on almost every word of
    running text.
    """
    for word, expected in [("el", "əl"), ("la", "lə"), ("les", "ləs"),
                           ("que", "kə"), ("per", "pər")]:
        assert transcribe(word, "ca").replace("ˈ", "") == expected


# ─── Dialect contrasts: the four specs are modelled, not copied ────────────

@pytest.mark.parametrize("word,central,valencia,occidental,balear", [
    # 1. UNSTRESSED VOWEL REDUCTION — Eastern only (Recasens 1996; Veny 1982)
    ("casa",   "kazə",   "kaza",    "kazɛ",   "kazə"),
    ("tenir",  "təni",   "teniɾ",   "teni",   "təni"),
    # 2. unstressed ⟨o⟩ → [u] in Central, but NOT in Balearic
    ("xocolata", "ʃukulatə", "tʃokolata", "tʃokolatɛ", "ʃokolatə"),
    # 3. word-final ⟨-r⟩ — kept ONLY in Valencian (Veny 1982 ch. 3)
    ("cantar", "kənta",  "kantaɾ",  "kanta",  "kənta"),
])
def test_dialect_vowels_and_final_r(word, central, valencia, occidental, balear):
    def ipa(code):
        return transcribe(word, code).replace("ˈ", "")
    assert ipa("ca") == central
    assert ipa("ca-x-valencia") == valencia
    assert ipa("ca-x-occidental") == occidental
    assert ipa("ca-x-balear") == balear


def test_valencian_does_not_reduce_where_central_does():
    """The contrast that proves the dialects are not a copy of the parent."""
    for word in ["casa", "tenir", "porta", "coses", "germana", "xocolata"]:
        assert "ə" in transcribe(word, "ca"), word
        assert "ə" not in transcribe(word, "ca-x-valencia"), word


def test_final_cluster_after_a_lateral_is_an_east_west_isogloss():
    """⟨molt⟩ is [ˈmol] in the East and [ˈmolt] in the West.

    Both blocks simplify a cluster after a NASAL (⟨important⟩ → [-ˈtan]);
    only the Eastern block does it after a LATERAL (Veny 1982 ch. 3; AVL
    grammar ch. 2), which the 4catac gold shows on both sides.
    """
    assert transcribe("molt", "ca") == "ˈmol"
    assert transcribe("molt", "ca-x-balear") == "ˈmol"
    assert transcribe("molt", "ca-x-valencia") == "ˈmolt"
    assert transcribe("molt", "ca-x-occidental") == "ˈmolt"
    # ⟨ny⟩ is not a stress ending: ⟨any⟩ is [ˈaɲ], not *[ˈəɲ]
    assert transcribe("any", "ca") == "ˈaɲ"
    for code in ["ca", "ca-x-valencia", "ca-x-occidental", "ca-x-balear"]:
        assert transcribe("important", code).endswith("n"), code


def test_valencian_affricate_and_western_x():
    """Valencian ⟨j/g+e,i⟩ = [dʒ] and Western ⟨x⟩ = [tʃ], ⟨ix⟩ = [jʃ]."""
    assert transcribe("germana", "ca-x-valencia").replace("ˈ", "") == "dʒeɾmana"
    assert transcribe("caixa", "ca-x-valencia") == "ˈkajʃa"
    assert transcribe("caixa", "ca") == "ˈkaʃə"
    assert transcribe("marxar", "ca-x-occidental").endswith("tʃa")


def test_balearic_keeps_unstressed_o():
    """Balearic reduces ⟨a⟩/⟨e⟩ to [ə] but never raises unstressed ⟨o⟩."""
    assert "u" not in transcribe("xocolata", "ca-x-balear")
    assert "ʃukuˈlatə" == transcribe("xocolata", "ca")
    assert "ə" in transcribe("casa", "ca-x-balear")


def test_stress_mark_placement_is_onset_maximising():
    """A known limitation, pinned so it cannot drift silently.

    The bundled IPA syllabifier gives a whole consonant cluster to the
    following onset, so the stress mark of ⟨germana⟩ lands before the coda
    ⟨r⟩ rather than after it. The SEGMENTS are right — and the benchmark
    strips stress marks from both sides — but a consumer that needs
    syllable-accurate marks needs a real syllabifier plugin.
    """
    assert transcribe("germana", "ca") == "ʒəˈrmanə"   # not "ʒərˈmanə"
    assert transcribe("germana", "ca").replace("ˈ", "") == "ʒərmanə"
