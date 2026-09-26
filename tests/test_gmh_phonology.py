"""Middle High German (gmh) phonology regressions.

Sourced against Paul, Hermann (rev. Klein, Solms & Wegera), *Mittelhochdeutsche
Grammatik* (25th ed., Niemeyer 2007) — the standard MHG reference grammar, and
against the shipped wikipron gold (``benchmarks``/``.benchmark_cache``
``gmh_latn_broad.tsv``), whose 1516 scored words were used to verify these
patterns hold at the token level, not just for the single example word below.
"""

from orthography2ipa import transcribe


def test_nebensilbenvokal_reduces_unstressed_final_e_to_schwa():
    """Unstressed inflectional ``-e``/``-en``/``-et`` surfaces as [ə].

    MHG root-initial stress leaves inflectional endings unstressed; the
    "Nebensilbenvokal" (Paul, *Mittelhochdeutsche Grammatik*, historical
    phonology of the unstressed syllables) reduces the written ⟨e⟩ of those
    endings to schwa, distinct from the full [ɛ] of a stressed root vowel.
    Before this rule the spec mapped every ⟨e⟩ to [ɛ] regardless of stress,
    which is wrong for the overwhelming majority of the gold's inflected
    forms (e.g. "bade" [ˈbadə], not *[ˈbadɛ]).
    """
    assert transcribe("bade", "gmh") == "ˈbadə"
    assert transcribe("baden", "gmh") == "ˈbadən"


def test_root_vowel_e_stays_full_when_stressed():
    """A stressed root ⟨e⟩ is not swept into the reduction rule.

    Regression guard for the reduction rule above being scoped to
    posttonic/unstressed nucleus positions only, not the flat grapheme
    table default.
    """
    assert transcribe("bette", "gmh") == "ˈbɛttə"


def test_grapheme_s_is_apical():
    """Orthographic ⟨s⟩ is the apical fricative [s̠], distinct from ⟨z⟩.

    Paul's *Mittelhochdeutsche Grammatik* describes MHG ⟨s⟩ and ⟨z⟩ as
    articulated at different places (apical vs. dorsal); the wikipron gold
    consistently transcribes plain orthographic ⟨s⟩ with the retracted
    diacritic (526 of 557 tokens containing ⟨s⟩ in the gold), which the
    unmarked ``s`` → [s] mapping never reached.
    """
    assert transcribe("as", "gmh") == "ˈas̠"


def test_z_digraphs_are_geminate():
    """⟨tz⟩ is a geminate affricate, ⟨zz⟩ a geminate fricative.

    MHG orthography marks the consonant-doubling that a short root vowel
    triggers; ⟨tz⟩ spells the geminate affricate [t͡sː] (e.g. "katze"),
    while ⟨zz⟩ spells the geminate dorsal fricative [sː] (e.g. "bizze"),
    the two outcomes of the High German Consonant Shift's *t depending on
    whether it patterns with the affricate or fricative reflex.
    """
    assert transcribe("katze", "gmh") == "ˈkat͡sːə"
    assert transcribe("bizze", "gmh") == "ˈbisːə"


def test_single_z_is_tied_affricate():
    """A bare ⟨z⟩ (post-resonant/initial reflex) is the tied affricate [t͡s].

    The tie bar is the linguistically correct IPA for an affricate and the
    spec should write it regardless of scoring. It does NOT move PER: the
    benchmark's normalizer strips tie bars (``_TIE_BARS`` at
    ``scripts/benchmark.py``) before comparison, so "t͡s" and "ts" score
    identically. The measured win from the z-grapheme change is entirely
    the ⟨tz⟩/⟨zz⟩ digraph split into distinct geminate mappings, not the
    tie bar.
    """
    assert transcribe("herze", "gmh") == "ˈhɛrt͡sə"


def test_wikt_variant_shares_phonology_with_lachmann_gmh():
    """`gmh-x-wikt` inherits phonology whole via `graphemes_base`.

    Regression guard against restating the phonology table for the
    Wiktionary title-form variant: the unstressed-e reduction, apical
    ⟨s⟩, and ⟨tz⟩/⟨zz⟩ gemination rules established on `gmh` above must
    hold identically here, since only the written convention (not the
    phonology) differs between the two specs.
    """
    assert transcribe("bade", "gmh-x-wikt") == "ˈbadə"
    assert transcribe("bette", "gmh-x-wikt") == "ˈbɛttə"
    assert transcribe("katze", "gmh-x-wikt") == "ˈkat͡sːə"
    assert transcribe("herze", "gmh-x-wikt") == "ˈhɛrt͡sə"


def test_wikt_variant_umlaut_vowels_survive_from_base():
    """⟨æ œ ä ö ü⟩ are kept: Wiktionary's own title policy treats them as
    separate letters, not as diacritics stripped from article titles
    (Wiktionary:About Middle High German), so they must still read exactly
    as they do under `gmh`.
    """
    assert transcribe("bræche", "gmh-x-wikt") == transcribe("bræche", "gmh")
    assert transcribe("bühse", "gmh-x-wikt") == transcribe("bühse", "gmh")


def test_wikt_variant_has_no_circumflex_length_graphemes():
    """The circumflex length graphemes (â î ô û) are nulled out.

    Wiktionary's title-slug convention never writes a circumflex — the
    style page reserves diacritic display for the ``head`` parameter only,
    not the page title WikiPron scrapes — so the plain vowel letter must
    read as short, and the circumflex spelling must not be a recognised
    grapheme of this variant at all.
    """
    from orthography2ipa.json_loader import load_json_spec

    lang = load_json_spec("gmh-x-wikt")
    for grapheme in ("â", "î", "ô", "û"):
        assert grapheme not in lang.graphemes, grapheme
    # the plain vowel default (short) survives unchanged from `gmh`
    assert transcribe("man", "gmh-x-wikt") == "ˈman"
