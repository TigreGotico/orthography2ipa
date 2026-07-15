"""Proto-Maghrebi Arabic (``ar-x-maghrebi``): the shared phonology of the
Maghrebi group, and — just as important for a GROUPING (glue) node — the
reflexes that are deliberately NOT asserted group-wide because the literature
treats them as sedentary-vs-Bedouin isoglosses.

``ar-x-maghrebi`` is the grouping node above Moroccan (ar-MA), Tunisian (ar-TN),
Algerian (ar-DZ), Libyan (ar-LY) and Ḥassāniyya (ar-MR). It declares only what
is shared across the whole group and serves as the data-inheritance root the
leaves build on. Every claim below is isolated on a real Arabic word and cited:

* Watson, J.C.E. (2002), *The Phonology and Morphology of Arabic*, OUP —
  p.13 (unstressed-vowel deletion → clusters), p.15 (sedentary interdental
  merger), p.16 (Maghribi ǧīm = /ž/ [ʒ]), p.17 (*q maintained sedentary /
  /ɡ/ Bedouin);
* Guerrero, J. (2019), "Reflexes of Old Arabic */ǧ/ in the Maghrebi Dialects",
  *Arabica* 66(1-2):137-193 — /ʒ/ is by far the most common *ǧ reflex across
  Libya, Tunisia, Mauritania and Morocco; /dʒ/ retained by pre-Hilali sedentary
  north-Algerian dialects;
* Guerrero, J. (2021), "On Interdental Fricatives in the First-Layer Dialects of
  Maghrebi Arabic", *JAAL* 13(2):288-308 — interdental LOSS is not a pan-Maghrebi
  hallmark; the fricatives are retained in many first-layer dialects;
* Souag, L. (2005), "Notes on the Algerian Arabic Dialect of Dellys", *EDNA*
  9:151-180 — a sedentary Algerian dialect with qāf /q/ that also RETAINS the
  interdentals.

Expectations are written with the engine's own stress marks (Arabic stress is
quantity-sensitive and declared on the spec).
"""
from orthography2ipa import transcribe, get
from orthography2ipa.types import QualityTier


NODE = "ar-x-maghrebi"


# ─── The group node is a research-tier glue node with the right sources ─────

def test_is_research_tier_glue_node_with_primary_sources():
    """The node is raised to research tier and cites the primary Maghrebi
    dialectology it rests on (Watson 2002, Guerrero 2019/2021, Souag 2005)."""
    spec = get(NODE)
    assert spec.quality is QualityTier.RESEARCH
    ids = {s.id for s in spec.sources}
    assert {"watson2002", "guerrero2019", "guerrero2021", "souag2005"} <= ids


def test_notes_document_the_glue_node_boundary():
    """A grouping node must say what it does NOT own: qāf, the interdental
    merger and imāla strength split within the group and are left to the
    leaves (glue-node rule; Guerrero 2021, Souag 2005)."""
    n = get(NODE).notes.lower()
    assert "not group-wide" in n or "not asserted group-wide" in n
    for token in ("qāf", "interdental", "imāla", "leaf"):
        assert token.lower() in n


# ─── SHARED feature #1: ǧīm ج → /ʒ/ (voiced postalveolar fricative) ─────────

def test_jim_is_the_fricative_zh_not_the_affricate():
    """Maghrebi ǧīm ج is the voiced postalveolar FRICATIVE /ʒ/ with no initial
    occlusive element (Watson 2002:16; Guerrero 2019 — /ʒ/ the most common
    reflex across Libya, Tunisia, Mauritania, Morocco): جَبَل 'mountain' →
    [ʒ...], ثَلْج 'snow/ice' → [...ʒ]."""
    assert get(NODE).graphemes["ج"][0] == "ʒ"
    assert transcribe("جَبَل", NODE) == "ˈʒabal"
    assert transcribe("ثَلْج", NODE).endswith("ʒ")


def test_jim_keeps_the_affricate_as_a_secondary_candidate():
    """The pre-Hilali sedentary dialects of northern Algeria (Tlemcen, Algiers,
    Constantine…) keep the affricate /dʒ/ (Guerrero 2019), so it stays as the
    node's second-ranked ǧīm candidate rather than being discarded."""
    assert get(NODE).graphemes["ج"][:2] == ["ʒ", "dʒ"]


# ─── SHARED feature #2: short-vowel syncope → consonant clusters ────────────

def test_short_vowels_may_delete_licensing_clusters():
    """The defining Maghrebi trait: unstressed short vowels delete (schwa in
    weak positions), yielding consonant clusters — CA kataba → MA ktəb (Watson
    2002:13). The node licenses this by giving every short vowel an empty
    (deletion) candidate alongside its full value."""
    allo = get(NODE).allophones
    for v in ("a", "i", "u"):
        assert "" in allo[v], f"short /{v}/ must license a deletion candidate"


# ─── SHARED feature #3: sun-letter assimilation is UNCHANGED ────────────────

def test_sun_letter_assimilation_is_inherited_unchanged():
    """The article ل assimilates to a following coronal (ʔidġām aš-šamsiyya)
    exactly as in Classical/MSA — a pan-Arabic process the node does not
    override: الشَّمْس 'the sun' → [aʃˈʃams] (assimilated), while the moon
    letter in الْقَمَر 'the moon' → [ˈalqamar] keeps the /l/."""
    assert transcribe("الشَّمْس", NODE) == "aʃˈʃams"
    assert transcribe("الْقَمَر", NODE) == "ˈalqamar"


# ─── NOT group-wide #1: qāf — sedentary /q/ default, split left to leaves ───

def test_qaf_default_is_q_and_split_is_left_to_leaves():
    """qāf is the sedentary/pre-Hilali /q/ at the inheritance root (Souag 2005,
    Dellys /q/), NOT a claim that the whole group is /q/: the /q/~/ɡ/ split is
    Bedouin-vs-sedentary (Watson 2002:17) and belongs to the leaves. قَلْب
    'heart' → [ˈqalb]; سُوق 'market' → [ˈsuːq]."""
    assert get(NODE).graphemes["ق"] == ["q"]
    assert transcribe("قَلْب", NODE) == "ˈqalb"
    assert transcribe("سُوق", NODE) == "ˈsuːq"


# ─── NOT group-wide #2: interdental merger is a sedentary koiné default ─────

def test_interdental_merger_is_the_sedentary_default_not_a_group_claim():
    """The interdental → stop merger (ث→[t], ذ→[d], ظ/ض→[dˤ]) is the sedentary
    koiné default the urban leaves rely on, NOT a Maghrebi hallmark: Guerrero
    (2021) shows the fricatives are retained across many first-layer dialects
    and Souag (2005) documents sedentary Dellys keeping them. ذَهَب 'gold' →
    [ˈdahab]; ظَهْر 'back' → [ˈdˤɑhr]; ثَوْب 'garment' → [ˈtawb]."""
    assert transcribe("ذَهَب", NODE) == "ˈdahab"
    assert transcribe("ظَهْر", NODE) == "ˈdˤɑhr"
    assert transcribe("ثَوْب", NODE) == "ˈtawb"


def test_emphatics_dad_and_dha_merge_to_dˤ():
    """Both ض and ظ surface as the emphatic stop /dˤ/ at the node level
    (Watson 2002:15, sedentary merger): ضَرَب 'he hit' → [ˈdˤɑrab]."""
    assert get(NODE).graphemes["ض"] == ["dˤ"]
    assert get(NODE).graphemes["ظ"] == ["dˤ"]
    assert transcribe("ضَرَب", NODE) == "ˈdˤɑrab"


# ─── Regression pin: the glue-node upgrade must not move ar-MA silently ─────

def test_moroccan_leaf_output_is_unchanged_by_the_node_upgrade():
    """ar-MA inherits from this node; raising the node to research tier changed
    only prose/metadata, so the Moroccan leaf's transcriptions must be
    byte-identical (no silent, uncited downstream change)."""
    assert transcribe("جَدِيد", "ar-MA") == "ʒaˈdiːd"
    assert transcribe("كِتَاب", "ar-MA") == "kiˈtaːb"
    assert transcribe("الشَّمْس", "ar-MA") == "aʃˈʃams"
