"""Saudi Arabic — the newer leaves beyond Najdi/Hejazi, and the facts that keep
them apart.

Saudi Arabia has no single dialect: its varieties split across the Najdi,
Hejazi, Gulf and Southwestern groups, so there is deliberately **no** ``ar-SA``
umbrella node (lang-code accuracy: null beats wrong). This module covers the
three leaves that fill out that spread:

* **ar-SA-x-qassim** — Qassimi, the Qaṣīm sub-variety of Najdi. Deepest source:
  Alhoody, M.M.A. (2019) *Phonological adaptation of English loanwords into
  Qassimi Arabic* (PhD, Newcastle), §3.1.2-3.1.4, pp.41-43; Al-Rojaie, Y. (2013)
  "Regional dialect levelling in Najdi Arabic: the deaffrication of [ts] in the
  Qaṣīmī dialect", *Language Variation and Change* 25(1):43-63.
* **ar-SA-x-rijal-alma** — Rijāl Almaʿ (SW ʿAsīr/Tihāmah), which preserves the
  archaic **lateral emphatics**. Watson, J.C.E. & Al-Azraqi, M. (2011) "Lateral
  fricatives and lateral emphatics in southern Saudi Arabia and Mehri", *PSAS*
  41:425-432, pp.427-428; Asiri, Y.M. (2009) PhD, Salford; Al-Azraqi, M. (2010)
  "The ancient Ḍād in southwest Saudi Arabia", *Arabica* 57:57-67.
* **ar-SA-x-sharqiyya** — Eastern Province (al-Hasa/Qatif), a Gulf dialect.
  Al-Taisan, H. (2022) PhD, Essex; Johnstone, T.M. (1967) *Eastern Arabian
  Dialect Studies*; Holes, C. (2004) *Modern Arabic*.

Input is FULLY DIACRITIZED, the specs' stated contract.
"""
import pytest

from orthography2ipa import G2P, get
from orthography2ipa.inventory import dead_allophone_rules, phoneme_inventory

QAS = G2P("ar-SA-x-qassim")
RIJ = G2P("ar-SA-x-rijal-alma")
SHQ = G2P("ar-SA-x-sharqiyya")


@pytest.mark.parametrize("lang", ["ar-SA-x-qassim", "ar-SA-x-rijal-alma", "ar-SA-x-sharqiyya"])
def test_no_dead_allophone_rules(lang):
    """Every declared/inherited rule targets a phoneme the spec can produce."""
    assert dead_allophone_rules(G2P(lang).spec) == ()


# ── Ancestry: each leaf hangs off the RIGHT group, and there is no ar-SA ──────
def test_leaves_parent_the_correct_group():
    assert get("ar-SA-x-qassim").parent == "ar-SA-x-najd"        # Najdi sub-variety
    assert get("ar-SA-x-rijal-alma").parent == "ar-x-peninsular"  # SW archaic type
    assert get("ar-SA-x-sharqiyya").parent == "ar-x-gulf"         # Gulf type


def test_no_ar_sa_umbrella_node():
    """Saudi dialects do not form a pan-Saudi phonological group, so there is no
    real ``ar-SA`` node (Ingham 1994; Prochazka 1988). Requesting the bare
    country code falls BACK to a leaf rather than resolving a genuine umbrella
    spec — the resolved code is never ``ar-SA`` itself."""
    assert get("ar-SA").code != "ar-SA"
    assert "no ar-sa umbrella" in get("ar-SA-x-najd").notes.lower()


# ── Qassimi: monophthongization is the delta from central Najdi ──────────────
@pytest.mark.parametrize("word,expected,why", [
    ("بَيْت", "ˈbeːt", "Alhoody 2019:42 ex.18: /bajt/ → [beːt] — Qassim monophthongizes"),
    ("لَوْن", "ˈloːn", "Alhoody 2019:42 ex.18: /lawn/ → [loːn]"),
    ("زَيْن", "ˈzeːn", "/zajn/ → [zeːn]"),
])
def test_qassimi_monophthongizes_where_najdi_keeps_diphthong(word, expected, why):
    assert QAS.transcribe_word(word) == expected, why
    # the central-Najdi parent keeps the diphthong — this is the discriminator
    assert G2P("ar-SA-x-najd").transcribe_word(word) != expected


@pytest.mark.parametrize("word,expected,why", [
    ("كِيس", "ˈtsiːs", "Alhoody 2019:42 (Al-Rojaie 2013:43): /k/ → [ts] before front vowel"),
    ("قِيمَة", "ˈdziːma", "the qaf reflex /ɡ/ → [dz] before front /iː/"),
])
def test_qassimi_inherits_najdi_velar_affrication(word, expected, why):
    """The dental affricate is the salient Qaṣīmī shibboleth (Al-Rojaie 2013);
    it is inherited unchanged from the Najdi parent, which already emits it."""
    assert QAS.transcribe_word(word) == expected, why


def test_qassimi_qaf_merger_and_gahawa_inherited():
    assert QAS.transcribe_word("قَال") == "ˈɡaːl"          # qaf → [ɡ] (Alhoody 2019:41)
    assert QAS.transcribe_word("ضَرَبَ") == "ˈðˤɑraba"      # ض/ظ → [ðˤ], /dˤ/ lost (p.41)
    assert QAS.transcribe_word("ظَهْر") == "ˈðˤɑhar"        # ظ → [ðˤ] (+ gahawa)
    assert QAS.transcribe_word("قَهْوَة") == "ˈɡahawa"      # gahawa syndrome (Ingham 1994)
    assert QAS.transcribe_word("ثَلَاثَة") == "θaˈlaːθa"    # ث retained /θ/


# ── Rijāl Almaʿ: the archaic lateral emphatics, kept DISTINCT ────────────────
def test_rijal_alma_dad_is_a_voiced_lateral_emphatic():
    """Watson & Al-Azraqi 2011:428; Asiri 2009: *ḍ (ض) → voiced lateralized
    pharyngealized fricative [ɮˤ], the sound that made Arabic lughat al-ḍād."""
    assert RIJ.transcribe_word("ضَرَبَ") == "ˈɮˤaraba"
    assert RIJ.transcribe_word("ضَان") == "ˈɮˤaːn"
    assert RIJ.transcribe_word("أَرْض") == "ˈʔarɮˤ"


def test_rijal_alma_dha_is_a_voiceless_lateral_emphatic():
    """Watson & Al-Azraqi 2011:428: *ẓ (ظ) → VOICELESS lateralized pharyngealized
    fricative [ɬˤ] — and it is kept DISTINCT from *ḍ, which every other modern
    dialect merges."""
    assert RIJ.transcribe_word("ظَهْر") == "ˈɬˤahr"
    assert RIJ.transcribe_word("ظِل") == "ˈɬˤil"
    # the *ḍ/*ẓ contrast: ض is voiced [ɮˤ], ظ is voiceless [ɬˤ]
    assert RIJ.transcribe_word("ضَرَبَ")[1] == "ɮˤ"[0]
    assert RIJ.transcribe_word("ظَهْر")[1] == "ɬˤ"[0]


def test_rijal_alma_is_qaf_retaining_and_interdental_keeping():
    """The southwestern highland/Tihāmah type is conservative: qaf stays [q]
    (NOT the Najdi/Bedouin [ɡ]), interdentals stay (Asiri 2009)."""
    assert RIJ.transcribe_word("قَلْب") == "ˈqalb"
    assert RIJ.transcribe_word("ثَلَاثَة") == "θaˈlaːθa"


def test_rijal_alma_lateral_emphatics_are_in_the_inventory():
    """A TTS frontend must have [ɮˤ] and [ɬˤ] in its embedding table; the
    inventory-closure derivation has to surface them because the spec emits
    them."""
    inv = phoneme_inventory(RIJ.spec)
    assert "ɮˤ" in inv
    assert "ɬˤ" in inv


# ── Eastern Province (Sharqiyya): Gulf phonology, affricate jīm ──────────────
def test_sharqiyya_jim_is_the_affricate():
    """Al-Taisan 2022: Hasawi jīm is /ʤ/ throughout (inventory p.12 and every
    example); the *ǧīm → [j] glide-lenition is only *cited* for other Northern
    Arabian dialects, never attested in Hasawi. In the Gulf sect isogloss [dʒ]
    is the Šiʿi Baḥārna reflex (the majority in al-Qaṭīf/al-Hasa) while [j] is
    the Sunni ʕArab/Dawāsir reflex (Holes 1980/2016, in Alaodini 2019:94). So
    the sedentary Eastern leaf has [dʒ] primary; [j] moves to ar-SA-x-dawasir."""
    assert SHQ.transcribe_word("جَمَل") == "ˈdʒamal"
    assert SHQ.transcribe_word("جِيب") == "ˈdʒiːb"


def test_dawasir_jim_is_the_traditional_glide():
    """Alaodini 2019: the Dawāsir (Sunni, Najdi-origin, Dammam) carry the
    traditional [j] reflex acquired under Bahraini Sunni prestige — the mirror
    image of the sedentary Baḥārna [dʒ], and receding back toward [dʒ]."""
    DAW = G2P("ar-SA-x-dawasir")
    assert DAW.transcribe_word("جَمَل") == "jamal"
    assert DAW.transcribe_word("جِيب") == "jiːb"


def test_sharqiyya_is_gulf_type():
    """Al-Taisan 2022; Prochazka 1988: qaf → [ɡ], kaf affricates to [tʃ] before a
    front vowel, interdentals retained — Eastern Saudi patterns Gulf, not Najd."""
    assert SHQ.transcribe_word("قَلْب") == "ˈɡalb"          # qaf → [ɡ] (Al-Taisan 2022:17)
    assert SHQ.transcribe_word("كِيس") == "ˈtʃiːs"          # GULF_K_AFFRICATION before front /iː/
    assert SHQ.transcribe_word("كَلْب") == "ˈkalb"          # no affrication before /a/
    assert SHQ.transcribe_word("ثَلَاثَة") == "θaˈlaːθa"    # interdental retained
