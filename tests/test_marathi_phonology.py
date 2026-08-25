"""Marathi (mr) phonology: vowel length, schwa deletion, anusvara, affricates.

Marathi shares its script and most of its abugida machinery with Hindi,
Konkani, Nepali and Sanskrit, but it diverges from all of them on the points
below, and each divergence is a place where a shared engine or a copied spec
would quietly give the Hindi answer. The Sanskrit and Hindi assertions at the
bottom are the leak detectors: they are what breaks first if any of this
migrates out of the Marathi data.

Sources for the rules under test:

- Loss of the Sanskrit vowel-length contrast, the alveolar tap, the retroflex
  lateral flap and the schwa-after-cluster exception: Wikipedia, "Marathi
  phonology" ("There is almost no phonemic length distinction, even though it
  is indicated in the script"; "it has conserved the schwas after consonant
  clusters in words like शब्द").
- ⟨ऋ⟩ read as [ɾu] and the two affricate series of ⟨च ज झ⟩: Wikipedia,
  "Marathi language" (vowel table "ऋ ṛ /ru/"; consonant table "च ca, ċa
  /t͡ɕə/ or /t͡sə/").
- Medial schwa retained far more freely than in Hindi: Wikipedia, "Schwa
  deletion in Indo-Aryan languages" ("In places where the schwa occurs in the
  middle of words, Marathi does exhibit a propensity to pronounce it far more
  regularly than Hindi"; "comprehension of Marathi is not impeded if all
  schwas are retained").
- Schwa deletion in modern Indo-Aryan generally, the anusvara as a homorganic
  nasal, and the murmured sonorants: Masica, *The Indo-Aryan Languages*
  (1991); Dhongde & Wali, *Marathi* (John Benjamins, 2009) — editions not
  consulted, these inventory claims are quoted at second hand.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def mr() -> G2P:
    return G2P("mr")


@pytest.fixture(scope="module")
def hi() -> G2P:
    return G2P("hi")


@pytest.fixture(scope="module")
def sa() -> G2P:
    return G2P("sa")


# ── no phonemic vowel length ────────────────────────────────────────────────

@pytest.mark.parametrize("word,ipa", [
    ("नाम", "nam"),          # nām 'name'
    ("फूल", "pʰul"),         # phūl 'flower' — ⟨ऊ⟩ is not a long vowel
    ("आग", "aɡ"),            # āg 'fire'
    ("देश", "d̪eɕ"),          # deś 'country' — ⟨े⟩ is not a long vowel
])
def test_no_length_mark_on_any_vowel(mr, word, ipa):
    """⟨अ⟩ vs ⟨आ⟩ is [ə] vs [a], a quality contrast, not a length one.

    The script writes the Sanskrit length distinction; the language has lost
    it. Every length mark the spec used to emit was notation copied from
    Sanskrit, and it cost more than every other Marathi error combined.
    """
    assert mr.transcribe_word(word) == ipa
    assert "ː" not in mr.transcribe_word(word)


def test_sanskrit_keeps_its_vowel_length(sa):
    """Leak detector: the length fold is Marathi's, not the script's."""
    assert "ː" in sa.transcribe_word("नाम")


# ── word-final schwa deletion, and the cluster exception ────────────────────

@pytest.mark.parametrize("word,ipa", [
    ("अंगण", "əŋɡəɳ"),       # aṅgaṇ 'courtyard'
    ("अंकुश", "əŋkuɕ"),      # aṅkuś 'goad'
    ("अजगर", "ədʑəɡəɾ"),     # ajgar 'python'
    ("अटकळ", "əʈəkəɭ̆"),     # aṭkaḷ 'guess'
])
def test_final_inherent_vowel_is_deleted_after_a_vowel(mr, word, ipa):
    assert mr.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("शब्द", "ɕəbd̪ə"),       # śabda 'word' — the textbook case
    ("अंतरिक्ष", "ənt̪əɾikʂə"),  # antarikṣa 'space'
])
def test_final_schwa_survives_a_written_cluster(mr, word, ipa):
    """Marathi's split from Hindi: deleting here would leave a word-final
    cluster, which Marathi does not allow, so the schwa stays."""
    assert mr.transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("अंक", "əŋkə"),         # aṅk 'number'
    ("अंत", "ənt̪ə"),         # ant 'end'
    ("अंड", "əɳɖə"),         # aṇḍ 'egg'
])
def test_final_schwa_survives_an_anusvara_cluster(mr, word, ipa):
    """The blocking cluster does not have to be written with a virama.

    An anusvara before a stop IS the first member of the cluster, so the same
    condition — a preceding slot that ends in a consonant — holds, and the
    schwa stays. This is the interaction the Devanagari specs get wrong in
    the other direction elsewhere: a nasal an anusvara produced is invisible
    to a guard that only lists letter-written consonants.
    """
    assert mr.transcribe_word(word) == ipa


def test_hindi_deletes_the_final_schwa_after_a_cluster(hi):
    """Leak detector on the exception itself: Hindi is the language that
    deletes here, and its rules must not acquire Marathi's condition."""
    assert not hi.transcribe_word("शब्द").endswith("ə")


def test_monosyllabic_one_letter_word_keeps_its_only_vowel(mr):
    """Over-application guard: न is [nə], never bare *[n]. The rule requires
    a preceding slot, and a one-letter word has none."""
    assert mr.transcribe_word("न") == "nə"


def test_sanskrit_keeps_the_inherent_vowel(sa):
    """Leak detector: mr declares sa as its parent and shares its script."""
    assert sa.transcribe_word("नाम").endswith("ə")


# ── medial schwa is NOT deleted ─────────────────────────────────────────────

@pytest.mark.parametrize("word,ipa", [
    ("अवसर", "əʋəsəɾ"),      # avsar 'occasion' — gold transcribes the
                              # deleted variant, əvsər; this asserts the
                              # fully-retained pronunciation this spec emits
    ("अननस", "ənənəs"),      # ananas 'pineapple' — same: gold keeps the
                              # deleted variant, this spec the retained one
    ("अंकगणित", "əŋkəɡəɳit̪"),  # aṅkgaṇit 'arithmetic' — the gold-backed
                              # exemplar: the gold itself keeps both schwas
])
def test_medial_schwa_is_retained(mr, word, ipa):
    """Marathi declares no VC_CV medial rule, on purpose.

    Medial deletion is optional in Marathi in a way it is not in Hindi, and a
    fully-retained pronunciation is well formed (Wikipedia, "Schwa deletion
    in Indo-Aryan languages": "comprehension of Marathi is not impeded if
    all schwas are retained"; "propensity to pronounce it far more
    regularly than Hindi"). Encoding Hindi's categorical rule here would
    fire on अंकगणित, where the gold keeps both vowels. Of the schwas this
    spec emits that a medial rule could target, the wikipron gold retains
    81% of them; अवसर and अननस above are two of the exceptions, where the
    gold happens to transcribe the deleted variant instead. The cost is
    real and is the largest single component of what Marathi still misses;
    it is a deliberate accuracy-over-score choice, not an oversight.
    """
    assert mr.transcribe_word(word) == ipa


def test_hindi_still_deletes_its_medial_schwa(hi):
    """The mirror leak detector: dropping the rule from Marathi must not
    drop it from Hindi."""
    assert hi.transcribe_word("नमकीन") == "nəmkiːn"


# ── anusvara as a homorganic nasal consonant ────────────────────────────────

@pytest.mark.parametrize("word,ipa", [
    ("अंकुश", "əŋkuɕ"),      # velar
    ("अंजीर", "əndʑiɾ"),     # palatal — coronal [n], not [ɲ]
    ("अंडे", "əɳɖe"),        # retroflex
    ("अंतर", "ənt̪əɾ"),       # dental
    ("आंबा", "amba"),        # labial
])
def test_anusvara_before_a_stop_is_a_homorganic_nasal(mr, word, ipa):
    """Not nasalization of the preceding vowel: the sign writes the nasal of
    a nasal+stop cluster and takes the stop's place of articulation."""
    assert mr.transcribe_word(word) == ipa


def test_anusvara_before_a_non_stop_still_nasalizes(mr):
    """Over-application guard: the homorganic rules are keyed to the stop
    letters, so an anusvara before anything else keeps the vowel-nasalizing
    reading — and still blocks the final schwa deletion, because what it
    writes there is a nasalized approximant, not nothing."""
    assert mr.transcribe_word("गांव") == "ɡãʋə"


# ── the two affricate series ────────────────────────────────────────────────

@pytest.mark.parametrize("word", ["अंजीर", "चिकन", "जिज्ञासा"])
def test_no_alveolar_affricate_before_a_front_vowel(mr, word):
    """⟨च ज झ⟩ stand for [t͡s d͡z d͡zʱ] as well as [t͡ɕ d͡ʑ d͡ʑʱ], but only the
    palato-alveolar member occurs before a front vowel or [j].

    Before a non-front vowel the choice is lexical — broadly native
    vocabulary against Sanskrit and Perso-Arabic loans — so it cannot be read
    off the spelling and both readings stay in the lattice there. Only the
    one-directional half is stated as a rule.
    """
    out = mr.transcribe_word(word)
    assert "ts" not in out and "dz" not in out


def test_alveolar_affricate_stays_available_before_a_back_vowel(mr):
    """The rule must not collapse the contrast: आज is [ad͡z] for many
    speakers and [ad͡ʑ] for others, and both must survive in the lattice."""
    readings = set(mr.word_candidates("आज"))
    assert "adz" in readings and "adʑ" in readings


# ── consonants Marathi does not share with Hindi ────────────────────────────

def test_r_is_a_tap(mr):
    assert mr.transcribe_word("राम") == "ɾam"


def test_lla_is_a_retroflex_lateral_flap(mr):
    """⟨ळ⟩, the Marathi hallmark: केळी 'bananas'."""
    assert mr.transcribe_word("केळी") == "keɭ̆i"


def test_sha_is_alveolo_palatal(mr):
    """⟨श⟩ is [ɕ], matching the alveolo-palatal affricates the spec already
    gives ⟨च ज⟩ — one place of articulation for the whole series."""
    assert mr.transcribe_word("देश") == "d̪eɕ"


@pytest.mark.parametrize("word,ipa", [
    ("ऋण", "ɾuɳ"),           # ṛṇ 'debt'
    ("अधिकृत", "əd̪ʱikɾut̪"),  # adhikṛt 'authorised'
])
def test_vocalic_r_is_read_ru(mr, word, ipa):
    """Marathi reads ⟨ऋ⟩ as [ɾu] — neither the Sanskrit syllabic [r̩] nor the
    Hindi [ɾɪ]."""
    assert mr.transcribe_word(word) == ipa


def test_sanskrit_keeps_the_syllabic_r(sa):
    """Leak detector for the ⟨ऋ⟩ reading."""
    assert "u" not in sa.transcribe_word("ऋण")


@pytest.mark.parametrize("word,ipa", [
    ("म्हण", "mʱəɳ"),        # mhaṇ 'proverb'
    ("गुन्हा", "ɡunʱa"),      # gunhā 'crime'
    ("कोल्हा", "kolʱa"),      # kolhā 'fox'
])
def test_sonorant_plus_ha_is_a_murmured_sonorant(mr, word, ipa):
    assert mr.transcribe_word(word) == ipa


def test_ha_before_a_sonorant_is_not_murmured(mr):
    """Order matters and the digraphs must not fire backwards: ब्रह्मा keeps
    a plain [ɦ] followed by [m]."""
    assert mr.transcribe_word("ब्रह्मा") == "bɾəɦma"
