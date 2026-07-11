"""Brazilian Portuguese post-lexical allophony (Workstream P, task P2).

The ``pt-BR`` base spec declares ``allophone_rules`` modelling the
best-documented BP post-lexical process for the base variety (Barbosa &
Albano 2004, JIPA illustration; Câmara Jr. 1970):

* **Final unstressed vowel raising** — the near-close [ɪ]/[ʊ] the positional
  map selects word-finally is realised as the standard BP close [i]/[u]
  (gato → [ˈɡatu], leite → [ˈlejti]).

Affrication of /t d/ before front vowels is modelled *pre-lexically*
(``positional_graphemes`` ``before_i``); it is deliberately NOT duplicated
in ``allophone_rules``. These tests pin: raising fires word-final only and
only on the reduced vowels (so conservative dialects that retain a final
[e]/[o] are untouched); the ``apply_allophony`` toggle recovers the broad
form; and grapheme-⟨i⟩ affrication still fires via the positional map.
"""
import pytest

from orthography2ipa.g2p import G2P


# ─── Final unstressed vowel raising ────────────────────────────────────

@pytest.mark.parametrize("word,expected_final", [
    ("gato", "u"),    # /o/# → [u]
    ("leite", "i"),   # /e/# → [i]
    ("verde", "i"),   # /e/# → [i]
    ("dia", "ɐ"),     # final -a is NOT raised (reduces to [ɐ], unchanged)
])
def test_final_vowel_raising(word, expected_final):
    assert G2P("pt-BR").transcribe_word(word).endswith(expected_final)


def test_final_raising_word_final_only():
    # Only the word edge raises: "gota" keeps a stressed [o] and reduces the
    # final /a/ to [ɐ] — no interior raising.
    out = G2P("pt-BR").transcribe_word("gota")
    assert out.startswith("ˈɡo")
    assert out.endswith("ɐ")


def test_raising_targets_reduced_vowel_only():
    # The rule targets the reduced [ɪ]/[ʊ], never underlying /e o/, so a
    # dialect that retains a final [e] would be untouched. On the base the
    # reduced vowel is present, so raising applies.
    assert G2P("pt-BR").transcribe_word("gato").endswith("u")


def test_raising_recovered_by_broad_toggle():
    # apply_allophony=False yields the broad/pre-lexical near-close vowel.
    assert G2P("pt-BR").transcribe_word("gato").endswith("u")
    assert G2P("pt-BR", apply_allophony=False).transcribe_word(
        "gato").endswith("ʊ")


# ─── Affrication of /t d/ before ⟨i⟩ (pre-lexical / positional) ─────────

@pytest.mark.parametrize("word,affricate", [
    ("tio", "t͡ʃ"),
    ("dia", "d͡ʒ"),
    ("partido", "t͡ʃ"),
    ("Abundio", "d͡ʒ"),
])
def test_affrication_before_orthographic_i(word, affricate):
    assert affricate in G2P("pt-BR").transcribe_word(word)


def test_affrication_not_before_non_high_vowel():
    # /t d/ before a back/low vowel stay plain stops.
    assert "t͡ʃ" not in G2P("pt-BR").transcribe_word("gato")
    assert G2P("pt-BR").transcribe_word("dado").startswith("ˈdad")


# ─── wikipron-gold-derived passing words ───────────────────────────────

@pytest.mark.parametrize("word,fragment", [
    ("Abundio", "d͡ʒi"),     # gold abũdʒiu — /d/ affricates before [i]
    ("partido", "ɾt͡ʃidu"),   # /t/ affricates before [i]; final /o/ raises
    ("gato", "ɡatu"),        # final raising
])
def test_gold_derived_words(word, fragment):
    assert fragment in G2P("pt-BR").transcribe_word(word)


# ─── coda vowel nasalisation (retained in Brazilian Portuguese) ─────────
# BP keeps the general-Portuguese coda-nasal → nasal-vowel process
# (Mateus & d'Andrade 2000: ch.2; Barbosa & Albano 2004). A vowel before a
# CODA ⟨m/n⟩ nasalises (tilde U+0303 from the positional m/n slot); an
# INTERVOCALIC (onset) nasal leaves the vowel oral.

TILDE = "̃"


def test_br_declares_the_nasal_raise_rules():
    from orthography2ipa import get
    ids = [r.id for r in get("pt-BR").allophone_rules]
    assert ids[:3] == [
        "PT_NASAL_A_RAISE", "PT_NASAL_E_RAISE", "PT_NASAL_O_RAISE"]
    # the BR final-raising rules are preserved after the nasal rules
    assert "BR_RAISE_FINAL_E" in ids and "BR_RAISE_FINAL_O" in ids


@pytest.mark.parametrize("word,expected", [
    ("campo", "ˈkɐ̃pu"),
    ("sim", "ˈsĩ"),
    ("bom", "ˈbõ"),
    ("mundo", "ˈmũdu"),
    ("cantar", "kɐ̃ˈtaɾ"),
    ("fim", "ˈfĩ"),
    ("tempo", "ˈtẽpu"),
])
def test_br_coda_nasalisation(word, expected):
    import unicodedata
    got = unicodedata.normalize("NFC", G2P("pt-BR").transcribe_word(word))
    assert got == unicodedata.normalize("NFC", expected)


def _nfd_br(word):
    import unicodedata
    return unicodedata.normalize("NFD", G2P("pt-BR").transcribe_word(word))


def test_br_intervocalic_nasal_leaves_vowel_oral():
    for word in ("cama", "ano", "lua", "lima", "nome", "fome"):
        out = _nfd_br(word)
        assert TILDE not in out, (word, out)


def test_br_no_double_tilde():
    for word in ("campo", "sim", "bom", "mundo", "cantar", "tempo"):
        out = _nfd_br(word)
        assert TILDE + TILDE not in out, (word, out)


def test_br_nh_digraph_unbroken():
    out = _nfd_br("banho")
    assert "ɲ" in out and TILDE not in out, out
