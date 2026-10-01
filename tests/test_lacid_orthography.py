"""Cited-rule tests for Lacid / Lashi (``lsi``), the Burmish Latin
orthography devised in the 1970s.

Every test pins ONE claim the spec makes, and the claim's source is named in
the spec's ``notes`` and ``sources``.  The letter values come from the
published alphabet chart for the Cangmokhung standard (Omniglot, "Lashi
(Lacid) language and alphabet"): the initials table, which gives the zero
initial as [ʔ] and the glottalised sonorant digraphs ⟨mh nh nyh ngh rh lh
yh⟩, and the finals table, which gives the checked rimes ⟨ab⟩ [ap], ⟨id⟩
[it], ⟨ag⟩ [ak], ⟨ug⟩ [uk], ⟨oug⟩ [ok], ⟨eig⟩ [ək] and the glottal-final
rimes ⟨aʼ⟩ [aʔ], ⟨oʼ⟩ [oʔ], ⟨uʼ⟩ [uʔ].

The phonetic detail below that chart comes from Hkaw Luk, *A grammatical
sketch of Lacid* (MA thesis, Payap University, 2017), a primary description
written by a native speaker.  Two of its statements are pinned here.  Page
14: "the unreleased voiceless plosive /p, t, k, ʔ/, and the nasals /m, n,
ŋ/ are the only ones used in the coda of a syllable" — so a checked rime
the chart writes [ap] is more precisely [ap̚].  The chart is a rime table in
broad notation and does not contradict this; it simply does not notate
release.  Page 16: creaky vowels occur with "the nasal initials /m, n, ɲ,
ŋ/, lateral initial /l/ and approximant initials /w, ɹ, j/", and its Table 9
gives the contrast as phonemic (jḭt 'liquor' against jit 'drunk').  That
sonorant set is exactly the set the chart spells with a postposed ⟨h⟩, which
is what makes the ⟨h⟩ a phonation mark on the nucleus rather than a segment.

Read the scope honestly.  Most of the words below also occur in the WikiPron
``lsi`` gold row the spec is scored against, so they pin the spec's behaviour
without independently corroborating it.  The one thing they DO establish
independently is that each behaviour follows from the chart entry named in
the docstring rather than from a per-word fit: the chart is a rime table, and
these tests read its rimes back out of whole words the chart never lists.

Counter-cases are included on purpose, because a rule that fires everywhere
is not a rule.  ⟨b⟩ must stay a stop onset in ⟨Abela⟩ and ⟨byu⟩ where it
becomes [p] in ⟨Abraham⟩ and ⟨yab⟩; ⟨o⟩ must stay [ɔ] in ⟨khokham⟩, where
the following ⟨kh⟩ is the next syllable's onset, while it lowers to [o] in
⟨Yokshan⟩, where the following ⟨k⟩ closes the rime.
"""

import unicodedata as U

from orthography2ipa.g2p import G2P


def ipa(word):
    """Transcribe *word* as Lacid, dropping tie bars (notation, not
    phonology) and normalising to NFC."""
    out = G2P("lsi").transcribe_word(U.normalize("NFC", word))
    return U.normalize("NFC", out.replace("͡", ""))


# ---------------------------------------------------------------------------
# The zero initial is [ʔ]
# ---------------------------------------------------------------------------

def test_syllable_with_no_initial_letter_begins_with_glottal_stop():
    """The initials table lists the zero initial as [ʔ], so a syllable
    written with no initial consonant letter is not vowel-initial."""
    assert ipa("Abela") == "ʔabela"
    assert ipa("uri") == "ʔuɹi"
    assert ipa("Aseing") == "ʔasɨŋ"


def test_zero_initial_also_applies_word_internally():
    """The claim is about a SYLLABLE, not about a word edge: a second
    syllable written with no initial letter carries the same [ʔ]."""
    assert ipa("Noa") == "nɔʔa"
    assert ipa("Midian") == "midiʔan"


def test_zero_initial_rime_still_obeys_the_open_closed_split():
    """The glottal onset does not consume the rime.  ⟨og⟩ is a closed rime
    with no initial letter, so it is [ʔok̚] with the same lowered nucleus
    ⟨Yokshan⟩ has — not [ʔɔk̚], which is what a word-initial reading that
    stopped at the glottal would give.  Its plosive is unreleased with
    every other coda plosive (Hkaw Luk 2017:14)."""
    assert ipa("og") == "ʔok̚"


def test_two_adjacent_zero_initial_syllables_each_get_a_glottal():
    """The zero-initial claim is per syllable, so it applies again to the
    second of two syllables that both lack an initial letter: ⟨ia⟩ is
    [ʔiʔa] and not [ʔia]."""
    assert ipa("ia") == "ʔiʔa"


def test_written_initial_blocks_the_glottal_stop():
    """COUNTER-CASE.  A syllable that HAS an initial letter takes no
    glottal onset, or the rule would prefix every word in the language."""
    assert ipa("da") == "da"
    assert ipa("lang") == "laŋ"


# ---------------------------------------------------------------------------
# Checked rimes: ⟨-b -d -g⟩ are [p t k]
# ---------------------------------------------------------------------------

def test_checked_rimes_are_voiceless():
    """The finals table writes the ⟨-b -d -g⟩ rimes voiceless: ⟨ab⟩ [ap],
    ⟨id⟩ [it], ⟨ug⟩ [uk], ⟨oug⟩ [ok].  A coda plosive is also unreleased —
    Hkaw Luk (2017:14) admits only "the unreleased voiceless plosive /p, t,
    k, ʔ/" and the nasals to a coda — so the rime is [ap̚] [it̚] [uk̚]."""
    assert ipa("yab") == "jap̚"
    assert ipa("yug") == "juk̚"
    assert ipa("tid") == "tit̚"
    assert ipa("mougmyid") == "mowk̚mjit̚"


def test_checked_rime_holds_before_a_following_consonant():
    """A checked rime closes its syllable whether the word ends there or
    another syllable follows: ⟨bidthu⟩, ⟨myidjang⟩, ⟨Abraham⟩.  Being in a
    coda, it is unreleased there too (Hkaw Luk 2017:14)."""
    assert ipa("bidthu") == "bit̚tʰu"
    assert ipa("myidjang") == "mjit̚dʑaŋ"
    assert ipa("Abraham") == "ʔap̚ɹaham"


def test_stop_before_a_medial_glide_is_an_onset_not_a_coda():
    """COUNTER-CASE.  ⟨by⟩ and ⟨gy⟩ are the initials table's
    labial/velar-plus-medial-glide onsets [pj] [kj], not a checked rime
    followed by ⟨y⟩, so the stop keeps its onset value — voiced, and with
    no release mark, which Hkaw Luk (2017:14) confines to a coda.  ⟨gyid⟩
    shows both halves at once: an onset ⟨gy⟩ [ɡj] and a coda ⟨d⟩ [t̚]."""
    assert ipa("byu") == "bju"
    assert ipa("gyid") == "ɡjit̚"


def test_stop_before_a_vowel_is_an_onset():
    """COUNTER-CASE.  ⟨b⟩ and ⟨g⟩ between vowels open a syllable and stay
    stops: without this the rule would devoice half the lexicon.  ⟨Ishabag⟩
    separates the two positions in one word — the intervocalic ⟨b⟩ stays
    [b], while the final ⟨g⟩ closes the word and is [k̚]."""
    assert ipa("Abela") == "ʔabela"
    assert ipa("Ishabag") == "ʔiɕabak̚"


# ---------------------------------------------------------------------------
# ⟨ʼ⟩ is the glottal final
# ---------------------------------------------------------------------------

def test_apostrophe_is_the_glottal_final():
    """The finals table gives ⟨aʼ⟩ [aʔ], ⟨oʼ⟩ [oʔ], ⟨uʼ⟩ [uʔ]: the
    modifier letter apostrophe spells a coda [ʔ], not a tone letter alone
    and not nothing."""
    assert ipa("khoʼ") == "kʰɔʔ"
    assert ipa("jhuʼ") == "tɕuʔ"
    assert ipa("yoʼ") == "jɔʔ"


# ---------------------------------------------------------------------------
# Glottalised sonorant digraphs: postposed ⟨h⟩, not preposed
# ---------------------------------------------------------------------------

def test_postposed_h_marks_the_glottalised_sonorant_series():
    """The initials table pairs ⟨m n ny ng l y⟩ with ⟨mh nh nyh ngh lh
    yh⟩.  The ⟨h⟩ follows its sonorant and is not a segment of its own:
    the glottalisation the chart writes [lʼ] is creaky phonation on the
    nucleus, and it is emitted there.  Hkaw Luk (2017:16) reports creaky
    vowels after exactly this sonorant set — "the nasal initials /m, n, ɲ,
    ŋ/, lateral initial /l/ and approximant initials /w, ɹ, j/" — and its
    Table 9 gives the contrast as phonemic, jḭt 'liquor' against jit
    'drunk'.  The mark rides the nucleus vowel, so a diphthong takes it on
    its first element: ⟨nghoid⟩ is [ŋo̰jt̚] and not [ŋoj̰t̚].  Creak after a
    plain obstruent is a different matter — the gold has it, the spelling
    gives no cue for it, and it stays unencoded."""
    assert ipa("lhangmyu") == "la̰ŋmju"
    assert ipa("nghoid") == "ŋo̰jt̚"
    assert ipa("nyhed") == "ɲḛt̚"
    assert ipa("yhoeb") == "jø̰p̚"


# ---------------------------------------------------------------------------
# Rimes that are not the sum of their letters
# ---------------------------------------------------------------------------

def test_ei_is_a_central_vowel_not_a_diphthong():
    """The finals table gives ⟨ei⟩/⟨eu⟩ as one central nucleus, [ə] in the
    Cangmokhung chart and [ɨ] in the Waingmaw transcriptions this spec
    ranks first — not [ei].  ⟨eig⟩ closes on an unreleased [k̚] (Hkaw Luk
    2017:14)."""
    assert ipa("Aseing") == "ʔasɨŋ"
    assert ipa("eig") == "ʔɨk̚"


def test_oe_is_a_front_rounded_vowel():
    """⟨oe⟩ is one nucleus, not [oe]: the finals table lists ⟨oem⟩ and
    ⟨oeb⟩ as rimes of a single vowel."""
    assert ipa("doem") == "døm"
    assert ipa("joem") == "dʑøm"


def test_oo_and_o_are_distinct_open_rimes():
    """⟨o⟩ and ⟨oo⟩ are both open rimes but are not interchangeable: the
    Waingmaw transcriptions contrast ⟨lo⟩ [lɔ] with ⟨loo⟩ [lo] and ⟨mo⟩
    [mɔ] with ⟨moo⟩ [mo], which the spec keeps while listing the chart's
    merged [o] as ⟨o⟩'s second candidate."""
    assert ipa("lo") == "lɔ"
    assert ipa("loo") == "lo"
    assert ipa("mo") == "mɔ"
    assert ipa("moo") == "mo"


def test_o_lowers_only_in_a_closed_rime():
    """COUNTER-CASE for the open/closed split.  In ⟨Yokshan⟩ the ⟨k⟩
    closes the rime, so ⟨o⟩ is [o]; in ⟨khokham⟩ the ⟨kh⟩ opens the next
    syllable, so the first ⟨o⟩ stays [ɔ].  Same letter, same neighbour
    class, different syllable position.  The closing ⟨k⟩ is unreleased, as
    a coda plosive is (Hkaw Luk 2017:14); the ⟨kh⟩ of ⟨khokham⟩ is not,
    because it is an onset."""
    assert ipa("Yokshan") == "jok̚ɕan"
    assert ipa("khokham") == "kʰɔkʰam"
    assert ipa("Babelon") == "babelon"


# ---------------------------------------------------------------------------
# Affricate letters
# ---------------------------------------------------------------------------

def test_affricate_letters_are_not_read_as_plain_latin():
    """⟨z⟩ ⟨j⟩ ⟨c⟩ are the affricate series of the initials table, not
    [z] [dʒ] [k]: the chart gives ⟨z⟩ [ts], ⟨j⟩ [tʃ], ⟨c⟩ [tʃʰ], read
    here with the Waingmaw voicing and place ranked first.  ⟨coid⟩ closes
    on the unreleased coda [t̚] of Hkaw Luk (2017:14)."""
    assert ipa("zain") == "dzajn"
    assert ipa("je") == "dʑe"
    assert ipa("coid") == "tɕʰojt̚"


def test_pyuzung_reads_both_affricate_and_medial_glide():
    """⟨py⟩ is the initials table's [pʼj] onset and ⟨z⟩ its affricate, so
    ⟨pyuzung⟩ has no [z] and no [y] in it anywhere."""
    assert ipa("pyuzung") == "pjudzuŋ"
