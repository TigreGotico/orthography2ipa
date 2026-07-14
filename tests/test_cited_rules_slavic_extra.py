"""Cited-rule conformance: West/South Slavic, Baltic, Finnic, Turkic, Caucasian.

Companion to ``test_cited_rules_slavic.py`` (ru/uk/be). Each test takes one
cited claim — from a spec's ``notes`` prose or from a single ``allophone_rules``
entry — quotes it with its citation, and proves the engine honours it on a real
word, isolating the claim to a single segment and pinning the complementary
environment with a minimal pair wherever the phonology allows.

Claims the engine does NOT honour are marked ``xfail(strict=True)`` with the
actual output in the reason; the assertion is left as the citation states it.
Where a spec honestly declares its own omission ("deliberately not mapped",
"currently under-generated"), the declared gap is pinned with a passing test.

Stress claims for cs, sk, pl, lv, hsb, dsb, csb and the Turkic specs are already
covered in ``test_stress.py`` / ``test_stress_other.py`` and are not repeated.
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(code, word):
    return G2P(code).transcribe_word(word)


def _bare(code, word):
    return _t(code, word).replace("ˈ", "").replace("ˌ", "")


# ===========================================================================
# pl — Standard Polish (Gussmann 2007, Rubach 1984, Bethin 1992)
# ===========================================================================


def test_pl_nasal_decomp_o_m():
    """PL_NASAL_DECOMP_O_M: /ɔ̃/ → [ɔm] before a labial stop.

    Rule notes: "Nasal vowel decomposes to oral vowel + homorganic nasal before
    stops/affricates (Gussmann (2007) The Phonology of Polish (OUP) §2.4): ząb
    [zɔmp], ręka [rɛŋka], kąt [kɔnt]."

    ząb is the cited word. The control is mąż, where the same ⟨ą⟩ stands before a
    fricative, not a stop, and must stay a nasal vowel.
    """
    assert _bare("pl", "ząb") == "zɔmp"
    assert "ɔ̃" in _bare("pl", "mąż")


def test_pl_nasal_decomp_o_n():
    """PL_NASAL_DECOMP_O_N: /ɔ̃/ → [ɔn] before a coronal stop.

    Rule notes: "Nasal vowel decomposes to oral vowel + homorganic nasal before
    stops/affricates (Gussmann (2007) The Phonology of Polish (OUP) §2.4): ząb
    [zɔmp], ręka [rɛŋka], kąt [kɔnt]."

    kąt is the cited word: the nasal is coronal [n], homorganic with the ⟨t⟩.
    """
    assert _bare("pl", "kąt") == "kɔnt"


def test_pl_nasal_decomp_o_ng():
    """PL_NASAL_DECOMP_O_NG: /ɔ̃/ → [ɔŋ] before a velar stop.

    Rule notes: "Nasal vowel decomposes to oral vowel + homorganic nasal before
    stops/affricates (Gussmann (2007) The Phonology of Polish (OUP) §2.4): ząb
    [zɔmp], ręka [rɛŋka], kąt [kɔnt]."

    mąka: ⟨ą⟩ before the velar ⟨k⟩ takes the velar nasal, where kąt takes [n].
    """
    assert _bare("pl", "mąka") == "mɔŋka"
    assert "ɔŋ" not in _bare("pl", "kąt")


def test_pl_nasal_decomp_e_m():
    """PL_NASAL_DECOMP_E_M: /ɛ̃/ → [ɛm] before a labial stop.

    Rule notes: "Nasal vowel decomposes to oral vowel + homorganic nasal before
    stops/affricates (Gussmann (2007) The Phonology of Polish (OUP) §2.4): ząb
    [zɔmp], ręka [rɛŋka], kąt [kɔnt]."
    """
    assert _bare("pl", "zęby") == "zɛmbɨ"


def test_pl_nasal_decomp_e_n():
    """PL_NASAL_DECOMP_E_N: /ɛ̃/ → [ɛn] before a coronal stop/affricate.

    Rule notes: "Nasal vowel decomposes to oral vowel + homorganic nasal before
    stops/affricates (Gussmann (2007) The Phonology of Polish (OUP) §2.4): ząb
    [zɔmp], ręka [rɛŋka], kąt [kɔnt]."

    tęcza has ⟨ę⟩ before the affricate ⟨cz⟩ /tʂ/, which the rule lists.
    """
    assert _bare("pl", "tęcza") == "tɛntʂa"


def test_pl_nasal_decomp_e_ng():
    """PL_NASAL_DECOMP_E_NG: /ɛ̃/ → [ɛŋ] before a velar stop.

    Rule notes: "Nasal vowel decomposes to oral vowel + homorganic nasal before
    stops/affricates (Gussmann (2007) The Phonology of Polish (OUP) §2.4): ząb
    [zɔmp], ręka [rɛŋka], kąt [kɔnt]."

    ręka is the cited word.
    """
    assert _bare("pl", "ręka") == "rɛŋka"


def test_pl_regr_devoice_b():
    """PL_REGR_DEVOICE_B: /b/ → [p] before a voiceless obstruent.

    Rule notes: "Regressive devoicing in obstruent clusters (Gussmann (2007) The
    Phonology of Polish (OUP) ch. 8): wódka [vutka], Abchaz- [apx-]."

    Abchazja is the cited word. The minimal pair is baba, where /b/ has no
    voiceless neighbour and stays [b].
    """
    assert _bare("pl", "Abchazja").startswith("apx")
    assert _bare("pl", "baba") == "baba"


def test_pl_regr_devoice_d():
    """PL_REGR_DEVOICE_D: /d/ → [t] before a voiceless obstruent.

    Rule notes: "Regressive devoicing in obstruent clusters (Gussmann (2007) The
    Phonology of Polish (OUP) ch. 8): wódka [vutka], Abchaz- [apx-]."

    wódka is the cited word; woda is the minimal pair with the same /d/
    intervocalic.
    """
    assert _bare("pl", "wódka") == "vutka"
    assert _bare("pl", "woda") == "vɔda"


def test_pl_regr_devoice_v():
    """PL_REGR_DEVOICE_V: /v/ → [f] before a voiceless obstruent.

    Rule notes: "Regressive devoicing in obstruent clusters (Gussmann (2007) The
    Phonology of Polish (OUP) ch. 8): wódka [vutka], Abchaz- [apx-]."

    wtorek: the initial ⟨w⟩ stands before the voiceless ⟨t⟩ and surfaces [f];
    in woda the same letter is prevocalic and stays [v].
    """
    assert _bare("pl", "wtorek").startswith("f")
    assert _bare("pl", "woda").startswith("v")


def test_pl_regr_devoice_z():
    """PL_REGR_DEVOICE_Z: /z/ → [s] before a voiceless obstruent.

    Rule notes: "Regressive devoicing in obstruent clusters (Gussmann (2007) The
    Phonology of Polish (OUP) ch. 8): wódka [vutka], Abchaz- [apx-]."

    rozkaz: the /z/ of the prefix stands before ⟨k⟩ and surfaces [s]; in rozum
    the same /z/ is prevocalic and stays [z].
    """
    assert _bare("pl", "rozkaz").startswith("rɔsk")
    assert _bare("pl", "rozum").startswith("rɔz")


def test_pl_regr_devoice_zh():
    """PL_REGR_DEVOICE_ʐ: /ʐ/ → [ʂ] before a voiceless obstruent.

    Rule notes: "Regressive devoicing in obstruent clusters (Gussmann (2007) The
    Phonology of Polish (OUP) ch. 8): wódka [vutka], Abchaz- [apx-]."

    ważka has ⟨ż⟩ before ⟨k⟩; ważny has the same ⟨ż⟩ before the sonorant /n/,
    which does not trigger devoicing.
    """
    assert _bare("pl", "ważka") == "vaʂka"
    assert _bare("pl", "ważny") == "vaʐnɨ"


def test_pl_regr_voice_t():
    """PL_REGR_VOICE_T: /t/ → [d] before a voiced obstruent.

    Rule notes: "Regressive voicing before voiced obstruents (Gussmann (2007) The
    Phonology of Polish (OUP) ch. 8): prośba [prɔʑba], Afgan- [avɡ-]. v and ʐ do
    not trigger."

    futbol: the ⟨t⟩ precedes the voiced ⟨b⟩ and surfaces [d].
    """
    assert _bare("pl", "futbol") == "fudbɔl"


def test_pl_regr_voice_k():
    """PL_REGR_VOICE_K: /k/ → [ɡ] before a voiced obstruent.

    Rule notes: "Regressive voicing before voiced obstruents (Gussmann (2007) The
    Phonology of Polish (OUP) ch. 8): prośba [prɔʑba], Afgan- [avɡ-]. v and ʐ do
    not trigger."

    jakby: the ⟨k⟩ precedes the voiced ⟨b⟩ and surfaces [ɡ]; in jaki the same
    ⟨k⟩ is prevocalic and stays [k].
    """
    assert _bare("pl", "jakby") == "jaɡbɨ"
    assert _bare("pl", "jaki") == "jaki"


def test_pl_regr_voice_f():
    """PL_REGR_VOICE_F: /f/ → [v] before a voiced obstruent.

    Rule notes: "Regressive voicing before voiced obstruents (Gussmann (2007) The
    Phonology of Polish (OUP) ch. 8): prośba [prɔʑba], Afgan- [avɡ-]. v and ʐ do
    not trigger."

    Afganistan is the cited stem: ⟨f⟩ before ⟨g⟩ surfaces [v].
    """
    assert _bare("pl", "Afganistan").startswith("avɡ")


def test_pl_regr_voice_sh_palatal():
    """PL_REGR_VOICE_ɕ: /ɕ/ → [ʑ] before a voiced obstruent.

    Rule notes: "Regressive voicing before voiced obstruents (Gussmann (2007) The
    Phonology of Polish (OUP) ch. 8): prośba [prɔʑba], Afgan- [avɡ-]. v and ʐ do
    not trigger."

    prośba is the cited word, reproduced in full; dziś keeps the same ⟨ś⟩
    word-finally as voiceless [ɕ].
    """
    assert _bare("pl", "prośba") == "prɔʑba"
    assert _bare("pl", "dziś").endswith("ɕ")


def test_pl_regr_voice_tsh_retroflex():
    """PL_REGR_VOICE_TꟅ: /tʂ/ → [dʐ] before a voiced obstruent.

    Rule notes: "Regressive voicing before voiced obstruents (Gussmann (2007) The
    Phonology of Polish (OUP) ch. 8): prośba [prɔʑba], Afgan- [avɡ-]. v and ʐ do
    not trigger."

    liczba: ⟨cz⟩ before the voiced ⟨b⟩ surfaces [dʐ]; in mecz the same ⟨cz⟩ is
    word-final and stays [tʂ].
    """
    assert _bare("pl", "liczba") == "lidʐba"
    assert _bare("pl", "mecz").endswith("tʂ")


def test_pl_progr_devoice_v_after_voiceless():
    """PL_PROGR_DEVOICE_V: /v/ → [f] after a voiceless obstruent.

    Rule notes: "Progressive devoicing of /v/ after a voiceless obstruent
    (Gussmann (2007) The Phonology of Polish (OUP) ch. 8): kwiat [kfjat], przy
    [pʂɨ] — the two Polish obstruents that assimilate rightward."

    kwiat is the cited word: /v/ follows /k/ and devoices leftward-triggered,
    where the regressive family would instead have voiced the /k/.
    """
    assert _bare("pl", "kwiat") == "kfjat"


@pytest.mark.xfail(
    strict=True,
    reason="PL_PROGR_DEVOICE_ʐ cites przy [pʂɨ]; engine produces [bʂɨ] — the /ʐ/ "
    "does devoice, but /p/ is simultaneously voiced to [b] because the "
    "PL_REGR_VOICE_* rules list ʐ among their triggers, contradicting their own "
    "note 'v and ʐ do not trigger'",
)
def test_pl_progr_devoice_zh_after_voiceless():
    """PL_PROGR_DEVOICE_ʐ: /ʐ/ → [ʂ] after a voiceless obstruent.

    Rule notes: "Progressive devoicing of /ʐ/ after a voiceless obstruent
    (Gussmann (2007) The Phonology of Polish (OUP) ch. 8): kwiat [kfjat], przy
    [pʂɨ] — the two Polish obstruents that assimilate rightward."

    przy is the cited word, and its cited transcription keeps the /p/ voiceless:
    ⟨rz⟩ assimilates rightward, it does not trigger regressive voicing.
    """
    assert _bare("pl", "przy") == "pʂɨ"


def test_pl_n_velar_before_velar_stop():
    """PL_N_VELAR: /n/ → [ŋ] before a velar stop.

    Rule notes: "/n/ assimilates to [ŋ] before velar stops (Gussmann (2007) The
    Phonology of Polish (OUP) §2.3): bank [baŋk], Kongo [kɔŋɡɔ]."

    Both cited words are reproduced; rana pins the complementary environment,
    where prevocalic /n/ stays coronal.
    """
    assert _bare("pl", "bank") == "baŋk"
    assert _bare("pl", "Kongo") == "kɔŋɡɔ"
    assert _bare("pl", "rana") == "rana"


def test_pl_final_devoicing():
    """Word-final obstruents devoice.

    pl notes: "FINAL DEVOICING: Polish obstruents devoice in coda/word-finally."
    Sources: Rubach (1984), Bethin (1992), Gussmann (2007).

    Three minimal pairs isolate the final segment: róg/rogu (ɡ~k), nóż/noża
    (ʐ~ʂ), wóz/wozu (z~s).
    """
    assert _bare("pl", "róg") == "ruk"
    assert _bare("pl", "rogu") == "rɔɡu"
    assert _bare("pl", "nóż") == "nuʂ"
    assert _bare("pl", "noża") == "nɔʐa"
    assert _bare("pl", "wóz") == "vus"
    assert _bare("pl", "wozu") == "vɔzu"


@pytest.mark.xfail(
    strict=True,
    reason="pl notes claim all obstruents devoice word-finally; engine produces "
    "[wudʑ] for łódź — word-final /dʑ/ stays voiced, while the plain /ʑ/ of weź "
    "and the /dz/ of wódz both devoice, so the affricate dʑ is the one gap",
)
def test_pl_final_devoicing_of_dz_palatal():
    """Word-final /dʑ/ devoices to [tɕ].

    pl notes: "FINAL DEVOICING: Polish obstruents devoice in coda/word-finally."

    łódź isolates the claim on a single word-final affricate. The sibling
    obstruents devoice as claimed: weź → [vɛɕ], wódz → [vuts].
    """
    assert _bare("pl", "weź").endswith("ɕ")
    assert _bare("pl", "wódz").endswith("ts")
    assert _bare("pl", "łódź") == "wutɕ"


def test_pl_word_final_e_nasal_denasalizes():
    """Word-final ⟨ę⟩ is [ɛ], not a nasal vowel.

    pl notes: "NASAL VOWELS: ą→[ɔ] and ę→[ɛ] word-finally in contemporary Polish
    (de-nasalization); nasal elsewhere before consonants."

    tę isolates the claim on the word-final vowel; tęcza keeps the same letter
    pre-consonantally, where it must stay nasal.
    """
    assert _bare("pl", "tę") == "tɛ"
    assert "ɛn" in _bare("pl", "tęcza")


@pytest.mark.xfail(
    strict=True,
    reason="pl notes claim ą → [ɔ] word-finally (de-nasalization); engine produces "
    "[sɔw̃] for są — the word-final nasal vowel keeps a nasal glide, while the "
    "parallel claim for ę is honoured (tę → [tɛ])",
)
def test_pl_word_final_a_nasal_denasalizes():
    """Word-final ⟨ą⟩ is [ɔ], not a nasal vowel.

    pl notes: "NASAL VOWELS: ą→[ɔ] and ę→[ɛ] word-finally in contemporary Polish
    (de-nasalization); nasal elsewhere before consonants."
    """
    assert _bare("pl", "są") == "sɔ"


# ===========================================================================
# cs — Standard Czech (Palková 1994, Šimáčková et al. 2012, Short 1993)
# ===========================================================================


def test_cs_final_devoicing_b_to_p():
    """Word-final /b/ devoices to [p].

    cs notes: "FINAL DEVOICING: obstruents devoice in coda/word-finally (b→p,
    d→t, ď→ť, g→k, v→f, z→s, ž→š, h→ch)." Sources: Palková (1994), Šimáčková et
    al. (2012), Short (1993).

    Minimal pair dub/duby: the same /b/ is medial in the plural and stays voiced.
    """
    assert _bare("cs", "dub") == "dup"
    assert _bare("cs", "duby") == "dubɪ"


def test_cs_final_devoicing_d_to_t():
    """Word-final /d/ devoices to [t].

    cs notes: "FINAL DEVOICING: obstruents devoice in coda/word-finally (b→p,
    d→t, ď→ť, g→k, v→f, z→s, ž→š, h→ch)."

    Minimal pair hrad/hradu.
    """
    assert _bare("cs", "hrad") == "ɦrat"
    assert _bare("cs", "hradu") == "ɦradu"


def test_cs_final_devoicing_dj_to_tj():
    """Word-final /ɟ/ (⟨ď⟩) devoices to [c] (⟨ť⟩).

    cs notes: "FINAL DEVOICING: obstruents devoice in coda/word-finally (b→p,
    d→t, ď→ť, g→k, v→f, z→s, ž→š, h→ch)."

    Minimal pair zeď/zedi: the palatal stop stays voiced before a vowel.
    """
    assert _bare("cs", "zeď") == "zɛc"
    assert _bare("cs", "zedi") == "zɛɟɪ"


def test_cs_final_devoicing_g_to_k():
    """Word-final /ɡ/ devoices to [k].

    cs notes: "FINAL DEVOICING: obstruents devoice in coda/word-finally (b→p,
    d→t, ď→ť, g→k, v→f, z→s, ž→š, h→ch)."

    gong isolates the claim: the word-initial ⟨g⟩ stays [ɡ], the final one is [k].
    """
    assert _bare("cs", "gong") == "ɡonk"


def test_cs_final_devoicing_v_to_f():
    """Word-final /v/ devoices to [f].

    cs notes: "FINAL DEVOICING: obstruents devoice in coda/word-finally (b→p,
    d→t, ď→ť, g→k, v→f, z→s, ž→š, h→ch)."

    Minimal pair krev/krvi.
    """
    assert _bare("cs", "krev") == "krɛf"
    assert _bare("cs", "krvi") == "krvɪ"


def test_cs_final_devoicing_z_to_s():
    """Word-final /z/ devoices to [s].

    cs notes: "FINAL DEVOICING: obstruents devoice in coda/word-finally (b→p,
    d→t, ď→ť, g→k, v→f, z→s, ž→š, h→ch)."

    Minimal pair vůz/vozu.
    """
    assert _bare("cs", "vůz") == "vuːs"
    assert _bare("cs", "vozu") == "vozu"


def test_cs_final_devoicing_zh_to_sh():
    """Word-final /ʒ/ (⟨ž⟩) devoices to [ʃ] (⟨š⟩).

    cs notes: "FINAL DEVOICING: obstruents devoice in coda/word-finally (b→p,
    d→t, ď→ť, g→k, v→f, z→s, ž→š, h→ch)."

    nůž/noze pins the alternation on the final consonant alone.
    """
    assert _bare("cs", "nůž") == "nuːʃ"
    assert "ʃ" not in _bare("cs", "noze")


def test_cs_h_devoices_to_x_in_coda():
    """⟨h⟩ is [ɦ] in the onset and [x] in the coda.

    cs notes: "H: voiced [ɦ] in onset; devoices to [x] in coda."

    Minimal pair sníh/sněhu: the same ⟨h⟩ is word-final in one and prevocalic in
    the other.
    """
    assert _bare("cs", "sníh") == "sɲiːx"
    assert _bare("cs", "sněhu").endswith("ɦu")


@pytest.mark.xfail(
    strict=True,
    reason="cs notes claim obstruents devoice in coda as well as word-finally "
    "(b→p); engine produces [obxot] for obchod — the coda /b/ before voiceless "
    "/x/ stays voiced, so only the word-final half of the claim is implemented",
)
def test_cs_coda_devoicing_word_internally():
    """Coda obstruents devoice word-internally, not only word-finally.

    cs notes: "FINAL DEVOICING: obstruents devoice in coda/word-finally (b→p,
    d→t, ď→ť, g→k, v→f, z→s, ž→š, h→ch)."

    obchod has /b/ in the coda of the prefix ob-, before the voiceless /x/ of
    -chod; the word-final /d/ of the same word devoices as claimed.
    """
    assert _bare("cs", "obchod") == "opxot"


def test_cs_e_hacek_is_je_after_labial():
    """⟨ě⟩ is [jɛ] after most consonants.

    cs notes: "Ě: [jɛ] after most consonants; causes palatal softening of
    preceding d/t/n."

    věc isolates the glide on the labial ⟨v⟩, which is not one of the softening
    consonants.
    """
    assert _bare("cs", "věc") == "vjɛts"


def test_cs_e_hacek_softens_preceding_dental():
    """⟨ě⟩ softens a preceding d/t/n to the palatal series.

    cs notes: "Ě: [jɛ] after most consonants; causes palatal softening of
    preceding d/t/n."

    děti, tělo and němý each isolate one member of the series; no [j] appears,
    because the glide is absorbed into the palatal stop/nasal.
    """
    assert _bare("cs", "děti").startswith("ɟɛ")
    assert _bare("cs", "tělo").startswith("cɛ")
    assert _bare("cs", "němý").startswith("ɲɛ")


def test_cs_r_hacek_is_the_raised_trill():
    """⟨ř⟩ is the phoneme /r̝/, distinct from plain /r/.

    cs notes: "Notable for the unique phoneme /r̝/ (⟨ř⟩)."

    Minimal pair řeka/ryba on the initial rhotic.
    """
    assert _bare("cs", "řeka").startswith("r̝")
    assert _bare("cs", "ryba").startswith("r")
    assert "r̝" not in _bare("cs", "ryba")


# ===========================================================================
# csb — Kashubian (Stone 1993)
# ===========================================================================


def test_csb_nasal_a_and_schwa():
    """⟨ą⟩ is the nasal vowel /ɔ̃/ and ⟨ë⟩ is the schwa /ə/.

    csb notes: "Nasal vowel ą /ɔ̃/, schwa ë /ə/." Stone (1993), Kashubian.

    kąsk isolates the nasal vowel; kaszëbsczi isolates the schwa, which no other
    West Slavic spec in this cluster has.
    """
    assert _bare("csb", "kąsk") == "kɔ̃sk"
    assert "ə" in _bare("csb", "kaszëbsczi")


def test_csb_digraphs_beat_single_letters():
    """The digraphs ⟨sz cz rz dż⟩ are matched ahead of their component letters.

    csb notes: "Digraphs sz, cz, rz, dż precede single letters."

    kaszëbsczi: ⟨sz⟩ surfaces as the single segment [ʃ], not as [s]+[z].
    """
    assert "ʃ" in _bare("csb", "kaszëbsczi")
    assert "sz" not in _bare("csb", "kaszëbsczi")


# ===========================================================================
# mk — Standard Macedonian
# ===========================================================================


def test_mk_unique_letters():
    """⟨ѕ⟩ = [dz], ⟨ѓ⟩ = [ɟ], ⟨ќ⟩ = [c].

    mk notes: "Unique letters: ⟨ѕ⟩ = [dz], ⟨ѓ⟩ = [ɟ], ⟨ќ⟩ = [c]."

    One word per letter, each isolating the claimed segment.
    """
    assert _bare("mk", "ѕвезда").startswith("dz")
    assert _bare("mk", "ѓавол").startswith("ɟ")
    assert _bare("mk", "куќа") == "kuca"


def test_mk_palatal_sonorants():
    """⟨љ⟩ = [ʎ], ⟨њ⟩ = [ɲ].

    mk notes: "⟨љ⟩ = [ʎ], ⟨њ⟩ = [ɲ]."
    """
    assert _bare("mk", "љубов").startswith("ʎ")
    assert _bare("mk", "њива").startswith("ɲ")


@pytest.mark.xfail(
    strict=True,
    reason="mk notes claim fixed antepenultimate stress; engine emits no stress "
    "mark at all for Macedonian (планина → [planina]) — the spec carries no "
    "stress block, unlike its Slavic siblings",
)
def test_mk_antepenultimate_stress():
    """Stress is fixed on the third-from-last syllable.

    mk notes: "Fixed antepenultimate stress (third-from-last syllable)."

    планина has three syllables, so the antepenult is the first.
    """
    assert _t("mk", "планина") == "ˈplanina"


# ===========================================================================
# rsk — Pannonian Rusyn
# ===========================================================================


def test_rsk_g_letters_are_distinct():
    """⟨г⟩ = /ɦ/ and ⟨ґ⟩ = /ɡ/ are fully independent letters.

    rsk notes: "⟨г⟩ and ⟨ґ⟩ are fully independent letters: /ɦ/ vs /ɡ/."
    """
    assert _bare("rsk", "гвизда").startswith("ɦ")
    assert _bare("rsk", "ґазда").startswith("ɡ")


def test_rsk_i_has_merged_with_y():
    """⟨и⟩ = /i/; there is no /ɪ/ or /ɨ/.

    rsk notes: "Vowels are a five-way system /i ɛ a ɔ u/ with no length contrast
    ... ⟨и⟩=/i/ (no /ɪ/ or /ɨ/ — *i and *y have merged, unlike Ukrainian and
    Carpathian Rusyn)."

    руски: the ⟨и⟩ is [i], where the Ukrainian cognate has [ɪ].
    """
    out = _bare("rsk", "руски")
    assert out == "ruski"
    assert "ɪ" not in out and "ɨ" not in out


def test_rsk_softened_dentals_are_true_palatals():
    """⟨д л н т⟩ + ⟨ь/є/ї/я/ю⟩ give the true palatals /ɟ ʎ ɲ c/, not /dʲ lʲ nʲ tʲ/.

    rsk notes: "Palatalisation: ONLY ⟨д л н т⟩ may be followed by ⟨ь⟩, and they
    then become the true palatals /ɟ ʎ ɲ c/ (not /dʲ lʲ nʲ tʲ/); the same four
    consonants take these values before ⟨є ї я ю⟩."

    конь isolates /ɲ/ before ⟨ь⟩; дїте isolates /ɟ/ before ⟨ї⟩.
    """
    assert _bare("rsk", "конь") == "kɔɲ"
    assert _bare("rsk", "дїте").startswith("ɟ")


def test_rsk_affricate_digraphs():
    """⟨дз⟩ = /d͡z/ and ⟨дж⟩ = /d͡ʒ/ are native affricate digraphs.

    rsk notes: "⟨дз⟩ /d͡z/ and ⟨дж⟩ /d͡ʒ/ are affricate digraphs and are frequent
    native reflexes (dj > dz, tj > ts)."
    """
    assert _bare("rsk", "дзвон").startswith("dz")
    assert _bare("rsk", "джем").startswith("dʒ")


def test_rsk_declared_omissions():
    """The spec's declared omissions hold: ⟨щ⟩ unmapped, stress not emitted.

    rsk notes: "DELIBERATELY OMITTED: ⟨щ⟩ — it is in the alphabet, but none of the
    sources read here gives it an IPA value for Pannonian Rusyn ... so it is left
    unmapped rather than invented. ... Stress is regularly penultimate but is not
    emitted."

    This pins the omissions the spec declares, rather than asserting values the
    spec explicitly refuses to invent.
    """
    assert _t("rsk", "щ") == ""
    assert "ˈ" not in _t("rsk", "вода")


# ===========================================================================
# ltg / lv — Baltic
# ===========================================================================


def test_ltg_y_is_the_central_vowel():
    """⟨y⟩ = /ɨ/, the letter that distinguishes Latgalian from standard Latvian.

    ltg notes: "unlike standard Latvian — the letter ⟨y⟩ for the central vowel
    /ɨ/." (2007 Latgalian Orthography Rules, State Language Centre.)
    """
    assert _bare("ltg", "ryga") == "rɨɡa"


def test_ltg_diphthongs_ie_and_uo():
    """⟨ie⟩ and ⟨uo⟩ spell the diphthongs /iɛ/ and /uɔ/.

    ltg notes: "Diphthongs /iɛ/ and /uɔ/ are written ⟨ie⟩ and ⟨uo⟩."
    """
    assert "iɛ" in _bare("ltg", "piens")
    assert "uɔ" in _bare("ltg", "muoja")


def test_ltg_macron_marks_length():
    """Macrons (ā ē ī ō ū) mark long vowels.

    ltg notes: "The 2007 standard orthography ... is close to phonemic, with
    macrons for long vowels (ā ē ī ō ū)."

    Minimal pair on the same letter: volūda has the long [uː], muoja the short.
    """
    assert _bare("ltg", "volūda") == "vɔluːda"


@pytest.mark.xfail(
    strict=True,
    reason="ltg notes claim first-syllable stress; engine emits no stress mark at "
    "all for Latgalian (volūda → [vɔluːda]), while its sister lv marks it "
    "(valoda → [ˈvaluoda]) — the ltg spec carries no stress block",
)
def test_ltg_initial_stress():
    """Stress is on the first syllable.

    ltg notes: "Pitch accent and vowel-length interactions are not modelled here;
    stress is generally on the first syllable."
    """
    assert _t("ltg", "volūda").startswith("ˈ")


# ===========================================================================
# olo / vep — Finnic
# ===========================================================================


def test_olo_finnic_vowel_convention():
    """⟨a⟩ = /ɑ/ and ⟨ä⟩ = /æ/; ⟨v⟩ = /ʋ/.

    olo notes: "Values follow the Finnic convention: <a>=/ɑ/, <ä>=/æ/, <ö>=/ø/,
    <y>=/y/, <c>=/ts/, <č>=/tʃ/, <š>=/ʃ/, <ž>=/ʒ/, <v>=/ʋ/."

    The ⟨a⟩/⟨ä⟩ pair is the falsifiable core: two back/front vowels written with
    the same base letter.
    """
    assert _bare("olo", "mua") == "muɑ"
    assert _bare("olo", "päivy").startswith("pæ")
    assert _bare("olo", "vezi").startswith("ʋ")


def test_olo_hacek_letters():
    """⟨č⟩ = /tʃ/ and ⟨š⟩ = /ʃ/.

    olo notes: "<c>=/ts/, <č>=/tʃ/, <š>=/ʃ/, <ž>=/ʒ/."
    """
    assert _bare("olo", "čoma").startswith("tʃ")
    assert _bare("olo", "šuuri").startswith("ʃ")


def test_vep_umlaut_letters():
    """⟨ü⟩ = /y/, ⟨ä⟩ = /æ/, ⟨c⟩ = /t͡s/.

    vep notes: "⟨c⟩ = /t͡s/, ⟨č⟩ = /t͡ʃ/, ⟨š⟩ = /ʃ/, ⟨ž⟩ = /ʒ/, ⟨ü⟩ = /y/, ⟨ä⟩ =
    /æ/, ⟨ö⟩ = /ø/."
    """
    assert _bare("vep", "vepsän") == "vepsæn"
    assert _bare("vep", "kacuhta").startswith("kɑt͡su")


def test_vep_prime_palatalisation_is_declared_undergenerated():
    """The prime ⟨ʹ⟩ does not palatalise the preceding consonant — a declared gap.

    vep notes: "PALATALISATION: the prime ⟨ʹ⟩ palatalises the PRECEDING consonant
    (kʹ tʹ mʹ …) ... It is a modifier, not a segment of its own, and is therefore
    not listed as a grapheme — a spec-level modifier for it is not yet expressed,
    so the palatalised series is currently under-generated."

    The spec documents this gap, so the declared behaviour is pinned rather than
    xfailed: kelʹ emits a plain [l], and the prime contributes no segment.
    """
    assert _bare("vep", "kelʹ") == "kel"


# ===========================================================================
# kv / koi — Permic
# ===========================================================================


def test_kv_dentals_palatalise_before_front_vowels():
    """⟨д з л н с т⟩ → /ɟ ʑ ʎ ɲ ɕ c/ before ⟨е ё и ю я ь⟩.

    kv notes: "⟨д з л н с т⟩ are realised as /ɟ ʑ ʎ ɲ ɕ c/ before ⟨е ё и ю я⟩ and
    before the soft sign ⟨ь⟩, so those sequences are entered here as multigraph
    keys."

    ти isolates /c/ before ⟨и⟩; де isolates /ɟ/; сьӧд isolates /ɕ/ before ⟨ь⟩.
    """
    assert _bare("kv", "ти") == "ci"
    assert _bare("kv", "де") == "ɟe"
    assert _bare("kv", "сьӧд").startswith("ɕ")


def test_kv_hard_i_does_not_palatalise():
    """⟨і⟩ is the 'hard i': it spells /i/ without palatalising the consonant.

    kv notes: "⟨і⟩ is the 'hard i': it spells /i/ after т д с з н л without
    palatalising them, so it is deliberately NOT part of any digraph."

    Minimal pair ті/ти: the same consonant letter, the same vowel /i/, and the
    palatalisation turns on exactly the choice of ⟨і⟩ vs ⟨и⟩.
    """
    assert _bare("kv", "ті") == "ti"
    assert _bare("kv", "ти") == "ci"


def test_kv_affricate_digraphs():
    """⟨дж дз тш⟩ spell /dʒ dʑ tʃ/.

    kv notes: "The affricates /dʒ dʑ tʃ/ are written with the digraphs ⟨дж дз
    тш⟩, also entered as keys."
    """
    assert _bare("kv", "джын").startswith("dʒ")
    assert _bare("kv", "дзоридз").startswith("dʑ")
    assert _bare("kv", "тшак").startswith("tʃ")


def test_koi_shares_the_zyrian_grapheme_map():
    """Komi-Permyak uses the Komi-Zyrian map: softened dentals, hard ⟨і⟩, digraphs.

    koi notes: "The grapheme map is therefore the Komi-Zyrian one: ⟨д з л н с т⟩
    → /ɟ ʑ ʎ ɲ ɕ c/ before ⟨е ё и ю я ь⟩ ... ⟨і⟩ = 'hard i' /i/ leaving the
    preceding consonant hard, and the affricate digraphs ⟨дж⟩ /dʒ/, ⟨дз⟩ /dʑ/,
    ⟨тш⟩ /tʃ/."
    """
    assert _bare("koi", "сё").startswith("ɕ")
    assert _bare("koi", "іб") == "ib"
    assert _bare("koi", "дзо").startswith("dʑ")
    assert _bare("koi", "тшак").startswith("tʃ")


# ===========================================================================
# Turkic
# ===========================================================================


def test_sah_long_vowels_are_written_doubled():
    """Yakut long vowels are written by doubling the vowel letter.

    sah notes: "Yakut has eight vowel qualities with a phonemic length contrast;
    long vowels are written by DOUBLING the vowel letter (аа оо уу ыы ии ээ өө
    үү) ... listed as multigraph keys so that maximal-munch matching prefers them
    over the single letters."

    Minimal pair кыыс/тыла on the same vowel letter ⟨ы⟩.
    """
    assert _bare("sah", "кыыс") == "kɯːs"
    assert _bare("sah", "тыла") == "tɯla"


def test_sah_written_diphthongs():
    """⟨ыа иэ уо үө⟩ are the four written diphthongs.

    sah notes: "the four diphthongs are written ⟨ыа иэ уо үө⟩ — all of these are
    listed as multigraph keys."
    """
    assert _bare("sah", "ыал") == "ɯal"
    assert _bare("sah", "уот") == "uɔt"
    assert _bare("sah", "үөрэх").startswith("yø")


def test_sah_soft_sign_digraphs():
    """⟨дь⟩ = /d͡ʒ/ and ⟨нь⟩ = /ɲ/; bare ⟨ь⟩ and ⟨ъ⟩ are deliberately unmapped.

    sah notes: "the digraphs ⟨дь⟩ /d͡ʒ/ and ⟨нь⟩ /ɲ/ ... The soft sign ⟨ь⟩ and
    hard sign ⟨ъ⟩ are NOT mapped: they carry no independent segment ... so they
    are deliberately omitted rather than given an invented value."

    The declared omission is pinned with a passing assertion, as the spec states.
    """
    assert _bare("sah", "дьол").startswith("d͡ʒ")
    assert _bare("sah", "ньуучча").startswith("ɲ")
    assert _t("sah", "ь") == ""
    assert _t("sah", "ъ") == ""


def test_krc_digraphs():
    """⟨гъ⟩ = /ʁ/, ⟨къ⟩ = /q/, ⟨нг⟩ = /ŋ/, ⟨дж⟩ = /dʒ/.

    krc notes: "Digraphs: <гъ> = /ʁ/, <къ> = /q/, <нг> = /ŋ/, <дж> = /dʒ/
    (Karachay; the Balkar varieties have /ʒ/ or /z/ here)."

    къарачай and малкъар isolate the uvular; нгы and джол the other two.
    """
    assert _bare("krc", "къарачай").startswith("q")
    assert _bare("krc", "малкъар").endswith("qar")
    assert _bare("krc", "нгы") == "ŋɯ"
    assert _bare("krc", "джол").startswith("dʒ")


def test_krc_front_rounded_vowels_use_iotated_letters():
    """⟨ю⟩ = /y/, ⟨ё⟩ = /ø/, ⟨ы⟩ = /ɯ/ — the Russian letters carry Turkic values.

    krc notes: "Front-rounded vowels are written with the Russian iotated letters:
    <ю> = /y/, <ё> = /ø/; <ы> = /ɯ/."
    """
    assert _bare("krc", "юй") == "yj"
    assert _bare("krc", "ёз") == "øz"
    assert _bare("krc", "ыз") == "ɯz"


def test_kk_cyrillic_letters():
    """Қ = /q/, Ғ = /ʁ/, Ң = /ŋ/, Ұ = /ʊ/, Ү = /y/, І = /ɪ/.

    kk notes: "Қ = uvular /q/; Ғ = /ʁ/; Ң = /ŋ/; Ұ = back unrounded /ʊ/; Ү = /y/;
    І = /ɪ/."
    """
    assert _bare("kk", "қазақ") == "qazaq"
    assert _bare("kk", "ғылым").startswith("ʁ")
    assert "ŋ" in _bare("kk", "маңғаз")
    assert _bare("kk", "ұл") == "ʊl"
    assert _bare("kk", "үй") == "yj"
    assert _bare("kk", "іс") == "ɪs"


def test_kaa_vowel_harmony_letters():
    """⟨á ó ú i e⟩ are front, ⟨a o u ı⟩ back.

    kaa notes: "Regular one-letter-one-phoneme orthography with front/back vowel
    harmony (⟨á ó ú i e⟩ front, ⟨a o u ı⟩ back)."

    Minimal pair tı/ta is not available across the harmony line, so the acute
    letters are pinned against their plain counterparts: á vs a, ı vs i.
    """
    assert _bare("kaa", "áke").startswith("æ")
    assert _bare("kaa", "ta") == "ta"
    assert _bare("kaa", "ıs") == "ɯs"
    assert _bare("kaa", "úy") == "yj"


def test_uz_latin_apostrophe_letters():
    """⟨oʻ⟩ = /ø/, ⟨gʻ⟩ = /ʁ/, ⟨q⟩ = /q/.

    uz notes: "Standard Uzbek in Latin script (official since 1993, Unicode
    apostrophe forms oʻ and gʻ). ... Q is uvular /q/. Oʻ represents /ø/ (front
    rounded). Gʻ represents voiced uvular fricative /ʁ/."
    """
    assert _bare("uz", "oʻzbek").startswith("ø")
    assert _bare("uz", "gʻalaba").startswith("ʁ")
    assert _bare("uz", "qalb").startswith("q")


def test_az_final_devoicing_b_to_p():
    """Azerbaijani word-final b → p.

    az notes: "Final devoicing: b→p, c→ç, d→t, g→k."

    Minimal pair kitab/kitabı: the suffixed form keeps the /b/ intervocalic.
    """
    assert _bare("az", "kitab") == "kitap"
    assert _bare("az", "kitabı") == "kitabɯ"


def test_az_final_devoicing_d_to_t():
    """Azerbaijani word-final d → t.

    az notes: "Final devoicing: b→p, c→ç, d→t, g→k."
    """
    assert _bare("az", "od") == "ot"


def test_az_final_devoicing_c_to_ch():
    """Azerbaijani word-final ⟨c⟩ /dʒ/ → ⟨ç⟩ /tʃ/.

    az notes: "Final devoicing: b→p, c→ç, d→t, g→k."
    """
    assert _bare("az", "ağac").endswith("tʃ")


def test_az_gh_is_a_fricative_unlike_turkish():
    """⟨ğ⟩ is the fricative [ɣ], not the silent Turkish ⟨ğ⟩.

    az notes: "Ğ is a fricative [ɣ] unlike Turkish where it is silent."
    """
    assert _bare("az", "dağ") == "daɣ"


def test_tg_uvular_q_is_maintained():
    """Tajik keeps /q/ as [q], and the Cyrillic special letters carry Persian values.

    tg notes: "CONSERVATIVE VOWELS: No Tehran vowel shift ... /q/ → [q] maintained
    (like Dari; more than Tehran). DISTINCTIVE: Cyrillic script with special
    letters (Ӣ=ī, Ӯ=ū, Қ=q, Ғ=ɣ, Ҷ=dʒ, Ҳ=h)." Perry (2005).
    """
    assert _bare("tg", "қалам").startswith("q")
    assert _bare("tg", "ғоз").startswith("ɣ")
    assert _bare("tg", "ҳаво").startswith("h")
    assert _bare("tg", "тоҷикӣ").startswith("todʒ")


def test_crh_latin_letter_values():
    """Crimean Tatar Latin: c=/dʒ/, ç=/tʃ/, ş=/ʃ/, j=/ʒ/, ğ=/ɣ/, h=/x/, ñ=/ŋ/, q=/q/.

    crh notes: "⟨c⟩=/dʒ/, ⟨ç⟩=/tʃ/, ⟨ş⟩=/ʃ/, ⟨j⟩=/ʒ/, ⟨ğ⟩=/ɣ/, ⟨h⟩=/x/, ⟨ñ⟩=/ŋ/,
    ⟨q⟩=/q/, ⟨ı⟩=/ɯ/."

    ⟨h⟩=/x/ and ⟨j⟩=/ʒ/ are what separate this spec from the Turkish norm it is
    otherwise modelled on.
    """
    assert _bare("crh", "cami").startswith("dʒ")
    assert _bare("crh", "çay").startswith("tʃ")
    assert _bare("crh", "han").startswith("x")
    assert _bare("crh", "jurnal").startswith("ʒ")
    assert _bare("crh", "ñe").startswith("ŋ")
    assert _bare("crh", "qırımtatar").startswith("qɯ")


def test_gag_tsedilla_letter():
    """⟨ţ⟩ = /ts/ in Romanian/Slavic loans; ⟨ä⟩ = /æ/.

    gag notes: "Written since 1996 in a 29-letter Latin alphabet modelled on
    Turkish, plus ⟨ä⟩, ⟨ê⟩ and ⟨ţ⟩ (the last used for /ts/ in Romanian/Slavic
    loans)."
    """
    assert _bare("gag", "ţar").startswith("ts")
    assert _bare("gag", "ä") == "æ"


@pytest.mark.xfail(
    strict=True,
    reason="gag notes claim /k ɡ/ front to [c ɟ] next to front vowels; engine "
    "produces [kim] and [ɡel] — no fronting rule exists in the spec, so the claim "
    "never fires",
)
def test_gag_velars_front_before_front_vowels():
    """Velars /k ɡ/ are fronted to [c ɟ] next to front vowels.

    gag notes: "Velars /k ɡ/ are fronted next to front vowels ([c ɟ])."

    kim and gel each place a velar immediately before a front vowel.
    """
    assert _bare("gag", "kim").startswith("c")
    assert _bare("gag", "gel").startswith("ɟ")


def test_tk_latin_letter_values():
    """Turkmen: ä=/æ/, ň=/ŋ/, ž=/ʒ/, w = labial-velar approximant.

    tk notes: "8-vowel system with vowel harmony. Ä = /æ/. Ň = /ŋ/. W is a labial-
    velar approximant. Ž = /ʒ/ for Russian loanwords."
    """
    assert _bare("tk", "äri").startswith("æ")
    assert _bare("tk", "ňe").startswith("ŋ")
    assert _bare("tk", "žurnal").startswith("ʒ")
    assert _bare("tk", "waka").startswith("w")


def test_tyv_grapheme_inventory_is_declared_empty():
    """Tuvan declares an empty grapheme map: nothing is transcribed.

    tyv notes: "GRAPHEME INVENTORY NOT YET SPECIFIED: a reliable spec must model
    the Cyrillic palatalisation/iotation conventions, vowel harmony, phonemic
    vowel length ... `graphemes` stays empty because none of that depends on the
    writing system."

    The spec declares the gap, so it is pinned rather than xfailed: the phoneme
    inventory exists, but no orthographic input yields output.
    """
    assert _t("tyv", "тыва") == ""
    assert _t("tyv", "дыл") == ""


# ===========================================================================
# Mongolic
# ===========================================================================


def test_xal_extended_cyrillic_letters():
    """Kalmyk: Җ = /d͡ʒ/, Ң = /ŋ/, Һ = /ɣ/, Ө = /ø/.

    xal notes: "written since 1938 in a Cyrillic alphabet: the Russian letters
    plus Әә /æ/, Өө /ø/, Үү /y/, Җҗ /d͡ʒ/, Ңң /ŋ/ and Һһ /ɣ/."
    """
    assert _bare("xal", "җаңһр").startswith("d͡ʒ")
    assert "ŋ" in _bare("xal", "җаңһр")
    assert _bare("xal", "һол").startswith("ɣ")
    assert _bare("xal", "үнн").startswith("y")


def test_xal_doubled_vowels_are_long():
    """Long vowels are written by doubling; the doubled digraph wins maximal munch.

    xal notes: "the Cyrillic orthography denotes long vowels by DOUBLING the vowel
    letter, so the doubled digraphs (аа әә ээ ии оо өө уу үү) are given as their
    own keys and win under maximal-munch matching."
    """
    assert _bare("xal", "өө") == "øː"


def test_xal_soft_sign_is_not_a_segment():
    """⟨ь⟩ is not mapped: palatalisation is under-specified, not invented.

    xal notes: "Most consonant letters also have palatalised realisations before
    front vowels / ⟨ь⟩; only the plain values are mapped here, so palatalisation
    is under-specified rather than invented. The soft sign ⟨ь⟩ and hard sign ⟨ъ⟩
    are NOT mapped."

    The declared omission is pinned: хальмг emits a plain [l] and no segment for
    ⟨ь⟩.
    """
    assert _bare("xal", "хальмг") == "xalmɡ"


def test_bxr_long_vowels_and_ai_sequences():
    """Doubled vowels are long, and ⟨ай ой үй⟩ are the long vowels [ɛː œː yː].

    bxr notes: "long vowels are written by DOUBLING the vowel letter (аа ээ ии оо
    өө уу үү) and the sequences ⟨ай ой үй⟩ are realised as the long vowels [ɛː œː
    yː]; all of these are given as multigraph keys and win under maximal-munch
    matching."
    """
    assert _bare("bxr", "өөр") == "oːr"
    assert _bare("bxr", "ай") == "ɛː"
    assert _bare("bxr", "үй") == "yː"


def test_bxr_h_letter_and_unmapped_russian_letters():
    """Һ = /h/; the loan-only letters (ф, к, п …) are deliberately unmapped.

    bxr notes: "written since 1939 in the Russian Cyrillic alphabet plus Өө, Үү
    and Һһ /h/. ... The letters в к п ф ц ч щ ъ are not used in native Buryat
    words and no source read here gives them a Buryat IPA value, so they are
    deliberately left unmapped."

    The declared omission is pinned rather than xfailed.
    """
    assert _bare("bxr", "һайн").startswith("h")
    assert _t("bxr", "ф") == ""


# ===========================================================================
# Caucasian
# ===========================================================================


def test_inh_multigraph_consonants():
    """Ingush digraphs/trigraph: кх=/q/, къ=/qʼ/, хь=/ħ/, хӏ=/h/, гӏ=/ʁ/, ӏ=/ʡ/, рхӏ=/r̥/.

    inh notes: "The orthography uses digraphs and one trigraph for the Nakh
    consonant inventory: ejectives пӏ тӏ кӏ цӏ чӏ, uvular кх /q/ and къ /qʼ/,
    pharyngeal хь /ħ/, laryngeal хӏ /h/, uvular fricative гӏ /ʁ/, the epiglottal
    stop ӏ /ʡ/, and рхӏ for the voiceless trill /r̥/; the engine matches these by
    maximal munch, so multigraphs win over their component letters."
    """
    assert _bare("inh", "кхы") == "q"
    assert _bare("inh", "къа").startswith("qʼ")
    assert _bare("inh", "хьа").startswith("ħ")
    assert _bare("inh", "хӏа").startswith("h")
    assert _bare("inh", "гӏалгӏай").startswith("ʁ")
    assert _bare("inh", "ӏа").startswith("ʡ")
    assert _bare("inh", "рхӏ") == "r̥"


def test_kbd_maximal_munch_prefers_the_longest_key():
    """кхъу beats кхъ beats къ under maximal munch.

    kbd notes: "each is a grapheme key of its own, matched by maximal munch
    (longest key wins, so кхъу beats кхъ beats къ)."

    кхъуэ takes the labialised uvular affricate, not къ + у.
    """
    assert _bare("kbd", "кхъуэ") == "q͡χʷa"
    assert _bare("kbd", "къэбэрдей").startswith("qa")


def test_kbd_vowel_letters():
    """⟨э⟩ = /a/, ⟨а⟩ = /aː/, ⟨ы⟩ = /ə/.

    kbd notes: "Phonemic vowels are ⟨э⟩ /a/, ⟨а⟩ /aː/, ⟨ы⟩ /ə/."

    адыгэбзэ carries all three: а=[aː], ы=[ə], э=[a].
    """
    assert _bare("kbd", "адыгэбзэ") == "aːdəɣabza"


def test_kbd_lateral_obstruents():
    """⟨лъ⟩ = /ɬ/, ⟨лӏ⟩ = /ɬʼ/, ⟨щӏ⟩ = /ɕʼ/.

    kbd notes: the digraphic series "гъ, гъу, къ, къу, кхъ, кхъу, кӏ, кӏу, лъ, лӏ,
    пӏ, тӏ, фӏ, хь, хъ, хъу, ху, цӏ, щӏ, ӏу — and each is a grapheme key of its
    own".

    лъы/лӏы is a minimal pair on ejection alone.
    """
    assert _bare("kbd", "лъы") == "ɬə"
    assert _bare("kbd", "лӏы") == "ɬʼə"
    assert _bare("kbd", "щӏы") == "ɕʼə"


def test_os_iron_sibilant_shifts():
    """Iron: ⟨с⟩ = [ʃ], ⟨з⟩ = [ʒ], ⟨ц⟩ = [s], ⟨дз⟩ = [z].

    os notes: "Note the Iron sound shifts the spelling preserves: ⟨с⟩ is [ʃ], ⟨з⟩
    is [ʒ], ⟨ц⟩ is [s] and ⟨дз⟩ is [z] in Iron (the Digor dialect keeps the
    sibilant/affricate values)."

    This is the claim that most distinguishes os from every other Cyrillic spec:
    the letters that spell /s z ts/ elsewhere spell /ʃ ʒ s/ here.
    """
    assert _bare("os", "сау").startswith("ʃ")
    assert _bare("os", "заз") == "ʒaʒ"
    assert _bare("os", "цӕуын").startswith("s")
    assert _bare("os", "дзурын").startswith("z")


def test_os_ae_and_uvulars():
    """⟨ӕ⟩ = /ɐ/; ⟨хъ⟩ = /q/ and ⟨гъ⟩ = /ʁ/.

    os notes: "The alphabet extends Russian Cyrillic with ⟨ӕ⟩ /ɐ/, the ejective
    digraphs ⟨къ пъ тъ цъ чъ⟩, the uvulars ⟨хъ⟩ /q/ and ⟨гъ⟩ /ʁ/."
    """
    assert _bare("os", "ӕвзаг").startswith("ɐ")
    assert _bare("os", "хъӕу").startswith("q")
    assert _bare("os", "гъе").startswith("ʁ")


def test_lez_aspiration_is_first_candidate():
    """Aspiration is phonemic but unwritten, so ⟨к п т ц ч⟩ are aspirated-first.

    lez notes: "Aspiration is phonemic but NOT written, so к п т ц ч are given
    aspirated-first with the unaspirated variant as a second candidate; this
    ambiguity cannot be resolved from the orthography alone."

    The spec declares the ambiguity, so the declared preference is pinned: the
    single best transcription of кар takes the aspirated [kʰ].
    """
    assert _bare("lez", "кар") == "kʰar"


def test_lez_uvular_and_front_vowel_multigraphs():
    """⟨къ⟩=/q/, ⟨кь⟩=/qʼ/, ⟨хъ⟩=/qʰ/, ⟨гь⟩=/h/, ⟨хь⟩=/x/, ⟨уь⟩=/y/, ⟨чӏ⟩=/t͡ʃʼ/.

    lez notes: "Multigraphs carry the ejective, uvular and front-vowel series — кӏ
    пӏ тӏ цӏ чӏ (ejectives), къ /q/, кь /qʼ/, хъ /qʰ/, гъ /ʁ/, гь /h/, хь /x/, уь
    /y/ — and are matched by maximal munch, so they win over their component
    letters; ь never occurs alone."

    къал/кьил is the minimal pair that separates plain uvular from ejective.
    """
    assert _bare("lez", "къал").startswith("q")
    assert _bare("lez", "кьил").startswith("qʼ")
    assert _bare("lez", "хъвер").startswith("qʰ")
    assert _bare("lez", "гьар").startswith("h")
    assert _bare("lez", "хьун").startswith("x")
    assert _bare("lez", "уьл").startswith("y")
    assert _bare("lez", "чӏал").startswith("t͡ʃʼ")


def test_av_doubled_letters_are_fortis():
    """Doubled letters mark the fortis (geminate) series.

    av notes: "Cyrillic alphabet since 1938; digraphs with ⟨ъ⟩, ⟨ь⟩ and the
    palochka ⟨ӏ⟩ mark uvulars, laterals and ejectives, and doubled letters mark
    the fortis (geminate) series."

    ччугӏа and ххинкӏал each isolate a fortis consonant, marked with the length
    diacritic; the ejective кӏ in the same word stays plain-length.
    """
    assert _bare("av", "ччугӏа").startswith("t͡ʃː")
    assert _bare("av", "ххинкӏал").startswith("χː")


def test_av_palochka_and_digraph_series():
    """⟨гь⟩ = /h/, ⟨лъ⟩ = /ɬ/, ⟨кӏ⟩ = /kʼ/, ⟨цӏ⟩ = /t͡sʼ/.

    av notes: "digraphs with ⟨ъ⟩, ⟨ь⟩ and the palochka ⟨ӏ⟩ mark uvulars, laterals
    and ejectives."
    """
    assert _bare("av", "гьан").startswith("h")
    assert _bare("av", "лъим").startswith("ɬ")
    assert _bare("av", "кӏал").startswith("kʼ")
    assert _bare("av", "мацӏ").endswith("t͡sʼ")


def test_ab_modifier_letters_form_digraphs():
    """⟨ь⟩ palatalises and ⟨ә⟩ labialises the preceding base letter.

    ab notes: "The orthography is heavily DIGRAPHIC: the modifier letters ⟨ь⟩
    (palatalisation) and ⟨ә⟩ U+04D9 (labialisation) combine with a base consonant
    to spell a distinct phoneme (гь /ɡʲ/, гә /ɡʷ/, шь /ʃ/, шә /ʃʷ/, ҟә /qʷʼ/ …),
    so every such digraph is listed as its own grapheme key and is matched by
    maximal munch ahead of the bare letter."

    гьы/гәы is the minimal pair: the same base ⟨г⟩, two different modifiers.
    """
    assert _bare("ab", "гьы") == "ɡʲɨ"
    assert _bare("ab", "гәы") == "ɡʷɨ"
    assert _bare("ab", "шьы") == "ʃɨ"
    assert _bare("ab", "шәы") == "ʃʷɨ"
    assert _bare("ab", "ҟәы") == "qʷʼɨ"


def test_ab_two_phonemic_vowels():
    """Only /ɑ/ and /ɨ/ are phonemic; ⟨ы⟩ is [ɨ] and ⟨а⟩ is [ɑ].

    ab notes: "Only two vowels are phonemic, /ɑ/ and /ɨ/; ⟨е о и у⟩ historically
    represent /ɑj ɑw jɨ wɨ/ sequences and are mapped to their surface values."

    аԥсшәа carries the /ɑ/ at both edges; the digraph tests above carry the /ɨ/.
    """
    out = _bare("ab", "аԥсшәа")
    assert out.startswith("ɑ") and out.endswith("ɑ")


# ===========================================================================
# din — Dinka (Rek standard orthography)
# ===========================================================================


def test_din_h_marks_the_dental_series():
    """⟨th dh nh⟩ are dental STOPS, not fricatives.

    din notes: "DENTAL vs ALVEOLAR: a following ⟨h⟩ marks the dental series —
    ⟨th⟩ = /t̪/, ⟨dh⟩ = /d̪/, ⟨nh⟩ = /n̪/. These are STOPS, not fricatives: Dinka
    has no fricatives other than /ɣ/. ⟨h⟩ occurs only in these digraphs."
    """
    assert _bare("din", "thuɔŋjäŋ").startswith("t̪")
    assert _bare("din", "dhien").startswith("d̪")
    assert _bare("din", "nhom").startswith("n̪")


def test_din_diaeresis_marks_breathy_voice():
    """The diaeresis marks the breathy-voice vowel series.

    din notes: "the DIAERESIS marks the breathy-voice series, transcribed here
    with the IPA breathy-voice diacritic (⟨ä⟩ = /a̤/, ⟨ë⟩ = /e̤/, ⟨ɛ̈⟩ = /ɛ̤/, ⟨ï⟩ =
    /i̤/, ⟨ö⟩ = /o̤/, ⟨ɔ̈⟩ = /ɔ̤/)."

    thuɔŋjäŋ contrasts the plain ⟨ɔ⟩ with the breathy ⟨ä⟩ inside one word.
    """
    out = _bare("din", "thuɔŋjäŋ")
    assert "a̤" in out
    assert "ɔ̤" not in out


def test_din_doubled_vowels_are_long():
    """Length is written by doubling the vowel letter.

    din notes: "LENGTH: written by DOUBLING the vowel letter (⟨aa⟩ = /aː/, e.g.
    baai 'home')."

    baai is the cited word.
    """
    assert _bare("din", "baai") == "baːi"


def test_din_tone_is_not_emitted():
    """Lexical tone is not written and is therefore not emitted.

    din notes: "LEXICAL TONE (and the tonal morphology of number/case marking) is
    NOT written in the standard orthography and is therefore NOT recoverable; no
    tone is emitted."

    The spec declares this gap, so it is pinned: no tone letters or accents appear.
    """
    out = _t("din", "raan")
    assert out == "ɾaːn"
    assert not any(c in out for c in "˥˦˧˨˩́̀̂̌")


# ===========================================================================
# xib — Iberian
# ===========================================================================


def test_xib_two_sibilants_and_two_rhotics():
    """Iberian contrasts /s/ vs /ś/ and /r/ vs /ŕ/.

    xib notes: "Phonological system inferred from writing: 5 vowels, two sibilants
    /s/ vs /ś/, two rhotics /r/ vs /ŕ/ (paralleling Basque)."

    Both contrasts are held apart in the output: ⟨s⟩/⟨ś⟩ → [s]/[ʃ] and ⟨r⟩/⟨ŕ⟩ →
    [ɾ]/[r].
    """
    assert _bare("xib", "s") == "s"
    assert _bare("xib", "ś") == "ʃ"
    assert _bare("xib", "bar") == "baɾ"
    assert _bare("xib", "baŕ") == "bar"
