"""Tests for scripts/benchmark.py's synthetic IPA-dictionary loaders:
``load_barranquenho_dict`` (TigreGotico/barranquenho-ipa-dict-synthetic,
``ext-PT-x-barrancos``) and ``load_mirandese_dict``
(TigreGotico/mirandese-ipa-dict-synthetic, ``mwl`` and sub-dialects).

Both golds are LLM-generated (research-conditioned), classified at the
``machine-generated`` reliability tier — see docs/benchmarks.md. Network
access is mocked out via benchmark._fetch so these run offline and
deterministically, mirroring the other loader tests.
"""
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
    pairs = benchmark.load_barranquenho_dict("ext-PT-x-barrancos", 100)
    assert ("abanicu", "ɐbɐˈniku") in pairs
    assert ("casa", "ˈkaza") in pairs
    # malformed empty row is skipped
    assert all(w and ipa for w, ipa in pairs)
    assert len(pairs) == 3


def test_load_barranquenho_dict_respects_limit(monkeypatch):
    monkeypatch.setattr(benchmark, "_fetch", lambda url, name: _BARR_CSV)
    pairs = benchmark.load_barranquenho_dict("ext-PT-x-barrancos", 1)
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


def test_synthetic_dict_loaders_registered():
    assert benchmark.DATASETS["barranquenho_dict"][0] is \
        benchmark.load_barranquenho_dict
    assert benchmark.DATASETS["barranquenho_dict"][1] == ["ext-PT-x-barrancos"]

    loader, langs = benchmark.DATASETS["mirandese_dict"]
    assert loader is benchmark.load_mirandese_dict
    assert langs == ["mwl", "mwl-x-ifanes", "mwl-x-sendim"]


def test_synthetic_dict_loaders_are_machine_generated():
    # LLM-generated golds must sit at the lowest reliability tier
    assert benchmark.PROVENANCE["barranquenho_dict"] == "machine-generated"
    assert benchmark.PROVENANCE["mirandese_dict"] == "machine-generated"
