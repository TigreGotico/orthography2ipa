"""Proto-Mashriqi Arabic (``ar-x-mashriqi``): the shared phonology of the
Eastern group, and — just as important for a GROUPING (glue) node — the
reflexes that are deliberately NOT asserted group-wide because the literature
treats them as leaf-level (bedouin-vs-sedentary or city-by-city) isoglosses.

``ar-x-mashriqi`` is the grouping node above Egyptian (ar-EG), Sudanese
(ar-SD), the West-Sudanic chain (ar-TD → ar-NG), Mesopotamian ar-IQ /
ar-IQ-x-qeltu and the Levantine subtree (ar-x-levantine → ar-SY/ar-LB/ar-JO/
ar-PS). It declares only what is shared across the whole Eastern group and
serves as the data-inheritance root the leaves build on. Every claim below is
isolated on a real Arabic word and cited:

* Watson, J.C.E. (2002), *The Phonology and Morphology of Arabic*, OUP —
  p.9 (East/West split: the West reduces the /a i u/ triad and deletes
  unstressed vowels — Moroccan smin vs Cairene simīn — while the East retains
  short vowels and trochaic stress; same page: voiced qāf and interdental
  preservation are BEDOUIN features, an axis that crosscuts geography),
  p.16 (§2.1.6, the four-way ǧīm reflex geography inside the East),
  p.17 (§2.1.9, the three-way qāf reflex geography inside the East; learned
  words keep /q/ even in ʔ-dialects: il-qurʔān, qarn, qarya);
* Versteegh, K. (2014), *The Arabic Language*, 2nd ed., Edinburgh UP — the
  handbook East/West primary split (cited as reported);
* Holes, C. (2004), *Modern Arabic*, Georgetown UP — sedentary/Bedouin reflex
  distributions (as reported via Watson 2002:16-17, citing Holes 1995:59-61).

Expectations are written with the engine's own stress marks (Arabic stress is
quantity-sensitive and declared on the spec).
"""
from orthography2ipa import transcribe, get
from orthography2ipa.types import QualityTier


NODE = "ar-x-mashriqi"


# ─── The group node is a research-tier glue node with the right sources ─────

def test_is_research_tier_glue_node_with_primary_sources():
    """The node is raised to research tier and cites the dialectology it
    rests on (Watson 2002 page-verified; Versteegh 2014 and Holes 2004 as
    reported)."""
    spec = get(NODE)
    assert spec.quality is QualityTier.RESEARCH
    ids = {s.id for s in spec.sources}
    assert {"watson2002", "versteegh2014", "holes2004"} <= ids


def test_notes_document_the_glue_node_boundary():
    """A grouping node must say what it does NOT own: the qāf, ǧīm and
    interdental reflexes split within the Eastern group (Watson 2002:9,
    16-17) and are left to the leaves (glue-node rule)."""
    n = get(NODE).notes.lower()
    assert "not group-wide" in n or "not asserted group-wide" in n
    for token in ("qāf", "ǧīm", "interdental", "leaf", "leaves"):
        assert token.lower() in n


# ─── SHARED feature #1: short-vowel retention (vs Maghrebi collapse) ────────

def test_short_vowels_are_retained_not_deleted():
    """The defining Eastern trait relative to Maghrebi: the /a i u/ triad is
    retained and unstressed vowels are not deleted — Cairene simīn vs
    Moroccan smin, baṛṛa vs bṛṛa (Watson 2002:9). The node licenses NO
    deletion candidates for the short vowels (contrast ar-x-maghrebi, whose
    a/i/u each license Ø)."""
    allo = get(NODE).allophones
    for v in ("a", "i", "u"):
        assert "" not in allo.get(v, []), (
            f"short /{v}/ must not license deletion on the Eastern node"
        )
    # the same word that collapses in the Maghreb keeps its vowels here
    assert transcribe("كِتَاب", NODE) == "kiˈtaːb"
    assert transcribe("مَدْرَسَة", NODE) == "ˈmadrasa"


def test_trochaic_type_stress_cascade_is_declared():
    """Watson 2002:9: the East has trochaic word stress ('katab, not the
    western ka'tab). The node declares the quantity-sensitive Eastern
    cascade: superheavy final > heavy penult > antepenult."""
    s = get(NODE).stress
    assert s is not None and s.quantity_sensitive
    assert transcribe("يَكْتُب", NODE) == "ˈjaktub"   # antepenult-type
    assert transcribe("جَدِيد", NODE) == "dʒaˈdiːd"   # superheavy final


# ─── SHARED feature #2: the Classical lateral ḍād is gone ───────────────────

def test_dad_is_the_pharyngealized_stop_not_the_lateral():
    """ض is /dˤ/ across the whole Eastern group; Sibawayh's lateral fricative
    ɮˤ survives only marginally outside it (Watson 2002:16 fn.). ضَرَب 'he
    hit' → [ˈdˤɑrab]."""
    assert get(NODE).graphemes["ض"] == ["dˤ"]
    assert get(NODE).allophones["ɮˤ"] == ["dˤ"]
    assert transcribe("ضَرَب", NODE) == "ˈdˤɑrab"


# ─── SHARED feature #3: sun-letter assimilation is UNCHANGED ────────────────

def test_sun_letter_assimilation_is_inherited_unchanged():
    """The article ل assimilates to a following coronal (ʔidġām
    aš-šamsiyya) exactly as in Classical/MSA — a pan-Arabic process the node
    does not override: الشَّمْس → [aʃˈʃams]; moon-letter الْقَمَر keeps /l/."""
    assert transcribe("الشَّمْس", NODE) == "aʃˈʃams"
    assert transcribe("الْقَمَر", NODE) == "ˈalqamar"


# ─── NOT group-wide #1: qāf splits three ways inside the group ──────────────

def test_qaf_default_is_q_and_split_is_left_to_leaves():
    """*q is /ʔ/ in Cairo and the urban Levant, /ɡ/ in Bedouin/Sudanic and
    gilit Iraqi, and maintained /q/ in qeltu (Watson 2002:17); the voiced
    reflex is a Bedouin feature crosscutting geography (Watson 2002:9). So
    the node states no group value: bare /q/ stays as the inheritance-root
    default and the leaves diverge — as they in fact do."""
    assert get(NODE).graphemes.get("ق", ["q"]) == ["q"] or "ق" not in get(NODE).graphemes
    assert transcribe("قَلْب", NODE) == "ˈqalb"
    # the leaves own the reflex: Cairo ʔ, Sudan g, qeltu q
    assert transcribe("قَلْب", "ar-EG") == "ˈʔalb"
    assert transcribe("قَلْب", "ar-SD") == "ˈɡalb"
    assert transcribe("قَلْب", "ar-IQ-x-qeltu") == "ˈqalb"


# ─── NOT group-wide #2: ǧīm splits four ways inside the group ───────────────

def test_jim_is_not_overridden_and_leaves_diverge():
    """Watson 2002:16: ǧīm is /dʒ/ (Bedouin, rural Levant, Mesopotamia),
    /ɡ/ (Cairene), /ɟ/ (Upper Egypt/Sudan), /ʒ/ (urban Levant). The node
    therefore states no group reflex: ج carries only the Classical/MSA
    /dʒ/ passed through from the reading base, and the leaves own it."""
    assert get(NODE).graphemes["ج"] == ["dʒ"]
    assert transcribe("جَبَل", NODE) == "ˈdʒabal"        # base (MSA) reading
    assert transcribe("جَبَل", "ar-EG") == "ˈɡabal"      # Cairene stop
    assert transcribe("جَبَل", "ar-SD") == "ˈɟabal"      # Sudanese palatal
    assert transcribe("جَبَل", "ar-x-levantine") == "ˈʒabal"  # urban Levant


# ─── NOT group-wide #3: interdental merger is a sedentary default ───────────

def test_interdental_merger_is_the_sedentary_default_not_a_group_claim():
    """Watson 2002:9 lists interdental PRESERVATION among Bedouin features:
    gilit Iraqi keeps θ/ð/ðˤ while Cairo and the urban Levant merge to
    stops. The stop-first candidates on the node are the sedentary-koine
    inheritance default (fricatives kept as second candidates), not a
    group-wide merger claim."""
    g = get(NODE).graphemes
    assert g["ث"] == ["t", "θ"]
    assert g["ذ"] == ["d", "ð"]
    assert transcribe("ثَوْب", NODE) == "ˈtawb"
    assert transcribe("ذَهَب", NODE) == "ˈdahab"
    # a retaining leaf really does override back to the fricatives
    assert transcribe("ثَوْب", "ar-IQ") == "ˈθoːb"
    assert transcribe("ذَهَب", "ar-IQ") == "ˈðahab"


# ─── Regression pin: the glue-node upgrade must not move any leaf ───────────

def test_descendant_output_is_unchanged_by_the_node_upgrade():
    """Every Mashriqi descendant inherits from this node; raising the node to
    research tier changed only prose/metadata, so descendant transcriptions
    must be byte-identical (no silent, uncited downstream change). One
    characteristic word per leaf, pinned from the pre-change engine."""
    pins = {
        "ar-EG": ("جَدِيد", "ɡaˈdiːd"),
        "ar-SD": ("جَبَل", "ˈɟabal"),
        "ar-TD": ("قَلْب", "ˈɡalb"),
        "ar-NG": ("قَلْب", "ˈɡalb"),
        "ar-IQ": ("كِتَاب", "tʃiˈtaːb"),
        "ar-IQ-x-qeltu": ("قَلْب", "ˈqalb"),
        "ar-x-levantine": ("ثَوْب", "ˈtoːb"),
        "ar-SY": ("جَبَل", "ˈʒabal"),
        "ar-LB": ("قَلْب", "ˈʔalb"),
        "ar-JO": ("ظَهْر", "ˈdˤɑhr"),
        "ar-PS": ("ثَوْب", "ˈtoːb"),
    }
    for code, (word, ipa) in pins.items():
        assert transcribe(word, code) == ipa, code
