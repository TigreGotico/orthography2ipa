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
from orthography2ipa.phonetok import IPAPath


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
    ("си́него", "nʲɪvə"),     # paired consonant softens before ⟨е⟩
    ("хорошего", "ʂɨvə"),     # ш is unconditionally hard, ⟨е⟩ -> [ɨ]
    ("рыжего", "ʐɨvə"),
    ("нашего", "ʂɨvə"),
])
def test_ego_desinence_is_v(word, tail):
    """-Cего is [Cʲɪvə], or [Cɨvə] after the unpaired hard ж ш ц.

    A soft-stem word carries its stem stress as a mark (си́него [си́ньвъ],
    Avanesov 1988, § 151, p. 678): unmarked, the penultimate default puts the
    stress on the desinence ⟨е⟩, and a stressed ⟨е⟩ is not [ɪ]."""
    out = _bare(word)
    assert out.endswith(tail), out
    assert "ɡ" not in out, out


def test_ego_keeps_preceding_palatalisation():
    """The per-consonant ending shape is load-bearing, not cosmetic.

    ⟨е⟩ palatalises the consonant before it, so a single bare ``"его"``
    ending would rewrite the whole tail and silently DELETE that
    palatalisation. синего must keep its [nʲ].
    """
    assert _bare("си́него") == "sʲinʲɪvə"


@pytest.mark.parametrize("word,tail", [
    ("тре́тьего", "tʲjɪvə"),
    ("пти́чьего", "tɕjɪvə"),
    ("ли́сьего", "sʲjɪvə"),
])
def test_soft_sign_ego_desinence(word, tail):
    """-Cьего keeps the soft sign's glide: [Cʲjɪvə]."""
    out = _bare(word)
    assert out.endswith(tail), out
    assert "ɡ" not in out, out


@pytest.mark.parametrize("word", ["бо́жьего", "медве́жьего", "вра́жьего"])
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


@pytest.mark.parametrize("word,expected", [
    ("иного", "ɪˈnovə"),
    ("какого", "kɐˈkovə"),
    ("большого", "bɐlʲˈʂovə"),
    ("другого", "drʊˈɡovə"),
    ("никакого", "nʲɪkɐˈkovə"),
])
def test_end_stressed_genitives_are_not_lexically_patched(word, expected):
    """The [ˈovə] class gets no word exceptions.

    These words stress the desinence (ино́го, како́го, большо́го, друго́го,
    никако́го), and no spelling rule can tell them from the stem-stressed
    но́вого or ста́рого. Patching one of them (иного was, briefly) to match a
    gold row while its twins stay wrong is gold-fitting, so none is patched.
    Unmarked, the penultimate default happens to put the stress on the
    desinence, and the stressed desinence vowel is the full [o]
    (Orfoepicheskii slovar' russkogo iazyka, ed. Avanesov 1988, § 151,
    p. 678: большо́го [бальшо́въ]).

    The DESINENTIAL ⟨г⟩ must still be [v] — that part IS rule-derivable.
    (Stem ⟨г⟩ is untouched: другого is [drʊˈɡovə], not *[drʊˈvovə].) The
    pretonic vowels follow akanje and ikanje as the spec notes state them.
    """
    from orthography2ipa.registry import get
    assert word not in (get("ru").word_exceptions or {})
    assert _t(word) == expected


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
    assert _bare("си́него").endswith("nʲɪvə")


# ===========================================================================
# The desinence vowels follow the stress
# ===========================================================================
#
# Orfoepicheskii slovar' russkogo iazyka, ed. R. I. Avanesov, 4th ed.,
# Moscow: Russkii iazyk, 1988, § 151, p. 678: "На месте буквы г в окончании
# -ого (-его) произносится звук [в]: [бальшо́въ] (большо́го), [бально́въ]
# (больно́го), [ста́ръвъ] (ста́рого), [си́ньвъ] (си́него), [каво́] (кого́),
# [чиᵉво́] (чего́), [фтаро́въ] (второ́го), [зна́фшъвъ] (зна́вшего)."
# Under desinential stress the first desinence vowel is a full [о]; the
# expected values map that transcription onto this spec's symbols (first
# pretonic [а] = [ɐ], [ъ] = [ə], ш = [ʂ]).

@pytest.mark.parametrize("word,expected", [
    ("большо́го", "bɐlʲˈʂovə"),   # [бальшо́въ]
    ("больно́го", "bɐlʲˈnovə"),   # [бально́въ]
    ("второ́го", "ftɐˈrovə"),     # [фтаро́въ]
    ("друго́го", "drʊˈɡovə"),
    ("дорого́го", "dərɐˈɡovə"),
])
def test_stressed_desinence_vowel_is_full(word, expected):
    """A marked stress on the desinence gives [ˈovə], never [ˈəvə]."""
    assert _t(word) == expected


def test_desinence_vowel_before_final_stress_is_first_pretonic():
    """самого́ stresses the last vowel, so the first desinence vowel is first
    pretonic: [ɐ], as in [каво́] (кого́), § 151, p. 678."""
    assert _t("самого́") == "səmɐˈvo"


_REDUCED = set("əɪɐʊ")


def _stressed_vowel(ipa):
    after = ipa.split("ˈ", 1)[1]
    return next(c for c in after if c in "aeiouɐəɪʊɨɛɔ")


@pytest.mark.parametrize("code", [
    "ru", "ru-x-moscow", "ru-x-ural", "ru-x-pskov", "ru-x-southern",
    "ru-x-don", "ru-x-kursk-orel", "ru-x-northern", "ru-x-vologda",
    "ru-x-arkhange", "ru-x-siberian",
])
@pytest.mark.parametrize("word", [
    "большо́го", "друго́го", "второ́го", "дорого́го", "самого́",
    "нового", "другого", "большого", "дорогого", "синего", "третьего",
    "горячего", "зодчего",
])
def test_desinence_rewrite_never_stresses_a_reduced_vowel(code, word):
    """No marked or unmarked input gets a stressed [ə ɪ ɐ ʊ] from the
    rewrite. Unmarked input takes the penultimate default, which can put the
    stress on the desinence; the vowel there must then be full too. In
    ru-x-pskov the path reads ⟨ч⟩ as [ts] and the stressed ⟨е⟩ after it as
    the allophone [ɛ], and the rewrite must still not keep the declared
    [ɪ] there."""
    out = G2P(code).transcribe_word(word)
    assert _stressed_vowel(out) not in _REDUCED, out



@pytest.mark.parametrize("code", ["ru", "ru-x-pskov"])
@pytest.mark.parametrize("word, tail", [
    ("горя́чего", "ˈrʲatɕɪvə"), ("зо́дчего", "tɕɪvə"),
])
def test_posttonic_desinence_after_ch_stays_front(code, word, tail):
    """A posttonic ⟨-чего⟩ keeps [ɪ] after the soft [tɕ] of the ending, as
    in си́него [си́ньвъ] (§ 151). ru-x-pskov reads ⟨ч⟩ as [ts] and ⟨е⟩
    after it as the allophone [ɨ]; that vowel belongs to [ts], which the
    declared ending replaces, so it does not reach the output."""
    assert G2P(code).transcribe_word(word).endswith(tail)


def test_pskov_stressed_desinence_after_ch_takes_the_table_vowel():
    """With the stress on the ending, ru-x-pskov gives the [e] the tables
    list for stressed ⟨е⟩, not the [ɛ] of its [ts] path. No standard word
    stresses ⟨-чего⟩; the unmarked default puts the stress there."""
    assert G2P("ru-x-pskov").transcribe_word("горячего").endswith("ˈtɕevə")

def test_southern_stressed_desinence_keeps_its_fricative():
    """The southern [ɣ] desinence follows the stress the same way."""
    assert G2P("ru-x-southern").transcribe_word("большо́го").endswith("ˈʂoɣə")


def test_rewrite_keeps_a_declared_value_whose_vowels_do_not_pair_up():
    """The declared vowels replace nothing unless each pairs with one vowel
    letter of the tail. Here [və] has one vowel for the two letters of
    ⟨ого⟩, so the [ə] stays even though the path reads the first ⟨о⟩ as a
    stressed [o]."""
    path = IPAPath(segments=("o", "ɡ", "ə"), score=0.0,
                   graphemes=("о", "г", "о"))
    assert G2P("ru")._ending_vowels_follow_stress(path, 3, "və") == "və"


def test_allophone_surface_maps_back_only_to_a_single_table_reading():
    """[ɛ] is the RU_HARD_BACK surface of [e] alone, so it maps back to
    [e]. [ɨ] is the surface of both [ɪ] and [i], so with both as readings
    no single vowel is the source and nothing is chosen."""
    g = G2P("ru")
    assert g._underlying_vowel("ɛ", frozenset({"e", "ɪ"})) == "e"
    assert g._underlying_vowel("ɨ", frozenset({"i", "ɪ"})) is None
    assert g._underlying_vowel("ɨ", frozenset({"e", "ɪ"})) == "ɪ"
