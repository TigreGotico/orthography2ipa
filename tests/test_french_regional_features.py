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


# --- Southern French (Midi) ----------------------------------------------

MIDI = "fr-FR-x-midi"


@pytest.mark.parametrize("text, expected", [
    ("patte", "patə"),             # PFC: patte [patə]
    ("pattes", "patə"),            # the plural ⟨-s⟩ is silent
    ("seule", "sœlə"),             # seul vs seule
    ("seul", "sœl"),
    ("petite", "pøtitə"),          # [ø] in the first syllable
    ("petit", "pøti"),             # PFC: petit [pøti]
    ("chemise", "ʃømizə"),
    ("le", "lø"),                  # monosyllables are [ø]
    ("vie", "vi"),                 # after a vowel the ⟨e⟩ stays mute
])
def test_the_midi_pronounces_the_final_schwa(text, expected):
    assert _say(text, MIDI) == expected


def test_the_midi_final_schwa_falls_before_a_vowel():
    # PFC: '(sauf s'il est suivi d'une voyelle)'
    assert _say("quatre heures", MIDI) == "katʁ‿ œʁə"
    assert _say("une petite fille", MIDI).split()[1] == "pøtitə"


@pytest.mark.parametrize("text, expected", [
    ("rose", "ʁɔzə"),              # open before the schwa syllable
    ("père", "pɛʁə"),              # Eychenne 2006: 120, père [ˈpɛ.rə]
    ("jaune", "ʒɔnə"),
    ("creuse", "kʁœzə"),
    ("port", "pɔʁ"),               # closed syllable
    ("peau", "po"),                # open syllable
    ("lait", "le"),                # close in an open syllable
    ("jamais", "ʒame"),
    ("bêtise", "betizə"),          # p. 124: bêtise [betiz]
    ("fleuri", "fløʁi"),           # p. 124: fleuri [fløri]
    ("poser", "poze"),             # before a full vowel: close
    ("cobra", "kobʁa"),            # an obstruent-liquid onset leaves it open
    ("problème", "pʁoblɛmə"),
    ("propre", "pʁɔpʁə"),          # the onset before a schwa: open
    ("perler", "pɛʁle"),           # [ʁl] is no onset: closed
])
def test_the_midi_follows_the_loi_de_position(text, expected):
    assert _say(text, MIDI) == expected


@pytest.mark.parametrize("text, expected", [
    ("pain", "pɛŋ"),               # velar appendix at the end of a word
    ("lent", "laŋ"),               # Durand 1988: 167: lent [laN]
    ("vin", "vɛŋ"),
    ("brun", "bʁœŋ"),
    ("bien", "bjɛŋ"),
    ("lampe", "lampə"),            # homorganic before a consonant
    ("lenteur", "lantœʁ"),
    ("plainte", "plɛntə"),
    ("enfant", "aɱfaŋ"),
])
def test_the_midi_nasal_vowel_is_a_vowel_plus_an_appendix(text, expected):
    assert _say(text, MIDI) == expected


@pytest.mark.parametrize("text, expected", [
    ("en patois", "am patwa"),     # Durand 1988: 167, en patois [ampatwa]
    ("un vin", "œɱ vɛŋ"),
    ("en tout", "an tu"),
    ("en cas", "aŋ ka"),           # velar before a velar
    ("en avion", "aŋ avjɔŋ"),      # no consonant follows
])
def test_the_midi_appendix_takes_the_place_of_the_next_word(text, expected):
    assert _say(text, MIDI) == expected


def test_the_midi_spec_is_a_variant_of_fr_fr():
    spec = o2i.get(MIDI)
    assert spec.parent == "fr-FR"
    assert o2i.resolve(MIDI) == MIDI
    assert "Gallo-Romance" in spec.family_path


# --- ⟨ê⟩ length, unit vowels, Laurentian length and proclitics, Midi schwa -------

@pytest.mark.parametrize("tag", ["fr-BE", "fr-CH"])
@pytest.mark.parametrize("text, expected", [
    ("fête", "fɛːt"),              # final closed syllable: long
    ("rêve", "ʁɛːv"),
    ("fêter", "fɛte"),             # the sources state the length in a final
    ("bêtise", "bɛtiz"),           # syllable only (Bardiaux et al. 2016:
    ("rêver", "ʁɛve"),             # 39-40; PFC faites ~ fête, belle ~ bêle)
    ("pêcheur", "pɛʃœʁ"),
    ("forêt", "fɔʁɛ"),             # open final syllable: no length stated
    ("prêt", "pʁɛ"),
])
def test_the_circumflex_e_is_long_only_in_a_closed_final_syllable(
        tag, text, expected):
    assert _say(text, tag) == expected


@pytest.mark.parametrize("text, be, ch", [
    ("pluie", "plwiː", "plɥiː"),   # PFC e-caduc page: the final e survives
    ("suie", "swiː", "sɥiː"),      # as the length of the vowel before it
    ("joie", "ʒwaː", "ʒwaː"),
    ("soie", "swaː", "swaː"),
    ("proie", "pʁwaː", "pʁwaː"),
])
def test_the_vowel_of_a_unit_before_a_final_mute_e_is_long(text, be, ch):
    assert _say(text, "fr-BE") == be
    assert _say(text, "fr-CH") == ch


@pytest.mark.parametrize("text, expected", [
    ("mer", "mai̯ʁ"),               # Dumas 1974: 18-21: every vowel before a
    ("fer", "fai̯ʁ"),               # word-final /r/; fr-FR lists these words
    ("hiver", "ivai̯ʁ"),            # as whole-word exceptions
    ("hier", "jai̯ʁ"),
    ("ouvre", "uːvʁ"),             # rule (6), ex. (7): ouvre [uːvr]
    ("livre", "liːvʁ"),
    ("lèvre", "lai̯vʁ"),
    ("chèvre", "ʃai̯vʁ"),
    ("moi", "mwɒ"),                # p. 27: [ɒ] at the end of a word
    ("trois", "tʁwɒ"),
    ("froid", "fʁwɒ"),
    ("noir", "nwɑu̯ʁ"),
    ("boîte", "bwat"),             # closed syllable: front [a]
    ("leur", "lœʁ"),               # proclitics carry no accent and are not
    ("par", "paʁ"),                # diphthongised (pp. 28-29; ex. (17):
    ("pour", "puʁ"),               # leur oncle)
    ("sur", "syʁ"),
])
def test_quebec_length_proclitics_and_final_back_a(text, expected):
    assert _say(text, "fr-CA") == expected


def test_quebec_proclitics_stay_short_inside_a_phrase():
    assert _say("par la porte", "fr-CA").split()[0] == "paʁ"
    assert _say("leur maison", "fr-CA").split()[0] == "lœʁ"


@pytest.mark.parametrize("text, expected", [
    ("fille", "fijə"),             # PFC: the final schwa after a consonant
    ("ville", "vilə"),             # sound, whatever spells it
    ("mille", "milə"),
    ("famille", "famijə"),
    ("Marseille", "maʁsɛjə"),
    ("paille", "pajə"),
    ("bouteille", "butɛjə"),
    ("feuille", "fœjə"),
    ("aime", "ɛmə"),
    ("semaine", "sømɛnə"),
    ("laine", "lɛnə"),
    ("fontaine", "fɔntɛnə"),
    ("Seine", "sɛnə"),
    ("escalier", "ɛskalje"),       # closed syllable before ⟨sc⟩ [sk]
    ("escargot", "ɛskaʁɡo"),
    ("poème", "poɛmə"),            # open syllable in hiatus: close
    ("automne", "otɔnə"),          # the appendix and a following nasal
])
def test_midi_schwa_after_units_and_loi_de_position(text, expected):
    assert _say(text, MIDI) == expected


def test_the_midi_final_schwa_links_its_consonant_before_a_vowel():
    # the schwa falls and the consonant links, as in fr-FR's enchaînement
    assert _say("une école", MIDI) == "yn‿ ekɔlə"


def test_the_midi_donc_is_an_oral_vowel_plus_an_appendix():
    # the appendix takes the place of the [k] after it (Durand 1988: 167)
    assert _say("donc", MIDI) == "dɔŋk"


#: fr-FR (PR #2710) reads donc and ginseng as word exceptions and keeps the
#: numeral consonant before donc; these cases need that parent.
needs_2710_words = pytest.mark.skipif(
    not {"donc", "ginseng"} <= set(o2i.get("fr-FR").word_exceptions),
    reason="fr-FR has no donc and ginseng exceptions on this base")


@needs_2710_words
@pytest.mark.parametrize("text, expected", [
    ("huit donc", "ɥit dɔŋk"),         # donc keeps the [t] of huit, as in fr-FR
    ("dix donc", "dis dɔŋk"),
    ("ginseng bio", "ʒinsɛŋ bjo"),     # a lexical [ŋ] is no appendix
])
def test_the_midi_reads_the_fr_fr_word_exceptions(text, expected):
    assert _say(text, MIDI) == expected


# --- numeral sandhi -------------------------------------------------------

def test_belgian_huit_drops_its_t_before_a_consonant():
    # fr-FR mutes the [t] of huit before a consonant; the Belgian [wit]
    # follows it (Bardiaux et al. 2016: 41 for the [w])
    assert _say("huit livres", "fr-BE").split()[0] == "wi"


def test_quebec_high_vowel_is_tense_once_the_numeral_consonant_falls():
    # Hall 2016: 7, ex. (11): a high vowel in an open final syllable is tense
    assert _say("dix livres", "fr-CA").split()[0] == "d͡zi"
    assert _say("huit livres", "fr-CA").split()[0] == "ɥi"


def _fr_fr_sounds_numeral_consonants():
    return _say("huit", "fr-FR") == "ɥit" and _say("dix", "fr-FR") == "dis"


#: The fr-FR numeral rules sound the final consonant of six, dix and huit
#: and drop or link it by sandhi. The cases below need those rules in the
#: parent and are skipped on a base whose fr-FR has none of them.
needs_numeral_rules = pytest.mark.skipif(
    not _fr_fr_sounds_numeral_consonants(),
    reason="fr-FR gives six, dix and huit no final consonant on this base")


@needs_numeral_rules
@pytest.mark.parametrize("tag, text, expected", [
    ("fr-BE", "huit", "wit"),                 # the consonant is there alone
    ("fr-BE", "huit livres", "wi livʁ"),      # and falls before a consonant
    ("fr-BE", "dix-huit", "diz wit"),
    ("fr-BE", "le huit juillet", "lə wit ʒwijɛ"),  # kept before a month
    ("fr-CA", "dix", "d͡zɪs"),                # lax in a closed final syllable
    ("fr-CA", "six", "sɪs"),
    ("fr-CA", "huit", "ɥɪt"),
    ("fr-CA", "dix livres", "d͡zi liːvʁ"),    # tense once the syllable opens
    ("fr-CA", "huit livres", "ɥi liːvʁ"),
    ("fr-CA", "six amis", "siz‿ ami"),
    ("fr-CA", "six insectes", "siz‿ ẽsɛkt"),  # [ẽ] opens a word
    ("fr-CA", "dix-huit", "d͡ziz ɥɪt"),
    ("fr-CA", "le dix novembre", "lə d͡zɪs nɔvɑ̃u̯bʁ"),
    ("fr-FR-x-midi", "le dix novembre", "lø dis nɔvambʁə"),
    ("fr-FR-x-midi", "dix octobre", "dis ɔktɔbʁə"),
    ("fr-FR-x-midi", "six enfants", "siz‿ aɱfaŋ"),
    ("fr-FR-x-midi", "huit chez moi", "ɥit ʃe mwa"),
    ("fr-FR-x-midi", "huit juifs", "ɥi ʒɥif"),    # juin, juillet: whole words
])
def test_numeral_consonant_and_its_sandhi(tag, text, expected):
    assert _say(text, tag) == expected


@pytest.mark.parametrize("tag, expected", [
    ("fr-CA", "nœv‿ ay̯ʁ"), ("fr-FR-x-midi", "nœv‿ œʁə"),
])
def test_neuf_heures_takes_v_before_the_regional_heures(tag, expected):
    assert _say("neuf heures", tag) == expected


@pytest.mark.parametrize("text, expected", [
    ("pointe", "pwɛ̃i̯t"),         # ⟨oin⟩ in a closed final syllable:
    ("joindre", "ʒwɛ̃i̯dʁ"),       # Dumas 1974: 21-22, Table II
    ("moins", "mwẽ"),             # open: short [ẽ]
    ("patience", "pasjɑ̃u̯s"),     # the ending -tience
])
def test_quebec_nasal_units_and_endings(text, expected):
    assert _say(text, "fr-CA") == expected


@pytest.mark.parametrize("text, expected", [
    ("élection", "elɛksjɔŋ"),     # the endings -tion, -stion, -tience
    ("question", "kɛstjɔŋ"),      # take the appendix (Eychenne 2006: 115)
    ("patience", "pasjansə"),
])
def test_midi_nasal_endings_take_the_appendix(text, expected):
    assert _say(text, MIDI) == expected


def test_the_midi_spec_lists_a_reference_url():
    assert o2i.get(MIDI).urls


# --- the ⟨uin⟩ unit ---------------------------------------------------------

#: fr-FR reads ⟨uin⟩ as one unit, [ɥɛ̃], or [ɥin] before a vowel (juin,
#: ruine). The cases below need that unit and are skipped on a base whose
#: fr-FR table has no ⟨uin⟩ entry; where it has one, they run, and
#: test_the_parent_reads_uin_as_one_unit checks the parent's reading.
needs_uin_unit = pytest.mark.skipif(
    "uin" not in o2i.get("fr-FR").graphemes,
    reason="fr-FR has no ⟨uin⟩ unit on this base")


@needs_uin_unit
def test_the_parent_reads_uin_as_one_unit():
    assert _say("juin", "fr-FR") == "ʒɥɛ̃"


@needs_uin_unit
@pytest.mark.parametrize("tag, text, expected", [
    ("fr-BE", "ruine", "ʁwin"),        # [w] for [ɥ] before [i]
    ("fr-BE", "juin", "ʒɥɛ̃"),         # not before [i]: [ɥ] kept
    ("fr-CA", "ruine", "ʁɥɪn"),        # lax in a closed final syllable
    ("fr-CA", "juin", "ʒɥẽ"),          # the close-mid front nasal
    ("fr-FR-x-midi", "ruine", "ʁɥinə"),  # final schwa after [n]
    ("fr-FR-x-midi", "juin", "ʒɥɛŋ"),    # oral vowel + appendix
])
def test_the_uin_unit_takes_the_regional_rules(tag, text, expected):
    assert _say(text, tag) == expected


@needs_uin_unit
@pytest.mark.parametrize("tag, text, expected", [
    ("fr-BE", "le huit juillet", "lə wit ʒwijɛ"),
    ("fr-BE", "le six juin", "lə sis ʒɥɛ̃"),
    ("fr-CA", "le six juin", "lə sɪs ʒɥẽ"),
    ("fr-CA", "le huit juillet", "lə ɥɪt ʒɥijɛ"),
    ("fr-FR-x-midi", "le huit juillet", "lø ɥit ʒɥije"),
    ("fr-FR-x-midi", "le six juin", "lø sis ʒɥɛŋ"),
])
def test_a_numeral_keeps_its_consonant_before_june_and_july(tag, text, expected):
    assert _say(text, tag) == expected


# --- nasal candidates, appendix before /f v/, loi de position contexts ------

@pytest.mark.parametrize("text, expected", [
    ("peine", "pɛn"),              # ⟨ein⟩ before a vowel keeps its [ɛn]
    ("pain", "pẽ"),                # the close-mid nasal stays reachable
])
def test_quebec_expanded_allophones_keep_the_front_nasal(text, expected):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        g2p = o2i.G2P("fr-CA", expand_allophones=True)
        assert g2p.transcribe(text) == expected


def test_quebec_hiers_reads_like_hier():
    assert _say("hiers", "fr-CA") == _say("hier", "fr-CA") == "jai̯ʁ"


def test_quebec_lists_a_reference_url():
    assert o2i.get("fr-CA").urls


def test_quebec_date_guard_holds_the_lax_aout():
    rule = [r for r in o2i.get("fr-CA").sandhi_rules
            if r.id == "FR_NUMERAL_Z_BEFORE_VOWEL"][0]
    import re
    assert not re.search(rule.right_context, "ʊt")
    assert re.search(rule.right_context, "ami")


@pytest.mark.parametrize("text, expected", [
    ("sainfoin", "sɛɱfwɛŋ"),       # the appendix is labiodental before [f]
    ("pain", "pɛŋ"),               # and velar at the end of a word
    ("perler", "pɛʁle"),           # [ʁl] closes the syllable (not an onset)
    ("Moscou", "mɔsku"),           # ⟨sc⟩ [sk] before a back vowel: closed
    ("escalier", "ɛskalje"),       # ⟨sc⟩ [sk]: closed
    ("aimer", "eme"),              # ⟨aim⟩ [ɛm] before a full vowel: close
    ("aime", "ɛmə"),               # before the final schwa: open
    ("peiner", "pene"),
])
def test_midi_appendix_and_loi_de_position_contexts(text, expected):
    assert _say(text, MIDI) == expected


def test_midi_sc_opens_a_syllable_only_where_it_reads_sk():
    # ⟨sc⟩ before a front vowel is one [s] (osciller, descendre), so the
    # rules that treat it as a cluster must name a back vowel or a
    # consonant after it.
    for rule in o2i.get(MIDI).allophone_rules:
        if "sc" in rule.followed_by_grapheme:
            assert rule.followed_by_2 in ("back_vowel", "consonant"), rule.id
