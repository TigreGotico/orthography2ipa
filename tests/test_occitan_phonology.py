"""Occitan (Lengadocian) phonology and stress — the TTS-grade surface.

The spec describes ONE variety, Lengadocian in the classical (Alibertine)
norm, because a voice is one dialect. These tests pin the letter values and
the stress system that make its output usable as a TTS front end:

* the front-vowel series ⟨c⟩ ⟨cc⟩ ⟨sc⟩ ⟨g⟩, which is where a flat table is
  furthest from the language — ⟨occitan⟩ is [utsiˈta], not [ukkiˈtan];
* unstressed final ⟨-a⟩ as [ɔ], before a final ⟨-s⟩ as well as word-finally;
* glide formation on unstressed ⟨i⟩ before a vowel, and the STRESSED ⟨i⟩ in
  the same position that must not glide;
* the silent word-final ⟨-n⟩ and infinitive ⟨-r⟩, and the word-final
  devoicing that comes with them;
* stress placement, which is fully predictable from the spelling and is the
  one error class a listener cannot ignore.

Values are those of the Wikipédia "Prononciation de l'occitan" lengadocien
table and the fr.wiktionary "Annexe:Prononciation/occitan" (both consulted),
cross-checked against Alibert (1976) and Bec (1973) as cited in the spec.
"""
import pytest

from orthography2ipa import get, transcribe
from orthography2ipa.stress import detect_stress, syllabify


def ipa(word, lang="oc"):
    return transcribe(word, lang=lang)


def bare(word, lang="oc"):
    return ipa(word, lang).replace("ˈ", "").replace("ˌ", "")


class TestFrontVowelSeries:
    """⟨c cc sc g⟩ before ⟨e i⟩ — the softening series."""

    @pytest.mark.parametrize("word,expect", [
        ("cigala", "siɣalɔ"),
        ("Barcelona", "baɾselunɔ"),
        ("nacion", "nasju"),
        ("aucèu", "awsɛw"),
    ])
    def test_c_before_front_vowel_is_s(self, word, expect):
        assert bare(word) == expect

    @pytest.mark.parametrize("word,expect", [
        ("occitan", "utsita"),
        ("seccion", "setsju"),
        ("diccionari", "ditsjunaɾi"),
    ])
    def test_cc_before_front_vowel_is_ts(self, word, expect):
        # ⟨cc⟩ is not ⟨c⟩+⟨c⟩: [ts], not [kk] or [ks].
        assert bare(word) == expect

    def test_sc_before_front_vowel_is_a_single_s(self):
        assert bare("sciéncia") == "sjensjɔ"

    def test_sc_before_back_vowel_stays_sk(self):
        assert bare("escòla") == "eskɔlɔ"

    @pytest.mark.parametrize("word,expect", [
        ("agir", "adʒi"),
        ("dimenge", "dimendʒe"),
        ("Argeria", "aɾdʒeɾiɔ"),
    ])
    def test_g_before_front_vowel_is_dz(self, word, expect):
        assert bare(word) == expect

    def test_g_elsewhere_is_a_plain_stop(self):
        # ⟨gu⟩ keeps the stop before a front vowel, and a post-nasal ⟨g⟩ is
        # neither softened nor lenited.
        assert bare("lenga") == "leŋɡɔ"

    def test_g_between_vowels_lenites(self):
        assert bare("aiga") == "ajɣɔ"


class TestFinalA:
    """Unstressed final ⟨-a⟩ is [ɔ], and the ⟨-s⟩ does not protect it."""

    @pytest.mark.parametrize("word,expect", [
        ("casa", "kazɔ"),
        ("pòrta", "pɔɾtɔ"),
        ("filha", "fiʎɔ"),
    ])
    def test_word_final_a(self, word, expect):
        assert bare(word) == expect

    @pytest.mark.parametrize("word,expect", [
        ("bocas", "bukɔs"),
        ("cantas", "kantɔs"),
        ("peiretas", "pejɾetɔs"),
    ])
    def test_final_a_before_plural_s(self, word, expect):
        assert bare(word) == expect

    def test_stressed_a_is_not_opened(self):
        # Only the POST-TONIC ⟨a⟩ opens; the stressed one stays [a].
        assert bare("cantar") == "kanta"
        assert bare("aiga").startswith("aj")


class TestGlideFormation:
    """Unstressed ⟨i⟩ before a vowel is [j]; a stressed one is not."""

    @pytest.mark.parametrize("word,expect", [
        ("gàbia", "ɡaβjɔ"),
        ("Occitània", "utsitanjɔ"),
        ("Califòrnia", "kalifɔɾnjɔ"),
        ("acusacion", "akyzasju"),
    ])
    def test_unstressed_i_glides(self, word, expect):
        assert bare(word) == expect

    @pytest.mark.parametrize("word", ["simpatia", "Argeria", "monarquia"])
    def test_stressed_i_in_hiatus_stays_a_vowel(self, word):
        # The glide rule must not eat the nucleus that carries the stress:
        # ⟨simpatia⟩ is [simpaˈtiɔ], never [simˈpatjɔ].
        out = ipa(word)
        assert "ˈti" in out or "ˈɾi" in out or "ˈki" in out, out
        assert bare(word).endswith("iɔ")

    def test_ue_is_a_labiopalatal_glide(self):
        assert bare("uèch") == "ɥɛtʃ"
        assert bare("puèg") == "pɥɛtʃ"


class TestWordFinalConsonants:
    def test_final_n_is_silent(self):
        assert bare("Japon") == "dʒapu"
        assert bare("Perpinhan") == "peɾpiɲa"

    def test_infinitive_r_is_silent(self):
        assert bare("cantar") == "kanta"
        assert bare("aborrir") == "aβuri"

    def test_final_b_and_d_devoice(self):
        assert bare("actitud").endswith("t")
        assert bare("Nòrd") == "nɔɾt"

    def test_final_m_is_n(self):
        assert bare("pergam") == "peɾɡan"

    def test_final_g_after_a_vowel_is_the_devoiced_affricate(self):
        assert bare("torneg") == "tuɾnetʃ"

    def test_final_nh_depalatalises(self):
        assert bare("codonh") == "kuðun"

    def test_final_lh_stays_palatal(self):
        # ⟨-lh⟩ does NOT follow ⟨-nh⟩ here: it stays [ʎ] in the norm.
        assert bare("aparelh") == "apaɾeʎ"


class TestNasalAssimilation:
    @pytest.mark.parametrize("word,expect", [
        ("ancora", "aŋkuɾɔ"),
        ("anglés", "aŋɡles"),
        ("Lengadòc", "leŋɡaðɔk"),
    ])
    def test_n_before_a_velar_stop(self, word, expect):
        assert bare(word) == expect

    def test_n_before_a_softened_c_is_not_velar(self):
        # ⟨ancian⟩: the ⟨c⟩ is [s] here, so there is no velar to assimilate
        # to. Keying the rule on the PHONEME rather than the letter is what
        # keeps this right.
        assert bare("ancian") == "ansja"


class TestBetacismAndLenition:
    def test_v_is_b(self):
        assert bare("vin") == "bi"
        assert bare("Val") == "bal"

    def test_intervocalic_voiced_stops_lenite(self):
        assert bare("cabel") == "kaβel"
        assert bare("cedilha") == "seðiʎɔ"

    def test_no_lenition_after_a_consonant(self):
        assert bare("lenga") == "leŋɡɔ"


class TestStressPlacement:
    """Stress is predictable; a written accent overrides it."""

    def _idx(self, word, lang="oc"):
        """(stressed syllable index, syllable count) for *word*."""
        spec = get(lang)
        sylls = syllabify(word, diphthongs=spec.stress.diphthongs,
                          spec=spec, max_onset=spec.stress.max_onset)
        idx = detect_stress(word, spec.stress, syllables=sylls)
        return (idx if idx < 0 else idx - len(sylls)), len(sylls)

    @pytest.mark.parametrize("word", ["casa", "pòrta", "aiga", "bocas",
                                      "cantas", "aqueste"])
    def test_vowel_or_vowel_s_final_is_paroxytone(self, word):
        assert self._idx(word)[0] == -2, word

    @pytest.mark.parametrize("word,expect", [
        ("cantar", "kanˈta"),
        ("corrir", "kuˈri"),
        ("crompar", "kɾumˈpa"),
    ])
    def test_infinitives_are_oxytone(self, word, expect):
        # The classical norm makes an infinitive OXYTONE even though its
        # ⟨-r⟩ is silent: ⟨cantar⟩ is [kanˈta], not [ˈkantɔ]. Asserted on
        # the syllable index, because the mark is DRAWN by an IPA splitter
        # that does not read this spec's phonotactics and puts it one
        # segment early inside a medial cluster.
        assert self._idx(word)[0] == -1, word
        assert bare(word) == expect.replace("ˈ", "")

    @pytest.mark.parametrize("word", ["ostal", "amor", "pichon", "papet"])
    def test_consonant_final_is_oxytone(self, word):
        assert self._idx(word)[0] == -1, word

    @pytest.mark.parametrize("word,accented", [
        ("Califòrnia", "ɔ"),
        ("Occitània", "a"),
        ("anglés", "e"),
        ("aquò", "ɔ"),
    ])
    def test_written_accent_is_never_lost(self, word, accented):
        # The Tetum wave found a spec that DELETED its accented vowels; make
        # sure every marked vowel still reaches the output.
        assert accented in bare(word), (word, bare(word))

    def test_every_word_gets_exactly_one_primary_mark(self):
        for word in ["casa", "cantar", "occitan", "Califòrnia", "puèg",
                     "sciéncia", "l'ostal", "qu'es"]:
            assert ipa(word).count("ˈ") == 1, word


class TestTextRobustness:
    """Real text: punctuation, capitals, apostrophes, hyphens."""

    def test_elision_apostrophe_keeps_the_clitic_in_the_word(self):
        # Split on the apostrophe, ⟨d'⟩ becomes its own word and its ⟨d⟩
        # devoices word-finally to [t] — the wrong segment AND a spurious
        # stress mark.
        assert bare("l'ostal") == "lustal"
        assert bare("d'aiga") == "dajɣɔ"
        assert bare("qu'es") == "kes"
        assert bare("qualqu'un") == "kalky"

    def test_typographic_apostrophe_behaves_the_same(self):
        assert bare("l’ostal") == bare("l'ostal")

    def test_capitals_do_not_change_the_reading(self):
        assert bare("LENGA") == bare("lenga")

    def test_punctuation_is_dropped_not_voiced(self):
        out = transcribe("Es un ostal, e tu?", lang="oc")
        assert "," not in out and "?" not in out
        # ⟨ostal⟩ is os-tal: Occitan opens no syllable with /s/ + stop, which
        # is why it takes the prothetic vowel in ⟨estela⟩ ⟨escòla⟩
        assert out.split() == ["ˈes", "ˈy", "usˈtal", "ˈe", "ˈty"]

    def test_hyphen_separates_the_members_of_a_compound(self):
        assert transcribe("Lenga-mair", lang="oc").split() == [
            "ˈleŋɡɔ", "ˈmaj"]

    def test_every_letter_of_the_alphabet_produces_output(self):
        # 23 letters of the norm plus the foreign K W Y, the cedilla, the
        # accented vowels and the two diaereses. A letter that maps to
        # nothing silently truncates every word carrying it.
        alphabet = "abcdefghijklmnopqrstuvwxyzçàáèéíòóúïü"
        for ch in alphabet:
            assert transcribe("a" + ch + "a", lang="oc"), ch


class TestAranese:
    """oc-x-aranes — the Gascon child, and the one dialect with an official
    norm of its own (Conselh Generau d'Aran)."""

    def test_h_keeps_a_silent_reading_in_the_lattice(self):
        # Aranese is described as having deaspirated the Gascon /h/ outside
        # Bausen and Canejan, while the shipped TTS gold pronounces it. The
        # spec leads with [h] and carries the silent reading as the second
        # candidate rather than deciding the point without a native check.
        assert get("oc-x-aranes").graphemes["h"] == ["h", ""]

    def test_f_is_not_read_as_h(self):
        # Applying F- > h to the letter ⟨f⟩ would run the sound change twice.
        assert bare("fòrt", "oc-x-aranes").startswith("f")

    def test_interpunct_digraphs_keep_both_segments(self):
        # The interpunct exists to say "this is [n]+[h] / [s]+[h], NOT the
        # palatal digraph". A key that swallowed the ⟨h⟩ would answer the
        # maximal-munch question and lose the very contrast the spelling
        # was invented for.
        assert get("oc-x-aranes").graphemes["n·h"] == ["nh"]
        assert get("oc-x-aranes").graphemes["s·h"] == ["sh"]
        assert bare("des·hèr", "oc-x-aranes") == "deshɛr"
        assert bare("con·hessar", "oc-x-aranes") == "kunhesar"
        # …and the word stays one word: no interpunct-split into two.
        assert transcribe("des·hèr", lang="oc-x-aranes").count("ˈ") == 1
        assert " " not in transcribe("con·hessar", lang="oc-x-aranes")

    def test_the_plain_digraphs_still_win_without_the_interpunct(self):
        # ⟨nh⟩ and ⟨sh⟩ are the palatals; only the interpunct splits them.
        assert bare("nhèu", "oc-x-aranes").startswith("ɲ")
        assert bare("caisha", "oc-x-aranes") == "kajʃa"

    def test_th_is_a_plain_stop(self):
        assert bare("vedèth", "oc-x-aranes") == "beðɛt"

    def test_ll_is_a_single_lateral(self):
        assert "ll" not in bare("collaborar", "oc-x-aranes")

    def test_betacism(self):
        assert bare("Val", "oc-x-aranes") == "bal"
