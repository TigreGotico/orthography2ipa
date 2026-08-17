"""Catalan beat-espeak wave: Majorcan vocalism, Majorcan total assimilation
and the pan-Catalan labiodental nasal.

Every rule pinned here was found by a per-word differential against espeak-ng
on the 4catac expert gold and then justified from the literature — espeak is
never the justification, only the pointer to the phenomenon:

* **Majorcan unstressed ⟨o⟩ = [o]** — mallorquí has a FOUR-vowel unstressed
  system [ə i o u]: /a e ɛ/ centralise to [ə] like the rest of the Eastern
  block, but /o ɔ/ reduce to [o] and stay distinct from /u/, as in the West
  (Wheeler 2005 §2.3; Veny 1982 ch. 4; Llompart & Simonet 2018). The spec
  previously inherited the Central raising to [u].
* **Majorcan stressed ⟨e⟩ defaults to [ə]** — the eighth vowel of the
  Balearic inventory continues Latin ē/ĭ, which is the majority source of a
  stressed unmarked ⟨e⟩; Latin ĕ (→ [ɛ], as in Central) is the minority, so
  [ə] is the candidate to prefer and [ɛ] the ranked alternative (Wheeler 2005
  §2.3; Veny 1982 ch. 4; Recasens 1996).
* **Majorcan total assimilation** — a word-final stop before a following
  consonant assimilates COMPLETELY to it, giving a geminate across the
  boundary (Wheeler 2005 §10.4; Veny 1982 ch. 4; Recasens 1996).
* **Labiodental nasal** — a nasal before /f v/ takes the LABIODENTAL place,
  [ɱ], not the bilabial [m] (Recasens 1993 §4; Wheeler 2005 §10.4; Bonet &
  Lloret 1998 §3). Pan-Catalan, so it lives on the Old-Catalan node.

Each test has an adversarial counter-case: a word or phrase in the same
neighbourhood where the rule must NOT fire.
"""
import pytest

from orthography2ipa import get, transcribe


# ── Majorcan unstressed ⟨o⟩ is [o], not [u] ───────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("xocolata", "ʃokoˈlatə"),
    ("política", "poˈlitikə"),
    ("podrà", "poˈðɾa"),
    ("torrent", "toˈrənt"),
    ("cossos", "ˈkosos"),
])
def test_majorcan_unstressed_o_is_not_raised(word, expected):
    """/o ɔ/ reduce to [o] in Majorcan (Wheeler 2005 §2.3; Veny 1982 ch. 4;
    Llompart & Simonet 2018) — the 4catac 'Balear' gold writes every one of
    these with [o]."""
    assert transcribe(word, "ca-x-balear") == expected


def test_majorcan_o_non_raising_does_not_touch_the_other_reductions():
    """COUNTER-CASE — only ⟨o⟩ changes.

    Majorcan still centralises unstressed /a e ɛ/ to [ə]; a spec that "stopped
    reducing" altogether would be Western, not Majorcan.
    """
    assert transcribe("casa", "ca-x-balear") == "ˈkazə"
    assert transcribe("tenir", "ca-x-balear") == "təˈni"


@pytest.mark.parametrize("lang,expected", [
    ("ca", "ʃukuˈlatə"),
    ("ca-x-nord", "ʃukuˈlatə"),
    ("ca-x-valencia", "tʃokoˈlata"),
    ("ca-x-occidental", "tʃokoˈlatɛ"),
])
def test_majorcan_o_non_raising_does_not_leak_to_other_varieties(lang, expected):
    """COUNTER-CASE — the change is declared on ca-x-balear, never on the
    shared Old-Catalan ancestor: Central and Northern keep the Eastern
    raising to [u], and the Western block keeps its own non-reducing [o]."""
    assert transcribe("xocolata", lang) == expected


# ── Majorcan stressed ⟨e⟩ prefers [ə] ─────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("tres", "ˈtɾəs"),
    ("aquell", "əˈkəʎ"),
    ("feina", "ˈfəjnə"),
    ("sentis", "ˈsəntis"),
    ("beix", "ˈbəʃ"),
])
def test_majorcan_stressed_e_defaults_to_schwa(word, expected):
    """The Majorcan eighth vowel is the DEFAULT reading of a stressed
    unmarked ⟨e⟩, not a lexical exception list (Wheeler 2005 §2.3)."""
    assert transcribe(word, "ca-x-balear") == expected


def test_majorcan_stressed_schwa_is_a_ranking_not_a_blanket_rewrite():
    """COUNTER-CASE — [ɛ] is still reachable, and the written accents win.

    ⟨è⟩ marks an open ⟨e⟩ and must not be schwa'd, and an unstressed ⟨e⟩ still
    reduces by the ordinary Eastern rule rather than by this ranking.
    """
    assert "ɛ" in transcribe("convèncer", "ca-x-balear")
    assert transcribe("tenir", "ca-x-balear").startswith("tə")
    assert "ə" in get("ca-x-balear").positional_graphemes["e"]["default"]
    assert "ɛ" in get("ca-x-balear").positional_graphemes["e"]["default"]


@pytest.mark.parametrize("lang", ["ca", "ca-x-nord", "ca-x-valencia",
                                  "ca-x-occidental", "ca-x-medieval"])
def test_stressed_schwa_does_not_leak_to_other_varieties(lang):
    """COUNTER-CASE — stressed [ə] is Balearic only; no other Catalan variety
    has it as a stressed vowel (Wheeler 2005 §2.3)."""
    assert "ə" not in transcribe("tres", lang)


# ── Majorcan total assimilation of a coda stop across a word boundary ─────

@pytest.mark.parametrize("phrase,expected", [
    ("cap sol", "ˈkas ˈsol"),
    ("cap taula", "ˈkat ˈtawlə"),
    ("cap fill", "ˈkaf ˈfiʎ"),
    ("recorregut feia", "rəkorəˈɣuf ˈfəjə"),
])
def test_majorcan_coda_stop_assimilates_totally(phrase, expected):
    """A word-final stop becomes a copy of the following consonant, so the
    boundary surfaces as a geminate (Wheeler 2005 §10.4; Veny 1982 ch. 4)."""
    assert transcribe(phrase, "ca-x-balear") == expected


def test_total_assimilation_yields_to_prevocalic_sonorant_voicing():
    """SCOPE — a competing pan-Catalan rule wins before a voiced sonorant.

    Catalan voices a word-final obstruent before a following sonorant, and
    that rule resolves ⟨cap moix⟩ as [ˈkab …] in every variety. Majorcan
    total assimilation is therefore observed here only before a VOICELESS
    onset; the gap is real and is named, not papered over.
    """
    assert transcribe("cap moix", "ca-x-balear").split()[0] == "ˈkab"
    assert transcribe("cap moix", "ca").split()[0] == "ˈkab"
    # Because the voicing rule always wins there, only the VOICELESS targets
    # are declared: a rule for /b d ɡ v z m n l ʎ ɲ ʒ/ could never fire, so
    # none is shipped. Pinned so nobody "completes the set" with dead rules.
    ids = {r.id for r in get("ca-x-balear").sandhi_rules
           if r.id.startswith("BALEAR_TOTAL_ASSIM_")}
    assert ids == {"BALEAR_TOTAL_ASSIM_P", "BALEAR_TOTAL_ASSIM_T",
                   "BALEAR_TOTAL_ASSIM_K", "BALEAR_TOTAL_ASSIM_F",
                   "BALEAR_TOTAL_ASSIM_S", "BALEAR_TOTAL_ASSIM_SH"}


def test_total_assimilation_needs_a_following_consonant():
    """COUNTER-CASE — before a VOWEL the stop keeps its own place, and a
    coda that is not a plain final stop is not a target either."""
    assert transcribe("cap amic", "ca-x-balear").split()[0] == "ˈkap"
    # ⟨-ps⟩: the word-final segment is the sibilant, not the stop
    assert transcribe("saps com", "ca-x-balear").split()[0] == "ˈsaps"


@pytest.mark.parametrize("lang", ["ca", "ca-x-nord", "ca-x-valencia",
                                  "ca-x-occidental", "ca-x-medieval"])
def test_total_assimilation_does_not_leak_to_other_catalan(lang):
    """COUNTER-CASE — declared on ca-x-balear only, never on an ancestor:
    Central and the Western dialects keep the coda stop distinct."""
    ids = {r.id for r in get(lang).sandhi_rules}
    assert not {i for i in ids if "TOTAL_ASSIM" in i}
    assert transcribe("cap sol", lang).split()[0].endswith("p")


# ── Pan-Catalan labiodental nasal ─────────────────────────────────────────

@pytest.mark.parametrize("lang", ["ca", "ca-x-balear", "ca-x-valencia",
                                  "ca-x-occidental", "ca-x-nord",
                                  "ca-x-medieval"])
@pytest.mark.parametrize("word", ["enfadar", "confortable", "àmfora"])
def test_nasal_is_labiodental_before_f(lang, word):
    """A nasal assimilates to the LABIODENTAL place before /f/, giving [ɱ]
    (Recasens 1993 §4; Wheeler 2005 §10.4; Bonet & Lloret 1998 §3). Declared
    on the Old-Catalan node, so every variety inherits it."""
    out = transcribe(word, lang)
    assert "ɱ" in out
    assert "mf" not in out


def test_nasal_is_labiodental_before_v_where_v_survives():
    """⟨convèncer⟩ keeps /v/ in the varieties that have it, and the nasal is
    [ɱ] there. Central and North-Western have betacism (/v/ → [b]), so the
    nasal correctly sees a BILABIAL and stays [m] — the same rule, applied to
    a different surface consonant."""
    # the cluster straddles the syllable boundary the stress mark is written
    # at, so the mark is stripped before looking for it
    assert "ɱv" in transcribe("convèncer", "ca-x-balear").replace("ˈ", "")
    assert "ɱv" in transcribe("convèncer", "ca-x-valencia").replace("ˈ", "")
    assert "mb" in transcribe("convèncer", "ca").replace("ˈ", "")


@pytest.mark.parametrize("phrase,expected_first", [
    ("un pare", "um"),
    ("en bici", "əm"),
])
def test_nasal_stays_bilabial_before_a_bilabial(phrase, expected_first):
    """COUNTER-CASE — the labiodental rule must not swallow the bilabial one.

    Before /p b m/ the nasal is [m], not [ɱ]; only /f v/ trigger [ɱ].
    """
    out = transcribe(phrase, "ca")
    assert out.split()[0] == expected_first
    assert "ɱ" not in out


def test_labiodental_rule_is_declared_once_on_the_ancestor():
    """The rule lives on ca-x-medieval and is inherited, not copy-pasted into
    each dialect spec — the phenomenon is pan-Catalan."""
    import json
    import os
    data = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "orthography2ipa", "data")
    owners = []
    for code in ["ca", "ca-x-balear", "ca-x-valencia", "ca-x-occidental",
                 "ca-x-nord", "ca-x-medieval"]:
        with open(os.path.join(data, code + ".json"), encoding="utf-8") as fh:
            spec = json.load(fh)
        if any(r["id"] == "CA_NASAL_LABIODENTAL"
               for r in spec.get("allophone_rules", [])):
            owners.append(code)
    assert owners == ["ca-x-medieval"]
