"""Paper-grounded refinements to the continental EP dialect specs.

Two acoustic-atlas findings from Fernando Brissos's AVOC work are exercised
here, each cited to the printed page it was read on:

* **Bilabial-context guard on /u/-fronting** (Centro-Sul: beira, alentejo,
  algarve). Brissos (2014b), *A vogal u, os dialectos do Centro-Sul português
  e a dialectologia acústica* (APL, pp. 85-102), shows the famous stressed
  /u/ → [y]/[ʉ] fronting is context-conditioned: **after a bilabial onset
  (/p, b, m/) the vowel loses most of its advancement and identifies with
  [u]** — Praia da Salema (Barlavento): 25 % of the F2 acoustic space after a
  bilabial ("muito mais perto de [u] do que de [y]", pp. 87-88) vs 64 %
  elsewhere; Alpalhão (Centro-Interior): 11 % ("identificando-se assim com
  [u]", p. 89). Modelled as a ``*_U_NO_FRONT_AFTER_BILABIAL`` guard ordered
  before the fronting rule, so /p,b,m/ + /u/ stays [u] while every other
  onset still fronts.

* **Open-mid diphthongisation in the Northwest** (porto, braga). Brissos
  (2018), *Proposta de reformulação da caracterização dialetal do noroeste
  português* (Estudos de Lingüística Galega, vol. esp. I: 193-208), reporting
  Brissos & Rodrigues (2016, *Revue Romane* 51-1), overturns the close-mid-only
  view: NW tonic diphthongisation reaches the **open** mids too — ``[ˈpi̯ɛ]``
  'pé', ``[ˈtu̯ɔkɨ]`` 'toque' (pp. 196-197, 200-201) — so only the cardinal
  vowels stay stable. Modelled as ``*_DIPHTHONGISE_E_OPEN`` ([ɛ] → [jɛ]) and
  ``*_DIPHTHONGISE_O_OPEN`` ([ɔ] → [wɔ]).
"""
from __future__ import annotations

import pytest

from orthography2ipa.g2p import G2P


def _t(code, word):
    return G2P(code).transcribe(word)


# ── Centro-Sul: /u/ not fronted after a bilabial (Brissos 2014b) ─────────────

@pytest.mark.parametrize("code", ["pt-PT-x-beira", "pt-PT-x-alentejo",
                                  "pt-PT-x-algarve"])
def test_bilabial_blocks_u_fronting(code):
    # 'puro' /p/, 'burro' /b/, 'mudo' /m/ — bilabial onsets keep the stressed
    # /u/ as [u]; the guard fires before the fronting rule.
    for word in ("puro", "burro", "mudo"):
        assert "y" not in _t(code, word), f"{code} {word} should not front /u/"


@pytest.mark.parametrize("code", ["pt-PT-x-beira", "pt-PT-x-alentejo",
                                  "pt-PT-x-algarve"])
def test_nonbilabial_u_still_fronts(code):
    # the guard is exact: non-bilabial onsets (t-, s-, l-) still front to [y].
    assert "y" in _t(code, "tudo")   # /t/
    assert "y" in _t(code, "sul")    # /s/
    assert "y" in _t(code, "lume")   # /l/


def test_beira_bilabial_guard_exact():
    assert _t("pt-PT-x-beira", "mudo") == "ˈmudu"
    assert _t("pt-PT-x-beira", "puro") == "ˈpuɾu"
    # contrast: non-bilabial fronts (apico-alveolar s beirão)
    assert _t("pt-PT-x-beira", "sul") == "ˈs̺yɫ"


def test_algarve_bilabial_guard_exact():
    assert _t("pt-PT-x-algarve", "mudo") == "ˈmudu"
    assert _t("pt-PT-x-algarve", "tudo") == "ˈtydu"


def test_alentejo_bilabial_guard_with_final_deletion():
    # 'mudo': /m/ blocks fronting; /d/ deletes intervocalically; final /u/
    # deletes — [ˈmu]. 'tudo' (non-bilabial) fronts: [ˈty].
    assert _t("pt-PT-x-alentejo", "mudo") == "ˈmu"
    assert _t("pt-PT-x-alentejo", "tudo") == "ˈty"


# ── Northwest: open-mid diphthongisation (Brissos 2018) ──────────────────────

@pytest.mark.parametrize("code", ["pt-PT-x-porto", "pt-PT-x-braga"])
def test_open_mid_front_diphthongises(code):
    # [ɛ] → [jɛ]: pé, café. Reproduces Brissos (2018) [ˈpi̯ɛ] 'pé'.
    assert _t(code, "pé") == "ˈpjɛ"
    assert _t(code, "café") == "kɐˈfjɛ"


@pytest.mark.parametrize("code", ["pt-PT-x-porto", "pt-PT-x-braga"])
def test_open_mid_back_diphthongises(code):
    # [ɔ] → [wɔ]: só, avó.
    assert _t(code, "só") == "ˈswɔ"
    assert _t(code, "avó") == "ɐˈbwɔ"


@pytest.mark.parametrize("code", ["pt-PT-x-porto", "pt-PT-x-braga"])
def test_close_mid_diphthongisation_still_fires(code):
    # the pre-existing close-mid rules are untouched: [e] → [je], [o] → [wo].
    assert _t(code, "mês") == "ˈmjeʃ"
    assert _t(code, "avô") == "ɐˈbwo"


def test_cardinal_vowels_stay_stable_in_nw():
    # only the mids diphthongise; the cardinals [a i u] do not.
    assert _t("pt-PT-x-porto", "vaca") == "ˈbakɐ"   # [a] stable (+ betacism)
    assert _t("pt-PT-x-porto", "vida") == "ˈbidɐ"   # [i] stable
    assert _t("pt-PT-x-porto", "uva") == "ˈubɐ"     # [u] stable
