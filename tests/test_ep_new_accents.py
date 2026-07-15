"""New European Portuguese accent specs: Coimbra, Braga, São Miguel.

Three deltas over the broad ``pt-PT`` base, enriched from native-speaker
(Portuguese With Leo) accent deep-dives and grounded against Cintra (1971),
Segura (2013) and Rogers (1948):

* ``pt-PT-x-coimbra`` — the conservative central norm ("o sotaque mais neutro
  de Portugal"): keeps the base values Lisbon innovates away from (no
  pre-palatal [ɐ], [ej] kept, [o] for ⟨ou⟩, unstressed /i/ retained) and adds
  only the marked local [ʒ] prevocalic external /s/-sandhi.
* ``pt-PT-x-braga`` — a heavier Northern (Minho) variety: betacism (v → b/β),
  tonic-close-vowel diphthongisation ([e] → [je], [o] → [wo]) and diphthong
  preservation (⟨ou⟩ → [ow], ⟨ei⟩ → [ej]).
* ``pt-PT-x-sao-miguel`` — the micaelense micro-variety: stressed open /u/ → [y]
  fronting, intervocalic /l/ → [ʎ] after /i/, and the [ʒ] prevocalic sandhi,
  keeping the conservative non-centralised mid vowel before palatals ("coêlho"
  vs the Madeiran/Lisbon "coâlho").

Each diagnostic delta is asserted against the ``pt-PT`` base value it departs
from, so the test genuinely exercises the delta (it would fail on the base).
"""
from orthography2ipa import get
from orthography2ipa.g2p import G2P


def _t(code, word):
    return G2P(code).transcribe(word)


# ─── the specs load and declare the expected structure ──────────────────

def test_new_specs_load_and_inherit_base():
    for code in ("pt-PT-x-coimbra", "pt-PT-x-braga", "pt-PT-x-sao-miguel"):
        spec = get(code)
        assert spec.code == code
        # every new spec inherits the pt-PT coda allophony
        ids = [r.id for r in spec.allophone_rules]
        assert "PT_CODA_L_DARK" in ids
        assert "PT_CODA_S_HUSH" in ids
        # dark coda /l/ still fires (inherited)
        assert "ɫ" in _t(code, "sol")


# ─── Coimbra: the [ʒ] prevocalic external /s/-sandhi delta ──────────────

def test_coimbra_prevocalic_s_is_palatal():
    # DELTA: os olhos → [ʒ] (native attestation), where the pt-PT base → [z]
    assert _t("pt-PT-x-coimbra", "os olhos") == "ˈoʒ ˈoʎuʃ"
    assert "ʒ" in _t("pt-PT-x-coimbra", "estás a ver")
    # base contrast: pt-PT keeps [z]
    assert "z" in _t("pt-PT", "estás a ver")
    assert "ʒ" not in _t("pt-PT", "estás a ver")


def test_coimbra_is_conservative_central_norm():
    # keeps the mid front vowel before a palatal (coêlho), NOT the Lisbon [ɐ]
    assert _t("pt-PT-x-coimbra", "coelho") == _t("pt-PT", "coelho")
    assert "ɐʎ" not in _t("pt-PT-x-coimbra", "coelho")
    assert "ɐʎ" in _t("pt-PT-x-lisbon", "coelho")   # Lisbon DOES centralise
    # ⟨ei⟩ kept as [ej] (not the Lisbon [ɐj]); ⟨ou⟩ monophthong [o]
    assert "ej" in _t("pt-PT-x-coimbra", "fevereiro")
    assert "ɐj" in _t("pt-PT-x-lisbon", "fevereiro")
    assert "ow" not in _t("pt-PT-x-coimbra", "pouco")
    # unstressed /i/ retained (Filipa, not the Lisbon "Flipa")
    assert "i" in _t("pt-PT-x-coimbra", "Filipa")


# ─── Braga: Northern betacism + diphthongisation ────────────────────────

def test_braga_betacism():
    # DELTA: /v/ → [b] (vaca → [ˈbakɐ]), where the pt-PT base keeps [v]
    assert _t("pt-PT-x-braga", "vaca") == "ˈbakɐ"
    assert _t("pt-PT-x-braga", "vou") == "ˈbow"
    assert "b" in _t("pt-PT-x-braga", "vacina")
    # base contrast
    assert _t("pt-PT", "vaca") == "ˈvakɐ"


def test_braga_tonic_close_vowel_diphthongisation():
    # close [e] → [je], close [o] → [wo] (Cintra Baixo-Minho marker)
    assert _t("pt-PT-x-braga", "mês") == "ˈmjeʃ"
    assert "je" in _t("pt-PT-x-braga", "ele")
    assert "wo" in _t("pt-PT-x-braga", "avô")
    # base contrast: no diphthongisation
    assert "je" not in _t("pt-PT", "mês")


def test_braga_diphthong_preservation():
    # ⟨ou⟩ → [ow] and ⟨ei⟩ → [ej] kept where Lisbon monophthongises/lowers
    assert "ow" in _t("pt-PT-x-braga", "pouco")
    assert "ej" in _t("pt-PT-x-braga", "fevereiro")
    assert "ow" not in _t("pt-PT-x-lisbon", "pouco")


# ─── São Miguel: /l/ → [ʎ] after /i/, /u/ → [y], and "coêlho" ────────────

def test_sao_miguel_l_palatalisation_after_i():
    # DELTA: intervocalic /l/ → [ʎ] after /i/, where the pt-PT base keeps [l]
    assert _t("pt-PT-x-sao-miguel", "quilo") == "ˈkiʎu"
    assert _t("pt-PT-x-sao-miguel", "Filipa") == "fiˈʎipɐ"
    assert _t("pt-PT-x-sao-miguel", "mochila") == "muˈʃiʎɐ"
    # base contrast
    assert _t("pt-PT", "quilo") == "ˈkilu"
    # gate is exact: /l/ after a non-/i/ front vowel is untouched
    assert "ʎ" not in _t("pt-PT-x-sao-miguel", "teleférico")


def test_sao_miguel_keeps_coelho_not_coalho():
    # the São Miguel "coêlho" keeps the mid vowel; NOT the Lisbon/Madeira "coâlho" [ɐ]
    assert _t("pt-PT-x-sao-miguel", "coelho") == _t("pt-PT", "coelho")
    assert "ɐʎ" not in _t("pt-PT-x-sao-miguel", "coelho")
    assert "ɐʎ" in _t("pt-PT-x-lisbon", "coelho")


def test_sao_miguel_stressed_u_fronting():
    # the stereotyped micaelense /u/ → [y] (número → [ˈnymɨɾu], tu → [ty])
    assert _t("pt-PT-x-sao-miguel", "número") == "ˈnymɨɾu"
    assert _t("pt-PT-x-sao-miguel", "tu") == "ˈty"
    # fronting applies BEFORE a coda too (Silva 2008:4: azul → [ɐˈzyl],
    # cruz → [kryʃ]) — the coda guard the general acores node keeps is dropped
    # for this leaf; see SM_U_FRONTING.
    assert _t("pt-PT-x-sao-miguel", "azul") == "ɐˈzyɫ"
    assert _t("pt-PT-x-sao-miguel", "cruz") == "ˈkɾyʃ"
    # the clitic guard: the article o is [u], never [y]
    assert _t("pt-PT-x-sao-miguel", "o").replace("ˈ", "") == "u"


def test_sao_miguel_prevocalic_s_is_palatal():
    # shares the Algarve [ʒ] prevocalic sandhi
    assert "ʒ" in _t("pt-PT-x-sao-miguel", "estás a ver")
    assert "ʒ" not in _t("pt-PT", "estás a ver")
