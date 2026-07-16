"""Ḥassāniyya Arabic (ar-MR) phonology: the reflexes that mark the Bedouin
Maghrebi dialect of Mauritania apart from Modern Standard Arabic and from the
sedentary Maghrebi leaves (Moroccan, Tunisian, Algerian).

Ḥassāniyya (*klām əl-Bīđ̣ān*) is a conservative **Bedouin** dialect that is
typologically closer to eastern Arabic than to sedentary Maghrebi. The reference
description is Catherine Taine-Cheikh, *Ḥassāniyya Arabic* (Encyclopedia of Arabic
Language and Linguistics, vol. 2, Brill 2007, pp. 240–250), read from the
open-access HAL author manuscript, alongside Cohen (1963) and Heath (2004).

Every claim below is isolated on a real form and cited to a section of
Taine-Cheikh (2007):

* §2.1.1.2 — qāf realised [ɡ]; the interdentals maintained, ḍād → đ̣ [ðˤ];
* §2.1.1.3 — the labial spirant realised preferentially as voiced **[v]** (the
  dialect's most famous consonantal trait); ǧīm a palato-alveolar fricative [ʒ];
* §2.1.1.1 — /ġ/ ~ /q/ merger; the rich emphatic system (/ṛ ḷ ẓ/);
* §2.1.2 — vowels and ʔimāla; §2.1.3 — the four diphthongs preserved.

Undiacritized abjad input carries no short vowels; diacritized forms are used
where a vowel is under test.
"""
from orthography2ipa import transcribe, get


# ─── Metadata: which variety, and the dialectology that says so ────────────

def test_targets_hassaniyya_and_cites_taine_cheikh():
    """Research-tier, cites the EALL reference (read for this spec) plus Cohen
    (1963) and Heath (2004)."""
    spec = get("ar-MR")
    assert spec.quality.value == "research"
    ids = {s.id for s in spec.sources}
    assert {"tainecheikh2007", "cohen1963", "heath2004hass"} <= ids
    assert spec.parent == "ar-x-maghrebi"


# ─── qāf → [ɡ] (Bedouin), and the ġ/q merger ───────────────────────────────

def test_qaf_is_g_bedouin_type():
    """Ḥassāniyya realises qāf ق → [ɡ] (Taine-Cheikh §2.1.1.2); [q] survives in
    Classical borrowings and as the ġ-merger reflex, so it is the second
    candidate."""
    assert get("ar-MR").graphemes["ق"] == ["ɡ", "q"]
    assert transcribe("قاس", "ar-MR") == "ˈɡaːs"        # gās
    assert transcribe("قلب", "ar-MR").startswith("ˈɡ")


def test_ghayn_merges_toward_q():
    """/ġ/ and /q/ merge, realised [q] for most speakers and always under
    gemination; [ʁ] survives for western speakers, so ġayn غ ranks [ʁ, q]
    (Taine-Cheikh §2.1.1.1)."""
    assert get("ar-MR").graphemes["غ"] == ["ʁ", "q"]


# ─── The Ḥassāniyya /v/: *f realised as voiced [v] ─────────────────────────

def test_labial_spirant_is_voiced_v():
    """The signature Ḥassāniyya trait: the labial spirant *f is realised
    PREFERENTIALLY as voiced [v] (Taine-Cheikh §2.1.1.3, 'particular to this
    dialect'), written ⟨ڤ⟩. ف ranks [v, f]; ⟨ڤ⟩ is [v]."""
    assert get("ar-MR").graphemes["ف"] == ["v", "f"]
    assert get("ar-MR").graphemes["ڤ"] == ["v"]
    assert transcribe("فم", "ar-MR") == "ˈvm"            # fm/vm 'mouth'
    assert transcribe("فَاس", "ar-MR") == "ˈvaːs"        # fās/vās 'axe/Fez'


# ─── Interdentals retained; ḍād and ẓāʾ both → [ðˤ] ────────────────────────

def test_interdentals_are_retained():
    """The interdentals are maintained (Taine-Cheikh §2.1.1.2): ث → [θ],
    ذ → [ð] — unlike the sedentary Maghrebi merger to stops."""
    g = get("ar-MR").graphemes
    assert g["ث"] == ["θ", "t"]
    assert g["ذ"] == ["ð", "d"]
    assert transcribe("ثلاثة", "ar-MR") == "ˈθlaːθa"     # θlāθa 'three'
    assert transcribe("ذهب", "ar-MR").startswith("ˈð")   # ðhab 'gold'


def test_dad_is_the_emphatic_interdental():
    """ḍād ض → đ̣ [ðˤ] 'the reflex of most words with ḍād', merging with ẓāʾ
    ظ [ðˤ] (Taine-Cheikh §2.1.1.2); the stop [dˤ] is the second candidate."""
    g = get("ar-MR").graphemes
    assert g["ض"] == ["ðˤ", "dˤ"]
    assert g["ظ"] == ["ðˤ", "dˤ"]
    assert transcribe("ضرب", "ar-MR") == "ˈðˤrb"          # đ̣rb 'to hit'
    assert transcribe("ظلم", "ar-MR") == "ˈðˤlm"          # đ̣lm 'injustice'


# ─── ǧīm → [ʒ] ─────────────────────────────────────────────────────────────

def test_jim_is_a_fricative():
    """ǧīm ج → [ʒ], a palato-alveolar fricative (Taine-Cheikh §2.1.1.3)."""
    assert get("ar-MR").graphemes["ج"] == ["ʒ", "dʒ"]
    assert transcribe("جبل", "ar-MR") == "ˈʒbl"           # jbal 'mountain'
    assert transcribe("جَمَل", "ar-MR") == "ˈʒamal"       # jamal 'camel'


# ─── Emphasis and diphthongs ───────────────────────────────────────────────

def test_emphasis_backs_long_a():
    """Emphasis backs an adjacent /aː/ to [ɑː]: ⟨طَاب⟩ 'to become good' → [tˤɑːb]
    (inherited emphasis; Ḥassāniyya has a rich emphatic system, Taine-Cheikh
    §2.1.1.1)."""
    assert transcribe("طَاب", "ar-MR") == "ˈtˤɑːb"


def test_classical_diphthongs_are_preserved():
    """The four Classical diphthongs are preserved (Taine-Cheikh §2.1.3), with
    /aj aw/ only variably tending to [eː oː]: ⟨بَيْت⟩ 'house' → [bajt],
    ⟨لَوْن⟩ 'colour' → [lawn]. (⟨سَيْف⟩ surfaces as [sajv] here, since word-final
    ف is realised as the Ḥassāniyya voiced [v] — see the /v/ test.)"""
    assert transcribe("بَيْت", "ar-MR") == "ˈbajt"
    assert transcribe("لَوْن", "ar-MR") == "ˈlawn"
    assert transcribe("سَيْف", "ar-MR") == "ˈsajv"
