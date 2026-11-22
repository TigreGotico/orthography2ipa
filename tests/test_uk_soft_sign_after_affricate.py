"""Ukrainian ⟨ь⟩ after ⟨ц⟩ writes one palatalization mark, as after every other consonant."""
import pytest

from orthography2ipa import G2P, transcribe
from orthography2ipa.inventory import phoneme_inventory, tokenize
from orthography2ipa.markup import MarkupError
from orthography2ipa.registry import get

CONSONANTS = "бвгґджзйклмнпрстфхцчшщ"

WORDS = ("кінець", "палець", "отець", "місць", "кінця", "кінцем", "борець",
         "день", "сіль", "ведмідь", "кістка", "дядько", "Індія", "життя")

CENSUS = [pre + c + post
          for c in CONSONANTS
          for pre, post in (("а", "ь"), ("ма", "ь"), ("а", "ьк"), ("а", "ьт"),
                            ("а", "ьн"), ("а", "ьц"), ("а", "ьс"), ("а", "ьл"))]


@pytest.mark.parametrize("word, ipa", [
    ("кінець", "ˈkʲinetsʲ"),
    ("палець", "ˈpaɫetsʲ"),
    ("отець", "ˈɔtetsʲ"),
    ("місць", "ˈmʲisʲtsʲ"),
    ("кінця", "ˈkʲinʲtsʲja"),
])
def test_word_final_tsj_has_one_mark(word, ipa):
    assert transcribe(word, "uk") == ipa


def test_no_double_mark_over_every_consonant_plus_soft_sign():
    doubled = {w: transcribe(w, "uk") for w in WORDS + tuple(CENSUS)
               if "ʲʲ" in transcribe(w, "uk")}
    assert doubled == {}


@pytest.mark.parametrize("before, after", [
    ("ацьк", "ˈatsʲk"),
    ("ацьт", "ˈatsʲt"),
    ("маць", "ˈmatsʲ"),
])
def test_tsj_before_a_consonant(before, after):
    assert transcribe(before, "uk") == after


def test_every_census_output_tokenizes_inside_the_inventory():
    """⟨в⟩ and ⟨й⟩ after a vowel become glides that take ʲ, a separate defect; they stay out."""
    spec = get("uk")
    inventory = phoneme_inventory(spec)
    outside = {t for w in WORDS + tuple(CENSUS) if not ("в" in w or "й" in w)
               for t in tokenize(transcribe(w, "uk"), spec) if t not in inventory}
    assert outside == set()


def test_kinets_is_accepted_as_a_forced_phoneme():
    ipa = G2P("uk").transcribe('<phoneme ph="ˈkʲinetsʲ">кінець</phoneme>')
    assert ipa == "ˈkʲinetsʲ"


def test_the_old_double_mark_is_refused_as_a_forced_phoneme():
    with pytest.raises(MarkupError):
        G2P("uk").transcribe('<phoneme ph="ˈkʲinetsʲʲ">кінець</phoneme>')


@pytest.mark.parametrize("word", ["кінець", "палець", "отець", "місць"])
def test_own_output_is_accepted_as_a_forced_phoneme(word):
    g2p = G2P("uk")
    own = g2p.transcribe(word)
    assert g2p.transcribe(f'<phoneme ph="{own}">{word}</phoneme>') == own
