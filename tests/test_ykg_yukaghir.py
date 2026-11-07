"""Cited-rule conformance for Northern (Tundra) Yukaghir (ykg) in Cyrillic
script.

ISO 639-3 ``ykg`` is Northern (Tundra) Yukaghir, not Southern (Kolyma)
Yukaghir (``yux``) — confirmed against the SIL ISO 639-3 registry and
NorthEuraLex's own language page (``northeuralex.org/languages/ykg``,
titled "Northern Yukaghir"). This spec's grapheme table and citations
target Tundra Yukaghir.

The lateral-consonant rule below corrects a citation defect: an earlier
revision of this spec attributed the ``л``/``ль`` mapping to "Maslova
2003, A Grammar of Tundra Yukaghir" at DOI 10.1515/9783110197174 — but
that DOI is Maslova's separate Mouton Grammar Library monograph "A
Grammar of Kolyma Yukaghir" (about Southern Yukaghir, ``yux``), not a
book about Tundra Yukaghir. No such title exists at that DOI. The real
Tundra Yukaghir grammar sketch is Maslova (2003), *Tundra Yukaghir*,
Languages of the World/Materials 372, LINCOM Europa.

The consonant claim itself is verified here against Schmalz, Mark
(2013), *Aspects of the Grammar of Tundra Yukaghir* (PhD dissertation,
University of Amsterdam; https://pure.uva.nl/ws/files/1518096/130869_thesis.pdf),
Table 2.1.2 (consonant inventory, pp.30-31): the lateral series is a
plain-vs-palatalised opposition, /l/ (coronal) vs. /l'/ (palatal), with
the minimal pair ``tuŋul`` 'covering' ~ ``tuŋul'`` 'patch' (p.26). No
velarised lateral phoneme or allophone is described anywhere in the
dissertation. NorthEuraLex's own Segments column for ``ykg`` corroborates
this: ``л`` is transcribed plain [l] and ``ль`` is transcribed
palatalised [lʲ] in every wired form, never the reverse.
"""
from orthography2ipa.g2p import G2P


def _t(word):
    return G2P("ykg").transcribe_word(word).replace("ˈ", "")


def test_plain_l_is_not_velarised():
    """⟨л⟩ is the plain lateral /l/, matching Schmalz (2013) Table 2.1.2
    and NorthEuraLex's хуруул -> xuruːl. It is not the velarised /lˠ/ an
    earlier, fabricated-citation revision of this spec claimed."""
    assert G2P("ykg").spec.graphemes["л"] == ["l"]
    assert _t("хуруул") == "xuruːl"  # хуруул 'wave' (NorthEuraLex)


def test_soft_sign_l_is_palatalised_not_plain():
    """⟨ль⟩ is the palatalised /lʲ/, matching Schmalz (2013) Table 2.1.2
    and NorthEuraLex's хайль -> xajlʲ. It is not the plain, non-palatalised
    /l/ an earlier, fabricated-citation revision of this spec claimed."""
    assert G2P("ykg").spec.graphemes["ль"] == ["lʲ"]
    assert _t("хайль") == "xa̟jlʲ"  # хайль 'hare' (NorthEuraLex); а̟ is this
    # spec's advanced-front realisation of /a/ (PHOIBLE 193), independent of
    # the л/ль contrast under test here


def test_l_and_soft_sign_l_contrast():
    """tuŋul 'covering' ~ tuŋul' 'patch' (Schmalz 2013:26) is the minimal
    pair establishing the plain/palatalised contrast; the spec must not
    collapse the two graphemes to the same phoneme."""
    assert G2P("ykg").spec.graphemes["л"] != G2P("ykg").spec.graphemes["ль"]
