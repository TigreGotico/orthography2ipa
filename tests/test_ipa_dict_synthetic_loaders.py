"""Tests for scripts/benchmark.py's synthetic IPA-dictionary loaders:
``load_barranquenho_dict`` (TigreGotico/barranquenho-ipa-dict-synthetic,
``ext-PT-x-barranco``) and ``load_mirandese_dict``
(TigreGotico/mirandese-ipa-dict-synthetic, ``mwl`` and sub-dialects).

Both golds are LLM-generated (research-conditioned), classified at the
``machine-generated`` reliability tier — see docs/evaluation/benchmarks.md. Network
access is mocked out via benchmark._fetch so these run offline and
deterministically, mirroring the other loader tests.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


_BARR_CSV = (
    "barranquenho_orthography,ipa_transcription,part_of_speech,"
    "portuguese_equivalent,spanish_equivalent,phonological_notes\n"
    "abanicu,ɐbɐˈniku,n.m.,leque,abanico,Spanish loan\n"
    "abaxu,ɐˈbaʃu,adv.,abaixo,abajo,monophthong\n"
    ",,,,,\n"                       # malformed: empty orthography + IPA
    "casa,ˈkaza,n.f.,casa,casa,\n"
)

_MIR_CSV = (
    "word,ipa,pos,english,portuguese,dialect,notes\n"
    "l,l,art.m.sg,the,o,central,\n"
    "quien,kjẽ,pron,who,quem,all,\n"
    "ella,ˈeɫa,pron,she,ela,sendinês,\n"
    "lo,lo,art,the,o,raiano,\n"
    ",,,,,central,\n"               # malformed: empty word + IPA
)


def test_load_barranquenho_dict_extracts_pairs(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _BARR_CSV)
    pairs = benchmark.load_barranquenho_dict("ext-PT-x-barranco", 100)
    assert ("abanicu", "ɐbɐˈniku") in pairs
    assert ("casa", "ˈkaza") in pairs
    # malformed empty row is skipped
    assert all(w and ipa for w, ipa in pairs)
    assert len(pairs) == 3


def test_load_barranquenho_dict_respects_limit(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _BARR_CSV)
    pairs = benchmark.load_barranquenho_dict("ext-PT-x-barranco", 1)
    assert pairs == [("abanicu", "ɐbɐˈniku")]


def test_load_mirandese_dict_splits_by_dialect(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _MIR_CSV)
    # central + "all" (dialect-neutral) both score under the Central norm
    assert benchmark.load_mirandese_dict("mwl", 100) == [
        ("l", "l"), ("quien", "kjẽ")]
    # sendinês -> mwl-x-sendim
    assert benchmark.load_mirandese_dict("mwl-x-sendim", 100) == [
        ("ella", "ˈeɫa")]
    # raiano -> mwl-x-ifanes (Ifanês is the Northern/Raiano subdialect)
    assert benchmark.load_mirandese_dict("mwl-x-ifanes", 100) == [("lo", "lo")]


def test_load_mirandese_dict_respects_limit(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _MIR_CSV)
    assert benchmark.load_mirandese_dict("mwl", 1) == [("l", "l")]


def test_synthetic_dicts_score_their_llm_corrected_file():
    for dataset, langs in [("barranquenho_dict", ["ext-PT-x-barranco"]),
                           ("mirandese_dict",
                            ["mwl", "mwl-x-ifanes", "mwl-x-sendim"])]:
        loader, registered = benchmark.DATASETS[dataset]
        assert registered == langs
        with open(benchmark.llm_corrected_path(dataset),
                  encoding="utf-8") as fh:
            rows = [json.loads(line) for line in fh]
        for lang in langs:
            expected = [(r["sentence"], r["ipa"]) for r in rows
                        if r["lect"] == lang]
            assert expected
            assert loader(lang, sys.maxsize) == expected
            assert loader(lang, 1) == expected[:1]


def test_synthetic_dicts_are_silver():
    # An LLM-written gold, corrected or not, has no lexicon and no rules, so
    # its IPA has no error model and can never gate a promotion
    # (docs/specs/quality_tiers.md).
    assert benchmark.PROVENANCE["barranquenho_dict"] == "llm-corrected"
    assert benchmark.PROVENANCE["mirandese_dict"] == "llm-corrected"
    assert not benchmark.can_gate_promotion("llm-corrected")
