"""Libyan Arabic (ar-LY) phonology: the reflexes that separate a Tripoli
transcription from Modern Standard Arabic and from the other Maghrebi leaves.

The baseline is the **urban koine of Tripoli** (Tripolitania) as described by
Christophe Pereira, *Le parler arabe de Tripoli (Libye)* (2010) and his EALL
article *Tripoli Arabic* (2011). Tripoli is a historically sedentary town speech
that took on the Bedouin-type qāf [ɡ]; like other sedentary Maghrebi dialects it
has **merged the interdentals into the dental stops**. Eastern (Cyrenaican /
Benghazi) and Bedouin Libyan are more conservative — they retain the interdentals
and keep the affricate [dʒ] for ǧīm (Owens 1984, *A Short Reference Grammar of
Eastern Libyan Arabic*) — so those reflexes are kept as the ranked-second
candidates rather than dropped.

Every claim below is isolated on a real word and cited:

* Pereira (2010, 2011 EALL) — qāf [ɡ] in the town, ǧīm [ʒ] (a *sun* letter in
  Tripoli);
* Benkato (2020, *Maghrebi Arabic*, open access) — sedentary Maghrebi merged the
  interdentals with the dental stops; Maghrebi deletes vowels in light syllables
  (*katab > Tripoli ktǝb); European contact added /v, č, ǧ/ to Italian loans;
* Watson (2002) — emphasis backs adjacent /a aː/ to [ɑ ɑː];
* Owens (1984) — eastern/Bedouin Libyan retention (the second candidates).

Undiacritized abjad input carries no short vowels, so bare-consonant skeletons
transcribe without them; diacritized forms are used where a vowel is under test.
"""
from orthography2ipa import transcribe, get


# ─── Metadata: which variety, and the dialectology that says so ────────────

def test_targets_the_tripoli_koine_and_cites_its_primary_sources():
    """The spec is research-tier and cites the Tripoli reference works plus the
    open-access Maghrebi contact study actually read for it."""
    spec = get("ar-LY")
    assert spec.quality.value == "research"
    ids = {s.id for s in spec.sources}
    assert {"pereira2010", "pereira2011eall", "owens1984", "benkato2020"} <= ids
    assert spec.parent == "ar-x-maghrebi"


# ─── qāf → [ɡ] (Bedouin-type), [q] only in Literary borrowings ─────────────

def test_qaf_is_g_bedouin_type():
    """Tripoli took the Bedouin reflex qāf ق → [ɡ]; [q] survives only in recent
    Literary-Arabic loans, so it is the second candidate (Pereira 2011 EALL)."""
    assert get("ar-LY").graphemes["ق"] == ["ɡ", "q"]
    assert transcribe("قاس", "ar-LY") == "ˈɡaːs"     # gās 'to measure/go toward'
    assert transcribe("قلب", "ar-LY").startswith("ˈɡ")


def test_dialectal_gaf_letter_is_g():
    """When Libyan is written in the dialectal spelling, the letter ⟨گ⟩ spells
    [ɡ] directly (e.g. ⟨گاز⟩ 'petrol/gas')."""
    assert get("ar-LY").graphemes["گ"] == ["ɡ"]
    assert transcribe("گاز", "ar-LY") == "ˈɡaːz"


# ─── ǧīm → [ʒ], a fricative and a sun letter (not the affricate) ───────────

def test_jim_is_the_fricative_and_a_sun_letter():
    """ǧīm ج → [ʒ] in Tripoli (a voiced post-alveolar *fricative*, and a sun
    letter unlike Classical Arabic); the affricate [dʒ] is the eastern / loan
    variant, kept as the second candidate (Pereira 2011; Owens 1984)."""
    assert get("ar-LY").graphemes["ج"] == ["ʒ", "dʒ"]
    assert transcribe("جبل", "ar-LY") == "ˈʒbl"      # jbal 'mountain'


# ─── Interdentals merge in the Tripoli koine, retained variant available ───

def test_interdentals_merge_to_dental_stops():
    """The urban Tripoli koine merges the interdentals into the dental stops:
    ث θ → [t], ذ ð → [d], ظ ðˤ → [dˤ] (Benkato 2020, sedentary Maghrebi merger).
    The conservative fricative is kept as the second candidate for eastern /
    Bedouin Libyan (Owens 1984)."""
    g = get("ar-LY").graphemes
    assert g["ث"] == ["t", "θ"]
    assert g["ذ"] == ["d", "ð"]
    assert g["ظ"] == ["dˤ", "ðˤ"]
    assert transcribe("ثلاثة", "ar-LY") == "ˈtlaːta"   # tlāta 'three'
    assert transcribe("ذهب", "ar-LY").startswith("ˈd")  # dhab 'gold'


# ─── Emphasis spreading backs /a aː/ to [ɑ ɑː] ─────────────────────────────

def test_emphasis_backs_adjacent_a():
    """A short /a/ next to an emphatic backs to [ɑ]; the same word also shows
    qāf → [ɡ]: ⟨طَبَق⟩ 'plate' → [tˤɑbaɡ] (Watson 2002, emphasis; Pereira 2011,
    qāf)."""
    assert transcribe("طَبَق", "ar-LY") == "ˈtˤɑbaɡ"
    assert transcribe("طَاب", "ar-LY") == "ˈtˤɑːb"      # long /aː/ → [ɑː]


# ─── Diphthongs: monophthongised as the mainline, retention a documented variant ─

def test_classical_diphthongs_monophthongise():
    """The urban Tripoli koine monophthongises the Classical diphthongs /aj aw/
    to [eː oː] as the mainline reflex (⟨سَيْف⟩ 'sword' → [seːf], ⟨لَوْن⟩ 'colour'
    → [loːn], ⟨زَوْج⟩ → [zoːʒ]) — Pereira 2010:66-67, 2011 EALL, matching the
    sibling sedentary koines ar-SY / ar-x-gulf / ar-SA-x-qassim (LY_MONO_AY/AW).
    Diphthong retention (sajf) is a documented residual variant, not the default.
    The ⟨وَيْ⟩/⟨يَوْ⟩ onset digraphs reach the monophthong via explicit graphemes."""
    assert transcribe("سَيْف", "ar-LY") == "ˈseːf"
    assert transcribe("لَوْن", "ar-LY") == "ˈloːn"
    assert transcribe("زَوْج", "ar-LY") == "ˈzoːʒ"
    assert transcribe("وَيْن", "ar-LY") == "ˈweːn"
    assert transcribe("يَوْم", "ar-LY") == "ˈjoːm"


def test_geminate_glides_do_not_monophthongise():
    """LY_MONO_AY/AW fire only on true /aj//aw/ atoms, never on a geminate glide
    (⟨الْجَوّ⟩ → [alˈʒaww]) or a long vowel plus glide (⟨الْعَايْلَة⟩ → [alˈʕaːjla])."""
    assert transcribe("الْجَوّ", "ar-LY") == "alˈʒaww"
    assert transcribe("الْعَايْلَة", "ar-LY") == "alˈʕaːjla"
