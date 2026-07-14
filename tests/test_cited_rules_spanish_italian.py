"""Cited-rule conformance: Spanish varieties, Italian varieties, Latin/Italic,
Ancient Greek, Romanian and the Romance/English-lexifier creoles.

Each test takes one cited claim from a spec's ``notes`` prose, quotes it with
its citation, and proves the engine honours it on a real word — isolating the
claim to a single segment, and pinning it with a minimal pair (the same word
under the dialect and under its parent) wherever the phonology allows one.

Claims the engine does NOT honour are marked ``xfail(strict=True)`` with the
actual output in the reason; the assertion still says what the citation says.
Specs that honestly declare their own gap ("deliberate stub", "not modelled")
have that declared omission pinned with a passing test.

Companion to ``test_cited_rules_romance.py`` (pt, es-ES, it-IT, fr-FR).
"""
import unicodedata

import pytest

from orthography2ipa.g2p import G2P


def _t(code, word):
    # NFC so a precomposed nasal glyph in an expected literal compares equal to
    # the engine's decomposed vowel + combining tilde.
    return unicodedata.normalize("NFC", G2P(code).transcribe_word(word))


def _bare(code, word):
    return _t(code, word).replace("ˈ", "").replace("ˌ", "")


# ===========================================================================
# Latin-American Spanish regional stubs — the pan-LatAm baseline
#
# Every es-*-x-* spec in this cluster carries the same STRUCTURAL STUB notes:
# "Only the pan-Latin-American baseline (seseo: c/z->/s/, yeismo: ll->/ʝ/;
# Lipski 1994) is modelled here; the dialect-specific phonology is deliberately
# not yet described (stub tier)."  es-HN and es-SV say the same of the national
# tier.  There are exactly two cited rules there, so there are two tests — each
# checked on every variety that claims it.
# ===========================================================================

LATAM_STUBS = [
    "es-HN", "es-SV",
    "es-AR-x-cordoba", "es-AR-x-cuyo", "es-AR-x-litoral", "es-AR-x-norte",
    "es-AR-x-patagonia",
    "es-BO-x-andino", "es-BO-x-camba",
    "es-CL-x-andino", "es-CL-x-chilote",
    "es-CO-x-llanero", "es-CO-x-pacifico", "es-CO-x-santander", "es-CO-x-valluno",
    "es-EC-x-andino", "es-EC-x-costa",
    "es-MX-x-norte", "es-MX-x-yucatan",
    "es-PE-x-amazonico", "es-PE-x-andino",
    "es-VE-x-andino", "es-VE-x-llanero", "es-VE-x-maracucho",
]


@pytest.mark.parametrize("code", LATAM_STUBS)
def test_latam_stub_seseo(code):
    """SESEO: ⟨c⟩ before e/i and ⟨z⟩ are /s/, never the Castilian /θ/.

    Stub notes (identical across the cluster): "Only the pan-Latin-American
    baseline (seseo: c/z->/s/, yeismo: ll->/ʝ/; Lipski 1994) is modelled here."

    Isolated on the sibilant: ⟨c⟩ of cielo and ⟨z⟩ of zapato are [s]; es-ES,
    whose own notes claim "DISTINCIÓN: /θ/ ≠ /s/", is the minimal pair.
    """
    assert _bare(code, "cielo").startswith("s")
    assert _bare(code, "zapato").startswith("s")
    assert "θ" not in _bare(code, "cielo")
    assert _bare("es-ES", "cielo").startswith("θ")


@pytest.mark.parametrize("code", LATAM_STUBS)
def test_latam_stub_yeismo(code):
    """YEÍSMO: ⟨ll⟩ is /ʝ/ — the historical lateral /ʎ/ is merged away.

    Stub notes: "Only the pan-Latin-American baseline (seseo: c/z->/s/, yeismo:
    ll->/ʝ/; Lipski 1994) is modelled here."

    Isolated on the single ⟨ll⟩ segment of pollo; es-ES-x-medieval, which keeps
    the pre-yeísta lateral, is the minimal pair.
    """
    assert "ʝ" in _bare(code, "pollo")
    assert "ʎ" not in _bare(code, "pollo")
    assert "ʎ" in _bare("es-ES-x-medieval", "cavallo")


def test_es_mx_yucatan_seseo_against_parent():
    """The Yucatán stub's cited seseo is a genuine delta from its parent es-MX.

    es-MX-x-yucatan notes: "Only the pan-Latin-American baseline (seseo:
    c/z->/s/ ...; Lipski 1994) is modelled here."

    Same word, dialect vs parent: es-MX still gives the Castilian [θ] for ⟨c⟩
    before a front vowel, so the stub's seseo is what changes the segment.
    """
    assert _bare("es-MX-x-yucatan", "cielo").startswith("s")
    assert _bare("es-MX", "cielo").startswith("θ")


def test_es_ar_litoral_yeismo_against_parent_sheismo():
    """The Litoraleño stub models only the Lipski yeísmo baseline, not Rioplatense šeísmo.

    es-AR-x-litoral notes: "Only the pan-Latin-American baseline (seseo:
    c/z->/s/, yeismo: ll->/ʝ/; Lipski 1994) is modelled here; the
    dialect-specific phonology is deliberately not yet described (stub tier)."

    Same word, dialect vs parent: es-AR realises ⟨ll⟩ as the Rioplatense [ʃ];
    the stub, by its own declaration, resets to the baseline [ʝ].
    """
    assert "ʝ" in _bare("es-AR-x-litoral", "pollo")
    assert "ʃ" in _bare("es-AR", "pollo")


# ===========================================================================
# es-ES-x-medieval — Old Spanish, the six-sibilant system
#
# notes: "The system is defined by a six-sibilant opposition (three voicing
# pairs): affricate /ts/~/dz/ (written ⟨c/ç⟩ vs ⟨z⟩), lamino-alveolar fricative
# /s/~/z/ (written ⟨ss⟩ vs ⟨s⟩ intervocalically), and palato-alveolar fricative
# /ʃ/~/ʒ/ (written ⟨x⟩ vs ⟨j, g+e,i⟩). ... ⟨ll⟩ = /ʎ/ (yeísmo post-medieval);
# ⟨v⟩ = /v~β/ distinct from ⟨b⟩ = /b/ ...; no /θ/ or /x/ phonemes.
# Source: Penny (2002), §§3.1–3.3; Lapesa (1981), §§52–56."
# ===========================================================================


def test_medieval_voiceless_affricate_c_cedilla():
    """⟨c/ç⟩ is the voiceless affricate /ts/.

    es-ES-x-medieval notes: "affricate /ts/~/dz/ (written ⟨c/ç⟩ vs ⟨z⟩)".
    Penny (2002), §§3.1–3.3.

    cabeça isolates the ⟨ç⟩: [ts], where modern es-ES has the merged [θ].
    """
    assert _bare("es-ES-x-medieval", "cabeça") == "kaβetsa"
    assert "θ" in _bare("es-ES", "cabeza")


def test_medieval_voiced_affricate_z():
    """⟨z⟩ is the VOICED affricate /dz/, the voiced partner of ⟨ç⟩.

    es-ES-x-medieval notes: "affricate /ts/~/dz/ (written ⟨c/ç⟩ vs ⟨z⟩)".
    Penny (2002), §§3.1–3.3.

    The voicing contrast is the whole point of the pair: dezir has [dz] where
    cabeça has [ts].
    """
    assert _bare("es-ES-x-medieval", "dezir") == "dedziɾ"
    assert "ts" in _bare("es-ES-x-medieval", "cabeça")


def test_medieval_intervocalic_s_is_voiced_and_ss_is_not():
    """⟨s⟩ between vowels is /z/; ⟨ss⟩ is /s/ — a spelled voicing contrast.

    es-ES-x-medieval notes: "lamino-alveolar fricative /s/~/z/ (written ⟨ss⟩ vs
    ⟨s⟩ intervocalically) ... intervocalic ⟨s⟩ = /z/ vs ⟨ss⟩ = /s/."
    Lapesa (1981), §§52–56.

    Minimal pair in the same environment: casa [z] vs passar [s].
    """
    assert _bare("es-ES-x-medieval", "casa") == "kaza"
    assert _bare("es-ES-x-medieval", "passar") == "pasaɾ"


def test_medieval_x_is_voiceless_hush():
    """⟨x⟩ is the voiceless palato-alveolar /ʃ/.

    es-ES-x-medieval notes: "palato-alveolar fricative /ʃ/~/ʒ/ (written ⟨x⟩ vs
    ⟨j, g+e,i⟩)". Penny (2002), §§3.1–3.3.

    dixo isolates the ⟨x⟩: [ʃ], where modern Spanish has the retracted [x].
    """
    assert _bare("es-ES-x-medieval", "dixo") == "diʃo"


def test_medieval_j_and_soft_g_are_voiced_hush():
    """⟨j⟩ and ⟨g⟩ before e/i are the VOICED palato-alveolar /ʒ/.

    es-ES-x-medieval notes: "palato-alveolar fricative /ʃ/~/ʒ/ (written ⟨x⟩ vs
    ⟨j, g+e,i⟩)". Penny (2002), §§3.1–3.3.

    fijo [ʒ] against dixo [ʃ] is the voicing pair; both are pre-merger.
    """
    assert _bare("es-ES-x-medieval", "fijo") == "fiʒo"
    assert _bare("es-ES-x-medieval", "muger") == "muʒeɾ"


def test_medieval_ll_is_lateral():
    """⟨ll⟩ is the palatal lateral /ʎ/ — yeísmo is post-medieval.

    es-ES-x-medieval notes: "⟨ll⟩ = /ʎ/ (yeísmo post-medieval)".

    Minimal pair against modern es-ES ("YEÍSMO: ⟨ll⟩ = ⟨y⟩ = /ʝ/"), on ⟨ll⟩.
    """
    assert "ʎ" in _bare("es-ES-x-medieval", "llamar")
    assert "ʝ" in _bare("es-ES", "llamar")


def test_medieval_v_distinct_from_b():
    """⟨v⟩ is /v~β/, distinct from ⟨b⟩ = /b/ — betacism is not yet complete.

    es-ES-x-medieval notes: "⟨v⟩ = /v~β/ distinct from ⟨b⟩ = /b/ (betacism
    complete by 16th c.)". Lapesa (1981), §§52–56.

    Minimal pair against modern es-ES ("BETACISM: ⟨b⟩ = ⟨v⟩ = /b/"), on the
    initial segment of a ⟨v⟩-word and a ⟨b⟩-word.
    """
    assert _bare("es-ES-x-medieval", "cavallo").startswith("kav")
    assert _bare("es-ES-x-medieval", "boca").startswith("b")
    assert _bare("es-ES", "vaca").startswith("b")


def test_medieval_has_no_theta_and_no_velar_fricative():
    """Old Spanish has neither /θ/ nor /x/ — both are post-medieval mergers.

    es-ES-x-medieval notes: "no /θ/ or /x/ phonemes"; "All six sibilants
    collapsed into the modern two-way /s/~/θ/ opposition by c. 1600."
    Penny (2002), §§3.1–3.3.

    The same words that carry [θ] and [x] in modern Castilian carry the
    pre-merger sibilants here.
    """
    for word in ("cabeça", "dezir", "fijo", "dixo"):
        out = _bare("es-ES-x-medieval", word)
        assert "θ" not in out
        assert "x" not in out
    assert "θ" in _bare("es-ES", "cabeza")
    assert "x" in _bare("es-ES", "hijo")


# ===========================================================================
# it-IT-x-toscana — Tuscan
#
# notes: "Distinguished from the standard primarily by GORGIA TOSCANA:
# intervocalic voiceless stops → fricatives (/p/→[ɸ], /t/→[θ], /k/→[h])."
# Giannelli (2000), Rohlfs (1966).
#
# The gorgia is present in the spec's allophone TABLE (see
# test_romance_extended2.TestTuscanItalian) but does not reach transcription.
# ===========================================================================


@pytest.mark.xfail(
    strict=True,
    reason="GORGIA TOSCANA cites /k/→[h] intervocalically; engine produces "
    "[amiko] for amico — the gorgia is listed in the allophone table but no "
    "allophone_rule fires it, so Tuscan is segmentally identical to it-IT",
)
def test_toscana_gorgia_k_to_h():
    """GORGIA TOSCANA: intervocalic /k/ → [h].

    it-IT-x-toscana notes: "GORGIA TOSCANA: intervocalic voiceless stops →
    fricatives (/p/→[ɸ], /t/→[θ], /k/→[h])." Giannelli (2000), Rohlfs (1966).

    amico isolates it: the ⟨c⟩ is intervocalic, so it is the one segment that
    should differ from standard it-IT [aˈmiko].
    """
    assert _bare("it-IT-x-toscana", "amico") == "amiho"


@pytest.mark.xfail(
    strict=True,
    reason="GORGIA TOSCANA cites /t/→[θ] intervocalically; engine produces "
    "[vita] for vita — no allophone_rule fires the gorgia",
)
def test_toscana_gorgia_t_to_theta():
    """GORGIA TOSCANA: intervocalic /t/ → [θ].

    it-IT-x-toscana notes: "intervocalic voiceless stops → fricatives (/p/→[ɸ],
    /t/→[θ], /k/→[h])." Giannelli (2000), Rohlfs (1966).

    vita isolates it on the single intervocalic ⟨t⟩.
    """
    assert _bare("it-IT-x-toscana", "vita") == "viθa"


@pytest.mark.xfail(
    strict=True,
    reason="GORGIA TOSCANA cites /p/→[ɸ] intervocalically; engine produces "
    "[lupo] for lupo — no allophone_rule fires the gorgia",
)
def test_toscana_gorgia_p_to_phi():
    """GORGIA TOSCANA: intervocalic /p/ → [ɸ].

    it-IT-x-toscana notes: "intervocalic voiceless stops → fricatives (/p/→[ɸ],
    /t/→[θ], /k/→[h])." Giannelli (2000), Rohlfs (1966).

    lupo isolates it on the single intervocalic ⟨p⟩.
    """
    assert _bare("it-IT-x-toscana", "lupo") == "luɸo"


# ===========================================================================
# it-IT-x-roma — Romanesco
#
# notes: "Key features: (1) NO gorgia. (2) Rhotacism: /l/ → [r] before
# consonants (alto → [ˈarto]). (3) -ND- → [nː], -MB- → [mː]. (4) Affricate
# strengthening: /dʒ/ → [dːʒ] intervocalically." D'Achille & Giovanardi (2001).
# ===========================================================================


def test_roma_no_gorgia():
    """Romanesco has NO gorgia — intervocalic /k/ stays a stop.

    it-IT-x-roma notes: "Key features: (1) NO gorgia."
    D'Achille & Giovanardi (2001).

    A declared absence, pinned so the Tuscan lenition cannot leak in: amico
    keeps its [k].
    """
    assert _bare("it-IT-x-roma", "amico") == "amiko"
    assert "h" not in _bare("it-IT-x-roma", "amico")


@pytest.mark.xfail(
    strict=True,
    reason="Romanesco rhotacism cites alto → [ˈarto]; engine produces [alto] — "
    "no allophone_rule turns pre-consonantal /l/ into [r]",
)
def test_roma_rhotacism_l_to_r_before_consonant():
    """Rhotacism: /l/ → [r] before a consonant.

    it-IT-x-roma notes: "(2) Rhotacism: /l/ → [r] before consonants (alto →
    [ˈarto])." D'Achille & Giovanardi (2001).

    The cited word itself: the coda ⟨l⟩ of alto is the only segment that should
    differ from standard it-IT [ˈalto].
    """
    assert _bare("it-IT-x-roma", "alto") == "arto"


@pytest.mark.xfail(
    strict=True,
    reason="Romanesco cites -ND- → [nː]; engine produces [kwando] for quando — "
    "the assimilation is not encoded",
)
def test_roma_nd_assimilates_to_geminate_n():
    """-ND- assimilates to the geminate [nː].

    it-IT-x-roma notes: "(3) -ND- → [nː], -MB- → [mː]."
    D'Achille & Giovanardi (2001).

    quando isolates it: the ⟨nd⟩ cluster is the only difference from standard
    it-IT [ˈkwando].
    """
    assert _bare("it-IT-x-roma", "quando") == "kwanːo"


@pytest.mark.xfail(
    strict=True,
    reason="Romanesco cites -MB- → [mː]; engine produces [ɡamba] for gamba — "
    "the assimilation is not encoded",
)
def test_roma_mb_assimilates_to_geminate_m():
    """-MB- assimilates to the geminate [mː].

    it-IT-x-roma notes: "(3) -ND- → [nː], -MB- → [mː]."
    D'Achille & Giovanardi (2001).

    gamba isolates it on the ⟨mb⟩ cluster.
    """
    assert _bare("it-IT-x-roma", "gamba") == "ɡamːa"


@pytest.mark.xfail(
    strict=True,
    reason="Romanesco cites /dʒ/ → [dːʒ] intervocalically; engine produces "
    "[redʒna] for regina — the affricate is not strengthened, and the spec's "
    "⟨gi⟩ digraph additionally swallows the following ⟨i⟩",
)
def test_roma_affricate_strengthening_intervocalic_dz():
    """Affricate strengthening: intervocalic /dʒ/ → [dːʒ].

    it-IT-x-roma notes: "(4) Affricate strengthening: /dʒ/ → [dːʒ]
    intervocalically." D'Achille & Giovanardi (2001).

    regina isolates it: the intervocalic ⟨g⟩ before ⟨i⟩ is the only segment
    that should differ from standard it-IT [reˈdʒina].
    """
    assert _bare("it-IT-x-roma", "regina") == "redːʒina"


# ===========================================================================
# it-IT-x-umbria — Umbrian (modern Romance)
#
# notes: "Key features: (1) No gorgia. (2) Some assimilatory processes (ND→nn,
# MB→mm) shared with Roman." Rohlfs (1966), Loporcaro (2009).
# ===========================================================================


def test_umbria_no_gorgia():
    """Umbrian has no gorgia — intervocalic /k/ stays a stop.

    it-IT-x-umbria notes: "(1) No gorgia." Rohlfs (1966), Loporcaro (2009).

    A declared absence, pinned: amico keeps its [k], with no Tuscan [h].
    """
    assert _bare("it-IT-x-umbria", "amico") == "amiko"


@pytest.mark.xfail(
    strict=True,
    reason="Umbrian cites ND→nn; engine produces [kwando] for quando — the "
    "assimilation is not encoded",
)
def test_umbria_nd_assimilates():
    """ND → nn.

    it-IT-x-umbria notes: "(2) Some assimilatory processes (ND→nn, MB→mm)
    shared with Roman." Rohlfs (1966), Loporcaro (2009).

    quando isolates it on the ⟨nd⟩ cluster.
    """
    assert "d" not in _bare("it-IT-x-umbria", "quando")


@pytest.mark.xfail(
    strict=True,
    reason="Umbrian cites MB→mm; engine produces [ɡamba] for gamba — the "
    "assimilation is not encoded",
)
def test_umbria_mb_assimilates():
    """MB → mm.

    it-IT-x-umbria notes: "(2) Some assimilatory processes (ND→nn, MB→mm)
    shared with Roman." Rohlfs (1966), Loporcaro (2009).

    gamba isolates it on the ⟨mb⟩ cluster.
    """
    assert "b" not in _bare("it-IT-x-umbria", "gamba")


# ===========================================================================
# it-IT-x-abruzzo — Abruzzese
#
# notes: "Key features: (1) Very strong vowel reduction (unstressed finals →
# [ə]). (2) Productive metaphony (vowel harmony). (3) Gemination preserved.
# (4) /ʃ/ in consonant clusters." Avolio (1995), Ledgeway (2009).
# ===========================================================================


@pytest.mark.xfail(
    strict=True,
    reason="Abruzzese cites 'unstressed finals → [ə]'; engine produces [kane] "
    "for cane — no vowel-reduction rule fires, so the final vowel is the full "
    "[e] of standard Italian",
)
def test_abruzzo_final_vowel_reduces_to_schwa():
    """Very strong vowel reduction: unstressed final vowels → [ə].

    it-IT-x-abruzzo notes: "(1) Very strong vowel reduction (unstressed finals
    → [ə])." Avolio (1995), Ledgeway (2009).

    cane isolates it on the final vowel — the only segment that should differ
    from standard it-IT [ˈkane].
    """
    assert _bare("it-IT-x-abruzzo", "cane").endswith("ə")


def test_abruzzo_gemination_preserved():
    """Gemination is preserved.

    it-IT-x-abruzzo notes: "(3) Gemination preserved."
    Avolio (1995), Ledgeway (2009).

    bello isolates it: the ⟨ll⟩ surfaces long, exactly as in standard Italian —
    the Southern reductions do not degeminate.
    """
    assert _bare("it-IT-x-abruzzo", "bello") == "belːo"


@pytest.mark.xfail(
    strict=True,
    reason="Abruzzese cites '/ʃ/ in consonant clusters'; engine produces "
    "[stelːa] for stella — pre-consonantal /s/ is not retracted",
)
def test_abruzzo_s_retracts_to_esh_in_cluster():
    """/ʃ/ appears in consonant clusters — pre-consonantal /s/ retracts.

    it-IT-x-abruzzo notes: "(4) /ʃ/ in consonant clusters."
    Avolio (1995), Ledgeway (2009).

    stella isolates it on the cluster-initial ⟨s⟩.
    """
    assert _bare("it-IT-x-abruzzo", "stella").startswith("ʃ")


# ===========================================================================
# it-IT-x-calabria — Calabrian
#
# notes: "Key features: (1) Vowel reduction to [ə]. (2) Metaphony.
# (3) Retroflex consonants in S. Calabria (-LL-→[ɖː], TR→[ʈɽ]). (4) Strong
# Greek substrate influence." Fanciullo (2015), Rohlfs (1966).
# ===========================================================================


def test_calabria_tr_cluster_is_retroflex():
    """Retroflex consonants: TR → [ʈɽ].

    it-IT-x-calabria notes: "(3) Retroflex consonants in S. Calabria (-LL-→[ɖː],
    TR→[ʈɽ])." Fanciullo (2015), Rohlfs (1966).

    tre isolates it on the onset cluster — standard it-IT has the plain [tr].
    """
    assert _bare("it-IT-x-calabria", "tre") == "ʈɽe"
    assert _bare("it-IT", "tre").startswith("tr")


@pytest.mark.xfail(
    strict=True,
    reason="Calabrian cites -LL-→[ɖː]; engine produces [belːo] for bello — the "
    "retroflex geminate is in the allophone table but no rule maps ⟨ll⟩ to it",
)
def test_calabria_ll_is_retroflex_geminate():
    """Retroflex consonants: -LL- → [ɖː].

    it-IT-x-calabria notes: "(3) Retroflex consonants in S. Calabria (-LL-→[ɖː],
    TR→[ʈɽ])." Fanciullo (2015), Rohlfs (1966).

    bello isolates it on the ⟨ll⟩ — the sister rule TR→[ʈɽ] does fire.
    """
    assert _bare("it-IT-x-calabria", "bello") == "beɖːo"


@pytest.mark.xfail(
    strict=True,
    reason="Calabrian cites vowel reduction to [ə]; engine produces [kane] for "
    "cane — no reduction rule fires",
)
def test_calabria_unstressed_vowel_reduces_to_schwa():
    """Vowel reduction to [ə].

    it-IT-x-calabria notes: "(1) Vowel reduction to [ə]."
    Fanciullo (2015), Rohlfs (1966).

    cane isolates it on the unstressed final vowel; the spec even carries a
    dedicated ⟨ë⟩→[ə] grapheme, so the schwa is in the inventory.
    """
    assert "ə" in _bare("it-IT-x-calabria", "cane")


# ===========================================================================
# it-IT-x-puglia — Apulian
#
# notes: "Key features: (1) Vowel reduction to [ə]. (2) Metaphony.
# (3) Centralised [ɐ] in unstressed position (Barese)." Fanciullo (2015),
# Ledgeway (2009).
# ===========================================================================


@pytest.mark.xfail(
    strict=True,
    reason="Apulian cites vowel reduction to [ə]; engine produces [kane] for "
    "cane — no reduction rule fires, so Apulian is segmentally standard Italian",
)
def test_puglia_unstressed_vowel_reduces_to_schwa():
    """Vowel reduction to [ə].

    it-IT-x-puglia notes: "(1) Vowel reduction to [ə]."
    Fanciullo (2015), Ledgeway (2009).

    cane isolates it on the unstressed final vowel.
    """
    assert "ə" in _bare("it-IT-x-puglia", "cane")


# ===========================================================================
# la — Reconstructed Classical Latin (Allen 1965/2003)
# ===========================================================================


def test_la_c_and_g_are_always_velar_stops():
    """⟨c⟩ is always [k] and ⟨g⟩ always [ɡ] — no palatalisation.

    la notes: "(1) ⟨c⟩ always [k], ⟨g⟩ always [ɡ] — NO palatalisation."
    Allen (1965/2003).

    Minimal pair against la-x-late, whose notes claim "(5) Palatalisation
    beginning: /k/ before e,i → [kʲ]": same word, cicero.
    """
    assert _bare("la", "cicero") == "kikero"
    assert _bare("la", "gens").startswith("ɡ")
    assert _bare("la-x-late", "cicero") == "kʲikʲero"


def test_la_v_is_the_glide_w():
    """⟨v⟩ is [w], not [v].

    la notes: "(2) ⟨v⟩ = [w], NOT [v]." Allen (1965/2003).

    vita isolates it on the initial segment; ro-RO, a descendant with a genuine
    /v/, is the contrast.
    """
    assert _bare("la", "vita") == "wita"


def test_la_diphthongs_preserved():
    """Diphthongs [aj, oj, aw] are preserved.

    la notes: "(4) Diphthongs [aj, oj, aw] preserved." Allen (1965/2003).

    One word per diphthong, isolating the nucleus: caelum [aj], poena [oj],
    aurum [aw]. la-x-late, which monophthongises ⟨ae⟩, is the minimal pair.
    """
    assert _bare("la", "caelum").startswith("kaj")
    assert _bare("la", "poena").startswith("poj")
    assert _bare("la", "aurum").startswith("aw")
    assert _bare("la-x-late", "caelum").startswith("kɛ")


def test_la_geminates_are_phonemic():
    """Geminate consonants are phonemic — they surface long.

    la notes: "(5) Geminate consonants phonemic." Allen (1965/2003).

    terra and annus isolate the geminate; the length mark is the only thing
    distinguishing them from a single consonant.
    """
    assert _bare("la", "terra") == "terːa"
    assert _bare("la", "annus") == "anːus"


def test_la_aspirated_stops_only_in_greek_loans():
    """Aspirated stops appear only in Greek loans — ⟨ph⟩ is [pʰ].

    la notes: "(6) Aspirated stops only in Greek loans." Allen (1965/2003).

    philosophia (a Greek loan) has [pʰ]; the native porta keeps a plain [p].
    """
    assert _bare("la", "philosophia").startswith("pʰ")
    assert _bare("la", "porta").startswith("p")
    assert "pʰ" not in _bare("la", "porta")


def test_la_final_m_weakens_to_nasalisation():
    """Word-final ⟨-m⟩ is weakened to nasalisation of the preceding vowel.

    la notes: "(7) Word-final -m weakened (probably nasalised vowel)."
    Allen (1965/2003).

    aurum: the final ⟨m⟩ surfaces as a nasalised [ũ], with no separate [m]
    segment; the medial ⟨m⟩ of mensa's onset is untouched.
    """
    assert _bare("la", "aurum") == "awrũ"
    assert _bare("la", "mensa").startswith("m")


@pytest.mark.xfail(
    strict=True,
    reason="la notes claim '/s/ always voiceless'; engine produces [rora] for "
    "rosa, [kara] for casa and [pʰiloropʰia] for philosophia — a synchronic "
    "intervocalic s→r rhotacism rule is applied in the CLASSICAL spec, where "
    "rhotacism is a prehistoric change already lexicalised. DATA BUG in la",
)
def test_la_intervocalic_s_stays_a_voiceless_sibilant():
    """⟨s⟩ is always the voiceless sibilant [s], including between vowels.

    la notes: "(9) /s/ always voiceless." Allen (1965/2003) — Classical Latin
    has no intervocalic /s/ voicing and no synchronic rhotacism; ROSA is
    [ˈrosa].

    rosa isolates the single intervocalic ⟨s⟩. la-x-archaic, which is the spec
    that actually claims ongoing rhotacism, transcribes rosa as [rosa].
    """
    assert _bare("la", "rosa") == "rosa"


# ===========================================================================
# la-x-archaic — Old Latin (Weiss 2020, Sihler 1995)
# ===========================================================================


def test_la_archaic_ei_and_ou_diphthongs_still_distinct():
    """Richer diphthong inventory: /ej/ and /ow/ are still distinct.

    la-x-archaic notes: "(1) Richer diphthong inventory: /ej/, /ow/, /oj/ still
    distinct (later monophthongised to ī, ū, ū)." Weiss (2020), Sihler (1995).

    Minimal pair on the same word: deivos keeps [ej] here, while Classical la
    has already monophthongised it to [iː]; douco keeps [ow].
    """
    assert _bare("la-x-archaic", "deivos").startswith("dej")
    assert _bare("la", "deivos").startswith("diː")
    assert _bare("la-x-archaic", "douco").startswith("dow")


@pytest.mark.xfail(
    strict=True,
    reason="la-x-archaic cites '/oj/ still distinct'; engine produces [poena] "
    "for poena — the ⟨oe⟩ (and ⟨ae⟩) digraph is absent from the archaic spec, "
    "so the diphthong is spelled out as two vowels. Classical la gives [pojna]",
)
def test_la_archaic_oe_is_the_oj_diphthong():
    """The /oj/ diphthong is still distinct.

    la-x-archaic notes: "(1) Richer diphthong inventory: /ej/, /ow/, /oj/ still
    distinct." Weiss (2020), Sihler (1995).

    poena isolates the nucleus. Its Classical parent la, which claims the same
    diphthong, gives [pojna] — the archaic stage cannot have less.
    """
    assert _bare("la-x-archaic", "poena").startswith("poj")


@pytest.mark.xfail(
    strict=True,
    reason="la-x-archaic lists no departure from la's '⟨v⟩ = [w]' yet the "
    "engine produces [ita] for vita — the ⟨v⟩ grapheme is missing from the "
    "archaic spec and is DELETED outright. DATA BUG in la-x-archaic",
)
def test_la_archaic_v_is_still_the_glide():
    """⟨v⟩ is [w] — Old Latin does not depart from the Classical value.

    la notes: "(2) ⟨v⟩ = [w], NOT [v]." la-x-archaic notes enumerate the "Key
    differences from Classical" — (1) diphthongs, (2) rhotacism, (3) final -d,
    (4) /h/, (5) the vowel system — and ⟨v⟩ is not among them, so the Classical
    [w] stands. Weiss (2020), Sihler (1995).
    """
    assert _bare("la-x-archaic", "vita") == "wita"


# ===========================================================================
# la-x-late — Late Latin (Herman 2000, Väänänen 1981, Adams 2013)
# ===========================================================================


def test_la_late_ae_and_oe_monophthongise():
    """ae→[ɛ], oe→[e] monophthongisation is complete.

    la-x-late notes: "(2) ae→[ɛ(ː)], oe→[e(ː)] monophthongisation complete."
    Herman (2000), Väänänen (1981).

    Minimal pair on the same words: Classical la keeps [aj]/[oj].
    """
    assert _bare("la-x-late", "caelum").startswith("kɛ")
    assert _bare("la-x-late", "poena").startswith("pe")
    assert _bare("la", "caelum").startswith("kaj")


def test_la_late_velar_palatalisation_begins():
    """Palatalisation begins: /k/ before e,i → [kʲ].

    la-x-late notes: "(5) Palatalisation beginning: /k/ before e,i → [kʲ]."
    Herman (2000), Adams (2013).

    cicero isolates it: both ⟨c⟩ are pre-front, and Classical la keeps [k].
    """
    assert _bare("la-x-late", "cicero") == "kʲikʲero"
    assert _bare("la", "cicero") == "kikero"


def test_la_late_greek_aspirates_become_fricatives():
    """Greek aspirated stops become fricatives: ph→[f], th→[t].

    la-x-late notes: "(6) Greek aspirated stops → fricatives (ph→[f], th→[t])."
    Väänänen (1981).

    Minimal pair on the same words: Classical la keeps [pʰ]/[tʰ].
    """
    assert _bare("la-x-late", "philosophia").startswith("f")
    assert _bare("la-x-late", "theatrum").startswith("t")
    assert _bare("la", "philosophia").startswith("pʰ")


@pytest.mark.xfail(
    strict=True,
    reason="la-x-late cites '/h/ effectively silent'; engine produces [hora] "
    "for hora — the ⟨h⟩ still maps to a full [h], identical to Classical la",
)
def test_la_late_h_is_silent():
    """/h/ is effectively silent.

    la-x-late notes: "(3) /h/ effectively silent."
    Herman (2000), Väänänen (1981).

    hora isolates it: the initial ⟨h⟩ is the only segment that should differ
    from Classical la [hora].
    """
    assert _bare("la-x-late", "hora") == "ora"


@pytest.mark.xfail(
    strict=True,
    reason="la-x-late cites the B/V merger; engine produces [wita] for vita and "
    "[bita] for bita — ⟨v⟩ is still the Classical glide [w] and is not merged "
    "with ⟨b⟩ at all",
)
def test_la_late_b_and_v_merge():
    """B/V merger (betacism): ⟨v⟩ and ⟨b⟩ no longer contrast.

    la-x-late notes: "(4) B/V merger (betacism) visible in misspellings."
    Herman (2000), Adams (2013) — the misspellings are evidence that the two
    graphemes had come to spell the same segment.

    The merger is falsifiable as a minimal pair on the initial segment: vita
    and bita must not begin with two different phonemes.
    """
    assert _bare("la-x-late", "vita")[0] == _bare("la-x-late", "bita")[0]


@pytest.mark.xfail(
    strict=True,
    reason="la-x-late cites /t/ + i + V → [tsʲ]; engine produces [natio] for "
    "natio — the assibilation is not encoded",
)
def test_la_late_ti_before_vowel_assibilates():
    """Palatalisation: /t/ + i + V → [tsʲ].

    la-x-late notes: "(5) Palatalisation beginning: /k/ before e,i → [kʲ]; /t/ +
    i + V → [tsʲ]." Herman (2000), Adams (2013).

    natio isolates it on the ⟨ti⟩ before ⟨o⟩; the sister /k/ palatalisation in
    the same cited clause does fire.
    """
    assert "ts" in _bare("la-x-late", "natio")


# ===========================================================================
# la-x-italia — Italo-Romance Vulgar Latin (Lausberg 1971)
# ===========================================================================


def test_la_italia_gemination_preserved():
    """Gemination is PRESERVED — the hallmark feature.

    la-x-italia notes: "(1) Gemination PRESERVED (hallmark feature: anno, bello,
    terra)." Lausberg (1971).

    annus isolates it on the ⟨nn⟩, which surfaces long.
    """
    assert _bare("la-x-italia", "annus") == "anːus"


def test_la_italia_u_is_not_fronted():
    """/u/ is not fronted to /y/, unlike Gallo-Romance.

    la-x-italia notes: "(2) /u/ not fronted to /y/ (unlike Gallo-Romance)."
    Lausberg (1971).

    Minimal pair on the same word against la-x-gallia, whose notes claim "(1)
    /u/ → /y/ fronting (mūrum → [myːr])": the ⟨u⟩ of lupus stays back here.
    """
    assert "u" in _bare("la-x-italia", "lupus")
    assert "y" not in _bare("la-x-italia", "lupus")
    assert _bare("la-x-gallia", "murum").startswith("my")


@pytest.mark.xfail(
    strict=True,
    reason="la-x-italia cites 'Final -s LOST'; engine produces [lupus] for "
    "lupus — the final ⟨s⟩ survives, exactly as in Classical la",
)
def test_la_italia_final_s_is_lost():
    """Final -s is LOST — Italian plurals go by vowel alternation, not -s.

    la-x-italia notes: "(4) Final -s LOST (plurals by vowel alternation, not
    -s)." Lausberg (1971).

    lupus isolates it on the word-final ⟨s⟩ — the segment whose loss is the
    defining Italo-Romance/Western-Romance split.
    """
    assert not _bare("la-x-italia", "lupus").endswith("s")


@pytest.mark.xfail(
    strict=True,
    reason="la-x-italia cites k/g before e,i → [tʃ]/[dʒ]; engine produces "
    "[kentum] for centum and [ɡens] for gens — the palatalisation is not "
    "encoded, so Italo-Romance is more conservative here than its own parent "
    "la-x-late, which at least reaches [kʲ]",
)
def test_la_italia_velar_palatalisation_to_affricate():
    """Palatalisation of k/g before e,i → [tʃ]/[dʒ].

    la-x-italia notes: "(5) Palatalisation of k/g before e,i → [tʃ]/[dʒ]."
    Lausberg (1971) — this is the change that gives Italian cento, gente.

    centum isolates it on the initial ⟨c⟩ before ⟨e⟩.
    """
    assert _bare("la-x-italia", "centum").startswith("tʃ")


# ===========================================================================
# la-x-gallia — Gallo-Romance Vulgar Latin (Price 1971, Bec 1970)
# ===========================================================================


def test_la_gallia_u_fronts_to_y():
    """/u/ → /y/ fronting.

    la-x-gallia notes: "(1) /u/ → /y/ fronting (mūrum → [myːr])."
    Price (1971), Bec (1970).

    The cited word: murum. Minimal pair against la-x-italia ("/u/ not fronted
    to /y/"), which keeps the back vowel.
    """
    assert _bare("la-x-gallia", "murum").startswith("my")
    assert "y" not in _bare("la-x-italia", "lupus")


def test_la_gallia_ca_palatalises_to_affricate():
    """CA- → [tʃ] palatalisation — the Gallo-Romance hallmark.

    la-x-gallia notes: "(3) CA- → [tʃ] palatalisation."
    Price (1971), Bec (1970) — this is the change behind French chanter.

    cantare isolates it on the initial ⟨ca⟩; la-x-italia, which does not have
    the change, keeps [k].
    """
    assert _bare("la-x-gallia", "cantare").startswith("t͡ʃ")
    assert _bare("la-x-italia", "cantare").startswith("k")


def test_la_gallia_initial_f_preserved():
    """F- is PRESERVED (it does not go to [h]).

    la-x-gallia notes: "(4) F- PRESERVED (not → [h])."
    Price (1971), Bec (1970).

    facere isolates it on the initial ⟨f⟩; es-ES, whose notes cite the
    F→H→∅ change ("FACERE→hacer"), is the Ibero-Romance contrast.
    """
    assert _bare("la-x-gallia", "facere").startswith("f")
    assert _bare("es-ES", "hacer").startswith("a")


def test_la_gallia_nasal_vowels_develop():
    """Nasal vowels develop.

    la-x-gallia notes: "(5) Nasal vowels develop."
    Price (1971), Bec (1970).

    murum: the final ⟨m⟩ leaves a nasalised vowel [ỹ] with no [m] segment.
    """
    assert _bare("la-x-gallia", "murum") == "myrỹ"


@pytest.mark.xfail(
    strict=True,
    reason="la-x-gallia cites 'intervocalic stops → ∅'; engine produces [ripə] "
    "for ripa — the intervocalic /p/ is not lenited at all, let alone deleted",
)
def test_la_gallia_intervocalic_stop_deletes():
    """More aggressive lenition: intervocalic stops → ∅.

    la-x-gallia notes: "(2) More aggressive lenition (intervocalic stops → ∅)."
    Price (1971), Bec (1970) — this is the change behind French rive < RIPA.

    ripa isolates it on the single intervocalic ⟨p⟩.
    """
    assert "p" not in _bare("la-x-gallia", "ripa")


@pytest.mark.xfail(
    strict=True,
    reason="la-x-gallia cites 'Voiced /v/ preserved (not merged with /b/)'; "
    "engine produces [witə] for vita — ⟨v⟩ is still the Classical glide [w], so "
    "there is no /v/ to preserve",
)
def test_la_gallia_v_is_a_voiced_fricative():
    """Voiced /v/ is preserved, not merged with /b/.

    la-x-gallia notes: "(7) Voiced /v/ preserved (not merged with /b/)."
    Price (1971), Bec (1970).

    vita isolates it on the initial segment: the claim only means anything if
    that segment is a labiodental /v/, distinct from both [b] and Classical [w].
    """
    assert _bare("la-x-gallia", "vita").startswith("v")


# ===========================================================================
# la-x-galloitalic — Gallo-Italic Vulgar Latin (Hull 1982, Pellegrini 1975)
# ===========================================================================


def test_la_galloitalic_u_fronts_to_y():
    """/u/ → /y/ fronting.

    la-x-galloitalic notes: "(1) /u/ -> /y/ fronting."
    Hull (1982), Pellegrini (1975).

    murum isolates it; la-x-italia, on the other side of the La Spezia-Rimini
    line, keeps the back vowel.
    """
    assert _bare("la-x-galloitalic", "murum").startswith("my")
    assert "y" not in _bare("la-x-italia", "lupus")


@pytest.mark.xfail(
    strict=True,
    reason="la-x-galloitalic cites Degemination; engine produces [bella] for "
    "bella and [annys] for annus — the doubled consonant survives as two "
    "segments, so the spec is not degeminated relative to la-x-italia [anːus]",
)
def test_la_galloitalic_degemination():
    """Degemination — the La Spezia-Rimini hallmark.

    la-x-galloitalic notes: "(2) Degemination. ... The La Spezia-Rimini line
    marks the boundary." Hull (1982), Pellegrini (1975).

    bella isolates it: exactly one [l] should surface, against la-x-italia,
    whose notes claim "Gemination PRESERVED (hallmark feature: ... bello)".
    """
    assert _bare("la-x-galloitalic", "bella").count("l") == 1
    assert "lː" in _bare("la-x-italia", "bella")


@pytest.mark.xfail(
    strict=True,
    reason="la-x-galloitalic cites 'Nasal vowels'; engine produces [myrym] for "
    "murum — the final ⟨m⟩ surfaces as a full [m], where the sister spec "
    "la-x-gallia, citing the same innovation, gives the nasalised [myrỹ]",
)
def test_la_galloitalic_nasal_vowels():
    """Nasal vowels develop.

    la-x-galloitalic notes: "(5) Nasal vowels."
    Hull (1982), Pellegrini (1975).

    murum isolates it on the final vowel; la-x-gallia is the minimal pair on
    the same word.
    """
    assert _bare("la-x-galloitalic", "murum") == "myrỹ"


@pytest.mark.xfail(
    strict=True,
    reason="la-x-galloitalic cites 'Final vowel loss/reduction'; engine "
    "produces [vita] for vita — the final vowel is the full Classical [a], "
    "where the sister spec la-x-gallia reduces it to [ə] ([witə])",
)
def test_la_galloitalic_final_vowel_reduces():
    """Final vowel loss/reduction.

    la-x-galloitalic notes: "(4) Final vowel loss/reduction."
    Hull (1982), Pellegrini (1975).

    vita isolates it on the final vowel — either lost, or reduced from [a].
    """
    assert not _bare("la-x-galloitalic", "vita").endswith("a")


# ===========================================================================
# la-x-balkans — Balkan Romance Vulgar Latin (Rosetti 1986, Sala 2005)
# ===========================================================================


def test_la_balkans_no_intervocalic_lenition():
    """NO intervocalic lenition — the defining Eastern-Romance conservatism.

    la-x-balkans notes: "(1) NO intervocalic lenition (lup, foc, not *lub,
    *fogo)." Rosetti (1986), Sala (2005).

    The cited etyma: lupus keeps [p] and focus keeps [k], and ripa keeps its
    intervocalic [p] — a declared absence, pinned against the Western-Romance
    lenition that la-x-gallia claims.
    """
    assert _bare("la-x-balkans", "lupus") == "lupus"
    assert _bare("la-x-balkans", "focus") == "fokus"
    assert "p" in _bare("la-x-balkans", "ripa")
    assert _bare("ro-RO", "lup") == "lup"
    assert _bare("ro-RO", "foc") == "fok"


@pytest.mark.xfail(
    strict=True,
    reason="la-x-balkans cites intervocalic /l/ → /r/; engine produces [solem] "
    "for solem — the rhotacism is not encoded (the very change the note "
    "illustrates with Romanian soare < SOLEM)",
)
def test_la_balkans_l_rhotacism():
    """Rhotacism: intervocalic /l/ → /r/.

    la-x-balkans notes: "(4) Rhotacism: intervocalic /l/ → /r/."
    Rosetti (1986), Sala (2005); ro-RO notes cite the outcome, "soare < SOLEM".

    solem isolates it on the single intervocalic ⟨l⟩.
    """
    assert "r" in _bare("la-x-balkans", "solem")


@pytest.mark.xfail(
    strict=True,
    reason="la-x-balkans cites labial palatalisation before front vowels; "
    "engine produces [bene] for bene — the labial is plain",
)
def test_la_balkans_labial_palatalisation():
    """Labial palatalisation before front vowels.

    la-x-balkans notes: "(3) Labial palatalisation before front vowels."
    Rosetti (1986), Sala (2005) — the process behind Romanian [bʲine]/[kʲept].

    bene isolates it on the initial labial, which precedes a front vowel.
    """
    assert "ʲ" in _bare("la-x-balkans", "bene")


# ===========================================================================
# ro-RO — Standard Romanian (Chițoran 2001, Sala 2005)
# ===========================================================================


def test_ro_central_vowels():
    """The central vowels /ə/ (⟨ă⟩) and /ɨ/ (⟨â/î⟩) — unique in Romance.

    ro-RO notes: "(1) Central vowels /ə/ (⟨ă⟩) and /ɨ/ (⟨â/î⟩) — unique in
    Romance." Chițoran (2001), Sala (2005).

    Each grapheme isolated in a real word: masă [ə], român [ɨ].
    """
    assert _bare("ro-RO", "masă") == "masə"
    assert _bare("ro-RO", "român") == "romɨn"
    assert _bare("ro-RO", "cânta") == "kɨnta"


def test_ro_no_intervocalic_lenition():
    """NO intervocalic lenition — lup, foc, not *lub, *fogo.

    ro-RO notes: "(2) NO intervocalic lenition (lup, foc — not *lub, *fogo)."
    Chițoran (2001), Sala (2005).

    The cited words, against es-ES, whose notes claim "INTERVOCALIC LENITION:
    voiced stops /b, d, ɡ/ → spirants [β, ð, ɣ] between vowels".
    """
    assert _bare("ro-RO", "lup") == "lup"
    assert _bare("ro-RO", "foc") == "fok"
    assert "ð" in _bare("es-ES", "nada")


def test_ro_carries_no_stress_marks():
    """The declared STRESS EXEMPTION: Romanian output carries no stress mark.

    ro-RO notes: "STRESS EXEMPTION (research/production tier rule): Romanian
    lexical stress is phonemic but NOT predictable from standard orthography
    (cópii 'copies' vs copíi 'children' are spelled identically); the standard
    norm writes no stress marks, so the spec carries no stress block per
    docs/quality_tiers.md."

    A declared omission, pinned so a stress block cannot be added by accident:
    the engine must not guess a position it cannot know.
    """
    for word in ("copii", "hotel", "masă", "român"):
        assert "ˈ" not in _t("ro-RO", word)


# ===========================================================================
# grc — Reconstructed Classical Attic Greek (Allen 1968)
# ===========================================================================


def test_grc_phi_theta_chi_are_aspirated_stops():
    """⟨φ θ χ⟩ are aspirated stops [pʰ tʰ kʰ], NOT fricatives.

    grc notes: "(1) ⟨φ θ χ⟩ = aspirated stops [pʰ tʰ kʰ], NOT fricatives."
    Allen (1968).

    One word per letter, isolating the onset: φιλοσοφια, θεος.
    """
    assert _bare("grc", "φιλοσοφια").startswith("pʰ")
    assert _bare("grc", "θεος").startswith("tʰ")
    assert "f" not in _bare("grc", "φιλοσοφια")


def test_grc_beta_delta_gamma_are_voiced_stops():
    """⟨β δ γ⟩ are voiced stops [b d ɡ], NOT the Modern-Greek fricatives.

    grc notes: "(2) ⟨β δ γ⟩ = voiced stops [b d ɡ], NOT fricatives."
    Allen (1968).

    One word per letter, isolating the onset: βιβλιον, δωρον, γαμος.
    """
    assert _bare("grc", "βιβλιον").startswith("b")
    assert _bare("grc", "δωρον").startswith("d")
    assert _bare("grc", "γαμος").startswith("ɡ")


def test_grc_upsilon_is_front_rounded():
    """⟨υ⟩ is the front rounded [y].

    grc notes: "(3) ⟨υ⟩ = front rounded [y]." Allen (1968).

    υιος isolates it on the initial vowel — Modern Greek iotacism would give
    [i].
    """
    assert _bare("grc", "υιος").startswith("y")


def test_grc_zeta_is_zd():
    """⟨ζ⟩ is the cluster [zd].

    grc notes: "(4) ⟨ζ⟩ = [zd]." Allen (1968).

    ζωη isolates it on the onset.
    """
    assert _bare("grc", "ζωη").startswith("zd")


def test_grc_ei_and_ou_already_monophthongs():
    """⟨ει ου⟩ are already monophthongised to [eː oː].

    grc notes: "(5) ⟨ει ου⟩ already monophthongised to [eː oː]." Allen (1968).

    ειμι and λογου isolate them; contrast ⟨αι⟩, which is still the genuine
    diphthong [aj] at this stage.
    """
    assert _bare("grc", "ειμι").startswith("eː")
    assert _bare("grc", "λογου").endswith("oː")


def test_grc_rough_breathing_is_h():
    """The rough breathing is [h].

    grc notes: "(7) Rough breathing = [h]." Allen (1968).

    ἁλς isolates it: the breathing on the initial vowel surfaces as a full [h].
    """
    assert _bare("grc", "ἁλς").startswith("h")
    assert _bare("grc", "ἡμερα").startswith("h")


def test_grc_gamma_before_velar_is_eng():
    """⟨γ⟩ before a velar is [ŋ] — the agma.

    grc notes: "(8) ⟨γ⟩ before velars = [ŋ]." Allen (1968).

    αγγελος isolates it: the first ⟨γ⟩ (before the second) is [ŋ], while the
    second is a plain [ɡ].
    """
    assert _bare("grc", "αγγελος") == "aŋɡelos"


def test_grc_geminates_are_phonemic():
    """Geminate consonants are phonemic.

    grc notes: "(9) Geminate consonants phonemic." Allen (1968).

    θαλασσα isolates the ⟨σσ⟩, which surfaces long.
    """
    assert _bare("grc", "θαλασσα") == "tʰalasːa"


@pytest.mark.xfail(
    strict=True,
    reason="grc cites rough breathing = [h] and word-initial /r/ = [r̥]; engine "
    "produces [odon] for ῥοδον — ⟨ῥ⟩ (rho with dasia, U+1FE5) is absent from "
    "the grapheme table, so BOTH the rhotic and its breathing are dropped. "
    "DATA BUG in grc",
)
def test_grc_initial_rho_is_voiceless():
    """Word-initial ⟨ῥ⟩ is the voiceless trill [r̥], with the rough breathing.

    grc notes: "(7) Rough breathing = [h]. ... (10) /r/ probably trilled,
    voiceless word-initially [r̥]." Allen (1968).

    ῥοδον isolates it on the onset: the rho carries a rough breathing, so the
    segment must be there at all.
    """
    assert _bare("grc", "ῥοδον").startswith("r̥")


# ===========================================================================
# Ancient Italic — etr, xum, osc
# ===========================================================================


def test_etr_four_vowel_system_has_no_o():
    """Etruscan has a 4-vowel system — there is no /o/.

    etr notes: "4-vowel system (no /o/!), aspirate stops prominent."
    Bonfante & Bonfante (2002), Wallace (2008).

    A declared inventory gap, pinned end-to-end: the Latin-transliteration
    ⟨o⟩ maps to nothing, so no [o] can enter a transcription; ⟨u⟩ is the back
    vowel that carries the load (ruma).
    """
    assert _t("etr", "o") == ""
    assert _bare("etr", "ruma") == "ruma"


@pytest.mark.xfail(
    strict=True,
    reason="etr cites 'aspirate stops prominent'; engine produces [efarie] for "
    "θefarie and [welur] for velθur — the transliteration grapheme ⟨θ⟩ is "
    "absent from the table and is DELETED, so the aspirated dental never "
    "surfaces (⟨ph⟩ does give [pʰ]). DATA BUG in etr",
)
def test_etr_theta_is_an_aspirated_stop():
    """The aspirate stops are prominent — ⟨θ⟩ is the aspirated dental [tʰ].

    etr notes: "aspirate stops prominent ... Input graphemes follow conventional
    Latin transliteration of the Old Italic (Etruscan) alphabet."
    Bonfante & Bonfante (2002), Wallace (2008).

    θefarie (the Etruscan name on the Praeneste fibula tradition) isolates it on
    the onset; the sister aspirate ⟨ph⟩ does surface as [pʰ] in phersu.
    """
    assert _bare("etr", "θefarie").startswith("tʰ")
    assert _bare("etr", "phersu").startswith("pʰ")


def test_xum_has_the_distinctive_sibilant():
    """Umbrian has a distinctive sibilant /ʃ/.

    xum notes: "Distinctive sibilant /ʃ/ and extensive rhotacism."
    Rix (2002); the Iguvine Tablets.

    śerfe (Iguvine ⟨ś⟩) isolates it on the onset; the plain ⟨s⟩ of esono stays
    [s], which is what makes the sibilant "distinctive".
    """
    assert _bare("xum", "śerfe").startswith("ʃ")
    assert _bare("xum", "esono").startswith("e")
    assert "ʃ" not in _bare("xum", "esono")


# ===========================================================================
# ht — Haitian Creole (IPN 1979 orthography)
# ===========================================================================


def test_ht_nasal_vowel_digraphs():
    """⟨an en on⟩ are the nasal vowels /ã ɛ̃ ɔ̃/.

    ht notes: "⟨an en on⟩ are the nasal vowels /ã ɛ̃ ɔ̃/."
    IPN (Institut Pédagogique National, 1979).

    One word per digraph, isolating the nucleus: lanmou [ã], pen [ɛ̃],
    bonjou [ɔ̃].
    """
    assert _bare("ht", "lanmou") == "lãmu"
    assert _bare("ht", "pen") == "pɛ̃"
    assert _bare("ht", "bonjou") == "bɔ̃ʒu"


def test_ht_r_is_a_velar_fricative():
    """⟨r⟩ is /ɣ/.

    ht notes: "⟨r⟩ = /ɣ/." IPN (1979).

    ri isolates it on the onset — the French lexifier's uvular /ʁ/ is not the
    Kreyòl value.
    """
    assert _bare("ht", "ri") == "ɣi"


def test_ht_ou_is_u():
    """⟨ou⟩ = /u/.

    ht notes: "⟨ou⟩ = /u/." IPN (1979) — the orthography "is strictly phonemic:
    32 symbols, no silent letters".

    bonjou isolates it on the final nucleus.
    """
    assert _bare("ht", "bonjou").endswith("u")


def test_ht_hyphen_blocks_the_nasal_reading():
    """A following hyphen blocks the nasal reading of ⟨an⟩.

    ht notes: "⟨an en on⟩ are the nasal vowels /ã ɛ̃ ɔ̃/ (a following hyphen or
    an ⟨n⟩+vowel sequence blocks the nasal reading)." IPN (1979).

    Minimal pair on the blocker: pa-n keeps an oral [a] plus a consonantal [n],
    where the unhyphenated an is the nasal vowel [ã].
    """
    assert _bare("ht", "pa-n") == "pan"
    assert _bare("ht", "an") == "ã"


@pytest.mark.xfail(
    strict=True,
    reason="ht cites 'an ⟨n⟩+vowel sequence blocks the nasal reading'; engine "
    "produces [ãe] for ane — the ⟨an⟩ digraph is matched greedily even when the "
    "⟨n⟩ is the onset of the next syllable, so the blocker never applies (the "
    "hyphen blocker does work). DATA BUG in ht",
)
def test_ht_n_plus_vowel_blocks_the_nasal_reading():
    """An ⟨n⟩+vowel sequence blocks the nasal reading of ⟨an⟩.

    ht notes: "⟨an en on⟩ are the nasal vowels /ã ɛ̃ ɔ̃/ (a following hyphen or
    an ⟨n⟩+vowel sequence blocks the nasal reading)." IPN (1979).

    ane isolates it: the ⟨n⟩ is followed by a vowel, so it is the onset of the
    second syllable and the ⟨a⟩ must stay oral.
    """
    assert _bare("ht", "ane") == "ane"


# ===========================================================================
# jam — Jamaican Patois (Cassidy/JLU orthography)
# ===========================================================================


def test_jam_cassidy_consonant_digraphs():
    """⟨ch⟩=/tʃ/, ⟨j⟩=/dʒ/, ⟨sh⟩=/ʃ/, ⟨zh⟩=/ʒ/.

    jam notes: "Phonemic by design: ... <ch>=/tʃ/, <j>=/dʒ/, <sh>=/ʃ/,
    <zh>=/ʒ/, <ng>=/ŋ/." Cassidy (1961); Jamaican Language Unit (2002).

    One word per digraph, isolating the onset.
    """
    assert _bare("jam", "chuu").startswith("tʃ")
    assert _bare("jam", "jan").startswith("dʒ")
    assert _bare("jam", "shel").startswith("ʃ")
    assert _bare("jam", "zhaans").startswith("ʒ")


def test_jam_long_vowels_are_doubled():
    """Long vowels are written doubled.

    jam notes: "short vowels i e a o u; long vowels doubled (ii, aa, uu)."
    Cassidy (1961); Jamaican Language Unit (2002).

    Minimal pair on the nucleus: tuu has the long [uː] that the doubling
    encodes, where a single ⟨u⟩ (pikni) is short.
    """
    assert _bare("jam", "tuu") == "tuː"
    assert "ː" not in _bare("jam", "pikni")


def test_jam_nasal_hn_convention_is_not_modelled():
    """The -hn nasal-vowel convention is declared NOT modelled.

    jam notes: "Nasal vowels are written with a following -hn (e.g. kyaahn);
    that convention and the palatalised <ky>/<gy> onsets are not modelled here."

    A declared omission, pinned: the cited word kyaahn yields the literal
    [h] + [n] of the spelling and no nasalised vowel — so the gap cannot be
    silently closed, and no nasal vowel can appear by accident.
    """
    out = _bare("jam", "kyaahn")
    assert out == "kjaːhn"
    assert "̃" not in unicodedata.normalize("NFD", out)


def test_jam_palatalised_onsets_are_not_modelled():
    """The palatalised ⟨ky⟩/⟨gy⟩ onsets are declared NOT modelled.

    jam notes: "that convention and the palatalised <ky>/<gy> onsets are not
    modelled here." Cassidy (1961); Jamaican Language Unit (2002).

    A declared omission, pinned: ⟨ky⟩ and ⟨gy⟩ come out as the compositional
    stop + glide, not as a palatalised /kʲ/ /ɡʲ/ segment.
    """
    assert _bare("jam", "gyal") == "ɡjal"
    assert "ʲ" not in _bare("jam", "kyaahn")


# ===========================================================================
# kea — Kabuverdianu (ALUPEC orthography)
# ===========================================================================


def test_kea_silent_h():
    """SILENT H: ⟨h⟩ has no phonetic value.

    kea notes: "(3) SILENT H: <h> has no phonetic value."
    ALUPEC (1998, revised 2009).

    hoji isolates it: the initial ⟨h⟩ contributes no segment at all.
    """
    assert _bare("kea", "hoji") == "oʒi"


def test_kea_affricates_tx_and_dj():
    """AFFRICATES: ⟨tx⟩=[tʃ], ⟨dj⟩=[dʒ] — innovations relative to Portuguese.

    kea notes: "(4) AFFRICATES: tx=[tʃ], dj=[dʒ] — innovations relative to PT."
    ALUPEC (1998, revised 2009).

    One word per digraph, isolating the onset.
    """
    assert _bare("kea", "txeu").startswith("tʃ")
    assert _bare("kea", "djar").startswith("dʒ")


def test_kea_sibilants_x_and_j():
    """SIBILANT: ⟨x⟩=[ʃ], ⟨j⟩=[ʒ], ⟨s⟩=[s].

    kea notes: "(6) SIBILANT: x=[ʃ], j=[ʒ], s=[s]."
    ALUPEC (1998, revised 2009).

    xuxu isolates ⟨x⟩, jogu isolates ⟨j⟩, and kabesa keeps ⟨s⟩ as [s] —
    the three-way contrast the note asserts.
    """
    assert _bare("kea", "xuxu") == "ʃuʃu"
    assert _bare("kea", "jogu").startswith("ʒ")
    assert "s" in _bare("kea", "kabesa")


def test_kea_nasal_vowels_are_phonemic():
    """NASAL VOWELS: ⟨ã ẽ ĩ õ ũ⟩ are phonemic.

    kea notes: "(1) NASAL VOWELS: ã/ẽ/ĩ/õ/ũ are phonemic, from African substrate
    influence and retention of archaic PT nasality."
    ALUPEC (1998, revised 2009).

    mãi isolates it: the tilde vowel surfaces nasal, with no [n]/[m] segment.
    """
    assert _bare("kea", "mãi") == "mãi"


def test_kea_five_vowel_system_has_no_central_vowel():
    """FIVE-VOWEL SYSTEM: no /ɨ/; unstressed vowels are preserved.

    kea notes: "(2) FIVE-VOWEL SYSTEM: no /ɨ/; unstressed vowels preserved."
    ALUPEC (1998, revised 2009).

    Minimal pair against the Portuguese lexifier on the same etymon: kabesa
    keeps its full unstressed vowels, where pt-PT's cabeça reduces them
    ([kɐˈbɛsɐ]) — and no [ɨ] appears anywhere.
    """
    assert _bare("kea", "kabesa") == "kabesa"
    assert "ɨ" not in _bare("kea", "kabesa")
    assert "ɐ" in _bare("pt-PT", "cabeça")


# ===========================================================================
# srn — Sranan Tongo (official 1986 spelling)
# ===========================================================================


def test_srn_o_grave_is_open_o():
    """⟨ò⟩ = /ɔ/.

    srn notes: "The mapping follows the official 1986 phonology-based spelling:
    ⟨ò⟩ = /ɔ/."

    Minimal pair on the nucleus: òso has the open [ɔ], where a plain ⟨o⟩ (oso's
    second vowel) is close [o].
    """
    assert _bare("srn", "òso") == "ɔso"


def test_srn_sy_is_esh():
    """⟨sy⟩ = /ʃ/.

    srn notes: "⟨sy⟩ = /ʃ/" (official 1986 spelling).

    syatu isolates it on the onset: the digraph is one segment, not [sj].
    """
    assert _bare("srn", "syatu") == "ʃatu"


def test_srn_ty_and_dy_are_affricates():
    """⟨ty dy⟩ = /t͡ʃ d͡ʒ/.

    srn notes: "⟨ty dy⟩ = /t͡ʃ d͡ʒ/" (official 1986 spelling).

    One word per digraph, isolating the onset.
    """
    assert _bare("srn", "tyari").startswith("t͡ʃ")
    assert _bare("srn", "dyaso").startswith("d͡ʒ")


def test_srn_aw_and_ow_are_diphthongs():
    """⟨aw ow⟩ are the diphthongs /au̯ ou̯/.

    srn notes: "⟨aw ow⟩ = the diphthongs /au̯ ou̯/" (official 1986 spelling).

    kaw and owru isolate them: the ⟨w⟩ is a non-syllabic vowel offglide, not a
    consonantal [w].
    """
    assert _bare("srn", "kaw") == "kau̯"
    assert _bare("srn", "owru") == "ou̯ɾu"


# ===========================================================================
# pih, gpe — deliberate stubs with NO grapheme inventory
# ===========================================================================


def test_pih_is_a_deliberate_stub_with_no_map():
    """Pitkern-Norfolk deliberately specifies NO grapheme inventory.

    pih notes: "STUB (deliberate): the grapheme inventory of Pitkern-Norfolk is
    NOT specified. ... English Wikipedia states outright that 'Pitkern spelling
    is not standardised' ... The only IPA on record is A. C. Gimson's
    transcription of a 1951 Moverley dialogue, which is a text transcription,
    not a grapheme map. No map is claimed."

    A declared omission, pinned: nothing may be invented, so no input yields any
    transcription at all.
    """
    assert _t("pih", "hello") == ""
    assert _t("pih", "a") == ""


def test_gpe_is_a_deliberate_stub_with_no_map():
    """Ghanaian Pidgin English deliberately specifies NO grapheme inventory.

    gpe notes: "DELIBERATE STUB: the grapheme inventory is NOT specified and
    must not be guessed. ... APiCS Online (Huber, survey chapter 16) states
    plainly that 'there is no official orthography for Ghanaian Pidgin English'
    ... a phonology is not an orthography ... until then an honest stub is
    preferred over a fabricated English-like map."

    A declared omission, pinned: no input yields a transcription, so no
    English-like map can creep in.
    """
    assert _t("gpe", "chop") == ""
    assert _t("gpe", "a") == ""
