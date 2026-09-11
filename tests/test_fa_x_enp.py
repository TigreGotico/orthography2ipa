"""Early New Persian (fa-x-enp) reading of the Perso-Arabic script.

fas_arab_broad.tsv (the wikipron gold scored against ``fa``) is
predominantly an Early New Persian (ENP) transcription, not Contemporary
Iranian Persian: gold ``aː`` where the modern spec has ``ɒː``, plain ``r``
where the modern spec has the tap ``ɾ``, ``q`` kept distinct from ``ɣ``
where the modern spec merges them, and a labialised ``xʷ`` for ⟨خو⟩ where
the modern spec has a silent wāw. See data/fa.json's ``audit.wikipron``
entry and data/fa-x-enp.json's ``notes`` for the cited sources (Paul,
"PERSIAN LANGUAGE i. Early New Persian", Encyclopaedia Iranica; Miller
2012, "Variation in Persian Vowel Systems").

Per issue #1426, an unregistered ``-x-`` subtag silently falls back to its
base spec, so a ``transcribe(word, "fa-x-enp")`` check alone would not
prove the spec is actually wired up. These tests pin the spec via
``load_json_spec`` directly, as the other ``-x-`` variant tests do (see
tests/test_gmh_phonology.py), so a regression that de-registers or
mis-parents the file fails loudly here instead of silently degrading to
plain ``fa``.
"""
from orthography2ipa.json_loader import load_json_spec


def test_fa_x_enp_is_registered_and_parented_on_fa():
    spec = load_json_spec("fa-x-enp")
    assert spec.code == "fa-x-enp"
    assert spec.parent == "fa"


def test_long_a_stays_front_not_backed():
    """Bare alef reads aː, not the Tehran-backed ɒː (Paul, Iranica: the
    modern-only backed 'ā (=[å])' is contrasted with the ENP figure in
    Miller 2012: 157, 'ā ē ī ō ū a (e) i (o) u')."""
    spec = load_json_spec("fa-x-enp")
    assert spec.graphemes["ا"] == ["ʔ", "aː"]
    assert spec.graphemes["آ"] == ["ʔaː"]
    assert spec.positional_graphemes["ا"]["default"] == ["aː"]
    assert spec.positional_graphemes["ا"]["word_initial"] == ["ʔ"]


def test_qaf_stays_distinct_from_ghayn():
    """⟨ق⟩ reads q, not merged with ⟨غ⟩'s ɣ (Paul, Iranica: 'The ENP
    distinct phonemes ġ and q turn into positional allophones ... in
    modern spoken NP, especially in ... Tehran')."""
    spec = load_json_spec("fa-x-enp")
    assert spec.graphemes["ق"] == ["q"]


def test_rhotic_is_plain_r():
    """⟨ر⟩ reads plain r, not the Tehran tap ɾ."""
    spec = load_json_spec("fa-x-enp")
    assert spec.graphemes["ر"] == ["r"]


def test_waw_reads_labial_glide_not_labiodental():
    """⟨و⟩'s consonantal reading is w, not the Tehran v (Paul, Iranica:
    'The pronunciation of wāw shifted from a bilabial glide [w] to a
    labiodental fricative [v] ... (Pisowicz, p. 120)' — ENP is pre-shift)."""
    spec = load_json_spec("fa-x-enp")
    assert spec.graphemes["و"][0] == "w"
    assert spec.positional_graphemes["و"]["word_initial"] == ["w"]


def test_labialised_khe_ye_madul_is_kept():
    """⟨خو⟩/⟨خوا⟩ keep the labial xʷ onset instead of the modern silent
    wāw reduction (Paul, Iranica: 'ḵʷ, which should be considered a
    phoneme in MP and ENP, lost its labial component (e.g., ḵʷār "mean"
    → [ḵār] ...)' — i.e. ENP still has ḵʷ)."""
    spec = load_json_spec("fa-x-enp")
    assert spec.graphemes["خو"] == ["xʷ"]
    assert spec.graphemes["خوا"] == ["xʷaː"]
    assert spec.graphemes["خواه"] == ["xʷaːh"]


def test_short_vowel_diacritics_are_quality_neutral():
    """The short-vowel diacritics keep ENP a/i/u, not the Tehran-shifted
    æ/e/o (Paul, Iranica: 'In modern NP, ENP i/u have been shifted to e/o
    ... the NP system being ā (=[å]) i u / a e o')."""
    spec = load_json_spec("fa-x-enp")
    assert spec.graphemes["َ"] == ["a"]
    assert spec.graphemes["ِ"] == ["i"]
    assert spec.graphemes["ُ"] == ["u"]


def test_undetermined_majhul_and_diphthongs_are_not_asserted():
    """Majhul ē/ō and the aj/au diphthongs are real ENP phonemes but are
    orthographically indistinguishable from maʿruf ī/ū and the plain
    vocalic readings already in the lattice (Miller 2012: 158, 'the
    Persian writing system, based on Arabic, does not provide any
    insight into changes in the pronunciation of these vowels'), so
    ⟨ی⟩'s default reading is left exactly as inherited from ``fa``
    rather than guessed."""
    fa_spec = load_json_spec("fa")
    enp_spec = load_json_spec("fa-x-enp")
    assert "ی" not in enp_spec.graphemes or enp_spec.graphemes["ی"] == fa_spec.graphemes["ی"]
    assert enp_spec.positional_graphemes.get("ی", fa_spec.positional_graphemes["ی"]) == \
        fa_spec.positional_graphemes["ی"]
