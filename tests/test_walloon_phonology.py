"""Walloon (rifondou walon) phonology: the rules that separate a Walloon
transcription from a French one.

This spec targets the unified **Common Walloon** orthography — the *rifondou
walon* standardised from the 1990s and used by the Walloon Wikipedia — not the
older phonetic Feller (1900) transcription. Rifondou is *diasystemic*: one
spelling is read with different sounds in different dialects, so the hallmark
graphemes (⟨å⟩, ⟨xh⟩, ⟨jh⟩, ⟨ea⟩, ⟨oi⟩) carry several ranked candidate values.

Every claim below is isolated on a real Walloon word and cited from:

* Espinosa Orjuela, Boula de Mareüil & Evrard (2025), *Speech synthesis for
  Walloon*, SSW 2025 — a rule-based rifondou grapheme-to-phoneme converter that
  documents the long vowels (⟨å⟩ /ɔː/), the nasal series /ẽ/ ⟨én⟩ alongside
  /ɛ̃/ ⟨in⟩ and /œ̃/ ⟨un⟩, the Germanic /h/ ⟨h⟩ and /x/ ⟨xh⟩, and word-final
  consonant devoicing (⟨jh⟩ /ʒ/ → [ç]);
* the Wikipedia *Walloon orthography* grapheme table for Common Walloon.

Expectations are written WITHOUT stress marks; the spec declares no lexical
stress (Walloon stress, like French, is phrase-level), so the engine emits none.
"""
import pytest

from orthography2ipa import transcribe, get


# ─── Which orthography, and the metadata that says so ──────────────────────

def test_targets_the_rifondou_not_the_feller_orthography():
    """The spec must declare it targets Common/rifondou Walloon, and cite the
    modern rule-based G2P that describes it (Orjuela et al. 2025)."""
    spec = get("wa")
    ids = {s.id for s in spec.sources}
    assert "orjuela2025" in ids
    assert "rifondou" in spec.notes.lower()
    assert spec.orthography_standard is not None
    assert "rifondou" in spec.orthography_standard.name.lower()


def test_is_a_langue_doil_sister_of_french():
    """Walloon descends from the Gallo-Romance Latin of northern Gaul, with a
    strong Frankish superstrate (stronger than French's) that preserved
    word-initial /h/ and Latin initial /w/."""
    spec = get("wa")
    assert spec.parent == "la-x-gallia"
    roles = {a.code: a.role.value for a in spec.ancestors}
    assert roles.get("la-x-gallia") == "parent"
    assert roles.get("gem") == "superstrate"
    assert "Romance" in get("wa").family


# ─── The hallmark graphemes rifondou revived ───────────────────────────────

def test_xh_is_the_diasystemic_fricative():
    """⟨xh⟩ is the hallmark rifondou grapheme (Feller ⟨ch⟩/⟨h⟩): ⟨pexhon⟩
    'fish' is read [pɛʃɔ̃] or [pɛhɔ̃] by region, so the spec lists [ʃ, h, x, ç]
    (Orjuela et al. 2025: /x/ ⟨xh⟩; Wikipedia: ⟨xh⟩ [h/ʃ/ç/x])."""
    assert get("wa").graphemes["xh"][:2] == ["ʃ", "h"]
    assert transcribe("pexhon", "wa") == "pɛʃɔ̃"


def test_jh_is_a_dorsal_fricative_diasystem():
    """⟨jh⟩ is [ʒ]/[h]/[ç] by region; ⟨måjhon⟩ 'house' is [mɔːʒɔ̃]."""
    assert get("wa").graphemes["jh"] == ["ʒ", "h", "ç"]
    assert transcribe("måjhon", "wa") == "mɔːʒɔ̃"


def test_a_ring_is_a_long_back_vowel():
    """⟨å⟩ is the emblematic Walloon letter: a long vowel [ɔː] (also [oː]/[ɑː]),
    which French lacks (Orjuela et al. 2025: long vowels like /ɔː/ ⟨å⟩)."""
    assert get("wa").graphemes["å"] == ["ɔː", "oː", "ɑː"]
    assert transcribe("på", "wa") == "pɔː"
    assert transcribe("tåve", "wa").startswith("tɔː")


def test_ea_is_the_rifondou_rising_diphthong():
    """⟨ea⟩ is read [ja] (also [eː]/[ɛː]): ⟨tchestea⟩ 'castle' → [tʃɛstja],
    ⟨bea⟩ 'beautiful' → [bja]."""
    assert get("wa").graphemes["ea"] == ["ja", "eː", "ɛː"]
    assert transcribe("bea", "wa") == "bja"
    assert transcribe("tchestea", "wa") == "tʃɛstja"


def test_oi_and_ai_are_walloon_digraphs():
    """⟨oi⟩ is [wa]/[wɛ]/[oː] and ⟨ai⟩ is a long [eː]/[ɛː] (Wikipedia table):
    ⟨froid⟩ 'cold' → [fʀwat], ⟨laid⟩ 'ugly' → [leːt]."""
    assert get("wa").graphemes["oi"][0] == "wa"
    assert get("wa").graphemes["ai"] == ["eː", "ɛː"]
    assert transcribe("froid", "wa") == "fʀwat"
    assert transcribe("laid", "wa") == "leːt"


# ─── The affricates: distinct from French /ʃ ʒ/ ────────────────────────────

def test_tch_and_dj_are_affricates():
    """Walloon has the affricates ⟨tch⟩ /tʃ/ and ⟨dj⟩ /dʒ/ that French
    palatalisation lost: ⟨vatche⟩ 'cow' [vatʃ], ⟨djin⟩ 'person' [dʒɛ̃]."""
    assert get("wa").graphemes["tch"] == ["tʃ"]
    assert get("wa").graphemes["dj"] == ["dʒ"]
    assert transcribe("vatche", "wa") == "vatʃ"
    assert transcribe("djin", "wa") == "dʒɛ̃"


# ─── Phonemic vowel length ─────────────────────────────────────────────────

def test_vowel_length_is_phonemic():
    """Length carries meaning, marked by the circumflex: ⟨cu⟩ /ky/ 'arse' vs
    ⟨cû⟩ /kyː/ 'cooked' (Wikipedia: minimal length pairs)."""
    assert transcribe("cu", "wa") == "ky"
    assert transcribe("cû", "wa") == "kyː"
    assert transcribe("djoû", "wa") == "dʒuː"


# ─── Nasal vowels: arise before a CODA nasal ───────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("bon", "bɔ̃"),      # ⟨on⟩ → [ɔ̃]
    ("djin", "dʒɛ̃"),    # ⟨in⟩ → [ɛ̃]
    ("an", "ɑ̃"),        # ⟨an⟩ → [ɑ̃]
    ("cén", "sẽ"),       # ⟨én⟩ → [ẽ], the nasal French lacks (Orjuela 2025)
    ("walon", "walɔ̃"),  # the language's own name
    ("pexhon", "pɛʃɔ̃"),
])
def test_nasal_vowels_before_coda_nasal(word, expected):
    """A vowel nasalises before a CODA nasal, and the nasal is absorbed:
    ⟨an⟩ [ɑ̃], ⟨in⟩ [ɛ̃], ⟨on⟩ [ɔ̃], ⟨un⟩ [œ̃], ⟨én⟩ [ẽ] (Orjuela et al. 2025)."""
    assert transcribe(word, "wa") == expected


def test_onset_nasal_leaves_the_vowel_oral():
    """The nasal series is a CODA effect: ⟨bon⟩ [bɔ̃] but ⟨bone⟩ [bɔn], ⟨an⟩
    [ɑ̃] but ⟨ane⟩ [an] — an onset nasal keeps the vowel oral."""
    assert transcribe("bon", "wa") == "bɔ̃"
    assert transcribe("bone", "wa") == "bɔn"
    assert transcribe("an", "wa") == "ɑ̃"
    assert transcribe("ane", "wa") == "an"


# ─── Germanic retentions: /h/ and /w/ ──────────────────────────────────────

def test_germanic_h_and_w_are_retained():
    """Unlike French, Walloon keeps the Frankish word-initial /h/ (⟨houbion⟩
    'hops' [hubiɔ̃]) and the Latin/Germanic initial /w/ (⟨walon⟩ [walɔ̃])."""
    assert transcribe("houbion", "wa").startswith("h")
    assert transcribe("walon", "wa").startswith("w")


# ─── Word-final obstruent devoicing (on a true final consonant) ─────────────

@pytest.mark.parametrize("word,expected", [
    ("grand", "ɡʀɑ̃t"),   # /d/ → [t]
    ("quand", "kɑ̃t"),    # /d/ → [t]
    ("pied", "piɛt"),     # /d/ → [t]
    ("froid", "fʀwat"),   # /d/ → [t]
    ("laid", "leːt"),     # /d/ → [t]
    ("tchôd", "tʃoːt"),   # /d/ → [t]
])
def test_final_devoicing_on_bare_final_consonant(word, expected):
    """Word-final obstruent devoicing (/b d ɡ v z/ → [p t k f s]) fires on a
    consonant that is genuinely word-final (Orjuela et al. 2025)."""
    assert transcribe(word, "wa") == expected


def test_c_softens_before_a_front_vowel():
    """⟨c⟩ is [s] before a front vowel, [k] otherwise: ⟨cén⟩ [sẽ], ⟨ceke⟩
    [sɛk], but ⟨cu⟩ [ky], ⟨cwate⟩ [kwat] (Wikipedia: ⟨c⟩ [k/s])."""
    assert transcribe("ceke", "wa") == "sɛk"
    assert transcribe("cén", "wa") == "sẽ"
    assert transcribe("cu", "wa").startswith("k")
    assert transcribe("cwate", "wa").startswith("k")


def test_final_atonic_e_is_mute():
    """Walloon lost the Latin final atonic vowels; the written final ⟨e⟩ is
    mute: ⟨vatche⟩ [vatʃ], ⟨rotche⟩ [ʀɔtʃ], ⟨biesse⟩ 'beast' [biɛs]."""
    assert transcribe("vatche", "wa") == "vatʃ"
    assert transcribe("rotche", "wa") == "ʀɔtʃ"
    assert transcribe("biesse", "wa") == "biɛs"


# ─── Known engine limitation, pinned so it cannot drift silently ───────────

def test_rodje_and_rotche_are_homophones():
    """⟨rodje⟩ 'red' and ⟨rotche⟩ 'rock' are homophones [ʀɔtʃ]: the final ⟨e⟩
    is mute and the exposed ⟨dj⟩ /dʒ/ devoices to [tʃ] (Wikipedia: "rodje and
    rotche sound identical"). The devoicing rule is declared (WA_DEVOICE_dzh)
    but the engine cannot see the ⟨dj⟩ as final behind the silent ⟨e⟩."""
    assert transcribe("rodje", "wa") == transcribe("rotche", "wa") == "ʀɔtʃ"
