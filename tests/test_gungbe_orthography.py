"""Cited-rule tests for Gun / Gungbe (``guw``), a Gbe lect of Benin and Nigeria.

Every test pins one claim the ``guw`` spec makes, isolating the segment the
claim is about.  Two orthographies are in use for the same language — the Benin
national alphabet (⟨ɛ ɔ ɖ x⟩) and a Yoruba-based Nigerian one (⟨ẹ ọ ṣ⟩) — and
the spec describes both, so the tests come in pairs wherever the WikiPron gold
attests a word in both spellings.  Words are given in the gold's own
capitalisation; a form the gold does not carry is not used as a test word.
"""

from orthography2ipa.g2p import G2P


def guw(word: str) -> str:
    return G2P("guw").transcribe_word(word)


def candidates(word: str):
    return G2P("guw").word_candidates(word)


# ---------------------------------------------------------------------------
# The Nigerian (Yoruba-based) letters
# ---------------------------------------------------------------------------

def test_subdot_e_is_open_e():
    """⟨ẹ⟩ is the Nigerian spelling of the Benin letter ⟨ɛ⟩ /ɛ/: the gold's
    doublet ⟨Lẹgba⟩ / ⟨Lɛgba⟩ spells one name two ways."""
    assert guw("Lẹgba") == guw("Lɛgba") == "lɛɡ͡ba"


def test_subdot_o_is_open_o():
    """⟨ọ⟩ is the Nigerian spelling of ⟨ɔ⟩ /ɔ/ — the doublet ⟨tohọ⟩ / ⟨toxɔ⟩,
    both [toxɔ] in the gold, differs in two letters and in neither sound."""
    assert guw("tohọ").endswith("ɔ")
    assert guw("toxɔ") == "toxɔ"


def test_subdot_s_is_postalveolar():
    """⟨ṣ⟩ carries its Yoruba value /ʃ/ — ⟨oṣo⟩ [oʃo]."""
    assert guw("oṣo") == "oʃo"


def test_subdot_s_also_stands_in_for_the_affricate():
    """⟨ṣ⟩ also does duty for Benin ⟨c⟩ /t͡ʃ/: the gold's ⟨Ajaṣẹ⟩ / ⟨Ajacɛ⟩ are
    one name, both [adʒatʃɛ], so the affricate stays reachable."""
    assert "tʃ" in " ".join(candidates("Ajaṣẹ"))
    assert guw("Ajacɛ") == "adʒatʃɛ"


# ---------------------------------------------------------------------------
# ⟨p⟩ spells the labial-velar
# ---------------------------------------------------------------------------

def test_p_spells_the_labial_velar_stop():
    """Gbe has no plain /p/ outside loans, and ⟨p⟩ spells /k͡p/ — the gold's
    doublet ⟨pataki⟩ / ⟨kpataki⟩ transcribes both spellings the same way."""
    assert guw("pataki") == guw("kpataki") == "k͡pataki"


# ---------------------------------------------------------------------------
# Nasal vowels: written ⟨Vn⟩ only in the coda
# ---------------------------------------------------------------------------

def test_vowel_plus_coda_n_is_a_nasal_vowel():
    """⟨Vn⟩ in the coda writes a nasal vowel and the ⟨n⟩ is not a segment:
    ⟨xlan⟩ [xlã], ⟨Glɛnsi⟩ [ɡlɛ̃si], ⟨xɔntɔn⟩ [xɔ̃tɔ̃]."""
    assert guw("xlan") == "xlã"
    assert guw("Glɛnsi") == "ɡlɛ̃si"
    assert guw("xɔntɔn") == "xɔ̃tɔ̃"


def test_onset_n_does_not_nasalise_the_preceding_vowel():
    """An ⟨n⟩ that opens the next syllable is an ordinary /n/ and leaves the
    vowel before it oral: ⟨Ayɔnu⟩ [ajɔnũ], ⟨oklunɔ⟩ [oklunɔ̃] — in both the
    ⟨n⟩ survives and the vowel in front of it does not nasalise.  Reading
    ⟨an ɛn ɔn⟩ as unconditional digraphs nasalised that vowel and swallowed
    the ⟨n⟩ in both."""
    assert guw("Ayɔnu") == "ajɔnũ"
    assert guw("oklunɔ") == "oklunɔ̃"


def test_e_and_o_have_no_nasal_counterpart():
    """Gbe nasalises only /i u ɛ ɔ a/; /e o/ have no nasal counterparts, so a
    coda nasal after them survives as a consonant — ⟨ogongo⟩ [oɡonɡo] keeps
    its nasal where ⟨xɔntɔn⟩ loses it.  (The gold writes [oɡoŋɡo]: the place
    assimilation is real but not modelled here.)"""
    assert guw("ogongo") == "oɡonɡo"
    assert guw("xɔntɔn") == "xɔ̃tɔ̃"


def test_doubled_n_is_nasalisation_plus_onset_not_a_geminate():
    """⟨nn⟩ is not a long consonant: the first ⟨n⟩ nasalises the vowel before
    it and the second opens the next syllable — ⟨sunnu⟩ [sũnũ],
    ⟨kinnikinni⟩ [kĩnĩkĩnĩ]."""
    assert guw("sunnu") == "sũnũ"
    assert guw("kinnikinni") == "kĩnĩkĩnĩ"


def test_vowel_after_a_written_nasal_consonant_is_nasal():
    """None of ⟨m n ny⟩ spells an independent consonant phoneme before a nasal
    vowel — [m] and [n] are what /b/ and /ɖ/ become there, and [ɲ] is /j/
    there, in free variation with [j̃] — so a written nasal consonant entails
    a nasal nucleus: ⟨mi⟩ [mĩ], ⟨nyɔ⟩ [ɲɔ̃], ⟨nyikɔ⟩ [ɲĩkɔ]."""
    assert guw("mi") == "mĩ"
    assert guw("nyɔ") == "ɲɔ̃"
    assert guw("nyikɔ") == "ɲĩkɔ"


def test_post_nasal_nasalisation_spares_e_and_o():
    """The same five-vowel limit applies after a nasal consonant: ⟨hwenuxo⟩
    [ɣʷenuxo] keeps its ⟨e⟩ oral."""
    assert guw("hwenuxo").startswith("ɣʷe")


# ---------------------------------------------------------------------------
# The velar fricatives
# ---------------------------------------------------------------------------

def test_hw_is_the_voiced_labialised_velar_fricative():
    """⟨hw⟩ is the voiced partner of ⟨xw⟩: ⟨hwe⟩ [ɣʷe], ⟨ahwan⟩ [aɣʷã],
    against ⟨xwe⟩ [xʷe]."""
    assert guw("hwe") == "ɣʷe"
    assert guw("ahwan") == "aɣʷã"
    assert guw("xwe") == "xʷe"


def test_wh_is_the_nigerian_spelling_of_hw():
    """The Nigerian orthography writes the same segment ⟨wh⟩ — the gold's
    ⟨awhan⟩ and ⟨ahwan⟩ are one word, both [aɣʷã]."""
    assert guw("awhan") == guw("ahwan") == "aɣʷã"


def test_h_is_ambiguous_between_the_velar_fricatives_and_glottal():
    """⟨h⟩ is not resolvable from spelling: the gold writes it [h] (⟨hɔn⟩
    [hɔ̃]), [x] (⟨hoho⟩ [xoxo]) and [ɣ] (⟨hlɔnhlɔn⟩ [ɣlɔ̃ɣlɔ̃]), so all three
    readings stay reachable in the lattice rather than one being picked."""
    assert candidates("hɔn") == ["hɔ̃", "xɔ̃", "ɣɔ̃"]
    assert "xoxo" in candidates("hoho")


def test_d_is_ambiguous_because_the_nigerian_spelling_lacks_hooked_d():
    """The Benin alphabet contrasts ⟨d⟩ /d/ with ⟨ɖ⟩ /ɖ/; the Nigerian one has
    only ⟨d⟩ and uses it for both, so the gold's ⟨todaho⟩ and ⟨toɖaxo⟩ are one
    word.  The hooked-d reading has to stay reachable for the plain ⟨d⟩."""
    assert "aɖi" in candidates("adi")
    assert guw("toɖaxo") == "toɖaxo"


def test_r_is_the_trilled_realisation_of_l():
    """/l/ is realised as a trill after laminal alveolars, palato-alveolars
    and palatals, which is the only environment ⟨r⟩ is written in — the gold
    gives ⟨jrɛ⟩ as both [dʒɾɛ] and [dʒlɛ], so both stay reachable."""
    assert set(candidates("jrɛ")) >= {"dʒɾɛ", "dʒlɛ"}


# ---------------------------------------------------------------------------
# /j/ before a nasal vowel
# ---------------------------------------------------------------------------

def test_y_before_a_nasal_vowel_is_the_palatal_nasal():
    """Capo (1991) states that a [+nasal] vowel nasalises a preceding
    [-paired] consonant, "thereby creating the systematic phonetic nasal
    consonants [m n ɲ ...] from non-nasal [b ɖ l y w]".  ⟨y⟩ spells /j/, so
    ⟨yẹn⟩ — a nasal vowel written ⟨ẹ⟩ + coda ⟨n⟩ — is [ɲɛ̃], not [jɛ̃]."""
    assert guw("yẹn") == "ɲɛ̃"
    assert guw("yọn") == "ɲɔ̃"


def test_y_before_a_nasal_vowel_is_the_palatal_nasal_word_internally():
    """The same nasalisation applies to a non-initial /j/: ⟨oyin⟩ [oɲĩ],
    ⟨yinkọ⟩ [ɲĩkɔ]."""
    assert guw("oyin") == "oɲĩ"
    assert guw("yinkọ") == "ɲĩkɔ"


def test_y_before_an_oral_vowel_stays_a_glide():
    """The rule is conditioned by nasality and must not bleed elsewhere:
    ⟨y⟩ before an oral vowel is plain /j/."""
    assert guw("yovo").startswith("j")


def test_the_free_variant_of_the_palatal_nasal_is_not_modelled():
    """The Gun source records [ɲ] and [j̃] — a NASALISED glide, not a plain
    one — as free variants before a nasal vowel.  The spec emits the [ɲ]
    variant only; no reading of ⟨yẹn⟩ keeps an oral /j/."""
    assert all(not c.startswith("j") for c in candidates("yẹn"))


def test_y_before_e_or_o_plus_coda_n_does_not_nasalise():
    """/e o/ have no nasal counterpart in Gbe, so a coda ⟨n⟩ after them does
    not create the nasal-vowel environment the /j/-nasalisation rule keys
    on: ⟨yen⟩ and ⟨yon⟩ keep a plain glide, unlike ⟨yẹn⟩/⟨yọn⟩ above."""
    assert guw("yen").startswith("j")
    assert guw("yon").startswith("j")


# ---------------------------------------------------------------------------
# Labialised consonants
# ---------------------------------------------------------------------------

def test_kw_is_a_labialised_velar_stop():
    """Gbe writes a labialised consonant ⟨Cw⟩ — the spec already reads ⟨xw⟩
    and ⟨hw⟩ that way, and ⟨kw⟩ is the same convention: ⟨akwẹ⟩ [akʷɛ]."""
    assert guw("akwẹ") == "akʷɛ"
    assert guw("akwekwe") == "akʷekʷe"


def test_u_before_a_vowel_spells_the_same_labialisation():
    """⟨u⟩ before a vowel is the same labialisation spelt with a vowel
    letter — the gold's doublet ⟨akuẹ⟩ / ⟨akwẹ⟩ is one word, [akʷɛ]."""
    assert guw("akuẹ") == guw("akwẹ") == "akʷɛ"
    assert guw("azui") == "azʷi"


def test_u_not_before_a_vowel_is_an_ordinary_vowel():
    """The labialisation reading is conditioned on a following vowel: ⟨u⟩
    elsewhere is the vowel /u/."""
    assert guw("adu") == "adu"


def test_w_after_a_coda_nasal_stays_a_glide():
    """A ⟨w⟩ that opens a new morpheme after a coda ⟨n⟩ is not part of a
    labialised consonant: ⟨azọnwatọ⟩ keeps [w]."""
    assert "w" in guw("azọnwatọ")
    assert "ʷ" not in guw("azọnwatọ")
