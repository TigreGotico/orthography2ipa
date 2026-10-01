"""Tests for scripts/benchmark.py's ``load_alphacep_ru_book`` loader
(alphacep/biggest-ru-book-cleanup).

The dataset file is stubbed out via monkeypatching ``huggingface_hub.
hf_hub_download`` so these run offline and deterministically, mirroring the
other loader test modules. One test reads the real cached dataset file (if
present in the local HF cache) to check segment-mapping completeness against
the actual shipped notation.
"""
import glob
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402


def _stub_hf_hub_download(monkeypatch, tmp_path, text):
    dest = tmp_path / "metadata-phones-ids.csv.dev"
    dest.write_text(text, encoding="utf-8")

    def _fake(*, repo_id, filename, repo_type):
        assert repo_id == "alphacep/biggest-ru-book-cleanup"
        assert filename == "metadata-phones-ids.csv.dev"
        assert repo_type == "dataset"
        return str(dest)

    import huggingface_hub
    monkeypatch.setattr(huggingface_hub, "hf_hub_download", _fake)


def test_molchal_is_unreduced_and_stressed(monkeypatch, tmp_path):
    """молчал: no akanje (unreduced [o]/[a]), stress on the final syllable.

    m_o0_l_ch_a1_l -> m o ɫ t͡ɕ ˈa ɫ, i.e. moɫt͡ɕˈaɫ. A surface-phonetic
    transcription would reduce the pretonic [o] to [ɐ]; this gold keeps it,
    per its morphophonemic/accentuator-driven production method.
    """
    text = "x.wav|Кардинал молчал.|k_a0_r_dj_i0_n_a1_l m_o0_l_ch_a1_l.\n"
    _stub_hf_hub_download(monkeypatch, tmp_path, text)

    pairs = dict(benchmark.load_alphacep_ru_book("ru", 100))

    assert pairs["молчал"] == "moɫt͡ɕˈaɫ"


def test_palatalized_cj_suffix_maps_to_ipa_j(monkeypatch, tmp_path):
    """``tj`` (Cj palatalization code) maps to /tʲ/, not a bare /t/+/j/."""
    text = "x.wav|тень.|tj_e0_nj.\n"
    _stub_hf_hub_download(monkeypatch, tmp_path, text)

    pairs = dict(benchmark.load_alphacep_ru_book("ru", 100))

    assert pairs["тень"] == "tʲenʲ"


def test_hard_and_soft_lateral_in_the_same_word(monkeypatch, tmp_path):
    """сделали: hard ``l`` (velarized /ɫ/) and palatalized ``lj`` (/lʲ/) are
    two distinct Russian consonants, not one consonant with an optional
    secondary articulation — ``lj`` must not derive from the hard-l base
    (that would notate the non-existent velarized-and-palatalized ɫʲ).
    """
    text = "x.wav|сделали.|s_dj_e0_l_a1_lj_i0.\n"
    _stub_hf_hub_download(monkeypatch, tmp_path, text)

    pairs = dict(benchmark.load_alphacep_ru_book("ru", 100))

    assert pairs["сделали"] == "sdʲeɫˈalʲi"
    assert "ɫʲ" not in pairs["сделали"]


def test_stressed_vs_unstressed_vowel_digit(monkeypatch, tmp_path):
    """Digit ``1`` = stressed (gets ˈ), digit ``0`` = unstressed (no mark)."""
    text = "x.wav|дома дома.|d_o1_m_a0 d_a0_m_a1.\n"
    _stub_hf_hub_download(monkeypatch, tmp_path, text)

    pairs = benchmark.load_alphacep_ru_book("ru", 100)

    # first occurrence of "дома" wins (loader de-dupes case-insensitively)
    assert pairs[0] == ("дома", "dˈoma")


def test_mismatched_word_and_phone_counts_are_skipped(monkeypatch, tmp_path):
    text = (
        "x.wav|привет мир|p_rj_i0_vj_e1_t\n"  # 2 words, 1 phone group
        "y.wav|мир|mj_i1_r\n"                  # matches
    )
    _stub_hf_hub_download(monkeypatch, tmp_path, text)

    pairs = benchmark.load_alphacep_ru_book("ru", 100)

    assert pairs == [("мир", "mʲˈir")]


def test_only_ru_is_registered():
    assert benchmark.load_alphacep_ru_book("en", 100) == []


def test_registered_in_datasets_and_provenance():
    assert "alphacep_ru_book" in benchmark.DATASETS
    loader, langs = benchmark.DATASETS["alphacep_ru_book"]
    assert loader is benchmark.load_alphacep_ru_book
    assert langs == ["ru"]
    assert benchmark.PROVENANCE["alphacep_ru_book"] == "machine-generated"


def _cached_dev_file():
    pattern = os.path.expanduser(
        "~/.cache/huggingface/hub/datasets--alphacep--biggest-ru-book-cleanup"
        "/snapshots/*/metadata-phones-ids.csv.dev"
    )
    matches = glob.glob(pattern)
    return matches[0] if matches else None


@pytest.mark.skipif(_cached_dev_file() is None,
                     reason="alphacep dataset not present in local HF cache")
def test_every_segment_in_the_real_cache_maps_to_something():
    """Enumerate every raw segment code in the cached dataset (after the
    same punctuation-stripping the loader applies) and assert each one is
    accounted for by ``_alphacep_ru_segment_to_ipa`` — no silent drops of a
    real phoneme code, only of genuine leftover punctuation.
    """
    path = _cached_dev_file()
    unmapped_non_punct = set()
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            parts = line.rstrip("\n").split("|")
            if len(parts) < 3:
                continue
            for group in parts[2].split():
                for seg in group.split("_"):
                    stripped = benchmark._alphacep_ru_strip_punct(seg)
                    if not stripped:
                        continue  # pure punctuation, correctly dropped
                    if benchmark._alphacep_ru_segment_to_ipa(seg) is None:
                        unmapped_non_punct.add(seg)
    assert unmapped_non_punct == set(), (
        f"segments with no IPA mapping and non-empty after punctuation "
        f"stripping: {sorted(unmapped_non_punct)}"
    )


@pytest.mark.skipif(_cached_dev_file() is None,
                     reason="alphacep dataset not present in local HF cache")
def test_no_gold_word_contains_the_impossible_velarized_palatalized_lateral():
    """Non-None completeness (above) proves every segment maps to
    SOMETHING, not that it maps CORRECTLY. This asserts the actual defect
    class directly: ``ɫʲ`` (velarized hard /ɫ/ plus a palatalization
    diacritic) does not occur in Russian and must never appear in any
    transcription this loader produces from the real cached data.
    """
    pairs = benchmark.load_alphacep_ru_book("ru", 10**9)

    offenders = [(w, ipa) for w, ipa in pairs if "ɫʲ" in ipa]

    assert offenders == [], f"impossible ɫʲ sequence in: {offenders[:10]}"
