"""Family-level coverage for the Kipchak/South-Siberian Turkic Cyrillic
specs added in the turkic-uralic language wave: Kumyk (kum), Nogai (nog),
Khakas (kjh), Shor (cjs).

Words are real, attested forms with a cited gloss/source; IPA is derived
independently from each spec's own cited grapheme table (see kum.json /
nog.json / kjh.json / cjs.json ``sources``), not read back from the engine.
"""
import orthography2ipa


def _tw(code, word):
    return orthography2ipa.G2P(code).transcribe_word(word)


# --- Kumyk (kum) ------------------------------------------------------------
# "Бир къарт гиши болгъан..." ("There was an old man...") is a widely
# reproduced Kumyk folktale opening (languagehat.com / Grokipedia, "Kumyk
# language"): бир "one", къарт "old", гиши "man/person" are pan-Turkic /
# pan-Kipchak cognates (cf. Turkish bir, Kazakh qart, Turkish kişi).

def test_kumyk_bir_one():
    assert _tw("kum", "бир") == "bir"


def test_kumyk_qart_old():
    assert _tw("kum", "къарт") == "qart"


def test_kumyk_gishi_person():
    assert _tw("kum", "гиши") == "ɡiʃi"


# --- Nogai (nog) --------------------------------------------------------
# "Йок" (no) and "Салам" (hello, from Arabic salam) are attested on the
# Omniglot Nogai phrasebook (omniglot.com/language/phrases/nogai.php).

def test_nogai_yok_no():
    assert _tw("nog", "йок") == "jok"


def test_nogai_salam_hello():
    assert _tw("nog", "салам") == "salam"


# --- Khakas (kjh) --------------------------------------------------------
# "кізі" (person/human being) is attested in the Khakas UDHR Article 1
# translation (ohchr.org/en/human-rights/universal-declaration/translations/khakas):
# "Полған на кiзi ... тöрiпче" = "All human beings are born ..." — the source
# text renders the letter ⟨і⟩ visually indistinguishably from Latin "i"; the
# actual Khakas alphabet letter is Cyrillic і (U+0456), used here.

def test_khakas_kizi_person():
    assert _tw("kjh", "кізі") == "kɘzɘ"


# --- Shor (cjs) -----------------------------------------------------------
# "кижи" (human being) and "туғча" (is born) are attested in the Shor
# UDHR Article 1 translation reproduced on omniglot.com/writing/shor.htm:
# "Парчын кижи, по чарыққа туғчадып, тең, пош туғча" = "All human beings
# are born free and equal ...". Front ⟨к⟩ realises /c/, back ⟨ғ⟩ realises /ɡ/.

def test_shor_kizhi_person():
    assert _tw("cjs", "кижи") == "ciʒi"


def test_shor_tugcha_is_born():
    assert _tw("cjs", "туғча") == "tuɡtʃa"
