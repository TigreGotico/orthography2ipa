"""Lithuanian palatalization: the process that dominates its residual PER.

Lithuanian consonants contrast palatalized/non-palatalized before front
vowels, and orthography marks that contrast before a BACK vowel with a
silent ⟨i⟩ that is not itself pronounced -- ⟨čia⟩ is /tʃʲa/, not /tʃia/
(Bakšienė, Čepaitienė, Jaroslavienė & Urbanavičienė, "Standard Lithuanian",
JIPA 54(1), 2024, pp. 414-444, doi:10.1017/S0025100323000105; Ambrazas (ed.),
*Lithuanian Grammar*, Vilnius: Baltos Lankos, 1997).

Before this fix the spec had no palatalization at all and read the silent
⟨i⟩ as a full vowel, so every ⟨Ci⟩+back-vowel sequence spelled out a
spurious /i/ that never surfaces (WikiPron gold: ⟨niukti⟩ -> [nʲʊktʲɪ], never
[nʲiʊktʲɪ]).
"""
from orthography2ipa import transcribe


def t(word: str) -> str:
    return transcribe(word, "lt")


# ─── The silent ⟨i⟩ before a back vowel does not surface ──────────────────

def test_cia_digraph_has_no_vowel_i():
    # ⟨čia⟩ = /tʃʲa/, not /tʃia/ -- the ⟨i⟩ is a palatalization mark only.
    ipa = t("čia")
    assert "tʃʲa" in ipa
    assert "tʃʲia" not in ipa and "tʃia" not in ipa


def test_delcia_matches_wikipron_shape():
    # WikiPron gold: delčia -> d ɛ l tʃ ɛ (no /i/ segment at all).
    ipa = t("delčia")
    assert "i" not in ipa


def test_niukti_matches_wikipron_gold():
    # WikiPron gold: niukti -> nʲ ʊ k tʲ ɪ
    assert t("niukti") == "nʲʊktʲɪ"


def test_derlius_matches_wikipron_gold():
    # WikiPron gold: derlius -> dʲ ɛ r lʲ ʊ s
    assert t("derlius") == "dʲɛrlʲʊs"


# ─── Consonants palatalize before front vowels (e ę ė i į y) ──────────────

def test_consonant_palatalizes_before_front_vowel():
    assert t("derlius").startswith("dʲ")
    assert t("niukti").startswith("nʲ")


def test_consonant_stays_plain_before_back_vowel():
    # No following front vowel / silent-i marker -> no palatalization.
    ipa = t("bosas")  # b + o (back vowel)
    assert not ipa.startswith("bʲ")


# ─── ą ę į ų mark historical LENGTH, never nasality ───────────────────────

def test_ogonek_vowels_are_long_not_nasal():
    from orthography2ipa import get
    spec = get("lt")
    for letter, ipa in (("ą", "aː"), ("ę", "ɛː"), ("į", "iː"), ("ų", "uː")):
        assert spec.graphemes[letter] == [ipa]
        assert "̃" not in ipa[0]  # no combining tilde (nasal marker)
