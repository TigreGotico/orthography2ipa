"""Dutch vowel length: what is long, what is only tense, and what decides it.

Three cited facts, one per section, and the phonotactic prerequisite the
first of them stands on.

* OPEN-SYLLABLE LENGTHENING/TENSING — Booij, *The Phonology of Dutch*, OUP
  1995, ch. 2; Gussenhoven, "Dutch", JIPA Illustration, 1999. A single vowel
  letter is the TENSE vowel in an open syllable and the LAX vowel in a closed
  one: ma·ken [ˈmaːkən] against mak·ken [ˈmɑkən].
* SHORT TENSE HIGH VOWELS — same two sources. Dutch /i y u/ are tense but
  SHORT; only /aː eː øː oː/ are long. They lengthen before /r/ and nowhere
  else: biet [bit] against banier [baːniːr].
* SYLLABLE-CODA DEVOICING — Booij 1995, ch. 2 § 2.5. A voiced obstruent in
  coda devoices before a following voiceless obstruent, not only word-finally.

The prerequisite is onset-constrained syllabification. Aperture is read off
the spec's own syllabifier, so the vowel of *abrikoos* is long only because
/br/ is a legal Dutch onset (a·bri·koos) and the vowel of *angel* is short
only because /ŋ/ is no onset at all (an·gel).
"""
import pytest

from orthography2ipa import G2P, get
from orthography2ipa.stress import _OnsetJudge, _syllables_for


def syllables(lang, word):
    spec = get(lang)
    diph = spec.stress.diphthongs if spec.stress is not None else ()
    return _syllables_for(word, lang, diph, spec=spec)


@pytest.fixture(scope="module")
def nl():
    return G2P("nl")


# ── open-syllable lengthening / tensing (Booij 1995, ch. 2) ──────────────

@pytest.mark.parametrize("word,ipa", [
    ("maken", "ˈmaːkən"),      # open: a → aː
    ("makken", "ˈmɑkən"),      # closed by a geminate: a stays ɑ
    ("lopen", "ˈloːpən"),      # open: o → oː
    ("wonen", "ˈʋoːnən"),
    ("lip", "ˈlɪp"),           # closed: i stays ɪ
    ("ik", "ˈɪk"),
    ("liter", "ˈlitər"),       # open: i → tense-but-short i, NOT iː
    ("tafel", "ˈtaːfəl"),
    ("water", "ˈʋaːtər"),
])
def test_open_syllable_alternation(nl, word, ipa):
    assert nl.transcribe(word) == ipa


def test_aperture_beats_the_single_consonant_heuristic(nl):
    """*abrikoos* is a·bri·koos, so the ⟨a⟩ is in an OPEN syllable.

    Counting intervocalic consonant LETTERS says the ⟨a⟩ is followed by two
    of them and calls the syllable closed. Reading the syllabification says
    otherwise, because /br/ is a legal Dutch onset (Booij 1995, ch. 2).
    """
    assert syllables("nl", "abrikoos") == ["a", "bri", "koos"]
    assert nl.transcribe("abrikoos") == "ˈaːbrikoːs"


# ── the velar nasal heads no syllable (Booij 1995, ch. 2) ────────────────

@pytest.mark.parametrize("lang,word,sylls", [
    ("nl", "angel", ["ang", "el"]),
    ("nl", "zingen", ["zing", "en"]),
    ("nl", "ankum", ["ank", "um"]),      # ⟨nk⟩ /ŋk/ — a cluster grapheme
    ("de-DE", "singen", ["sing", "en"]),
])
def test_velar_nasal_is_never_an_onset(lang, word, sylls):
    assert syllables(lang, word) == sylls


def test_onset_judge_rejects_the_velar_nasal_directly():
    judge = _OnsetJudge(get("nl"))
    assert judge.licit("ng") is False
    assert judge.licit("nk") is False
    assert judge.licit("n") is True       # the plain coronal nasal is fine
    assert judge.licit("g") is True


def test_closed_by_a_velar_nasal_keeps_the_lax_vowel(nl):
    """*angel* is an·gel: a CLOSED first syllable, so [ɑ] and not [aː].

    This is the length rule reading the phonotactic fact above. Letting /ŋ/
    open a syllable gave a·ngel and the wrong vowel.
    """
    assert nl.transcribe("angel") == "ˈɑŋəl"
    assert nl.transcribe("zingen") == "ˈzɪŋən"


# ── /i y u/ are tense but SHORT (Booij 1995; Gussenhoven 1999) ───────────

@pytest.mark.parametrize("word,ipa", [
    ("biet", "ˈbit"),
    ("boek", "ˈbuk"),
    ("fuut", "ˈfyt"),
])
def test_high_tense_vowels_are_short(nl, word, ipa):
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("banier", "ˈbaːniːr"),
    ("bankier", "ˈbɑŋkiːr"),
    ("aanvuren", "ˈaːnvyːrən"),
    ("afsturen", "ˈɑfstyːrən"),
])
def test_high_tense_i_and_y_lengthen_before_r(nl, word, ipa):
    """Only /i/ and /y/. WikiPron gold: 703 [iːr] to 349 [ir] and 739
    [yːr] to 257 [yr] — 2.0:1 and 2.9:1 FOR lengthening. Every word here
    is gold-attested (banier `baː niː r`, aanvuren `aː n v yː r ə`)."""
    assert nl.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("boer", "ˈbur"),
    ("aanvoer", "ˈaːnvur"),
    ("armsnoer", "ˈɑrmsnur"),
])
def test_u_does_not_lengthen_before_r(nl, word, ipa):
    """Booij 1995 states pre-/r/ lengthening for the whole /i y u/ series,
    but Dutch gold REFUTES it for /u/: 78 [uːr] against 450 [ur], 5.8:1
    the other way, and these three are gold verbatim (boer `b u r`, armsnoer `ɑ r m s n u r`).
    So NL_HIGH_TENSE_LENGTHENING_BEFORE_R_U is deliberately absent — a
    cited rule the data does not support for this member. Adding it
    measured PER 0.0902 -> 0.0910, WER 0.4444 -> 0.4486 on nl wikipron."""
    assert nl.transcribe(word) == ipa


# ── coda devoicing before a voiceless obstruent (Booij 1995, § 2.5) ──────

def test_coda_obstruent_devoices_before_a_voiceless_obstruent(nl):
    """*raadsel* is raad·sel: the ⟨d⟩ is in coda before /s/, so [t].

    ⟨g⟩ already had this rule; the whole voiced-obstruent series follows the
    same generalisation.
    """
    assert nl.transcribe("raadsel") == "ˈraːtsəl"


# ── ⟨y⟩-final words: pinned on the MERGED #850 + #851 result ────────────

@pytest.mark.parametrize("word,ipa", [
    ("beryl", "ˈbɛril"),
    ("butyl", "ˈbʏtil"),
    ("body", "ˈbɔdi"),
    ("baby", "ˈbɑbi"),
    ("hobby", "ˈɦɔbi"),
])
def test_y_final_words_current_behaviour(nl, word, ipa):
    """Pins ⟨y⟩-final words as they stand with #850 MERGED, and records a
    known regression rather than hiding it.

    ⟨y⟩ is not in the engine's closed orthographic-vowel inventory (⟨ý⟩
    is; bare ⟨y⟩ is a consonant letter by construction — see
    ``LanguageSpec.vowel_graphemes``, whose docstring names ⟨y⟩ as exactly
    the letter that must not flip globally). So a final syllable whose only
    vowel LETTER is ⟨y⟩ reads as nucleus-less, and #850's
    ``merge_nucleusless_final_syllable`` folds it into the syllable before,
    closing it: *bo·dy* becomes one closed syllable and the ⟨o⟩ laxes,
    [boːdi] -> [bɔdi].

    Measured on nl wikipron, the 159 ⟨y⟩-final words score PER 0.2157 with
    the merge disabled and 0.2334 with it — a real +0.0177 regression on
    that class, gold-refuted (*baby* is [beːbi] in gold, cf. *babydier*
    `b eː b i d iː r`). It is invisible at corpus level: whole-corpus PER
    is 0.1201 either way, and the published nl/wikipron row is 0.0902 on
    both branches.

    The fix is NOT a spec-side ``vowel_graphemes: ["y"]`` declaration —
    measured, that changes none of these outputs, because
    ``positional._is_open_syllable`` and ``merge_nucleusless_final_syllable``
    call the bare ``is_orthographic_vowel`` on raw syllable strings and
    never consult the spec. Threading ``vowel_graphemes`` into the aperture
    path is an engine change to code #850 has just landed, so it is a
    separate PR (see this PR's description). These pins are the tripwire
    that will fail loudly when it happens.
    """
    assert nl.transcribe(word) == ipa
