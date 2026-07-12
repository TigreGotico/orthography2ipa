"""Uruguayan Portuguese (pt-UY) — Riverense / DPU contact-variety phonology.

Uruguayan Portuguese is the Portuguese-based border-contact vernacular of
northern Uruguay (Rivera), documented as Dialectos Portugueses del Uruguay
(DPU, Elizaincín), 'fronterizo' (Rona) and popularly 'portuñol'. It inherits
Brazilian Portuguese (pt-BR) — its structural base and diffusion norm — and
overrides it with the rural/focused local features and border-Spanish adstrate
traits documented in the literature.

Primary read source: Carvalho, Ana Maria (1998), "Variation and diffusion of
Uruguayan Portuguese in a bilingual border town", Actas do I Simposio
Internacional sobre o Bilingüismo, U. Vigo, pp. 642-651. Two diagnostic
variables: (1) vocalisation of the palatal lateral ⟨lh⟩ /ʎ/ → glide [j]
(pp. 646-647; Rona 1965: 23); (2) retention of dental /t d/ before /i/ — no
palatalisation (p. 646; Rona 1965: 40; Hensey 1972: 60, both via Carvalho).
Secondary (Wikipedia): coda /l/ lateral retention and word-initial alveolar
trill /r/.
"""

import pytest

import orthography2ipa
from orthography2ipa.g2p import G2P


@pytest.fixture(scope="module")
def spec():
    return orthography2ipa.get("pt-UY")


@pytest.fixture(scope="module")
def g2p():
    return G2P("pt-UY")


class TestRegistrationAndAncestry:
    def test_registered(self, spec):
        assert spec.code == "pt-UY"
        assert {"Indo-European", "Romance", "Ibero-Romance"} <= set(spec.family_path)
        assert spec.quality.value == "research"

    def test_parent_is_brazilian_portuguese(self, spec):
        assert spec.parent == "pt-BR"

    def test_spanish_adstrate_declared(self, spec):
        roles = {a.code: a.role.value for a in spec.ancestors}
        assert roles.get("pt-BR") == "parent"
        assert roles.get("es-UY") == "adstrate"


class TestLhVocalisation:
    """⟨lh⟩ /ʎ/ → glide [j] — the focused rural marker (Carvalho 1998: 646-647)."""

    def test_lh_grapheme_glide_first(self, spec):
        assert spec.graphemes.get("lh")[0] == "j", "focused local form is the glide [j]"
        assert "ʎ" in spec.graphemes.get("lh"), "diffusing standard [ʎ] kept as a variant"

    @pytest.mark.parametrize("word", ["mulher", "colher", "trabalho", "filho"])
    def test_lh_realised_as_glide(self, g2p, word):
        out = g2p.transcribe(word)
        assert "j" in out and "ʎ" not in out, f"{word} -> {out} should show [j], not [ʎ]"


class TestDentalStopRetention:
    """Dental /t d/ before /i/ are NOT palatalised (Carvalho 1998: 646-648)."""

    def test_before_i_stays_dental(self, spec):
        assert spec.positional_graphemes["t"][
            list(spec.positional_graphemes["t"])[0]
        ] == ["t"]

    @pytest.mark.parametrize(
        "word,frag", [("dia", "di"), ("tia", "ti"), ("tira", "ti"), ("partido", "ti")]
    )
    def test_no_affrication_before_i(self, g2p, word, frag):
        out = g2p.transcribe(word)
        assert "t͡ʃ" not in out and "d͡ʒ" not in out, f"{word} -> {out} must stay dental"
        assert frag in out, f"{word} -> {out} should contain dental {frag}"


class TestCodaLRetention:
    """Coda /l/ stays lateral [l] — no L-vocalisation to [w] (Wikipedia, secondary)."""

    @pytest.mark.parametrize("word", ["Brasil", "sal", "alto", "sul"])
    def test_coda_l_not_vocalised(self, g2p, word):
        out = g2p.transcribe(word)
        assert "w" not in out, f"{word} -> {out} must NOT vocalise coda /l/ to [w]"
        assert "l" in out, f"{word} -> {out} should keep lateral [l]"


class TestAlveolarTrill:
    """Word-initial ⟨r⟩ and ⟨rr⟩ = alveolar trill [r], not guttural [ʁ] (Wikipedia)."""

    def test_rr_grapheme_is_trill(self, spec):
        assert spec.graphemes.get("rr") == ["r"]

    @pytest.mark.parametrize("word", ["Rivera", "carro", "rua", "roda"])
    def test_no_guttural_r(self, g2p, word):
        out = g2p.transcribe(word)
        assert "ʁ" not in out and "χ" not in out, f"{word} -> {out} must have alveolar [r]"


class TestBrazilianBaseRetained:
    """Vowels and non-overridden segments follow the Brazilian base."""

    @pytest.mark.parametrize(
        "word,expected",
        [
            ("mulher", "muˈjeɾ"),   # lh -> [j]; final -r tap
            ("dia", "ˈdiɐ"),        # dental d before i
            ("tia", "ˈtiɐ"),        # dental t before i
            ("Brasil", "bɾaˈzil"),  # coda l retained; alveolar r
            ("carro", "ˈkaru"),     # rr -> trill [r]
        ],
    )
    def test_whole_word(self, g2p, word, expected):
        assert g2p.transcribe(word) == expected

    def test_v_not_betacised(self, g2p):
        # Unlike Barranquenho, DPU keeps /v/ (no betacism).
        assert "v" in g2p.transcribe("vida")
