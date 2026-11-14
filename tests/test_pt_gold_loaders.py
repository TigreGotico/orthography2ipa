"""Tests for the Portuguese/Mirandese gold loaders in scripts/benchmark.py:

- ``load_mirandese`` (TigreGotico/mirandese_g2p, human gold, row
  ``mirandese_g2p``) — dialect-column split incl. Raiano → ``mwl-x-ifanes``;
- ``load_portuguese_unified`` and ``load_portal_lupo``
  (TigreGotico/portuguese-unified-pronunciation-lexicon): the human rows
  (Infopédia + pt.wiktionary) and the Portal LUPo rows of one merged file —
  source split, per-region split, ipa_narrow scoring, variant preservation,
  fixed-seed sampling, untagged-"pt" exclusion.

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


_INFOPEDIA = {"infopedia_url": "https://www.infopedia.pt/x"}
_PORTAL = {"phones": "ˈɔ|vʊ"}

_UNIFIED_ROWS = [
    {"word": "casa", "region": "pt-PT", "ipa_narrow": "ˈkazɐ", "ipa_broad": "ˈkaza",
     **_INFOPEDIA},
    {"word": "casa", "region": "pt-PT", "ipa_narrow": "ˈkazɐ"},          # duplicate variant
    {"word": "voltear", "region": "pt-PT", "ipa_narrow": "vɔɫtjˈaɾ"},
    {"word": "voltear", "region": "pt-PT", "ipa_narrow": "voɫtjˈaɾ"},    # real variant
    {"word": "ovo", "region": "pt-TL-x-dili", "ipa_narrow": "ˈɔvʊ", **_PORTAL},
    {"word": "maputo", "region": "pt-MZ-x-maputo", "ipa_narrow": "mɐˈputu", **_PORTAL},
    {"word": "geral", "region": "pt", "ipa_narrow": "ʒɨˈɾaɫ"},           # untagged: excluded
    {"word": "vazio", "region": "pt-PT", "ipa_narrow": ""},              # empty: skipped
]


def test_load_unified_splits_by_region(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch",
                        lambda url, name: _jsonl(_UNIFIED_ROWS))
    pt = benchmark.load_portuguese_unified("pt-PT", 10)
    words = {w for w, _ in pt}
    assert words == {"casa", "voltear"}
    assert benchmark.load_portal_lupo("pt-TL", 10) == [("ovo", "ˈɔvʊ")]
    assert benchmark.load_portal_lupo("pt-MZ", 10) == [("maputo", "mɐˈputu")]


#: One human row and one Portal row in every region the dataset holds, each
#: with a reading that names its source, so a returned pair shows which row it
#: came from.
_SOURCE_REGIONS = ("pt-PT", "pt-BR", "pt-BR-x-carioca", "pt-BR-x-caipira",
                   "pt-PT-x-lisboa", "pt-BR-x-saopaulo", "pt-BR-x-riodejaneiro",
                   "pt-AO", "pt-MZ-x-maputo", "pt-TL-x-dili")
_SOURCE_ROWS = [
    row for region in _SOURCE_REGIONS for row in (
        {"word": "falar", "region": region, "ipa_narrow": f"human-{region}",
         "wiktionary_url": "https://pt.wiktionary.org/wiki/falar"},
        {"word": "falar", "region": region, "ipa_narrow": f"portal-{region}",
         "phones": "fɐ|ˈlaɾ"},
    )
]


def test_unified_loaders_never_return_a_portal_row(monkeypatch):
    """The Portal rows are LUPo generator output, not human transcriptions:
    no language of ``portuguese_unified`` or its overlay reads one."""
    monkeypatch.setattr(benchmark, "_fetch",
                        lambda url, name: _jsonl(_SOURCE_ROWS))
    portal = {r["ipa_narrow"] for r in _SOURCE_ROWS if r.get("phones")}
    read = []
    for dataset in ("portuguese_unified", "portuguese_unified_corrected"):
        loader, langs = benchmark.DATASETS[dataset]
        for lang in langs:
            pairs = loader(lang, 100)
            assert pairs, (dataset, lang)
            read += [(dataset, lang, ipa) for _, ipa in pairs]
    assert [r for r in read if r[2] in portal] == []
    assert len(read) == len(benchmark.DATASETS["portuguese_unified"][1]) + len(
        benchmark.DATASETS["portuguese_unified_corrected"][1])


def test_portal_lupo_returns_only_portal_rows(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch",
                        lambda url, name: _jsonl(_SOURCE_ROWS))
    loader, langs = benchmark.DATASETS["portal_lupo"]
    assert loader is benchmark.load_portal_lupo
    assert langs == sorted(benchmark._PORTAL_LUPO_REGIONS)
    for lang in langs:
        region = benchmark._PORTAL_LUPO_REGIONS[lang]
        assert loader(lang, 100) == [("falar", f"portal-{region}")]


def test_michaelis_rows_are_human_pt_br_rows(monkeypatch):
    """A Michaelis row carries no ``phones`` and no Infopédia or Wiktionary
    URL. It is a dictionary transcription: the pt-BR human loader reads it and
    the Portal loader does not."""
    rows = [
        {"word": "calva", "region": "pt-BR", "ipa_narrow": "ˈkawvɐ",
         "michaelis_url": "https://michaelis.uol.com.br/x/calva/"},
        {"word": "calva", "region": "pt-BR-x-saopaulo", "ipa_narrow": "ˈkaw.və",
         "phones": "ˈkaw|və"},
    ]
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _jsonl(rows))
    assert benchmark.pt_unified_source(rows[0]) == "michaelis"
    assert benchmark.load_portuguese_unified("pt-BR", 10) == [("calva", "ˈkawvɐ")]
    assert benchmark.load_portal_lupo("pt-BR-x-sp", 10) == [("calva", "ˈkaw.və")]


def test_unified_and_portal_regions_do_not_overlap():
    """A language reads one source kind: human rows or the generator."""
    assert not set(benchmark._PT_UNIFIED_REGIONS) & set(benchmark._PORTAL_LUPO_REGIONS)
    assert not (set(benchmark._PT_UNIFIED_REGIONS.values())
                & set(benchmark._PORTAL_LUPO_REGIONS.values()))


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
    for lang in ("pt-PT", "pt-BR"):
        assert benchmark.provenance_for("portuguese_unified", lang) == "lexicon-derived"
    for lang in ("pt-BR-x-carioca", "pt-BR-x-caipira"):
        assert benchmark.provenance_for("portuguese_unified", lang) == "crowd-scraped"
    for lang in benchmark._PORTAL_LUPO_REGIONS:
        assert benchmark.provenance_for("portal_lupo", lang) == "lupo-derived"
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
