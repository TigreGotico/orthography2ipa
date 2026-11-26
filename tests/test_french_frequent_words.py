"""French rules for frequent words that the letters decide.

Each rule is cited by page from Martinon, *Comment on prononce le français*
(Larousse, 1913), read in the archive.org scan of the University of Toronto
copy (https://archive.org/details/commentonprononc00martuoft), unless the test
names another source. The expected IPA is written here, never read back from
the engine, and each rule has a counter-case where it must not fire.
"""
import pytest

import orthography2ipa as o2i


def _t(text):
    return o2i.transcribe(text, "fr-FR")


# Martinon (1913: 161): the ⟨nt⟩ of the third-person plural changes nothing,
# tombait dru and tombaient dru sound the same. Larousse, s.v. être
# (Homonymes): étaient is a homonym of étai, soient of soi, soie and soit.
@pytest.mark.parametrize("text, expected", [
    ("étaient", "etɛ"), ("avaient", "avɛ"), ("seraient", "səʁɛ"),
    ("parlaient", "paʁlɛ"), ("aient", "ɛ"), ("paient", "pɛ"),
    ("soient", "swa"), ("voient", "vwa"),
])
def test_ent_after_ai_and_oi_is_mute(text, expected):
    assert _t(text) == expected


@pytest.mark.parametrize("text, expected", [
    # Bare ⟨-ent⟩ keeps its deferred nasal reading (ENDING "ent").
    ("vent", "vɑ̃"), ("moment", "mɔmɑ̃"), ("ils parlent", "il paʁlɑ̃"),
    # ⟨-ient⟩ is not ⟨ai⟩ or ⟨oi⟩: client keeps its nasal vowel.
    ("client", "kljɛ̃"),
])
def test_other_ent_endings_are_untouched(text, expected):
    assert _t(text) == expected
