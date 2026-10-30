"""Tests locking in the Persian (fa) vowel/rhotic convention against the
cited primary sources — Windfuhr 1979/2009 "Persian Grammar"; Majidi &
Ternes 1991 "Persian (Farsi)" (JIPA Illustrations of the IPA 21(2),
pp. 96-97); Lazard 1992 "A Grammar of Contemporary Persian";
Toosarvandani 2004.

Context (worst-PER wave, 2026-08): fa scored PER≈0.55 against the
WikiPron gold set, with the single dominant confusion pair
'a' (gold) -> 'ɒ' (hyp) on ~100% of words. Investigation
(scripts/error_analysis.py fa --dataset wikipron) showed this is NOT a
bug in the o2i spec: fa.json already encodes the modern Tehrani
six-vowel system /æ e o ɒː iː uː/ (long ā backed to [ɒː]), matching
every cited reference. WikiPron's gold instead uses an
older/transliteration-flavored broad transcription (plain 'a' for the
long vowel, plain 'r' for the rhotic, no word-initial glottal onset)
that does not match the phonetic value described by the cited sources.

Per project policy the spec follows the cited standard, not the gold,
when the two disagree — so these tests pin the CORRECT convention and
must keep failing loudly if anyone "fixes" fa.json by mechanically
copying WikiPron's ⟨a⟩ instead of ⟨ɒː⟩.
"""
from orthography2ipa import G2P


def strip_marks(s: str) -> str:
    drop = "ˈˌ.·‿()"
    return "".join(c for c in s if c not in drop)


class TestTehranSixVowelSystem:
    """Windfuhr 1979/2009; Majidi & Ternes 1991 (JIPA): long ā is backed
    and rounded to [ɒː] in modern Tehrani Persian, distinct from the
    fronted short /æ/. This is the opposite of WikiPron's broad 'a'."""

    def test_long_a_is_backed_rounded(self):
        """Bare alef (ا), the long-ā grapheme, must surface as ɒː, never
        as plain 'a' (Majidi & Ternes 1991, JIPA illustration)."""
        fa = G2P("fa")
        result = fa.transcribe("آری")  # "yes" — gold(WikiPron)='aːreː'
        assert "ɒː" in result, f"Expected backed ɒː in {result!r}"
        assert "a" not in strip_marks(result).replace("ɒ", ""), (
            f"Unexpected plain 'a' in {result!r} — Tehrani ā is [ɒː], "
            "not [aː] (Windfuhr 1979; Majidi & Ternes 1991)"
        )

    def test_short_a_fronted_to_ae(self):
        """The short-a diacritic (zabar/fatha, َ) is fronted to /æ/ in
        Tehrani Persian, not left as plain /a/ (Windfuhr 1979)."""
        fa = G2P("fa")
        result = fa.transcribe("سَلام")
        assert "æ" in result

    def test_rhotic_defaults_to_tap(self):
        """ر defaults to the alveolar tap [ɾ] in most positions (Majidi &
        Ternes 1991); trilled [r] remains an available allophone but is
        not the WikiPron-style plain broad 'r'."""
        fa = G2P("fa")
        result = fa.transcribe("ایران")
        assert "ɾ" in result


class TestDariKeepsClassicalVowels:
    """fa-AF (Dari) must NOT inherit the Tehran vowel shift: Dari keeps
    the Classical New Persian distinction the Tehran dialect merged."""

    def test_dari_long_a_stays_front(self):
        dari = G2P("fa-AF")
        result = dari.transcribe("آری")
        assert "aː" in result
        assert "ɒː" not in result, (
            f"Dari should not show the Tehran ā→ɒː backing in {result!r}"
        )


class TestTajikConservativeVowels:
    """tg (Tajik, Cyrillic) is the most conservative variety and must not
    show the Tehran vowel shift either — it is a sibling, not a
    Tehran-derived dialect."""

    def test_tajik_a_stays_plain(self):
        tg = G2P("tg")
        result = tg.transcribe("хона")  # "house": x-o-n-a
        assert "ɒː" not in result
