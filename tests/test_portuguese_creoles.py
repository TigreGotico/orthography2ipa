"""Cited-rule tests for the Portuguese-based creole specs added in the
Portuguese-creoles round: Kristang (mcm), Sãotomense/Forro (cri), Korlai
Indo-Portuguese (vkp) and Sri Lanka Portuguese Creole (idb).

Every test pins ONE claim the spec makes with a citation, on a real word of
the language taken from the cited source. Fa d'Ambô (fab) was DECLINED this
round: the accessible literature disagrees on the most basic fact a G2P spec
needs (five oral vowels per Post/APiCS vs seven per Balduino & Bandeira 2021)
and the primary grammars (Zamora Segorbe 2010; Hagemeijer et al. 2020) were
not accessible to adjudicate.
"""

from orthography2ipa.g2p import G2P


# ---------------------------------------------------------------------------
# mcm — Kristang / Papia Kristang (Baxter's Malay-based practical orthography)
# ---------------------------------------------------------------------------

def test_mcm_ch_and_j_are_the_retained_affricates():
    """Kristang keeps the older Portuguese affricates /tʃ dʒ/ where modern
    Portuguese has fricatives: cheru [t͡ʃə́ru] 'smell', jeru [d͡ʒə́ru]
    'son-in-law' (Baxter 1988, A Grammar of Kristang, p. 21; Table 2.1 p. 20).
    Baxter's orthography writes them ch and j (APiCS survey ch. 42)."""
    g = G2P("mcm")
    assert g.transcribe_word("cheru").endswith("tʃeru") or "tʃ" in g.transcribe_word("cheru")
    assert "dʒ" in g.transcribe_word("jeru")


def test_mcm_ny_and_ng_are_malay_digraphs():
    """The Malay-based orthography writes ny /ɲ/ and ng /ŋ/ (Baxter, APiCS
    survey ch. 42): linya [liɲa] 'line' (Baxter 1988, p. 22), mang [maŋ]
    'hand' — Portuguese mão denasalized to oral vowel + velar nasal
    (Baxter 1988, p. 22)."""
    g = G2P("mcm")
    assert g.transcribe_word("linya") == "ˈliɲa"
    assert g.transcribe_word("mang") == "ˈmaŋ"


def test_mcm_stress_is_penultimate_and_acute_marks_oxytones():
    """Contrastive stress: kaza [ˈkaza] 'house' vs kazá [kaˈza] 'marry'
    (Baxter 1988, p. 29); 'tonic stress is indicated ... by a written accent
    when the tonic does not fall on a penultimate syllable' (Baxter, APiCS
    survey ch. 42)."""
    g = G2P("mcm")
    assert g.transcribe_word("kaza") == "ˈkaza"
    assert g.transcribe_word("kazá") == "kaˈza"


def test_mcm_homorganic_nasal_clusters():
    """Nasal+consonant clusters are homorganic (Baxter 1988, p. 22):
    kanggrezu [kaŋgrezu] 'crab', kambrang [kambraŋ] 'prawn'."""
    g = G2P("mcm")
    assert "ŋɡ" in g.transcribe_word("kanggrezu")
    assert "mb" in g.transcribe_word("kambrang")


def test_mcm_coda_s_and_l_stay_plain_no_inherited_chiado():
    """Kristang has no /ʃ ʒ/ and no dark [ɫ]: mas [mas] 'more' (the only
    fricative attested word-finally), mal [mal] 'bad' (Baxter 1988, pp. 21,
    23). The inherited pt-PT chiado/dark-l rules are disabled by id."""
    g = G2P("mcm")
    assert g.transcribe_word("mas") == "ˈmas"
    assert g.transcribe_word("mal") == "ˈmal"


# ---------------------------------------------------------------------------
# cri — Sãotomense / Forro (ALUSTP orthography)
# ---------------------------------------------------------------------------

def test_cri_circumflex_marks_close_mid_bare_letters_open_mid():
    """ALUSTP: ê/ô are close-mid /e o/, bare e/o are open-mid /ɛ ɔ/ (Araujo &
    Agostinho 2010, p. 66): ôbô /obo/ 'forest', ope 'foot' opens with /ɔ/,
    djêlu /dʒelu/ 'money'."""
    g = G2P("cri")
    assert g.transcribe_word("ôbô") == "obo"
    assert g.transcribe_word("ope").startswith("ɔ")
    assert g.transcribe_word("djêlu") == "dʒelu"


def test_cri_biphonemic_nasality_coda_nasal_deletes():
    """Nasality is bi-phonemic: V + nasal coda, the coda deletes and
    nasalizes the vowel (Araujo & Agostinho 2010, p. 65): tason /tasõ/
    'to sit' (p. 66), tamen /tamẽ/ 'big' (p. 65)."""
    g = G2P("cri")
    assert g.transcribe_word("tason") == "tasõ"
    assert g.transcribe_word("tamen") == "tamẽ"


def test_cri_prenasalized_onsets():
    """Word-initial prenasalized onsets (Edo/Kongo substrate): ngembu
    [ŋɡembu] 'bat' (Araujo & Agostinho 2010, p. 68), mpon [mpõ] 'bread'
    (p. 69, ALUSTP writes V+m before p/b)."""
    g = G2P("cri")
    assert g.transcribe_word("ngembu").startswith("ŋɡ")
    assert g.transcribe_word("mpon") == "mpõ"


def test_cri_labial_velar_gb_and_affricates():
    """The labial-velar stop /ɡ͡b/ ⟨gb⟩ is an Edoid substrate retention:
    gbêgbê 'a snail sp.'; affricates tx /tʃ/ and dj /dʒ/ (ALUSTP table,
    Araujo & Agostinho 2010, pp. 66-67): kitxiba /kitʃiba/ 'silver banana'."""
    g = G2P("cri")
    assert g.transcribe_word("gbêgbê") == "ɡ͡beɡ͡be"
    assert g.transcribe_word("kitxiba") == "kitʃiba"


def test_cri_coda_sibilant_is_palatal():
    """The only licit non-nasal coda is /ʃ/ ⟨x⟩ (Araujo & Agostinho 2010,
    pp. 55, 67): mlaxka 'mask' keeps [ʃ] in the coda; stlijón [ʃtliʒõ]
    'healer'."""
    g = G2P("cri")
    assert g.transcribe_word("mlaxka") == "mlaʃka"


# ---------------------------------------------------------------------------
# vkp — Korlai Indo-Portuguese (Clements' scholarly transcription)
# ---------------------------------------------------------------------------

def test_vkp_aspirated_digraphs():
    """Korlai has an aspirated/breathy series written C+h (Clements, APiCS
    survey ch. 40, citing Clements 1996: 59-66): bharig 'belly', kharm
    'meat', thɛr 'unripe'."""
    g = G2P("vkp")
    assert g.transcribe_word("bharig") == "bʱaɾiɡ"
    assert g.transcribe_word("kharm") == "kʰaɾm"
    assert g.transcribe_word("thɛr") == "tʰɛɾ"


def test_vkp_tilde_nasal_vowels():
    """Nasal vowels /ĩ ũ ɛ̃ ɔ̃/ are written with the tilde in Clements'
    transcription (APiCS survey ch. 40): sĩk 'five', ɔ̃m 'man'."""
    g = G2P("vkp")
    assert g.transcribe_word("sĩk") == "sĩk"
    assert g.transcribe_word("ɔ̃m") == "ɔ̃m"


def test_vkp_final_j_is_the_glide():
    """The attested ⟨j⟩ example is the glide: lɔ̃j 'far' [lɔ̃j] (Clements,
    APiCS survey ch. 40); the spec ranks the glide reading first."""
    assert G2P("vkp").transcribe_word("lɔ̃j") == "lɔ̃j"


def test_vkp_v_is_the_approximant_and_no_dark_l():
    """/v/ is the approximant [ʋ] (South Asian areal feature) and no
    velarized [ɫ] is documented (Clements, APiCS survey ch. 40); the
    inherited pt-PT dark-l rule is disabled by id."""
    g = G2P("vkp")
    assert "ʋ" in g.transcribe_word("vaka")
    assert g.transcribe_word("mal") == "mal"


def test_vkp_apocope_monosyllables():
    """Posttonic deletion of the Portuguese cognate's final syllable
    (Clements 1996; Clements & Koontz-Garboden 2002): fáca > fak 'knife',
    água > ag 'water' — the apocopated forms transcribe as closed
    monosyllables."""
    g = G2P("vkp")
    assert g.transcribe_word("fak") == "fak"
    assert g.transcribe_word("ag") == "aɡ"


# ---------------------------------------------------------------------------
# idb — Sri Lanka Portuguese Creole (scholarly documentation convention)
# ---------------------------------------------------------------------------

def test_idb_doubled_vowel_is_long_and_attracts_stress():
    """Vowel length is phonemic and stress falls on the syllable with a long
    vowel, else initial (Cardoso, APiCS survey ch. 41): saaku 'sack' has a
    long stressed [aː]; penera 'sift' (Hume & Tserdanelis 2002, p. 4) takes
    initial stress."""
    g = G2P("idb")
    assert g.transcribe_word("saaku") == "ˈsaːku"
    assert g.transcribe_word("penera") == "ˈpenera"


def test_idb_retroflex_lateral_after_back_vowel():
    """Substrate retroflex allophony: /l/ → [ɭ] after non-high back vowels —
    maal [mɑːɭ] 'bad' (Cardoso, APiCS survey ch. 41); after front vowels the
    lateral stays plain."""
    g = G2P("idb")
    assert g.transcribe_word("maal") == "ˈmaːɭ"
    assert g.transcribe_word("mil") == "ˈmil"


def test_idb_retroflex_nasal_after_back_vowel():
    """/n/ → [ɳ] after non-high back vowels: nɔɔna [nɔːɳɐ] 'woman'
    (Cardoso, APiCS survey ch. 41)."""
    assert G2P("idb").transcribe_word("nɔɔna") == "ˈnɔːɳa"


def test_idb_homorganic_nc_clusters_not_prenasalized_units():
    """SLPC has obligatory homorganic NC clusters morpheme-internally, not
    prenasalized unit phonemes: li:ŋgu 'tongue' (Hume & Tserdanelis 2002,
    p. 5) — medial ⟨ng⟩ is [ŋɡ], word-final ⟨ng⟩ is bare [ŋ] (uŋ 'one',
    p. 4)."""
    g = G2P("idb")
    assert g.transcribe_word("liingu") == "ˈliːŋɡu"
    assert g.transcribe_word("ung") == "ˈuŋ"


def test_idb_coda_s_stays_plain_no_inherited_chiado():
    """SLPC coda /s/ is plain [s]: no:s 'we' (Hume & Tserdanelis 2002,
    p. 4); the inherited pt-PT chiado rules are disabled by id."""
    assert G2P("idb").transcribe_word("noos") == "ˈnoːs"
