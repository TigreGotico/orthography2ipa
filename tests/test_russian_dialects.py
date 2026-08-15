"""Cited-rule conformance for the ten Russian dialect specs.

Every ``ru-x-*`` spec used to be a note that claimed a dialect feature and a
table that did not implement it. The three worst cases, all pinned below:

* ``ru-x-northern`` announced ОКАНЬЕ and inherited the standard's akanje
  reduction table, so голова came out [ɡɐˈɫovə] — an akanje form, in the
  file whose whole reason to exist is that the north does not akaje.
* ``ru-x-southern`` carried a standalone 33-grapheme table with no
  ``graphemes_base``, so it inherited neither stress placement nor any
  positional reading: вода was [voda], город was [ɣorod] — no reduction, no
  final devoicing, no stress mark — under a note claiming "strong аканье and
  яканье".
* every dialect emitted его as [ˈjeɡə] or [jeɣo], a spelling pronunciation
  that no Russian variety has, because ``grammatical_endings`` is BASE_MERGE
  and none of the children had opted in.

Sources. The zone-level facts (окание/аканье, the [ɣ] isogloss, цоканье,
the jakanje subtypes) are the classification criteria of the Dialectological
Atlas tradition; the claim set is standard — e.g. Avanesov 1949, Zakharova &
Orlova 1970, Kasatkin 2005 — and no edition of any of those was consulted
here, so no page locators are given anywhere in this file or in the specs.
What WAS consulted, and what the Russian wording quoted in the specs' notes
comes from, are the Russian-language dialectological descriptions of the
individual groups (северное/южное наречие, псковская, вологодская,
курско-орловская, донская группы, поморские и сибирские старожильческие
говоры). The [v] genitive is Timberlake 2004 and Jones & Ward 1969, as in
``ru``; the SOUTHERN [ɣ] genitive is the один place where the Southern zone
departs from it, and it is listed among that zone's morphological — not
phonetic — diagnostics.

No gold set is consulted by any test here, and no ru-x-* lect has a row on
the benchmark board.
"""
import json
import pathlib

import pytest

import orthography2ipa
from orthography2ipa.g2p import G2P

_DATA = pathlib.Path(orthography2ipa.__file__).parent / "data"


def _raw(code):
    """The spec's JSON as authored — inheritance not yet resolved."""
    return json.loads((_DATA / f"{code}.json").read_text(encoding="utf-8"))

DIALECTS = [
    "ru-x-moscow", "ru-x-northern", "ru-x-vologda", "ru-x-arkhangelsk",
    "ru-x-pskov", "ru-x-siberian", "ru-x-ural", "ru-x-southern",
    "ru-x-don", "ru-x-kursk-orel",
]

#: A probe list that exercises every feature under test at once.
PROBE = ["его", "кого", "чего", "этого", "нового", "много", "город", "снег",
         "голова", "вода", "часто", "цена", "лицо", "деревня", "тяжело"]


def t(code, word):
    return G2P(code).transcribe_word(word)


def bare(code, word):
    return t(code, word).replace("ˈ", "").replace("ˌ", "")


# ===========================================================================
# The genitive desinence reaches every dialect
# ===========================================================================

@pytest.mark.parametrize("code", DIALECTS)
def test_no_dialect_spells_out_the_genitive_g(code):
    """его is never [jeɡo]/[ˈjeɡə] anywhere.

    ⟨-ого/-его⟩ is a desinence, not a ⟨г⟩: no Russian variety reads the
    letter here (Timberlake 2004). This is the regression the whole family
    shared — ``grammatical_endings`` is BASE_MERGE, so a child that does not
    declare ``grammatical_endings_base`` (or its own table) silently falls
    back to the grapheme table and spells the letter out."""
    out = bare(code, "его")
    assert "ɡ" not in out, out
    assert out.endswith("vo") or out.endswith("ɣo"), out


@pytest.mark.parametrize("code", DIALECTS)
def test_ogo_desinence_reaches_every_dialect(code):
    """-ого on a real adjective is a desinence in every lect too, so the
    fix is the ending table and not 25 hard-coded words."""
    assert "ɡ" not in bare(code, "нового"), bare(code, "нового")


# ===========================================================================
# The [v]/[ɣ] split — morphological, and it follows the zone
# ===========================================================================

@pytest.mark.parametrize("code", [
    "ru-x-moscow", "ru-x-northern", "ru-x-vologda", "ru-x-arkhangelsk",
    "ru-x-pskov", "ru-x-siberian", "ru-x-ural",
])
def test_non_southern_zones_keep_the_v_genitive(code):
    """The [v] desinence is a morphological fact of Russian and does not
    care about the окание/аканье isogloss, so it is identical in the
    okanje North and the akanje Centre (Timberlake 2004)."""
    assert bare(code, "его").endswith("vo")
    assert "ɣ" not in bare(code, "его")


@pytest.mark.parametrize("code", ["ru-x-southern", "ru-x-don",
                                  "ru-x-kursk-orel"])
def test_southern_zone_has_the_fricative_genitive(code):
    """The Southern zone is the exception, and it is not a phonetic one:
    the ending ⟨-его/-ого⟩ is pronounced через фрикативное /ɣ/, а не через
    /в/, and the Atlas tradition lists it among южное наречие's
    MORPHOLOGICAL diagnostics. So [ɣ] here is a different desinence, not
    the Southern realisation of [v] — which is why ⟨в⟩ itself stays [v] in
    the same words."""
    assert bare(code, "его").endswith("ɣo"), bare(code, "его")
    assert "v" not in bare(code, "его")
    # ⟨в⟩ is untouched: only the desinence changed.
    assert bare(code, "вода").startswith("v")


@pytest.mark.parametrize("code", ["ru-x-southern", "ru-x-don",
                                  "ru-x-kursk-orel"])
def test_southern_fricative_genitive_does_not_eat_a_stem_v(code):
    """[ɣ] replaces the DESINENTIAL ⟨г⟩ and nothing else.

    ⟨-вьего⟩ is the soft-sign genitive after a stem-final ⟨в⟩, so it holds
    both letters at once — соловьего is [-vʲjɪɣə], with the stem's [vʲ]
    intact. Deriving the southern ending table by rewriting every [v] in
    the standard's table swept the stem consonant up with the desinence and
    produced [ɣʲjɪɣə], putting a segment ([ɣʲ]) into the output that is not
    in this spec's inventory at all. It is the one entry of the 21 where a
    [v] is not the ⟨г⟩."""
    out = bare(code, "соловьего")
    assert out.endswith("vʲjɪɣə"), out
    assert "ɣʲ" not in out, out
    assert out.count("ɣ") == 1, out


def test_southern_genitive_is_not_reachable_by_the_g_grapheme():
    """A ⟨г⟩ = [ɣ] table alone would ALSO produce [jeɣo] — the pre-fix
    output. The test that separates a desinence from a spelling
    pronunciation is the VOWELS: the desinence carries jakanje [a], the
    spelling pronunciation carries the unreduced [e] of the letter ⟨е⟩."""
    assert bare("ru-x-southern", "его") == "jaɣo"


# ===========================================================================
# Northern: оканье, еканье, soft цоканье
# ===========================================================================

@pytest.mark.parametrize("code", ["ru-x-northern", "ru-x-vologda",
                                  "ru-x-arkhangelsk", "ru-x-siberian"])
@pytest.mark.parametrize("word", ["голова", "вода", "город", "много"])
def test_okanje_keeps_unstressed_o(code, word):
    """Полное оканье: unstressed non-high vowels stay distinct after hard
    consonants, so the standard's [ɐ]/[ə] reflexes of ⟨о⟩ never appear.
    Before the fix these specs inherited ``ru``'s positional table wholesale
    and reduced exactly like Moscow."""
    out = bare(code, word)
    assert "ɐ" not in out, out
    assert "ə" not in out, out
    assert "o" in out, out


def test_okanje_reaches_the_genitive_vowels_too():
    """The [v] desinence and the okanje vowels are independent facts and
    both have to land: -ого is [-ovo] in the north, not [-əvə]."""
    assert bare("ru-x-northern", "нового") == "novovo"
    assert bare("ru-x-northern", "его") == "jevo"


def test_northern_ekanje_after_soft_consonants():
    """The counterpart of окание after SOFT consonants: unstressed ⟨е⟩ is
    [(j)e] and ⟨я⟩ is [ja], not the standard's [ɪ]."""
    assert "ɪ" not in bare("ru-x-northern", "деревня")
    assert bare("ru-x-northern", "деревня") == "dʲerʲevnʲa"


@pytest.mark.parametrize("code", ["ru-x-northern", "ru-x-vologda",
                                  "ru-x-arkhangelsk"])
def test_soft_tsokanje_merges_c_and_ch_in_one_soft_affricate(code):
    """Цоканье in the Northern zone is the SOFT type — one affricate
    [tsʲ] — not the hard [ts] this family emitted before. ⟨ч⟩ and ⟨ц⟩ must
    come out as the SAME segment, and it must be one segment: the earlier
    attempt produced [tʲsʲ], i.e. [t] + [sʲ], because nothing declared
    [tsʲ] as a segmentation atom."""
    assert bare(code, "часто").startswith("tsʲa"), bare(code, "часто")
    assert bare(code, "лицо").endswith("tsʲo"), bare(code, "лицо")
    for word in ("часто", "лицо", "цена", "конец"):
        assert "tɕ" not in bare(code, word), (word, bare(code, word))
        assert "tʲsʲ" not in bare(code, word), (word, bare(code, word))


def test_soft_tsokanje_does_not_back_a_following_e():
    """⟨це⟩ = [tsɨ] is a rule about the UNPAIRED HARD /ts/. A dialect whose
    affricate is soft has no unpaired hard /ts/ left, so the backing must
    not fire — and the iotation must still be absorbed."""
    assert bare("ru-x-northern", "цена") == "tsʲena"


def test_northern_stays_on_the_plosive_side_of_the_g_isogloss():
    """[ɣ] is Southern. The northern zone has plosive /г/ alternating with
    [k] word-finally, so снег is [-k] here and [-x] in the south."""
    assert bare("ru-x-northern", "город").startswith("ɡ")
    assert bare("ru-x-northern", "снег").endswith("k")


# ===========================================================================
# Siberian: Northern-based okanje, but NO цоканье and plosive [ɡ]
# ===========================================================================

def test_siberian_okajet_but_distinguishes_the_affricates():
    """Сибирские старожильческие говоры developed на основе севернорусского
    наречия, so they okajut; but unlike the Northern zone proper they
    DISTINGUISH /ч/ and /ц/, so no цоканье is encoded. The old note claimed
    'partial аканье', which is the wrong zone entirely."""
    assert bare("ru-x-siberian", "вода") == "voda"
    assert bare("ru-x-siberian", "часто").startswith("tɕa")
    assert bare("ru-x-siberian", "лицо").endswith("tso")


def test_siberian_g_is_plosive():
    assert bare("ru-x-siberian", "город").startswith("ɡ")


# ===========================================================================
# Southern: fricative /ɣ/~/x/, akanje that actually reduces, jakanje
# ===========================================================================

@pytest.mark.parametrize("code", ["ru-x-southern", "ru-x-don",
                                  "ru-x-kursk-orel"])
def test_southern_g_is_fricative_and_devoices_to_x(code):
    """The Southern obstruent pair is /ɣ/~/x/, not /ɡ/~/k/, so word-final
    ⟨г⟩ is [x]. Before the fix the southern specs had no positional table
    at all and left final obstruents voiced: город was [ɣorod]."""
    assert bare(code, "город").startswith("ɣ")
    assert bare(code, "снег").endswith("x"), bare(code, "снег")
    assert bare(code, "снег")[-1] != "k"


@pytest.mark.parametrize("code", ["ru-x-southern", "ru-x-don",
                                  "ru-x-kursk-orel"])
def test_southern_final_devoicing_is_alive_at_all(code):
    """The southern family inherited no ``positional_graphemes`` and so had
    no final devoicing of any kind — not just for ⟨г⟩."""
    assert bare(code, "город").endswith("t"), bare(code, "город")


@pytest.mark.parametrize("code", ["ru-x-southern", "ru-x-don",
                                  "ru-x-kursk-orel"])
def test_southern_output_carries_a_stress_mark(code):
    """No ``graphemes_base`` meant no inherited ``StressRules``, so every
    southern transcription came out unstressed — and unstressed output
    means no reduction context can ever be computed."""
    assert "ˈ" in t(code, "голова"), t(code, "голова")


def test_southern_akanje_is_a_full_a_not_the_standard_schwa():
    """In the eastern (Ryazan-anchored) part of the zone the pretonic
    merger is NON-dissimilative, with a full [a]: вада, трава — where the
    standard has [ɐ]."""
    assert bare("ru-x-southern", "голова") == "ɣaɫovə"
    assert "ɐ" not in bare("ru-x-southern", "голова")


def test_southern_jakanje_lowers_the_first_pretonic_after_soft_consonants():
    """Яканье: /e o a/ after a soft consonant go to [a] in the first
    pretonic syllable, where the standard has [ɪ]."""
    assert bare("ru-x-southern", "деревня") == "dʲarʲevnʲə"
    assert bare("ru", "деревня") == "dʲɪrʲevnʲə"


# ===========================================================================
# The jakanje SUBTYPES are what separate the three southern files
# ===========================================================================

def _first_pretonic(code, grapheme):
    pos = G2P(code).spec.positional_graphemes[grapheme]
    return pos["first_pretonic"]


def test_kursk_orel_is_the_dissimilative_zone_not_the_strong_one():
    """The group's diagnostic is DISSIMILATIVE аканье and яканье (the
    Zhizdra/Sudzha type): травинкой — травой — тръва, пятóк — питáк. The
    spec used to claim 'strong яканье', which is the Pskov–Tver system and
    puts the file in the wrong half of the Southern zone.

    Dissimilation looks RIGHTWARD at the stressed vowel's height, which a
    positional grapheme table cannot see, so both outcomes are declared as
    ranked alternatives. The test pins that the alternation EXISTS — a
    single value would be a claim the sources do not support."""
    assert _first_pretonic("ru-x-kursk-orel", "а") == ["a", "ə"]
    assert _first_pretonic("ru-x-kursk-orel", "о") == ["a", "ə"]
    assert len(_first_pretonic("ru-x-kursk-orel", "я")) == 2


def test_don_ranks_the_dissimilative_alternants_the_other_way_round():
    """Донской тип диссимилятивного яканья: [a] only before a HIGH stressed
    vowel and [i] before every other one — the mirror image of the
    Kursk–Orel distribution. Both files rank the same pair of outcomes;
    the ORDER is the dialect claim, and it must not be the same order."""
    don = _first_pretonic("ru-x-don", "я")
    kursk = _first_pretonic("ru-x-kursk-orel", "я")
    assert don[0] == "jɪ" and don[1] == "ja"
    assert kursk[0] == "ja" and kursk[1] == "jɪ"
    assert don != kursk


def test_pskov_strong_jakanje_needs_no_lookahead():
    """Сильное яканье is [a] in the first pretonic syllable after a soft
    consonant НЕЗАВИСИМО ОТ ГЛАСНОГО, НАХОДЯЩЕГОСЯ ПОД УДАРЕНИЕМ. Being
    independent of the stressed vowel is the whole point: unlike the
    dissimilative types it needs no rightward lookahead, so it encodes
    exactly — as a SINGLE value, not a ranked pair."""
    assert _first_pretonic("ru-x-pskov", "я") == ["ja"]
    assert bare("ru-x-pskov", "деревня") == "dʲarʲevnʲə"
    assert bare("ru-x-pskov", "тяжело") == "tʲaʐɨɫə"


def test_pskov_akajet_and_stays_north_of_the_g_isogloss():
    """The Pskov group is западные среднерусские АКАЮЩИЕ говоры, not the
    'mixed North-Central' variety the old note described without committing
    to a vowel system: it reduces after hard consonants exactly like the
    standard, and its /г/ is the plosive."""
    assert bare("ru-x-pskov", "голова") == "ɡɐɫovə"
    assert bare("ru-x-pskov", "город").startswith("ɡ")


def test_pskov_tsokanje_is_the_hard_partial_type():
    """Pskov цоканье merges the affricates in [ц] — the hard type — and the
    merger is partial across the group, so ⟨ч⟩ is ranked [ts] over [tɕ]
    rather than given either value alone."""
    assert G2P("ru-x-pskov").spec.graphemes["ч"] == ["ts", "tɕ"]


# ===========================================================================
# The aliases are honest aliases, and say so
# ===========================================================================

@pytest.mark.parametrize("code", ["ru-x-moscow", "ru-x-ural"])
@pytest.mark.parametrize("word", PROBE)
def test_standard_aliases_match_ru_exactly(code, word):
    """These two claim no phonology of their own. ``ru-x-moscow`` is the
    regional variety the standard was codified FROM (the старомосковская
    layer that would make it more than an alias is deliberately unencoded,
    for want of a source); ``ru-x-ural`` is a говоры позднего формирования
    zone with no single vowel system to encode. An honest alias is a
    legitimate spec state — an invented inventory is not — but an alias
    must be BYTE-identical to its base, which before the genitive opt-in it
    was not."""
    assert t(code, word) == t("ru", word)


@pytest.mark.parametrize("code", ["ru-x-vologda", "ru-x-arkhangelsk"])
@pytest.mark.parametrize("word", PROBE)
def test_northern_subtypes_match_their_parent_exactly(code, word):
    """Vologda and Arkhangelsk (Pomor) both have полное оканье and soft
    цоканье, which IS the Northern-group system, so they add no tables and
    must track ``ru-x-northern`` exactly — including its genitive, which
    they only inherit because they declare ``grammatical_endings_base``."""
    assert t(code, word) == t("ru-x-northern", word)


# ===========================================================================
# ru is the standard; ru-x-moscow is the region. Neither is the other.
# ===========================================================================

def test_ru_does_not_describe_itself_as_a_regional_variety():
    """``ru`` opened with "Standard Moscow Russian", which made it both the
    codified norm AND a named region — leaving ``ru-x-moscow`` with no role
    and no way to say what it adds. The base is the STANDARD; the regional
    Moscow layer is the child. Each note now names the other."""
    ru_notes = G2P("ru").spec.notes
    assert "Standard Moscow Russian" not in ru_notes
    assert "Codified standard literary Russian" in ru_notes
    assert "ru-x-moscow" in ru_notes
    assert "ru-x-moscow" not in G2P("ru").spec.notes.split(
        "Codified standard")[0]


def test_moscow_note_states_what_it_would_add_and_that_it_does_not_yet():
    """An alias that does not say it is an alias reads as a finished
    dialect spec. This one names the старомосковская items it would carry
    and records that no source for them was consulted."""
    notes = G2P("ru-x-moscow").spec.notes
    assert "NOT the standard itself" in notes
    assert "NEEDS SOURCING" in notes


# ===========================================================================
# Every dialect is actually a dialect of something
# ===========================================================================

@pytest.mark.parametrize("code", DIALECTS)
def test_every_dialect_pulls_its_tables_from_a_base(code):
    """``ru-x-southern`` used to carry a standalone 33-grapheme table with
    no ``graphemes_base``, which is how it lost stress placement and every
    positional reading in one move — the loader hangs stress, positional
    readings and the ``*_base`` overlays off that one edge. A dialect spec
    states DELTAS against its base, never a whole table."""
    raw = _raw(code)
    assert raw.get("graphemes_base"), code
    assert len(raw.get("graphemes") or {}) < 10, (
        f"{code}: a dialect spec should state its divergences, not restate "
        f"the whole table")
    assert G2P(code).spec.stress is not None, code


@pytest.mark.parametrize("code", DIALECTS)
def test_declared_vowel_system_is_the_one_that_reaches_the_output(code):
    """The class of defect this whole file exists for, checked
    mechanically and without reading prose: whatever reading a spec
    DECLARES for an unstressed slot is what must actually surface there.

    голова́ is stressed on the last syllable, so its ⟨о⟩s are the SECOND
    and FIRST pretonic. This probe does not depend on that: ``ru``'s stress
    is a lexical property the spec declares it cannot place (see its STRESS
    note), and its predictor puts the accent on ло here, which makes the
    first ⟨о⟩ the first-pretonic slot as far as the engine is concerned.
    The assertion is about the ENGINE's own slot assignment — whichever
    unstressed slot its stress guess produces must be filled from that
    slot's declared readings — not about where the accent really falls.
    The mis-stressing is a separate, pre-existing defect; it changes which
    slot is probed and never which readings the slot may take.

    Every pre-revision failure was exactly this declared/emitted mismatch,
    and every one of them arrived through inheritance rather than through
    the table: the northern specs declared okanje in prose and resolved to
    ``ru``'s akanje table, and the southern specs resolved to no positional
    table at all. Same check for ⟨г⟩ and the first segment."""
    spec = G2P(code).spec
    out = bare(code, "голова")
    assert out[1] in spec.positional_graphemes["о"]["first_pretonic"], (
        code, out, spec.positional_graphemes["о"]["first_pretonic"])
    assert out[0] in spec.graphemes["г"], (code, out, spec.graphemes["г"])
