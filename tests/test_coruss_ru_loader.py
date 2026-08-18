"""Tests for scripts/benchmark.py's ``load_coruss_ru`` loader (the CoRuSS
phonetic dictionary published by the SPbU phonetics lab).

The archive is stubbed via a fake ``rarfile`` module and a patched
``_fetch_file``, so the unit tests run offline and deterministically. The
completeness tests read the real archive from ``CACHE_DIR`` when it has been
fetched, and are skipped otherwise.
"""
import os
import re
import sys
import types

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402

ARCHIVE_URL = "https://russpeech.spbu.ru/SLOVARI/slovari.rar"
CACHED_ARCHIVE = os.path.join(benchmark.CACHE_DIR, "coruss_slovari.rar")


def _stub_archive(monkeypatch, tmp_path, rows, member="SLOVARI/READ/VAR-01"):
    """Install a fake ``rarfile`` whose one member holds *rows*, encoded the
    way the real files are (cp1251, CRLF, trailing per-file tally line)."""
    body = "".join(f" {w} [{t}]      1\r\n" for w, t in rows) + " 1/0\r\n"
    dest = tmp_path / "coruss_slovari.rar"
    dest.write_bytes(body.encode("cp1251"))
    fetched = []

    class _FakeRarFile:
        def __init__(self, path):
            self._path = path

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def namelist(self):
            return ["SLOVARI/", "SLOVARI/READ/", member]

        def read(self, name):
            assert name == member
            return open(self._path, "rb").read()

    monkeypatch.setitem(sys.modules, "rarfile",
                        types.SimpleNamespace(RarFile=_FakeRarFile))

    def _fake_fetch(url, name):
        fetched.append((url, name))
        return str(dest)

    monkeypatch.setattr(benchmark, "_fetch_file", _fake_fetch)
    return fetched


def test_palatalization_and_after_soft_e(monkeypatch, tmp_path):
    """день [d'e:n']: ``'`` palatalizes the consonant it follows, and ``e:``
    (⟨э⟩ after a soft consonant) is /e/ where bare ``e`` is /ɛ/."""
    _stub_archive(monkeypatch, tmp_path, [("де+нь", "d'e:n'")])

    assert benchmark.load_coruss_ru("ru", 100) == [("день", "dʲˈenʲ")]


def test_hard_e_stays_open_mid(monkeypatch, tmp_path):
    _stub_archive(monkeypatch, tmp_path, [("э+то", "et@")])

    assert benchmark.load_coruss_ru("ru", 100) == [("это", "ˈɛtə")]


def test_hard_and_soft_lateral_in_the_same_word(monkeypatch, tmp_path):
    """владелица: hard ⟨л⟩ is velarized /ɫ/ and soft ⟨ль⟩ is /lʲ/ — two
    distinct Russian consonants, so ``l'`` must not derive from the hard-l
    base (that would notate the non-existent ɫʲ)."""
    _stub_archive(monkeypatch, tmp_path, [("владе+лица", "vled'il'ic@")])

    (_word, ipa), = benchmark.load_coruss_ru("ru", 100)

    assert ipa == "vɫɛdʲˈilʲit͡sə"
    assert "ɫʲ" not in ipa


def test_voiced_shcha_is_not_a_palatalized_zh(monkeypatch, tmp_path):
    """``Z'`` takes the conventions page's value, voiced ⟨щ⟩ (/ʑː/), not
    ⟨ж⟩ plus palatalization — /ʐʲ/ is not a Russian segment either way.

    The row is a real one, ``выезжа+ть [vQiZ'a:t']``, and one of the three
    of the archive's sixteen ``Z'`` rows where the long soft /ʑː/ is the
    genuine old-Moscow reading of ⟨зж⟩. No archive row spells ⟨щ⟩ with it.
    """
    _stub_archive(monkeypatch, tmp_path, [("выезжа+ть", "vQiZ'a:t'")])

    (_word, ipa), = benchmark.load_coruss_ru("ru", 100)

    assert ipa == "vɨiʑːˈatʲ"
    assert "ʐʲ" not in ipa


def test_undocumented_palatalized_sibilants_are_rejected(
        monkeypatch, tmp_path):
    """The conventions page is the criterion. It defines no palatalized
    ⟨ц ш ч⟩, so ``c'``/``S'``/``C'`` are annotation slips with nothing to
    map them to that would not be a guess — the same page that licenses
    ``Z'`` rejects these."""
    _stub_archive(monkeypatch, tmp_path, [
        ("ца+рь", "c'ar'"), ("ша+р", "S'ar"), ("ча+с", "C'as"),
        ("до+м", "dom"),
    ])

    assert benchmark.load_coruss_ru("ru", 100) == [("дом", "dˈom")]


def test_context_diacritics_collapse_but_the_segment_survives(
        monkeypatch, tmp_path):
    """``:``/``I``/``#`` on a vowel mark a palatal environment and excess
    duration. Only the ⟨э⟩ ``:`` carries a phoneme distinction; the rest are
    coarticulation and are dropped WITHOUT dropping the vowel itself."""
    _stub_archive(monkeypatch, tmp_path, [
        ("ма+й", "maIj"), ("ма+ть", "ma:t'"), ("та+к", "ta#k"),
        ("э+ти", "e:It'i"),
    ])

    assert dict(benchmark.load_coruss_ru("ru", 100)) == {
        "май": "mˈaj", "мать": "mˈatʲ", "так": "tˈak", "эти": "ˈetʲi",
    }


def test_weakly_realized_segment_in_brackets_is_kept(monkeypatch, tmp_path):
    """Round brackets mark a segment the annotator heard only weakly; the
    segment is real phonetics, the bracket is notation."""
    _stub_archive(monkeypatch, tmp_path, [("Бре+жнев", "br'e:Zn'e:(f)")])

    (_word, ipa), = benchmark.load_coruss_ru("ru", 100)

    assert ipa == "brʲˈeʐnʲef"


def test_every_realization_of_a_word_is_kept_as_a_reference(
        monkeypatch, tmp_path):
    """A wordform said several ways contributes several rows: the harness
    scores against the best of a word's references, so the corpus's
    pronunciation variation is multi-reference gold, not noise to collapse."""
    _stub_archive(monkeypatch, tmp_path, [
        ("коне+чно", "kaeSn@"), ("коне+чно", "kan'e:Sn@"),
        ("коне+чно", "kaeSn@"),
    ])

    assert benchmark.load_coruss_ru("ru", 100) == [
        ("конечно", "kaˈɛʂnə"), ("конечно", "kanʲˈeʂnə"),
    ]


def test_composite_and_truncated_wordforms_are_rejected(monkeypatch, tmp_path):
    """Cross-word coalescences (``_``/``=``) carry sandhi a word-level G2P
    cannot produce, and a trailing hyphen marks a cut-off fragment."""
    _stub_archive(monkeypatch, tmp_path, [
        ("если_они", "je:sl'a:n'i"), ("потому=что", "p@t@muSta"),
        ("Инфо+рм-", "inform"), ("до+м", "dom"),
    ])

    assert benchmark.load_coruss_ru("ru", 100) == [("дом", "dˈom")]


def test_an_undocumented_symbol_rejects_the_whole_row(monkeypatch, tmp_path):
    """A shortened reference would score as a deletion error against a
    correct hypothesis, so a row with a symbol the conventions page does not
    define is dropped entirely rather than partially mapped."""
    _stub_archive(monkeypatch, tmp_path, [
        ("до+м", "dOm"), ("до+м", "dom"),
    ])

    assert benchmark.load_coruss_ru("ru", 100) == [("дом", "dˈom")]


def test_secondary_stress_caret_is_not_part_of_the_spelling(
        monkeypatch, tmp_path):
    _stub_archive(monkeypatch, tmp_path, [("вме^сто", "vm'e:st@")])

    assert benchmark.load_coruss_ru("ru", 100) == [("вместо", "vmʲestə")]


def test_stress_is_not_anchored_when_a_vowel_was_swallowed(
        monkeypatch, tmp_path):
    """Александровна [l'iksan@] has four vowels for the spelling's five: in
    spontaneous speech a whole syllable can vanish, and there is no
    defensible way to say which vowel survived, so the reference stays
    unmarked rather than guessing."""
    _stub_archive(monkeypatch, tmp_path, [("Алекса+ндровна", "l'iksan@")])

    (_word, ipa), = benchmark.load_coruss_ru("ru", 100)

    assert ipa == "lʲiksanə"
    assert "ˈ" not in ipa


def test_archive_is_fetched_once_from_the_official_url(monkeypatch, tmp_path):
    """The loader goes through the harness cache helper, so the archive is
    downloaded from the corpus site once and reused from ``CACHE_DIR``."""
    fetched = _stub_archive(monkeypatch, tmp_path, [("до+м", "dom")])

    benchmark.load_coruss_ru("ru", 100)
    benchmark.load_coruss_ru("ru", 100)

    assert fetched == [(ARCHIVE_URL, "coruss_slovari.rar")] * 2


def test_limit_caps_the_rows(monkeypatch, tmp_path):
    _stub_archive(monkeypatch, tmp_path, [
        ("до+м", "dom"), ("ко+т", "kot"), ("ле+с", "l'e:s"),
    ])

    assert len(benchmark.load_coruss_ru("ru", 2)) == 2


def test_only_ru_is_registered():
    assert benchmark.load_coruss_ru("en", 100) == []


def test_registered_in_datasets_and_provenance():
    assert "coruss_ru" in benchmark.DATASETS
    loader, langs = benchmark.DATASETS["coruss_ru"]
    assert loader is benchmark.load_coruss_ru
    assert langs == ["ru"]
    assert benchmark.PROVENANCE["coruss_ru"] == "expert-human"


# ── against the real archive ────────────────────────────────────────────────

_REAL = pytest.mark.skipif(
    not os.path.exists(CACHED_ARCHIVE),
    reason="CoRuSS archive not fetched into the benchmark cache")


def _real_transcriptions():
    import rarfile
    rows = []
    with rarfile.RarFile(CACHED_ARCHIVE) as rf:
        for name in sorted(n for n in rf.namelist() if not n.endswith("/")):
            text = rf.read(name).decode("cp1251", errors="replace")
            for line in text.splitlines():
                row = benchmark._CORUSS_ROW.match(line)
                if row is not None:
                    rows.append(row.group(2))
    return rows


@_REAL
def test_every_symbol_in_the_real_archive_is_accounted_for():
    """Enumerate every distinct character that occurs in a real
    transcription and assert each is either a mapped symbol, a documented
    diacritic, or one of the annotation slips this loader knowingly
    rejects. Nothing is allowed to be silently unaccounted for.
    """
    documented = (set(benchmark._CORUSS_VOWELS)
                  | set(benchmark._CORUSS_CONSONANTS)
                  | set(":I#'()"))
    #: Characters that occur only as annotation slips — a stress ``+`` typed
    #: into the transcription field, Latin letters with no defined value,
    #: punctuation, and single Cyrillic letters typed in the Latin field.
    slips = set("+OUAVTEw;?3![-") | set("хуСнрзб")

    seen = {ch for trans in _real_transcriptions() for ch in trans}

    assert seen <= documented | slips, sorted(seen - documented - slips)
    assert documented <= seen | {"D", "G"}, sorted(documented - seen)


@_REAL
def test_impossible_russian_segments_never_appear():
    """Non-rejection proves every symbol maps to SOMETHING, not that it maps
    correctly. ⟨л⟩ and the unpaired sibilants are the two places where a
    naive base + ``ʲ`` rule would fabricate a segment Russian does not have.
    """
    pairs = benchmark.load_coruss_ru("ru", 10 ** 9)

    offenders = [(w, i) for w, i in pairs
                 if re.search("ɫʲ|ʐʲ|ʂʲ|t͡sʲ", i)]

    assert offenders == [], offenders[:10]


@_REAL
def test_the_real_archive_yields_multi_reference_russian_gold():
    pairs = benchmark.load_coruss_ru("ru", 10 ** 9)
    words = [w for w, _ in pairs]

    assert len(pairs) > 15000
    assert len(set(words)) < len(words)  # variants survive as extra rows
    assert all(w and i for w, i in pairs)
