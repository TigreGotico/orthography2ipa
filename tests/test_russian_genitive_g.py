"""Cited-rule conformance: the Russian genitive desinence ⟨-ого/-его⟩ = [v].

The ``ru`` spec's ``notes`` have always described this rule::

    Г IN GENITIVE: -ого/-его endings: г->[v] (его=[jɪvo])

but until the ``grammatical_endings``/``word_exceptions`` blocks were added
the tables did not implement it — ``его`` transcribed as ``[ˈjeɡə]``. These
tests pin the rule, and — more importantly — pin the COUNTER-CASES that stop
it from being applied as a blind word-final string rewrite.

Citations, all independent of any gold set:

* Timberlake, A. (2004) *A Reference Grammar of Russian*, CUP — the
  adjectival/pronominal genitive singular desinence is pronounced with [v].
* Avanesov, R. I. (1956) *Russkoe literaturnoe proiznoshenie* — same rule,
  prescriptive Moscow norm; also ⟨е⟩ = [ɨ] after the unpaired hard
  consonants ж ш ц.
* Jones, D. & Ward, D. (1969) *The Phonetics of Russian*, CUP.

No page locators are given: these works were not consulted directly, and the
year for Avanesov is the one the spec already carried (several editions of
that title exist; none was verified here).
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(word):
    return G2P("ru").transcribe_word(word)


def _bare(word):
    return _t(word).replace("ˈ", "").replace("ˌ", "")


# ===========================================================================
# The rule fires on real genitive desinences
# ===========================================================================

@pytest.mark.parametrize("word", [
    "красного", "нового", "большого", "русского", "абсолютного",
])
def test_ogo_desinence_is_v(word):
    """-ого is [v], never [ɡ] (Timberlake 2004; Avanesov 1956)."""
    out = _bare(word)
    assert out.endswith("və"), out
    assert "ɡ" not in out, out


@pytest.mark.parametrize("word,tail", [
    ("синего", "nʲɪvə"),      # paired consonant softens before ⟨е⟩
    ("хорошего", "ʂɨvə"),     # ш is unconditionally hard, ⟨е⟩ -> [ɨ]
    ("рыжего", "ʐɨvə"),
    ("нашего", "ʂɨvə"),
])
def test_ego_desinence_is_v(word, tail):
    """-Cего is [Cʲɪvə], or [Cɨvə] after the unpaired hard ж ш ц."""
    out = _bare(word)
    assert out.endswith(tail), out
    assert "ɡ" not in out, out


def test_ego_keeps_preceding_palatalisation():
    """The per-consonant ending shape is load-bearing, not cosmetic.

    ⟨е⟩ palatalises the consonant before it, so a single bare ``"его"``
    ending would rewrite the whole tail and silently DELETE that
    palatalisation. синего must keep its [nʲ].
    """
    assert _bare("синего") == "sʲɪnʲɪvə"


@pytest.mark.parametrize("word,tail", [
    ("третьего", "tʲjɪvə"),
    ("птичьего", "tɕjɪvə"),
    ("лисьего", "sʲjɪvə"),
])
def test_soft_sign_ego_desinence(word, tail):
    """-Cьего keeps the soft sign's glide: [Cʲjɪvə]."""
    out = _bare(word)
    assert out.endswith(tail), out
    assert "ɡ" not in out, out


@pytest.mark.parametrize("word", ["божьего", "медвежьего", "вражьего"])
def test_zhego_soft_sign_desinence(word):
    """-жьего is [ʐjɪvə] — the glide SURVIVES.

    The ⟨ь⟩ here is the separating soft sign and carries a stem /j/ before
    the desinence. ⟨ж⟩ being unpaired-hard governs the CONSONANT only: it
    stays [ʐ] and never palatalises, but it does not delete the glide, and
    the vowel after /j/ is [ɪ] rather than the hard-sibilant [ɨ] of bare
    -жего (Avanesov 1956; Timberlake 2004).

    Evidence, and its limits. The 75-of-75 [ʐj] count that fixes the VALUE
    is about the ⟨жь⟩+vowel sequence generally (ружьё, Запорожье), NOT about
    the genitive desinence: ⟨-жьего⟩ matches zero gold types, so this is a
    zero-coverage entry like сьего and ньего, kept because the
    possessive-adjective declension is productive rather than because any
    row measures it.

    Those two words are also not engine output — the base grapheme tables
    still lose the ⟨жь⟩ glide (ружьё -> [rʊˈʐɵ] against a gold of [rʊʐjɵ]).
    This ending patches the desinence only; the general gap is a separate
    open defect and is deliberately not fixed here.

    Regression guard, two ways: before this entry existed these words fell
    through to the bare grapheme tables and came out doubly wrong —
    [bɐʐɨɡə], keeping the plosive AND losing the desinence. The first fix
    for that was ALSO wrong ([ʐɨvə]), deleting the glide by over-applying
    ⟨ж⟩'s hardness to it.
    """
    out = _bare(word)
    assert out.endswith("ʐjɪvə"), out
    assert "ɡ" not in out, out
    assert "ʐɨ" not in out, f"hardness must not eat the glide: {out}"


def test_removed_endings_stay_removed():
    """The 15-paired-consonant -Cего set must NOT come back.

    Russian soft-stem adjectives are essentially the -ний type only, so
    endings like "бего" or "хего" assert a morphology the language does not
    have. They matched zero words in the 403,873 wikipron gold types and
    were removed; re-adding them would be citing a rule into existence.
    """
    from orthography2ipa.registry import get
    endings = get("ru").grammatical_endings or {}
    impossible = ["бего", "вего", "гего", "дего", "зего", "кего", "лего",
                  "мего", "пего", "рего", "тего", "фего", "хего"]
    present = [e for e in impossible if e in endings]
    assert not present, f"morphologically impossible endings present: {present}"


@pytest.mark.parametrize("word", ["иного", "какого", "большого", "другого",
                                  "никакого"])
def test_stem_stressed_genitives_are_not_lexically_patched(word):
    """The stem-stressed [ovə] class is deliberately left to the ceiling.

    These are structural twins: all take stem stress, none is derivable from
    spelling. Patching one of them (иного was, briefly) to match a gold row
    while its twins stay wrong is gold-fitting, so none is patched. They all
    get the reduced desinence and are booked as stress-ceiling error.

    The DESINENTIAL ⟨г⟩ must still be [v] — that part IS rule-derivable.
    (Stem ⟨г⟩ is untouched: другого is [drʊɡəvə], not *[drʊvəvə].)
    """
    out = _bare(word)
    assert out.endswith("əvə"), out
    assert not out.endswith("ɡə"), out


# ===========================================================================
# COUNTER-CASES — word-final -ого that is NOT a genitive desinence
# ===========================================================================

@pytest.mark.parametrize("word,expected", [
    ("много", "mnoɡə"),
    ("немного", "nʲɪmnoɡə"),
    ("намного", "nɐmnoɡə"),
    ("дорого", "dorəɡə"),
    ("недорого", "nʲɪdorəɡə"),
    ("строго", "stroɡə"),
    ("убого", "ʊboɡə"),
    ("лого", "ɫoɡə"),
])
def test_non_desinential_ogo_keeps_g(word, expected):
    """Adverbs and nouns merely ENDING in -ого keep the plosive [ɡ].

    This is the adversarial case for the whole feature: a blind word-final
    ``-ого -> -ово`` rewrite turns много into *[mnəvə]. The [ɡ] words are a
    closed lexical class (adverbs in -о on stems in -г, plus a few nouns),
    not separable from genitives by spelling, so they are enumerated in
    ``word_exceptions``.
    """
    assert _bare(word) == expected


# ===========================================================================
# Pronouns — desinential stress the penultimate default cannot place
# ===========================================================================

@pytest.mark.parametrize("word,expected", [
    ("его", "jɪˈvo"),
    ("него", "nʲɪˈvo"),
    ("кого", "kɐˈvo"),
    ("того", "tɐˈvo"),
    ("всего", "fsʲɪˈvo"),
    ("чего", "tɕɪˈvo"),
    ("одного", "ɐdnɐˈvo"),
    ("моего", "məjɪˈvo"),
    ("ничьего", "nʲɪtɕjɪˈvo"),
    ("сего", "sʲɪˈvo"),
])
def test_pronoun_genitive_has_desinential_stress(word, expected):
    """The closed pronoun set stresses the desinence: [jɪˈvo], not [ˈjɪvə].

    сего is here for a second reason too: an ending equal to the WHOLE word
    can never fire (a match must leave a nonempty head — see
    positional.match_grammatical_ending), so the "сего" ending covers всего
    but not сего itself, which needs its own exception.

    ``ru`` declares no stress rules (Russian stress is lexical and free), so
    the engine falls back to a statistical penultimate default. That default
    is wrong for every one of these, and no spelling-derivable rule can fix
    it — hence a closed, enumerated pronoun list.
    """
    assert _t(word) == expected


def test_word_exceptions_outrank_grammatical_endings():
    """Precedence is load-bearing: ``него`` matches BOTH a -Cего ending and a
    ``word_exceptions`` entry, and the exception must win."""
    assert _t("него") == "nʲɪˈvo"
    # ...while the same ending still fires on a word with no exception.
    assert _bare("синего").endswith("nʲɪvə")
