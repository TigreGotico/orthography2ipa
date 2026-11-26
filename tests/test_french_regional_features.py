"""Regional French features: Belgium, Switzerland, Laurentian length, the Midi.

Each case pins a reading that an opened source states, with a counter case
the rule must leave alone. The expected IPA is written in the test, never
read back from the engine. ``tests/test_french_variants.py`` holds the older
pins of the same specs.

Sources, all opened:

* Bardiaux, Racine, Simon & Hambye (2016), *Le français en Belgique*, in
  Detey et al. (eds.), *La prononciation du français dans le monde*, CLE
  International: pp. 39-40 (long vowel of the feminine, fête [fɛːt]), p. 41
  (huit [wit], never *[mwɛt] for muette).
* PFC, *Le e caduc : variation géographique*: section 'Français méridional'
  (final schwa of a polysyllable, [ø] in the first syllable and in
  monosyllables) and section 'Français de Suisse et de Belgique' (amie
  [amiː], jouée [ʒueː], bleue [bløː]).
* PFC, *Prononciation 3*, II d) 4): vingt [vɛ̃t] at Nyon, Genève, Gembloux.
* Avanzi (2024), *Français*, in *Sprachenräume der Schweiz* 1: pp. 115-117.
* Dumas (1974), *Durée vocalique et diphtongaison en français québécois*,
  Cahier de linguistique 4: pp. 15-31 and Table II, p. 26; p. 41, n. 13.
* Eychenne (2006), PhD thesis, Toulouse: pp. 115-117 (nasal appendix, after
  Durand 1988: 167), p. 120 and p. 124 (loi de position).
"""
import warnings

import pytest

import orthography2ipa as o2i


def _say(text, tag):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return o2i.transcribe(text, tag)


# --- Belgium and Switzerland ---------------------------------------------

@pytest.mark.parametrize("text, be, ch", [
    ("lui", "lwi", "lɥi"),         # Bardiaux et al. 2016: 41; ⟨ui⟩ context
    ("nuit", "nwi", "nɥi"),        # from Wikipedia only (see FR_BE_UI_W)
    ("cuisine", "kwizin", "kɥizin"),
    ("muette", "myɛt", "myɛt"),    # never *[mwɛt] (p. 41)
    ("nuage", "nyaʒ", "nyaʒ"),     # [ɥ] outside ⟨ui⟩ is not touched
])
def test_belgian_french_has_w_for_the_glide_of_ui(text, be, ch):
    assert _say(text, "fr-BE") == be
    assert _say(text, "fr-CH") == ch


@pytest.mark.parametrize("tag", ["fr-BE", "fr-CH"])
@pytest.mark.parametrize("text, expected", [
    ("aimée", "ɛmeː"),             # joué ~ jouée (PFC e-caduc page)
    ("jouée", "ʒueː"),
    ("amie", "amiː"),              # ami ~ amie
    ("bleue", "bløː"),             # bleu ~ bleue
    ("nue", "nyː"),                # nu ~ nue (Avanzi 2024: 115-116)
    ("vie", "viː"),
    ("ami", "ami"),                # no mute ⟨e⟩: short
    ("aimé", "ɛme"),
    ("amies", "ami"),              # the plural is not modelled
    ("dame", "dam"),               # a mute ⟨e⟩ after a consonant: no vowel to lengthen
])
def test_a_vowel_before_a_final_mute_e_is_long(tag, text, expected):
    assert _say(text, tag) == expected


@pytest.mark.parametrize("tag, expected", [
    ("fr-BE", "vɛ̃t"), ("fr-CH", "vɛ̃t"),
])
def test_vingt_keeps_its_final_t(tag, expected):
    # PFC consonant page II d) 4); Avanzi 2016 (map); Avanzi 2024: 117
    assert _say("vingt", tag) == expected


# --- Laurentian French: length and diphthongs (Dumas 1974) ----------------

@pytest.mark.parametrize("text, expected", [
    ("père", "pai̯ʁ"),             # ɛ before a final /ʁ/: ɛː -> aⁱ
    ("chaise", "ʃai̯z"),            # ex. (15): deux chaises
    ("rase", "ʁɑu̯z"),             # ex. (15): il se rase; ɒː -> ɑᵘ
    ("cuir", "kɥiːʁ"),            # high vowels are written long (Hall 2016)
    ("pire", "piːʁ"),             # p. 20: pire
    ("juge", "ʒyːʒ"),
    ("fête", "fai̯t"),              # ex. (1): bête, même; the circumflex
    ("pâte", "pɑu̯t"),             # ex. (1): âme, pâle
    ("rose", "ʁɔu̯z"),             # close-mid tense vowel, closed syllable
    ("jaune", "ʒɔu̯n"),
    ("côte", "kɔu̯t"),             # ex. (8)
    ("jeûne", "ʒœy̯n"),            # ex. (8)
    ("monde", "mɔ̃u̯d"),            # ex. (8): nasal vowels
    ("ventre", "vɑ̃u̯tʁ"),
    ("mince", "mɛ̃i̯s"),
    ("humble", "ãy̯bl"),
])
def test_quebec_diphthongises_a_long_vowel_in_the_last_syllable(
        text, expected):
    assert _say(text, "fr-CA") == expected


@pytest.mark.parametrize("text, expected", [
    ("barbe", "baʁb"),             # /ʁ/ is not the final consonant
    ("porte", "pɔʁt"),
    ("fêter", "fɛte"),             # not the last syllable
    ("patte", "pat"),              # /a/ in a closed syllable: short and front
    ("mai", "me"),                 # word-final close-mid: never diphthongised
    ("élite", "elɪt"),             # the laxing rule still applies
])
def test_quebec_leaves_short_vowels_alone(text, expected):
    assert _say(text, "fr-CA") == expected


@pytest.mark.parametrize("text, expected", [
    ("Canada", "kanadɒ"),          # Dumas 1974: 27: [ɒ] at the end of a word
    ("pas", "pɒ"),                 # ex. (17); a silent letter does not close it
    ("là", "lɒ"),                  # n. 13: the adverb là is [ɒ]
    ("la", "la"),                  # n. 13: the proclitics stay [a]
    ("à", "a"),
    ("ça", "sa"),
    ("jusqu'à", "ʒyska"),
])
def test_quebec_a_is_back_at_the_end_of_a_word(text, expected):
    assert _say(text, "fr-CA") == expected


@pytest.mark.parametrize("text, expected", [
    ("pain", "pẽ"),                # Dumas 1974: 26: the front nasal is [ẽ]
    ("vin", "vẽ"),
    ("moins", "mwẽ"),
    ("bien", "bjẽ"),
    ("enfant", "ɑ̃fã"),            # /ɑ̃/ is front [ã] at the end of a word
    ("temps", "tã"),
    ("ensemble", "ɑ̃sɑ̃u̯bl"),        # but long and back before a coda
])
def test_quebec_nasal_vowel_values(text, expected):
    assert _say(text, "fr-CA") == expected
