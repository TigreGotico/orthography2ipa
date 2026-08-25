"""Syllabification maximises the onset only as far as the language licenses it.

Onset Maximisation is a preference law, not a licence (Blevins, "The Syllable
in Phonological Theory", in Goldsmith ed., *The Handbook of Phonological
Theory*, Blackwell 1995, § 3.1; Vennemann, *Preference Laws for Syllable
Structure*, Mouton de Gruyter 1988, ch. 1). Handing a whole medial cluster
forward regardless of what may open a syllable produced e·le·ktro·nisch,
Mo·nsieur and wa·nde·len — onsets no language has.

Each case below names the phonotactic fact it pins.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.stress import _syllables_for
from orthography2ipa.vowels import (
    SONORITY_FRICATIVE, SONORITY_GLIDE, SONORITY_LIQUID, SONORITY_NASAL,
    SONORITY_STOP, SONORITY_VOWEL, is_sibilant, sonority_class)


def syllables(lang, word):
    spec = get(lang)
    diph = spec.stress.diphthongs if spec.stress is not None else ()
    return _syllables_for(word, lang, diph, spec=spec)


def judge(lang):
    """The onset judge for *lang*, built regardless of the opt-in gate.

    The gate decides whether a spec's syllabification is constrained; the
    judge's verdicts are a separate question and are tested directly, so a
    language that does not opt in can still pin what its onsets ARE.
    """
    from orthography2ipa.stress import _OnsetJudge
    return _OnsetJudge(get(lang))


# ── the sonority scale itself ────────────────────────────────────────────

@pytest.mark.parametrize("ipa,tier", [
    ("p", SONORITY_STOP), ("t", SONORITY_STOP), ("b", SONORITY_STOP),
    ("g", SONORITY_STOP),        # Latin ⟨g⟩, not IPA ⟨ɡ⟩ — both are stops
    ("ʔ", SONORITY_STOP),        # a glottal STOP is a stop, not a glide
    ("ts", SONORITY_STOP), ("t͡s", SONORITY_STOP),   # affricates are stops
    ("tʃ", SONORITY_STOP), ("d͡ʒ", SONORITY_STOP), ("pf", SONORITY_STOP),
    ("ᵐb", SONORITY_STOP), ("ⁿd", SONORITY_STOP),   # prenasalized = its stop
    ("h", SONORITY_FRICATIVE), ("ɦ", SONORITY_FRICATIVE),
    ("m̩", SONORITY_VOWEL), ("n̩", SONORITY_VOWEL), ("l̩", SONORITY_VOWEL),
    ("f", SONORITY_FRICATIVE), ("s", SONORITY_FRICATIVE),
    ("m", SONORITY_NASAL), ("n", SONORITY_NASAL), ("ɲ", SONORITY_NASAL),
    ("l", SONORITY_LIQUID), ("r", SONORITY_LIQUID),
    ("ʁ", SONORITY_LIQUID),      # French ⟨r⟩ is a uvular FRICATIVE by its
                                 # features and a liquid by its patterning
    ("j", SONORITY_GLIDE), ("w", SONORITY_GLIDE), ("ɥ", SONORITY_GLIDE),
    ("a", SONORITY_VOWEL), ("y", SONORITY_VOWEL),
])
def test_sonority_scale(ipa, tier):
    assert sonority_class(ipa) == tier


def test_rhotics_are_liquids_whatever_their_phonetics():
    """The rhotic class is phonological, not articulatory (Ladefoged &
    Maddieson 1996, § 7.1): a tap, a trill and a uvular fricative all pattern
    as liquids. Without this, French ⟨br⟩ /bʁ/ is not a rising onset and
    ``septembre`` splits sep-temb-re."""
    for r in "rɾɹɻʀʁ":
        assert sonority_class(r) == SONORITY_LIQUID


def test_sibilants_are_the_appendix_class():
    assert is_sibilant("s") and is_sibilant("z") and is_sibilant("ʃ")
    assert not is_sibilant("f")   # strident but not the appendix in Germanic
    assert not is_sibilant("n")


# ── Dutch: the case #836 diagnosed ───────────────────────────────────────

def test_dutch_elektronisch_does_not_invent_a_ktr_onset():
    """⟨ktr⟩ falls in sonority (stop-stop-liquid) and opens no syllable in any
    language. Only ⟨tr⟩ does, so the ⟨k⟩ closes the preceding syllable."""
    assert syllables("nl", "elektronisch") == ["e", "lek", "tro", "nisch"]


def test_dutch_nasal_plus_stop_is_no_onset():
    """⟨nd⟩ FALLS in sonority — a nasal cannot head a rising onset."""
    assert syllables("nl", "wandelen") == ["wan", "de", "len"]
    assert syllables("nl", "kinderen") == ["kin", "de", "ren"]


def test_dutch_s_plus_stop_stays_an_onset():
    """The sibilant appendix: /s/ is adjoined outside the rising core, which
    is why ⟨st-⟩ opens words (Vennemann 1988, ch. 1; Blevins 1995, § 3.2).
    be-staan, never bes-taan."""
    assert syllables("nl", "bestaan") == ["be", "staan"]


def test_dutch_glide_before_consonant_closes_the_syllable():
    """⟨schrijven⟩: ⟨j⟩ is more sonorous than ⟨v⟩, so ⟨jv⟩ cannot rise into
    the nucleus and the ⟨j⟩ closes the first syllable."""
    assert syllables("nl", "schrijven") == ["schrij", "ven"]


# ── French: the ⟨e⟩/⟨o⟩ aperture blocker ─────────────────────────────────

def test_french_monsieur_has_no_ns_onset():
    assert syllables("fr-FR", "Monsieur") == ["Mon", "sieur"]


def test_french_obstruent_clusters_split():
    """⟨pt⟩ and ⟨bs⟩ are two obstruents with no sibilant appendix: they are
    heterosyllabic, and the preceding syllable is CLOSED — which is exactly
    what the loi de position reads."""
    assert syllables("fr-FR", "septembre") == ["sep", "tem", "bre"]
    assert syllables("fr-FR", "absolu") == ["ab", "so", "lu"]
    assert syllables("fr-FR", "capsule") == ["cap", "su", "le"]


def test_french_obstruent_plus_liquid_stays_together():
    """⟨tr⟩ ⟨br⟩ ⟨bl⟩ rise into the nucleus and are licit onsets — the fix
    must not over-correct and close every syllable."""
    assert syllables("fr-FR", "extra") == ["ex", "tra"]
    assert syllables("fr-FR", "table") == ["ta", "ble"]


def test_french_silent_h_does_not_form_a_cluster():
    assert syllables("fr-FR", "malheur") == ["mal", "heur"]


# ── words that were already right and must not move ──────────────────────

@pytest.mark.parametrize("lang,word,expected", [
    ("nl", "water", ["wa", "ter"]),
    ("nl", "moeder", ["moe", "der"]),
    ("nl", "tafel", ["ta", "fel"]),
    ("nl", "sterk", ["sterk"]),       # one syllable, word-initial cluster
    ("nl", "herfst", ["herfst"]),     # a coda the rule must never touch
    ("fr-FR", "paris", ["pa", "ris"]),
    ("de-DE", "Zeitung", ["Zei", "tung"]),
])
def test_correct_cases_do_not_move(lang, word, expected):
    assert syllables(lang, word) == expected


def test_word_initial_cluster_is_licit_by_definition():
    """The first syllable's onset is never re-judged: a cluster that begins a
    word of the language IS a licit onset of that language."""
    assert syllables("nl", "strand") == ["strand"]
    assert syllables("fr-FR", "structure")[0] == "struc"


# ── the cascade's own guarantees ─────────────────────────────────────────

def test_a_declared_max_onset_is_not_the_default_one():
    """The default ``max_onset`` is a placeholder, not a declaration. Applying
    it as a cap would split ⟨tr⟩ in every language on earth."""
    assert get("nl").stress.max_onset_declared is False
    assert get("ar").stress.max_onset_declared is True


def test_a_multigraph_is_never_cut_in_half():
    """Onsets are judged over the spec's own graphemes, so ⟨sch⟩ ⟨ch⟩ ⟨ng⟩
    stay whole no matter where the boundary falls."""
    assert syllables("nl", "lachen") == ["la", "chen"]
    # ⟨ssch⟩ is two sibilants; the appendix is ONE. Standard Dutch mis-schien
    # (Booij, *The Phonology of Dutch*, OUP 1995, ch. 2).
    assert syllables("nl", "misschien") == ["mis", "schien"]
    assert any("sch" in s for s in syllables("de-DE", "waschen"))


def test_syllabification_is_lossless():
    """Every rebalancing move is a move, never an edit."""
    for lang in ("nl", "fr-FR", "de-DE", "sv", "pt-PT", "ca", "ru"):
        spec = get(lang)
        for word in ("elektronisch", "constant", "abstract", "wandelen",
                     "instrument", "prompt"):
            assert "".join(syllables(lang, word)) == word


def test_without_a_spec_the_split_is_unconstrained():
    """The bare public :func:`syllabify` has no phonotactics to consult, so it
    keeps its documented naive behaviour — no caller is broken by this fix."""
    from orthography2ipa.stress import syllabify
    assert syllabify("elektronisch") == ["e", "le", "ktro", "nisch"]


# ── what the fix is FOR: aperture reads these boundaries ─────────────────

def test_aperture_follows_the_corrected_boundary():
    """The open/closed-syllable positions are read straight off the syllable
    string. With the cluster handed forward wholesale, the ⟨e⟩ of Dutch
    *elektronisch* sat in an OPEN syllable ``le`` — which is why the Dutch
    vowel-aperture and the French loi de position could not be written against
    it. Constrained, it sits in ``lek``: CLOSED, which is what it is."""
    from orthography2ipa.positional import _is_open_syllable
    sylls = syllables("nl", "elektronisch")
    assert sylls[1] == "lek"
    assert _is_open_syllable(sylls[1], spec=get("nl")) is False
    assert _is_open_syllable("le", spec=get("nl")) is True


def test_french_closed_syllables_the_loi_de_position_needs():
    from orthography2ipa.positional import _is_open_syllable
    spec = get("fr-FR")
    for word, idx in (("septembre", 0), ("absolu", 0), ("capsule", 0),
                      ("Monsieur", 0)):
        syll = syllables("fr-FR", word)[idx]
        assert _is_open_syllable(syll, spec=spec) is False, (word, syll)


# ── the four onset shapes, each with the language that needs it ──────────

def test_tie_bar_never_changes_a_verdict():
    """``t͡s`` and ``ts`` are the same affricate written two ways. A judgement
    that depends on U+0361 is judging the typography."""
    from orthography2ipa.vowels import is_affricate
    for bare, tied in (("ts", "t͡s"), ("tʃ", "t͡ʃ"), ("dʒ", "d͡ʒ")):
        assert sonority_class(bare) == sonority_class(tied) == SONORITY_STOP
        assert is_affricate(bare) and is_affricate(tied)


def test_cw_onsets_survive():
    """Obstruent + labial approximant. The head may be ANY obstruent: an
    earlier revision demanded a stop or a non-anterior sibilant on the false
    premise that no Germanic language has ⟨sw⟩ — English *swim*, Swedish
    *svensk* and Icelandic *svartur* all do."""
    for lang, run in [("sv", "kv"), ("sv", "sv"), ("sv", "tv"), ("sv", "qv"),
                      ("is", "sv"), ("ru", "св"), ("ru", "зв"), ("ru", "хв"),
                      ("pl", "kw"), ("pl", "sw"), ("pl", "zw"), ("pl", "chw"),
                      ("pl", "św"), ("de-DE", "zw"), ("de-DE", "schw"),
                      ("el", "σβ")]:
        assert judge(lang).licit(run), (lang, run)
    assert syllables("de-DE", "zwei") == ["zwei"]


def test_greek_sigma_beta_is_tautosyllabic():
    """⟨σβ⟩ begins Greek words (*σβήνω*), so it does not split. An earlier
    revision cited *Λέσ·βος* as the desired answer; it is *Λέ·σβος*."""
    assert judge("el").licit("σβ")


def test_polish_swiat_is_an_onset():
    """⟨św⟩ /ɕf~ɕv/ — the table and the code must agree that it is licensed."""
    assert judge("pl").licit("św")


def test_cj_onsets_over_a_sonorant_head():
    """Icelandic ⟨mj lj nj rj⟩ (*mjólk*, *ljós*, *njóta*, *rjúpa*) and the
    three-member ⟨brj glj⟩ — no rising shape reaches a sonorant head
    (Árnason, *The Phonology of Icelandic and Faroese*, OUP 2011, ch. 5)."""
    for run in ("mj", "lj", "nj", "rj", "brj", "glj"):
        assert judge("is").licit(run), run


def test_sibilant_appendix_is_voiceless_only():
    """German licenses ⟨st⟩ and not ⟨sd⟩, ⟨sb⟩ — so *Ausdruck* and *Hausbau*
    split at the seam the appendix cannot cross."""
    assert syllables("de-DE", "Ausdruck") == ["Aus", "druck"]
    assert syllables("de-DE", "Hausbau") == ["Haus", "bau"]
    assert syllables("nl", "bestaan") == ["be", "staan"]


def test_obstruent_plus_nasal_is_not_blanket_licit():
    """/kn gn pn/ are onsets; /bm/ (homorganic) and /fn/ (fricative) are not
    (Wiese, *The Phonology of German*, OUP 1996, ch. 2)."""
    assert syllables("de-DE", "Abmeldung") == ["Ab", "mel", "dung"]
    assert syllables("de-DE", "Aufnahme") == ["Auf", "nah", "me"]
    assert syllables("nl", "ritme") == ["rit", "me"]


def test_szcz_is_one_appendix():
    """⟨sz⟩+⟨cz⟩ is sibilant + voiceless affricate — the appendix shape."""
    assert judge("pl").licit("szcz")


# ── the token↔syllable contract the aperture positions ride on ───────────

def test_tokens_locate_themselves_in_the_syllabified_word():
    """A character the spec has no grapheme for (a digit, a hyphen) is
    emitted as no token at all. Counting token lengths against syllable
    lengths desynchronised the two and drove every later token into the wrong
    syllable — which read as STRESSED and gave German *jährige* a final ɛ."""
    from orthography2ipa import G2P
    g = G2P("de-DE")
    toks = g._tokenizer.grapheme_tokens("102-jährige")
    sylls = g._syllables_cached("102-jährige")
    mapped = g._map_tokens_to_syllables(toks, sylls)
    assert mapped[-1] == len(sylls) - 1        # final ⟨e⟩ is in the last one
    assert g.transcribe_word("102-jährige").endswith("ɡə")
    assert g.transcribe_word("102-jährige")[1:] == g.transcribe_word("jährige")[1:]


# ── punctuation: what this change does and does not claim ────────────────

def test_punctuation_always_lands_in_the_coda():
    """UNIFORMLY, whether or not a consonant precedes it. An earlier revision
    put the hyphen of *Kaffee-Ersatz* in the onset and the hyphen of
    *peut-être* in the coda, differing only on whether a consonant stood
    before it."""
    assert syllables("de-DE", "Kaffee-Ersatz") == ["Kaf", "fee-", "Er", "satz"]
    assert syllables("fr-FR", "peut-être") == ["peut-", "ê", "tre"]
    # ⟨cc⟩ is one grapheme spelling a single /k/ (French has no phonetic
    # geminates — Fouché 1959; Tranel 1987 §2), so the /k/ is a whole onset
    # and the break falls before it: d'a·ccord = /da.kɔʁ/. The apostrophe
    # still lands in the coda, which is what this test is about.
    assert syllables("fr-FR", "d'accord") == ["d'a", "ccord"]


def test_punctuation_is_transparent_to_syllable_weight():
    """A hyphen is no coda: it cannot make an open syllable closed. It is a
    word boundary, so the syllable ending at it is word-final and drops its
    silent tail — *peut-être* is /pø.tɛtʁ/, never *[pœ]."""
    from orthography2ipa import G2P
    from orthography2ipa.positional import _is_open_syllable
    spec = get("fr-FR")
    assert _is_open_syllable("peut-", spec=spec) is True
    assert _is_open_syllable("peu", spec=spec) is True
    assert _is_open_syllable("peut", spec=spec) is False   # no seam, no strip
    g = G2P("fr-FR")
    assert g.transcribe_word("peut-être") == "pøtɛtʁ"
    assert g.transcribe_word("à-peu-près") == "pøpʁɛ"


# ── the opt-in gate ──────────────────────────────────────────────────────

@pytest.mark.parametrize("lang", ["el", "is", "ru", "pl", "sv", "cs", "sk",
                                  "uk", "fi", "hu", "tr", "da", "nb", "it-IT",
                                  "es-ES", "pt-PT", "ca"])
def test_a_spec_that_has_not_opted_in_is_untouched(lang):
    """The shapes are calibrated on Germanic and Romance. A language whose
    onset inventory exceeds them — Modern Greek ⟨σμ κτ πτ γν μν βγ βδ⟩ all
    begin words and so never split — would have every one of them broken.
    Those specs do not set ``constrain_onsets`` and get the unconstrained
    split, byte-identical to before."""
    from orthography2ipa.registry import get_syllabifier
    from orthography2ipa.stress import syllabify
    spec = get(lang)
    assert spec.constrain_onsets is False
    if get_syllabifier(lang) is not None:
        pytest.skip(f"{lang} ships a syllabifier plugin; the bundled splitter "
                    f"is not what it uses")
    diph = spec.stress.diphthongs if spec.stress is not None else ()
    for word in ("elektronisch", "constant", "abstract", "instrument"):
        assert syllables(lang, word) == syllabify(word, diphthongs=diph)


def test_greek_word_initial_clusters_do_not_split():
    """The Modern Greek rule: a cluster that can begin a word is
    tautosyllabic (Holton, Mackridge & Philippaki-Warburton, *Greek: A
    Comprehensive Grammar*, Routledge 2012, § 1.4)."""
    assert syllables("el", "αναγνωρισμένους") == [
        "α", "να", "γνω", "ρι", "σμέ", "νους"]
    assert syllables("el", "πάχνη") == ["πά", "χνη"]


def test_icelandic_runs_the_unconstrained_path():
    """Icelandic does not opt in, so its syllabification is `dev`'s. ⟨brj⟩
    survives here because nothing re-divided it, not because the judge was
    asked — the judge's verdict on ⟨brj⟩ is pinned separately in
    :func:`test_cj_onsets_over_a_sonorant_head`."""
    from orthography2ipa.stress import syllabify
    spec = get("is")
    assert spec.constrain_onsets is False
    diph = spec.stress.diphthongs if spec.stress is not None else ()
    assert syllables("is", "hnetubrjótur") == syllabify(
        "hnetubrjótur", diphthongs=diph) == ["hne", "tu", "brjó", "tur"]


def test_constrain_onsets_is_inherited_along_the_grapheme_base():
    """Whether a grapheme table's onsets are constrained is a property OF that
    table, so a variety that pulls the table in gets the judgement with it.
    Without this, ``de-AT`` read ``de-DE``'s graphemes while syllabifying them
    by a different rule — a language-feature parity gap, which is a bug."""
    for code in ("nl", "nl-NL", "nl-BE", "de-DE", "de-AT", "de-CH",
                 "de-x-bavarian", "de-x-alemannic", "fr-FR"):
        assert get(code).constrain_onsets is True, code
    # …and it does not leak to a language that never asked for it
    for code in ("el", "is", "sv", "ru", "pl", "pt-PT", "en", "ar"):
        assert get(code).constrain_onsets is False, code


def test_inheritance_is_transitive_and_overridable():
    """``de-x-bavarian`` resolves through ``de-AT`` to ``de-DE``; a spec that
    states the field either way wins over what it would inherit."""
    from orthography2ipa.types import FIELD_INHERITANCE, InheritanceMode
    assert (FIELD_INHERITANCE["constrain_onsets"]
            is InheritanceMode.BASE_SCALAR)
    assert get("de-x-bavarian").constrain_onsets is True   # via de-AT
    assert get("nl-NL").constrain_onsets is True           # stated: no base


def test_a_variant_syllabifies_exactly_like_its_base():
    """The parity the inheritance exists to guarantee."""
    for variant, base in (("nl-BE", "nl"), ("nl-NL", "nl"),
                          ("de-AT", "de-DE"), ("de-x-bavarian", "de-DE")):
        for word in ("elektronisch", "Abmeldung", "wandelen", "misschien"):
            assert syllables(variant, word) == syllables(base, word), (
                variant, word)


# ── the four corrections the cross-language syllable differential forced ──

def test_a_glottal_never_heads_a_complex_onset():
    """⟨h⟩ between a vowel and a consonant closes the syllable it follows —
    German *jäh·rig* (Duden, 28. Aufl., § 107). A placeless glottal makes a
    poor Head (Vennemann 1988, ch. 1). Icelandic ⟨hr- hl- hv-⟩ are
    word-initial and never re-judged."""
    assert syllables("de-DE", "jährige") == ["jäh", "ri", "ge"]
    assert not judge("de-DE").licit("hr")
    assert not judge("nl").licit("hl")


def test_no_homorganic_coronal_stop_plus_lateral():
    """*/tl dl/ is the systematic gap in the Germanic and Romance onset
    inventories. Without it every ⟨-land⟩ compound resyllabified."""
    assert syllables("de-DE", "Gotland") == ["Got", "land"]
    for lang in ("de-DE", "nl", "fr-FR"):
        assert not judge(lang).licit("tl"), lang
        assert not judge(lang).licit("dl"), lang
        # …while the non-coronal ⟨pl kl bl gl fl⟩ stay licit onsets
        for run in ("pl", "kl", "bl", "gl", "fl"):
            assert judge(lang).licit(run), (lang, run)


def test_german_cw_onsets():
    assert syllables("de-DE", "schwer") == ["schwer"]
    assert judge("de-DE").licit("schw")


def test_the_appendix_sibilant_is_voiceless():
    """The extrasyllabic appendix is /s/, not /z/."""
    assert judge("nl").licit("st")
    assert not judge("nl").licit("zd")
    assert syllables("de-DE", "Ausdruck") == ["Aus", "druck"]


def test_a_geminate_never_joins_a_complex_onset():
    """A geminate is heterosyllabic (Hayes 1989). It may stand alone as the
    grapheme the spec declared — *Wa·sser* is unchanged — but it never joins
    a complex onset."""
    assert not judge("de-DE").licit("ssk")
    assert not judge("nl").licit("ssch")
    assert syllables("de-DE", "Wasser") == ["Wa", "sser"]


def test_german_st_splits_medially():
    """Modern German separates ⟨st⟩ — *Fens·ter* (Duden, 28. Aufl., K165)."""
    assert syllables("de-DE", "Fenster") == ["Fens", "ter"]
