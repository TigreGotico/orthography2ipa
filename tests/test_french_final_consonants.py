"""French beat-espeak wave 2: final-consonant deletion behind the transparent
plural, the accented vowel digraphs, intervocalic ⟨y⟩, and the ⟨-ai⟩ aperture.

Every rule pinned here was found by a per-word differential against espeak-ng
on the full ``wikipron`` ``fr`` gold and then justified from the literature —
espeak is only the pointer to the phenomenon, never the justification:

* **Final-consonant deletion sees through the transparent suffix** — French
  drops the word-final consonant of a root, and the plural/verbal ⟨-s⟩/⟨-x⟩ is
  itself silent, so ⟨petit⟩ and ⟨petits⟩ are both [pəti] and ⟨mot⟩/⟨mots⟩ both
  [mo] (Tranel 1987 §3; Fouché 1959). The engine already knew ⟨-s⟩/⟨-x⟩ is a
  transparent grammatical suffix — the ⟨vie⟩/⟨vies⟩ case — but only let a
  VOWEL behind it count as effectively word-final; a consonant did not, so the
  root-final letter stayed audible in the plural.
* **The circumflex does not change a vowel digraph's value** — it marks a lost
  etymological ⟨s⟩ (⟨coste⟩ > ⟨coût⟩, ⟨aoust⟩ > ⟨août⟩, ⟨jeûne⟩ < ⟨jeusne⟩), so
  ⟨oû⟩ is ⟨ou⟩ [u], ⟨aî⟩ is ⟨ai⟩ [ɛ], ⟨eû⟩ is ⟨eu⟩ [ø]~[œ] and ⟨oî⟩ is ⟨oi⟩
  [wa] (Fouché 1959; Tranel 1987 ch. 2). The grave of ⟨où⟩ is the same digraph
  ⟨ou⟩ [u], written only to keep the relative/interrogative apart from the
  conjunction ⟨ou⟩ (Fouché 1959).
* **Intervocalic ⟨y⟩ counts as two ⟨i⟩** — the first joins the preceding vowel
  letter into that letter's own digraph, the second is the glide: ⟨royal⟩ =
  ⟨roi⟩+⟨ial⟩ [ʁwajal], ⟨payer⟩ [pɛje], ⟨appuyer⟩ [apɥije] (Fouché 1959;
  Tranel 1987 §5 on the glides; Walker 2001). Between a vowel and a consonant,
  or word-finally, there is no second ⟨i⟩ and the digraph alone surfaces:
  ⟨Roy⟩ [ʁwa], ⟨Puy⟩ [pɥi], ⟨Épinay⟩ [epinɛ].
* **⟨-ai⟩ at the word edge is close-mid** — [e] when nothing follows (⟨j'ai⟩,
  ⟨vrai⟩, ⟨quai⟩, the futures ⟨chanterai⟩), against [ɛ] as soon as a consonant
  letter follows, pronounced or not (⟨mais⟩, ⟨lait⟩, ⟨français⟩, the
  conditionals ⟨chanterais⟩) — the loi de position stated for the word's last
  syllable (Walker 2001; Fouché 1959). The condition is the TRUE word edge,
  not the "effectively final" one: the transparent ⟨-s⟩ of ⟨-ais⟩ must NOT
  make that ending look final, or every conditional turns into a future.

Each rule has an adversarial counter-case: a word in the same neighbourhood
where it must NOT fire.
"""
import pytest

from orthography2ipa import transcribe


def _t(word):
    return transcribe(word, "fr-FR")


# ── final-consonant deletion behind the transparent plural ────────────────

@pytest.mark.parametrize("singular,plural,expected", [
    ("mot", "mots", "mo"),
    ("petit", "petits", "pəti"),
    ("nid", "nids", "ni"),
    ("drap", "draps", "dʁa"),
])
def test_silent_final_consonant_stays_silent_under_the_plural(
        singular, plural, expected):
    """The plural ⟨-s⟩ is itself silent, so the root-final consonant is still
    the last audible slot and still drops (Tranel 1987 §3; Fouché 1959)."""
    assert _t(singular) == expected
    assert _t(plural) == expected


def test_temps_drops_the_p_behind_the_s():
    """⟨temps⟩ [tɑ̃]: ⟨p⟩ is the root-final consonant, ⟨s⟩ the transparent
    suffix behind it (Tranel 1987 §3)."""
    assert _t("temps") == "tɑ̃"


def test_only_the_letter_next_to_the_suffix_is_reached():
    """COUNTER-CASE — the rule promotes exactly ONE slot. In ⟨corps⟩ the ⟨p⟩
    is silenced but the ⟨r⟩ behind it is not word-final and keeps its [ʁ],
    which is also the pronunciation French has (Fouché 1959)."""
    assert _t("corps") == "kɔʁ"


def test_a_pronounced_final_consonant_is_not_silenced_by_the_suffix():
    """COUNTER-CASE — word-final ⟨r⟩ is [ʁ] in French, and being promoted to
    word-final position must not change that: ⟨toujours⟩ [tuʒuʁ]."""
    assert _t("toujours") == "tuʒuʁ"


@pytest.mark.parametrize("word,expected", [
    ("DS", "d"),
    ("PS", "p"),
    ("ts", "t"),
    ("ps", "p"),
    ("pts", "p"),
])
def test_the_promotion_never_empties_the_word(word, expected):
    """COUNTER-CASE, and a regression pin. A ``word_final`` entry is usually
    a SILENCING one, so promoting the slot in front of a transparent suffix
    can delete the last thing a word has: ⟨DS⟩ and ⟨ts⟩ are a silenced
    consonant plus a silenced suffix and nothing else, and an unfloored
    promotion transcribed them as the empty string. The harness drops an
    empty hypothesis from coverage rather than scoring it, so this would
    have flattered PER instead of failing loudly. The floor is the word's
    first slot: with nothing audible in front of it there is no root for
    the suffix to be transparent to, which is not the ⟨petit⟩/⟨petits⟩ fact
    the position states (Tranel 1987 §3)."""
    assert transcribe(word, "fr-FR") == expected


def test_the_floor_also_covers_a_vowel_first_slot():
    """The same floor applies to the pre-existing vowel branch, where the
    empty-word bug was already reachable on ``dev``: ⟨es⟩ and ⟨ex⟩ both
    transcribed as the empty string there."""
    assert transcribe("es", "fr-FR") == "ɛ"
    assert transcribe("ex", "fr-FR") == "ɛ"


def test_the_vowel_case_of_the_transparent_suffix_is_unchanged():
    """COUNTER-CASE — the pre-existing vowel branch (⟨vie⟩/⟨vies⟩, ⟨pied⟩/
    ⟨pieds⟩) keeps its answers byte-for-byte."""
    assert _t("vie") == _t("vies") == "vi"
    assert _t("pied") == _t("pieds") == "pjɛ"


# ── the circumflex/grave vowel digraphs ───────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("goût", "ɡu"),
    ("goûts", "ɡu"),
    ("coûte", "kut"),
    ("voûte", "vut"),
    ("soûl", "sul"),
    ("où", "u"),
])
def test_ou_keeps_its_value_under_the_circumflex_and_the_grave(word, expected):
    """⟨oû⟩/⟨où⟩ are the digraph ⟨ou⟩ [u]; the accent marks a lost ⟨s⟩ or
    separates a homophone, and changes nothing about the vowel (Fouché 1959;
    Tranel 1987 ch. 2)."""
    assert _t(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("naît", "nɛ"),
    ("faîtes", "fɛt"),
    ("jeûne", "ʒøn"),
    ("cloître", "klwatʁ"),
    ("maître", "mɛtʁ"),
])
def test_the_other_circumflexed_digraphs(word, expected):
    """⟨aî⟩ = ⟨ai⟩ [ɛ], ⟨eû⟩ = ⟨eu⟩ [ø], ⟨oî⟩ = ⟨oi⟩ [wa] (Fouché 1959;
    Tranel 1987 ch. 2)."""
    assert _t(word) == expected


def test_the_single_circumflexed_letters_are_untouched():
    """COUNTER-CASE — the claim is about the DIGRAPHS. A circumflexed letter
    on its own keeps the value it already had: ⟨île⟩ [il], ⟨fête⟩ [fɛt]."""
    assert _t("île") == "il"
    assert _t("fête") == "fɛt"


def test_the_unaccented_spellings_are_untouched():
    """COUNTER-CASE — ⟨ou⟩ was already [u] and the reformed ⟨gout⟩ was already
    right; the new keys must not disturb them."""
    assert _t("ou") == "u"
    assert _t("nous") == "nu"
    assert _t("gout") == "ɡu"


# ── intervocalic ⟨y⟩ = two ⟨i⟩ ────────────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("royal", "ʁwajal"),
    ("voyer", "vwaje"),
    ("noyer", "nwaje"),
    ("croyons", "kʁwajɔ̃"),
    ("appuyer", "apɥije"),
    ("tuyau", "tɥijo"),
    ("payer", "pɛje"),
    ("rayon", "ʁɛjɔ̃"),
    ("asseyez", "asɛje"),
])
def test_intervocalic_y_is_digraph_plus_yod(word, expected):
    """Before a vowel letter, ⟨oy uy ay ey⟩ are ⟨oi ui ai ei⟩ plus the glide
    (Fouché 1959; Tranel 1987 §5; Walker 2001)."""
    assert _t(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("Roy", "ʁwa"),
    ("Puy", "pɥi"),
    ("Épinay", "epinɛ"),
])
def test_non_prevocalic_y_contributes_no_yod(word, expected):
    """COUNTER-CASE — with no following vowel letter there is no second ⟨i⟩,
    so only the digraph surfaces and no [j] is added."""
    assert _t(word) == expected


# ── ⟨-ai⟩ aperture at the true word edge ──────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("ai", "e"),
    ("vrai", "vʁe"),
    ("quai", "ke"),
    ("chanterai", "ʃɑ̃təʁe"),
])
def test_word_final_ai_is_close_mid(word, expected):
    """⟨ai⟩ with nothing after it is [e] (Walker 2001; Fouché 1959)."""
    assert _t(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("mais", "mɛ"),
    ("lait", "lɛ"),
    ("français", "fʁɑ̃sɛ"),
    ("chanterais", "ʃɑ̃təʁɛ"),
    ("chanterait", "ʃɑ̃təʁɛ"),
])
def test_ai_before_any_final_consonant_letter_stays_open_mid(word, expected):
    """COUNTER-CASE, and the reason the rule is conditioned on the TRUE word
    edge rather than on the effectively-final position: the transparent ⟨-s⟩
    of ⟨-ais⟩ must not make the conditional look like the future. Stating the
    same claim as a ``word_final`` positional entry gave ⟨mais⟩ *[me] and
    ⟨français⟩ *[fʁɑ̃se] and measured 0.0707 against 0.0673 on the full
    wikipron fr gold."""
    assert _t(word) == expected
