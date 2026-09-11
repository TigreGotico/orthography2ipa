"""Zulu (isiZulu, ``zu``): clicks, implosives, penultimate length, syllabic ⟨m⟩.

Five facts from the Wikipedia Zulu phonology and Zulu language articles,
which are the spec's cited sources:

* the click letters ⟨c q x⟩ are bare [ǀ ǃ ǁ] and their slack-voiced and
  breathy-nasal series ⟨gc ngc⟩ carry the depressor's breathy release;
* ⟨b⟩ is the implosive /ɓ/ while ⟨bh⟩ is the plain slack-voiced /b/;
* ⟨k⟩ is read as the implosive /ɠ/, not as a plosive;
* stress is penultimate and is realised as vowel length, so the last vowel
  of a word is never long;
* the class 1/3 prefix ⟨um-⟩ has the syllabic nasal /m̩/, while the class 9
  prefix ⟨im-⟩ before a labial does not.

Whole transcriptions are pinned rather than substrings: penultimate length
and the implosives move segments all through the word, and a substring
assertion would pass on an output that got the rest of it wrong.
"""
from orthography2ipa import G2P


def _ipa(word: str) -> str:
    return G2P("zu").transcribe_word(word)


def test_click_letters_are_bare_clicks():
    """⟨c q x⟩ write the click alone, with no velar-closure symbol."""
    assert _ipa("cela") == "ǀeːla"
    assert _ipa("qala") == "ǃaːla"
    assert _ipa("xola") == "ǁoːla"


def test_aspirated_click_series():
    """⟨ch qh xh⟩ are the aspirated clicks."""
    assert _ipa("chaza") == "ǀʰaːza"
    assert _ipa("qhuba") == "ǃʰuːɓa"
    assert _ipa("xhasa") == "ǁʰaːsa"


def test_voiced_and_nasal_click_series_carry_the_depressor_release():
    """⟨gc⟩ [ɡǀʱ] and ⟨ngc⟩ [ŋǀʱ] against the plain nasal ⟨nc⟩ [ŋǀ]."""
    assert _ipa("amagcino") == "amaɡǀʱiːno"
    assert _ipa("ingcebo") == "iŋǀʱeːɓo"
    assert _ipa("ingqondo") == "iŋǃʱoːndo"
    assert _ipa("ingxenye") == "iŋǁʱeːɲe"
    assert _ipa("incwadi") == "iŋǀwaːdi"


def test_b_is_implosive_and_bh_is_the_plain_plosive():
    """The ⟨b⟩/⟨bh⟩ pair is a voicing-quality contrast, not aspiration."""
    assert _ipa("ubaba") == "uɓaːɓa"
    assert _ipa("ibhasi") == "ibaːsi"
    assert "bʱ" not in _ipa("ibhasi")


def test_k_is_read_as_the_implosive():
    """⟨k⟩ is the implosive /ɠ/; ⟨kh⟩ stays the aspirated plosive."""
    assert _ipa("dabuka") == "daɓuːɠa"
    assert _ipa("ukudla") == "uɠuːɮa"
    assert _ipa("ukuthanda") == "uɠutʰaːnda"


def test_lateral_obstruents_and_the_kl_affricate():
    """⟨hl⟩ [ɬ], ⟨dl⟩ [ɮ], ⟨kl⟩ [kx], and ⟨ndl⟩ as one multigraph."""
    assert _ipa("mhla") == "m̩ɬa"
    assert _ipa("indlu") == "iːnɮu"
    assert _ipa("ibandla") == "iɓaːnɮa"
    assert _ipa("iklabishi") == "ikxaɓiːʃi"


def test_h_and_hh_are_distinct():
    """⟨h⟩ is [h] and the doubled ⟨hh⟩ is the breathy [ɦ]."""
    assert _ipa("ihansi") == "ihaːnsi"
    assert _ipa("ihhashi") == "iɦaːʃi"


def test_palatal_nasal_before_the_affricates():
    """⟨nj⟩ [ɲdʒ] and ⟨ntsh⟩ [ɲtʃ] carry the homorganic palatal nasal."""
    assert _ipa("inja") == "iːɲdʒa"
    assert _ipa("intshonalanga") == "iɲtʃonalaːŋɡa"


def test_nz_is_not_hardened():
    """Zulu ⟨nz⟩ is [nz], unlike the Xhosa cognate spelling's [ndz]."""
    assert _ipa("amanzi") == "amaːnzi"


def test_penultimate_syllable_carries_the_length():
    """Stress is penultimate and is realised as length, never on the last vowel."""
    assert _ipa("amabele") == "amaɓeːle"
    assert _ipa("umuntu") == "umuːntu"
    assert not _ipa("amabele").endswith("ː")
    assert not _ipa("umuntu").endswith("ː")


def test_um_prefix_nasal_is_syllabic_but_im_prefix_nasal_is_not():
    """⟨um-⟩ reduces older /mu-/ to /m̩/; the class 9 ⟨im-⟩ stays prenasalised."""
    assert _ipa("umfana") == "um̩faːna"
    assert _ipa("umbala") == "um̩ɓaːla"
    assert _ipa("imfene") == "imfeːne"
    assert _ipa("imbali") == "imbaːli"


def test_um_prefix_mb_and_mbh_series_do_not_shadow_each_other():
    """⟨mb⟩ (implosive) and ⟨mbh⟩ (plain) share the phoneme string "mb", so
    the two ZU_UM_PREFIX_SYLLABIC_MB/_MBH allophone rules must key on the
    ⟨grapheme⟩ that produced it, not just the phoneme: both classes have to
    resolve correctly at once, or one of the rules is silently dead."""
    assert _ipa("umbala") == "um̩ɓaːla"
    assert _ipa("umbhali") == "um̩baːli"
    assert _ipa("umbhede") == "um̩beːde"


def test_syllabic_m_only_before_a_consonant():
    """⟨m⟩ before a vowel is a plain onset; before a consonant it is a syllable."""
    assert _ipa("umuntu") == "umuːntu"
    assert _ipa("kamnandi") == "ɠam̩naːndi"
    assert _ipa("umklomelo") == "um̩kxomeːlo"
