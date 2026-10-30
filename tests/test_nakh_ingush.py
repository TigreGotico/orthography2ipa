"""Ingush (inh) grapheme-to-IPA coverage for the Nakh Cyrillic spec.

Words are real, attested Ingush forms with a gloss; the expected IPA is
composed independently from the grapheme table cited in ``inh.json``
``sources`` (Schrijver 2021:88 for the vowel qualities, the Berkeley Ingush
project page for the palochka), never read back from the engine.
"""
import json
import unicodedata
from pathlib import Path

import orthography2ipa

DATA = Path(orthography2ipa.__file__).parent / "data"


def _tw(word):
    return orthography2ipa.G2P("inh").transcribe_word(word)


# --- vowel qualities --------------------------------------------------------
# Schrijver (2021:88, §2.1) gives the Ingush inventory after Nichols 2011:22
# and Imnajshvili 1977:37 with the low vowel written ``a`` and the high
# vowels ``i iː`` / ``u uː`` — not ``ɑ``, ``ɪ`` or ``ʊ``.

def test_da_father_low_vowel_is_a():
    # да "father": д /d/ + а /a/.
    assert _tw("да") == "da"


def test_nana_mother_low_vowel_is_a():
    # нана "mother": н /n/ + а /a/ + н /n/ + а /a/.
    assert _tw("нана") == "nana"


def test_xi_water_high_front_vowel_is_i():
    # хи "water": х /x/ + и /i/.
    assert _tw("хи") == "xi"


def test_tux_salt_high_back_vowel_is_u():
    # тух "salt": т /t/ + у /u/ + х /x/.
    assert _tw("тух") == "tux"


# --- unwritten vowel length reaches the lattice -----------------------------
# Schrijver (2021:88): the standard Chechen and Ingush orthographies "do not
# distinguish vowel length or diphthongization", and gives phonemic short/long
# pairs for ``и``/``у`` but no ``aː`` for ``а`` (footnote 1: Nichols treats
# that length as allophonic, not phonemic). So the ambiguity reaches the
# lattice for ``и``/``у`` but not for ``а``.

def test_length_ambiguity_is_a_lattice_alternative_not_a_decision():
    assert orthography2ipa.G2P("inh").word_candidates("хи")[:2] == ["xi", "xiː"]


def test_a_has_no_long_alternate():
    assert orthography2ipa.G2P("inh").word_candidates("да") == ["da"]


# --- the palochka writes a pharyngeal outside the ejective digraphs ---------
# Berkeley Ingush project ("Ingush Phonology and Orthography"): the letter
# writes ejectives after a voiceless consonant — covered by the digraphs
# пӏ тӏ кӏ цӏ чӏ — and pharyngeals word-initially, after a vowel, and after a
# voiced consonant.

def test_bare_palochka_word_initial_is_pharyngeal():
    # ӏа "winter": ӏ /ʕ/ + а /a/.
    assert _tw("ӏа") == "ʕa"


def test_bare_palochka_after_vowel_is_pharyngeal():
    # ниӏ "door": н /n/ + и /i/ + ӏ /ʕ/.
    assert _tw("ниӏ") == "niʕ"


def test_palochka_digraph_still_writes_an_ejective():
    # цӏи "name/fire": цӏ /t͡sʼ/ + и /i/ — the digraph must keep winning
    # maximal munch over ц + ӏ.
    assert _tw("цӏи") == "t͡sʼi"


# --- script integrity -------------------------------------------------------

def test_every_grapheme_key_is_cyrillic():
    """No Latin or digit lookalike may stand in for a Cyrillic letter.

    ⟨Ӏ⟩ U+04C0 / ⟨ӏ⟩ U+04CF (palochka), Latin ⟨I⟩ U+0049, Cyrillic ⟨І⟩
    U+0406 and the digit ⟨1⟩ are visually near-identical; a key built from
    the wrong one silently never matches.
    """
    spec = json.loads((DATA / "inh.json").read_text(encoding="utf-8"))
    for table in ("graphemes", "positional_graphemes", "word_exceptions"):
        for key in spec.get(table) or {}:
            for ch in key:
                name = unicodedata.name(ch)
                assert name.startswith("CYRILLIC"), (
                    f"{table} key {key!r} contains U+{ord(ch):04X} ({name})"
                )
