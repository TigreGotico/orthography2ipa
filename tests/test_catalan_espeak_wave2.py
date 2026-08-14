"""Catalan beat-espeak wave 2: stressed mid-vowel aperture that is NOT lexical,
and the phrase-level behaviour of the monosyllabic clitics.

Wave 1 (the Majorcan/assimilation wave) closed its residual by calling the
remaining stressed mid-vowel errors "lexical". They are not all lexical. The
literature states the aperture of a stressed mid vowel in three ways, and only
the third is a word list:

1. **The written accent already says it.** ⟨é ó⟩ = close [e o], ⟨è ò⟩ = open
   [ɛ ɔ] (IEC 2016 ch. 3; Wheeler 2005 §3.1). This spec already exploited it in
   every Catalan variety before this wave — the tests below PIN that, so a
   later change cannot quietly break the one part of the problem the
   orthography solves outright.
2. **A named context or ending.** Coda /nt/ closes a stressed ⟨e⟩ (Fabra's
   1906 law of the front mid vowels, restated in Mascaró 2009 §1: the opening
   contexts are l, r, r+non-labial consonant, n'r > /ndr/ and implosive D —
   /nt/ is deliberately not among them, which is what separates entre/centre
   from vendre/prendre). The endings -or/-ors and -ió/-ions carry the regular
   close reflex of Latin long ō (Recasens 1996; Wheeler 2005 §2.3).
3. **The lexeme, and nothing else.** Everything left over. Mascaró 2009 §1 is
   explicit that outside the factors which determine aperture categorically
   there is no clear tendency in either direction (his Conclusions, §9, add
   that those factors do yield an overall predominance of open mid vowels —
   a predominance §1 credits to the factors, not to an elsewhere preference),
   so this spec states the contexts and leaves the remainder to
   ``word_exceptions`` rather than inventing an elsewhere default. The
   refuted-experiment tests at the bottom pin that decision with the evidence
   that produced it.

The residual, counted on the Central 4catac gold. Basis, stated once because
the two units differ: TOKEN counts are over all 160 sentences; the BUCKETS are
over distinct word TYPES drawn from the 82 sentences whose gold aligns
token-for-token with the orthography (the other 78 cannot be split per word).

* Unmarked stressed ⟨e⟩ — 172 tokens, 90 close / 82 open; 139 types. Wheeler's
  cited opening contexts (Mascaró 2009 ex. 1a and 1c) classify 12 types. The
  shipped CA_E_CLOSE_BEFORE_CODA_NT decides 10 more. The remaining 117 fall in
  no cited context at all and split 56 close / 61 open.
* Unmarked stressed ⟨o⟩ — 140 tokens, 82 close / 58 open; 90 types. Cited
  contexts classify 4 types, CA_O_CLOSE_SUFFIX_OR(_CLUSTER) and
  CA_O_CLOSE_SUFFIX_IONS decide 12. The remaining 74 split 31 close / 43 open.

Those two remainders — 117 + 74 = 191 word types — ARE the lexical ceiling.
Both split close to even and both lean slightly OPEN, which is the direct
measurement behind two decisions here: that Mascaró's "no clear tendency" is
real, and that the spec keeps its open elsewhere default rather than flipping
it (see test_central_keeps_the_open_elsewhere_default).

The clitic rules are the other half of the wave: ⟨que⟩, ⟨i⟩, ⟨hi⟩ and ⟨ho⟩ are
closed-class atonic monosyllables (IEC 2016 §6.2) whose vowel elides or glides
into a following vowel-initial word (Wheeler 2005 ch. 11-12; Bonet & Lloret
1998 ch. 5).

Every rule was found by a per-word differential against espeak-ng on the
4catac expert gold and then justified from the literature — espeak is never
the justification, only the pointer to the phenomenon. Each test carries an
adversarial counter-case: a word or phrase in the same neighbourhood where the
rule must NOT fire.
"""
import pytest

from orthography2ipa import get, transcribe


CA_VARIETIES = ["ca", "ca-x-nord", "ca-x-balear", "ca-x-occidental",
                "ca-x-valencia", "ca-x-alguer", "ca-x-medieval"]


# ── 1. The written accent decides aperture, in every variety ──────────────

@pytest.mark.parametrize("lang", CA_VARIETIES)
@pytest.mark.parametrize("word,vowel", [
    ("cafè", "ɛ"),      # è  → open front
    ("nét", "e"),       # é  → close front
    ("allò", "ɔ"),      # ò  → open back
    ("córrer", "o"),    # ó  → close back
])
def test_written_accent_fixes_aperture_in_every_variety(lang, word, vowel):
    """⟨è é ò ó⟩ are not decoration: the IEC orthography writes the aperture
    of the stressed mid vowel directly (IEC 2016 ch. 3; Wheeler 2005 §3.1),
    and no Catalan variety may ignore it. Balearic is included deliberately:
    its stressed ⟨e⟩ defaults to [ə], but an ACCENTED ⟨è⟩/⟨é⟩ still wins."""
    assert vowel in transcribe(word, lang)


@pytest.mark.parametrize("lang", CA_VARIETIES)
@pytest.mark.parametrize("close_word,open_word", [("bé", "bè"), ("sól", "sòl")])
def test_accent_minimal_pairs_stay_distinct(lang, close_word, open_word):
    """COUNTER-CASE — the accent must be doing the work, not the consonants.
    ⟨bé⟩/⟨bè⟩ and ⟨sól⟩/⟨sòl⟩ differ ONLY in the accent, so a spec that
    merely happened to guess one of them right fails here. This is the test
    that caught the North-Western defect this wave fixes: an unconditioned
    ``NW_FINAL_A_STRESSED_KEEP`` rewrote every word-final stressed [ɛ] to
    [a], so ⟨bè⟩ came out [ˈba] and ⟨cafè⟩ [kaˈfa]."""
    assert transcribe(close_word, lang) != transcribe(open_word, lang)


# ── 2. Stressed ⟨e⟩ before a coda /nt/ is close [e] (Central) ──────────────

@pytest.mark.parametrize("word,expected", [
    ("dent", "ˈden"),
    ("vent", "ˈben"),
    ("centre", "ˈsentɾə"),
    ("entre", "ˈentɾə"),
    ("trenta", "ˈtɾentə"),
])
def test_central_stressed_e_closes_before_coda_nt(word, expected):
    """Fabra 1906's law (Mascaró 2009 §1) opens a stressed front mid vowel
    before l, r, r+non-labial consonant, n'r (> /ndr/) and implosive D. Coda
    /nt/ is not an opening context, and the whole -ent/-ment derivational
    family follows: accent, valents, fragments, sobtadament."""
    assert transcribe(word, "ca") == expected


@pytest.mark.parametrize("word,expected", [
    ("vendre", "ˈbɛndɾə"),
    ("prendre", "ˈpɾɛndɾə"),
    ("cendra", "ˈsɛndɾə"),
    ("tendre", "ˈtɛndɾə"),
])
def test_coda_nd_is_not_coda_nt(word, expected):
    """COUNTER-CASE, and the reason the rule keys on the STOP rather than on
    the nasal: /ndr/ words are exactly the ones Fabra's n'r member opens
    (they come from a syncopated n'r), and they are spelled like the /nt/
    words. A rule stated over "e before a nasal" would wreck all four."""
    assert transcribe(word, "ca") == expected


@pytest.mark.parametrize("lang,word", [
    ("ca-x-valencia", "dent"), ("ca-x-occidental", "dent"),
    ("ca-x-balear", "dent"),
])
def test_coda_nt_rule_does_not_leak_to_varieties_that_opt_out(lang, word):
    """The rule is declared on ``ca`` only. Valencian and North-Western
    already default a stressed unmarked ⟨e⟩ to close [e] (no reduction, and
    the Western vowel system), and Balearic defaults it to [ə] (wave 1); in
    all three the rule would be vacuous or actively wrong, so they do not
    inherit it."""
    ids = {r.id for r in get(lang).allophone_rules}
    assert "CA_E_CLOSE_BEFORE_CODA_NT" not in ids


# ── 3. The endings -or/-ors and -ió/-ions take close [o] ──────────────────

@pytest.mark.parametrize("word,expected", [
    ("amor", "əˈmo"),
    ("color", "kuˈlo"),
    ("colors", "kuˈlos"),
    ("autor", "əˈwto"),
    ("menjador", "məɲʒəˈðo"),
])
def test_suffix_or_takes_close_o(word, expected):
    """-or/-ors (< Latin -ŌRE, -ATŌRE) is the regular close reflex of a Latin
    long ō (Recasens 1996; Wheeler 2005 §2.3), not a lexical fact."""
    assert transcribe(word, "ca") == expected


@pytest.mark.parametrize("word,expected", [
    ("tambor", "təˈmbo"),
    ("ardor", "əˈrðo"),
])
def test_suffix_or_reaches_past_a_complex_onset(word, expected):
    """The sister rule CA_O_CLOSE_SUFFIX_OR_CLUSTER: same ending, same claim,
    but the stem vowel sits one slot further back because the stressed ⟨o⟩
    has a complex onset."""
    assert transcribe(word, "ca") == expected


@pytest.mark.parametrize("word,expected", [
    ("flor", "ˈflɔ"),     # CCVr monosyllable — the bug the stem gate had
    ("flors", "ˈflɔs"),
    ("plor", "ˈplɔ"),
    ("clor", "ˈklɔ"),
    ("cor", "ˈkɔr"),      # mono-morphemic: no stem before the ⟨o⟩
    ("or", "ˈɔr"),
    ("porc", "ˈpɔrk"),    # ⟨o⟩ + rhotic + consonant: not the ending
    ("nord", "ˈnɔrt"),
    ("suport", "suˈpɔrt"),
])
def test_suffix_or_rule_does_not_swallow_roots(word, expected):
    """COUNTER-CASE — the rule is stated over the ENDING, so it must not fire
    on a root that merely happens to end in ⟨or⟩.

    ⟨flor⟩/⟨plor⟩/⟨clor⟩ are the ones that matter and the ones an earlier
    draft of this rule got WRONG. Its stem gate was ``preceded_by_2: any``,
    which a monosyllable's ONSET CLUSTER satisfies — so ⟨flor⟩ closed to
    [ˈflo], and ⟨cor⟩/⟨or⟩ survived only because their onset happens to be a
    single consonant. The gate is now a preceding VOWEL, which is what
    actually states 'the ⟨o⟩ is not in the first syllable': no monosyllable
    has one, whatever its onset. ⟨porc⟩/⟨nord⟩/⟨suport⟩ are excluded by the
    word-boundary condition instead."""
    assert transcribe(word, "ca") == expected


@pytest.mark.parametrize("word,expected", [
    ("estacions", "əstəsiˈons"),
    ("accions", "əksiˈons"),
    ("donacions", "dunəsiˈons"),
])
def test_plural_ions_takes_close_o(word, expected):
    """The singular -ió carries the written acute (estació) and is handled by
    the accent alone; only the plural -ions drops it, which is the gap this
    rule closes."""
    assert transcribe(word, "ca") == expected


# ── 4. ⟨que⟩ elides its schwa before a vowel-initial word ─────────────────

@pytest.mark.parametrize("phrase,expected_first", [
    ("que havien", "k"),
    ("que ens", "k"),
    ("que agafés", "k"),
])
def test_que_elides_before_a_vowel(phrase, expected_first):
    """Phrase-level elision of the final unstressed [ə] of the atonic
    ⟨que⟩ (Wheeler 2005 ch. 11; Bonet & Lloret 1998 ch. 5; ⟨que⟩ is in the
    IEC 2016 §6.2 mots-àtons closed class)."""
    assert transcribe(phrase, "ca").split()[0] == expected_first


def test_que_survives_before_a_consonant():
    """COUNTER-CASE — nothing elides when the next word starts with a
    consonant."""
    assert transcribe("que la", "ca").split()[0] == "kə"
    assert transcribe("que no", "ca").split()[0] == "kə"


@pytest.mark.parametrize("lang", ["ca-x-valencia", "ca-x-occidental"])
def test_que_elision_is_eastern_only(lang):
    """The Western block does not reduce: its ⟨que⟩ is [ke], not [kə], and
    the 4catac Valencian and North-Western expert transcriptions keep it
    intact before a vowel. The rule is not declared there."""
    ids = {r.id for r in get(lang).sandhi_rules}
    assert "CA_QUE_ELISION" not in ids


def test_que_elision_covers_the_whole_eastern_block():
    """"Eastern" is Central AND Northern, not Central alone: Rossellonès
    reduces too and its ⟨que⟩ is [kə]. Declared there on the same citation,
    though unmeasured — 4catac covers Central, Balearic, North-Western and
    Valencian, not Rossellonès."""
    assert transcribe("que havien", "ca-x-nord").split()[0] == "k"
    assert transcribe("que la", "ca-x-nord").split()[0] == "kə"


# ── 5. The monosyllabic clitics ⟨i⟩ ⟨hi⟩ ⟨ho⟩ glide before a vowel ────────

@pytest.mark.parametrize("lang", ["ca", "ca-x-nord", "ca-x-balear",
                                  "ca-x-occidental", "ca-x-valencia"])
@pytest.mark.parametrize("phrase,index", [
    ("on hi ha", 1),
    ("príncep i arriba", 1),
    ("i arribo", 0),
])
def test_clitic_i_glides_before_a_vowel_in_every_dialect(lang, phrase, index):
    """The trigger is the FOLLOWING vowel, not a preceding one — which is
    what the inherited CA_HIATUS_GLIDE_I could not see (its left context
    requires a preceding vowel, so it misses ⟨on hi ha⟩, ⟨príncep i
    arriba⟩ and an utterance-initial ⟨I arribo⟩). Wheeler 2005 ch. 11-12;
    Bonet & Lloret 1998 ch. 5. All four 4catac dialect golds agree, so the
    rule is declared on every dialect spec.

    The second probe used to be ⟨príncep i el⟩ and was changed
    DELIBERATELY. The Western specs now elide the article's vowel after a
    vowel (CA_ELIDE_EL), so ⟨el⟩ presents nothing to glide into, and the
    4catac North-Western gold writes that very phrase — el príncep i el
    rei — as [... i l ˈrej], with the ⟨i⟩ syllabic. Gliding it there
    produced *[j l ˈrej], two words with no nucleus between them. The
    clitic rule is unchanged in substance; only the probe moved off the
    one right-hand word that is now a counter-case. See
    tests/test_catalan_dialect_margins.py::
    test_the_i_clitic_keeps_a_nucleus_when_the_article_elides.
    """
    assert transcribe(phrase, lang).split()[index] == "j"


@pytest.mark.parametrize("lang", ["ca", "ca-x-nord", "ca-x-balear",
                                  "ca-x-occidental", "ca-x-valencia"])
def test_clitic_i_stays_syllabic_before_a_consonant(lang):
    """COUNTER-CASE — no following vowel, no glide."""
    assert transcribe("pins i coberts", lang).split()[1] == "i"


def test_the_matching_ho_glide_is_deliberately_not_shipped():
    """REFUTED EXPERIMENT, pinned. The 4catac gold glides the neuter clitic
    ⟨ho⟩ the same way (no ho abastes [ˈno w əˈβastəs]), and the rule was
    written and measured (−0.0005 PER on Central). It is NOT shipped: a
    sandhi rule matches IPA, and after Eastern reduction the disjunctive
    conjunction ⟨o⟩ is ALSO [u] — but ⟨o⟩ is a word in its own right and
    must stay syllabic, as ``test_glide_never_leaves_a_bare_nonsyllabic_word``
    in ``test_catalan_phonology.py`` already pinned. The two are
    indistinguishable at the layer the rule runs on, so the rule cannot be
    made correct, and 0.0005 does not buy a wrong one. ⟨i⟩/⟨hi⟩ have no such
    clash: both glide in the gold, which is why that rule ships."""
    assert transcribe("no ho abastes", "ca").split()[1] == "u"
    assert transcribe("O Anna o Eva", "ca").split()[0] == "u"
    for lang in ("ca", "ca-x-nord", "ca-x-balear", "ca-x-valencia",
                 "ca-x-occidental"):
        ids = {r.id for r in get(lang).sandhi_rules}
        assert "CA_CLITIC_GLIDE_U_BEFORE_VOWEL" not in ids


# ── 6. What stayed lexical, and why — the refuted experiments ─────────────

def test_central_keeps_the_open_elsewhere_default():
    """REFUTED EXPERIMENT, pinned so it is not retried blind.

    The obvious move — since Wheeler 2005's Table 1 (Mascaró 2009 ex. 1)
    states only contexts that EXCLUDE the close vowel, rank the close vowel
    first everywhere else — was measured on the 4catac Central gold and made
    things WORSE: PER 0.0793 → 0.0841 for both vowels, 0.0783 for ⟨e⟩ alone
    (a wash) and 0.0852 for ⟨o⟩ alone. Mascaró 2009 §1 is the reason: outside
    the factors that determine aperture categorically, "no s'observen
    tendències clares en un sentit o altre". The Conclusions (§9) do report
    a real overall predominance of OPEN mid vowels — but §1 attributes that
    predominance to those same categorical factors, which this spec now
    states outright, so adopting a close elsewhere default would have been
    reading §9 against §1. Measuring it settled the matter.
    """
    e = get("ca").positional_graphemes["e"]["default"]
    o = get("ca").positional_graphemes["o"]["default"]
    assert e[0] == "ɛ" and "e" in e
    assert o[0] == "ɔ" and "o" in o


def test_palatal_lateral_does_not_raise_a_preceding_e():
    """REFUTED EXPERIMENT. Wheeler 2005 is reported (Renwick & Nadeu 2019) as
    giving /ʎ/ a raising effect on a preceding front mid vowel, which would
    give castell/cervell/ell close [e]. Measured, it made Central WORSE
    (0.0793 → 0.0800): the demonstratives ⟨aquell⟩/⟨aquella⟩ are frequent and
    open, and on this gold they outweigh the nouns. Left unstated rather than
    shipped with a demonstrative word-list bolted on to rescue it."""
    assert transcribe("ell", "ca") == "ˈɛʎ"
    assert transcribe("aquell", "ca") == "əˈkɛʎ"


@pytest.mark.parametrize("word,expected", [
    ("dent", "ˈden"),        # CA_E_CLOSE_BEFORE_CODA_NT
    ("color", "kuˈɾo"),      # CA_O_CLOSE_SUFFIX_OR (+ Alguerese rhotacism)
    ("accions", "aksiˈons"),  # CA_O_CLOSE_SUFFIX_IONS
    ("flor", "ˈflɔ"),        # ... and the stem gate holds here too
])
def test_alguerese_inherits_the_aperture_rules_by_descent(word, expected):
    """DISCLOSED INHERITANCE, pinned. ca-x-alguer declares no rule layer of
    its own — its parent is ``ca`` — so it takes every wave-2 rule along with
    every Central rule it already inherited (CA_CENTRAL_CLOSE_O among them).
    That is defensible: alguerès keeps the same seven-quality tonic vowel set
    with the same phoneme identities as Central (its è/ò are merely less open
    acoustically, which this spec documents and does not re-map), and -ŌRE /
    -IŌNE are reflexes of the whole language, not a Central innovation.

    It is NOT measured: this repo has no Alguerese gold. The spec's notes say
    so in those words, and this test exists so the inheritance is a stated,
    visible commitment rather than a silent side effect — if Alguerese
    evidence ever contradicts it, the spec opts out by re-declaring the ids
    with no phonemes and this test changes with it."""
    assert transcribe(word, "ca-x-alguer") == expected


def test_lexical_mid_vowels_are_listed_not_derived():
    """The honest residual: Central ⟨torn⟩/⟨forma⟩ are close and ⟨porc⟩/
    ⟨nord⟩ open in the SAME phonological context, so no rule can separate
    them — Mascaró 2009 §1's "no clear tendency" case. Closed-class items
    that the gold shows this spec getting wrong are listed instead."""
    exc = get("ca").word_exceptions
    for closed_class in ("he", "meu", "meva", "teu", "teva", "seu",
                         "ser", "fer"):
        assert closed_class in exc
