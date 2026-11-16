"""Limburgish written in Rheinische Dokumenta (`li-x-rheindok`).

Sourced against the standard itself — Honnen, Peter (after Fritz
Langensiepen), *Rheinische Dokumenta. Lautschrift für rheinische Mundarten*
(Rheinland-Verlag, Köln, 2nd ed. 1987, ISBN 3-7927-0947-3), issued by the
Landschaftsverband Rheinland — and cross-checked against the shipped
wikipron gold (``lim_latn_broad.tsv``), 89 of whose headwords carry a sign
that belongs to this notation and to no other Limburgish convention.

`li` models the Veldeke Spelling 2003 norm and is unchanged. The two are
disjoint sign systems, so the entries are separate rather than nested.
"""

from orthography2ipa import transcribe
from orthography2ipa.json_loader import load_json_spec


def _bare(word, code="li-x-rheindok"):
    """Transcription without the primary-stress mark."""
    return transcribe(word, code).replace("ˈ", "")


def test_diacritic_signs_are_distinct_from_their_plain_counterparts():
    """The nine diacritic signs carry the system and must not collapse.

    Rheinische Dokumenta separates ⟨e̩⟩ [ə] from ⟨e⟩ [e], ⟨ǫ⟩ [ɔ] from ⟨o⟩
    [o], ⟨ṣ⟩ [z] from ⟨s⟩ [s], and ⟨c͜h⟩ [ɣ] from ⟨ch⟩ [x]. A spec that
    drops a diacritic reads the wrong phoneme, not a near miss.
    """
    spec = load_json_spec("li-x-rheindok")
    assert spec.graphemes["e̩"] == ["ə"]
    assert spec.graphemes["e"] == ["e"]
    assert spec.graphemes["ǫ"] == ["ɔ"]
    assert spec.graphemes["o"] == ["o", "ʊ"]
    assert spec.graphemes["ṣ"] == ["z"]
    assert spec.graphemes["s"] == ["s"]
    assert spec.graphemes["c͜h"] == ["ɣ"]
    assert spec.graphemes["ch"] == ["x"]


def test_postalveolar_fricative_is_written_sch_not_sj():
    """⟨sch⟩ is [ʃ] here, where Spelling 2003 writes ⟨sj⟩.

    This is the single cleanest discriminator between the two conventions,
    and it is where `li` fails hardest on this part of the gold: reading
    ⟨sch⟩ as ⟨s⟩ + ⟨ch⟩ yields two segments where the word has one.
    """
    assert _bare("Be̩schǫǫt") == "bəʃɔːt"
    assert _bare("Kie̩sch") == "kiəʃ"


def test_vowel_length_comes_from_doubling_not_from_quality():
    """The standard is phonemic and writes length by doubling the sign.

    ⟨u⟩ and ⟨uu⟩ differ in length alone; the source table (English
    Wikipedia's Rheinische Dokumenta article) lists the lax vowel first
    for this pair — ⟨u⟩ [ʊ, u], ⟨uu⟩ [ʊː, uː], sample words "put" [ʊ] and
    "boot" [uː] — matching the canonical Germanic short=lax/long=tense
    pairing (ɪ/iː, ʊ/uː, ʏ/yː). ⟨o⟩ and ⟨oo⟩ pattern the same way.
    """
    assert _bare("Lue̩k") == "lʊək"
    assert _bare("Me̩luun") == "məlʊːn"
    assert _bare("Mǫǫnt") == "mɔːnt"


def test_entry_models_a_convention_li_does_not():
    """`li-x-rheindok` is its own table, not a silent fallback to `li`.

    An unknown ``-x-`` subtag resolves to the base spec, so a test written
    against ``transcribe`` alone would pass even if this entry did not
    exist. Pin the variant's own table, and pin that the two conventions
    genuinely disagree on the same string.
    """
    spec = load_json_spec("li-x-rheindok")
    assert spec.code == "li-x-rheindok"
    assert spec.orthography_standard.name == "Rheinische Dokumenta"
    # Spelling 2003's own signs are absent here, and vice versa.
    assert "sj" not in spec.graphemes
    assert "ao" not in spec.graphemes
    assert "ǫ" not in load_json_spec("li").graphemes
    assert transcribe("Kie̩sch", "li") != transcribe("Kie̩sch", "li-x-rheindok")


def test_li_records_the_gold_convention_mismatch():
    """The `li` row's audit verdict is in the tree, not only in a PR body."""
    spec = load_json_spec("li")
    assert spec.audit["wikipron"].conclusion.value == "mislabeled_gold"


def test_stress_comes_from_li_through_parent():
    """Rheinische Dokumenta writes the same Limburgish material as `li`.

    A second notation is not a second lect, so the place of the stress is
    the same. The entry states the `li` block with the unstressed prefixes
    in its own signs: schwa is ⟨e̩⟩ here, so ⟨ge⟩ is ⟨ge̩⟩. A one-syllable
    word takes the stress (Peters 2006, JIPA 36(1), p. 119).
    """
    from dataclasses import replace

    from orthography2ipa import G2P

    li_rules = G2P("li").spec.stress
    rd_rules = G2P("li-x-rheindok").spec.stress
    assert li_rules is not None and rd_rules is not None
    respelled = tuple(p.replace("e", "e\u0329") for p in li_rules.unstressed_prefixes)
    assert rd_rules.unstressed_prefixes == respelled
    assert replace(rd_rules, notes=li_rules.notes) == replace(li_rules, unstressed_prefixes=respelled)
    assert transcribe("Mǫǫnt", "li-x-rheindok") == "ˈmɔːnt"


def test_the_stress_skips_a_prefix_written_with_e_vertical_line():
    """⟨be̩⟩, ⟨ge̩⟩ and ⟨ve̩r⟩ are the schwa prefixes that `li` writes ⟨be⟩, ⟨ge⟩, ⟨ver⟩.

    The words are wikipron headwords; the gold carries no stress mark, so
    the place comes from the `li` sources (Peters 2006, p. 123, bəˈɣɔs).
    """
    assert transcribe("Be̩schǫǫt", "li-x-rheindok") == "bəˈʃɔːt"
    assert transcribe("ve̩rstand", "li-x-rheindok").startswith("vəʁˈ")
    assert transcribe("ge̩broek", "li-x-rheindok").startswith("ɡəˈ")


def test_a_plain_e_is_not_a_prefix():
    """Plain ⟨e⟩ is [e] here, so ⟨ge⟩ and ⟨be⟩ keep the default stress."""
    assert transcribe("gebroek", "li-x-rheindok").startswith("ˈɡe")
    assert transcribe("Gele̩", "li-x-rheindok") == "ˈɡelə"
