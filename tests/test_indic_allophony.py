"""Indic post-lexical allophony: Hindi schwa deletion and Tamil stop voicing.

Both processes are the *data* half of the abugida model. The engine gives a
consonant letter its inherent vowel and cancels it when a matra or a virama
follows; what happens to the inherent vowel *after* that — deleted in Hindi,
kept in Sanskrit — and how a stop is realised in context — voiceless initially
and in geminates, voiced between vowels and after a nasal in Tamil — is stated
per language in ``allophone_rules``.

The Sanskrit tests are the load-bearing ones: sa and hi share a script, an
inherent vowel and an ancestry link, and differ *only* in their data. If schwa
deletion ever leaks into the engine, Sanskrit is what breaks.

Word→IPA pairs are the cited ones:

- Hindi schwa deletion: Ohala, *Aspects of Hindi Phonology* (1983), ch. 5;
  Ohala, "Hindi", *Handbook of the IPA* (1999), pp. 100-103; Narasimhan,
  Sproat & Kiraz, "Schwa-Deletion in Hindi Text-to-Speech Synthesis",
  *IJST* 7(4) (2004), pp. 319-333; Wikipedia, "Schwa deletion in Indo-Aryan
  languages".
- Tamil stop allophony: Keane, "Tamil", *JIPA* 34(1) (2004), pp. 111-116;
  Krishnamurti, *The Dravidian Languages* (2003), §4.2; Wikipedia,
  "Tamil phonology".
- Malayalam: Asher & Kumari, *Malayalam* (1997), pp. 405-406.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import G2P, get


# ═══════════════════════════════════════════════════════════════════════════
# Hindi — schwa deletion
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    # Word-final deletion: the inherent vowel of a final consonant letter is
    # not pronounced (Ohala 1999: 100-103).
    ("राम", "ɾaːm"),        # raam, not *raama
    ("घर", "ɡʱəɾ"),         # ghar
    ("शब्द", "ʃəbd̪"),       # shabd — final deletion applies after a cluster
    # Medial VC_CV deletion, right-to-left (Narasimhan et al. 2004: 319-333).
    ("नमकीन", "nəmkiːn"),   # namkeen, not *namakeen
    ("सरकार", "səɾkaːɾ"),   # sarkaar
    ("मालदीवी", "maːld̪iːʋiː"),
    # …but only when a vowel precedes: no deletion inside an onset cluster.
    ("प्रकार", "pɾəkaːɾ"),   # prakaar, not *prkaar
    # …and only when the FOLLOWING consonant carries a vowel of its own. In
    # कमल the final schwa goes, which leaves ल vowel-less — but the rule is
    # right-to-left, so म's schwa was already licensed to stay.
    ("कमल", "kəməl"),       # kamal, not *kaml
    ("भारत", "bʱaːɾət̪"),
    ("शोधक", "ʃoːd̪ʱək"),
])
def test_hindi_schwa_deletion(word, expected):
    assert G2P("hi").transcribe(word) == expected


def test_hindi_monosyllable_keeps_its_only_vowel():
    """A one-letter word is word-initial *and* word-final; the schwa stays."""
    assert G2P("hi").transcribe("न") == "nə"


# ═══════════════════════════════════════════════════════════════════════════
# Sanskrit — does NOT delete schwa (the rule lives in the DATA, not the engine)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    ("राम", "raːmə"),
    ("कमल", "kəmələ"),
    ("शब्द", "ɕəbd̪ə"),
])
def test_sanskrit_preserves_the_inherent_vowel(word, expected):
    """Same script, same inherent vowel, no schwa deletion — by data alone."""
    assert G2P("sa").transcribe(word) == expected


def test_only_hindi_declares_schwa_deletion():
    """Neither Sanskrit nor Vedic carries a schwa-deletion rule…"""
    for code in ("sa", "sa-x-vedic"):
        ids = [r.id for r in get(code).allophone_rules]
        assert not [i for i in ids if i.startswith("HI_SCHWA")], code
    assert [r.id for r in get("hi").allophone_rules
            if r.id.startswith("HI_SCHWA")]


def test_hindi_rules_do_not_reach_devanagari_descendants_by_accident():
    """…and hi's descendants inherit rules that cannot fire on their data.

    bho declares ⟨a⟩ (not ⟨ə⟩) as its inherent vowel and ur is Arabic-script,
    so the ⟨ə⟩-keyed Hindi rules are inert there. Bhojpuri schwa deletion is a
    separate, still-uncited question — it must be stated on its own merits, not
    inherited by accident.
    """
    assert G2P("bho").transcribe("कमल") == "kamala"
    assert get("bho").inherent_vowel == "a"


def test_hindi_nukta_letters_are_mapped():
    """⟨ड़⟩/⟨ढ़⟩ (NFC-precomposed) are the retroflex flaps, not unknown."""
    assert G2P("hi").transcribe("बड़ा") == "bəɽaː"


# ═══════════════════════════════════════════════════════════════════════════
# Tamil — positional stop allophony (no phonemic voicing contrast)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    # Intervocalic voicing: க → [ɡ], த → [d̪], ட → [ɖ], ப → [b].
    ("புத்தகம்", "put̪ːaɡam"),   # puttakam: geminate த stays voiceless, க voices
    ("எதிரி", "ed̪iri"),
    ("மகன்", "maɡan"),
    ("பெயர்ப்படு", "pejarpːaɖu"),
    # Post-nasal voicing.
    ("தங்கம்", "t̪aŋɡam"),
    ("நன்கொடை", "nanɡoɖai"),
    ("சாந்து", "tɕaːnd̪u"),
    ("உண்டா", "uɳɖaː"),
    # Word-initial and geminate stops stay voiceless; a geminate is a long
    # consonant (Keane 2004: 111-116).
    ("அக்கா", "akːaː"),
    ("பழம்", "paɻam"),
    ("குறுகுறுக்கும்", "kuruɡurukːum"),
    # A stop after a non-nasal vowel-less consonant is NOT voiced.
    ("பார்வை", "paːrʋai"),
])
def test_tamil_stop_allophony(word, expected):
    assert G2P("ta").transcribe(word) == expected


def test_tamil_palatal_lenites_between_vowels():
    """⟨ச⟩ is [s] intervocalically, not the voiced stop (Keane 2004: 113)."""
    assert G2P("ta").transcribe("இசை") == "isai"


# ═══════════════════════════════════════════════════════════════════════════
# Malayalam — inherits the Dravidian voicing, overrides the palatal
# ═══════════════════════════════════════════════════════════════════════════

def test_malayalam_inherits_tamil_voicing():
    assert G2P("ml").transcribe("മരുതം") == "marud̪a\u0303m"
    assert G2P("ml").transcribe("ചട്ട") == "tɕaʈːa"


def test_malayalam_overrides_the_palatal_by_id():
    """ml voices ⟨ച⟩ to [dʑ] where ta lenites it to [s] (Asher & Kumari 1997)."""
    assert G2P("ml").transcribe("വചനം") == "ʋadʑana\u0303m"
    overrides = {r.id for r in get("ml").allophone_rules
                 if r.id.startswith("TA_VOICE_tɕ")}
    assert overrides
    for rule in get("ml").allophone_rules:
        if rule.id in overrides:
            assert rule.surface.startswith("dʑ")


# ═══════════════════════════════════════════════════════════════════════════
# The rules are cited
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("code,source_ids", [
    ("hi", {"ohala1983", "ohala1999", "narasimhan2004"}),
    ("ta", {"keane2004", "krishnamurti2003"}),
    ("ml", {"asher_kumari1997"}),
])
def test_sources_are_declared(code, source_ids):
    spec = get(code)
    assert spec.allophone_rules
    assert source_ids <= {s.id for s in spec.sources}
    assert all(r.notes for r in spec.allophone_rules)


# ═══════════════════════════════════════════════════════════════════════════
# The rules are REACHABLE — the slot-shape invariant
# ═══════════════════════════════════════════════════════════════════════════
#
# ``AllophoneRescorer._realize`` matches a whole SLOT's IPA string
# (``ipa in rule.phonemes``). In an abugida a slot is one grapheme, so its IPA
# is only ever a candidate of that grapheme, optionally with the inherent vowel
# appended (phonetok: the inherent vowel surfaces unless a matra or virama
# cancels it) — ``k`` or ``ka``, NEVER ``kaː``/``ki``/``ku``, because a matra is
# a slot of its own. A rule keyed on ``kaː`` is therefore dead by construction.
#
# Enumerating a full C × V cross-product is the natural way to write these rules
# by hand and it is always wrong; this test pins the invariant so the dead-rule
# cross-product cannot grow back.


def _reachable_slot_ipas(code):
    """Every IPA string a slot can ever carry: {C} ∪ {C + inherent_vowel}."""
    spec = get(code)
    vals = set()
    for cands in spec.graphemes.values():
        vals.update(cands)
    for entry in (spec.positional_graphemes or {}).values():
        for cands in entry.values():
            for cand in cands:
                ipa = getattr(cand, "ipa", cand)
                if isinstance(ipa, str):
                    vals.add(ipa)
    iv = spec.inherent_vowel
    if iv:
        vals |= {v + iv for v in vals}
    return vals


@pytest.mark.parametrize("code", ["hi", "ta", "ml", "sa"])
def test_allophone_rules_key_only_on_reachable_slot_shapes(code):
    """Every rule a spec DECLARES must key on a shape that spec can emit.

    Read from the raw JSON, not the resolved spec: an inherited rule may key on
    a shape only its declaring ancestor emits (ta's grantha ⟨ஜ⟩ /dʒ/ is not a
    Malayalam letter), which is fine — the file that states a rule is the file
    that has to be able to fire it.
    """
    raw = json.loads(
        (Path(orthography2ipa.__file__).parent / "data" / f"{code}.json").read_text()
    )
    reachable = _reachable_slot_ipas(code)
    for rule in raw.get("allophone_rules", ()):
        assert rule["phonemes"], rule["id"]
        dead = [p for p in rule["phonemes"] if p not in reachable]
        assert not dead, (
            f"{code}: rule {rule['id']} keys on slot IPA(s) {dead} that the "
            f"tokenizer can never emit (a slot is C or C+inherent vowel)"
        )
        for field in ("preceded_by_phoneme", "followed_by_phoneme"):
            dead = [p for p in rule.get(field) or () if p not in reachable]
            assert not dead, (
                f"{code}: rule {rule['id']} has unreachable neighbour IPA(s) {dead}"
            )
