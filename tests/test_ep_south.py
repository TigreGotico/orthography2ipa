"""Southern European Portuguese dialects: Alentejano and Algarvio.

These specs inherit the pt-PT base (graphemes, positional rules and the
post-lexical ``allophone_rules`` dark-l / coda-sibilant realisations) and add
their own cited dialect deltas:

- Algarvio: fronting of the STRESSED labio-velar /u/ -> [y] (the defining
  Barlavento feature; Cintra 1971; Brissos 2014; Segura da Cruz 1989), with a
  ``word_exceptions`` proclitic guard so the common clitics (o, no, do, ...)
  keep their correct [u] vowel and are never fronted to [y].
- Alentejano: the defining Beira-Baixa / Alto-Alentejo zone feature is the same
  stressed /u/ -> [y] palatalisation (Cintra 1971, ``a palatalizacao ... da
  vogal tonica u``; explicit [y] in his adjacent Algarvio passage), with the
  same proclitic guard; plus deletion of final unstressed high vowels -u/-i/-e
  (Brissos 2014; Cintra 1971 note 58, reporting Ludtke 1956/57 -- NOT one of
  Cintra's own diagnostics).

Expected forms are grounded in the ep_dialects gold words and the published
example words quoted in the sources.
"""

import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.registry import resolve


@pytest.fixture(scope="module")
def algarve():
    return G2P(resolve("pt-PT-x-algarve"))


@pytest.fixture(scope="module")
def alentejo():
    return G2P(resolve("pt-PT-x-alentejo"))


# ── Algarvio: stressed /u/ -> [y] ────────────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("tudo", "ˈtydu"),   # Brissos (2014): [tˈyd] 'tudo'
    ("lume", "ˈlymɨ"),   # Brissos (2014): [lˈymɨ] 'lume'
    ("mudo", "ˈmydu"),
    ("sul", "ˈsyɫ"),     # stressed lexical /u/ + inherited dark coda l
])
def test_algarve_stressed_u_fronts_to_y(algarve, word, expected):
    assert algarve.transcribe(word) == expected


def test_algarve_fronting_has_front_rounded_vowel(algarve):
    assert "y" in algarve.transcribe("tudo")


def test_algarve_unstressed_u_is_not_fronted(algarve):
    # 'turistas' (ep_dialects gold: tuˈɾiʃtɐʒ) — the /u/ is UNstressed, so the
    # stress='stressed' condition must leave it as [u], never [y].
    out = algarve.transcribe("turistas")
    assert "u" in out
    assert "y" not in out


# ── Algarvio: proclitic guard (regression test for the o -> [y] leak) ─────────

@pytest.mark.parametrize("word,expected", [
    ("o", "ˈu"),    # definite article — [u], NEVER [y]
    ("no", "ˈnu"),  # em + o contraction
    ("do", "ˈdu"),  # de + o contraction
    ("ao", "ˈaw"),  # a + o contraction
])
def test_algarve_proclitics_keep_u_never_front(algarve, word, expected):
    out = algarve.transcribe(word)
    assert out == expected
    assert "y" not in out


def test_algarve_no_mar_proclitic_is_nu(algarve):
    # The prepositional contraction 'no' must be [nu ...], not [ny ...].
    out = algarve.transcribe("no mar")
    assert out.split()[0].endswith("nu")
    assert "y" not in out


# ── Alentejano: defining stressed /u/ -> [y] palatalisation ──────────────────

@pytest.mark.parametrize("word,expected", [
    ("sul", "ˈsyɫ"),    # stressed lexical /u/ + inherited dark coda l
    ("lume", "ˈlym"),   # stressed /u/->[y]; final [ɨ] (< e) then deleted
    ("tudo", "ˈty"),    # /u/->[y]; intervocalic /d/ + final vowel deleted
    ("mudo", "ˈmy"),
])
def test_alentejo_stressed_u_fronts_to_y(alentejo, word, expected):
    # Cintra (1971): 'a palatalizacao, em maior ou menor grau, da vogal tonica u'
    # delimits the Beira-Baixa / Alto-Alentejo zone; [y] is its phonetic value.
    assert alentejo.transcribe(word) == expected


def test_alentejo_unstressed_u_is_not_fronted(alentejo):
    # 'turistas' — the /u/ is UNstressed, so stress='stressed' leaves it [u].
    out = alentejo.transcribe("turistas")
    assert "u" in out
    assert "y" not in out


# ── Alentejano: proclitic guard (o -> [u], never [y]) ─────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("o", "ˈu"),    # definite article — [u], NEVER [y]
    ("no", "ˈnu"),  # em + o contraction
    ("do", "ˈdu"),  # de + o contraction
    ("ao", "ˈaw"),  # a + o contraction
])
def test_alentejo_proclitics_keep_u_never_front(alentejo, word, expected):
    out = alentejo.transcribe(word)
    assert out == expected
    assert "y" not in out


# ── Alentejano: final unstressed high-vowel deletion ─────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("gosto", "ˈɡɔʃt"),   # final [u] (< o) deleted
    ("noite", "ˈnojt"),   # final [ɨ] (< e) deleted
])
def test_alentejo_deletes_final_unstressed_high_vowel(alentejo, word, expected):
    assert alentejo.transcribe(word) == expected


def test_alentejo_keeps_final_low_vowel(alentejo):
    # Sources list only final -u/-i/-e; final /ɐ/ (< -a) is spared.
    out = alentejo.transcribe("calma")
    assert out.endswith("ɐ")


def test_alentejo_keeps_stressed_final_vowel(alentejo):
    # 'café' — the final vowel is STRESSED, so the unstressed condition must
    # not delete it.
    out = alentejo.transcribe("café")
    assert out and out[-1] in "ɛe"


# ── Both inherit the pt-PT base allophony ────────────────────────────────────

@pytest.mark.parametrize("eng_name", ["algarve", "alentejo"])
def test_south_inherits_dark_coda_l(eng_name, algarve, alentejo):
    eng = {"algarve": algarve, "alentejo": alentejo}[eng_name]
    # 'sol' — coda /l/ velarises to [ɫ] (inherited pt-PT PT_CODA_L_DARK).
    assert "ɫ" in eng.transcribe("sol")


def test_alentejo_inherits_coda_sibilant_hush(alentejo):
    # 'gosto' — pre-consonantal coda /s/ -> [ʃ] (inherited PT_CODA_S_HUSH).
    assert "ʃ" in alentejo.transcribe("gosto")


def test_algarve_final_sibilant_voices(algarve):
    # Algarvio delta: word-final /s/ -> [ʒ] (positional_graphemes s/word_final).
    assert algarve.transcribe("mas").endswith("ʒ")
