"""Tests for the three Portuguese/Mirandese gold loaders in
scripts/benchmark.py:

- ``load_mirandese`` (TigreGotico/mirandese_g2p, human gold, row
  ``mirandese_g2p``) — dialect-column split incl. Raiano → ``mwl-x-ifanes``;
- ``load_infopedia_pt`` (TigreGotico/infopedia-pt-ipa) — fixed-seed sampling;
- ``load_portuguese_phonetic_lexicon``
  (TigreGotico/portuguese_phonetic_lexicon) — per-region split, ``|``
  stripping, fixed-seed sampling.

Network access is mocked via benchmark._fetch so these run offline and
deterministically, mirroring tests/test_hitz_basque_loader.py.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


# ─── load_mirandese (human gold) ─────────────────────────────────────────────

_MIRANDESE_TSV = "\n".join([
    "dialect\tword\tipa",
    "central\tabandono\tabɐ̃ˈdonu",
    "central\tcasa\tˈkaz̺ɐ",
    "sendinese\tqualquiera\tkwalˈkjeɾɐ",
    "raiano\tdóndio\tdõdiʉ",
    "raiano\tbúltio\tbʉɫtiʉ",
])


def test_load_mirandese_central_maps_to_mwl(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _MIRANDESE_TSV)
    pairs = benchmark.load_mirandese("mwl", 10)
    assert ("abandono", "abɐ̃ˈdonu") in pairs
    assert ("casa", "ˈkaz̺ɐ") in pairs
    # only central rows are scored under mwl
    assert all(w in {"abandono", "casa"} for w, _ in pairs)


def test_load_mirandese_raiano_maps_to_ifanes(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _MIRANDESE_TSV)
    pairs = benchmark.load_mirandese("mwl-x-ifanes", 10)
    assert pairs == [("dóndio", "dõdiʉ"), ("búltio", "bʉɫtiʉ")]


def test_load_mirandese_sendim_maps_to_sendinese(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _MIRANDESE_TSV)
    pairs = benchmark.load_mirandese("mwl-x-sendim", 10)
    assert pairs == [("qualquiera", "kwalˈkjeɾɐ")]


def test_mirandese_g2p_registered_expert_human():
    assert "mirandese_g2p" in benchmark.DATASETS
    loader, langs = benchmark.DATASETS["mirandese_g2p"]
    assert loader is benchmark.load_mirandese
    assert langs == ["mwl", "mwl-x-ifanes", "mwl-x-sendim"]
    assert benchmark.PROVENANCE["mirandese_g2p"] == "expert-human"
    # the superseded id is gone (renamed, not duplicated)
    assert "mirandese" not in benchmark.DATASETS


# ─── load_infopedia_pt (fixed-seed sampling) ─────────────────────────────────

def _jsonl(rows):
    return "\n".join(json.dumps(r) for r in rows)


def test_load_infopedia_pt_emits_all_pronunciation_variants(monkeypatch):
    data = _jsonl([
        {"word": "casa", "ipa": "ˈkazɐ", "pronunciations": ["ˈkazɐ"]},
        {"word": "voltear", "pronunciations": ["vɔɫtjar", "voɫtjar"]},
    ])
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: data)
    pairs = benchmark.load_infopedia_pt("pt-PT", 10)
    assert ("casa", "ˈkazɐ") in pairs
    assert ("voltear", "vɔɫtjar") in pairs
    assert ("voltear", "voɫtjar") in pairs


def test_load_infopedia_pt_sampling_is_fixed_seed_and_bounded(monkeypatch):
    rows = [{"word": f"w{i}", "pronunciations": [f"p{i}"]} for i in range(50)]
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _jsonl(rows))
    first = benchmark.load_infopedia_pt("pt-PT", 5)
    second = benchmark.load_infopedia_pt("pt-PT", 5)
    assert first == second                 # deterministic
    assert len({w for w, _ in first}) == 5  # capped at limit words
    # a genuine sample, not the alphabetical head (w0..w4)
    assert [w for w, _ in first] != [f"w{i}" for i in range(5)]


def test_infopedia_pt_registered_lexicon_derived():
    assert benchmark.DATASETS["infopedia_pt"][1] == ["pt-PT"]
    assert benchmark.PROVENANCE["infopedia_pt"] == "lexicon-derived"


# ─── load_portuguese_phonetic_lexicon (region split) ─────────────────────────

_LEXICON_CSV = "\n".join([
    "id,word,postag,gender,phones,syllables,region_code",
    "n_male_ovo_lbx,ovo,nome,male,ˈo|vu,o|vo,lbx",
    "n_f_casa_lbx,casa,nome,female,ˈka|zɐ,ca|sa,lbx",
    "n_male_ovo_dli,ovo,nome,male,ˈɔ|vʊ,o|vo,dli",
    "n_x_maputo_map,maputo,nome,,mɐ|ˈpu|tu,ma|pu|to,map",  # non-std, skipped
])


def test_load_lexicon_splits_by_region_and_strips_separator(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _LEXICON_CSV)
    pt = benchmark.load_portuguese_phonetic_lexicon("pt-PT", 10)
    assert ("ovo", "ˈovu") in pt          # lbx, "|" stripped
    assert ("casa", "ˈkazɐ") in pt
    assert all(w in {"ovo", "casa"} for w, _ in pt)
    tl = benchmark.load_portuguese_phonetic_lexicon("pt-TL", 10)
    assert tl == [("ovo", "ˈɔvʊ")]        # dli only


def test_load_lexicon_sampling_is_fixed_seed(monkeypatch):
    rows = ["id,word,postag,gender,phones,syllables,region_code"]
    rows += [f"i{i},w{i},n,,p{i},s{i},lbx" for i in range(40)]
    csv_text = "\n".join(rows)
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: csv_text)
    first = benchmark.load_portuguese_phonetic_lexicon("pt-PT", 5)
    second = benchmark.load_portuguese_phonetic_lexicon("pt-PT", 5)
    assert first == second
    assert len(first) == 5
    assert [w for w, _ in first] != [f"w{i}" for i in range(5)]


def test_lexicon_registered_crowd_scraped():
    assert "portuguese_phonetic_lexicon" in benchmark.DATASETS
    loader, langs = benchmark.DATASETS["portuguese_phonetic_lexicon"]
    assert loader is benchmark.load_portuguese_phonetic_lexicon
    assert langs == ["pt-AO", "pt-BR", "pt-MZ", "pt-PT", "pt-TL"]
    assert benchmark.PROVENANCE["portuguese_phonetic_lexicon"] == "crowd-scraped"
