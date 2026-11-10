"""Cited-rule conformance: Russian words whose reading is lexical.

Source for every expected value below: Orfoepicheskii slovar' russkogo
iazyka: proiznoshenie, udarenie, grammaticheskie formy, ed. R. I. Avanesov,
4th ed., Moscow: Russkii iazyk, 1988 (scan:
https://archive.org/details/20231109_20231109_1822). The article on
pronunciation in that book is by Avanesov. The expected values map its
transcriptions onto the ``ru`` spec's symbols: ш = [ʂ], ы = [ɨ], [ъ] = [ə],
[ь] and pretonic [иᵉ] = [ɪ], first-pretonic [а] = [ɐ], a raised ь = [ʲ].

§ 129, p. 676: "Сочетание чт произносится в соответствии с написанием, т. е.
[чт]: ср. ма́чта, по́чта, мечта́ть, прочту́, почти́ть, ничто́жный. Однако в
слове что и производных от него на месте чт произносится [шт]. Таковы слова:
что, что́бы, что́-то, что́-нибудь, ко́е-что́, не́ за что, ни за что́, ничто́,
которые произносятся: [што], [што́бы], [што́-тъ], [што́-нибутʹ], [ко́йь-што́],
[не́-зъ-штъ], [ни-за-што́], [ништо́]. В слове не́что сочетание чт
произносится в соответствии с написанием: [не́чтъ]."

§ 151, p. 678: "Согласный [в] на месте буквы г произносится также в словах
сего́дня, сего́дняшний, итого́."

§ 53, p. 666: "сего́дня (произносится [сиᵉво́дʹнʹъ])". The headwords on p. 523
mark сего́дня and сего́дняшний [во́; дʹнʹ], and the key on p. 12 reads a raised
ь as softness. § 54, p. 666: ⟨я⟩ outside a case ending "в неконечном
заударном слоге" is [ь] (при́няты [при́нʹьты]).
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(word):
    return G2P("ru").transcribe_word(word)


def _words(text):
    return G2P("ru").transcribe(text).split()


# ===========================================================================
# ⟨чт⟩ = [ʂt] in что and the words made from it
# ===========================================================================

@pytest.mark.parametrize("word,expected", [
    ("что", "ˈʂto"),        # [што]
    ("что́", "ˈʂto"),
    ("чтобы", "ˈʂtobɨ"),    # [што́бы]
    ("что́бы", "ˈʂtobɨ"),
    ("чтоб", "ˈʂtop"),      # headword p. 635: чтоб [шт]
    ("ничто", "nʲɪˈʂto"),   # [ништо́]
    ("ничто́", "nʲɪˈʂto"),
])
def test_chto_family_is_sht(word, expected):
    assert _t(word) == expected


@pytest.mark.parametrize("text,index", [
    ("что-то", 0),          # [што́-тъ]
    ("что-нибудь", 0),      # [што́-нибутʹ]
    ("что-либо", 0),        # headword p. 636: что́-либо [шт]
    ("кое-что", 1),         # [ко́йь-што́]
])
def test_hyphenated_chto_forms_reach_the_entry(text, index):
    """The engine splits a word at the hyphen, so the что part of each
    hyphenated form takes the entry for что."""
    assert _words(text)[index] == "ˈʂto"


@pytest.mark.parametrize("word", ["почта", "мачта", "ничто́жный", "не́что",
                                  "прочту́"])
def test_other_cht_words_keep_tsch(word):
    """Control: ⟨чт⟩ outside the что family is read as written, [tɕt],
    нечто and ничтожный included (§ 129, p. 676)."""
    assert "tɕt" in _t(word).replace("ˈ", "")


# ===========================================================================
# ⟨г⟩ = [v] in сегодня, сегодняшний, итого
# ===========================================================================

@pytest.mark.parametrize("word,expected", [
    ("сегодня", "sʲɪˈvodʲnʲə"),            # [сиᵉво́дʹнʹъ]
    ("сего́дня", "sʲɪˈvodʲnʲə"),
    ("сегодняшний", "sʲɪˈvodʲnʲɪʂnʲɪj"),   # [во́; дʹнʹ], ⟨я⟩ = [ь] by § 54
    ("итого", "ɪtɐˈvo"),                   # headword p. 198: итого́ [во́]
])
def test_g_is_v_outside_the_desinence(word, expected):
    assert _t(word) == expected


# ===========================================================================
# Free stress: unmarked input is NOT patched word by word
# ===========================================================================

def test_marked_voda_is_end_stressed():
    """Control: вода́ with its mark is [vɐˈda]. Unmarked вода takes the
    documented penultimate default and is deliberately not listed in
    ``word_exceptions``."""
    from orthography2ipa.registry import get
    assert _t("вода́") == "vɐˈda"
    assert "вода" not in (get("ru").word_exceptions or {})
