"""Saudi Arabic — Najdi (ars) and Hejazi (acw) dialect behaviour.

Every expectation here is tied to a citation carried in the spec's own
``sources``:

* Ingham, B. (1994) *Najdi Arabic: Central Arabian*, John Benjamins.
* Al Mahmoud, M.S. (2020) "A Constraint-based Analysis of Velar Affrication in
  Najdi vs. Hijazi Arabic", *Education and Linguistics Research* 6(2), 62-72.
* Omar, M.K. (1975) *Saudi Arabic, Urban Hijazi Dialect*; Abdoh, E. (2010)
  *Urban Meccan Arabic*.

Input is FULLY DIACRITIZED, which is the specs' stated contract.
"""
import pytest

from orthography2ipa import G2P
from orthography2ipa.inventory import dead_allophone_rules

NAJD = G2P("ar-SA-x-najd")
HEJAZ = G2P("ar-SA-x-hejaz")


@pytest.mark.parametrize("lang", ["ar-SA-x-najd", "ar-SA-x-hejaz"])
def test_no_dead_allophone_rules(lang):
    """Every declared rule targets a phoneme the spec can actually produce."""
    assert dead_allophone_rules(G2P(lang).spec) == ()


# ── Hejazi: monophthongization ─────────────────────────────────────────────
# Omar 1975; Abdoh 2010: inherited /aj aw/ are [eː oː].
@pytest.mark.parametrize("word,expected,why", [
    ("بَيْت", "ˈbeːt", "bayt → beːt, via the ⟨َي⟩ digraph's /aj/ atom"),
    ("لَوْن", "ˈloːn", "lawn → loːn, via the ⟨َو⟩ digraph's /aw/ atom"),
    # These two are the reason ar-SA-x-hejaz spells ⟨يَوْ⟩/⟨وَيْ⟩ out in
    # `graphemes`: the inherited `ar` onset digraphs يَ→/ja/ and وَ→/wa/ eat the
    # fatha first, so no /aw/ or /aj/ atom is ever formed for HEJ_MONO_* to
    # rewrite, and these words used to come out *[jawm] and *[wajn].
    ("يَوْم", "ˈjoːm", "yawm → joːm (the atom never forms; spelled out)"),
    ("وَيْن", "ˈweːn", "wayn → weːn (the atom never forms; spelled out)"),
    ("يَوْمَيْن", "joːˈmeːn", "both environments in one word"),
    ("الْيَوْمَ", "alˈjoːma", "and under the definite article"),
])
def test_hejazi_monophthongization(word, expected, why):
    assert HEJAZ.transcribe_word(word) == expected, why


@pytest.mark.parametrize("word,expected,why", [
    # The explicit sukun in the ⟨يَوْ⟩/⟨وَيْ⟩ keys is load-bearing: where the waw
    # carries its OWN vowel there is no diphthong and nothing to monophthongize.
    ("حَيَوَان", "ħajaˈwaːn", "ħayawaːn: waw is a consonant with its own fatha"),
    ("يَوَدّ", "jaˈwadd", "yawadd: likewise, no /aw/ here"),
])
def test_hejazi_monophthong_rule_does_not_overreach(word, expected, why):
    assert HEJAZ.transcribe_word(word) == expected, why


def test_hejazi_has_no_velar_affrication():
    """Al Mahmoud 2020: HA keeps [k] and [ɡ] where NA alternates with [ts]/[dz]."""
    assert HEJAZ.transcribe_word("كِيس") == "ˈkiːs"
    assert HEJAZ.transcribe_word("دِيك") == "ˈdiːk"
    assert HEJAZ.transcribe_word("قَرِيب") == "ɡaˈriːb"  # qaf → [ɡ], never [dz]


# ── Najdi: velar affrication ───────────────────────────────────────────────
@pytest.mark.parametrize("word,expected,why", [
    ("كِيس", "ˈtsiːs", "Al Mahmoud 2020 ex. 1: /kis/ → [tsis] before front /i/"),
    ("دِيك", "ˈdiːts", "ex. 2: /dik/ → [dits] after front /iː/"),
    ("قِيمَة", "ˈdziːma", "ex. 10-13: the qaf reflex /ɡ/ → [dz] before front /iː/"),
    ("كِتَاب", "tsiˈtaːb", "affrication is not restricted to monosyllables (exx. 6-9)"),
])
def test_najdi_affrication_fires_on_front_vowels(word, expected, why):
    assert NAJD.transcribe_word(word) == expected, why


@pytest.mark.parametrize("word,expected,why", [
    ("قُرُود", "ɡuˈruːd", "ex. 22: back vowel blocks affrication"),
    ("فَوْق", "ˈfawɡ", "ex. 19: /foq/ → [foɡ], *[fodz]"),
    ("شَوْك", "ˈʃawk", "ex. 15: /ʃok/ → [ʃok], *[ʃots]"),
    ("كُل", "ˈkul", "ex. 16: /kʊl/ → [kʊl], *[tsʊl]"),
    # The fatha is the honest gap, not an oversight: Al Mahmoud §3.1 shows it
    # splits lexically — dog is front [tsɛlb] but heart is central [ɡʌlb] — and
    # the two are written with the SAME fatha. A rule that affricated كلب would
    # also affricate قلب, which the informant rejects; so neither is affricated.
    ("قَلْب", "ˈɡalb", "§3.1: /qʌlb/ 'heart' → [ɡʌlb], central vowel, no [dz]"),
    ("كَلْب", "ˈkalb", "§3.1: كلب is [tsɛlb] but the fatha cannot say so — under-applied"),
])
def test_najdi_affrication_is_blocked_or_undecidable(word, expected, why):
    assert NAJD.transcribe_word(word) == expected, why


def test_najdi_affrication_gap_is_tautosyllabic_not_adjacent():
    """KNOWN GAP, asserted so it is visible rather than forgotten.

    Al Mahmoud 2020 exx. 3 and 11: /ʕɪlk/ → [ʕɪlts] and /rɪzq/ → [rɪzdz]. The
    trigger is a front vowel ANYWHERE IN THE SYLLABLE, but the rule schema can
    only condition on the immediately neighbouring phoneme, so a coda velar
    separated from its nucleus by another consonant is missed. Expressing this
    needs a "my syllable's nucleus is front" predicate the schema does not have.
    """
    assert NAJD.transcribe_word("عِلْك") == "ˈʕilk"    # literature: [ʕilts]
    assert NAJD.transcribe_word("رِزْق") == "ˈrizɡ"    # literature: [rizdz]


# ── Najdi: the other declared features ─────────────────────────────────────
def test_najdi_gahawa_syndrome():
    """Ingham 1994 pp. 15-16: epenthetic /a/ after a coda guttural."""
    assert NAJD.transcribe_word("قَهْوَة") == "ˈɡahawa"   # gahwa → gahawa
    assert NAJD.transcribe_word("لَحْم") == "ˈlaħam"      # laħm → laħam
    assert NAJD.transcribe_word("نَخْل") == "ˈnaxal"


def test_najdi_interdentals_and_dad_dha_merger():
    """Ingham 1994: interdentals preserved; ض/ظ neutralise to [ðˤ]."""
    assert NAJD.transcribe_word("ثَلَاثَة") == "θaˈlaːθa"
    assert NAJD.transcribe_word("ضَرَبَ") == "ˈðˤɑraba"   # ض → [ðˤ], not [dˤ]
    assert NAJD.transcribe_word("ظَهْر") == "ˈðˤɑhar"     # ظ → [ðˤ] (+ gahawa)


def test_najdi_keeps_diphthongs_unlike_hejazi():
    """Najdi does not monophthongize: bayt stays [bajt] where Hejazi has [beːt]."""
    assert NAJD.transcribe_word("بَيْت") == "ˈbajt"
    assert HEJAZ.transcribe_word("بَيْت") == "ˈbeːt"


def test_qaf_is_g_in_both():
    assert NAJD.transcribe_word("قَلْب") == "ˈɡalb"
    assert HEJAZ.transcribe_word("قَلْب") == "ˈɡalb"


def test_hejazi_interdentals_merge_to_stops():
    """Omar 1975: the urban koine has ث→/t/, ذ→/d/, ض/ظ→/dˤ/."""
    assert HEJAZ.transcribe_word("ثَلَاثَة") == "taˈlaːta"
    assert HEJAZ.transcribe_word("ذَهَب") == "ˈdahab"
    assert HEJAZ.transcribe_word("ظَهْر") == "ˈdˤɑhr"
