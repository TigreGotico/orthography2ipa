"""Cited-rule conformance: Ubykh (uby), Abkhaz-based Cyrillic orthography.

Ubykh never had a community orthography. The spelling this spec converts is
the Abkhaz-based Cyrillic system published as the Wiktionary Ubykh entry
guidelines (the "Ubykh (2022)" column of that page's alphabet table,
https://en.wiktionary.org/wiki/Wiktionary:Ubykh_entry_guidelines), which is
the convention every Ubykh headword in the reference gold set is written in.
Each test takes one claim from that table, or one epenthesis rule stated in
the spec's ``notes``, and proves the engine honours it on a real headword.

These are reproduction tests, not claims about Ubykh as spoken: the target is
the published transcription convention.
"""
from orthography2ipa.g2p import G2P


def _t(word):
    return G2P("uby").transcribe_word(word)


# ===========================================================================
# Secondary articulation is written with trailing modifier letters
# ===========================================================================


def test_uby_apostrophe_is_pharyngealization():
    """⟨б'⟩ = bˤ, ⟨ӷ'ә⟩ = ʁˤʷ — the apostrophe marks pharyngealisation and
    stacks with the labialisation letter ⟨ә⟩ (guidelines table rows
    "bˤ | Б' б'" and "ʁˤʷ | Ӷ'ә ӷ'ә")."""
    assert _t("Уаб'а") == "wabˤa"
    assert _t("Лаӷ'әа") == "laʁˤʷa"


def test_uby_soft_sign_is_palatalization():
    """⟨гь⟩ = ɡʲ, ⟨ӄь⟩ = qʲ — ⟨ь⟩ marks palatalisation (guidelines table rows
    "ɡʲ | Гь гь" and "qʲ ~ qʰʲ | Ӄь ӄь")."""
    assert _t("Алагьыӄә") == "alaɡʲəqʷ"
    assert _t("Адыгасеԥӄьы") == "adəɣase̞pʰqʲə"


def test_uby_schwa_letter_is_labialization():
    """⟨гә⟩ = ɡʷ, ⟨шә⟩ = ʃʷ, ⟨ӷә⟩ = ʁʷ — ⟨ә⟩ marks labialisation (guidelines
    table rows "ɡʷ | Гә гә", "ʃʷ | Шә шә", "ʁʷ | Ӷә ӷә")."""
    assert _t("Гәымзаӷ") == "ɡʷəmzaʁ"
    assert _t("Азӷашәабла") == "azʁaʃʷabla"


# ===========================================================================
# Abkhaz plosive convention: plain letter = ejective, descender = aspirate
# ===========================================================================


def test_uby_plain_plosive_letters_are_ejective():
    """⟨п т к⟩ = pʼ tʼ kʼ and ⟨ԥ ҭ қ⟩ = pʰ tʰ kʰ, inheriting the Abkhaz
    Cyrillic convention in which "the plosive letters к п т represent ejective
    consonants; the non-ejectives are derived from these by means of a
    descender" (Abkhaz alphabet, https://en.wikipedia.org/wiki/Abkhaz_alphabet;
    guidelines table rows "(pʼ) | П п" vs "pʰ | Ԥ ԥ", "tʼ | Т т" vs
    "tʰ | Ҭ ҭ", "(kʼ) | К к" vs "(kʰ) | Қ қ").

    This is the REVERSE of the Circassian convention, where the bare letter is
    the aspirate and the ejective carries a palochka.
    """
    assert _t("пԯьы") == "pʼɬʼə"
    assert _t("ԥса") == "pʰsa"
    assert _t("бат") == "batʼ"
    assert _t("ҭыҭ") == "tʰətʰ"
    assert _t("кады") == "kʼadə"
    assert _t("уоқ") == "wo̞kʰ"


def test_uby_uvular_letters():
    """⟨ҟ⟩ = qʼ against ⟨ӄ⟩ = q, and ⟨ҟ'ә⟩ = qˤʼʷ (guidelines table rows
    "qʼ | Ҟ ҟ", "q ~ qʰ | Ӄ ӄ", "qˤʼʷ | Ҟ'ә ҟ'ә")."""
    assert _t("Баҟҟәы") == "baqʼqʼʷə"
    assert _t("ӄаз") == "qaz"


# ===========================================================================
# Four sibilant series kept apart by letter shape
# ===========================================================================


def test_uby_sibilant_series():
    """⟨ш⟩ = ʂ against ⟨шь⟩ = ʃ against ⟨ҫ⟩ = ɕ, and ⟨ҽ⟩ = ʈʂʰ against
    ⟨ч⟩ = tʃʰ (guidelines table rows "ʂ | Ш ш", "ʃ | Шь шь", "ɕ (ṡ) | Ҫ ҫ",
    "ʈʂʰ ~ tʂʰ | Ҽ ҽ", "tʃʰ | Ч ч")."""
    assert _t("Ебзыш") == "e̞bzəʂ"
    assert _t("ашьа") == "aʃa"
    assert _t("ҫа") == "ɕa"
    assert _t("ҽан") == "ʈʂʰan"
    assert _t("ча") == "tʃʰa"


# ===========================================================================
# Vowels: two phonemes plus allophone spellings
# ===========================================================================


def test_uby_vowel_letters():
    """⟨а⟩ = a, ⟨аа⟩ = aː, ⟨ы⟩ = ə, with ⟨е⟩ and ⟨о⟩ spelling the allophones
    e̞ and o̞ (guidelines "Vowels" table: А а /a/, Ы ы /ə/, аа /aː/;
    "Allophones": Е е /e̞/, О о /o̞/)."""
    assert _t("Мыҫаакьа") == "məɕaːkʼʲa"
    assert _t("фы") == "fə"
    assert _t("ҭоԥ") == "tʰo̞pʰ"


# ===========================================================================
# Glide letters and the epenthetic /ə/ nucleus
# ===========================================================================


def test_uby_glide_after_consonant_takes_schwa_before_it():
    """⟨и⟩ = j and ⟨у⟩ = w are consonant letters; after another consonant the
    default nucleus /ə/ surfaces BEFORE the glide (spec notes: "before the
    glide after a consonant")."""
    assert _t("диа") == "dəja"
    assert _t("зуруԯ") == "zəwrəwɬ"
    assert _t("бзыкәи") == "bzəkʼʷəj"


def test_uby_glide_elsewhere_takes_schwa_after_it():
    """Word-initially, and after a vowel where no vowel follows, the epenthetic
    /ə/ surfaces AFTER the glide (spec notes: "after it otherwise")."""
    assert _t("Урысшәабла") == "wərəsʃʷabla"
    assert _t("ибадеҭ") == "jəbade̞tʰ"
    assert _t("арнауҭ") == "arnawətʰ"
    assert _t("блау") == "blawə"


def test_uby_intervocalic_glide_takes_no_schwa():
    """Between two vowels the glide is a plain onset and no epenthetic nucleus
    appears (spec notes: "not at all when the glide sits between two vowels")."""
    assert _t("ҟауа") == "qʼawa"
    assert _t("Уа") == "wa"


def test_uby_final_ou_is_a_plain_coda_glide():
    """Word-final ⟨оу⟩ is [o̞w] with no epenthetic nucleus: ⟨о⟩ already spells
    the rounded allophone (spec notes)."""
    assert _t("ӷәоу") == "ʁʷo̞w"
    assert _t("наноу") == "nano̞w"


# ===========================================================================
# Declared gap
# ===========================================================================


def test_uby_doubled_o_is_long():
    """Doubled ⟨оо⟩ is written [o̞ː], parallel to ⟨аа⟩ = aː. The guidelines
    table lists no long counterpart for the ⟨о⟩ allophone, so this length comes
    from the gold transcriptions, not from the published table (spec notes)."""
    assert _t("ӷәоомыл") == "ʁʷo̞ːməl"
    assert _t("хаироон") == "χajro̞ːn"


def test_uby_loanword_readings_are_not_spelling_decidable():
    """The guidelines table gives ⟨г⟩ and ⟨х⟩ two values each — (ɡ)/ɣ and
    (x)/χ — with nothing in the spelling to separate them. The spec takes the
    native value; the parenthesised loanword value is not reachable, and this
    pins that declared gap rather than hiding it."""
    assert _t("га") == "ɣa"
    # Two place names where the gold takes the OTHER value of each letter,
    # with nothing in the spelling to distinguish them from the native words.
    # The engine gives the native reading, and pinning the exact output makes
    # the gap visible instead of asserting a bare inequality.
    assert _t("Гурџьышәабла") == "ɣəwrdʒəʃʷabla"   # gold: ɡwərdʒəʃʷabla
    assert _t("дыхоу") == "dəχo̞w"   # gold: dəxo̞w
