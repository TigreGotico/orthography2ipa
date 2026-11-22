"""The emitted symbol set is closed, enumerable, and free of dead rules.

A neural TTS frontend builds its embedding table from the phoneme inventory
before training. A symbol the phonemizer can emit but nobody enumerated has no
embedding, and the word carrying it is mispronounced permanently and silently.
So "what can this spec emit?" must have an exact answer, and transcription must
never step outside it.
"""
import unicodedata

import pytest

from orthography2ipa import available_codes, get
from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import (
    dead_allophone_rules, emission_inventory, phoneme_atoms, phoneme_inventory, tokenize,
)

ALL_CODES = sorted(available_codes())

#: Specs whose transcription is exercised against the closure invariant. The
#: sweep runs over every spec; these carry a lexicon worth transcribing.
SAMPLE_WORDS = {
    "ar": ["كِتَاب", "قَهْوَة", "مَدْرَسَة", "صَبْر", "الشَّمْس", "بَيْت"],
    "ar-SA-x-najd": ["كِتَاب", "قَهْوَة", "لَحْم", "قَلَم"],
    "ar-SA-x-hejaz": ["بَيْت", "قَلَم", "كِتَاب"],
    "en": ["hello", "world", "phoneme"],
    "pt": ["coelho", "palavra"],
    "es": ["hola", "mundo"],
}


# ─── the closure invariant ──────────────────────────────────────────────

@pytest.mark.parametrize("code", sorted(SAMPLE_WORDS))
def test_transcription_never_leaves_the_inventory(code):
    """Nothing transcription emits may fall outside the declared token set."""
    spec = get(code)
    tokens = phoneme_inventory(spec)
    g2p = G2P(code)

    for word in SAMPLE_WORDS[code]:
        ipa = g2p.transcribe(word)
        for token in tokenize(ipa, spec):
            assert token in tokens, (
                f"{code}: transcribing {word!r} emitted {token!r}, which is "
                f"outside the phoneme inventory"
            )


@pytest.mark.parametrize("code", ALL_CODES)
def test_inventory_is_derivable_for_every_spec(code):
    """Every spec can answer 'what can you emit?' without raising."""
    spec = get(code)
    emissions = emission_inventory(spec)
    tokens = phoneme_inventory(spec)
    assert "" not in emissions, "a deleted slot is the absence of a symbol"
    assert "" not in tokens
    # A spec with graphemes must be able to emit something.
    if spec.graphemes:
        assert emissions, f"{code} has graphemes but emits nothing"


@pytest.mark.parametrize("code", ALL_CODES)
def test_every_allophone_surface_is_in_the_inventory(code):
    """A rule's surface is a symbol the engine can emit, so it must be counted.

    This is the invariant that actually bites: an allophone rule is a *new*
    source of IPA (Najdi's [ts] exists nowhere in the grapheme table), so an
    inventory derived only from the graphemes would miss it — and a TTS trained
    on that inventory would have no embedding for the affricate it is about to
    be asked to say.
    """
    spec = get(code)
    emissions = emission_inventory(spec)
    for rule in (spec.allophone_rules or ()):
        if rule.surface:
            assert rule.surface in emissions


def test_a_rule_only_surface_is_counted():
    """Najdi's VOICED affricate comes from a rule, not the grapheme table.

    The voiceless [ts] used to be the example here and no longer can be: ⟨چ⟩ now
    carries it directly, because a letter spelling an already-affricated word gives
    the rule no ⟨ك⟩ to fire on. [dz] is the same phenomenon's voiced half
    (NAJD_AFFRIC_G_*) and is still reachable only through the rule, so the property
    under test — that a surface no grapheme emits is still counted — is unchanged.
    """
    najd = get("ar-SA-x-najd")
    assert "dz" not in {r for readings in najd.graphemes.values() for r in readings}
    assert "dz" in emission_inventory(najd)
    assert "dz" in phoneme_inventory(najd)


def test_stress_is_its_own_token():
    """Prosody is not a phoneme: ˈ modifies a syllable, not the vowel after it.

    The generic IPA segmenter treats a spacing modifier as part of the preceding
    character, which would make `ɐˈ` a "phoneme" — in no inventory, and a symbol
    a model would have to learn separately from `ɐ`.
    """
    spec = get("pt")
    tokens = tokenize(G2P("pt").transcribe("palavra"), spec)
    assert "ˈ" in tokens
    assert not any(t != "ˈ" and "ˈ" in t for t in tokens)


def test_multi_character_segments_stay_whole():
    """[ts] is one token, not t + s — the affricate is declared, so it holds."""
    assert "ts" in phoneme_inventory(get("ar-SA-x-najd"))
    assert "aː" in phoneme_inventory(get("ar"))


def test_a_whole_word_reading_is_cut_into_segments():
    """The Aragonese of Tena lists ``ros`` [ɾos] as a word exception. A word
    is not a phoneme: the inventory holds [ɾ], [o] and [s], never [ɾos]."""
    spec = get("an-x-tensino")
    assert spec.word_exceptions["ros"] == "ɾos"
    inventory = phoneme_inventory(spec)
    assert {"ɾ", "o", "s"} <= inventory
    assert not {"ɾo", "ɾos", "ɾa", "ɾas"} & inventory
    assert tokenize("ɾos", spec) == ["ɾ", "o", "s"]


def test_a_segment_only_a_word_exception_emits_is_declared():
    """Qeltu Arabic emits [ʁ] only inside its word exceptions (أَعْرِف
    [ʔaʕʁif], دُغْرِي [duɣʁiː], بَاكِر [baːkiʁ]). The segment is in the
    inventory, so a forced reading that uses it is accepted."""
    spec = get("ar-IQ-x-qeltu")
    assert spec.word_exceptions["أَعْرِف"] == "ʔaʕʁif"
    assert "ʁ" in phoneme_inventory(spec)
    assert G2P("ar-IQ-x-qeltu").transcribe('<phoneme ph="ʁa">x</phoneme>') == "ʁa"


def test_the_lexicon_argument_of_tokenize_and_phoneme_atoms_is_deprecated():
    spec = get("pt-PT")
    with pytest.warns(DeprecationWarning, match="lexicon argument of tokenize"):
        assert tokenize("ˈkazɐ", spec, {}) == tokenize("ˈkazɐ", spec)
    with pytest.warns(DeprecationWarning, match="lexicon argument of phoneme_atoms"):
        assert phoneme_atoms(spec, {}) == phoneme_atoms(spec)


# ─── the dead-rule lint ─────────────────────────────────────────────────

#: Specs carrying allophone rules whose target phoneme they cannot produce, so
#: the rule can never fire. Each is a real bug — a rule written against a symbol
#: the spec does not use — and each needs a language owner to say what the rule
#: *should* target, which is not a mechanical fix. Listed rather than skipped so
#: they stay visible, and so no NEW dead rule can be added without failing here.
#: Оканье and its after-soft-consonant counterpart еканье keep unstressed
#: /o e a/ distinct, so the Northern lects never emit the standard's reduced
#: [ɪ] or [ə] in the iotated slots — ⟨я⟩ is [ja] and ⟨е⟩ is [(j)e] there, not
#: [jɪ]/[jə]. The de-iotation and hard-backing rules that target those two
#: candidates therefore have nothing to fire on. This is the okanje system
#: doing what it is defined to do, not a gap: the rule set is the standard
#: language's, inherited whole, and it is live in every akanje lect.
#: ``RU_DEIOTA_jʊ`` is NOT dead here — okanje is about the non-high vowels,
#: so ⟨ю⟩/⟨у⟩ keep the base [jʊ]/[ʊ] readings.
_RU_OKANJE_DEAD = {
    "RU_DEIOTA_jə", "RU_DEIOTA_jɪ", "RU_HARD_BACK_jɪ",
}

KNOWN_DEAD_RULES = {
    # Maltese inherits the Arabic allophone rules wholesale but emits neither
    # the long vowels they target (/aː/, /iː/, /uː/) nor their environments, so
    # the whole inherited family is unreachable there.
    "mt": {
        "AR_EMPH_BACK_AA_AFTER", "AR_EMPH_BACK_AA_BEFORE",
        "AR_GLIDE_YA_BEFORE_GEMINATE", "AR_GLIDE_YA_GEMINATE_COPY",
        "AR_GLIDE_YA_CONSONANTAL", "AR_GLIDE_WAW_CONSONANTAL",
        # Same reason, for the generic arb-level emphasis-spread family
        # (AR_EMPHASIS_SPREAD_*, engine-generic "emphatic" neighbour class,
        # Watson 2002; Davis 1995): Maltese emits neither the long vowels
        # (/aː iː uː/) nor the short /i u/ these target.
        "AR_EMPHASIS_SPREAD_AA_AFTER", "AR_EMPHASIS_SPREAD_AA_BEFORE",
        "AR_EMPHASIS_SPREAD_I_AFTER", "AR_EMPHASIS_SPREAD_I_BEFORE",
        "AR_EMPHASIS_SPREAD_II_AFTER", "AR_EMPHASIS_SPREAD_II_BEFORE",
        "AR_EMPHASIS_SPREAD_UU_AFTER", "AR_EMPHASIS_SPREAD_UU_BEFORE",
    },
    # Targets /ɪ/, which these specs never emit.
    "pt-BR-x-pr": {"BR_RAISE_FINAL_E"},
    "pt-BR-x-sul": {"BR_RAISE_FINAL_E"},
    # The Portuguese-based creoles inherit pt-PT's word-final nasal-diphthong
    # rules (PT_FINAL_EM_GLIDE / PT_FINAL_AM_GLIDE, which target the coda
    # nasalisation tilde [̃]), but a defining feature of these creoles is the
    # LOSS of the Portuguese nasal-coda system — they do not emit the tilde the
    # glide rules attach to, so the rules are inert here. The open/close mid
    # vowel pins (PT_LEX_*) inherit and fire normally; only the nasal-glide
    # pair is dead. Inherited correctly for the pt lects that keep nasalisation.
    # PT_FINAL_ENS_GLIDE is the plural ⟨-ens⟩ glide and PT_FINAL_EN_CODA the
    # learned ⟨-en⟩ consonant; both target the tilde and are dead for the same
    # reason; PT_NASAL_E_UNRED targets the reduced [ɨ], which these specs lack.
    "kea": {"PT_FINAL_EM_GLIDE", "PT_FINAL_AM_GLIDE", "PT_FINAL_ENS_GLIDE", "PT_FINAL_EN_CODA", "PT_NASAL_E_UNRED"},
    "pap": {"PT_FINAL_EM_GLIDE", "PT_FINAL_AM_GLIDE", "PT_FINAL_ENS_GLIDE", "PT_FINAL_EN_CODA", "PT_NASAL_E_UNRED"},
    "pov": {"PT_FINAL_EM_GLIDE", "PT_FINAL_AM_GLIDE", "PT_FINAL_ENS_GLIDE", "PT_FINAL_EN_CODA", "PT_NASAL_E_UNRED"},
    "cri": {"PT_FINAL_EM_GLIDE", "PT_FINAL_AM_GLIDE", "PT_FINAL_ENS_GLIDE", "PT_FINAL_EN_CODA", "PT_NASAL_E_UNRED"},
    "mcm": {"PT_FINAL_EM_GLIDE", "PT_FINAL_AM_GLIDE", "PT_FINAL_ENS_GLIDE", "PT_FINAL_EN_CODA", "PT_NASAL_E_UNRED", "PT_LEX_X_S"},
    "aoa": {"PT_FINAL_EM_GLIDE", "PT_FINAL_AM_GLIDE", "PT_FINAL_ENS_GLIDE", "PT_FINAL_EN_CODA", "PT_NASAL_E_UNRED"},
    "mzs": {"PT_FINAL_EM_GLIDE", "PT_FINAL_AM_GLIDE", "PT_FINAL_ENS_GLIDE", "PT_FINAL_EN_CODA", "PT_NASAL_E_UNRED"},
    "idb": {"PT_FINAL_EM_GLIDE", "PT_FINAL_AM_GLIDE", "PT_FINAL_ENS_GLIDE", "PT_FINAL_EN_CODA", "PT_NASAL_E_UNRED", "PT_LEX_X_S"},
    "pre": {"PT_FINAL_EM_GLIDE", "PT_FINAL_AM_GLIDE", "PT_FINAL_ENS_GLIDE", "PT_FINAL_EN_CODA", "PT_NASAL_E_UNRED"},
    "vkp": {"PT_FINAL_EM_GLIDE", "PT_FINAL_AM_GLIDE", "PT_FINAL_ENS_GLIDE", "PT_FINAL_EN_CODA", "PT_NASAL_E_UNRED"},
    # Dead only because the spec inherits a grapheme table without its
    # positional readings, so the vowel the rule targets is never emitted.
    # Fixed by the positional-inheritance default in #348, which revives it.
    "da-x-copenhag": {"DA_SHORTEN_A"},
    # The southern Russian lects used to be listed here, on the reading that
    # they had "their own unstressed-vowel system". They did not: they had no
    # positional table at all, because the spec carried a standalone grapheme
    # table with no `graphemes_base` and so inherited nothing positional. They
    # reduce now — akanje IS reduction — and all four rules are live there
    # again. The okanje North is the real case of this shape.
    "ru-x-northern": _RU_OKANJE_DEAD,
    "ru-x-vologda": _RU_OKANJE_DEAD,
    "ru-x-arkhange": _RU_OKANJE_DEAD,
    # Sendinês monophthongises the Leonese rising diphthongs (⟨ie⟩→[i],
    # ⟨uo⟩→[u]), so the [jɪ]/[ʊ] nuclei and the [je]/[wo] second candidates
    # that the inherited Mirandese nasalisation rules target never surface
    # here. The rules are live in the parent mwl and in mwl-x-ifanes, which
    # keep the diphthongs.
    "mwl-x-sendim": {"MWL_NASAL_DIPHTHONG_JE", "MWL_NASAL_DIPHTHONG_WO",
                     "MWL_NASAL_DIPHTHONG_JI", "MWL_NASAL_U_LAX"},
    # Cypriot Maronite Arabic lost the glottal stop /ʔ/ entirely (Borg 1985;
    # Roth 2004), so the inherited hamzat-al-waṣl prosthesis rule — which
    # targets /ʔ/ — can never fire here. It is live in every Arabic lect that
    # keeps /ʔ/; the rule set is Classical Arabic's, inherited unchanged.
    "acy": {"AR_WASL_EPENTHESIS"},
    # Seychellois Creole levelled French /y/ to /i/ and /ə/ to /e/~/ɛ/ in its
    # own vowel merger (Michaelis & Rosalie, APiCS ch. 56; Bollée 1977), so
    # the inherited French front-rounded/schwa nasalisation rules can never
    # fire here. They are live in fr-FR, which keeps both phonemes. The same
    # merger took the front-rounded mid vowels: crs has no /œ/ PHONEME target
    # (⟨eu⟩ is [e]~[ɛ] here), so the inherited loi-de-position rule on /œ/
    # can never fire. (emission_inventory still lists the rule's /ø/ surface —
    # it unions dead-rule surfaces — so the claim is about targets, not the
    # derived inventory.) FR_AU_BEFORE_R is NOT dead here — crs keeps /o/.
    # crs replaces fr-FR's grapheme table with its own 28-grapheme Kreol
    # orthography, which has no ⟨ien⟩/⟨oin⟩ multigraph and no ⟨x⟩: the
    # nasal-blocking rules for those two spellings have no /jɛ̃/ or /wɛ̃/
    # to rewrite, and FR_E_CLOSED_MULTIGRAPH has neither a /ə/ target (see
    # above) nor a single letter spelling a consonant cluster to close a
    # syllable with. All four are live in fr-FR.
    "crs": {"FR_NASAL_y", "FR_NASAL_ə", "FR_EU_BEFORE_Z",
            "FR_NASAL_BLOCK_PREVOCALIC_IEN", "FR_NASAL_BLOCK_GEMINATE_IEN",
            "FR_NASAL_BLOCK_PREVOCALIC_OIN", "FR_NASAL_BLOCK_GEMINATE_OIN",
            "FR_E_CLOSED_MULTIGRAPH"},
    # jrb (Judeo-Arabic macrolanguage node) is metadata-only: graphemes is
    # intentionally empty pending a sourced Hebrew-script grapheme table (see
    # its `notes`), so no phoneme -- including /ʔ/ -- is in the inventory yet
    # and the inherited Classical-Arabic hamzat-al-waṣl rule can never fire.
    # Same class of dead rule as "acy" above; will resolve itself once a real
    # grapheme table is added for jrb.
    "jrb": {"AR_WASL_EPENTHESIS",
            "AR_EMPHASIS_SPREAD_A_AFTER", "AR_EMPHASIS_SPREAD_A_BEFORE",
            "AR_EMPHASIS_SPREAD_AA_AFTER", "AR_EMPHASIS_SPREAD_AA_BEFORE",
            "AR_EMPHASIS_SPREAD_I_AFTER", "AR_EMPHASIS_SPREAD_I_BEFORE",
            "AR_EMPHASIS_SPREAD_II_AFTER", "AR_EMPHASIS_SPREAD_II_BEFORE",
            "AR_EMPHASIS_SPREAD_U_AFTER", "AR_EMPHASIS_SPREAD_U_BEFORE",
            "AR_EMPHASIS_SPREAD_UU_AFTER", "AR_EMPHASIS_SPREAD_UU_BEFORE"},
    # ajt/aju/yhd (Judeo-Tunisian/Moroccan/Iraqi Arabic) are likewise
    # metadata-only stubs (graphemes: {}) whose single genetic PARENT is
    # their regional Arabic dialect spec (ar-TN/ar-MA/ar-IQ respectively --
    # jrb is wired as RELATED, not PARENT, since it is a sociolinguistic
    # macrolanguage collective, not genetic descent). They inherit that
    # dialect's full allophone rule set, none of which can fire against an
    # empty own inventory. Will resolve once a real Hebrew-script grapheme
    # table is sourced for each code.
    # ajt/aju/yhd additionally inherit the arb-level, engine-generic
    # AR_EMPHASIS_SPREAD_* family (the "emphatic" neighbour class, Watson
    # 2002; Davis 1995) — dead here for the same reason as the rest of the
    # inherited rule set: empty own inventory, nothing can ever fire.
    "ajt": {"AR_EMPH_BACK_A_AFTER", "AR_EMPH_BACK_A_BEFORE",
            "AR_TN_MONO_AJ", "AR_TN_MONO_AW", "AR_WASL_EPENTHESIS",
            "AR_EMPHASIS_SPREAD_A_AFTER", "AR_EMPHASIS_SPREAD_A_BEFORE",
            "AR_EMPHASIS_SPREAD_AA_AFTER", "AR_EMPHASIS_SPREAD_AA_BEFORE",
            "AR_EMPHASIS_SPREAD_I_AFTER", "AR_EMPHASIS_SPREAD_I_BEFORE",
            "AR_EMPHASIS_SPREAD_II_AFTER", "AR_EMPHASIS_SPREAD_II_BEFORE",
            "AR_EMPHASIS_SPREAD_U_AFTER", "AR_EMPHASIS_SPREAD_U_BEFORE",
            "AR_EMPHASIS_SPREAD_UU_AFTER", "AR_EMPHASIS_SPREAD_UU_BEFORE"},
    "aju": {"AR_EMPH_BACK_AA_AFTER", "AR_EMPH_BACK_AA_BEFORE",
            "AR_EMPH_BACK_A_AFTER", "AR_EMPH_BACK_A_BEFORE",
            "AR_GLIDE_WAW_CONSONANTAL", "AR_GLIDE_YA_BEFORE_GEMINATE",
            "AR_GLIDE_YA_CONSONANTAL", "AR_GLIDE_YA_GEMINATE_COPY",
            "MA_SHORT_REDUCE", "AR_WASL_EPENTHESIS",
            "AR_EMPHASIS_SPREAD_A_AFTER", "AR_EMPHASIS_SPREAD_A_BEFORE",
            "AR_EMPHASIS_SPREAD_AA_AFTER", "AR_EMPHASIS_SPREAD_AA_BEFORE",
            "AR_EMPHASIS_SPREAD_I_AFTER", "AR_EMPHASIS_SPREAD_I_BEFORE",
            "AR_EMPHASIS_SPREAD_II_AFTER", "AR_EMPHASIS_SPREAD_II_BEFORE",
            "AR_EMPHASIS_SPREAD_U_AFTER", "AR_EMPHASIS_SPREAD_U_BEFORE",
            "AR_EMPHASIS_SPREAD_UU_AFTER", "AR_EMPHASIS_SPREAD_UU_BEFORE"},
    "yhd": {"AR_EMPH_BACK_AA_AFTER", "AR_EMPH_BACK_AA_BEFORE",
            "AR_EMPH_BACK_A_AFTER", "AR_EMPH_BACK_A_BEFORE",
            "AR_GLIDE_WAW_CONSONANTAL", "AR_GLIDE_YA_BEFORE_GEMINATE",
            "AR_GLIDE_YA_CONSONANTAL", "AR_GLIDE_YA_GEMINATE_COPY",
            "IQ_EMPH_AA_AFTER", "IQ_EMPH_AA_BEFORE", "IQ_EMPH_A_AFTER",
            "IQ_EMPH_A_BEFORE", "IQ_GILIT_AFFRIC_G_AFTER",
            "IQ_GILIT_AFFRIC_G_BEFORE", "IQ_GILIT_AFFRIC_K_AFTER",
            "IQ_GILIT_AFFRIC_K_BEFORE", "AR_WASL_EPENTHESIS",
            "AR_EMPHASIS_SPREAD_A_AFTER", "AR_EMPHASIS_SPREAD_A_BEFORE",
            "AR_EMPHASIS_SPREAD_AA_AFTER", "AR_EMPHASIS_SPREAD_AA_BEFORE",
            "AR_EMPHASIS_SPREAD_I_AFTER", "AR_EMPHASIS_SPREAD_I_BEFORE",
            "AR_EMPHASIS_SPREAD_II_AFTER", "AR_EMPHASIS_SPREAD_II_BEFORE",
            "AR_EMPHASIS_SPREAD_U_AFTER", "AR_EMPHASIS_SPREAD_U_BEFORE",
            "AR_EMPHASIS_SPREAD_UU_AFTER", "AR_EMPHASIS_SPREAD_UU_BEFORE"},
    # Yevanic (yej) is a stub: its Hebrew-script grapheme table is intentionally
    # left empty because no sourced letter-by-letter correspondence could be
    # located (see the spec's notes), so it emits nothing of its own at all.
    # It still inherits el's allophone rule *set* (parent_dialect), but with
    # zero graphemes there is no /s/ or /ɣ/ slot for EL_S_VOICING / EL_
    # GAMMA_FRONTING to match against. Both are live in el, which has the
    # grapheme table this spec is deliberately missing; revisit once yej gains
    # a sourced Hebrew-abjad grapheme table.
    "yej": {"EL_S_VOICING", "EL_GAMMA_FRONTING"},
    # vls (West Flemish) declares parent="nl-NL" with its own "graphemes": {} to
    # inherit nl-NL's table wholesale, but (pre-existing, unrelated to the
    # Germanic beat-espeak campaign that added these rules) that inheritance
    # does not actually populate the plain vowel letters a/e/i/o/u for this
    # spec -- G2P('vls').transcribe(...) already returns empty output for
    # ordinary words before and after this change. With no 'a'/'e'/'i'/'o'/'u'
    # slot at all, the open-syllable-lengthening rules inherited from nl-NL can
    # never fire here.
    # Same pre-existing "graphemes": {} inheritance gap accounts for the
    # three rules the beat-espeak Dutch wave added: no 'g' slot means
    # NL_CODA_DEVOICE_G's /ɣ/ target can't fire, and no 'i' slot means
    # NL_UNSTRESSED_TENSE_I_FINAL / NL_UNSTRESSED_TENSE_I_HIATUS's /ɪ/
    # target can't either. The same gap leaves no /eː øː oː/ slot for the six
    # NL_MID_TENSE_* rules, no /r/ slot for NL_CODA_R_APPROXIMANT, and no
    # ⟨veld⟩ slot for NL_CODA_DEVOICE_VELD, and no ⟨ij⟩ slot for NL_LIJK_SCHWA.
    "vls": {"NL_CODA_DEVOICE_B", "NL_CODA_DEVOICE_D", "NL_CODA_DEVOICE_G",
            "NL_CODA_DEVOICE_V", "NL_CODA_DEVOICE_Z",
            "NL_UNSTRESSED_TENSE_I_FINAL", "NL_UNSTRESSED_TENSE_I_HIATUS",
            "NL_HIGH_TENSE_LENGTHENING_BEFORE_R_U",
            "NL_HIGH_TENSE_LENGTHENING_BEFORE_R_Y",
            "NL_MID_TENSE_CENTRING_BEFORE_R_E", "NL_MID_TENSE_CENTRING_BEFORE_R_OE",
            "NL_MID_TENSE_CENTRING_BEFORE_R_O", "NL_MID_TENSE_CLOSING_DIPHTHONG_E",
            "NL_MID_TENSE_CLOSING_DIPHTHONG_OE", "NL_MID_TENSE_CLOSING_DIPHTHONG_O",
            "NL_CODA_R_APPROXIMANT", "NL_CODA_DEVOICE_VELD", "NL_QU_FRENCH_K",
            "NL_LIJK_SCHWA"},
    # Afrikaans has no /z/ (Donaldson, *A Grammar of Afrikaans*, Mouton de
    # Gruyter 1993, ch. 1: ⟨z⟩ is not part of the inventory, and ⟨s⟩ is
    # voiceless everywhere), so the /z/ member of nl-NL's coda-devoicing series
    # has no target here. The other members are live. af has no ⟨veld⟩ or ⟨qu⟩
    # key, so NL_CODA_DEVOICE_VELD and NL_QU_FRENCH_K have no slot to match.
    # af reads ⟨ij⟩ as /əi/, so NL_LIJK_SCHWA, which targets /ɛi aːi/, has no
    # target either.
    "af": {"NL_CODA_DEVOICE_Z", "NL_CODA_DEVOICE_VELD", "NL_QU_FRENCH_K",
           "NL_LIJK_SCHWA"},
    # pnb-PK (Shahmukhi abjad, no inherent vowel): the inherent-vowel half
    # of each word-initial *DH rule pair has no ``Cə`` slot to match.
    "pnb-PK": {"PA_DH_INITIAL_ɡ˩_0", "PA_DH_INITIAL_dʒ˩_0", "PA_DH_INITIAL_ɖ˩_0", "PA_DH_INITIAL_d̪˩_0", "PA_DH_INITIAL_b˩_0"},
}

#: The Dravidian gemination families target whole CV emissions (``dʒa``, ``kʂa``)
#: that no slot carries directly. Since the mr abugida fix taught this check to
#: add reading + inherent vowel to the producible set for any abugida spec, ta
#: and ml pick up the same treatment and most of these targets turn out to be
#: reachable after all: 18 of ta's TA_GEM rules and 15 of ml's are no longer
#: dead. What is left (0 for ta, 12 for ml) is a systematic bug in one rule
#: generator rather than many independent ones — allowed by prefix so the
#: group is visible and so a *new* dead rule outside it still fails.
#: Krio inherits en-GB's rules through its lexifier link but declares its own
#: graphemes, and the creole's vowel system has none of RP's rhotic nuclei
#: (ɑːɹ, ɜːɹ, ɔːɹ, əɹ …) the coda-/r/ and prevocalic-/r/ rules target, so the
#: whole English rhoticity family is unreachable here. Its tables also have no
#: silent final ⟨e⟩, the target of the English sole-vowel ⟨e⟩ rule.
#: Andh and Deccan are registry stubs under Marathi, declared as pure genealogy
#: ("graphemes": {}, "allophones": {}, script Zyyy, no script_type and no
#: inherent vowel) so the ancestry graph covers every living ISO 639-3 code.
#: Marathi's rules travel down that link but its inventory does not, so the
#: whole MR_ family arrives with no slot to match. These entries go away when
#: either stub gains a cited orthography.
#: pnb-PK is Shahmukhi, an ABJAD: it declares its own Perso-Arabic grapheme
#: table and no ``inherent_vowel``, so no letter ever emits a bare consonant
#: plus schwa. Every Punjabi rule whose target is such a ``Cə`` reading —
#: the whole word-final schwa-deletion family, and the inherent-vowel half of
#: each word-initial *DH pair — has no slot to match here. The bare half of
#: each *DH pair (``PA_DH_INITIAL_*_1``) is live and still checked.
KNOWN_DEAD_PREFIXES = {"ta": ("TA_GEM",), "ml": ("TA_GEM",),
                       "pnb-PK": ("PA_SCHWA_FINAL",),
                       "kri": ("EN_GB_NONRHOTIC", "EN_GB_PREVOCALIC_R",
                               "EN_GB_FINAL_E_SOLE_VOWEL"),
                       "anr": ("MR_",), "dcc": ("MR_",),
                       # crs inherits the fr-FR rule set but has no schwa
                       # slot to match (its parent's open-e rule for ⟨ell⟩,
                       # ⟨ett⟩, ⟨err⟩ has nothing to rewrite there).
                       "crs": ("FR_E_BEFORE_DOUBLED_CONSONANT",)}


@pytest.mark.parametrize("code", ALL_CODES)
def test_no_new_dead_allophone_rules(code):
    """A rule targeting a phoneme the spec cannot produce can never fire."""
    dead = set(dead_allophone_rules(get(code)))
    known = KNOWN_DEAD_RULES.get(code, set())
    prefixes = KNOWN_DEAD_PREFIXES.get(code, ())
    unexplained = {
        rule_id for rule_id in dead - known
        if not (prefixes and rule_id.startswith(prefixes))
    }
    assert not unexplained, (
        f"{code}: new dead allophone rules {sorted(unexplained)} — the target "
        f"phoneme is not in this spec's inventory, so the rule can never fire"
    )


# ─── every token is one segment ─────────────────────────────────────────

@pytest.mark.parametrize("code", ALL_CODES)
def test_no_token_starts_with_a_combining_mark(code):
    """A mark a slot emits alone lands on the segment before it. The coda
    tilde of Portuguese is never a token of its own."""
    assert not [t for t in phoneme_inventory(get(code)) if unicodedata.combining(t[0])]


@pytest.mark.parametrize("code", ALL_CODES)
def test_every_token_is_nfc(code):
    """The engine writes NFC, so a carried mark joins its base as one code
    point where Unicode has one (e + U+0303 is ẽ), and a token never has a
    decomposed twin."""
    assert not [t for t in phoneme_inventory(get(code)) if unicodedata.normalize("NFC", t) != t]


@pytest.mark.parametrize("code", ALL_CODES)
def test_no_token_carries_a_mark_twice(code):
    """A carried mark joins a token only once: bch e̯ and lsi a̰ already hold
    theirs, and the engine never writes e̯̯ or a̰̰."""
    assert not [t for t in phoneme_inventory(get(code))
                if any(a == b and unicodedata.combining(a) for a, b in zip(t, t[1:]))]


@pytest.mark.parametrize("code", ["pt-PT-x-algarve", "pt-PT-x-alentejo"])
def test_a_precomposed_nasal_vowel_the_engine_writes_is_a_token(code):
    """nenhum ends in [ỹ] (U+1EF9) in the lects that front /u/; the carried
    tilde must give that code point, not y + U+0303."""
    spec = get(code)
    ipa = G2P(code).transcribe("nenhum")
    assert "\u1ef9" in ipa
    assert set(tokenize(ipa, spec)) - {"ˈ", "ˌ"} <= phoneme_inventory(spec)


def test_the_coda_tilde_joins_the_vowels_and_glides():
    """pt-PT: the coda ⟨m n⟩ emits a bare tilde, and PT_FINAL_EM_GLIDE emits
    ``̃j̃``. The tilde joins the oral vowels and glides the engine lets carry
    it, and the offglide [j̃] stands alone."""
    inventory = phoneme_inventory(get("pt-PT"))
    assert {unicodedata.normalize("NFC", t) for t in ("ɐ̃", "ẽ", "ĩ", "õ", "ũ", "j̃", "w̃")} <= inventory
    assert not {"\u0303", "\u0303j\u0303", "\u0303w\u0303", "ɐ̃j̃", "ɐ̃w̃"} & inventory
    assert tokenize("ˈɔmɐ̃j̃", get("pt-PT")) == ["ˈ", "ɔ", "m", "ɐ̃", "j̃"]


@pytest.mark.parametrize("code,emission,segments", [
    ("pt-PT", "ks", ["k", "s"]),          # ⟨x⟩ of táxi
    ("pt-PT", "ɡz", ["ɡ", "z"]),          # ⟨x⟩ of exame
    ("pt-PT", "kw", ["k", "w"]),          # ⟨qu⟩ of quatro
    ("pt-PT", "ɡw", ["ɡ", "w"]),          # ⟨gu⟩ of água
    ("pt-PT", "ku", ["k", "u"]),          # ⟨qu⟩ read as a syllable
    ("pt-PT-x-alentejo", "me", ["m", "e"]),            # ⟨meu⟩
    ("pt-PT-x-madeira", "õns", ["õ", "n", "s"]),       # ⟨-ões⟩
    ("pt-PT-x-madeira", "ɐ̃ns", ["ɐ̃", "n", "s"]),       # ⟨-ães⟩
])
def test_a_cluster_or_syllable_is_cut_into_its_segments(code, emission, segments):
    spec = get(code)
    assert emission in emission_inventory(spec)
    inventory = phoneme_inventory(spec)
    assert emission not in inventory
    assert set(segments) <= inventory
    assert tokenize(emission, spec) == segments


@pytest.mark.parametrize("code,segment", [
    ("ar-SA-x-najd", "ts"),   # an affricate without the tie, not declared
    ("ar-SA-x-najd", "dz"),
    ("en-GB", "tʃ"),
    ("en-GB", "dʒ"),
])
def test_an_affricate_stays_one_token_without_the_tie(code, segment):
    spec = get(code)
    assert not spec.phonemes or segment not in spec.phonemes
    assert segment in phoneme_inventory(spec)
    assert tokenize(segment + "a", spec) == [segment, "a"]


def test_one_segment_spellings_stay_whole_and_clusters_do_not():
    from orthography2ipa.inventory import _segments
    assert _segments("t͡s") == ["t͡s"]
    assert _segments("k͡p") == ["k͡p"]
    assert _segments("kp") == ["kp"]
    assert _segments("ŋm") == ["ŋm"]
    assert _segments("ᵐb") == ["ᵐb"]
    assert _segments("ⁿd͡z") == ["ⁿd͡z"]
    assert _segments("d̠ʒ") == ["d̠ʒ"]
    assert _segments("tʃʰ") == ["tʃʰ"]
    assert _segments("n̠d̠ʒ") == ["n̠", "d̠ʒ"]
    assert _segments("t͡sa") == ["t͡s", "a"]
    assert _segments("ks") == ["k", "s"]
    assert _segments("aj") == ["a", "j"]
    assert _segments("mb") == ["m", "b"]
    assert _segments("ʔaː") == ["ʔ", "aː"]


# ─── a bare modifier letter joins the segment before it ─────────────────

@pytest.mark.parametrize("code", ALL_CODES)
def test_no_token_is_a_bare_length_or_palatalization_mark(code):
    """A slot that emits ``ː`` or ``ʲ`` alone (the Arabic shadda, the Cyrillic
    soft sign) modifies the segment before it, so neither is a token."""
    assert not {"ː", "ʲ"} & phoneme_inventory(get(code))


def test_the_soft_sign_palatalizes_the_consonants_before_it():
    """be: ⟨д⟩ → d, ⟨т⟩ → t and ⟨ь⟩ → ʲ, so ⟨дь⟩ is [dʲ] and ⟨ть⟩ is [tʲ]. No
    grapheme writes dʲ or tʲ on its own. A vowel cannot take ʲ."""
    inventory = phoneme_inventory(get("be"))
    assert {"dʲ", "tʲ"} <= inventory
    assert not {"ʲ", "aʲ", "iʲ"} & inventory


def test_the_shadda_lengthens_the_segments_before_it():
    """acq: ⟨ب⟩ → b, ⟨ت⟩ → t and the shadda ⟨ّ⟩ → ː, so ⟨بّ⟩ is [bː] and ⟨تّ⟩ is
    [tː]. A segment that is long already does not take a second mark."""
    inventory = phoneme_inventory(get("acq"))
    assert {"bː", "tː", "aː"} <= inventory
    assert not {"ː", "aːː", "ːː"} & inventory


def test_a_palatalized_long_consonant_keeps_its_length_mark_last():
    """be writes the long consonants sː zː lː nː and the soft sign adds ʲ to
    them, so the token is [sʲː], never [sːʲ]."""
    inventory = phoneme_inventory(get("be"))
    assert {"sʲː", "zʲː", "lʲː", "nʲː"} <= inventory
    assert not [t for t in inventory if "ːʲ" in t]


@pytest.mark.parametrize("code,word", [
    ("abh", "حَجّ"),      # shadda after ج: ʒ + ː
    ("dar", "цьа"),       # soft sign after an aspirated affricate
    ("bo", "ཚཱི"),        # long vowel mark after an aspirated affricate
    ("bo", "ིཚཱི"),
    ("be", "конь"),       # soft sign after a nasal
])
def test_every_token_of_a_real_word_is_in_the_inventory(code, word):
    """An attached mark must give the tokens :func:`tokenize` returns: ``dʒː``
    is cut into ``d`` and ``ʒː``, and ``t͡s`` plus a mark is cut after ``t͡``."""
    spec = get(code)
    tokens = set(tokenize(G2P(code).transcribe(word), spec)) - {"ˈ", "ˌ"}
    assert tokens <= phoneme_inventory(spec), tokens - phoneme_inventory(spec)


@pytest.mark.parametrize("code", ALL_CODES)
def test_an_attached_token_is_one_that_tokenize_returns(code):
    """The tokens a bare mark adds are the pieces :func:`tokenize` cuts out of
    the longer segment, so none of them is a dead embedding."""
    spec = get(code)
    inventory = phoneme_inventory(spec)
    assert not [t for t in inventory
                if ("ʲ" in t or "ː" in t) and t[0] not in "ʲʷːˑ" and tokenize(t, spec) != [t]]


def test_a_shadda_that_doubles_the_letter_adds_no_length_mark():
    """ar writes ⟨بّ⟩ as the doubled letter [bb], so a ː never follows ⟨ب⟩ there.
    acq keeps the shadda as ː, so [bː] is a token."""
    assert "bː" not in phoneme_inventory(get("ar"))
    assert "bː" in phoneme_inventory(get("acq"))
