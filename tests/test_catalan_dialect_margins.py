"""Catalan dialect-margins wave: the two Romance rows that still lost to a
rules-only espeak-ng, ca-x-balear and ca-x-occidental, on the 4catac expert
gold (n=160 sentences per row).

Every rule below was FOUND by a per-sentence differential against
espeak-ng's rules-only build and then justified from the literature.
espeak-ng is the pointer to the phenomenon and never the justification —
no rule here is stated as "espeak does X". Each test carries an
adversarial counter-case: a word or phrase in the same neighbourhood
where the rule must NOT fire, so a rule that over-applies fails here even
when the aggregate PER improves.

Gold-attestation counts are stated per rule, honestly, on the subset of
the 160 sentences whose gold aligns token-for-token with the orthography
(the rest cannot be split per word). n=160 is small: a rule justified by
a handful of sentences would be gold-fitting, so each rule below is a
statement the sources make about the VARIETY, and the gold count is
reported as corroboration, not as the argument.

Refuted experiments are pinned at the bottom with the measurement that
killed them, so a later wave does not re-run them.
"""
import pytest

from orthography2ipa import G2P, get


WESTERN = ["ca-x-occidental", "ca-x-valencia"]
EASTERN = ["ca", "ca-x-balear", "ca-x-nord"]
ALL_CA = ["ca", "ca-x-nord", "ca-x-balear", "ca-x-occidental",
          "ca-x-valencia", "ca-x-alguer", "ca-x-medieval"]


# ── 1. Balearic: the coda rhotic is a TAP ────────────────────────────────

@pytest.mark.parametrize("word,expect", [
    ("carn", "ˈkaɾn"),
    ("porta", "ˈpoɾtə"),
    ("perquè", "pəˈɾkɛ"),
])
def test_balearic_coda_r_is_a_tap(word, expect):
    """Wheeler 2005 §7.1/§2.4 and Recasens 1993 ch. 5: the /ɾ/~/r/ contrast
    is neutralised outside intervocalic position, and Balearic (with
    Valencian) realises the single coda rhotic as the TAP.

    FAIL-BEFORE: on dev these came out with the trill — [ˈkarn], [ˈportə],
    [pəˈrkɛ] — because ca-x-balear's ⟨r⟩ entry fell through to a ["r"]
    default. 102 of the ca-x-balear row's alignment errors were exactly
    this one substitution.
    """
    assert G2P("ca-x-balear").transcribe_word(word) == expect


@pytest.mark.parametrize("word,expect", [
    ("rosa", "ˈrozə"),        # word-initial: trill
    ("carrer", "kəˈre"),      # ⟨rr⟩: trill
    ("honra", "ˈonrə"),       # after heterosyllabic /n/: trill (and see
    ("Enric", "əˈnrik"),      # test_trill_after_l_n_s_is_pan_catalan)
])
def test_balearic_trill_contexts_survive(word, expect):
    """The counter-case to the tap default. The trill is not gone from
    Balearic — it keeps every context Wheeler 2005 §7.1 gives it."""
    assert G2P("ca-x-balear").transcribe_word(word) == expect


@pytest.mark.parametrize("word,expect", [
    ("tres", "ˈtɾəs"),
    ("quatre", "ˈkwatɾə"),
    ("pobre", "ˈpoβɾə"),
])
def test_balearic_obstruent_r_onset_clusters_stay_taps(word, expect):
    """The reason CA_TRILL_AFTER_NLS names /l n s/ instead of using the
    generic ``after_consonant`` position: a tautosyllabic obstruent+r
    onset cluster is a TAP. Stating the trill as "after any consonant"
    was measured and made the ca-x-balear row WORSE (0.1471 -> 0.1534),
    which is the evidence behind the /l n s/ list. Parametrised over
    ca-x-balear here and over every Catalan spec in
    test_obstruent_r_onset_clusters_stay_taps_everywhere."""
    assert G2P("ca-x-balear").transcribe_word(word) == expect


def test_eastern_mainland_keeps_the_coda_trill():
    """Blast-radius pin. The tap is a BALEARIC (and Valencian) statement,
    not a pan-Catalan one: Central and North-Western keep the coda trill
    (Recasens 1993 ch. 5), and the 4catac Central/North-Western gold
    transcribes it that way. Flipping them too was measured and regressed
    both rows (ca 0.0643 -> 0.0752, ca-x-occidental 0.0944 -> 0.1037)."""
    assert G2P("ca").transcribe_word("carn") == "ˈkarn"
    assert G2P("ca-x-occidental").transcribe_word("carn") == "ˈkarn"


@pytest.mark.parametrize("lang", ALL_CA)
@pytest.mark.parametrize("word", ["honra", "Enric"])
def test_trill_after_l_n_s_is_pan_catalan(lang, word):
    """CA_TRILL_AFTER_NLS is declared on ca-x-medieval, so EVERY Catalan
    spec inherits it. Wheeler 2005 §7.1 and Recasens 1993 state the
    context for Catalan, not for one variety.

    FAIL-BEFORE: on dev every one of these came out with a TAP — [ˈɔnɾə],
    [ənˈɾik] — in all seven specs, because ⟨r⟩'s ``before_vowel`` position
    caught it first. The rule was found while fixing the Balearic coda
    rhotic; declaring it on ca-x-balear alone (as the first draft of this
    wave did) would have been fitting the rule to the row that paid for
    it, since the same citation covers Central and Western too.
    """
    assert "r" in G2P(lang).transcribe_word(word)
    assert "ɾ" not in G2P(lang).transcribe_word(word)


@pytest.mark.parametrize("lang", ALL_CA)
@pytest.mark.parametrize("word", ["tres", "quatre", "pobre"])
def test_obstruent_r_onset_clusters_stay_taps_everywhere(lang, word):
    """The pan-Catalan counter-case to the pan-Catalan rule."""
    assert "r" not in G2P(lang).transcribe_word(word).replace("ɾ", "")


def test_balearic_coda_r_rule_is_reachable():
    """Reachability (#858's lesson): CA_TRILL_AFTER_NLS must exist and must
    actually fire, or it is a dead rule dressed as a citation."""
    ids = {r.id for r in get("ca-x-balear").allophone_rules}
    assert "CA_TRILL_AFTER_NLS" in ids
    assert "r" in G2P("ca-x-balear").transcribe_word("honra")


# ── 2. The affricate /dʒ/ does not spirantise ────────────────────────────

@pytest.mark.parametrize("lang", WESTERN)
@pytest.mark.parametrize("phrase,expect_sub", [
    ("la gent", "ˈdʒen"),
    ("de jutge", "ˈdʒudʒe"),
    ("una gent", "ˈdʒen"),
])
def test_western_affricate_never_lenites_across_a_word_boundary(
        lang, phrase, expect_sub):
    """Wheeler 2005 §5.2 / Recasens 1993 §5: post-vocalic spirantisation
    targets the voiced STOPS /b d ɡ/. The affricate /dʒ/ is not one.

    FAIL-BEFORE: CA_EXT_SPIRANT_D's right context was a bare ``^([ˈˌ]?)d``,
    which bit the stop half of the affricate and produced an impossible
    *[ðʒ]: la gent -> *[la ˈðʒen]. Only the Western varieties were hit,
    because they are the ones with the affricate; Eastern has [ʒ].
    """
    assert expect_sub in G2P(lang).transcribe(phrase)
    assert "ðʒ" not in G2P(lang).transcribe(phrase)


@pytest.mark.parametrize("lang", WESTERN + ["ca"])
def test_the_real_stop_still_spirantises(lang):
    """Counter-case: narrowing the regex must not switch the rule off.
    A genuine /d/ after a vowel still lenites."""
    assert "ð" in G2P(lang).transcribe("la dona")


# ── 3. Western glide formation: REFUTED, and pinned as such ─────────────

@pytest.mark.parametrize("lang", WESTERN + EASTERN)
@pytest.mark.parametrize("word,expect_sub", [
    ("València", "ˈlɛnsi"),
    ("notícia", "ˈtisi"),
    ("memòria", "ˈmɔɾi"),
    ("història", "ˈstɔɾi"),
    ("família", "ˈmili"),
    ("església", "ˈsɡlezi"),
    ("experiència", "ˈɛnsi"),
])
def test_the_accented_ia_class_keeps_its_written_accent(lang, word,
                                                        expect_sub):
    """REFUTED RULE, PINNED. A WESTERN_GLIDE_I rule (unstressed /i/ before a
    non-high vowel -> [j], Wheeler 2005 §2.5/§10.2) was written, measured
    and REMOVED from both Western specs.

    It is applied BEFORE stress assignment, so gliding the ⟨i⟩ deletes a
    syllable and the whole accented ⟨-ància -ència -òria -ícia -èdia⟩
    class loses the syllable its WRITTEN ACCENT sits on: València came out
    as *[ˈvalɛnsja] instead of [vaˈlɛnsia], and notícia, memòria,
    història, família, església, experiència with it. The orthography
    states that stress outright (IEC 2016 ch. 3), so no PER gain justifies
    contradicting it.

    Cost of the removal, measured on the 4catac rows: ca-x-occidental
    0.0795 -> 0.0824 (still beats espeak rules-only at 0.0832) and
    ca-x-valencia 0.0653 -> 0.0646, which is BETTER. These counter-cases
    are pinned so a future glide rule cannot reintroduce the defect
    without failing here first.
    """
    assert expect_sub in G2P(lang).transcribe_word(word)


@pytest.mark.parametrize("lang", WESTERN)
def test_no_western_glide_rule_is_declared(lang):
    """The other half of the pin: the rule id must stay absent."""
    ids = {r.id for r in get(lang).allophone_rules}
    assert "WESTERN_GLIDE_I" not in ids
    assert "WESTERN_GLIDE_U" not in ids


# ── 4. North-Western initial atonic ⟨e-⟩ → [a] ──────────────────────────

@pytest.mark.parametrize("word", ["estendre", "escales", "encara", "enciam",
                                  "enrere", "estimat"])
def test_north_western_initial_atonic_e_lowers_to_a(word):
    """Veny 1982 ch. 3 (nord-occidental): «en síl·laba inicial àtona, e > a
    davant de nasal o de s implosiva».

    FAIL-BEFORE: dev kept [e] — [esˈtendɾe], [esˈkales], [eŋˈkaɾa].
    Attested in the token-aligned 4catac North-Western subset in 14 of 15
    eligible types.

    SCOPE: nord-occidental ONLY, deliberately narrower than the
    measurement supports. The Valencian gold attests the same change in
    17 of 18 types, and an earlier revision of this wave declared the rule
    on ca-x-valencia too, citing a Recasens 1996 §5 that could not be
    verified against the source. Gold agreement is not a justification, so
    the Valencian scope was withdrawn — see
    test_valencian_scope_was_withdrawn_for_want_of_a_citation.
    """
    assert G2P("ca-x-occidental").transcribe_word(word).startswith("a")


def test_the_nasal_or_s_must_be_implosive():
    """Counter-case inside the same prefix: enorme keeps [e], because its
    /n/ is the onset of the next syllable and not a coda. Without the
    ``followed_by_2: consonant`` gate this word lowers too."""
    assert G2P("ca-x-occidental").transcribe_word("enorme").startswith("e")


@pytest.mark.parametrize("word", ["este", "esta", "estos", "estes"])
def test_stressed_initial_e_is_untouched(word):
    """The stress gate, and the reason the demonstrative paradigm needs no
    word list: their initial ⟨e⟩ is stressed."""
    assert G2P("ca-x-occidental").transcribe_word(word).startswith("ˈe")


def test_word_internal_atonic_e_is_untouched():
    """Counter-case for the word_initial gate."""
    assert "a" not in G2P("ca-x-occidental").transcribe_word("temperatura")[:4]


def test_valencian_scope_was_withdrawn_for_want_of_a_citation():
    """The withdrawal, pinned. ca-x-valencia must NOT carry the rule until
    a Valencian-scoped source is in hand; escales stays [esˈkales] there.
    Cost of the withdrawal on the 4catac Valencian row: 0.0646 -> 0.0677,
    which still beats espeak rules-only (0.0762)."""
    ids = {r.id for r in get("ca-x-valencia").allophone_rules}
    assert "WESTERN_INITIAL_E_TO_A" not in ids
    assert G2P("ca-x-valencia").transcribe_word("escales").startswith("e")


@pytest.mark.parametrize("lang", EASTERN)
def test_eastern_reduces_the_same_vowel_to_schwa(lang):
    """Blast-radius pin for the East/West split."""
    assert G2P(lang).transcribe_word("escales").startswith("ə")


# ── 5. Elision of the atonic article vowel (Western) ─────────────────────

@pytest.mark.parametrize("lang", WESTERN)
@pytest.mark.parametrize("phrase,gone,expect", [
    # `gone` is the substring dev produced and the branch must NOT: asserting
    # only that "l ˈrej" appears would pass against the UN-elided output too,
    # since "el ˈrej" contains it. Both halves verified by mutation — with
    # CA_ELIDE_EL removed, every `gone` reappears.
    ("ningú el veu", "u el ", "ŋɡu l ˈ"),
    ("i el rei", " el ", "i l ˈrej"),
    ("que el tap", "e el ", "ke l ˈtap"),
])
def test_western_article_vowel_elides_after_a_vowel(lang, phrase, gone,
                                                     expect):
    """Wheeler 2005 §11.2 (elision in external sandhi) and ch. 4 on the
    article's allomorphs; Bonet & Lloret 1998 ch. 5 on clitic vowel
    deletion; IEC 2016 §6.2 lists ⟨el/els⟩ among the atonic monosyllables.
    The article has no vowel to defend — written ⟨l'⟩ before a
    vowel-initial word is the same allomorph.

    FAIL-BEFORE: dev kept [el] in every one of these. In the token-aligned
    4catac subset the two Western rows elide it in all 18 V+⟨el⟩ tokens.
    HONEST CAVEAT: the Eastern rows of the SAME corpus keep [əl] in 17 of
    18, which is why this rule is declared on the Western specs only.
    Whether that is a variety fact or a register difference between the
    two recording teams cannot be settled from n=160; the rule is scoped
    to what is measured and cited, not extrapolated.
    """
    got = G2P(lang).transcribe(phrase)
    assert gone not in got
    assert expect in got


@pytest.mark.parametrize("lang", WESTERN)
@pytest.mark.parametrize("phrase", ["i el rei", "i els reis"])
def test_the_i_clitic_keeps_a_nucleus_when_the_article_elides(lang, phrase):
    """The two rules meet at one boundary and the sandhi engine resolves
    the two sides INDEPENDENTLY, against the original words. Without the
    Western narrowing of CA_CLITIC_GLIDE_I_BEFORE_VOWEL both fire and the
    phrase comes out as *[j l ˈrej] — two words with no syllable nucleus
    between them. There is nothing to glide into once the article has lost
    its vowel, and the 4catac North-Western gold writes [i l ˈrej].
    """
    first = G2P(lang).transcribe(phrase).split()[0]
    assert first == "i"
    assert not G2P(lang).transcribe(phrase).startswith("j ")


@pytest.mark.parametrize("lang", WESTERN)
@pytest.mark.parametrize("phrase", ["i ara", "i això"])
def test_the_i_clitic_still_glides_before_any_other_vowel(lang, phrase):
    """Counter-case: the narrowing names ⟨el⟩/⟨els⟩ and nothing else."""
    assert G2P(lang).transcribe(phrase).startswith("j ")


@pytest.mark.parametrize("lang", WESTERN)
def test_article_vowel_survives_after_a_consonant(lang):
    """Counter-case: after a consonant the support vowel is the only thing
    making the clitic pronounceable, and it stays."""
    assert "el" in G2P(lang).transcribe("amb el tap")


@pytest.mark.parametrize("lang", WESTERN)
def test_elision_is_closed_class_by_construction(lang):
    """The right context is the WHOLE word anchored at both ends, so no
    lexical word starting with the same segments is touched. el·la is the
    adversarial neighbour: same two opening letters, not a clitic."""
    assert "ˈelːɛ" in G2P(lang).transcribe("la el·la") or \
           "ˈelːa" in G2P(lang).transcribe("la el·la")


@pytest.mark.parametrize("lang", EASTERN)
def test_eastern_article_keeps_its_schwa(lang):
    """Blast-radius pin. Adding this rule to ca was measured and REGRESSED
    the Central row (0.0643 -> 0.0658), so it is not there."""
    assert "əl" in G2P(lang).transcribe("i el rei")


# ── 6. Western nasal assimilation stops at the affricates ────────────────

@pytest.mark.parametrize("lang", WESTERN)
@pytest.mark.parametrize("phrase,forbidden", [
    ("mengen", "ɲ"),
    ("enxampar", "ɲ"),
    ("un jutge", "ɲ"),
])
def test_western_nasal_does_not_palatalise_before_an_affricate(
        lang, phrase, forbidden):
    """Recasens 1993 ch. 5; Wheeler 2005 §10.3: nasal place assimilation
    copies the place of the following consonant's CLOSURE, and the closure
    of /tʃ dʒ/ is alveolar, not palatal.

    FAIL-BEFORE: dev gave [ˈmeɲdʒen], [eɲtʃaˈmpa], [uɲ ˈdʒudʒe]. The
    token-aligned 4catac Western gold is categorical: [n] before the
    affricates in all 15 tokens, [ɲ] before the fricatives and /ʎ/ in all
    5. Only Western is affected, because only Western has the affricate
    where Eastern has [ʒ].
    """
    assert forbidden not in G2P(lang).transcribe(phrase)


@pytest.mark.parametrize("lang", WESTERN)
@pytest.mark.parametrize("phrase", ["any llunyà", "un llibre"])
def test_western_nasal_still_palatalises_before_a_lateral(lang, phrase):
    """Counter-case: narrowing the trigger must not switch the rule off."""
    assert "ɲ" in G2P(lang).transcribe(phrase)


@pytest.mark.parametrize("lang", EASTERN)
def test_eastern_still_palatalises_before_its_fricative(lang):
    """Blast-radius pin: Eastern ⟨g+e⟩ is the fricative [ʒ] and the
    inherited pan-Catalan rule is unchanged there."""
    assert "ɲ" in G2P(lang).transcribe_word("àngel")


# ── 7. Refuted experiments ───────────────────────────────────────────────

@pytest.mark.parametrize("lang", WESTERN)
def test_unstressed_u_before_a_vowel_does_not_glide(lang):
    """REFUTED. The back counterpart of WESTERN_GLIDE_I was written,
    shipped into a measurement run, and REMOVED: it made both Western rows
    worse (ca-x-occidental 0.0885 -> 0.0895, ca-x-valencia 0.0736 ->
    0.0743). Wheeler 2005 §2.5 states glide formation for /i/ far more
    strongly than for /u/, and the gold agrees — the /u/ hiatus survives.
    Pinned so a later wave does not re-run the experiment."""
    ids = {r.id for r in get(lang).allophone_rules}
    assert "WESTERN_GLIDE_U" not in ids
    assert "u" in G2P(lang).transcribe_word("actuar")


def test_the_stressed_mid_vowel_remainder_is_left_alone():
    """REFUTED as a rule problem, recorded as the honest ceiling.

    The single largest remaining error class on BOTH Western rows is the
    aperture of an unmarked stressed mid vowel — 99 [o]-for-[ɔ]
    substitutions on ca-x-occidental alone. It is not closed here, and it
    is not a rule: the sources that decide aperture categorically
    (Mascaró 2009 §1's opening contexts, the written accent, the -or/-ió
    endings) are already shipped by the wave-2 Catalan work, and Mascaró
    is explicit that outside them there is no tendency to state. Inventing
    an elsewhere default that fits 160 sentences would be gold-fitting.
    This test pins that the Western specs still declare BOTH apertures as
    candidates rather than collapsing to one."""
    for lang in WESTERN:
        pg = get(lang).positional_graphemes
        assert set(pg["o"]["default"]) == {"o", "ɔ"}
