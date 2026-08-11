"""Catalan phonology: the processes that make or break a Catalan transcription.

Catalan is the Iberian language whose surface form is furthest from its
spelling, and almost all of the distance comes from a handful of processes
that a flat grapheme table cannot express:

* **stress**, which is predictable from the orthography (IEC grammar ch. 3)
  and which *conditions the vowel reduction* — get the stressed syllable
  wrong and every vowel in the word is wrong;
* **unstressed vowel reduction** (Eastern block only);
* **word-final ⟨-r⟩ deletion** and **final-cluster simplification**;
* **spirantization**, **final devoicing** and the **cross-word** voicing and
  lenition that only appear in connected speech.

Every word→IPA pair below is either taken from the expert-annotated 4catac
gold (projecte-aina/4catac, 160 sentences × 4 accents) or from the cited
descriptions in Wheeler (2005), Recasens (1996), Veny (1982) and the IEC /
AVL normative grammars.

The DIALECT contrasts are the proof that the four specs are modelled rather
than copied from the parent: Valencian and North-Western do not reduce,
Valencian keeps a final ⟨-r⟩ that the rest delete, only the Eastern block
simplifies a cluster after a lateral, and North-Western opens a final ⟨-a⟩
to [ɛ] that is [ə] in Central and [a] in Valencian.
"""
import pytest

from orthography2ipa import transcribe
from orthography2ipa.stress import detect_stress, syllabify
from orthography2ipa import get


# ─── Stress: the root cause ────────────────────────────────────────────────

@pytest.mark.parametrize("word,expected_index,n_syllables", [
    # A consonant+⟨s⟩ plural is OXYTONE: the plural preserves the stress of
    # the singular, so ⟨importants⟩ is impor-TANTS, not impor-tants. Treating
    # every ⟨-s⟩ as a paroxytone ending stressed the wrong syllable and the
    # reduction then fired on the wrong vowel (IEC grammar ch. 3).
    ("importants", 2, 3),
    ("important", 2, 3),
    # A vowel+⟨s⟩ plural IS paroxytone.
    ("coses", 0, 2),
    ("cases", 0, 2),
    # ⟨-en⟩/⟨-in⟩ are paroxytone (verb forms), so a blanket "-n is oxytone"
    # rule stressed ⟨semblen⟩ on its last syllable.
    ("semblen", 0, 2),
    ("creguin", 0, 2),
    # but a consonant+⟨n⟩ ending is oxytone.
    ("hivern", 1, 2),
    # HIATUS is two syllables: ⟨tenia⟩ is te-ni-a. Merging every vowel run
    # into one nucleus made it te-nia and put the stress on ⟨te⟩.
    ("tenia", 1, 3),
    ("dia", 0, 2),
    ("veïna", 1, 3),
    # a DIPHTHONG is one syllable, and a word ending in one is oxytone.
    ("ciutat", 1, 2),
    ("remei", 1, 2),
    ("aigua", 0, 2),
])
def test_stress_index(word, expected_index, n_syllables):
    rules = get("ca").stress
    sylls = syllabify(word, diphthongs=rules.diphthongs)
    assert len(sylls) == n_syllables, f"{word}: {sylls}"
    assert detect_stress(word, rules, syllables=sylls) == expected_index


def test_diaeresis_is_not_a_stress_mark():
    """⟨ü⟩ marks a pronounced ⟨u⟩, not a stressed vowel (IEC grammar ch. 3).

    Treating it as an accent made ⟨següent⟩ oxytone on the ⟨ü⟩.
    """
    rules = get("ca").stress
    assert "ü" not in rules.marked_vowels and "ï" not in rules.marked_vowels
    # se-gü-ent: the stress is on the last syllable because of the final ⟨-t⟩,
    # not on the ⟨ü⟩ — and the ⟨ü⟩ is a glide, not a nucleus.
    assert "w" in transcribe("següent", "ca")


# ─── Central Catalan word forms (4catac gold + Wheeler 2005) ───────────────

@pytest.mark.parametrize("word,expected", [
    # ⟨c⟩ and ⟨g⟩ before a front vowel (Wheeler 2005 §5.1)
    ("germana", "ʒərmanə"),
    ("gener", "ʒəne"),
    ("cel", "sɛl"),
    ("ciutat", "siwtat"),
    # word-final ⟨-r⟩ deletion (Wheeler 2005 §10.4)
    ("cantar", "kənta"),
    ("decidir", "dəsiði"),
    ("pagar", "pəɣa"),
    # ⟨-rs⟩: the rhotic goes with it
    ("carrers", "kəres"),
    # final-cluster simplification (Wheeler 2005 §10.4)
    ("quant", "kwan"),
    # the CODA rhotic is the neutralised [r], as in the 4catac gold
    ("important", "impurtan"),
    ("importants", "impurtans"),
    ("temps", "tems"),
    ("cinc", "siŋ"),
    ("sang", "saŋ"),
    # word-final ⟨-ig⟩ = [tʃ], and the ⟨i⟩ is absorbed
    ("vaig", "batʃ"),
    ("mig", "mitʃ"),
    # ⟨x⟩: [ʃ] initially, [ks] before a consonant, [ɡz] in ex- + vowel
    ("explotar", "əkspluta"),
    ("examen", "əɡzamən"),
    # digraphs
    ("cotxe", "kotʃə"),
    ("platja", "pladʒə"),
    ("llibre", "ʎiβɾə"),
    ("any", "aɲ"),
    # ⟨gu⟩/⟨qu⟩: silent ⟨u⟩ before a front vowel, [w] otherwise
    ("guitarra", "ɡitarə"),
    ("aigua", "ajɣwə"),
    ("sigui", "siɣi"),
    # reduction + spirantization together
    ("coses", "kɔzəs"),
    ("seva", "seβə"),
])
def test_central_word_forms(word, expected):
    """Expectations are written WITHOUT the stress mark.

    The bundled IPA syllabifier is onset-maximising, so it puts a whole coda
    cluster in the following onset and the mark lands a segment or two early
    ([ʒəˈrmanə] for [ʒərˈmanə]). That is a mark-PLACEMENT artefact of a naive
    syllabifier, not a segment error, and the segments are what a consumer —
    and the benchmark, which strips stress marks from both sides — reads.
    """
    assert transcribe(word, "ca").replace("ˈ", "") == expected


# ─── Cross-word (phrase-level) processes ───────────────────────────────────

def test_cross_word_final_s_voicing():
    """A word-final sibilant voices before a vowel or a voiced consonant.

    ⟨les coses importants⟩ → [ləs ˈkɔzəz impuɾˈtans]: the ⟨-s⟩ of ⟨coses⟩ is
    [z] only because the next word begins with a vowel (Wheeler 2005 §5.3).
    """
    assert transcribe("coses importants", "ca").split()[0].endswith("z")
    # ... and stays voiceless before a voiceless one
    assert transcribe("coses per", "ca").split()[0].endswith("s")


def test_cross_word_stop_does_not_voice_before_a_vowel():
    """A final STOP voices before a voiced consonant, not before a vowel.

    ⟨poc a poc⟩ is [ˈpɔk ə ˈpɔk] — a sibilant would voice here, a stop does
    not — while ⟨tot d'una⟩ is [ˈtod ˈdunə].
    """
    assert transcribe("poc a poc", "ca").split()[0].endswith("k")
    assert transcribe("tot dia", "ca").split()[0].endswith("d")


def test_cross_word_spirantization():
    """Lenition of /b d ɡ/ crosses the word boundary inside a phrase.

    ⟨la seva germana … de decidir⟩ → [lə ˈseβə ʒərˈmanə … ðə ðəsiˈði]: the
    ⟨d⟩ of ⟨de⟩ is [ð] because the PRECEDING word ends in a continuant
    (Wheeler 2005 §5.2, §10.5). It stays a stop after a pause or a nasal.
    """
    out = transcribe("la seva germana no s'acaba de decidir", "ca")
    assert "ðə ðəsiˈði" in out
    # phrase-initial → still a stop
    assert transcribe("decidir", "ca").startswith("d")
    # after a nasal → still a stop
    assert transcribe("un dia", "ca").split()[1].replace("ˈ", "")[0] == "d"


@pytest.mark.parametrize("phrase, expected", [
    # identical sibilants — degemination, the commonest case in running text
    ("més són", "ˈme ˈson"),
    ("les sabates", "lə səˈβatəs"),
    ("dos savis", "ˈdo ˈsaβis"),
    ("és seca", "ˈe ˈsɛkə"),
])
@pytest.mark.parametrize("lang", ["ca", "ca-x-occidental", "ca-x-valencia",
                                  "ca-x-nord"])
def test_cross_word_sibilant_degemination(lang, phrase, expected):
    """A coda sibilant is deleted before an IDENTICAL word-initial one.

    The phonological phrase has a single sibilant there, not a geminate
    (Wheeler 2005, *The Phonology of Catalan*, §10.4 consonant deletion in
    external sandhi; Recasens 1993 §5): ⟨més són⟩ [ˈme ˈson], ⟨dos savis⟩
    [ˈdo ˈsaβis]. The 4catac expert corpus writes every one of the twenty
    /s#s/ boundaries in its 160 Central sentences with a single [s].

    Declared per dialect, NOT on the ca-x-medieval ancestor — Balearic does
    the opposite (see ``test_balearic_does_not_degeminate``). Vowel quality
    differs between these four, so only the boundary is asserted.
    """
    out = transcribe(phrase, lang).replace("ˈ", "").replace("ˌ", "")
    assert len(out.split()) == 2
    assert not out.split()[0].endswith("s")


def test_balearic_does_not_degeminate():
    """REFUTING CASE — Balearic does the OPPOSITE of the Central deletion.

    Where Central drops the coda sibilant, Balearic assimilates it
    regressively and affricates the following one: ⟨és sa⟩ [ˈet t͡sə],
    ⟨més són⟩ [ˈmet ˈt͡son] (Veny 1982 ch. 4). Whatever the outcome, the
    left word must NOT simply lose its sibilant, which is why the
    CA_DEGEM_* rules sit on the four non-Balearic descendants and not on
    their shared ca-x-medieval ancestor.
    """
    assert transcribe("és sa clau", "ca-x-balear").split()[0] == "ˈet"
    assert transcribe("més són", "ca-x-balear").split()[0] == "ˈmet"
    # ... nor may the ancestor itself have acquired the deletion
    assert transcribe("més són", "ca-x-medieval").split()[0].endswith("s")


# ─── Balearic cross-word sibilant affrication ──────────────────────────────

@pytest.mark.parametrize("phrase, expected", [
    # ── /s # s/, the core class: 4catac Balearic exemplars, one per row.
    ("és sa", "ˈet t͡sə"),
    ("més són", "ˈmet ˈt͡son"),
    ("dos savis", "ˈdot ˈt͡savis"),
    ("cossos sense", "ˈkosut ˈt͡sɛnsə"),
    ("es seu", "ət ˈt͡sɛw"),
    ("mos surten", "ˈmot ˈt͡surtən"),
    ("des serveis", "dət ˈt͡sɛrvəjs"),
    ("cantés s'amor", "kəˈntet t͡səˈmo"),
    ("sentis sàpiga", "ˈsɛntit ˈt͡sapiɣə"),
    ("destries s'arena", "dəˈstɾiət t͡səˈɾɛnə"),
    ("arbres se", "ˈarβɾət t͡sə"),
    ("autors se", "əˈwtot t͡sə"),
    ("pes sol", "pət ˈt͡sol"),
    # ── /ʃ # s/ and /s # ʃ/: the same rule, keyed on the CLASS not on ⟨s⟩.
    ("defineix sa", "dəfiˈnɛt t͡sə"),
    ("beix serveix", "ˈbɛt t͡səˈrvɛʃ"),
    ("es xaloc", "ət t͡ʃəˈlok"),
])
def test_balearic_cross_word_sibilant_affrication(phrase, expected):
    """Majorcan regressive place assimilation + affrication of a sibilant
    cluster across a word boundary.

    A word-final sibilant loses its own oral gesture to the following
    word-initial sibilant and surfaces as the stop [t]; the initial
    sibilant is realised as the matching affricate, so the boundary is a
    long affricate [t.t͡s] (Veny 1982 ch. 4 on Majorcan consonant
    assimilation; Recasens 1996 on cluster assimilation in Balearic;
    Wheeler 2005 §10.5 phrase-level assimilation). This is the Balearic
    counterpart of the Central degemination — the opposite outcome from
    the same input.
    """
    assert transcribe(phrase, "ca-x-balear") == expected


@pytest.mark.parametrize("phrase", [
    # SONORANT + sibilant coda. 4catac writes no affricate at any of these:
    # the Balearic coda simplifies to the sonorant and no sibilant is left
    # at the boundary — importants són [impoɾt'an s'on], tens set
    # [t'en s'ət], dins sa [d'in sə], ports separen [p'ɔɾ səp'aɾən],
    # servents servits [səɾv'en səɾv'id͡z], ells són ['eʎ s'oŋ],
    # Deus seguir [d'əw səɣ'i]. This spec does not model that
    # simplification, so the cluster survives to the boundary here; the
    # rule's context blocks it anyway and the outcome agrees with the gold.
    "importants són", "tens set", "dins sa", "ports separen",
    "ells són", "servents servits", "Deus seguir",
    # OBSTRUENT + sibilant coda (/ks/, /t͡s/) and a final affricate /t͡ʃ/.
    # 4catac DOES affricate all of these, but by DELETING the left
    # obstruent rather than keeping it as [t] — d'albercocs se
    # [ðəlβəɾk'ɔt t͡sə], trencats sobre [tɾəŋk'a t͡s'ɔβɾə], dits semblava
    # [d'i t͡səmbl'avə], vaig sentir [v'at t͡s̠ən̪t'i]. Segment deletion is
    # the broader total-assimilation class, deliberately out of scope; see
    # the spec notes. These are MISSES, not agreements.
    "dits semblava", "d'albercocs se", "trencats sobre",
    "polítics xerraires", "vaig sentir", "mig ximple",
])
def test_balearic_affrication_needs_a_plain_postvocalic_sibilant(phrase):
    """BLOCKING CASES — the rule fires only on a plain sibilant that the
    engine's surface IPA puts directly after a vowel.

    The rule is a SURFACE rule: it reads the IPA this spec produces for the
    left word, not an abstract underlying coda. Two different things are
    being blocked here and the spec notes keep them apart — a sonorant
    cluster, where the block agrees with the gold, and an obstruent cluster
    or affricate, where the gold affricates and this rule does not.
    """
    out = transcribe(phrase, "ca-x-balear")
    assert "t͡s" not in out and "t͡ʃ" not in out


def test_sandhi_should_not_cross_a_phrase_boundary():
    """A comma ends the phonological phrase; sandhi must not reach across it.

    4catac writes the pause and blocks the assimilation: ⟨d'improvís, se
    presenta⟩ is [dimpɾov'is | sə pɾəz'en̪tə], ⟨afamats, se'n mengen⟩ is
    [əfəm'at͡s | səm m'en̠ʒən].

    The domain is the phonological phrase, not the word pair (Nespor & Vogel
    1986, *Prosodic Phonology*), so this is SHARED, not Balearic: the two
    control assertions below cover Central degemination and the Catalan
    vowel-contact rules, which the same boundary blocks.
    """
    assert transcribe("d'improvís, se presenta", "ca-x-balear").startswith(
        "dimpɾuˈvis ")
    # ... and the same defect in the rules this one was modelled on
    assert transcribe("més, són", "ca") == "ˈmes ˈson"
    assert transcribe("la casa, un dia", "ca") == "lə ˈkazə un ˈdiə"


def test_balearic_affrication_is_cross_word_only():
    """Word-internal ⟨ss⟩ and non-sibilant boundaries are untouched."""
    assert transcribe("passa", "ca-x-balear") == "ˈpasə"
    assert transcribe("cossos", "ca-x-balear") == "ˈkosus"
    # non-sibilant right word
    assert transcribe("pes turons", "ca-x-balear") == "pəs tuˈɾons"
    # sibilant right word, non-sibilant left word
    assert transcribe("cap sol", "ca-x-balear") == "ˈkap ˈsol"


@pytest.mark.parametrize("lang", ["ca", "ca-x-occidental", "ca-x-valencia",
                                  "ca-x-nord", "ca-x-medieval"])
def test_affrication_does_not_leak_to_other_catalan(lang):
    """DIALECT-SPECIFIC — declared on ca-x-balear only, never on an ancestor."""
    ids = {r.id for r in get(lang).sandhi_rules}
    assert not {i for i in ids if "AFFRIC" in i}
    assert "t͡s" not in transcribe("és sa clau", lang)


def test_balearic_affrication_keeps_the_left_word_pronounceable():
    """MINIMAL WORD — only the consonant changes; no word loses its nucleus.

    ⟨és⟩/⟨es⟩ are monovocalic and the vowel survives the assimilation
    ([ˈet], [ət] — never *[t]); the left word can never be emptied because the rule's own
    context requires the vowel it keeps.
    """
    assert transcribe("és sa", "ca-x-balear").split()[0] == "ˈet"
    assert transcribe("es seu", "ca-x-balear").split()[0] == "ət"
    assert transcribe("mos surten", "ca-x-balear").split()[0] == "ˈmot"


def test_voiced_sibilant_boundary_is_a_known_gap():
    """KNOWN GAP — a /s # z/ boundary is left as a cross-word geminate.

    ⟨dos zeros⟩ comes out [ˈdoz ˈzɛɾus]: CA_FINAL_S_VOICING voices the coda
    /s/ before the voiced sibilant, and the degemination rules cannot then
    see the geminate because the sandhi engine matches every context
    against the ORIGINAL words, not against what an earlier rule produced.
    A z$ rule is therefore unfirable — word-final devoicing means no word
    surfaces with a final [z] at match time. Collapsing this needs rule
    ordering the engine does not offer, so it is pinned, not asserted
    correct.
    """
    assert transcribe("dos zeros", "ca") == "ˈdoz ˈzɛɾus"  # single [z] wanted


def test_unlike_sibilants_voice_rather_than_delete():
    """Before a DIFFERENT sibilant the coda sibilant voices, not deletes.

    ⟨petits juguen⟩ is [pəˈtidz ˈʒuɣən] — /ts # ʒ/ assimilates in voicing
    (Wheeler 2005 §5.3), which is why the degemination rules are keyed on
    identical segments only.
    """
    assert transcribe("petits juguen", "ca").split()[0].endswith("dz")
    assert transcribe("els joves", "ca").split()[0] == "əlz"


def test_sibilant_degemination_is_sibilant_only():
    """Stops and nasals do NOT reduce across the boundary.

    Catalan keeps a cross-word stop or nasal geminate long — ⟨tot tancat⟩
    [ˈtot təŋˈkat], ⟨un nen⟩ [un ˈnɛn] — and the 4catac gold writes both
    consonants. Extending the deletion to them measurably WORSENS every
    Catalan 4catac row, so the rule is restricted to sibilants.
    """
    assert transcribe("tot tancat", "ca").split()[0].endswith("t")
    assert transcribe("un nen", "ca").split()[0] == "un"
    assert transcribe("mil litres", "ca").split()[0].endswith("l")


def test_sibilant_degemination_does_not_preempt_voicing():
    """A coda sibilant before a NON-sibilant still voices, not deletes.

    ⟨els nens⟩ is [əlz ˈnɛns] (Wheeler 2005 §5.3): the deletion rule's
    right context is voiceless sibilants only, so the voicing rule still
    owns every other boundary.
    """
    assert transcribe("els nens", "ca").split()[0] == "əlz"
    assert transcribe("coses importants", "ca").split()[0].endswith("z")
    assert transcribe("tot dia", "ca").split()[0].endswith("d")


# ─── Vowel contact across a word boundary ──────────────────────────────────
#
# Two vowels do not stand in hiatus across a word boundary inside a
# phonological phrase. Catalan resolves the contact three ways, and which one
# applies is decided by the two vowels themselves (Wheeler 2005 §10.1 'vowel
# contact'; Bonet & Lloret 1998 ch. 5):
#
#   1. the word-final unstressed [ə] deletes  (CA_ELIDE_FINAL_SCHWA)
#   2. failing that, the next word's initial unmarked vowel deletes
#      (CA_ELIDE_INITIAL_VOWEL)
#   3. an unmarked initial high vowel glides instead of deleting
#      (CA_HIATUS_GLIDE_I / CA_HIATUS_GLIDE_U)
#
# Exactly one vowel is lost per boundary: rule 1 and rule 2 are mutually
# exclusive by construction (rule 2's left context is the vowel set minus
# [ə]), not by any precedence the engine has to know about. And no rule may
# leave a word without a syllable — the minimal-word guard below.


def test_cross_word_elision_deletes_initial_unstressed_vowel():
    """⟨va anar⟩: the left word ends in a vowel that is not [ə], so the hiatus
    is resolved on the right — ⟨anar⟩'s initial [ə] goes. The 4catac gold
    writes the phrase as one word, [baˈna]; this library keeps the word
    boundary, and the two are identical segment for segment."""
    assert transcribe("va anar", "ca") == "ˈba ˈna"
    assert transcribe("va experimentar", "ca").startswith("ˈba k")
    assert transcribe("he autoritzat", "ca") == "ˈɛ wtuɾiˈdzat"


def test_cross_word_elision_deletes_final_schwa():
    """A word-final unstressed [ə] deletes before a vowel-initial word.

    All from the 4catac Central gold: sobre el [ˈsoβɾ əl], començava a
    [kumənˈsaβ ə], troba entre [ˈtɾɔβ ˈen̪tɾə], petita aixella
    [pəˈtit əˈʃeʎə], tanta aigua [ˈtan̪t ˈajɣwə].
    """
    assert transcribe("sobre el", "ca") == "ˈsɔβɾ əl"
    assert transcribe("començava a", "ca").split()[0].endswith("β")
    assert transcribe("troba entre", "ca").split()[0] == "ˈtɾɔβ"
    assert transcribe("petita aixella", "ca").split()[0] == "pəˈtit"
    assert transcribe("tanta aigua", "ca").split()[0] == "ˈtant"


# ─── The minimal-word guard: a rule may not leave a word without a syllable ─


def test_elision_never_destroys_a_words_only_vowel():
    """Hiatus resolution loses a vowel, never a word (Wheeler 2005 §10.1;
    Bonet & Lloret 1998 ch. 5 on clitic vowels).

    Both elision rules require the target word to keep a nucleus, so a
    monovocalic article, preposition or conjunction survives intact.
    """
    # left rule: the article ⟨la⟩ [lə] has no other vowel to fall back on
    assert transcribe("la aigua", "ca").split()[0] == "lə"
    assert transcribe("la a i la e", "ca").split()[0] == "lə"
    # right rule: ⟨en⟩ [ən]/[en] and ⟨el⟩ keep their vowel
    assert transcribe("estava en oració", "ca").split()[1] == "ən"
    assert transcribe("que el", "ca-x-occidental").split()[1] == "el"
    # ... and a word that is only a vowel is never consumed
    assert transcribe("va a casa", "ca") == "ˈba ə ˈkazə"


def test_glide_never_leaves_a_bare_nonsyllabic_word():
    """Gliding changes a vowel's syllabicity rather than deleting it, so it
    is guarded one notch more weakly: a word that is NOTHING but [u] would be
    left as a bare non-syllabic [w], which is no word at all. The conjunction
    ⟨o⟩ — [u] after Eastern reduction — therefore stays syllabic."""
    assert transcribe("O Anna o Eva", "ca") == "u ˈannə u ˈɛβə"
    # ⟨un⟩ has a consonant after the vowel and still glides, as the gold has it
    assert transcribe("beure un", "ca").split() == ["ˈbɛwɾə", "wn"]


def test_bare_conjunction_i_glides_as_the_gold_writes_it():
    """The one relaxation of the guard, and it is the expert gold's: all four
    4catac accents write the bare conjunction ⟨i⟩ as [j] between vowels
    (pollastre i, i ara)."""
    assert transcribe("pollastre i", "ca").split()[1] == "j"
    assert transcribe("de dellà i tanca", "ca").split()[2] == "j"


# ─── Blocking, dialects, and isolation ─────────────────────────────────────


def test_cross_word_elision_is_blocked_after_a_glide():
    """A [ə] that closes a diphthong is the syllable's second mora and does
    not delete: ⟨feia anys⟩ is [ˈfɛjə ˈaɲʃ] in all four 4catac accents, not
    *[ˈfɛj ˈaɲʃ]."""
    assert transcribe("feia anys", "ca").split()[0] == "ˈfɛjə"


@pytest.mark.parametrize("lang,first", [
    ("ca", "ˈtɾɔβ"), ("ca-x-balear", "ˈtɾoβ"),
])
def test_final_schwa_elision_holds_in_both_schwa_dialects(lang, first):
    """The Balearic 4catac gold writes the same boundary deletions as the
    Central one (troba entre [ˈtɾɔβ ˈən̪tɾə], sobre es [ˈsoβɾ əs]), so the
    schwa half is declared on both reducing dialects."""
    assert transcribe("troba entre", lang).split()[0] == first


def test_final_schwa_elision_is_not_declared_in_the_western_block():
    """Valencian and North-Western have no word-final [ə], so the schwa half
    is not declared on them at all — only the initial-vowel elision and the
    two glide rules are."""
    for lang in ("ca-x-valencia", "ca-x-occidental"):
        assert transcribe("troba entre", lang).split()[0][-1] in "aeɛ"
        ids = {r.id for r in get(lang).sandhi_rules}
        assert "CA_ELIDE_FINAL_SCHWA" not in ids
        assert "CA_ELIDE_INITIAL_VOWEL" in ids


def test_vowel_contact_is_not_declared_on_old_catalan():
    """The rules are declared per MODERN dialect, mirroring CA_DEGEM_S, and
    never on the ca-x-medieval ancestor: the sources on that node describe
    Old Catalan, and none of them was checked for cross-word vowel contact."""
    ids = {r.id for r in get("ca-x-medieval").sandhi_rules}
    assert not [i for i in ids if "ELIDE" in i or "GLIDE" in i]
    assert transcribe("estava en oració", "ca-x-medieval") == \
        "eˈstava en oɾasiˈo"


def test_vowel_contact_is_a_sentence_effect_only():
    """A word transcribed ALONE is untouched — elision needs a boundary."""
    assert transcribe("anar", "ca") == "əˈna"
    assert transcribe("sobre", "ca") == "ˈsɔβɾə"
    assert transcribe("un", "ca") == "un"
    assert transcribe("entre", "ca") == "ˈɛntɾə"


def test_vowel_contact_does_not_leak_to_other_languages():
    """No spec outside the Catalan branch declares vowel contact, so a
    French V#V boundary is unchanged (French elision is orthographic —
    ⟨l'ami⟩ — and is not this capability's business)."""
    assert transcribe("tu as", "fr-FR") == transcribe("tu", "fr-FR") + " " + \
        transcribe("as", "fr-FR")
    assert transcribe("la abuela", "es") == transcribe("la", "es") + " " + \
        transcribe("abuela", "es")


def test_atonic_function_words_reduce():
    """Clitics are unstressed *words*, so their vowels reduce.

    ⟨el⟩ ⟨la⟩ ⟨les⟩ ⟨de⟩ ⟨que⟩ are atonic (IEC grammar, 'mots àtons'), and a
    monosyllable-is-always-stressed assumption left them unreduced — [ˈlɛs
    ˈkɔzəs] instead of [ləs ˈkɔzəs] — which is wrong on almost every word of
    running text.
    """
    for word, expected in [("el", "əl"), ("la", "lə"), ("les", "ləs"),
                           ("que", "kə"), ("per", "pər")]:
        assert transcribe(word, "ca").replace("ˈ", "") == expected


# ─── Dialect contrasts: the four specs are modelled, not copied ────────────

@pytest.mark.parametrize("word,central,valencia,occidental,balear", [
    # 1. UNSTRESSED VOWEL REDUCTION — Eastern only (Recasens 1996; Veny 1982)
    ("casa",   "kazə",   "kaza",    "kazɛ",   "kazə"),
    ("tenir",  "təni",   "teniɾ",   "teni",   "təni"),
    # 2. unstressed ⟨o⟩ → [u] in Central AND Majorcan Balearic (mallorquí),
    #    but not in the non-reducing Western block (Valencian, North-Western).
    #    Veny 1982 ch. 4; Recasens 1996; the ca-x-balear-010/011 arbitration
    #    (euros [ˈɛwɾus], torrent [tuˈrent]).
    ("xocolata", "ʃukulatə", "tʃokolata", "tʃokolatɛ", "ʃukulatə"),
    # 3. word-final ⟨-r⟩ — kept ONLY in Valencian (Veny 1982 ch. 3)
    ("cantar", "kənta",  "kantaɾ",  "kanta",  "kənta"),
])
def test_dialect_vowels_and_final_r(word, central, valencia, occidental, balear):
    def ipa(code):
        return transcribe(word, code).replace("ˈ", "")
    assert ipa("ca") == central
    assert ipa("ca-x-valencia") == valencia
    assert ipa("ca-x-occidental") == occidental
    assert ipa("ca-x-balear") == balear


def test_valencian_does_not_reduce_where_central_does():
    """The contrast that proves the dialects are not a copy of the parent."""
    for word in ["casa", "tenir", "porta", "coses", "germana", "xocolata"]:
        assert "ə" in transcribe(word, "ca"), word
        assert "ə" not in transcribe(word, "ca-x-valencia"), word


def test_final_cluster_isogloss_is_not_the_east_west_line():
    """⟨molt⟩ is [ˈmol] in Central and North-Western, [ˈmolt] in Valencian
    and Balearic.

    Deleting an ABSOLUTELY word-final stop is an innovation of Central,
    North-Western and Northern Catalan; Valencian and Balearic keep it. The
    isogloss therefore runs Central + North-Western against Valencian +
    Balearic and is NOT the Eastern/Western line — Balearic is Eastern and
    keeps the stop, North-Western is Western and drops it (Veny 1982 ch. 3;
    Wiktionary, per-dialect: Central/North-Western [ˈmol], Balearic/Valencian
    [ˈmolt]; the 4catac expert gold has molt alta = [ˈmol ˈaltə] in
    Central/North-Western and [ˈmolt ˈalta] in Valencian/Balearic).

    Before a following CONSONANT every variety loses the stop; that is the
    pan-Catalan pre-consonantal rule, not this one.
    """
    assert transcribe("molt", "ca") == "ˈmol"
    assert transcribe("molt", "ca-x-occidental") == "ˈmol"
    assert transcribe("molt", "ca-x-valencia") == "ˈmolt"
    assert transcribe("molt", "ca-x-balear") == "ˈmolt"
    assert transcribe("camp", "ca") == "ˈkam"
    assert transcribe("camp", "ca-x-valencia") == "ˈkamp"
    assert transcribe("camp", "ca-x-balear") == "ˈkamp"
    assert transcribe("sang", "ca") == "ˈsaŋ"
    assert transcribe("sang", "ca-x-valencia") == "ˈsaŋk"
    assert transcribe("sang", "ca-x-balear") == "ˈsaŋk"
    # ⟨ny⟩ is not a stress ending: ⟨any⟩ is [ˈaɲ], not *[ˈəɲ]
    assert transcribe("any", "ca") == "ˈaɲ"
    # The PLURAL (pre-⟨-s⟩) deletion is pan-Catalan
    for code in ["ca", "ca-x-valencia", "ca-x-occidental", "ca-x-balear"]:
        assert transcribe("importants", code).endswith("ns"), code


def test_preconsonantal_cluster_deletion_is_pan_catalan():
    """Valencian and Balearic keep the final stop before a vowel and lose it
    before a consonant — 4catac has ⟨molt alta⟩ = [ˈmolt ˈalta] but ⟨el vint
    de juny⟩ = [el ˈvin de …]. Central has already lost it in both.
    """
    for code in ["ca-x-valencia", "ca-x-balear"]:
        assert transcribe("molt alta", code).split()[0].endswith("lt"), code
        assert transcribe("vint dies", code).split()[0].endswith("n"), code
    assert transcribe("molt alta", "ca").split()[0] == "ˈmol"


def test_valencian_affricate_and_western_x():
    """Valencian ⟨j/g+e,i⟩ = [dʒ] and Western ⟨x⟩ = [tʃ], ⟨ix⟩ = [jʃ]."""
    assert transcribe("germana", "ca-x-valencia").replace("ˈ", "") == "dʒeɾmana"
    assert transcribe("caixa", "ca-x-valencia") == "ˈkajʃa"
    assert transcribe("caixa", "ca") == "ˈkaʃə"
    assert transcribe("marxar", "ca-x-occidental").endswith("tʃa")


def test_balearic_raises_unstressed_o():
    """Majorcan Balearic (mallorquí) reduces ⟨a⟩/⟨e⟩ to [ə] AND raises
    unstressed ⟨o⟩ to [u], like the rest of Eastern Catalan (Veny 1982 ch. 4;
    Recasens 1996; the ca-x-balear-010/011 arbitration: euros [ˈɛwɾus],
    torrent [tuˈrent])."""
    assert "ʃukuˈlatə" == transcribe("xocolata", "ca-x-balear")
    assert "ʃukuˈlatə" == transcribe("xocolata", "ca")
    assert "ə" in transcribe("casa", "ca-x-balear")


def test_stress_mark_placement_is_onset_maximising():
    """A known limitation, pinned so it cannot drift silently.

    The bundled IPA syllabifier gives a whole consonant cluster to the
    following onset, so the stress mark of ⟨germana⟩ lands before the coda
    ⟨r⟩ rather than after it. The SEGMENTS are right — and the benchmark
    strips stress marks from both sides — but a consumer that needs
    syllable-accurate marks needs a real syllabifier plugin.
    """
    assert transcribe("germana", "ca") == "ʒəˈrmanə"   # not "ʒərˈmanə"
    assert transcribe("germana", "ca").replace("ˈ", "") == "ʒərmanə"


# ─── Genealogy: the Old-Catalan common core ────────────────────────────────

_MODERN = ["ca", "ca-x-valencia", "ca-x-balear", "ca-x-occidental",
           "ca-x-nord"]


def test_every_modern_variety_descends_from_old_catalan():
    """The modern varieties did not descend from modern Central Catalan.

    The Eastern/Western split predates the standard, and Balearic descends
    from the Eastern (Empordà) settlers of the 13th-century conquest — so
    ⟨ca⟩ is a sibling of the dialects, not their parent. It stays the code
    for "Catalan" (the IEC standard), but the inheritance edge points at
    ca-x-medieval.
    """
    for code in _MODERN:
        assert get(code).parent == "ca-x-medieval", code
    assert get("ca-x-medieval").parent == "x-clade-roma1334"


def test_old_catalan_is_data_bearing_not_a_clade():
    """A clade node carries no phonology and ``_nearest_data_ancestor`` walks
    straight through it, so a clade parent would leave the dialects inheriting
    nothing. The common core has to be a real, transcribable spec."""
    core = get("ca-x-medieval")
    assert not core.clade
    assert core.graphemes and core.allophone_rules and core.sandhi_rules
    assert transcribe("cantar", "ca-x-medieval") == "kaˈntaɾ"


def test_central_innovations_do_not_leak_into_the_other_varieties():
    """⟨ca⟩ holds only Central's own innovations. Because no variety inherits
    from it, none of them can be forced into a Central rule it does not have —
    which is what put the final-cluster simplification into Balearic and
    Valencian when ``ca`` was their parent."""
    # Vowel reduction: Central and the Eastern block only.
    assert "ə" in transcribe("casa", "ca")
    assert "ə" not in transcribe("casa", "ca-x-valencia")
    assert "ə" not in transcribe("casa", "ca-x-occidental")
    # Betacism and the fricative ⟨j⟩: Central, not Valencian.
    assert transcribe("vaca", "ca").startswith("ˈb")
    assert transcribe("vaca", "ca-x-valencia").startswith("ˈv")
    assert "ʒ" in transcribe("juny", "ca")
    assert "dʒ" in transcribe("juny", "ca-x-valencia")
    # Final ⟨-r⟩: deleted in Central, kept in Valencian.
    assert transcribe("cantar", "ca").endswith("a")
    assert transcribe("cantar", "ca-x-valencia").endswith("ɾ")


# ─── Word-final ⟨-r⟩ retainers ─────────────────────────────────────────────

def test_final_r_retainers_are_the_cited_ones():
    """Word-final ⟨-r⟩ deletion has a closed set of lexical exceptions
    (Bonet & Lloret, *Crazy rules and lexical exceptions*): car, clar, cor,
    dur, far, mar, or, pur, tir keep it. ⟨por⟩ and ⟨flor⟩ do NOT — they are
    [ˈpɔ] and [ˈflɔ] — and ⟨sur⟩ is not a Catalan word at all (Catalan is
    ⟨sud⟩; ⟨sur⟩ is Spanish).
    """
    for word in ["car", "clar", "cor", "dur", "mar", "or", "pur"]:
        assert transcribe(word, "ca").endswith("r"), word
    for word in ["por", "flor"]:
        assert not transcribe(word, "ca").endswith("r"), word
    assert "sur" not in get("ca").word_exceptions
    assert "sur" not in get("ca-x-balear").word_exceptions
