"""Dutch ⟨qu⟩ reads [kʋ], and [k] in the French loans the guide lists.

Source:

- P.C. Paardekooper, *ABN-uitspraakgids*, 2nd rev. ed., 1987. Latin
  loans have kw: quota kwota, quantum kwɑntəm (p. 164), equator e'kwatɔr
  (p. 59), aquarel akwa'rɛl (p. 12), eloquent elo'kwɛnt (p. 57). The w is
  labiodental: "De w is in het ABN een liptandklank" (p. XVIII). French
  loans have k: queue kø, quarantaine kɑrɑn'tɛ.nə (p. 164), equipe e'kip
  (p. 59), etiquette eti'kɛtə (p. 60).

nl-BE writes [kw], because its ⟨w⟩ is [w] (Verhoeven 2005, p. 245).
"""
import pytest

from orthography2ipa import G2P

LATIN = ["quota", "quantum", "equator", "aquarel", "eloquent", "frequent", "requiem", "colloquium"]
FRENCH = ["queue", "quarantaine", "quotiënt", "equipe", "etiquette", "cheque", "croquet",
          "calqueren", "communiqué", "quatre-mains"]
DIALECTS = ["nl-NL", "nl-NL-x-polder", "nl-NL-x-groninge", "nl-NL-x-limburg"]


@pytest.mark.parametrize("lang", DIALECTS + ["nl-BE", "nl-BE-x-antwerp"])
@pytest.mark.parametrize("word", LATIN)
def test_latin_qu_reads_as_kw_spelling(lang, word):
    """The guide writes kw, so ⟨qu⟩ must read like a written ⟨kw⟩."""
    g2p = G2P(lang)
    assert g2p.transcribe(word) == g2p.transcribe(word.replace("qu", "kw"))


@pytest.mark.parametrize("lang", DIALECTS + ["nl-BE", "nl-BE-x-antwerp"])
@pytest.mark.parametrize("word", FRENCH)
def test_listed_french_qu_reads_as_k_spelling(lang, word):
    """The guide writes k, so ⟨qu⟩ must read like a written ⟨k⟩."""
    g2p = G2P(lang)
    assert g2p.transcribe(word) == g2p.transcribe(word.replace("qu", "k"))


@pytest.mark.parametrize("lang, word, ipa", [
    ("nl-NL", "quiz", "ˈkʋɪs"),
    ("nl-NL", "quota", "ˈkʋoutaː"),
    ("nl-BE", "quota", "ˈkwoːtaː"),
])
def test_qu_whole_word(lang, word, ipa):
    assert G2P(lang).transcribe(word) == ipa


@pytest.mark.parametrize("lang", DIALECTS + ["nl-BE", "nl-BE-x-antwerp"])
@pytest.mark.parametrize("word", ["huurquote", "spaarquote", "pubquiz", "dragqueen"])
def test_coda_rules_see_the_k_of_qu(lang, word):
    """A coda consonant before ⟨qu⟩ takes the same value as before a written ⟨kw⟩.

    The voiced obstruent devoices before the [k] (Gussenhoven 1992, p. 46), and
    the nl-BE [r] devoices before it.
    """
    g2p = G2P(lang)
    assert g2p.transcribe(word) == g2p.transcribe(word.replace("qu", "kw"))


def test_enquete_qu_is_plain_k():
    """Compared by ending: the [ŋ] of ɑŋ'kɛ.tə (p. 58) is not modelled before ⟨qu⟩."""
    assert G2P("nl-NL").transcribe("enquête").endswith("kɛtə")


def test_unlisted_inflection_keeps_k_labiodental():
    """A stated gap: the rule lists headwords, so a plural is not reached."""
    assert "kʋ" in G2P("nl-NL").transcribe("etiquettes")
