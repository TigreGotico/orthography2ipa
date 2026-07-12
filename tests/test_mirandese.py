"""Mirandese (mwl) and its sub-dialects Sendinês and Ifanês.

Mirandese is an Asturleonese language (parent ``ast-PT-x-medieval``), NOT a
Portuguese dialect. These tests pin the research-grounded features taken from
the *Convenção Ortográfica da Língua Mirandesa* (Ferreira & Raposo 1999),
Leite de Vasconcelos' *Estudos de Philologia Mirandesa* (1900) and the
TigreGotico/mirandese_g2p expert gold:

* the hallmark sibilant system — apical ⟨s⟩ /s̺ z̺/ vs dorso-dental
  ⟨c,ç,z⟩ /s z/, ⟨x⟩ /ʃ/, ⟨j,g⟩ /ʒ/, ⟨ch⟩ affricate /tʃ/;
* Leonese initial-l palatalisation (⟨l⟩→/ʎ/) and ⟨lh⟩/⟨nh⟩;
* the Leonese diphthongs ⟨iê/ie⟩ [je/jɛ] and ⟨uô/uo⟩ [wo/wɔ];
* Sendinês deltas: monophthongisation to /i/,/u/ and ⟨lh⟩→/l/;
* Ifanês (Raiano/Northern): phonologically tracks Central Mirandese.
"""
from orthography2ipa import get
from orthography2ipa.g2p import G2P


def _t(code):
    return G2P(code)


# --- the sibilant system (hallmark) -----------------------------------------

def test_apical_s_marked_dorsal_c_z_plain():
    """Apical ⟨s⟩ carries the ̺ diacritic; dorso-dental ⟨c,ç,z⟩ are plain."""
    spec = get("mwl")
    assert spec.graphemes["ç"] == ["s"]
    assert spec.graphemes["z"] == ["z"]
    assert "s" in spec.graphemes["c"]
    # apical series keeps the ̺ diacritic (word-initial / coda)
    s_pos = spec.positional_graphemes["s"]
    from orthography2ipa.types import GraphemePosition
    assert s_pos[GraphemePosition.WORD_INITIAL] == ["s̺"]
    assert s_pos[GraphemePosition.INTERVOCALIC] == ["z̺"]


def test_predorsal_sibilant_transcription():
    g = _t("mwl")
    # ⟨c⟩ before front vowel and ⟨ç⟩ -> plain /s/
    assert g.transcribe("brício") == "ˈbɾisjo"
    assert g.transcribe("rapaç").endswith("s")
    # ⟨z⟩ -> plain /z/
    assert "z" in g.transcribe("bizarro")
    assert "z̻" not in g.transcribe("bizarro")


def test_apical_s_transcription():
    g = _t("mwl")
    # word-initial and coda ⟨s⟩ -> apical /s̺/
    assert "s̺" in g.transcribe("tascar")


def test_postalveolars_and_affricate():
    spec = get("mwl")
    assert spec.graphemes["x"] == ["ʃ"]
    assert spec.graphemes["j"] == ["ʒ"]
    assert spec.graphemes["ch"] == ["tʃ"]  # still an affricate, unlike EP
    assert spec.graphemes["y"] == ["j"]     # glide, not /ʝ/


# --- Leonese lateral / initial-l palatalisation -----------------------------

def test_initial_l_palatalises():
    g = _t("mwl")
    # Convenção § L: word-initial ⟨l⟩ before a vowel = /ʎ/
    assert g.transcribe("luç") == "ˈʎus"


def test_lh_and_nh_digraphs():
    spec = get("mwl")
    assert spec.graphemes["lh"] == ["ʎ"]
    assert spec.graphemes["nh"] == ["ɲ"]


def test_vnh_trigraph_keeps_palatal_nasal():
    """The greedy nasal-vowel digraph must not swallow the /ɲ/ of ⟨nh⟩."""
    g = _t("mwl")
    assert g.transcribe("danho") == "ˈdaɲu"
    assert "ɲ" in g.transcribe("canhona")


# --- Leonese diphthongs -----------------------------------------------------

def test_leonese_diphthongs_central():
    g = _t("mwl")
    assert g.transcribe("tierra").startswith("ˈtjɛr")   # ie -> [jɛ]
    assert "wo" in g.transcribe("puorta")                # uo -> [wo]


# --- allophony (B8) ---------------------------------------------------------

def test_nasal_place_assimilation_rules_present():
    spec = get("mwl")
    ids = {r.id for r in spec.allophone_rules}
    assert {"MWL_NASAL_LABIAL", "MWL_NASAL_VELAR"} <= ids


def test_spirants_declared_in_inventory():
    """The voiced-stop spirants are declared in the allophone inventory."""
    spec = get("mwl")
    assert "β" in spec.allophones["b"]
    assert "ð" in spec.allophones["d"]


def test_intervocalic_d_spirant_declared_but_not_default():
    """[ð] stays an inventory allophone / lattice candidate: intervocalic /d/
    is stop-dominant in the expert gold (Asturleonese /d/-occlusion), so it is
    NOT rewritten by default — contrast /b/, which IS (see the spirantisation
    tests below)."""
    assert _t("mwl").transcribe("nada") == "ˈnadɐ"
    assert _t("mwl").transcribe("rabudo") == "rɐˈβudu"  # /b/ lenites, /d/ does not


# --- Sendinês deltas --------------------------------------------------------

def test_sendim_monophthongisation():
    g = _t("mwl-x-sendim")
    # iê/ie -> /i/, uô/uo -> /u/
    assert g.transcribe("puorta") == "ˈpuɾtɐ"


def test_sendim_depalatalisation():
    g = _t("mwl-x-sendim")
    # ⟨lh⟩ -> /l/ and no initial-l palatalisation (isolate the lateral: use
    # words without an intervocalic voiced stop so the /b/-spirant rule does
    # not muddy the assertion)
    assert g.transcribe("lhado") == "ˈladu"
    assert g.transcribe("alhá") == "ɐˈla"
    assert g.transcribe("luç") == "ˈlus"


def test_sendim_inherits_sibilants():
    # graphemes_base=mwl -> Sendinês keeps the Central sibilant system
    assert get("mwl-x-sendim").graphemes["ç"] == ["s"]


# --- Ifanês (Raiano / Northern) ---------------------------------------------

def test_ifanes_tracks_central():
    """Ifanês has no documented segmental delta from Central Mirandese;
    it keeps the diphthongs [je]/[wo] and /ʎ/ (only Sendinês diverges)."""
    gi, gc = _t("mwl-x-ifanes"), _t("mwl")
    for w in ["tierra", "puorta", "lhobo", "luç", "danho", "bizarro"]:
        assert gi.transcribe(w) == gc.transcribe(w)


def test_ifanes_promoted_to_research():
    assert get("mwl-x-ifanes").quality == "research"
    assert get("mwl-x-sendim").quality == "research"


# --- intervocalic voiced-stop spirantisation --------------------------------
# Ibero-Romance lenition: /b d ɡ/ → [β ð ɣ] between vowels, except after a
# pause or a nasal (Mateus & d'Andrade 2000:11; Ferreira & Raposo 1999; mwl
# Wikipedia phonology). Grounded per-phoneme on the TigreGotico/mirandese_g2p
# expert gold: /b/ is spirant-dominant intervocalically (β:9/b:5) so it is
# rewritten; intervocalic ⟨g⟩ is already spirantised at the positional layer;
# intervocalic /d/ is stop-dominant (d:13/ð:7, Asturleonese /d/-occlusion) and
# is deliberately left as a stop.

def test_intervocalic_b_spirantises_to_beta():
    g = _t("mwl")
    # /b/ between vowels lenites to [β] (gold: haber→ɐˈβeɾ, rabudo→rɐˈβudu)
    assert g.transcribe("haber") == "ɐˈβeɾ"
    assert g.transcribe("rabudo") == "rɐˈβudu"
    assert g.transcribe("nuobo") == "ˈnwoβu"


def test_word_initial_and_post_nasal_b_stays_a_stop():
    g = _t("mwl")
    # word-initial ⟨b⟩ is a stop; only the intervocalic one lenites
    assert g.transcribe("bibal") == "biˈβal"
    # post-nasal ⟨b⟩ (after [m]) keeps the stop — the spirant rule requires a
    # preceding vowel, not a nasal
    assert g.transcribe("ambos") == "ˈambus̺"
    assert g.transcribe("cambo") == "ˈkambu"


def test_intervocalic_d_is_not_spirantised():
    # Asturleonese /d/ resists intervocalic spirantisation (gold stop-dominant):
    # ⟨d⟩ between vowels stays [d], NOT [ð]
    g = _t("mwl")
    assert g.transcribe("nada") == "ˈnadɐ"
    assert "ð" not in g.transcribe("nada")


def test_intervocalic_g_spirantises_via_positional_layer():
    # intervocalic ⟨g⟩ → [ɣ] is handled at the positional_graphemes layer, so
    # no allophone rule is needed and none double-applies after a glide
    g = _t("mwl")
    assert g.transcribe("mogadouro") == "muɣɐˈdowɾu"
    # ⟨g⟩ after the glide of a falling diphthong keeps the stop (gold: eigual
    # → [ɐjˈɡwal]); a naive /ɡ/→[ɣ] allophone rule would wrongly lenite it
    assert g.transcribe("eigual") == "eˈjɡal"


def test_only_the_b_spirant_rule_is_declared():
    ids = [r.id for r in get("mwl").allophone_rules]
    assert "MWL_SPIRANT_B" in ids
    # /ɡ/ (positional layer) and /d/ (stop-dominant) get no allophone rewrite
    assert "MWL_SPIRANT_G" not in ids
    assert "MWL_SPIRANT_D" not in ids


def test_spirantisation_is_pan_mirandese():
    # /b/ spirantisation is inherited by the sub-dialects (graphemes_base=mwl)
    assert _t("mwl-x-sendim").transcribe("haber") == "ɐˈβeɾ"
    assert _t("mwl-x-ifanes").transcribe("haber") == "ɐˈβeɾ"
    assert "MWL_SPIRANT_B" in [r.id for r in get("mwl-x-sendim").allophone_rules]
