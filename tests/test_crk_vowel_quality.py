"""Plains Cree (`crk`) short high vowels are lax.

Bloomfield's symbol key in *Plains Cree Texts* (1934) gives short i "the vowel
of English pin, varying all the way to French fini" and short u -- written o in
the Standard Roman Orthography -- a range "from English put to French cou", so
the typical values are [ɪ] and [ʊ] rather than the cardinal [i] and [o].

Short a and long â are deliberately NOT lowered or backed here. Bloomfield's
usual value for short a is the vowel of German *nass*, with backing to [ɑ] or
[ʌ] named as an occasional excursion, and the one hand-transcribed word in the
wikipron gold (`pakamâkan`, cited to Wolfart 1996:430) writes long â as [aː].
The gold's wholesale a → ʌ and â → ɑː are `Module:crk-IPA` rewrite rules, so
matching them would fit the module rather than the sources.
"""
from orthography2ipa import transcribe


def test_short_i_is_near_close_lax():
    out = transcribe("astis", "crk")
    assert "ɪ" in out
    assert "i" not in out


def test_short_o_is_near_close_lax():
    out = transcribe("otôtêm", "crk")
    assert "ʊ" in out
    assert "o" not in out.replace("oː", "")


def test_short_a_stays_open_front():
    out = transcribe("amisk", "crk")
    assert "a" in out
    assert "ʌ" not in out


def test_long_a_circumflex_stays_front():
    out = transcribe("asâm", "crk")
    assert "aː" in out
    assert "ɑ" not in out
