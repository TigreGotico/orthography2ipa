"""A syllable-final nasal inside a word is velar before a velar consonant.

Navarro Tomás, Manual de pronunciación española (1918), § 133, pp. 111-112:
"La n final de sílaba, en contacto con una consonante velar siguiente, se
asimila en la conversación ordinaria, por lo que a la posición de la lengua se
refiere, a la articulación de dicha consonante velar". His examples inside a
word: cinco [θíŋko], banco [báŋko], ronco, manco [máŋko], lengua, pongo, monja,
enjambre and fingir, all with [ŋ]. § 111 (p. 86) gives cinco with [ŋ], and
§ 149 (p. 134) gives nunca and lonja with [ŋ].

The rule takes a syllable-final nasal only. In anual and continuo the nasal
begins the syllable of the glide, so it is not in the context.

Where ⟨j⟩ or ⟨g⟩ before a front vowel is the glottal [h] (es-CU, es-HN,
es-ES-x-canarias and others), [h] is not a velar consonant, and the nasal
before it stays [n], as it does across a word boundary.
"""
import pytest

from orthography2ipa.g2p import G2P

# Each word with Navarro's own reading, written with the engine's stress mark.
NAVARRO_ES_ES = [
    ("cinco", "ˈθiŋko"),
    ("banco", "ˈbaŋko"),
    ("ronco", "ˈroŋko"),
    ("manco", "ˈmaŋko"),
    ("lengua", "ˈleŋɡwa"),
    ("pongo", "ˈpoŋɡo"),
    ("monja", "ˈmoŋxa"),
    ("enjambre", "eŋˈxambɾe"),
    ("fingir", "fiŋˈxiɾ"),
    ("nunca", "ˈnuŋka"),
    ("lonja", "ˈloŋxa"),
]

# The specs that inherit the es-ES rule unchanged.
INHERIT = [
    "es-ES", "es-419", "es-AR", "es-AR-x-cordoba", "es-AR-x-cuyo",
    "es-AR-x-litoral", "es-AR-x-norte", "es-AR-x-patagoni", "es-BO",
    "es-BO-x-andino", "es-BO-x-camba", "es-CL", "es-CL-x-andino",
    "es-CL-x-chilote", "es-CO", "es-CO-x-costa", "es-CO-x-paisa",
    "es-CO-x-santande", "es-CO-x-valluno", "es-CR", "es-CU", "es-DO", "es-EC",
    "es-EC-x-andino", "es-EC-x-costa", "es-ES-x-andalusi-e",
    "es-ES-x-andalusi-w", "es-ES-x-cantabri", "es-ES-x-murcia", "es-GQ",
    "es-GT", "es-MX", "es-MX-x-costa", "es-MX-x-norte", "es-MX-x-yucatan",
    "es-NI", "es-PA", "es-PE", "es-PE-x-amazonia", "es-PE-x-andino",
    "es-PE-x-lima", "es-PR", "es-PY", "es-UY", "es-VE", "es-VE-x-andino",
    "es-VE-x-zulia", "ext", "ast-x-cantabri", "ast-x-pasiego",
]
# The specs whose /x/ is [h] by an allophone rule; they keep the rule for k ɡ ɣ w.
H_BY_RULE = [
    "es-CO-x-llanero", "es-CO-x-pacifico", "es-ES-x-canarias",
    "es-ES-x-extremad", "es-HN", "es-SV", "es-VE-x-llanero",
]
CREOLES = ["cbk-PH", "cbk-PH-x-cavite", "cbk-PH-x-ternate", "pln"]
# The specs whose grapheme table spells ⟨j⟩ and ⟨g⟩ before a front vowel [h].
H_SPELLING = ["es-CU", "es-DO", "es-MX-x-yucatan"]
J_IS_X = [c for c in INHERIT if c not in H_SPELLING]
J_IS_H = H_BY_RULE + H_SPELLING
# ext spells ⟨j⟩ [x] but ⟨g⟩ before a front vowel [h].
GI_IS_X = [c for c in J_IS_X if c != "ext"]
GI_IS_H = J_IS_H + ["ext"]


def _nasal_before(ipa, consonants):
    """The nasal written immediately before each of *consonants* in *ipa*."""
    plain = ipa.replace("ˈ", "").replace("ˌ", "")
    return [plain[i - 1] for i, c in enumerate(plain) if c in consonants and i > 0]


@pytest.mark.parametrize("word, expected", NAVARRO_ES_ES)
def test_es_es_gives_navarros_velar_nasal(word, expected):
    assert G2P("es-ES").transcribe_word(word) == expected


@pytest.mark.parametrize("code", INHERIT + H_BY_RULE)
@pytest.mark.parametrize("word", ["cinco", "banco", "nunca", "tengo", "lengua", "pongo"])
def test_nasal_before_k_and_g_is_velar_in_every_child(code, word):
    ipa = G2P(code).transcribe_word(word)
    assert _nasal_before(ipa, "kɡ") == ["ŋ"], ipa


@pytest.mark.parametrize("code, word", [(c, w) for w in ("monja", "lonja", "enjambre") for c in J_IS_X]
                         + [(c, "fingir") for c in GI_IS_X])
def test_nasal_before_x_is_velar(code, word):
    ipa = G2P(code).transcribe_word(word)
    assert "ŋx" in ipa.replace("ˈ", "") and "n" not in ipa, ipa


@pytest.mark.parametrize("code, word", [(c, w) for w in ("monja", "lonja", "enjambre") for c in J_IS_H]
                         + [(c, "fingir") for c in GI_IS_H])
def test_nasal_before_glottal_h_stays_n(code, word):
    ipa = G2P(code).transcribe_word(word)
    assert "nh" in ipa.replace("ˈ", "") and "ŋ" not in ipa, ipa


@pytest.mark.parametrize("code", ["es-ES"] + INHERIT[1:6] + H_BY_RULE[:2])
@pytest.mark.parametrize("word, expected", [
    ("anual", "aˈnwal"),
    ("continuo", "konˈtinwo"),
])
def test_onset_nasal_before_a_glide_stays_n(code, word, expected):
    assert G2P(code).transcribe_word(word) == expected


@pytest.mark.parametrize("word, expected", [
    ("ancho", "ˈantʃo"),
    ("enfermo", "enˈfeɾmo"),
    ("envase", "emˈbase"),
    ("canto", "ˈkanto"),
])
def test_nasal_before_other_consonants_is_unchanged(word, expected):
    assert G2P("es-ES").transcribe_word(word) == expected


@pytest.mark.parametrize("code", CREOLES)
@pytest.mark.parametrize("word", ["cinco", "banco", "nunca"])
def test_creoles_keep_the_nasal(code, word):
    ipa = G2P(code).transcribe_word(word)
    assert _nasal_before(ipa, "k") == ["n"], ipa
