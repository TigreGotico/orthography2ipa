"""Old Irish (sga) orthography-to-phonology.

Full-transcription pins for what Old Irish spelling encodes: consonant
quality under caol le caol, the unwritten lenition of ⟨b d g m⟩, the
single/double letter voicing convention, the fortis/lenis sonorant
contrast, and the unstressed vowel system that keeps [u] everywhere and
keeps every vowel quality in absolute word-final position. That last one
is what separates Old Irish from the sibling ``mga`` entry, where the
collapse to schwa reaches every non-initial vowel.

Every expectation states the whole transcription, so a rule cannot pass by
getting one segment right while breaking its neighbour. Every headword is
attested Old Irish taken from the WikiPron gold, and every expectation
agrees with that gold verbatim apart from the two named departures below.

Rules and citations live in ``orthography2ipa/data/sga.json``.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def sga():
    return G2P("sga")


# A consonant flanked by ⟨e i⟩ is slender, by ⟨a o u⟩ broad, and the vowel
# letter written only to signal quality is silent. A following vowel letter
# outranks a preceding one, and the quality spreads through a cluster.
QUALITY = [
    ("aile", "ˈalʲe"),
    ("Mide", "ˈmʲiðʲe"),
    ("cain", "ˈkanʲ"),
    ("Laigin", "ˈlaɣʲənʲ"),
    ("icht", "ˈixʲt̠ʲ"),
    ("chenél", "ˈxʲenʲeːl"),
    # The cluster spread reaches a sonorant coda: the ⟨m⟩ of ⟨cuirm⟩ is
    # slender because the ⟨r⟩ it clusters with is, not because a front
    # vowel letter stands next to it. ⟨tarm⟩ is the broad control.
    ("cuirm", "ˈkuɾʲmʲ"),
    ("teinm", "ˈt̠ʲenʲmʲ"),
    ("tarm", "ˈtaɾm"),
]

# Lenition of ⟨b d g m⟩ is not written: a single letter after a vowel spells
# the fricative, the doubled letter the stop. ⟨b g⟩ lenite after ⟨l r n⟩
# too; ⟨d⟩ does not. Single ⟨c t p⟩ after a vowel spell the voiced stop.
LENITION = [
    ("Ulad", "ˈuləð"),
    ("Ultaib", "ˈultəβʲ"),
    ("oc", "ˈoɡ"),
    ("ícc", "ˈiːkʲ"),
    ("dam", "ˈdaβ̃"),
    ("cumal", "ˈkuβ̃əl"),
    ("amrae", "ˈaβ̃ɾe"),
    # ⟨d⟩ after ⟨r⟩ keeps its stop, which is what makes ⟨rd nd ld⟩ the
    # spelling of an unlenited [d].
    ("ard", "ˈard"),
    # KNOWN DEPARTURE, vowel only: the gold writes the ⟨i⟩ of ⟨ir-⟩ as [œ]
    # (a reading it gives 13 headwords in the whole set and nowhere else),
    # so its transcription is [œɾβaːɣ]. The ⟨b⟩ after ⟨r⟩ is the point of
    # the pin and the gold agrees on it.
    ("irbág", "ˈiɾʲβaːɣ"),
]

# An unstressed short vowel reduces to [ə], except ⟨u⟩, which keeps its
# quality anywhere, and except in absolute word-final position, where every
# vowel keeps its own. Long vowels never reduce.
VOWELS = [
    ("Muman", "ˈmuβ̃ən"),
    ("buiden", "ˈbuðʲən"),
    ("cumang", "ˈkuβ̃əŋɡ"),
    ("assu", "ˈasu"),
    ("arae", "ˈaɾe"),
    ("aille", "ˈal̠ʲe"),
    ("ailiu", "ˈalʲu"),
    ("Grécu", "ˈɡʲɾʲeːɡu"),
    ("chenna", "ˈxʲena"),
    # A word-final ⟨ae⟩ without the acute is a plain [e]; the same digraph
    # elsewhere in the word is hiatus, not the diphthong.
    ("Machae", "ˈmaxe"),
    ("accae", "ˈake"),
    ("aer", "ˈaeɾ"),
]

# The fortis sonorants are written double only where they continue a
# Proto-Celtic geminate. Word-initially and before a coronal they are
# written single and are fortis anyway; before a labial or velar they are
# lenis.
FORTIS = [
    ("ní", "ˈn̠ʲiː"),
    ("ré", "ˈrʲeː"),
    ("lí", "ˈl̠ʲiː"),
    ("aird", "ˈarʲd̠ʲ"),
    ("ind", "ˈin̠ʲd̠ʲ"),
    ("Ultu", "ˈultu"),
    # Lenis before a labial or velar, against the coronal cases above.
    ("tarm", "ˈtaɾm"),
    ("togairm", "ˈtoɣəɾʲmʲ"),
    # Written double, so fortis wherever it stands.
    ("aill", "ˈal̠ʲ"),
    ("Conn", "ˈkon"),
    ("barr", "ˈbar"),
    # ⟨ss⟩ is a single [s], not a geminate the engine spells out twice.
    ("assa", "ˈasa"),
    ("less", "ˈl̠ʲes"),
]

# ⟨áe aí óe oí⟩ spell the diphthong early /ai/ and /oi/ merged into;
# ⟨ía úa⟩ the reflexes of the long mid vowels. ⟨ía úa⟩ do not slenderize a
# FOLLOWING consonant — quality there is set by the digraph's closing ⟨a⟩
# under leathan le leathan, not by its opening ⟨í ú⟩.
DIPHTHONGS = [
    ("Goídel", "ˈɡoːi̯ðʲəl"),
    ("Lóegaire", "ˈloːi̯ɣəɾʲe"),
    ("Cináed", "ˈkʲinaːi̯ð"),
    ("blíadain", "ˈbʲlʲiːa̯ðənʲ"),
    ("fíada", "ˈɸʲiːa̯ða"),
    ("búachaill", "ˈbuːa̯xəl̠ʲ"),
    ("anúas", "ˈanuːa̯s"),
    ("cían", "ˈkʲiːa̯n"),
    ("cíall", "ˈkʲiːa̯l"),
    ("cíar", "ˈkʲiːa̯ɾ"),
    ("bíad", "ˈbʲiːa̯ð"),
    ("dagníat", "ˈdaɣnʲiːa̯d"),
]


@pytest.mark.parametrize("word,ipa", QUALITY)
def test_consonant_quality(sga, word, ipa):
    assert sga.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", LENITION)
def test_lenition_and_medial_voicing(sga, word, ipa):
    assert sga.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", VOWELS)
def test_unstressed_vowels(sga, word, ipa):
    assert sga.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", FORTIS)
def test_fortis_and_lenis_sonorants(sga, word, ipa):
    assert sga.transcribe(word) == ipa


@pytest.mark.parametrize("word,ipa", DIPHTHONGS)
def test_diphthongs(sga, word, ipa):
    assert sga.transcribe(word) == ipa


def test_old_irish_keeps_final_vowel_quality_middle_irish_reduces_it():
    """The one contrast that separates the two stages of the same spelling.

    Old Irish keeps the quality of an absolutely final unstressed vowel;
    Middle Irish reduces it to schwa. Both entries read the same letters.
    """
    assert G2P("sga").transcribe("aille") == "ˈal̠ʲe"
    assert G2P("mga").transcribe("aille") == "ˈal̠ʲə"
