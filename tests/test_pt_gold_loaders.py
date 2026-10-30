"""Tests for the Portuguese/Mirandese gold loaders in scripts/benchmark.py:

- ``load_mirandese`` (TigreGotico/mirandese_g2p, human gold, row
  ``mirandese_g2p``) — dialect-column split incl. Raiano → ``mwl-x-ifanes``;
- ``load_portuguese_unified``
  (TigreGotico/portuguese-unified-pronunciation-lexicon) — the single
  merged Portuguese gold (Infopedia + Portal lexicon + Wiktionary):
  per-region split, ipa_narrow scoring, variant preservation, fixed-seed
  sampling, untagged-"pt" exclusion.

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


# ─── load_portuguese_unified (region split, narrow IPA, sampling) ───────────

def _jsonl(rows):
    return "\n".join(json.dumps(r, ensure_ascii=False) for r in rows)


_UNIFIED_ROWS = [
    {"word": "casa", "region": "pt-PT", "ipa_narrow": "ˈkazɐ", "ipa_broad": "ˈkaza"},
    {"word": "casa", "region": "pt-PT", "ipa_narrow": "ˈkazɐ"},          # duplicate variant
    {"word": "voltear", "region": "pt-PT", "ipa_narrow": "vɔɫtjˈaɾ"},
    {"word": "voltear", "region": "pt-PT", "ipa_narrow": "voɫtjˈaɾ"},    # real variant
    {"word": "ovo", "region": "pt-TL-x-dili", "ipa_narrow": "ˈɔvʊ"},
    {"word": "maputo", "region": "pt-MZ-x-maputo", "ipa_narrow": "mɐˈputu"},
    {"word": "geral", "region": "pt", "ipa_narrow": "ʒɨˈɾaɫ"},           # untagged: excluded
    {"word": "vazio", "region": "pt-PT", "ipa_narrow": ""},              # empty: skipped
]


def test_load_unified_splits_by_region(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch",
                        lambda url, name: _jsonl(_UNIFIED_ROWS))
    pt = benchmark.load_portuguese_unified("pt-PT", 10)
    words = {w for w, _ in pt}
    assert words == {"casa", "voltear"}
    assert benchmark.load_portuguese_unified("pt-TL", 10) == [("ovo", "ˈɔvʊ")]
    assert benchmark.load_portuguese_unified("pt-MZ", 10) == [("maputo", "mɐˈputu")]


def test_load_unified_excludes_untagged_pt_rows(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch",
                        lambda url, name: _jsonl(_UNIFIED_ROWS))
    for lang in benchmark._PT_UNIFIED_REGIONS:
        assert all(w != "geral"
                   for w, _ in benchmark.load_portuguese_unified(lang, 100))


def test_load_unified_keeps_variants_dedupes_exact(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch",
                        lambda url, name: _jsonl(_UNIFIED_ROWS))
    pt = benchmark.load_portuguese_unified("pt-PT", 10)
    assert pt.count(("casa", "ˈkazɐ")) == 1            # exact dupes collapse
    assert ("voltear", "vɔɫtjˈaɾ") in pt               # both real variants kept
    assert ("voltear", "voɫtjˈaɾ") in pt


def test_load_unified_sampling_is_fixed_seed_and_word_bounded(monkeypatch):
    rows = [{"word": f"w{i}", "region": "pt-PT", "ipa_narrow": f"p{i}"}
            for i in range(50)]
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _jsonl(rows))
    first = benchmark.load_portuguese_unified("pt-PT", 5)
    second = benchmark.load_portuguese_unified("pt-PT", 5)
    assert first == second                  # deterministic
    assert len({w for w, _ in first}) == 5  # capped at limit WORDS
    assert [w for w, _ in first] != [f"w{i}" for i in range(5)]  # not the head


def test_unified_registration_and_provenance():
    loader, langs = benchmark.DATASETS["portuguese_unified"]
    assert loader is benchmark.load_portuguese_unified
    assert langs == sorted(benchmark._PT_UNIFIED_REGIONS)
    assert benchmark.PROVENANCE["portuguese_unified"] == "lexicon-derived"
    # the three superseded datasets are gone (merged, not duplicated)
    for old in ("infopedia_pt", "portuguese_phonetic_lexicon",
                "wiktionary_pt", "styletts2_phonemes"):
        assert old not in benchmark.DATASETS
        assert old not in benchmark.PROVENANCE


def test_vox_communis_registration_and_provenance():
    loader, langs = benchmark.DATASETS["vox_communis"]
    assert loader is benchmark.load_vox_communis
    assert langs == sorted(benchmark._VOX_COMMUNIS_FILES)
    # epitran-built lexicons: competitor tier, never gates
    assert benchmark.PROVENANCE["vox_communis"] == "epitran-derived"
    assert not benchmark.can_gate_promotion("epitran-derived")


def test_load_vox_communis_word_alignment(monkeypatch):
    tsv = "\n".join([
        "path\tclient_id\tsentence_id\tlocale\tduration\tsentence\taligned_sentence\tphonemized_sentence\tsentence_domain\tphone_set\taccents\tvariant\tage\tgender\tspeaker_id",
        "a.mp3\t\t\t\t1.0\tOla mundo\tola mundo\tˈo l a | m ˈu n d u\t\tvxc\t\t\t\t\t1",
        "b.mp3\t\t\t\t1.0\tMau\tmau linha\tm ˈa w\t\tvxc\t\t\t\t\t2",  # count mismatch: skipped
    ])
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: tsv)
    pairs = benchmark.load_vox_communis("ca", 10)
    assert pairs == [("ola", "ˈola"), ("mundo", "mˈundu")]
