"""Cited-rule conformance: Portuguese, Spanish, French, Italian.

Each test takes one cited claim from a spec — its ``notes`` prose or the
``notes`` of a single ``allophone_rules``/``sandhi_rules``/``stress`` entry —
quotes it with its citation, and proves the engine honours it on a real word,
isolating the rule to a single segment and pinning the complementary
environment with a minimal pair wherever the phonology allows one.

Claims the engine does NOT honour are marked ``xfail(strict=True)`` with the
actual output in the reason, never weakened to match.
"""
import unicodedata

import pytest

from orthography2ipa.g2p import G2P


def _t(code, word):
    # NFC so a precomposed nasal glyph in an expected literal compares equal to
    # the engine's decomposed vowel + combining tilde.
    return unicodedata.normalize("NFC", G2P(code).transcribe_word(word))


def _s(code, text):
    return unicodedata.normalize("NFC", G2P(code).transcribe(text))


def _bare(code, word):
    return _t(code, word).replace("ˈ", "").replace("ˌ", "")


# ===========================================================================
# pt-PT — European Portuguese
# ===========================================================================


def test_pt_pt_coda_l_dark():
    """PT_CODA_L_DARK: coda /l/ is velarised to [ɫ]; onset /l/ stays clear.

    Rule notes: "Velarised (dark) coda /l/ -> [ɫ]. In European Portuguese /l/ is
    velarised in the syllable coda (word-finally and pre-consonantally: sol,
    alto, mel) while onset /l/ stays clear. Mateus & d'Andrade (2000: ch.2);
    Cruz-Ferreira (1995)."

    Minimal pair: sol (coda) vs lua (onset) — the same phoneme, one segment
    apart in realisation.
    """
    assert _bare("pt-PT", "sol") == "sɔɫ"
    assert _bare("pt-PT", "alto") == "ɐɫtu"
    assert _bare("pt-PT", "lua") == "luɐ"


def test_pt_pt_coda_s_hush():
    """PT_CODA_S_HUSH: coda /s/ palatalises to [ʃ] — the 'chiado'.

    Rule notes: "Coda sibilant palatalisation /s/ -> [ʃ] (the 'chiado'): the
    Lisbon/standard European Portuguese realisation of a coda /s/ (word-final
    and pre-consonantal: as, pasta)." Mateus & d'Andrade (2000: ch.2).

    pasta has a pre-consonantal coda ⟨s⟩ → [ʃ]; casa has an intervocalic onset
    ⟨s⟩, which is untouched (and voiced to [z] pre-lexically).
    """
    assert _bare("pt-PT", "pasta") == "paʃtɐ"
    assert _bare("pt-PT", "casa") == "kazɐ"


def test_pt_pt_nasal_a_raise():
    """PT_NASAL_A_RAISE: a vowel before a coda nasal nasalises; the nasal is absorbed.

    Rule notes: "Coda-conditioned vowel nasalisation, general Portuguese (Mateus
    & d'Andrade 2000: ch.2, 'Nasality'): a vowel followed by a tautosyllabic
    (coda) nasal ⟨m/n⟩ nasalises while the nasal consonant is absorbed into the
    nasal vowel."

    campo: ⟨a⟩ + coda ⟨m⟩ → [ɐ̃], with no separate [m] segment surfacing.
    """
    assert _bare("pt-PT", "campo") == "kɐ̃pu"


def test_pt_pt_nasal_e_raise():
    """PT_NASAL_E_RAISE: the nasal mid front vowel is close-mid [ẽ], not [ɛ̃].

    Rule notes: "The nasal mid front vowel of Portuguese is the close-mid [ẽ],
    so the open [ɛ] selected by the pre-lexical map raises to [e] before the
    nasalisation." Mateus & d'Andrade (2000: ch.2).
    """
    assert _bare("pt-PT", "vento") == "vẽtu"


def test_pt_pt_nasal_o_raise():
    """PT_NASAL_O_RAISE: the nasal mid back vowel is close-mid [õ], not [ɔ̃].

    Rule notes: "The nasal mid back vowel of Portuguese is the close-mid [õ], so
    the open [ɔ] selected by the pre-lexical map raises to [o]." Mateus &
    d'Andrade (2000: ch.2).

    Minimal pair: ponte (before a coda nasal, raised and nasalised) vs bota
    (plain, stays open [ɔ]).
    """
    assert _bare("pt-PT", "ponte") == "põtɨ"
    assert _bare("pt-PT", "bota") == "bɔtɐ"


def test_pt_pt_nasal_o_unreduced():
    """PT_NASAL_O_UNRED: EP unstressed ⟨o⟩→[u] reduction is BLOCKED before a coda nasal.

    Rule notes: "European-Portuguese unstressed vowel reduction lowers ⟨o⟩ to
    [u] ... But that reduction is BLOCKED before a tautosyllabic nasal: an
    unstressed ⟨o⟩ before a coda ⟨m/n⟩ surfaces [õ]" — the note names
    "contar [kũˈtaɾ] would be wrong" as the failure this rule prevents.
    """
    assert _t("pt-PT", "contar") == "kõˈtaɾ"


def test_pt_pt_coda_s_voicing_before_voiced_consonant():
    """PT_CODA_S_VOICING: word-final coda /s/ voices to [ʒ] before a voiced consonant.

    Rule notes: "External (cross-word) VOICING ASSIMILATION of coda /s/: a
    word-final coda /s/ — which surfaces [ʃ] in isolation and before a voiceless
    consonant via the coda 'chiado' PT_CODA_S_HUSH — assimilates in voicing to a
    following VOICED consonant."

    Minimal pair across the word boundary: "as bocas" ([ʒ], voiced [b]) vs
    "as portas" ([ʃ], voiceless [p]).
    """
    assert _s("pt-PT", "as bocas").startswith("ɐʒ ")
    assert _s("pt-PT", "as portas").startswith("ɐʃ ")


def test_pt_pt_final_s_voices_before_vowel():
    """PT_FINAL_S_PREVOCALIC_VOICE: word-final coda /s/ voices to [z] before a vowel.

    Rule notes: "External (cross-word) sandhi: a word-final coda /s/ — which
    surfaces [ʃ] in isolation and pre-consonantally via the coda 'chiado'
    PT_CODA_S_HUSH — VOICES across the word boundary to [z] before a
    vowel-initial following word."

    Note the outcome is alveolar [z], not the palatal [ʒ] of the pre-consonantal
    voicing rule above — that contrast is the whole point of having two rules.
    """
    assert _s("pt-PT", "os amigos").startswith("oz ")


def test_pt_pt_preserves_b_v_distinction():
    """European Portuguese keeps /v/ ≠ /b/, unlike Castilian.

    pt-PT notes: "Portuguese preserves the /v/~/b/ distinction (unique in
    Ibero-Romance — Castilian merged them)."

    Minimal pair against es-ES, whose notes claim "(4) BETACISM: ⟨b⟩ = ⟨v⟩ =
    /b/ (complete, unlike Portuguese)".
    """
    assert _bare("pt-PT", "vento").startswith("v")
    assert _bare("es-ES", "vaca").startswith("b")


def test_pt_pt_spirantisation_deliberately_absent():
    """Intervocalic /b d ɡ/ spirantisation is deliberately NOT encoded in pt-PT.

    pt-PT notes: "Intervocalic voiced-stop spirantisation (/b d ɡ/->[β ð ɣ];
    Mateus & d'Andrade 2000) is a genuine EP process but is DELIBERATELY NOT
    encoded here: every available pt gold ... is broad/phonemic and transcribes
    the stops."

    A declared omission, pinned so it cannot appear by accident — es-ES, whose
    notes DO claim the process, is the contrast.
    """
    assert "ð" not in _bare("pt-PT", "nada")
    assert "ð" in _bare("es-ES", "nada")


# ===========================================================================
# pt-BR — Brazilian Portuguese
# ===========================================================================


def test_pt_br_raise_final_o():
    """BR_RAISE_FINAL_O: word-final unstressed /o/ raises to close [u].

    Rule notes: "Final unstressed vowel raising (Barbosa & Albano 2004: 229;
    Câmara Jr. 1970 §III): word-final unstressed /o/ raises to close [u] (gato →
    [ˈɡatu])."
    """
    assert _t("pt-BR", "gato") == "ˈɡatu"


def test_pt_br_raise_final_e():
    """BR_RAISE_FINAL_E: word-final unstressed /e/ raises to close [i].

    Rule notes: "Final unstressed vowel raising (Barbosa & Albano 2004: 229;
    Câmara Jr. 1970 §III): word-final unstressed /e/ raises to close [i] (leite
    → [ˈlejt͡ʃi], dente → [ˈdẽt͡ʃi])."

    This isolates the raising itself: the final vowel is [i], not the [ɪ] the
    pre-lexical map selects.
    """
    assert _t("pt-BR", "leite").endswith("i")
    assert "ɪ" not in _t("pt-BR", "leite")


def test_pt_br_affrication_before_raised_final_e():
    """BR affricates /t d/ before a RAISED final unstressed ⟨e⟩ — dente → [ˈdẽt͡ʃi].

    Rule notes: "word-final unstressed /e/ raises to close [i] (leite →
    [ˈlejt͡ʃi], dente → [ˈdẽt͡ʃi])" (Barbosa & Albano 2004: 229; Câmara Jr. 1970
    §III). The BR_AFFRIC_T_RAISED / BR_AFFRIC_D_RAISED allophone rules close the
    feeding gap the positional grapheme-⟨i⟩ map could not reach: they condition
    on the FOLLOWING slot's underlying high front vowel (the near-close [ɪ] the
    final-⟨e⟩ raising selects, or a lexical [i]), so a /t d/ before it affricates
    whether the trigger was spelled ⟨i⟩ or a raised ⟨e⟩. The non-palatalising
    nordeste and conservative-dental caipira/sul/pr/pt-UY varieties opt out by id.
    """
    assert _t("pt-BR", "dente") == "ˈdẽt͡ʃi"
    assert _t("pt-BR", "leite") == "ˈlejt͡ʃi"
    assert _t("pt-BR", "tarde") == "ˈtaɾd͡ʒi"


def test_pt_br_affrication_before_grapheme_i():
    """/t d/ affricate to [t͡ʃ d͡ʒ] before /i/ — the pre-lexical half of the claim.

    pt-BR notes: "(4) Palatalisation of /t, d/ > [t͡ʃ, d͡ʒ] before /i/ ...
    Deliberately kept in the positional map ... (grapheme-⟨i⟩ handled by the
    before_i positional rule)."
    """
    assert _bare("pt-BR", "tio").startswith("t͡ʃ")


def test_pt_br_l_vocalisation_in_coda():
    """BP coda /l/ vocalises to [w], where EP velarises it to [ɫ].

    pt-BR notes: "(3) L-vocalisation (l→w) strong and categorical in coda."

    Minimal pair against pt-PT's PT_CODA_L_DARK on the same word.
    """
    assert _bare("pt-BR", "sol") == "sɔw"
    assert _bare("pt-PT", "sol") == "sɔɫ"


def test_pt_br_coda_sibilants_stay_alveolar():
    """BP coda sibilants stay alveolar — no EP-style 'chiado'.

    pt-BR notes: "(2) Coda sibilants remain alveolar (s, z), no universal
    palato-alveolar outcome ... Deliberately NOT modelled in the base: ... coda
    /s/→[ʃ] chiado."

    Minimal pair against pt-PT's PT_CODA_S_HUSH on the same word.
    """
    assert "ʃ" not in _bare("pt-BR", "pasta")
    assert "ʃ" in _bare("pt-PT", "pasta")


# ===========================================================================
# es-ES — Peninsular Castilian
# ===========================================================================


def test_es_distincion():
    """DISTINCIÓN: ⟨c⟩ before e/i and ⟨z⟩ are /θ/, distinct from /s/.

    es-ES notes: "(1) DISTINCIÓN: /θ/ ≠ /s/ — ⟨c⟩ before e/i and ⟨z⟩ = /θ/
    (interdental fricative); absent in Latin American Spanish. Sources: Quilis
    (1999), Penny (2002), Hualde (2014)."

    Minimal pair on ⟨c⟩: cielo (before ⟨i⟩ → [θ]) vs casa (before ⟨a⟩ → [k]).
    """
    assert _bare("es-ES", "cielo").startswith("θ")
    assert _bare("es-ES", "zapato").startswith("θ")
    assert _bare("es-ES", "casa").startswith("k")


def test_es_yeismo():
    """YEÍSMO: ⟨ll⟩ is /ʝ/, the historical /ʎ/ distinction being lost.

    es-ES notes: "(3) YEÍSMO: ⟨ll⟩ = ⟨y⟩ = /ʝ/ in modern standard (RAE 2010
    norm); the historical /ʎ/ distinction is preserved in some regions."

    Contrast it-IT, which keeps a genuine /ʎ/ for ⟨gli⟩.
    """
    assert "ʝ" in _bare("es-ES", "pollo")
    assert "ʎ" not in _bare("es-ES", "pollo")


def test_es_betacism():
    """BETACISM: ⟨v⟩ and ⟨b⟩ are both /b/.

    es-ES notes: "(4) BETACISM: ⟨b⟩ = ⟨v⟩ = /b/ (complete, unlike Portuguese)."
    """
    assert _bare("es-ES", "vaca") == "baka"


def test_es_velar_fricative_j_and_soft_g():
    """⟨j⟩ and ⟨g⟩ before e/i are /x/.

    es-ES notes: "(5) VELAR FRICATIVE /x/: ⟨j⟩ and ⟨g+e,i⟩ = /x/."

    Minimal pair on ⟨g⟩: gente (before ⟨e⟩ → [x]) vs gato (before ⟨a⟩ → [ɡ]).
    """
    assert _bare("es-ES", "gente").startswith("x")
    assert _bare("es-ES", "gato").startswith("ɡ")


def test_es_silent_h():
    """SILENT ⟨h⟩: orthographic ⟨h⟩ is not pronounced.

    es-ES notes: "(6) SILENT ⟨h⟩: etymological F- underwent F→H→∅ change:
    FILIU→hijo, FACERE→hacer." Sources: Penny (2002), Hualde (2014).
    """
    assert _bare("es-ES", "hijo") == "ixo"
    assert _bare("es-ES", "hacer") == "aθeɾ"


def test_es_intervocalic_lenition():
    """INTERVOCALIC LENITION: /b d ɡ/ → [β ð ɣ] between vowels only.

    es-ES notes: "(7) INTERVOCALIC LENITION: voiced stops /b, d, ɡ/ → spirants
    [β, ð, ɣ] between vowels." Sources: Quilis (1999), Hualde (2014).

    Minimal pair on /d/: nada (intervocalic → [ð]) vs padre (post-consonantal,
    stays the stop [d]).
    """
    assert _bare("es-ES", "nada") == "naða"
    assert _bare("es-ES", "sabe") == "saβe"
    assert _bare("es-ES", "lago") == "laɣo"
    assert _bare("es-ES", "padre") == "padɾe"


def test_es_final_d_lenites():
    """Word-final /d/ → [ð].

    es-ES notes: "(8) Word-final /d/ → [ð] or [∅]: verdad [berˈdað]."
    """
    assert _t("es-ES", "verdad") == "beˈɾdað"


# ===========================================================================
# it-IT — Standard Italian
# ===========================================================================


def test_it_c_softening():
    """C/G SOFTENING: ⟨c⟩ → [tʃ] before e/i, [k] elsewhere.

    it-IT notes: "C/G SOFTENING: c→[tʃ] and g→[dʒ] before e/i (ci, ce, gi, ge);
    [k]/[ɡ] elsewhere. Sources: Lepschy & Lepschy (1988), Maiden (1995)."
    """
    assert _bare("it-IT", "cena").startswith("tʃ")
    assert _bare("it-IT", "casa").startswith("k")


def test_it_g_softening():
    """C/G SOFTENING: ⟨g⟩ → [dʒ] before e/i, [ɡ] elsewhere.

    it-IT notes: "c→[tʃ] and g→[dʒ] before e/i (ci, ce, gi, ge); [k]/[ɡ]
    elsewhere." Lepschy & Lepschy (1988).
    """
    assert _bare("it-IT", "gelo").startswith("dʒ")
    assert _bare("it-IT", "gatto").startswith("ɡ")


def test_it_intervocalic_s_voices():
    """INTERVOCALIC s: [z] between vowels, [s] word-initially.

    it-IT notes: "INTERVOCALIC s: [z] between vowels in standard Italian (N.
    Italy); [s] word-initially." Rogers & d'Arcangeli (2004).
    """
    assert _bare("it-IT", "rosa") == "roza"
    assert _bare("it-IT", "sole").startswith("s")


def test_it_sc_before_front_vowel():
    """SC: [ʃ] before e/i, [sk] elsewhere.

    it-IT notes: "SC: [ʃ] before e/i, [sk] elsewhere." Lepschy & Lepschy (1988).
    """
    assert _bare("it-IT", "scena").startswith("ʃ")
    assert _bare("it-IT", "scala").startswith("sk")


def test_it_z_word_initial_is_voiced():
    """Z: [dz] word-initially.

    it-IT notes: "Z: [dz] word-initially and post-consonantally, [ts] in other
    positions." Rogers & d'Arcangeli (2004).
    """
    assert _bare("it-IT", "zona").startswith("dz")


def test_it_inherent_geminate_gn():
    """IT_INHERENT_GEMINATE_GN: intervocalic /ɲ/ is inherently long.

    Rule notes: "Intervocalic /ɲ/ is inherently long in Italian (Krämer (2009)
    The Phonology of Italian (OUP) §7.2; Canepari DiPI): bagno [baɲɲo]."
    """
    assert _bare("it-IT", "bagno") == "baɲɲo"


def test_it_inherent_geminate_gli():
    """IT_INHERENT_GEMINATE_GLI: intervocalic /ʎ/ is inherently long.

    Rule notes: "Intervocalic /ʎ/ is inherently long in Italian (Krämer (2009)
    §7.2; Canepari DiPI): aglio [aʎʎo]."
    """
    assert _bare("it-IT", "aglio") == "aʎʎo"


def test_it_inherent_geminate_sc():
    """IT_INHERENT_GEMINATE_SC: intervocalic /ʃ/ is inherently long.

    Rule notes: "Intervocalic /ʃ/ is inherently long in Italian (Krämer (2009)
    §7.2; Canepari DiPI): pesce [peʃʃe]."
    """
    assert _bare("it-IT", "pesce") == "peʃʃe"


def test_it_inherent_geminate_ts():
    """IT_INHERENT_GEMINATE_TS: intervocalic /ts/ is inherently long.

    Rule notes: "Intervocalic /ts/ is inherently long in Italian (Krämer (2009)
    §7.2; Canepari DiPI): vizio [vittsjo]."
    """
    assert _bare("it-IT", "vizio") == "vittsjo"


# ===========================================================================
# fr-FR — Standard Metropolitan French
# ===========================================================================


def test_fr_denasalisation_before_vowel():
    """Nasal grapheme sequences denasalise before a vowel within the word.

    fr-FR notes: "Nasal grapheme sequences (⟨an⟩, ⟨am⟩, ⟨en⟩, ⟨em⟩, ⟨in⟩, ⟨im⟩,
    ⟨on⟩, ⟨om⟩, ⟨un⟩, ⟨um⟩) denasalise before a following vowel within the word
    (positional_graphemes before_vowel branch, e.g. amateur [amatœʁ], inutile
    [inytil], bonasse [bɔnas])." Sources: Fouché (1959), Tranel (1987).

    Isolated on the nasal grapheme: ⟨in⟩ in inutile reads [in], not [ɛ̃]; the
    minimal pair is a pre-consonantal ⟨en⟩ (chant) which stays nasal.
    """
    assert _t("fr-FR", "inutile") == "inytil"
    assert _t("fr-FR", "bonasse") == "bɔnas"
    assert _t("fr-FR", "chant") == "ʃɑ̃"


def test_fr_final_consonants_silent():
    """FINAL CONSONANTS: t, d, p, s, x, r are typically silent word-finally.

    fr-FR notes: "FINAL CONSONANTS: t, d, p, s, x, r typically silent
    word-finally in modern French, resurfacing in liaison." Tranel (1987).

    Minimal pair on ⟨t⟩: silent word-finally in chant, pronounced in the coda of
    porte (where a following ⟨e⟩ makes it non-final).
    """
    assert not _t("fr-FR", "chant").endswith("t")
    assert _t("fr-FR", "porte") == "pɔʁt"


def test_fr_c_and_g_softening():
    """SOFTENING: c→[s] and g→[ʒ] before e/i/y.

    fr-FR notes: "SOFTENING: c→[s] before e/i/y; g→[ʒ] before e/i/y." Fouché
    (1959).

    Minimal pairs: cité vs carte, gel vs gare.
    """
    assert _t("fr-FR", "cité").startswith("s")
    assert _t("fr-FR", "carte").startswith("k")
    assert _t("fr-FR", "gel").startswith("ʒ")
    assert _t("fr-FR", "gare").startswith("ɡ")


def test_fr_intervocalic_s_voices():
    """INTERVOCALIC s: [z] between vowels within a word.

    fr-FR notes: "INTERVOCALIC s: [z] between vowels within a word." Fouché
    (1959), Tranel (1987).
    """
    assert _t("fr-FR", "rose") == "ʁɔz"


def test_fr_e_caduc_silent_word_finally():
    """Word-final ⟨e⟩ (e caduc) is silent; the monosyllabic function words are not.

    fr-FR notes: "Word-final unstressed ⟨e⟩ (e caduc) defaults to silent
    (positional_graphemes word_final), matching modern colloquial elision of the
    mute e; monosyllabic function words whose sole vowel is that final ⟨e⟩ (le,
    de, que, ce, ne, se, je, me, te) are handled via the word_exceptions
    whole-word override ... the schwa is grammatically obligatory there."

    Minimal pair: porte (silent) vs le (the carved-out exception, [lə]).
    """
    assert _t("fr-FR", "porte") == "pɔʁt"
    assert _t("fr-FR", "le") == "lə"


def test_fr_doubled_consonants_degeminate():
    """Doubled consonants degeminate to a single consonant.

    fr-FR notes: "Doubled consonants (bb, dd, ff, gg, ll, mm, nn, pp, rr, tt)
    degeminate to a single consonant, the modern-French default (Fouché 1959;
    Tranel 1987)."

    belle: the ⟨ll⟩ digraph yields exactly one [l].
    """
    assert _t("fr-FR", "belle").count("l") == 1


@pytest.mark.xfail(
    strict=True,
    reason="FR_LIAISON_Z cites 'les amis → lez‿ami'; engine produces 'lə ami' — "
    "the spec silences word-final ⟨s⟩ pre-lexically, so no /z/ ever reaches the "
    "sandhi rule's left_context 'z$' and the rule is structurally inert",
)
def test_fr_liaison_z():
    """FR_LIAISON_Z: /s/ resurfaces as [z] before a vowel-initial word.

    fr-FR notes: "LIAISON: s/x→[z] ... before vowel-initial words (sandhi_rules,
    obligatory after determiners/pronouns ... per Tranel 1995)." The rule's own
    notes cite "les amis → lez‿ami", and it is declared ``obligatory: true``.
    """
    assert "z‿" in _s("fr-FR", "les amis")


@pytest.mark.xfail(
    strict=True,
    reason="FR_LIAISON_N cites 'un ami → ɛ̃n‿ami'; engine produces 'œ̃ ami' — the "
    "nasal grapheme absorbs the ⟨n⟩, so no /n/ reaches the sandhi rule's "
    "left_context 'n$' and the rule is structurally inert",
)
def test_fr_liaison_n():
    """FR_LIAISON_N: /n/ resurfaces before a vowel-initial word.

    fr-FR notes: "LIAISON: ... n→[n] before vowel-initial words (sandhi_rules,
    obligatory after determiners/pronouns ... per Tranel 1995)." The rule's own
    notes cite "un ami → ɛ̃n‿ami", and it is declared ``obligatory: true``.
    """
    assert "n‿" in _s("fr-FR", "un ami")


@pytest.mark.xfail(
    strict=True,
    reason="fr-FR notes cite amateur [amatœʁ]; engine produces [amatø] — the "
    "spec's own 'FINAL CONSONANTS: ... r typically silent word-finally' claim "
    "deletes the ⟨r⟩ of the -eur suffix, contradicting the cited transcription",
)
def test_fr_amateur_cited_transcription():
    """fr-FR notes cite amateur as [amatœʁ].

    fr-FR notes: "⟨am⟩ ... denasalise before a following vowel within the word
    (positional_graphemes before_vowel branch, e.g. amateur [amatœʁ] ...)."
    Sources: Fouché (1959), Tranel (1987).

    The denasalisation itself fires (see test_fr_denasalisation_before_vowel);
    the cited whole-word transcription is not reached, because the blanket
    final-⟨r⟩ deletion rule strips the suffix's [ʁ].
    """
    assert _t("fr-FR", "amateur") == "amatœʁ"
