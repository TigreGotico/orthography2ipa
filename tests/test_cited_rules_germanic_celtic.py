"""Cited-rule conformance: Germanic (minus en-GB/de-DE), Celtic and Greek.

Each test takes one cited claim from a spec's ``notes`` prose or from a single
rule entry, quotes it with its citation, and proves the engine honours it on a
real word — isolating the rule to a single segment and pinning the complementary
environment with a minimal pair wherever the phonology allows one. For dialect
specs the pair is the same word under the dialect and under its parent, so only
the declared delta is under test.

Claims the engine does NOT honour are marked ``xfail(strict=True)`` with the
actual output in the reason, never weakened to match. Claims a spec honestly
declares it does not model are pinned with a passing test.

en-GB and de-DE are covered in ``test_cited_rules_germanic.py``; the cited
claims of da / sv / nb are covered in ``test_scandinavian.py``.
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(code, word):
    return G2P(code).transcribe_word(word)


def _bare(code, word):
    """Transcription without the primary-stress mark."""
    return _t(code, word).replace("ˈ", "")


# ===========================================================================
# nl / nl-NL / nl-BE — Dutch
# ===========================================================================


def test_nl_final_devoicing():
    """FINAL DEVOICING: b/d/g/v/z devoiced in coda and word-finally.

    nl notes: "FINAL DEVOICING: b/d/g/v/z devoiced in coda and word-finally."
    Sources: van Oostendorp (2000), Gussenhoven (1992), Booij (1995).

    Minimal pair on the same ⟨d⟩: hond (word-final → [t]) vs honden (the same
    ⟨d⟩ now medial, staying [d]).
    """
    assert _t("nl", "hond").endswith("t")
    assert "nd" in _t("nl", "honden")


def test_nl_g_onset_voiced_coda_voiceless():
    """G: voiced [ɣ] in the onset, voiceless [x] in the coda — northern Dutch.

    nl notes: "G: voiced [ɣ] onset, voiceless [x] coda — northern Dutch."
    Booij (1995).

    Minimal pair on ⟨g⟩ alone: gaan (onset) vs dag (coda).
    """
    assert _t("nl", "gaan").startswith("ɣ")
    assert _t("nl", "dag").endswith("x")


def test_nl_h_is_breathy():
    """H: breathy voiced [ɦ], not [h].

    nl notes: "H: breathy [ɦ]; fully silent in southern dialects."
    van Oostendorp (2000).
    """
    assert _t("nl", "huis").startswith("ɦ")


def test_nl_nl_northern_g_is_voiced_fricative():
    """⟨g⟩ is [ɣ] in northern NL.

    nl-NL notes: "⟨g⟩ realisation is [ɣ] in northern NL and [x] in southern NL /
    Flanders." Source: Booij, G. (1995). The Phonology of Dutch; Gussenhoven, C.
    (1999).
    """
    assert _t("nl-NL", "goed").startswith("ɣ")


def test_nl_nl_final_devoicing():
    """Final obstruent devoicing, same as German Auslautverhärtung.

    nl-NL notes: "Final obstruent devoicing (same as German Auslautverhärtung)."
    Booij (1995).
    """
    assert _t("nl-NL", "goed").endswith("t")


@pytest.mark.xfail(
    strict=True,
    reason="⟨g⟩ is claimed to be [x] in Flanders; nl-BE produces [ɣuːt] for goed "
    "— the Flemish spec inherits the northern voiced [ɣ] unchanged",
)
def test_nl_be_flemish_g_is_voiceless():
    """⟨g⟩ is [x] in southern NL / Flanders.

    nl notes: "⟨g⟩ realisation is [ɣ] in northern NL and [x] in southern NL /
    Flanders." Booij (1995).

    nl-BE is the Flemish spec, so the same ⟨g⟩ that is [ɣ] in nl-NL must be [x].
    """
    assert _t("nl-BE", "goed").startswith("x")


def test_nl_be_alveolar_r():
    """Alveolar /r/ [r] in most Flemish varieties.

    nl-BE notes: "Alveolar /r/ [r] in most varieties (vs. NL uvular [ʀ])."
    Source: König & van der Auwera (1994).
    """
    assert _t("nl-BE", "rood").startswith("r")


# ===========================================================================
# af — Afrikaans
# ===========================================================================


def test_af_initial_v_is_f():
    """DEFINING CHANGE (1): /v/ → /f/ word-initially.

    af notes: "DEFINING CHANGES from Dutch: (1) /v/→/f/ word-initially."
    Source: Donaldson (1993).

    Minimal pair against the Dutch ancestor: Dutch keeps ⟨v⟩-initial voicing
    where Afrikaans devoices it.
    """
    assert _t("af", "vier").startswith("f")


def test_af_new_diphthong_oey():
    """DEFINING CHANGE (5): the new diphthong /œɪ/ (Dutch /œy/).

    af notes: "(5) New diphthong /œɪ/ (Dutch /œy/)." Donaldson (1993).

    Minimal pair on ⟨ui⟩: af huis [ɦœɪs] vs nl huis [ɦœys].
    """
    assert "œɪ" in _t("af", "huis")
    assert "œy" in _t("nl", "huis")


@pytest.mark.xfail(
    strict=True,
    reason="Donaldson (1993) claims initial /ɡ/ (Dutch ɣ→ɡ); engine produces "
    "[xud] for goed and [xaːn] for gaan — the fricative is kept, not stopped",
)
def test_af_initial_g_is_a_stop():
    """DEFINING CHANGE (2): /ɡ/ initial (Dutch ɣ → ɡ).

    af notes: "(2) /ɡ/ initial (Dutch ɣ→ɡ)." Source: Donaldson (1993).

    Isolated on the initial ⟨g⟩ only, against the Dutch ancestor's [ɣ].
    """
    assert _t("af", "goed").startswith("ɡ")


@pytest.mark.xfail(
    strict=True,
    reason="Donaldson (1993) claims /r/ = uvular [ʀ] or [χ]; engine produces "
    "[roːɪ] for rooi — the alveolar trill inherited from Dutch",
)
def test_af_uvular_r():
    """DEFINING CHANGE (4): /r/ = uvular [ʀ] or [χ].

    af notes: "(4) /r/ = uvular [ʀ] or [χ]." Source: Donaldson (1993).
    """
    out = _t("af", "rooi")
    assert out.startswith("ʀ") or out.startswith("χ")


# ===========================================================================
# de-AT / de-CH / de-x-bavarian — German varieties
# ===========================================================================


@pytest.mark.xfail(
    strict=True,
    reason="Dudenredaktion (2015) claims Austrian ä merges with /eː/; de-AT "
    "produces [bɛʁ] for Bär — identical to the de-DE parent, so the declared "
    "delta is absent from the spec",
)
def test_de_at_ae_raises_to_long_e():
    """ä [ɛ] → [eː] in most Austrian German (merged with /eː/).

    de-AT notes: "ä [ɛ] → [eː] in most Austrian (merged with e:)."
    Source: Dudenredaktion (2015).

    Isolated on the ⟨ä⟩ nucleus: de-DE Bär is [bɛʁ], so Austrian must differ
    exactly here and nowhere else.
    """
    assert "eː" in _t("de-AT", "Bär")
    assert "ɛ" in _t("de-DE", "Bär")


def test_de_ch_no_glottal_stop():
    """NO glottal stop /ʔ/ — absent from Swiss German phonology.

    de-CH notes: "NO glottal stop /ʔ/ — absent from Swiss German phonology."
    Source: König & van der Auwera (1994).

    A declared absence, pinned on a vowel-initial word where Standard German
    would insert one.
    """
    assert "ʔ" not in _t("de-CH", "Abend")


@pytest.mark.xfail(
    strict=True,
    reason="König & van der Auwera (1994) claim Swiss /r/ = alveolar trill [r]; "
    "de-CH produces [ʁɔt] for rot — the uvular fricative inherited from de-DE",
)
def test_de_ch_alveolar_trill_r():
    """/r/ = alveolar trill [r], vs Standard German uvular [ʀ].

    de-CH notes: "/r/ = alveolar trill [r] (vs. Standard German uvular [ʀ])."
    Source: König & van der Auwera (1994).

    Isolated on the onset ⟨r⟩ of one word, against the de-DE parent's [ʁ].
    """
    assert _t("de-CH", "rot").startswith("r")


def test_de_bavarian_pf_cluster_preserved():
    """pf- cluster fully preserved.

    de-x-bavarian notes: "pf- cluster fully preserved."
    Source: König & van der Auwera (1994).
    """
    assert _t("de-x-bavarian", "Pfand").startswith("pf")


@pytest.mark.xfail(
    strict=True,
    reason="König & van der Auwera (1994) claim r-vocalisation to [ɐ] before a "
    "consonant; de-x-bavarian produces [vɔʁt] for Wort — the consonantal [ʁ] is "
    "kept",
)
def test_de_bavarian_r_vocalisation_before_consonant():
    """r-vocalisation [ɐ] before consonants is common.

    de-x-bavarian notes: "r-vocalisation [ɐ] before consonants common."
    Source: König & van der Auwera (1994).

    Isolated on the pre-consonantal ⟨r⟩ of Wort, where the onset ⟨r⟩ of a word
    like rot is untouched by the rule.
    """
    assert "ɐ" in _t("de-x-bavarian", "Wort")


# ===========================================================================
# sv-FI / sv-x-rikssvenska / sv-x-skanska — Swedish varieties
# ===========================================================================


def test_sv_fi_no_tonal_accent():
    """NO TONAL ACCENT in Finland-Swedish.

    sv-FI notes: "NO TONAL ACCENT (Finnish influence — Finnish has no pitch
    accent)." Source: Elert (1994).

    A declared absence: no accent-1/accent-2 mark may appear.
    """
    out = _t("sv-FI", "anden")
    assert "¹" not in out and "²" not in out


@pytest.mark.xfail(
    strict=True,
    reason="Elert (1994) claims Finland-Swedish has NO retroflexion; sv-FI "
    "produces [baɳ] for barn — the retroflex series is inherited from sv "
    "unchanged",
)
def test_sv_fi_no_retroflexion():
    """NO RETROFLEXION: alveolar r always; no ɳ ɖ ʈ ʂ clusters.

    sv-FI notes: "NO RETROFLEXION (alveolar r always; no ɳ ɖ ʈ ʂ clusters)."
    Source: Elert (1994).

    Isolated on the ⟨rn⟩ cluster: mainland sv barn is [bɑːɳ], so Finland-Swedish
    must keep [rn] here.
    """
    assert "ɳ" not in _t("sv-FI", "barn")


@pytest.mark.xfail(
    strict=True,
    reason="Elert (1994) claims the Finland-Swedish sj-sound is [ʃ] or [sk], not "
    "the mainland [ɧ]; sv-FI produces [ɧœ] for sjö",
)
def test_sv_fi_sj_sound_is_not_the_mainland_sound():
    """sj-sound = [ʃ] or [sk], not the mainland [ɧ].

    sv-FI notes: "sj-sound = [ʃ] or [sk] (not the mainland [ɧ])."
    Source: Elert (1994).

    Isolated on ⟨sj⟩: mainland sv sjö is [ɧøː].
    """
    assert "ɧ" not in _t("sv-FI", "sjö")


def test_sv_rikssvenska_retroflexion():
    """RETROFLEXION: rn rd rt rs → ɳ ɖ ʈ ʂ (Central Swedish).

    sv-x-rikssvenska notes: "RETROFLEXION: rn rd rt rs → ɳ ɖ ʈ ʂ (Central
    Swedish)." Source: Elert (1994), Wells (1982).

    Isolated on the coda cluster: ⟨rn⟩ → [ɳ], ⟨rs⟩ → [ʂ].
    """
    assert "ɳ" in _t("sv-x-rikssvenska", "barn")
    assert _t("sv-x-rikssvenska", "fars").endswith("ʂ")


def test_sv_rikssvenska_sj_sound():
    """/ɧ/ (sj-sound) is realised as [ɧ].

    sv-x-rikssvenska notes: "/ɧ/ (sj-sound): the most debated phoneme in Swedish;
    realised as [ɧ], [ʃ], [ɕ], or [x] depending on speaker/region."
    Source: Elert (1994).
    """
    assert _t("sv-x-rikssvenska", "sjö").startswith("ˈɧ")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982), Elert (1994) claim Scanian /r/ is uvular [ʀ]/[ʁ]; "
    "sv-x-skanska produces [rɔt] for rot — the alveolar trill inherited from sv",
)
def test_sv_skanska_uvular_r():
    """UVULAR /r/ [ʀ] or [ʁ] — shared with Danish.

    sv-x-skanska notes: "UVULAR /r/ [ʀ] or [ʁ] — shared with Danish (historical
    Danish territory)." Source: Wells (1982), Elert (1994).

    Isolated on the onset ⟨r⟩, against mainland sv's alveolar [r].
    """
    out = _t("sv-x-skanska", "rot")
    assert out.startswith("ʀ") or out.startswith("ʁ")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982), Elert (1994) claim Scanian has no retroflexion because "
    "the uvular r cannot trigger it; sv-x-skanska produces [baɳ] for barn",
)
def test_sv_skanska_no_retroflexion():
    """No retroflexion — the uvular r does not trigger it.

    sv-x-skanska notes: "No retroflexion (uvular r doesn't trigger it)."
    Source: Wells (1982), Elert (1994).

    The consequence of the uvular-r claim above, isolated on ⟨rn⟩.
    """
    assert "ɳ" not in _t("sv-x-skanska", "barn")


# ===========================================================================
# da-x-copenhagen — Copenhagen Danish
# ===========================================================================


@pytest.mark.xfail(
    strict=True,
    reason="Grønnum (1998) claims stød on sonorant-final syllables, hund "
    "[hɔnˀ]; da-x-copenhagen produces [hun] — stød is suprasegmental and the da "
    "parent explicitly does not encode it",
)
def test_da_cph_stod():
    """STØD: glottalisation on etymologically long vowels and sonorant-final syllables.

    da-x-copenhagen notes: "STØD: glottalisation / laryngealisation on
    etymologically long vowels and sonorant-final syllables — replaces the Nordic
    pitch accent ... hund [hɔnˀ]." Source: Grønnum (1998).

    Isolated on the very word the citation transcribes.
    """
    assert "ˀ" in _t("da-x-copenhagen", "hund")


@pytest.mark.xfail(
    strict=True,
    reason="Grønnum (1998) claims the Copenhagen soft d is the very weak "
    "approximant [ð̞], bide [ˈb̥iˀð̞ə]; da-x-copenhagen produces [biðɛ] — the "
    "plain [ð] inherited from da",
)
def test_da_cph_soft_d_is_weak_approximant():
    """SOFT D: /d/ → [ð̞] (very weak approximant) in common words.

    da-x-copenhagen notes: "SOFT D: /d/ → [ð̞] (very weak approximant, almost
    zero) in common words: bide [ˈb̥iˀð̞ə]." Source: Grønnum (1998).
    """
    assert "ð̞" in _t("da-x-copenhagen", "bide")


@pytest.mark.xfail(
    strict=True,
    reason="Grønnum (1998) claims /r/ → [ɐ] before consonants; "
    "da-x-copenhagen produces [kɔʁt] for kort — the consonantal uvular [ʁ] "
    "inherited from da, whose notes state coda r-vocalisation is not encoded",
)
def test_da_cph_r_vocalisation_before_consonant():
    """/r/ → [ɐ] before consonants; often deleted.

    da-x-copenhagen notes: "/r/ → [ɐ] before consonants; often deleted."
    Source: Grønnum (1998).

    Isolated on the pre-consonantal ⟨r⟩ of kort; the onset ⟨r⟩ is not affected.
    """
    assert "ɐ" in _t("da-x-copenhagen", "kort")


# ===========================================================================
# nn — Norwegian Nynorsk
# ===========================================================================


def test_nn_old_norse_diphthongs_preserved():
    """More diphthongs preserved from Old Norse: ei, au, øy.

    nn notes: "More diphthongs preserved from Old Norse: ei, au, øy."
    Source: Kristoffersen (2000).

    Each of the three digraphs must surface as a two-target nucleus, not a
    monophthong.
    """
    assert "æi" in _t("nn", "stein")
    assert "æʉ" in _t("nn", "auge")
    assert "øy" in _t("nn", "øy")


@pytest.mark.xfail(
    strict=True,
    reason="Kristoffersen (2000) claims Nynorsk/western /r/ is the alveolar trill "
    "[r]; nn produces [ɾɔt] for rot — the tap inherited from the nb-type spec",
)
def test_nn_alveolar_trill_r():
    """Alveolar /r/ [r].

    nn notes: "Alveolar /r/ [r]; less retroflexion than Bokmål/Eastern."
    Source: Kristoffersen (2000).

    Isolated on the onset ⟨r⟩; nb explicitly calls the tap [ɾ] one realisation of
    its /r/, so a distinct trill is the declared Nynorsk delta.
    """
    assert _t("nn", "rot").startswith("r")


# ===========================================================================
# is — Icelandic
# ===========================================================================


def test_is_voiceless_sonorants():
    """UNIQUE: voiceless sonorants — hl [l̥], hn [n̥], hr [r̥].

    is notes: "UNIQUE: Voiceless sonorants — hl [l̥], hn [n̥], hr [r̥]."
    Source: Árnason (2011).
    """
    assert _bare("is", "hlaupa").startswith("l̥")
    assert _bare("is", "hnífur").startswith("n̥")
    assert _bare("is", "hringur").startswith("r̥")


def test_is_preaspiration():
    """PREASPIRATION: ⟨pp tt kk⟩ = [ʰp ʰt ʰk].

    is notes: "PREASPIRATION: ⟨pp tt kk⟩ = [ʰp ʰt ʰk]." Source: Árnason (2011).

    Minimal pair on ⟨pp⟩ vs a single ⟨p⟩: uppi is preaspirated, the singleton is
    not.
    """
    assert "ʰp" in _bare("is", "uppi")
    assert "ʰt" in _bare("is", "katt")


def test_is_u_is_front_rounded():
    """⟨u⟩ = [ʏ] (front rounded).

    is notes: "⟨u⟩ = [ʏ] (front rounded!)." Source: Árnason (2011).
    """
    assert "ʏ" in _bare("is", "hnífur")


def test_is_a_acute_and_au():
    """⟨á⟩ = [au]; ⟨au⟩ = [øɪ].

    is notes: "⟨á⟩ = [au]; ⟨au⟩ = [øɪ]." Source: Árnason (2011).

    The two are a near-minimal pair: the same two letters in the opposite roles.
    """
    assert "au" in _bare("is", "áfram")
    assert "øɪ" in _bare("is", "auga")


def test_is_thorn_and_eth_preserved():
    """PRESERVED: thorn þ [θ] and eth ð [ð].

    is notes: "PRESERVED: ... thorn þ [θ] and eth ð [ð]." Source: Árnason (2011).
    """
    assert _bare("is", "þing").startswith("θ")


def test_is_no_stod_no_tonal_accent():
    """No stød, no tonal accent.

    is notes: "No stød, no tonal accent." Source: Árnason (2011).

    A declared absence, pinned against the Danish stød mark and the
    Swedish/Norwegian accent marks.
    """
    out = _t("is", "dagur")
    assert "ˀ" not in out and "¹" not in out and "²" not in out


def test_is_initial_stress():
    """Icelandic has categorical initial stress.

    is `stress` notes: "Icelandic has categorical initial stress. Accent letters
    (á é í ó ú ý ö) mark vowel quality, not stress placement."
    Source: Einarsson (1945).

    The second clause is the falsifiable half: ⟨á⟩ in a non-initial syllable must
    not attract the stress mark.
    """
    assert _t("is", "dagur").startswith("ˈ")
    assert _t("is", "áfram").startswith("ˈ")


# ===========================================================================
# fo — Faroese
# ===========================================================================


def test_fo_a_acute_differs_from_icelandic():
    """⟨á⟩ = [ɔa] (cf. Icelandic á = [au]).

    fo notes: "⟨á⟩ = [ɔa] (cf. Icelandic á = [au])."
    Source: Árnason (2011), Hanssen (2010).

    The citation states the contrast itself, so the minimal pair is the same
    letter under fo and under is.
    """
    assert "ɔa" in _t("fo", "ár")
    assert "au" in _bare("is", "áfram")


def test_fo_eth_weakens_between_vowels():
    """⟨ð⟩ → [j] or [∅] between vowels (weakening).

    fo notes: "⟨ð⟩ → [j] or [∅] between vowels (weakening)."
    Source: Árnason (2011).

    Minimal pair against Icelandic, which preserves the interdental: fo hlaða has
    no [ð] at all where Icelandic ⟨ð⟩ is [ð].
    """
    assert "ð" not in _t("fo", "hlaða")


def test_fo_preaspiration():
    """Preaspiration present (⟨pp tt kk⟩ = [ʰp ʰt ʰk]).

    fo notes: "Preaspiration present (⟨pp tt kk⟩ = [ʰp ʰt ʰk])."
    Source: Árnason (2011).
    """
    assert "ʰp" in _t("fo", "uppi")
    assert "ʰt" in _t("fo", "gott")


def test_fo_no_voiceless_sonorants():
    """No voiceless sonorants (unlike Icelandic).

    fo notes: "No voiceless sonorants (unlike Icelandic)."
    Source: Árnason (2011).

    A declared absence, and the exact contrast the citation draws: fo hlaða keeps
    [hl], where Icelandic ⟨hl⟩ is [l̥].
    """
    assert "l̥" not in _t("fo", "hlaða")
    assert _t("fo", "hlaða").startswith("hl")


@pytest.mark.xfail(
    strict=True,
    reason="Árnason (2011), Hanssen (2010) claim ⟨g⟩ → [w] before back vowels and "
    "[j] elsewhere; fo produces [ɡʊlʊr] for gulur and [ɡera] for gera — the plain "
    "stop in both environments",
)
def test_fo_g_glides():
    """⟨g⟩ → [w] before back vowels, [j] elsewhere.

    fo notes: "⟨g⟩ → [w] before back vowels, [j] elsewhere."
    Source: Árnason (2011), Hanssen (2010).

    Minimal pair on the same ⟨g⟩: before back ⟨u⟩ vs before front ⟨e⟩.
    """
    assert _t("fo", "gulur").startswith("w")
    assert _t("fo", "gera").startswith("j")


# ===========================================================================
# fy — West Frisian
# ===========================================================================


def test_fy_breaking_diphthongs():
    """KEY FEATURE (1): BREAKING DIPHTHONGS /iə/, /ɪə/, /oə/.

    fy notes: "(1) BREAKING DIPHTHONGS: distinctive centring diphthongs /iə/,
    /ɪə/, /oə/ from historical long vowels — a hallmark of Frisian."
    Sources: Tiersma (1999), Popkema (2006).
    """
    assert "iə" in _t("fy", "hier")
    assert "ɪə" in _t("fy", "gean")
    assert "oə" in _t("fy", "doar")


def test_fy_final_devoicing():
    """KEY FEATURE (2): FINAL DEVOICING of voiced obstruents.

    fy notes: "(2) FINAL DEVOICING: voiced obstruents devoiced word-finally and in
    coda, as in Dutch." Source: Tiersma (1999).
    """
    assert _t("fy", "tiid").endswith("t")


def test_fy_onset_g_is_a_stop():
    """KEY FEATURE (3): /ɡ/ not /ɣ/ in the onset.

    fy notes: "(3) /ɡ/ not /ɣ/: West Frisian has a voiced stop /ɡ/ in onset (not
    the fricative [ɣ] of Dutch)." Source: Tiersma (1999).

    The contrast the citation draws: fy goed [ɡ] vs nl goed [ɣ].
    """
    assert _t("fy", "goed").lstrip("ˈˌ").startswith("ɡ")
    assert _t("nl", "goed").lstrip("ˈˌ").startswith("ɣ")


def test_fy_circumflex_a_e_o():
    """KEY FEATURE (4): ⟨â⟩ /ɔː/, ⟨ê⟩ /ɛː/, ⟨ô⟩ /oː/.

    fy notes: "(4) CIRCUMFLEX VOWELS: ⟨â⟩ /ɔː/, ⟨ê⟩ /ɛː/, ⟨ô⟩ /oː/, ⟨û⟩ /yː/ —
    unique orthographic convention." Source: Popkema (2006).
    """
    assert "ɔː" in _t("fy", "hân")
    assert "ɛː" in _t("fy", "nêst")
    assert "oː" in _t("fy", "hôf")


@pytest.mark.xfail(
    strict=True,
    reason="Popkema (2006) claims ⟨û⟩ = /yː/; fy produces [huːs] for hûs — the "
    "back rounded [uː], so the circumflex-⟨u⟩ grapheme is not front-rounded",
)
def test_fy_circumflex_u_is_front_rounded():
    """KEY FEATURE (4): ⟨û⟩ /yː/.

    fy notes: "(4) CIRCUMFLEX VOWELS: ⟨â⟩ /ɔː/, ⟨ê⟩ /ɛː/, ⟨ô⟩ /oː/, ⟨û⟩ /yː/."
    Source: Popkema (2006).

    Isolated on the one grapheme: the other three circumflex vowels do resolve as
    the citation says.
    """
    assert "yː" in _t("fy", "hûs")


def test_fy_y_is_a_vowel():
    """KEY FEATURE (5): ⟨y⟩ = /i/ (not a consonant).

    fy notes: "(5) ⟨y⟩ = /i/ (not a consonant)." Source: Tiersma (1999).
    """
    assert _t("fy", "by").endswith("i")


# ===========================================================================
# nds — Low German
# ===========================================================================


def test_nds_no_high_german_consonant_shift():
    """DID NOT UNDERGO the High German Consonant Shift.

    nds notes: "DID NOT UNDERGO the High German Consonant Shift: maken vs. German
    machen; water vs. German Wasser." Source: Gallée (1993), Robinson (1992).

    Isolated on the single shifted segment of each word the citation names: the
    intervocalic ⟨k⟩ stays [k] (not [x]) and the intervocalic ⟨t⟩ stays [t] (not
    [s]).
    """
    assert "k" in _t("nds", "maken") and "x" not in _t("nds", "maken")
    assert "t" in _t("nds", "water")


def test_nds_g_allophony():
    """G ALLOPHONY: word-initial [ɡ], intervocalic [ɣ], coda/word-final [x].

    nds notes: "G ALLOPHONY: word-initial [ɡ], intervocalic [ɣ], coda/word-final
    [x] or [ç] (front vowel context)." Source: Gallée (1993).

    A three-way isolation of the same letter, conditioned solely on position.
    """
    assert _t("nds", "gaan").startswith("ɡ")
    assert "ɣ" in _t("nds", "regen")
    assert _t("nds", "weg").endswith("x")


# ===========================================================================
# li — Limburgish
# ===========================================================================


def test_li_mouillering_j_digraphs():
    """Mouillering is written with the ⟨j⟩ digraphs (tj, dj, sj, zj, nj, lj).

    li notes: "Mouillering is written with the <j> digraphs (tj, dj, sj, zj, nj,
    lj)." Commitment: Spelling 2003 voor de Limburgse dialecten (Veldekespelling),
    Raod veur 't Limburgs.

    Each digraph must be one palatal/postalveolar segment, not a consonant plus a
    [j] glide.
    """
    assert _t("li", "sjoon").startswith("ʃ")
    assert _t("li", "zjoon").startswith("ʒ")
    assert _t("li", "tjeun").startswith("tʃ")
    assert _t("li", "djoon").startswith("dʒ")
    assert _t("li", "njoon").startswith("ɲ")
    assert _t("li", "ljoon").startswith("ʎ")


def test_li_tone_is_not_emitted():
    """TONE IS NOT REPRESENTED: no tonal information is emitted.

    li notes: "TONE IS NOT REPRESENTED: Limburgish contrasts sleeptoon (dragging
    tone, Accent 1) with stoottoon (push tone, Accent 2); Spelling 2003 does not
    write the contrast, so no tonal information can be recovered from the
    orthography and none is emitted."

    A declared omission, pinned so no tone mark can appear by accident.
    """
    out = _t("li", "haas")
    assert not any(c in out for c in "˥˦˧˨˩¹²ˊˋ")


# ===========================================================================
# zea — Zeelandic
# ===========================================================================


def test_zea_is_a_declared_stub():
    """STUB (deliberate): the grapheme inventory of Zeelandic is NOT specified.

    zea notes: "STUB (deliberate): the grapheme inventory of Zeelandic is NOT
    specified ... No source consulted gives a letter->IPA table ... A defensible
    spec must first pick ONE variety (e.g. Walcheren) and cite a dialectological
    source for its vowel values."

    A declared gap: the spec must emit nothing rather than guess.
    """
    assert _t("zea", "huus") == ""
    assert _t("zea", "water") == ""


# ===========================================================================
# stq — Saterland Frisian
# ===========================================================================


def test_stq_centring_diphthongs():
    """KEY FEATURE (2): CENTRING DIPHTHONGS /iə, oə, uə/.

    stq notes: "(2) CENTRING DIPHTHONGS /iə, oə, uə/ — shared Frisian heritage."
    Sources: Fort (1980), Kramer (1982).
    """
    assert "oə" in _t("stq", "Woater")
    assert "oə" in _t("stq", "Loand")


def test_stq_final_devoicing():
    """KEY FEATURE (3): FINAL DEVOICING.

    stq notes: "(3) FINAL DEVOICING as in all Frisian and continental West
    Germanic." Sources: Fort (1980), Markey (1981).
    """
    assert _t("stq", "Loand").endswith("t")


def test_stq_initial_sp_st_hushing():
    """KEY FEATURE (5): /sp, st/ → [ʃp, ʃt] word-initially.

    stq notes: "(5) /sp, st/ → [ʃp, ʃt] word-initially (shared with Low German)."
    Sources: Fort (1980), Kramer (1982).
    """
    assert _t("stq", "Spräke").startswith("ʃp")
    assert _t("stq", "stien").startswith("ʃt")


def test_stq_s_voices_initially_and_intervocalically():
    """KEY FEATURE (6): /s/ → [z] intervocalically and word-initially before vowels.

    stq notes: "(6) /s/ → [z] intervocalically and word-initially before vowels."
    Sources: Fort (1980), Markey (1981).

    Minimal pair on the same ⟨s⟩: voiced before a vowel (initial suuk, medial
    reesen), voiceless in the ⟨st⟩/⟨sp⟩ clusters above.
    """
    assert _t("stq", "suuk").startswith("z")
    assert "z" in _t("stq", "reesen")


def test_stq_long_aa_umlaut_distinct_from_ee():
    """KEY FEATURE (8): long ää /ɛː/ preserved as distinct from ee /eː/.

    stq notes: "(8) Long ää /ɛː/ preserved as distinct from ee /eː/."
    Sources: Fort (1980), Kramer (1982).

    A true minimal contrast on the nucleus alone.
    """
    assert "ɛː" in _t("stq", "ääbend")
    assert "eː" in _t("stq", "lees")


# ===========================================================================
# ofs / osx / goh / non / ang / enm / gem — older Germanic
# ===========================================================================


def test_ofs_no_high_german_consonant_shift():
    """KEY FEATURE (4): NO HIGH GERMAN CONSONANT SHIFT.

    ofs notes: "(4) NO HIGH GERMAN CONSONANT SHIFT." Sources: Bremmer (2009),
    Stiles (1995).

    The one segment the shift would have moved: OHG shifts ⟨k⟩ to an affricate or
    fricative; Old Frisian ⟨k⟩ stays a plain stop.
    """
    assert _t("ofs", "kening").startswith("k")


def test_ofs_geminates_distinctive():
    """KEY FEATURE (6): geminate consonants still distinctive.

    ofs notes: "(6) Geminate consonants still distinctive." Source: Bremmer (2009).
    """
    assert "nː" in _t("ofs", "kinn")


def test_osx_no_high_german_consonant_shift():
    """NO HIGH GERMAN CONSONANT SHIFT: OS p, t, k unchanged.

    osx notes: "NO HIGH GERMAN CONSONANT SHIFT: OS p, t, k unchanged (cf. OHG
    pf/ff, tz/ss, hh). OS makōn vs. OHG mahhōn 'to make'; OS water vs. OHG wazzer
    'water'." Source: Gallée (1993), Robinson (1992).

    The exact contrast the citation draws, isolated on the intervocalic obstruent
    of each of the two named words.
    """
    assert "k" in _t("osx", "makon")
    assert "t" in _t("osx", "watar")


def test_goh_high_german_consonant_shift_p_to_pf():
    """HGCS: PGmc *p → OHG pf.

    goh notes: "THE DEFINING FEATURE: HIGH GERMAN CONSONANT SHIFT ... PGmc *p →
    OHG pf/ff ... OHG apful vs. OE æppel 'apple'." Source: Braune (2018).

    Isolated on the shifted segment of the very word the citation names, against
    the unshifted Old Saxon ⟨p⟩ of the test above.
    """
    assert "pf" in _t("goh", "apful")


def test_goh_high_german_consonant_shift_t_to_ts():
    """HGCS: PGmc *t → OHG tz [ts].

    goh notes: "PGmc ... *t → tz/ss ... OHG herza vs. OE heorte 'heart'."
    Source: Braune (2018), Fulk (2018).
    """
    assert "ts" in _t("goh", "herza")


def test_non_umlaut_vowels():
    """FULL UMLAUT SYSTEM: y [y], ø [ø], œ [œ], ǫ [ɔ], æ [æ].

    non notes: "FULL UMLAUT SYSTEM: y [y], ø [ø], œ [œ], ǫ [ɔ], æ [æ]."
    Source: Gordon (1957), Noreen (1923).
    """
    assert _t("non", "yfir").startswith("y")
    assert "œ" in _t("non", "fœra")
    assert "ɔ" in _t("non", "ǫnd")
    assert "æ" in _t("non", "sær")


def test_non_thorn_and_eth_preserved():
    """PRESERVED: /θ/ (þ) and /ð/ (ð).

    non notes: "PRESERVED: /θ/ (þ) and /ð/ (ð); kn-, gn- clusters; voiceless
    resonants hl-, hr-, hn-." Source: Gordon (1957).
    """
    assert _t("non", "þing").startswith("θ")
    assert "ð" in _t("non", "hlaða")


def test_non_kn_and_gn_clusters_preserved():
    """PRESERVED: the kn-, gn- clusters.

    non notes: "PRESERVED: ... kn-, gn- clusters." Source: Gordon (1957).

    Both letters of the onset must be pronounced, unlike the later Germanic
    reductions.
    """
    assert _t("non", "kné").startswith("kn")
    assert _t("non", "gnaga").startswith("ɡn")


@pytest.mark.xfail(
    strict=True,
    reason="Gordon (1957), Noreen (1923) claim Old Norse preserves the voiceless "
    "resonants hl-, hr-, hn-; non produces [hlaða] for hlaða and [hriŋɡr] for "
    "hringr — a plain [h] plus a voiced sonorant, where the Icelandic descendant "
    "spec does devoice them ([l̥], [r̥])",
)
def test_non_voiceless_resonants():
    """PRESERVED: voiceless resonants hl-, hr-, hn-.

    non notes: "PRESERVED: ... voiceless resonants hl-, hr-, hn-."
    Source: Gordon (1957), Noreen (1923).

    Minimal pair against the Icelandic descendant, which does encode [l̥ n̥ r̥].
    """
    assert _t("non", "hlaða").startswith("l̥")
    assert _t("non", "hringr").startswith("r̥")


def test_ang_sc_is_postalveolar():
    """⟨sc⟩ = /ʃ/ (scip 'ship').

    ang notes: "⟨sc⟩ = /ʃ/ (scip 'ship')." Source: Campbell (1959), Hogg (1992).
    """
    assert _t("ang", "scip").startswith("ʃ")


def test_ang_cg_is_affricate():
    """⟨cg⟩ = /dʒ/ (ecg 'edge').

    ang notes: "⟨cg⟩ = /dʒ/ (ecg 'edge')." Source: Campbell (1959), Hogg (1992).
    """
    assert _t("ang", "ecg").endswith("dʒ")


@pytest.mark.xfail(
    strict=True,
    reason="Campbell (1959), Hogg (1992) claim ⟨c⟩ → [tʃ] before a front vowel "
    "(cild 'child'); ang produces [kild] — the velar stop, so the palatalisation "
    "the notes name is not in the spec",
)
def test_ang_palatalisation_of_c():
    """Palatalisation: *k → [tʃ] / ⟨c⟩ before a front vowel (cild 'child').

    ang notes: "Palatalisation: *k→[tʃ] / ⟨c⟩ before front V (cild 'child')."
    Source: Campbell (1959), Hogg (1992).

    Isolated on the onset ⟨c⟩ of the word the citation names; the ⟨sc⟩ and ⟨cg⟩
    digraphs above do resolve as claimed, so this is the plain-⟨c⟩ rule alone.
    """
    assert _t("ang", "cild").startswith("tʃ")


@pytest.mark.xfail(
    strict=True,
    reason="Campbell (1959), Hogg (1992) claim ⟨g⟩ → [j] before a front vowel "
    "(gear 'year'); ang produces [ɡæɑr] — the velar stop",
)
def test_ang_palatalisation_of_g():
    """Palatalisation: *g → [j] before a front vowel (gear 'year').

    ang notes: "*g→[j] before front V (gear 'year')."
    Source: Campbell (1959), Hogg (1992).
    """
    assert _t("ang", "gear").startswith("j")


@pytest.mark.xfail(
    strict=True,
    reason="Campbell (1959) claims ⟨f⟩ = [v] between voiced sounds; ang produces "
    "[ofer] for ofer — the voiceless fricative in a fully voiced environment",
)
def test_ang_intervocalic_f_is_voiced():
    """⟨f⟩ = [v] between voiced sounds.

    ang notes: "⟨f⟩ = [v] between voiced sounds."
    Source: Campbell (1959), Hogg (1992).

    Minimal pair on the same letter: fīf keeps [f] word-initially and finally,
    ofer must have [v] between two vowels.
    """
    assert "v" in _t("ang", "ofer")
    assert _t("ang", "fīf").startswith("f")


@pytest.mark.xfail(
    strict=True,
    reason="Hogg (1992), Fischer (2000) claim /ʒ/ enters late ME in vision, "
    "pleasure; enm produces [visiɔn] for vision — a plain [s]",
)
def test_enm_zh_from_french():
    """NORMAN FRENCH SUPERSTRATE: /ʒ/ enters (vision, pleasure) in late ME.

    enm notes: "NORMAN FRENCH SUPERSTRATE: /v/ phonemicised; /dʒ/ extended via
    French; /ʒ/ enters (vision, pleasure) in late ME."
    Source: Hogg (1992), Fischer (2000).

    Isolated on the medial ⟨si⟩ of the word the citation names.
    """
    assert "ʒ" in _t("enm", "vision")


@pytest.mark.xfail(
    strict=True,
    reason="Ringe (2006), Kroonen (2013) claim *ɸ is still bilabial at the "
    "Proto-Germanic stage, not yet [f]; gem produces [fader] for fader — the "
    "labiodental",
)
def test_gem_f_is_still_bilabial():
    """*ɸ (bilabial) at this stage, not yet [f].

    gem notes: "*ɸ (bilabial) at this stage, not yet [f]."
    Source: Ringe (2006), Kroonen (2013).

    Isolated on the single onset segment of a reconstructed form.
    """
    assert _t("gem", "fader").startswith("ɸ")


# ===========================================================================
# en-US / en-AU / en-CA / en-IE / en-ZA / en-GB-x-scotland
# ===========================================================================


def test_en_us_rhotic():
    """RHOTIC: /r/ preserved in all positions.

    en-US notes: "RHOTIC: fully rhotic — /r/ preserved in all positions."
    Source: Wells (1982) vol. 3, Ladefoged & Johnson (2011).

    The cited feature: /r/ preserved word-finally in car → [kɑːɹ]. (The
    non-rhotic RP parent that would complete the minimal pair is itself now
    rhotic — a regression tracked by the xfail test_en_gb_non_rhotic.)
    """
    assert _t("en-US", "car").endswith("ɹ")


def test_en_us_no_trap_bath_split():
    """No TRAP-BATH split: BATH words = /æ/.

    en-US notes: "No TRAP-BATH split (bath words = /æ/)."
    Source: Wells (1982) vol. 3.
    """
    assert "æ" in _t("en-US", "bath")
    assert "æ" in _t("en-US", "dance")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 3 claims /t/ and /d/ flap to [ɾ] intervocalically "
    "in butter, ladder, city; en-US produces [bʌttɜːɹ], [læddɜːɹ] and [sɪtj] — "
    "the flap fires only on a single ⟨t⟩ (water → [wæɾɜːɹ]), so the ⟨tt⟩/⟨dd⟩ "
    "geminate graphemes bypass the rule entirely",
)
def test_en_us_t_flapping():
    """T-FLAPPING: /t/ and /d/ → [ɾ] intervocalically in unstressed syllables.

    en-US notes: "T-FLAPPING: /t/ → [ɾ] between vowels (butter, water, city).
    ... FLAPPING: /t/ and /d/ → [ɾ] intervocalically in unstressed syllables
    (butter, ladder, city)." Source: Wells (1982) vol. 3, Ladefoged & Johnson
    (2011).

    Isolated on the intervocalic obstruent of the three words the citation names,
    against the en-GB parent which has [t]/[d] there.
    """
    assert "ɾ" in _t("en-US", "butter")
    assert "ɾ" in _t("en-US", "ladder")
    assert "ɾ" in _t("en-US", "city")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 3 claims the LOT-PALM merger gives /ɑː/ for both; "
    "en-US produces [lɒt] for lot and [pælm] for palm — three distinct vowels "
    "instead of one",
)
def test_en_us_lot_palm_merger():
    """LOT-PALM merger: /ɑː/ for both.

    en-US notes: "LOT-PALM merger: /ɑː/ for both."
    Source: Wells (1982) vol. 3.

    The merger is falsifiable as an identity between the two nuclei.
    """
    assert "ɑː" in _t("en-US", "lot")
    assert "ɑː" in _t("en-US", "palm")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 3 claims the CAUGHT-COT merger (thought = lot); "
    "en-US produces [θɔːt] for thought and [lɒt] for lot — two distinct nuclei",
)
def test_en_us_caught_cot_merger():
    """CAUGHT-COT merger: thought = lot.

    en-US notes: "CAUGHT-COT merger common (thought = lot for most speakers)."
    Source: Wells (1982) vol. 3.

    The claim states an identity between the two nuclei, which is exactly what is
    checked here — nothing else in the two words is compared.
    """
    thought = _t("en-US", "thought")
    lot = _t("en-US", "lot")
    assert thought[1:-1] == lot[1:-1]


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 3 claims Australian English is non-rhotic; en-AU "
    "produces [kɑːɹ] for car — the en-GB parent is non-rhotic ([kɑː]), so the "
    "dialect spec has actively introduced a rhotic ⟨r⟩",
)
def test_en_au_non_rhotic():
    """Australian English is non-rhotic.

    en-AU notes: "Australian English. Non-rhotic."
    Source: Wells (1982) vol. 3.

    Isolated on the word-final ⟨r⟩, against the non-rhotic en-GB parent.
    """
    assert _t("en-AU", "car") == "kɑː"


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 3 claims FACE raising /eɪ/ → [æɪ]; en-AU produces "
    "[deɪ] for day — the unraised RP nucleus",
)
def test_en_au_face_raising():
    """FACE raising: /eɪ/ → [æɪ] (the 'Strine' stereotype).

    en-AU notes: "FACE raising: /eɪ/ → [æɪ] (the 'Strine' stereotype)."
    Source: Wells (1982) vol. 3.

    Isolated on the FACE nucleus of a word whose spelling makes it unambiguous.
    """
    assert "æɪ" in _t("en-AU", "day")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 3 claims PRICE = [ɑɪ]; en-AU produces [pɹɪs] for "
    "price — a bare short [ɪ], not a diphthong at all",
)
def test_en_au_price_backing():
    """PRICE = [ɑɪ].

    en-AU notes: "PRICE = [ɑɪ]; FLEECE = [ɪi] (diphthongal)."
    Source: Wells (1982) vol. 3.
    """
    assert "ɑɪ" in _t("en-AU", "price")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 3 claims FLEECE = [ɪi] (diphthongal); en-AU "
    "produces [fliːs] for fleece — the RP monophthong",
)
def test_en_au_fleece_is_diphthongal():
    """FLEECE = [ɪi] (diphthongal).

    en-AU notes: "PRICE = [ɑɪ]; FLEECE = [ɪi] (diphthongal)."
    Source: Wells (1982) vol. 3.
    """
    assert "ɪi" in _t("en-AU", "fleece")


def test_en_ca_rhotic():
    """Canadian English is rhotic.

    en-CA notes: "Canadian English. Rhotic; close to GA."
    Source: Wells (1982) vol. 3.

    Minimal pair against the non-rhotic en-GB parent: car → [kɑːɹ] vs [kɑː].
    """
    assert _t("en-CA", "car").endswith("ɹ")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 3 claims CANADIAN RAISING /aɪ/ → [ʌɪ] before a "
    "voiceless consonant only; en-CA produces [nɪf] for knife and [nɪvɛs] for "
    "knives — a bare [ɪ] in both, so the nucleus is neither the raised diphthong "
    "nor conditioned by the following consonant's voicing",
)
def test_en_ca_canadian_raising():
    """CANADIAN RAISING: /aɪ/ → [ʌɪ] before a voiceless consonant.

    en-CA notes: "CANADIAN RAISING: /aɪ/ → [ʌɪ] before voiceless C (knife, ice);
    /aʊ/ → [ʌʊ] before voiceless C (out, about)."
    Source: Wells (1982) vol. 3.

    The perfect minimal pair for a voicing-conditioned rule: knife (before
    voiceless [f], raised) vs knives (before voiced [v], unraised).
    """
    assert "ʌɪ" in _t("en-CA", "knife")
    assert "aɪ" in _t("en-CA", "knives")


def test_en_ie_rhotic():
    """Hiberno-English is rhotic.

    en-IE notes: "Hiberno-English / Irish English. Rhotic."
    Source: Wells (1982) vol. 2.

    Minimal pair against the non-rhotic en-GB parent.
    """
    assert _t("en-IE", "car").endswith("ɹ")


def test_en_ie_clear_l_everywhere():
    """Clear [l] everywhere (no dark l).

    en-IE notes: "Clear [l] everywhere (no dark l)." Source: Wells (1982) vol. 2.

    A declared absence, pinned in the coda position where a dark [ɫ] would appear.
    """
    assert "ɫ" not in _t("en-IE", "feel")
    assert _t("en-IE", "feel").endswith("l")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 2 claims the Gaelic-substrate dental stops /θ/ → "
    "[t̪] and /ð/ → [d̪]; en-IE produces [θɪnk] for think — the RP interdental "
    "fricative is inherited unchanged",
)
def test_en_ie_th_stopping():
    """/θ/ → [t̪] and /ð/ → [d̪] (dental stops — Gaelic substrate).

    en-IE notes: "/θ/ → [t̪] and /ð/ → [d̪] (dental stops — Gaelic substrate)."
    Source: Wells (1982) vol. 2.

    Isolated on the ⟨th⟩ digraph alone, against the en-GB parent's [θ].
    """
    assert _t("en-IE", "think").startswith("t̪")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 3 claims South African English is non-rhotic; en-ZA "
    "produces [kɑːɹ] for car, where the en-GB parent gives the non-rhotic [kɑː]",
)
def test_en_za_non_rhotic():
    """South African English is non-rhotic.

    en-ZA notes: "South African English. Non-rhotic."
    Source: Wells (1982) vol. 3.
    """
    assert _t("en-ZA", "car") == "kɑː"


def test_en_scotland_rhotic():
    """Scottish English is rhotic (unlike RP).

    en-GB-x-scotland notes: "Scottish English. Rhotic (unlike RP)."
    Source: Wells (1982) vol. 2.

    The cited feature: Scottish English keeps word-final /r/, car → [kɑːɹ]. (The
    RP parent that would complete the minimal pair is itself now rhotic — a
    regression tracked by the xfail test_en_gb_non_rhotic.)
    """
    assert _t("en-GB-x-scotland", "car").endswith("ɹ")


def test_en_scotland_no_trap_bath_split():
    """No TRAP-BATH split in Scottish English.

    en-GB-x-scotland notes: "No TRAP-BATH split."
    Source: Wells (1982) vol. 2.

    The declared absence, on the BATH word that en-GB's own notes name.
    """
    assert "æ" in _t("en-GB-x-scotland", "castle")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) vol. 2 claims /x/ is phonemic in Scottish English, loch "
    "[lɔx]; en-GB-x-scotland produces [lɒtʃ] — the English ⟨ch⟩ = [tʃ] reading "
    "inherited from en-GB",
)
def test_en_scotland_velar_fricative():
    """/x/ phonemic (loch [lɔx]).

    en-GB-x-scotland notes: "/x/ phonemic (loch [lɔx])."
    Source: Wells (1982) vol. 2.

    Isolated on the ⟨ch⟩ digraph of the word the citation transcribes.
    """
    assert _t("en-GB-x-scotland", "loch").endswith("x")


# ===========================================================================
# ga — Irish
# ===========================================================================


def test_ga_svarabhakti_r_broad():
    """GA_SVARABHAKTI_R_BROAD: /ɾˠ/ → [ɾˠə] before ⟨b bh ch f g mh⟩.

    Rule notes: "Svarabhakti (epenthesis): in Irish an unwritten short /ə/ is
    inserted between a preceding ⟨l n r⟩ and a following ⟨b bh ch f g mh⟩ inside a
    single morpheme after a SHORT vowel — gorm /ˈɡɔɾˠəmˠ/, dearg /ˈdʲaɾˠəɡ/,
    borb /ˈbˠɔɾˠəbˠ/." (Wikipedia, 'Irish phonology' §Epenthesis; Ó Siadhail 1989.)
    """
    assert _t("ga", "gorm") == "ˈɡɔɾˠəmˠ"
    assert _t("ga", "dearg") == "ˈdʲaɾˠəɡ"
    assert _t("ga", "borb") == "ˈbˠɔɾˠəbˠ"


def test_ga_svarabhakti_r_slender():
    """GA_SVARABHAKTI_R_SLENDER: /ɾʲ/ → [ɾʲə] before the same consonant class.

    Rule notes: "Svarabhakti (epenthesis): ... an unwritten short /ə/ is inserted
    between a preceding ⟨l n r⟩ and a following ⟨b bh ch f g mh⟩ inside a single
    morpheme after a SHORT vowel." (Ó Siadhail 1989.)

    The slender counterpart of the rule above, on ⟨rbh⟩.
    """
    assert "ɾʲə" in _t("ga", "gairbh")


def test_ga_svarabhakti_n_broad_dental():
    """GA_SVARABHAKTI_N_BROAD_DENTAL: /n̪ˠ/ → [n̪ˠə] before ⟨b bh ch f g mh⟩.

    Rule notes: "... leanbh /ˈl̠ʲanˠəw/ ..." (Wikipedia, 'Irish phonology'
    §Epenthesis; Ó Siadhail 1989.)
    """
    assert "n̪ˠə" in _t("ga", "leanbh")
    assert "n̪ˠə" in _t("ga", "banbh")


def test_ga_svarabhakti_n_slender():
    """GA_SVARABHAKTI_N_SLENDER: /nʲ/ → [nʲə] before ⟨b bh ch f g mh⟩.

    Rule notes: "... ainm /ˈanʲəmʲ/ ..." (Wikipedia, 'Irish phonology'
    §Epenthesis; Ó Siadhail 1989.)
    """
    assert "nʲə" in _t("ga", "ainm")


def test_ga_svarabhakti_l_broad_dental():
    """GA_SVARABHAKTI_L_BROAD_DENTAL: /l̪ˠ/ → [l̪ˠə] before ⟨b bh ch f g mh⟩.

    Rule notes: "Svarabhakti (epenthesis): an unwritten short /ə/ is inserted
    between a preceding ⟨l n r⟩ and a following ⟨b bh ch f g mh⟩ inside a single
    morpheme after a SHORT vowel." (Ó Siadhail 1989.)
    """
    assert "l̪ˠə" in _t("ga", "balbh")
    assert "l̪ˠə" in _t("ga", "colm")


def test_ga_svarabhakti_l_broad():
    """GA_SVARABHAKTI_L_BROAD: /lˠ/ → [lˠə] before ⟨b bh ch f g mh⟩.

    Rule notes: "Svarabhakti (epenthesis): an unwritten short /ə/ is inserted
    between a preceding ⟨l n r⟩ and a following ⟨b bh ch f g mh⟩." (Ó Siadhail
    1989.)
    """
    assert "lˠə" in _t("ga", "talamh")


def test_ga_svarabhakti_l_slender():
    """GA_SVARABHAKTI_L_SLENDER: /lʲ/ → [lʲə] before ⟨b bh ch f g mh⟩.

    Rule notes: "Svarabhakti (epenthesis): an unwritten short /ə/ is inserted
    between a preceding ⟨l n r⟩ and a following ⟨b bh ch f g mh⟩." (Ó Siadhail
    1989.)
    """
    assert "lʲə" in _t("ga", "seilbh")
    assert "lʲə" in _t("ga", "ailm")


def test_ga_svarabhakti_not_blocked_after_long_vowel():
    """The declared over-generation of the svarabhakti rules.

    Rule notes: "LIMITATION: the engine's rule vocabulary cannot see vowel length
    in the preceding nucleus, so the blocking of epenthesis after a long vowel or
    diphthong (téarma /ˈtʲeːɾˠmˠə/) and across a morpheme boundary is NOT
    captured; those words are over-generated."

    The spec's own declared gap, pinned on the word the note names: the epenthetic
    schwa appears where the phonology says it should not.
    """
    assert "ɾˠə" in _t("ga", "téarma")


def test_ga_eclipsis_digraphs():
    """Initial mutation: eclipsis (urú), encoded as the digraphs mb/gc/nd/bp/dt/bhf/ts.

    ga notes: "Initial mutation: lenition (séimhiú) and eclipsis (urú, encoded as
    the digraphs mb/gc/nd/bp/dt/bhf/ts)." Refs: Ó Siadhail (1989).

    Eclipsis is written, so the falsifiable claim is that the digraph is read as
    the first letter alone: ⟨mb⟩ = [mˠ] with no [bˠ], ⟨gc⟩ = [ɡ] with no [k].
    """
    assert _t("ga", "mbád") == "ˈmˠaːd̪ˠ"
    assert _t("ga", "gcat") == "ˈɡat̪ˠ"
    assert _t("ga", "bpost").startswith("ˈbˠ")
    assert _t("ga", "bhfuil").startswith("ˈw")


def test_ga_lenition_digraphs():
    """Initial mutation: lenition (séimhiú).

    ga notes: "Initial mutation: lenition (séimhiú) and eclipsis (urú ...)."
    Refs: Ó Siadhail (1989), Ní Chiosáin (1999).

    Lenition is written with ⟨h⟩, so the falsifiable claim is the fricative
    outcome: ⟨bh⟩ = [w], ⟨ch⟩ = [x], ⟨dh⟩ = [ɣ], ⟨fh⟩ = silent.
    """
    assert _t("ga", "bhád").startswith("ˈw")
    assert _t("ga", "chat").startswith("ˈx")
    assert _t("ga", "dhún").startswith("ˈɣ")
    assert _t("ga", "fharraige").startswith("ˈa")


def test_ga_initial_stress():
    """Irish (Connacht/Ulster) stresses the FIRST syllable.

    ga `stress` notes: "Irish (Connacht/Ulster) stresses the FIRST syllable
    (Wikipedia, 'Irish phonology' §Prosody) ... Munster instead attracts stress to
    a long vowel or diphthong in the 2nd/3rd syllable and is NOT modelled here."

    The falsifiable half is the Munster carve-out: a long vowel in a later
    syllable must NOT attract the stress mark.
    """
    assert _t("ga", "gorm").startswith("ˈɡ")
    assert _t("ga", "banbh").startswith("ˈbˠ")


def test_ga_quality_marker_vowels_are_silent():
    """Quality-marker vowels are not pronounced.

    ga notes: "Many of those flanking vowels are pure quality markers and are not
    pronounced (⟨e⟩ before ⟨a o⟩; ⟨i⟩ next to a back vowel), which is why they map
    to the empty string in positional_graphemes." Refs: Ó Siadhail (1989).

    Isolated on the marker itself: the ⟨e⟩ of ⟨ea⟩ contributes no segment, it only
    makes the preceding consonant slender.
    """
    assert _t("ga", "nead") == "ˈnʲad̪ˠ"


# ===========================================================================
# gd — Scottish Gaelic
# ===========================================================================


def test_gd_preasp_c_broad():
    """GD_PREASP_C_BROAD: /kʰ/ → [xk] after a vowel.

    Rule notes: "Preaspiration: Scottish Gaelic preaspirates the aspirated stops
    ⟨p t c⟩ medially and finally after a stressed vowel — the diagnostic feature
    that separates Gaelic from Irish ... the mainstream pattern encoded here is
    [xk]/[çkʲ] for the velars ... Conditioned on a preceding vowel, so word-initial
    and post-consonantal stops keep their plain aspirated realisation."
    (Wikipedia, 'Scottish Gaelic phonology'; Ó Maolalaigh 2008.)

    The minimal pair the rule's own condition demands: post-vocalic ⟨c⟩ in mac is
    [xk], word-initial ⟨c⟩ in cù stays plain [kʰ].
    """
    assert _t("gd", "mac") == "ˈmaxk"
    assert _t("gd", "cù").startswith("ˈkʰ")


def test_gd_preasp_c_slender():
    """GD_PREASP_C_SLENDER: /kʲʰ/ → [çkʲ] after a vowel.

    Rule notes: "... the mainstream pattern encoded here is [xk]/[çkʲ] for the
    velars ..." (Ó Maolalaigh 2008.)

    The slender counterpart of the rule above, with the same word-initial control:
    faic is [façkʲ], while ⟨c⟩ in onset position keeps [kʲʰ] (ceap → [kʲʰahp]).
    """
    assert "çkʲ" in _t("gd", "faic")
    assert _t("gd", "ceap").startswith("ˈkʲʰ")


def test_gd_preasp_t_broad():
    """GD_PREASP_T_BROAD: /t̪ʰ/ → [ht̪] after a vowel.

    Rule notes: "... [h]+stop for the coronals and labials. Conditioned on a
    preceding vowel, so word-initial and post-consonantal stops keep their plain
    aspirated realisation." (Ó Maolalaigh 2008.)

    Minimal pair: the medial ⟨t⟩ of bata preaspirates, the initial ⟨t⟩ of tapaidh
    does not.
    """
    assert "ht̪" in _t("gd", "bata")
    assert _t("gd", "tapaidh").startswith("ˈt̪ʰ")


def test_gd_preasp_t_slender():
    """GD_PREASP_T_SLENDER: /tʲʰ/ → [htʲ] after a vowel.

    Rule notes: "... [h]+stop for the coronals and labials." (Ó Maolalaigh 2008.)
    """
    assert "htʲ" in _t("gd", "aite")


def test_gd_preasp_p():
    """GD_PREASP_P: /pʰ/ → [hp] after a vowel.

    Rule notes: "Preaspiration: Scottish Gaelic preaspirates the aspirated stops
    ⟨p t c⟩ medially and finally after a stressed vowel ... [h]+stop for the
    coronals and labials. Conditioned on a preceding vowel, so word-initial and
    post-consonantal stops keep their plain aspirated realisation."
    (Ó Maolalaigh 2008.)

    Minimal pair on ⟨p⟩: post-vocalic in tapaidh, word-initial in piuthar.
    """
    assert "hp" in _t("gd", "tapaidh")
    assert _t("gd", "piuthar").startswith("ˈpʰ")


def test_gd_stops_are_voiceless():
    """Stops are voiceless throughout: ⟨b d g⟩ = unaspirated /p t̪ k/.

    gd notes: "Stops are voiceless throughout (⟨b d g⟩ = unaspirated /p t̪ k/,
    ⟨p t c⟩ = aspirated)." Refs: Bauer (2011), Gillies (2009).

    Minimal pair on the letter alone: ⟨b⟩ = [p] unaspirated, ⟨p⟩ = [pʰ].
    """
    assert _t("gd", "beag").startswith("ˈp")
    assert not _t("gd", "beag").startswith("ˈpʰ")
    assert _t("gd", "piuthar").startswith("ˈpʰ")


def test_gd_slender_velars_are_palatalised_not_palatal():
    """Slender velars are palatalised /kʲ kʲʰ/ rather than palatal /c ɟ/.

    gd notes: "slender velars are palatalised /kʲ kʲʰ/ rather than palatal /c ɟ/."
    Refs: Bauer (2011), Ó Baoill (2010).

    A declared contrast with Irish, which does use /c ɟ/ (ga ceol → [ˈcoːl̪ˠ]).
    """
    assert "c" not in _t("gd", "ceap")
    assert _t("gd", "ceap").startswith("ˈkʲʰ")
    assert _t("ga", "ceol").startswith("ˈc")


# ===========================================================================
# cy / br / cel — other Celtic
# ===========================================================================


def test_cy_voiceless_lateral_nasals_and_rhotic():
    """Voiceless lateral /ɬ/, voiceless nasals /m̥ n̥/, voiceless rhotic /r̥/.

    cy notes: "Voiceless lateral /ɬ/ (⟨ll⟩), voiceless nasal /m̥ n̥/ (⟨mh nh⟩),
    voiceless rhotic /r̥/ (⟨rh⟩), velar fricative /x/ (⟨ch⟩)."
    Refs: Thomas (1996), Ball & Müller (2009).
    """
    assert _t("cy", "llan").startswith("ɬ")
    assert _t("cy", "mham").startswith("m̥")
    assert _t("cy", "nhad").startswith("n̥")
    assert _t("cy", "rhan").startswith("r̥")


def test_cy_velar_fricative():
    """Velar fricative /x/ (⟨ch⟩).

    cy notes: "... velar fricative /x/ (⟨ch⟩)."
    Refs: Thomas (1996), Ball & Müller (2009).
    """
    assert _t("cy", "bach").endswith("x")


@pytest.mark.xfail(
    strict=True,
    reason="Thomas (1996), Ball & Müller (2009) claim penultimate stress; cy "
    "produces [kariad] for cariad with no stress mark at all — the spec declares "
    "no stress block",
)
def test_cy_penultimate_stress():
    """Stress on the penultimate syllable.

    cy notes: "Stress on penultimate syllable."
    Refs: Thomas (1996), Ball & Müller (2009).
    """
    assert "ˈ" in _t("cy", "cariad")


def test_br_ch_and_zh():
    """⟨c'h⟩ = /x/; ⟨zh⟩ = /z/ (KLT).

    br notes: "⟨c'h⟩ = /x/; ⟨zh⟩ = /z/ (KLT) or /h/ (Vannetais)."
    Refs: Hemon (1975), Press (1986).
    """
    assert _t("br", "c'hoar").startswith("x")
    assert "z" in _t("br", "brezhoneg")


def test_br_uvular_r_from_french():
    """French influence: uvular /ʁ/.

    br notes: "French strongly influenced phonology (uvular /ʁ/, nasal vowels in
    loans)." Refs: Hemon (1975), Press (1986).
    """
    assert _t("br", "brezhoneg").startswith("bʁ")


def test_cel_no_plain_long_e():
    """Matasović (2009) reconstructs no plain *ē for Proto-Celtic.

    cel notes: "*ē → *ī (hence ē is absent from the reconstructed phoneme
    inventory) ... Matasović (2009) reconstructs no plain *ē for Proto-Celtic (only
    marginal/secondary long e)."

    A declared absence: no [eː] may be emitted for a form written with ⟨ē⟩.
    """
    assert "eː" not in _t("cel", "matēr")


def test_cel_labiovelars_preserved():
    """Preserves PIE labiovelars (*kʷ splits later).

    cel notes: "Preserves PIE labiovelars (*kʷ splits later: Goidelic → /k/,
    Brythonic → /p/)." Source: Matasović (2009).
    """
    assert _t("cel", "kʷekʷos").startswith("kʷ")


# ===========================================================================
# el — Modern Greek
# ===========================================================================


def test_el_palatalization_before_front_vowels():
    """PALATALIZATION: γ→[ʝ], κ→[c], χ→[ç] before front vowels.

    el notes: "PALATALIZATION: γ/κ/χ palatalize before front vowels (e/i/η/ι/υ):
    γ→[ʝ], κ→[c], χ→[ç]." Sources: Arvaniti (2007), Holton et al. (2004).

    Minimal pair on each consonant: the same letter before a back vowel keeps its
    velar reading (γάτα [ɣ], κότα [k], χώρα [x]).
    """
    assert _t("el", "γη").startswith("ˈʝ")
    assert _t("el", "κερί").startswith("c")
    assert _t("el", "χέρι").startswith("ˈç")
    assert _t("el", "γάτα").startswith("ˈɣ")
    assert _t("el", "κότα").startswith("ˈk")
    assert _t("el", "χώρα").startswith("ˈx")


def test_el_af_ef_before_voiceless():
    """ΑΥ/ΕΥ: [af]/[ef] before voiceless sounds.

    el notes: "ΑΥ/ΕΥ: [av]/[ev] before voiced sounds; [af]/[ef] before voiceless."
    Sources: Arvaniti (2007), Setatos (1974).

    The voiceless half of the alternation, on the ⟨υ⟩ segment alone.
    """
    assert "af" in _bare("el", "αυτό")
    assert "ef" in _bare("el", "εύκολο")


@pytest.mark.xfail(
    strict=True,
    reason="Arvaniti (2007), Setatos (1974) claim ΑΥ/ΕΥ = [av]/[ev] before voiced "
    "sounds; el produces [aˈfɣo] for αυγό and [ˈefʝe] for εύγε — the voiceless [f] "
    "fires in every environment, so only half the cited alternation is encoded",
)
def test_el_av_ev_before_voiced():
    """ΑΥ/ΕΥ: [av]/[ev] before voiced sounds.

    el notes: "ΑΥ/ΕΥ: [av]/[ev] before voiced sounds; [af]/[ef] before voiceless."
    Sources: Arvaniti (2007), Holton et al. (2004), Setatos (1974).

    The perfect minimal pair for the rule: the same ⟨αυ⟩ before voiced ⟨γ⟩ (αυγό)
    vs before voiceless ⟨τ⟩ (αυτό, which is [af] as the test above shows).
    """
    assert "av" in _bare("el", "αυγό")
    assert "ev" in _bare("el", "εύγε")


def test_el_s_voicing():
    """EL_S_VOICING: /s/ → [z] before voiced consonants.

    Rule notes: "/s/ voices to [z] before voiced consonants (Arvaniti 2007 §2.2;
    Holton, Mackridge & Philippaki-Warburton, Greek: A Comprehensive Grammar, ch.
    1.1): Άρκανσας [aɾkanzas], σβήνω [zvino], κόσμος [kozmos]."

    Minimal pair on ⟨σ⟩: voiced before ⟨β⟩/⟨μ⟩, voiceless before a vowel.
    """
    assert _t("el", "σβήνω") == "ˈzvino"
    assert _t("el", "κόσμος") == "ˈkozmos"
    assert _t("el", "σβέλτος").endswith("os")


def test_el_voiced_stop_digraphs():
    """Digraphs ⟨μπ⟩, ⟨ντ⟩, ⟨γκ⟩ represent voiced stops, prenasalised medially.

    el notes: "Digraphs ⟨μπ⟩, ⟨ντ⟩, ⟨γκ⟩ represent voiced stops, with
    prenasalisation medially." Sources: Arvaniti (2007), Holton et al. (2004).

    Minimal pair on position: word-initial ⟨μπ⟩ is a bare [b], medial ⟨ντ⟩/⟨μπ⟩
    carry the homorganic nasal.
    """
    assert _t("el", "μπάλα").startswith("ˈb")
    assert _t("el", "ντύνω").startswith("ˈd")
    assert _t("el", "γκολ").startswith("ˈɡ")
    assert "nd" in _t("el", "πέντε")
    assert "mb" in _t("el", "τύμπανο")


def test_el_stress_on_marked_vowel():
    """The written acute marks the stressed syllable on every polysyllable.

    el `stress` notes: "Modern Greek (Standard) uses a single written acute accent
    (monotonic system since 1982) to mark the stressed syllable on every
    polysyllable ... Monosyllables are unaccented." Source: Arvaniti (2007).

    Isolated on placement, not on the segments: the stress mark must land on the
    syllable whose vowel bears the acute, not on the default penult.
    """
    assert _t("el", "άνθρωπος").startswith("ˈa")
    assert _t("el", "κερί").startswith("ce")
    assert "ˈɾi" in _t("el", "κερί")


# ===========================================================================
# grc — Classical Attic Greek
# ===========================================================================


def test_grc_phi_theta_chi_are_aspirated_stops():
    """(1) ⟨φ θ χ⟩ = aspirated stops [pʰ tʰ kʰ], NOT fricatives.

    grc notes: "(1) ⟨φ θ χ⟩ = aspirated stops [pʰ tʰ kʰ], NOT fricatives."
    Per Allen (1968).

    Minimal pair against the Modern Greek descendant, where the same three letters
    are fricatives ([f θ x]).
    """
    assert _t("grc", "φιλος").startswith("pʰ")
    assert _t("grc", "θεος").startswith("tʰ")
    assert _t("grc", "χορος").startswith("kʰ")


def test_grc_beta_delta_gamma_are_voiced_stops():
    """(2) ⟨β δ γ⟩ = voiced stops [b d ɡ], NOT fricatives.

    grc notes: "(2) ⟨β δ γ⟩ = voiced stops [b d ɡ], NOT fricatives."
    Per Allen (1968).

    Minimal pair against Modern Greek, where the same letters are [v ð ɣ].
    """
    assert _t("grc", "βιος").startswith("b")
    assert "d" in _t("grc", "υδωρ")
    assert "ɡ" in _t("grc", "λογος")


def test_grc_upsilon_is_front_rounded():
    """(3) ⟨υ⟩ = front rounded [y].

    grc notes: "(3) ⟨υ⟩ = front rounded [y]." Per Allen (1968).
    """
    assert _t("grc", "υμνος").startswith("y")


def test_grc_zeta_is_zd():
    """(4) ⟨ζ⟩ = [zd].

    grc notes: "(4) ⟨ζ⟩ = [zd]." Per Allen (1968).
    """
    assert _t("grc", "ζωη").startswith("zd")


def test_grc_ei_ou_are_monophthongs():
    """(5) ⟨ει ου⟩ already monophthongised to [eː oː].

    grc notes: "(5) ⟨ει ου⟩ already monophthongised to [eː oː]."
    Per Allen (1968).
    """
    assert _t("grc", "ειμι").startswith("eː")
    assert _t("grc", "νους") == "noːs"


def test_grc_gamma_before_velar_is_nasal():
    """(8) ⟨γ⟩ before velars = [ŋ].

    grc notes: "(8) ⟨γ⟩ before velars = [ŋ]." Per Allen (1968).

    Minimal pair on the same letter: [ŋ] in ⟨γγ⟩, [ɡ] before a vowel (λογος).
    """
    assert "ŋɡ" in _t("grc", "αγγελος")
    assert "ɡ" in _t("grc", "λογος")


def test_grc_geminates_are_phonemic():
    """(9) Geminate consonants phonemic.

    grc notes: "(9) Geminate consonants phonemic." Per Allen (1968).
    """
    assert "lː" in _t("grc", "αλλος")
    assert "sː" in _t("grc", "θαλασσα")


@pytest.mark.xfail(
    strict=True,
    reason="Allen (1968) claims the rough breathing is [h]; grc produces [dɔːr] "
    "for ὕδωρ — not only is no [h] emitted, the rough-breathing vowel ⟨ὕ⟩ itself "
    "contributes no segment at all",
)
@pytest.mark.xfail(
    strict=True,
    reason="Allen (1968): rough breathing = [h]; grc produces [ydɔːr] for ὕδωρ — "
    "the breathing adds no [h] (the vowel itself is now preserved, so the failure "
    "is the missing onset, not a dropped nucleus)",
)
def test_grc_rough_breathing_is_h():
    """(7) Rough breathing = [h].

    grc notes: "(7) Rough breathing = [h]." Per Allen (1968).

    Minimal pair against the same word without the breathing: υδωρ → [ydɔːr], so
    ὕδωρ must be [hydɔːr].
    """
    assert _t("grc", "ὕδωρ").startswith("hy")
    assert _t("grc", "υδωρ").startswith("y")


@pytest.mark.xfail(
    strict=True,
    reason="Allen (1968) claims /r/ is voiceless word-initially [r̥]; grc produces "
    "[rɛːtɔːr] for ρητωρ — the plain trill in both positions",
)
def test_grc_initial_r_is_voiceless():
    """(10) /r/ probably trilled, voiceless word-initially [r̥].

    grc notes: "(10) /r/ probably trilled, voiceless word-initially [r̥]."
    Per Allen (1968).

    Minimal pair on position: word-initial ⟨ρ⟩ vs the same letter word-finally,
    which stays voiced.
    """
    assert _t("grc", "ρητωρ").startswith("r̥")


def test_grc_pitch_accent_is_ignored_not_destructive():
    """(6) Pitch accent (not captured segmentally).

    grc notes: "(6) Pitch accent (not captured segmentally)." Per Allen (1968).

    Not capturing the accent means dropping the tone, not the vowel: the polytonic
    ⟨ό⟩ must still be the vowel [o].
    """
    assert _t("grc", "λόγος") == _t("grc", "λογος")
