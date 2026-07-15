"""Proto-Peninsular Arabic (``ar-x-peninsular``): the shared phonology of the
Arabian Peninsula group, and — just as important for a GROUPING (glue) node —
the reflexes that are deliberately NOT asserted group-wide because the
literature shows them splitting inside the Peninsula.

``ar-x-peninsular`` is the grouping node above the Gulf subtree (ar-x-gulf →
ar-AE/ar-BH/ar-KW/ar-QA), Najdi (ar-SA-x-najd), Hejazi (ar-SA-x-hejaz),
Yemeni (ar-YE) and Omani (ar-OM). It declares only what is shared across the
whole Peninsula and serves as the data-inheritance root the leaves build on.
Every claim below is isolated on a real Arabic word and cited:

* Watson, J.C.E. (2002), *The Phonology and Morphology of Arabic*, OUP —
  ch.10 'Emphasis': §10.4 p.273 (spread from the pharyngealized coronals may
  encompass the whole phonological word; ex.(6) p.274), §10.5 pp.279-281
  (Ṣanʿānī; p.279: the DOMAIN of spread is not constant cross-dialectally —
  Abha rarely beyond the adjacent vowel vs Qatari whole-word), p.17 (§2.1.9,
  *q maintained in sedentary west/south Peninsula vs voiced [ɡ] in Bedouin
  dialects and Ṣanʿānī — gāl), p.16 (§2.1.6, ǧīm /dʒ/~/ɟ/~/ɡ/~/j/ within the
  Peninsula), pp.14-15 (Ṣanʿānī interdentals retained), p.9 (interdental
  preservation is a Bedouin-axis feature);
* Ingham, B. (1994), *Najdi Arabic: Central Arabian*, Benjamins — Najdi [ɡ]
  and ts/dz affrication (as reported; primary reference of the Najdi leaf);
* Holes, C. (2006), "Gulf Arabic", *EALL* II, Brill — Gulf subgroup profile
  (as reported);
* Al-Balushi, R. (2016), *Omani Arabic: More than One Dialect*,
  Macrolinguistics 4(4):80-125 — sedentary Omani /q/ retained (p.88), the
  counter-example to any group-wide qāf voicing;
* Omar, M.K. (1975), *Saudi Arabic: Urban Hijazi Dialect*, FSI — urban
  Hejazi merges the interdentals, the counter-example to any group-wide
  interdental retention.

Expectations are written with the engine's own stress marks (Arabic stress is
quantity-sensitive and declared on the spec).
"""
from orthography2ipa import transcribe, get
from orthography2ipa.types import QualityTier


NODE = "ar-x-peninsular"


# ─── The group node is a research-tier glue node with the right sources ─────

def test_is_research_tier_glue_node_with_primary_sources():
    """The node is raised to research tier and cites the Peninsular
    dialectology it rests on (Watson 2002 page-verified; Ingham 1994, Holes
    2006, Al-Balushi 2016 and Omar 1975 for the leaf-territory splits)."""
    spec = get(NODE)
    assert spec.quality is QualityTier.RESEARCH
    ids = {s.id for s in spec.sources}
    assert {"watson2002", "ingham1994", "holes2006",
            "albalushi2016", "omar1975"} <= ids


def test_notes_document_the_glue_node_boundary():
    """A grouping node must say what it does NOT own: qāf voicing, the
    interdental split, ǧīm and velar affrication all split within the
    Peninsula and are left to the leaves (glue-node rule)."""
    n = get(NODE).notes.lower()
    assert "not group-wide" in n or "not asserted group-wide" in n
    for token in ("qāf", "interdental", "affrication", "leaf", "leaves"):
        assert token.lower() in n


# ─── SHARED feature #1: emphasis spreading (Watson 2002 ch.10, verified) ────

def test_emphatic_spreading_rules_are_declared_and_fire():
    """Low vowels back to [ɑ]/[ɑː] adjacent to an emphatic — the AR_PEN_EMPH_*
    rules verified against Watson 2002 ch.10 (p.273-274; pp.279-281 for
    Ṣanʿānī): طَرِيق → [tˤɑˈriːq] (rightward, cf. San'ani ṭarīg p.281),
    صَغِير → [sˤɑˈɣiːr]."""
    ids = {r.id for r in get(NODE).allophone_rules}
    assert {"AR_PEN_EMPH_BACK_A_AFTER", "AR_PEN_EMPH_BACK_A_BEFORE",
            "AR_PEN_EMPH_BACK_AA_AFTER", "AR_PEN_EMPH_BACK_AA_BEFORE"} <= ids
    assert transcribe("طَرِيق", NODE) == "tˤɑˈriːq"
    assert transcribe("صَغِير", NODE) == "sˤɑˈɣiːr"
    assert transcribe("قَاضِي", NODE) == "ˈqɑːdˤiː"   # long aː backs too


def test_emphasis_rules_stay_adjacent_only():
    """The rules state only ADJACENT-vowel backing — the minimal common
    denominator — because the spread domain is not constant across the
    Peninsula: Abha rarely beyond the adjacent vowel vs Qatari whole-word
    (Watson 2002:279). A vowel not adjacent to the emphatic stays plain:
    the second /a/ of ضَرَب surfaces [a], not [ɑ]."""
    assert transcribe("ضَرَب", NODE) == "ˈdˤɑrab"
    for r in get(NODE).allophone_rules:
        if r.id.startswith("AR_PEN_EMPH"):
            assert r.preceded_by_phoneme or r.followed_by_phoneme, (
                "emphasis rules must be conditioned on an adjacent emphatic"
            )


# ─── SHARED feature #2: interdentals as the conservative root default ───────

def test_interdentals_are_first_candidates_at_the_root():
    """Most Peninsular varieties keep θ/ð/ðˤ (Najdi, Gulf, Ṣanʿānī — Watson
    2002:14-15, Omani), so the fricatives head the candidate lists:
    ثَوْب → [ˈθawb], ذَهَب → [ˈðahab], ظَهْر → [ˈðˤɑhr]."""
    g = get(NODE).graphemes
    assert g["ث"][0] == "θ"
    assert g["ذ"][0] == "ð"
    assert g["ظ"][0] == "ðˤ"
    assert transcribe("ثَوْب", NODE) == "ˈθawb"
    assert transcribe("ذَهَب", NODE) == "ˈðahab"
    assert transcribe("ظَهْر", NODE) == "ˈðˤɑhr"


# ─── NOT group-wide #1: interdental retention (Hejazi merges) ───────────────

def test_interdental_retention_is_not_asserted_group_wide():
    """Retention cannot be a group claim because urban Hejazi merges the
    interdentals to stops (Omar 1975; the ar-SA-x-hejaz leaf): the same words
    surface with stops there while Najdi keeps the fricatives. The stops stay
    available as second candidates at the root for exactly this reason."""
    g = get(NODE).graphemes
    assert "t" in g["ث"] and "d" in g["ذ"]
    assert transcribe("ثَوْب", "ar-SA-x-hejaz") == "ˈtoːb"      # merging leaf
    assert transcribe("ذَهَب", "ar-SA-x-hejaz") == "ˈdahab"
    assert transcribe("ثَوْب", "ar-SA-x-najd") == "ˈθawb"       # retaining leaf
    assert transcribe("ذَهَب", "ar-SA-x-najd") == "ˈðahab"


# ─── NOT group-wide #2: qāf voicing is a tendency, not a group value ────────

def test_qaf_keeps_both_candidates_and_leaves_split():
    """*q → [ɡ] is the majority Peninsular tendency (Najdi — Ingham 1994;
    Ṣanʿānī gāl — Watson 2002:17) but NOT universal: sedentary west/south
    Peninsula maintains *q (Watson 2002:17, after Behnstedt 1985:41) and
    sedentary Omani keeps [q] (Al-Balushi 2016:88). The root lists both and
    the leaves pick: Najdi/Yemeni [ɡ], Omani [q]."""
    assert get(NODE).graphemes["ق"] == ["q", "ɡ"]
    assert transcribe("قَلْب", NODE) == "ˈqalb"                 # root default
    assert transcribe("قَلْب", "ar-SA-x-najd") == "ˈɡalb"
    assert transcribe("قَلْب", "ar-YE") == "ˈɡalb"
    assert transcribe("قَلْب", "ar-OM") == "ˈqalb"              # the exception


# ─── NOT group-wide #3: velar affrication is subgroup territory ─────────────

def test_velar_affrication_is_left_to_the_subgroups():
    """Gulf k→[tʃ] and Najdi k→[ts] near front vowels are declared on
    ar-x-gulf and ar-SA-x-najd, not here: the node itself never affricates
    (كِتَاب → [kiˈtaːb]) while the subgroup leaves do."""
    node_rule_ids = {r.id for r in get(NODE).allophone_rules}
    assert not any("AFFRIC" in i for i in node_rule_ids)
    assert transcribe("كِتَاب", NODE) == "kiˈtaːb"
    assert transcribe("كِتَاب", "ar-x-gulf") == "tʃiˈtaːb"
    assert transcribe("كِتَاب", "ar-SA-x-najd") == "tsiˈtaːb"


# ─── Regression pin: the glue-node upgrade must not move any leaf ───────────

def test_descendant_output_is_unchanged_by_the_node_upgrade():
    """Every Peninsular descendant inherits from this node; raising the node
    to research tier changed only prose/metadata, so descendant
    transcriptions must be byte-identical (no silent, uncited downstream
    change). One characteristic word per leaf, pinned from the pre-change
    engine."""
    pins = {
        "ar-x-gulf": ("كِتَاب", "tʃiˈtaːb"),
        "ar-AE": ("سُوق", "ˈsuːɡ"),
        "ar-BH": ("قَلْب", "ˈɡalb"),
        "ar-KW": ("جَدِيد", "dʒaˈdiːd"),
        "ar-QA": ("ثَوْب", "ˈθoːb"),
        "ar-SA-x-najd": ("كِتَاب", "tsiˈtaːb"),
        "ar-SA-x-hejaz": ("ثَوْب", "ˈtoːb"),
        "ar-YE": ("قَلْب", "ˈɡalb"),
        "ar-OM": ("قَلْب", "ˈqalb"),
    }
    for code, (word, ipa) in pins.items():
        assert transcribe(word, code) == ipa, code
