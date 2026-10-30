"""Cited-rule tests for Hadza (``hts``), a language isolate of Tanzania.

Every test pins ONE claim the ``hts`` spec makes with a citation, on a real
Hadza word, isolating the segment the claim is about. The two organising
conventions of the practical orthography this spec follows (Miller 2008;
Miller & Anyawire et al. 2013) are what most of these tests defend, because
both are easy to get backwards:

* a DOUBLED letter spells the ejective / glottalised member of a series,
  never a geminate and never a long vowel;
* the clicks are written with the plain Latin letters ``c q x``, with ``h``
  for aspiration and a preceding ``n`` for the nasal click.

Counter-cases are tested alongside each rule: a rule that fires everywhere
is not a rule. Phoneme values come from Sands, Maddieson & Ladefoged 1996
(*The phonetic structures of Hadza*, Studies in African Linguistics 25(2))
and Sands 2013 (*Hadza*, in Vossen ed., *The Khoesan Languages*, Routledge).
"""

import pytest

from orthography2ipa import get
from orthography2ipa.g2p import G2P


@pytest.fixture(scope="module")
def hts():
    return G2P("hts")


# ---------------------------------------------------------------------------
# Doubled letters are the ejective series, not geminates
# ---------------------------------------------------------------------------

def test_doubled_b_is_an_ejective_not_a_geminate(hts):
    """"DOUBLING the letter marks the glottalised ... ⟨bb⟩=[pʼ]" (Sands,
    Maddieson & Ladefoged 1996, ejective series). hûbbu has ⟨bb⟩ between
    vowels: one ejective [pʼ], not [bb] and not [bː]."""
    assert hts.transcribe_word("hûbbu") == "ɦuːpʼu"


def test_doubled_z_is_the_ejective_affricate(hts):
    """⟨zz⟩=[t͡sʼ] against single ⟨z⟩=[d͡z] (SM&L 1996). hozzo 'to be
    afraid' and hazane contrast the two spellings in the same environment."""
    assert hts.transcribe_word("hozzo") == "ɦot͡sʼo"
    assert hts.transcribe_word("hazane") == "ɦad͡zane"


def test_doubled_j_is_the_ejective_affricate(hts):
    """⟨jj⟩=[t͡ʃʼ] against ⟨tch⟩=[t͡ʃʰ] (SM&L 1996). hajjapitchi carries
    both in one word, so a rule that collapsed them would be visible here."""
    assert hts.transcribe_word("hajjapitchi") == "ɦat͡ʃʼapit͡ʃʰi"


def test_doubled_g_is_the_velar_ejective_affricate(hts):
    """⟨gg⟩=[k͡xʼ], labialised ⟨ggw⟩=[k͡xʷʼ] (SM&L 1996)."""
    assert hts.transcribe_word("himiggê") == "ɦimik͡xʼeː"
    assert hts.transcribe_word("dlaggwa") == "c͡ʎ̥˔ʼak͡xʷʼa"


def test_no_tʼ_is_claimed_for_hadza(hts):
    """COUNTER-CASE to the doubling convention. The documented ejective set
    is built on ⟨bb zz jj dl gg ggw⟩; SM&L 1996 describe no /tʼ/ for Hadza,
    so ⟨dd⟩ is deliberately NOT mapped. The spec must not invent the
    segment: ⟨dd⟩ falls through to its plain letters."""
    assert "ʼ" not in hts.transcribe_word("dd")


# ---------------------------------------------------------------------------
# COUNTER-CASE: doubled VOWELS are hiatus, not length and not gemination
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word,expected", [
    ("paana", "paʔana"),
    ("beena", "beʔena"),
    ("roo", "ɺoʔo"),
    ("xxoo", "ŋ͡ǁˀoʔo"),
    ("tlhiika", "c͡ʎ̥˔ʰiʔika"),
])
def test_doubled_vowels_are_glottal_hiatus_not_length(hts, word, expected):
    """The doubling convention is about CONSONANT letters only. Hadza has no
    vowel-initial syllable and no true vowel sequence (Sands 2013, syllable
    structure), so two written vowels are two syllables separated by [ʔ] —
    not one long vowel (length is written with the circumflex) and not a
    geminate. Each word here also proves the ejective rules did not leak
    onto vowel letters."""
    assert hts.transcribe_word(word) == expected


def test_length_is_written_with_the_circumflex(hts):
    """Vowel length is the circumflex, ⟨â ê î ô û⟩ = [aː eː iː oː uː]
    (Miller/Anyawire orthography; Sands 2013 for phonemic length). bôko
    against the doubled-vowel words above: circumflex gives [oː], ⟨oo⟩
    gives [oʔo]."""
    assert hts.transcribe_word("bôko") == "boːko"
    assert hts.transcribe_word("hantâ") == "ɦantʰaː"


# ---------------------------------------------------------------------------
# ⟨dl⟩ is one lateral segment, and must not double
# ---------------------------------------------------------------------------

def test_dl_is_a_single_voiceless_lateral_ejective_affricate(hts):
    """⟨tl tlh dl⟩ are the palatal lateral affricate series [c͡ʎ̥˔],
    [c͡ʎ̥˔ʰ], [c͡ʎ̥˔ʼ] (SM&L 1996). The ejective member is VOICELESS like the
    other two, so ⟨dl⟩ is neither [d]+[l] nor a voiced lateral."""
    out = hts.transcribe_word("midla")
    assert out == "mic͡ʎ̥˔ʼa"
    assert "d" not in out and "l" not in out


def test_dl_is_not_read_as_a_doubled_letter(hts):
    """COUNTER-CASE to the doubling convention: ⟨dl⟩ is a digraph of two
    DIFFERENT letters, so the ejective it spells comes from the lateral
    series, not from the ⟨dd⟩ reading. dlomako has it word-initially, where
    a mis-tokenisation into ⟨d⟩+⟨l⟩ would show immediately."""
    assert hts.transcribe_word("dlomako") == "c͡ʎ̥˔ʼomako"


def test_sl_is_the_lateral_fricative(hts):
    """⟨sl⟩=[ɬ] (SM&L 1996, lateral obstruents) — the other ⟨l⟩ digraph,
    and evidence that ⟨l⟩ is a lateral-marking letter here."""
    assert hts.transcribe_word("sleme") == "ɬeme"


# ---------------------------------------------------------------------------
# ⟨j⟩ is /d͡ʒ/; [t͡ʃ] is its post-nasal realisation
# ---------------------------------------------------------------------------

def test_j_is_underlyingly_voiced(hts):
    """The ejective ⟨jj⟩ is built on the VOICED letter ⟨j⟩, exactly as ⟨bb⟩
    is built on ⟨b⟩ and ⟨gg⟩ on ⟨g⟩, so ⟨j⟩ is /d͡ʒ/ (SM&L 1996). Its
    only environment in the attested lexicon is after a nasal, where the
    general post-nasal devoicing gives [t͡ʃ] — a derived surface form, not
    the phoneme."""
    assert G2P("hts").transcribe_word("qukunju") == "k͡ǃukunt͡ʃu"
    assert get("hts").graphemes["j"][0] == "d͡ʒ"


# ---------------------------------------------------------------------------
# Post-nasal series: the ⟨nd⟩/⟨nt⟩ and ⟨ng⟩/⟨nk⟩ contrasts
# ---------------------------------------------------------------------------

def test_postnasal_voiced_letter_is_a_plain_voiceless_stop(hts):
    """"Hadza has no voiced stop after a nasal" (SM&L 1996): the voiced
    letter of ⟨nd⟩ / ⟨ng⟩ is phonetically [t] / [k]."""
    assert hts.transcribe_word("dunduhina") == "duntuɦina"
    assert hts.transcribe_word("khenangu") == "kʰenanku"


def test_postnasal_voiceless_letter_is_aspirated(hts):
    """The CONTRAST the two spellings encode: ⟨nt⟩ is [ntʰ] and ⟨nk⟩ is
    [nkʰ], against ⟨nd⟩ [nt] and ⟨ng⟩ [nk] (Sands 2013; SM&L 1996). Without
    the aspiration rule the two spellings would merge."""
    assert hts.transcribe_word("intawe") == "ʔintʰawe"
    assert hts.transcribe_word("dlonkô") == "c͡ʎ̥˔ʼonkʰoː"


def test_postnasal_aspiration_is_complete_at_the_labial_place(hts):
    """The documented series is complete at all three places, so ⟨mp⟩ is
    [mpʰ] like ⟨nt⟩ and ⟨nk⟩ (Sands 2013). No word in the current hts gold
    spells ⟨mp⟩ — that is a fact about the word list, not about Hadza, so
    the rule is pinned here on the spelling itself rather than dropped."""
    assert hts.transcribe_word("hampa") == "ɦampʰa"


def test_postnasal_aspiration_does_not_reach_a_derived_voiceless_stop(hts):
    """COUNTER-CASE: the aspiration rule targets the UNDERLYING voiceless
    stop, so the [p] that ⟨mb⟩ derives by devoicing must stay unaspirated.
    cinambo would come out [kǀinampʰo] if the two rules fed each other."""
    assert hts.transcribe_word("cinambo") == "k͡ǀinampo"


def test_stops_are_not_devoiced_or_aspirated_away_from_a_nasal(hts):
    """COUNTER-CASE: neither post-nasal rule may fire without the nasal.
    gewedako keeps [ɡ] and [d]; petena keeps unaspirated [t]."""
    assert hts.transcribe_word("gewedako") == "ɡewedako"
    assert hts.transcribe_word("petena") == "petena"


def test_word_initial_nasal_before_a_consonant_is_syllabic(hts):
    """A word-initial ⟨n⟩ before a consonant is its own syllable nucleus
    [n̩] (Sands 2013, syllable structure)."""
    assert hts.transcribe_word("nkoro") == "n̩kʰoɺo"
    assert hts.transcribe_word("ntsako") == "n̩t͡sʰako"


def test_word_initial_nasal_before_a_vowel_is_not_syllabic(hts):
    """COUNTER-CASE to the syllabic-nasal rule: nube begins with the same
    letter but the nasal has a vowel to lean on, so it is a plain onset."""
    assert hts.transcribe_word("nube") == "nube"


# ---------------------------------------------------------------------------
# The click series
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word,expected", [
    # plain: ⟨c q x⟩
    ("puche", "puk͡ǀʰe"),      # aspirated dental
    ("cinambo", "k͡ǀinampo"),  # plain dental
    ("qhate", "k͡ǃʰate"),      # aspirated alveolar
    ("exekeke", "ʔek͡ǁekeke"),  # plain lateral
    ("naxhi", "nak͡ǁʰi"),      # aspirated lateral
])
def test_clicks_are_written_with_plain_latin_letters(hts, word, expected):
    """The orthography writes the dental, alveolar and lateral clicks with
    ⟨c q x⟩ rather than the click letters, and ⟨h⟩ after the letter marks
    aspiration (Miller/Anyawire orthography; SM&L 1996 for the values)."""
    assert hts.transcribe_word(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("minca", "miŋ͡ǀa"),
    ("henqee", "ɦeŋ͡ǃeʔe"),
    ("binxo", "biŋ͡ǁo"),
])
def test_preceding_n_marks_the_nasal_click(hts, word, expected):
    """A preceding ⟨n⟩ marks the nasal click ⟨nc nq nx⟩ (SM&L 1996)."""
    assert hts.transcribe_word(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("ccama", "ŋ͡ǀˀama"),
    ("haqqako", "ɦaŋ͡ǃˀako"),
    ("khaxxe", "kʰaŋ͡ǁˀe"),
])
def test_doubled_click_letter_marks_the_glottalised_nasal_click(hts, word, expected):
    """The same doubling convention inside the click series: ⟨cc qq xx⟩ are
    the glottalised nasal clicks (SM&L 1996)."""
    assert hts.transcribe_word(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("tanchê", "tank͡ǀʰeː"),
    ("hengcê", "ɦenk͡ǀeː"),
    ("penqhenqhe", "penk͡ǃʰenk͡ǃʰe"),
])
def test_nasal_plus_click_is_not_read_as_a_nasal_click(hts, word, expected):
    """COUNTER-CASE to the nasal-click rule. ⟨nch ngc nqh⟩ are a nasal
    consonant followed by an ORAL click, not the ⟨nc⟩/⟨nq⟩ nasal click:
    tanchê is [tank͡ǀʰeː], not [taŋ͡ǀheː]. Without these keys the greedy
    ⟨nc⟩/⟨nq⟩ match would swallow the following ⟨h⟩."""
    assert hts.transcribe_word(word) == expected


def test_marginal_bilabial_click(hts):
    """A bilabial click survives in a handful of items, written ⟨mc⟩ and
    labialised ⟨mcw⟩ (Sands 2013)."""
    assert hts.transcribe_word("mcw") == "ᵑʘʷ"


# ---------------------------------------------------------------------------
# Glottal onset and hiatus
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word,expected", [
    ("ikha", "ʔikʰa"),
    ("epheme", "ʔepʰeme"),
    ("onoko", "ʔonoko"),
    ("unu", "ʔunu"),
    ("ôbee", "ʔoːbeʔe"),
])
def test_vowel_initial_words_take_a_glottal_onset(hts, word, expected):
    """Hadza has no vowel-initial syllable: every vowel-initial word takes a
    predictable [ʔ] onset (Sands 2013, syllable structure)."""
    assert hts.transcribe_word(word) == expected


def test_word_initial_y_spells_the_glottal_onset_plus_high_vowel(hts):
    """Word-initial ⟨y⟩ is that same onset plus [i] (Sands 2013): there is
    no vowel-initial syllable for a glide to be an onset of."""
    assert hts.transcribe_word("yamua") == "ʔiamuʔa"


def test_consonant_initial_words_take_no_glottal_onset(hts):
    """COUNTER-CASE: the onset rule is conditioned on the vowel, not
    inserted everywhere."""
    assert hts.transcribe_word("bami") == "bami"
    assert hts.transcribe_word("sleme") == "ɬeme"


def test_unlike_vowels_in_hiatus_are_also_separated(hts):
    """The rule is about hiatus, not about identical letters: ⟨ae⟩, ⟨ai⟩
    and ⟨ao⟩ are broken by [ʔ] exactly as ⟨aa⟩ is (Sands 2013)."""
    assert hts.transcribe_word("nxae") == "ŋ͡ǁaʔe"
    assert hts.transcribe_word("kwai") == "kʷaʔi"
    assert hts.transcribe_word("tethao") == "tetʰaʔo"


# ---------------------------------------------------------------------------
# ⟨y⟩ / ⟨w⟩ as written hiatus separators, not segments
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word,expected", [
    # ⟨y⟩ adjacent to a front vowel
    ("hayiko", "ɦaiko"),
    ("piye", "pie"),
    ("tcanjayi", "t͡ʃant͡ʃai"),
    ("yekeko", "ʔiekeko"),
    # ⟨w⟩ adjacent to a round vowel
    ("ukhuwa", "ʔukʰua"),
    ("beggawuko", "bek͡xʼauko"),
    ("thawo", "tʰao"),
])
def test_glide_letter_deletes_next_to_its_own_vowel(hts, word, expected):
    """Sands 2013 describes ⟨y⟩ and ⟨w⟩ between vowels as the written
    separator of a true vowel sequence, and (fn. 7) the [j] / [w] so
    written as mere TRANSITIONS between the flanking vowels rather than
    segments. The transition is inaudible — the two vowels are simply
    adjacent — when a flanking vowel already shares the glide's own place:
    a front vowel for ⟨y⟩, a round vowel for ⟨w⟩. Note the separator also
    blocks the hiatus [ʔ]: these are vowel sequences, not two syllables."""
    assert hts.transcribe_word(word) == expected


@pytest.mark.parametrize("word,expected", [
    # ⟨y⟩ with neither neighbour front
    ("phoyâbii", "pʰojaːbiʔi"),
    # ⟨w⟩ with neither neighbour round
    ("awanika", "ʔawanika"),
    ("hawâ", "ɦawaː"),
    ("gewedako", "ɡewedako"),
    ("nxawejjene", "ŋ͡ǁawet͡ʃʼene"),
    ("zzawabee", "t͡sʼawabeʔe"),
])
def test_glide_letter_survives_when_no_neighbour_shares_its_place(hts, word, expected):
    """COUNTER-CASE, and the reason the rule is stated on place rather than
    as blanket deletion: with neither flanking vowel matching the glide's
    own place the transition is audible and is transcribed. phoyâbii is the
    decisive case — ⟨y⟩ between [o] and [aː], both non-front, keeps [j]."""
    assert hts.transcribe_word(word) == expected


# ---------------------------------------------------------------------------
# Remaining single-letter values that a Latin reading would get wrong
# ---------------------------------------------------------------------------

def test_r_is_a_lateral_flap(hts):
    """⟨r⟩ is [ɺ], not [ɾ] (Sands 2013)."""
    assert hts.transcribe_word("mura") == "muɺa"


def test_h_is_breathy_and_doubled_h_is_the_velar_fricative(hts):
    """Single ⟨h⟩ is [ɦ] and ⟨hh⟩ is [x] (Sands 2013) — the one doubled
    letter that is a fricative rather than an ejective."""
    assert hts.transcribe_word("naha") == "naɦa"
    assert hts.transcribe_word("hh") == "x"


def test_a_written_n_after_a_vowel_is_a_consonant_not_nasalisation(hts):
    """COUNTER-CASE against reading ⟨an en in on un⟩ as nasal vowels: this
    orthography has no nasal-vowel series, so the ⟨n⟩ of zana is a nasal
    CONSONANT and the ⟨a⟩ before it is plain oral [a]."""
    out = hts.transcribe_word("zana")
    assert out == "d͡zana"
    assert "̃" not in out
