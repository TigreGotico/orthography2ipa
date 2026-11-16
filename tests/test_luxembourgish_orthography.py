"""Luxembourgish letter values, from the Illustration of the IPA.

Every assertion cites Peter Gilles & Jürgen Trouvain, "Luxembourgish",
*Journal of the International Phonetic Association* 43(1), 67-74 (2013),
doi:10.1017/S0025100312000278; section numbers are the article's own.

Luxembourgish shares an alphabet with German and diverges from it in the
places these tests probe, so a spec that reads Luxembourgish spelling with
German values is wrong in exactly those places.
"""

from orthography2ipa import G2P


def _bare(code: str, word: str) -> str:
    return G2P(code).transcribe(word).replace("ˈ", "").replace("ˌ", "")


def test_doubled_consonants_are_single_consonants():
    """A doubled consonant letter marks the preceding vowel short and spells
    one consonant: Mamm [mɑm], Mann [mɑn], Kapp [kɑp], Hiwwel [ˈhivəl]
    (§2, Tables 2 and 3)."""
    assert _bare("lb", "Mamm").count("m") == 2      # onset + coda, not three
    assert _bare("lb", "Kapp").endswith("p")
    assert not _bare("lb", "Kapp").endswith("pp")
    assert "vv" not in _bare("lb", "Hiwwel")


def test_ss_spells_s_where_single_s_spells_z():
    """Keess [keːs] beside Sak [zaːk] and Tasen [ˈtaːzən] (§2, Table 2):
    ⟨ss⟩ is /s/, single ⟨s⟩ is /z/ initially and between vowels and /s/
    word-finally."""
    assert _bare("lb", "Keess").endswith("s")
    assert _bare("lb", "Sak").startswith("z")
    assert "z" in _bare("lb", "Tasen")
    assert _bare("lb", "Glas").endswith("s")


def test_final_obstruents_devoice():
    """"voiced obstruents cannot occur syllable-finally and will be devoiced
    ('Auslautverhärtung')" (§2).

    Only the word-final case is modelled. Syllable-final devoicing inside a
    word (Abt [ɑpt]) needs a syllabifier the positional contexts do not have.
    """
    assert _bare("lb", "Land").endswith("t")
    assert _bare("lb", "Kand").endswith("t")


def test_g_is_a_stop_only_word_initially():
    """"[ɡ] is found only word-initially and banned in all other positions,
    where the successors of historical [ɡ] are realized as fricatives"
    (§2): Vugel [ˈfuʁel], Dag [daːχ]."""
    assert _bare("lb", "goen").startswith("ɡ")
    assert "ʁ" in _bare("lb", "Vugel")
    assert _bare("lb", "Dag").endswith("χ")


def test_ch_is_uvular_after_back_vowels_and_alveolo_palatal_elsewhere():
    """"[χ] and [ɕ] are allophones of one single phoneme /χ/ ... determined
    ... by the preceding context ([χ ʁ] after phonologically back vowels,
    [ɕ ʑ] elsewhere)" (§2): Kuch [kuχ], aacht [aːχt], liicht [liːɕt]."""
    assert _bare("lb", "Kuch").endswith("χ")
    assert "χ" in _bare("lb", "aacht")
    assert "ɕ" in _bare("lb", "liicht")


def test_ae_is_short_open_front_not_the_german_long_vowel():
    """Männer [ˈmænɐ], hell [hæl] (§3.1, Table 3): ⟨ä⟩ is [æ]."""
    assert _bare("lb", "Männer").startswith("mæ")


def test_e_umlaut_is_schwa():
    """dënn [dən], Fësch [fəʃ], wëschen [ˈvəʃən] (§3.1, Table 3)."""
    assert _bare("lb", "dënn") == "dən"


def test_x_and_c_are_pronounced():
    """Neither letter may be dropped. ⟨x⟩ is /ks/ and ⟨qu⟩ is /kw/
    (Quatsch [kwɑtʃ], Quell [kwæl], §2)."""
    assert "ks" in _bare("lb", "Aaxt")
    assert _bare("lb", "Quell").startswith("kw")
    assert "k" in _bare("lb", "Bock")


def test_eifel_rule_does_not_fire_on_an_isolated_word():
    """The Eifel Rule is external sandhi — "In external sandhi, all final -n
    are deleted unless the following syllable starts with a vowel or the
    consonants [h d t ʦ n]" (§5) — so a citation form keeps its -n."""
    assert _bare("lb", "hinnen").endswith("n")
    assert _bare("lb", "goen").endswith("n")
