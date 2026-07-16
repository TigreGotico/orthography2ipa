"""Insular European Portuguese: the Atlantic-island dialects and the rules that
separate an island transcription from a continental one.

Four leaves are exercised here, each a delta over the broad ``pt-PT`` base:

* **Madeira** (``pt-PT-x-madeira``) — the nasal-diphthong → nasal+N reduction
  (⟨-ões⟩ → [õns], ⟨-ães⟩ → [ɐ̃ns]) and the intervocalic /l/ → [ʎ] after /i/.
* **Azores, general node** (``pt-PT-x-acores``) — the São-Miguel-class stressed
  /u/ → [y] fronting (conservative before a coda), ⟨ou⟩ kept as the [ow]
  diphthong, and the [ʒ] prevocalic external /s/-sandhi. Terceira is its gold
  reference.
* **São Miguel / micaelense** (``pt-PT-x-sao-miguel``) — the two emblematic
  front-rounded vowels [y] < stressed ⟨u⟩ and [ø] < ⟨oi⟩/⟨ou⟩, plus /l/ → [ʎ].
* **Terceira / terceirense** (``pt-PT-x-terceira``) — the central-group island
  that, unlike São Miguel, does NOT front /u/; its own features are the
  a-metaphony before final ⟨-o⟩ and the crescent [w] on-glide after labials.

Every claim is isolated on a real word and cited:

* Segura, Luísa (2013), *Variedades dialetais do português europeu*, in Raposo
  et al. (eds.), *Gramática do Português* I: 85-142 — Madeiran /l/ → [ʎ];
* Silva, David J. (2008), *The Persistence of Stereotyped Dialect Features…*,
  *Journal of Portuguese Linguistics* 7-1: 3-21, p. 4 — the micaelense [y] and
  [ø] (with azul [ɐˈzyl], cruz [kryʃ], oito [øt], pouco [pøk]);
* Mikołajczak, Sylwia (2014), *Caraterísticas fonéticas do Português da Ilha
  Terceira*, *Studia Iberystyczne* 13: 417-424 — Terceira has NO /u/-fronting
  (pp. 417-418, 424), the a-metaphony pato [ˈpɔtu] (p. 423) and the crescent
  glide porco [pwˈorku], bicho [bwˈiʃu] (pp. 422-423);
* Rogers, Francis M. (1948), *Insular Portuguese Pronunciation: Porto Santo and
  Eastern Azores*, *Hispanic Review* 16(1): 1-32 — the eastern-Azorean [y].

The four leaves and the ``pt-PT`` base are compared directly so each delta is a
minimal pair against the continental value.
"""
from orthography2ipa import transcribe, get


def _t(code, word):
    return transcribe(word, code)


# ═══════════════════════ Madeira (pt-PT-x-madeira) ════════════════════════

def test_madeira_nasal_diphthong_becomes_nasal_plus_n():
    """The salient Madeiran reduction of the plural nasal diphthongs: ⟨-ões⟩ →
    [õns] and ⟨-ães⟩ → [ɐ̃ns], where the continent keeps the diphthong
    [õj̃ʃ]/[ɐ̃j̃ʃ]. Native attestation: 'leões → leôns', 'cães → câns'
    (Portuguese With Leo, Madeira deep-dive)."""
    assert _t("pt-PT-x-madeira", "cães") == "ˈkɐ̃ns"
    assert _t("pt-PT-x-madeira", "leões") == "lɨˈõns"
    # the continental base keeps the nasal diphthong
    assert _t("pt-PT", "cães") == "ˈkɐ̃j̃ʃ"


def test_madeira_intervocalic_l_palatalises_after_i():
    """The diagnostic Madeiran palatalisation of an intervocalic /l/ to [ʎ]
    after /i/: quilo → [ˈkiʎu], vila → [ˈviʎɐ], mochila → [muˈʃiʎɐ]
    (Segura 2013; native '-il → -ilh', quilómetro → 'quilhómetro')."""
    assert _t("pt-PT-x-madeira", "quilo") == "ˈkiʎu"
    assert _t("pt-PT-x-madeira", "vila") == "ˈviʎɐ"
    assert _t("pt-PT-x-madeira", "mochila") == "muˈʃiʎɐ"
    assert _t("pt-PT", "quilo") == "ˈkilu"


def test_madeira_l_palatalisation_needs_a_preceding_i():
    """The gate is a PRECEDING /i/: an /l/ after any other (reduced) vowel is
    untouched, so teleférico keeps its [l] and gains no [ʎ]."""
    assert "ʎ" not in _t("pt-PT-x-madeira", "teleférico")


def test_madeira_keeps_v_no_betacism():
    """Madeiran, like standard EP and unlike the northern mainland, has NO
    betacism: /v/ stays [v] (vila → [ˈviʎɐ], not [ˈbiʎɐ])."""
    assert _t("pt-PT-x-madeira", "vila").lstrip("ˈ").startswith("v")


def test_madeira_does_not_diphthongise_stressed_i():
    """A documented LIMIT, pinned so it cannot drift: the reported stressed-/i/
    diphthongisation is lexically restricted and deliberately NOT modelled —
    this gold keeps [i] (dia → [ˈdiɐ], ilha → [ˈiʎɐ])."""
    assert _t("pt-PT-x-madeira", "dia") == "ˈdiɐ"
    assert _t("pt-PT-x-madeira", "ilha") == "ˈiʎɐ"


def test_madeira_is_research_tier_and_cited():
    """The spec is research-tier and cites the Segura (2013) dialectology."""
    spec = get("pt-PT-x-madeira")
    assert spec.quality.value == "research"
    assert "segura2013" in {s.id for s in spec.sources}


# ═════════════════ Azores general node (pt-PT-x-acores) ═══════════════════

def test_acores_fronts_stressed_u_to_y():
    """The stereotyped Azorean (São-Miguel-class) fronting of a stressed /u/ to
    the front rounded [y]: muda → [ˈmydɐ], tu → [ˈty], where the continent has
    [ˈmudɐ]/[ˈtu] (Rogers 1948)."""
    assert _t("pt-PT-x-acores", "muda") == "ˈmydɐ"
    assert _t("pt-PT-x-acores", "tu") == "ˈty"
    assert _t("pt-PT", "muda") == "ˈmudɐ"


def test_acores_keeps_conservative_u_before_a_coda():
    """The GENERAL node keeps the conservative Rogers-based open-nucleus
    restriction: no fronting before a tautosyllabic coda liquid, so
    azul → [ɐˈzuɫ] (contrast the São Miguel leaf, which fronts it)."""
    assert _t("pt-PT-x-acores", "azul") == "ɐˈzuɫ"


def test_acores_preserves_the_ou_diphthong():
    """Azorean keeps the falling ⟨ou⟩ diphthong [ow] where standard Lisbon
    monophthongises to [o]: touradas → [toˈwɾadɐʃ] vs base [toˈɾadɐʃ]."""
    assert _t("pt-PT-x-acores", "touradas") == "toˈwɾadɐʃ"
    assert _t("pt-PT", "touradas") == "toˈɾadɐʃ"


def test_acores_prevocalic_s_sandhi_is_palatal():
    """The shared Algarvean-Azorean external sandhi: a word-final /s/ is [ʒ]
    before a vowel-initial word (estás a ver → [eˈʃtaʒ …]), where the base has
    [z]. The clitic article o is pinned to [u]: os olhos → [uʒ ˈoʎuʃ]."""
    assert _t("pt-PT-x-acores", "estás a ver").startswith("eˈʃtaʒ")
    assert _t("pt-PT-x-acores", "os olhos") == "uʒ ˈoʎuʃ"


def test_acores_article_o_is_never_fronted():
    """The proclitic guard: the definite article o is pinned [u], never [y],
    so the stressed-/u/ fronting can never mis-fire on it."""
    assert _t("pt-PT-x-acores", "o").replace("ˈ", "") == "u"


# ═════════════════ São Miguel / micaelense (pt-PT-x-sao-miguel) ═══════════

def test_sao_miguel_fronts_u_to_y_even_before_a_coda():
    """Silva (2008: 4): the micaelense [y] < stressed ⟨u⟩ is a property of the
    nucleus, NOT blocked by a coda — fruta → [ˈfrytɐ], and crucially
    azul → [ɐˈzyl] and cruz → [kryʃ] with [y] before the coda. This is why the
    Rogers-based coda guard is dropped for this leaf (contrast pt-PT-x-acores,
    where azul is [ɐˈzuɫ])."""
    assert _t("pt-PT-x-sao-miguel", "fruta") == "ˈfɾytɐ"
    assert _t("pt-PT-x-sao-miguel", "azul") == "ɐˈzyɫ"
    assert _t("pt-PT-x-sao-miguel", "cruz") == "ˈkɾyʃ"
    assert _t("pt-PT-x-acores", "azul") == "ɐˈzuɫ"


def test_sao_miguel_oi_ou_monophthongise_to_front_rounded_o():
    """The second emblematic micaelense vowel: [ø] < the diphthongs ⟨oi⟩/⟨ou⟩
    (Silva 2008: 4, oito [øt], noite [nøt], pouco [pøk]). This diverges from the
    general acores node, which PRESERVES ⟨ou⟩ as [ow]."""
    assert _t("pt-PT-x-sao-miguel", "oito") == "ˈøtu"
    assert _t("pt-PT-x-sao-miguel", "noite") == "ˈnøtɨ"
    assert _t("pt-PT-x-sao-miguel", "pouco") == "ˈpøku"
    assert get("pt-PT-x-sao-miguel").graphemes["ou"] == ["ø"]


def test_sao_miguel_l_palatalises_after_i():
    """Intervocalic /l/ → [ʎ] after /i/, shared with Madeira: quilo → [ˈkiʎu]
    (overview: São Miguel grouped with Madeira, Filipa → 'Flhipa')."""
    assert _t("pt-PT-x-sao-miguel", "quilo") == "ˈkiʎu"


def test_sao_miguel_keeps_coelho_not_coalho():
    """The island-distinguishing conservatism: São Miguel keeps the mid front
    vowel before a palatal ('coêlho' [ɛ]), like the base, where Lisbon
    centralises to [ɐ] ('coâlho'). São Miguel = base ≠ Lisbon."""
    assert _t("pt-PT-x-sao-miguel", "coelho") == _t("pt-PT", "coelho")
    assert _t("pt-PT-x-sao-miguel", "coelho") != _t("pt-PT-x-lisbon", "coelho")


def test_sao_miguel_prevocalic_s_sandhi_is_palatal():
    """The [ʒ] prevocalic external /s/-sandhi, shared with the Algarve:
    os olhos → [uʒ ˈoʎuʃ] (article o pinned [u], sandhi [ʒ])."""
    assert _t("pt-PT-x-sao-miguel", "os olhos") == "uʒ ˈoʎuʃ"


def test_sao_miguel_is_research_tier_and_cites_silva():
    """The leaf is research-tier and cites the Silva (2008) acoustic account
    that grounds the [y]/[ø] fronting."""
    spec = get("pt-PT-x-sao-miguel")
    assert spec.quality.value == "research"
    assert "silva2008" in {s.id for s in spec.sources}


# ═════════════════ Terceira / terceirense (pt-PT-x-terceira) ═══════════════

def test_terceira_does_not_front_u():
    """The DEFINING negative feature: Terceira, unlike São Miguel and the
    western group, does NOT front the stressed /u/ (Mikołajczak 2014: 417-418,
    424 — the labialisation 'não se aplica ao dialeto da Terceira'). So
    muda → [ˈmudɐ] (base value), NOT the São Miguel [ˈmydɐ]."""
    assert _t("pt-PT-x-terceira", "muda") == "ˈmudɐ"
    assert "y" not in _t("pt-PT-x-terceira", "tudo")
    assert _t("pt-PT-x-terceira", "muda") != _t("pt-PT-x-sao-miguel", "muda")


def test_terceira_a_metaphony_before_final_o():
    """Vocalic harmonisation: a stressed /a/ opens to [ɔ] under the final atonic
    [u] of ⟨-o⟩ — pato → [ˈpɔtu], gato → [ˈɡɔtu] (Mikołajczak 2014: 423, after
    Segura & Saramago 2001: 230). The continent has [ˈpatu]. This is the
    pan-insular tonic-harmonisation feature."""
    assert _t("pt-PT-x-terceira", "pato") == "ˈpɔtu"
    assert _t("pt-PT-x-terceira", "gato") == "ˈɡɔtu"
    assert _t("pt-PT", "pato") == "ˈpatu"


def test_terceira_a_metaphony_needs_a_final_o_not_a_final_a():
    """The gate is the final ⟨-o⟩ [u] two segments on: a stressed /a/ before a
    final ⟨-a⟩ ([ɐ], not a trigger) is untouched — casa → [ˈkazɐ], mar →
    [ˈmaɾ]."""
    assert _t("pt-PT-x-terceira", "casa") == "ˈkazɐ"
    assert _t("pt-PT-x-terceira", "mar") == "ˈmaɾ"


def test_terceira_crescent_w_glide_after_a_labial():
    """The individualising terceirense trait: a [w] on-glide before a stressed
    vowel after a labial/labiodental onset — porco → [ˈpwɔɾku], bicho →
    [ˈbwiʃu] (Mikołajczak 2014: 422-423, porco [pwˈorku], bicho [bwˈiʃu])."""
    assert _t("pt-PT-x-terceira", "porco") == "ˈpwɔɾku"
    assert _t("pt-PT-x-terceira", "bicho") == "ˈbwiʃu"


def test_terceira_crescent_glide_needs_a_labial_onset():
    """The glide is labial-conditioned: a stressed vowel after a non-labial
    onset gets no [w] (gato → [ˈɡɔtu], no glide; the harmonic [j]-type glide of
    ceifar/pintar is a documented not-modelled case)."""
    assert "w" not in _t("pt-PT-x-terceira", "gato")


def test_terceira_is_research_tier_and_cites_mikolajczak():
    """The new leaf is research-tier and cites the dedicated Mikołajczak (2014)
    phonetic description of terceirense."""
    spec = get("pt-PT-x-terceira")
    assert spec.quality.value == "research"
    assert "mikolajczak2014" in {s.id for s in spec.sources}
