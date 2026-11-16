"""Sranan Tongo (`srn`) — the 1986 orthography, and the edge of it.

The spec transcribes the official spelling fixed by Resolution 4501 of 15 July
1986 and nothing else. The tests below do two jobs. The first group pins the
grapheme values of that standard. The second group pins its BOUNDARY, which is
the part that is easy to erode by accident.

Suriname wrote Sranan in a Dutch-based spelling before 1986, and pre-1986 forms
turn up in scraped corpora. They are not loanwords carrying Dutch phonology —
they are the same Sranan words in a superseded spelling, which is why a corpus
can contain both ⟨loekoe⟩ and ⟨luku⟩ for 'look'. It is therefore tempting to
give the Dutch digraphs their Dutch values in this table. Some of them can
never collide, because the 1986 rules forbid the sequence outright: rule 1
bans ⟨ie⟩, rule 6 bans ⟨oe⟩, rule 8 bans the letter ⟨j⟩ altogether. But ⟨ui⟩
and ⟨uw⟩ are ordinary conformant spellings of a vowel plus a glide, and reading
them as Dutch /œy/ and /y/ silently breaks conformant words. The last tests
here exist to make that breakage loud.

Forms and transcriptions are from the WikiPron `srn_latn_broad` gold; the
spelling rules are from the source recorded as `srn_spelling_1986` in
orthography2ipa/data/srn.json.
"""
from orthography2ipa import transcribe


def test_o_with_grave_is_open_o():
    assert transcribe("lòt", "srn") == "lɔt"


def test_sy_is_a_postalveolar_fricative():
    assert transcribe("basya", "srn") == "baʃa"


def test_ty_and_dy_are_affricates():
    assert transcribe("tyari", "srn") == "t͡ʃaɾi"
    assert transcribe("Adyuba", "srn") == "ad͡ʒuba"


def test_r_is_a_flap():
    assert transcribe("bugru", "srn") == "buɡɾu"


def test_aw_and_ow_are_diphthongs():
    assert transcribe("skowtu", "srn") == "skou̯tu"


def test_ui_is_a_vowel_plus_glide_not_a_dutch_diphthong():
    # Rule 9 of the 1986 spelling writes this sequence ⟨ui⟩, never ⟨uy⟩, so it
    # is conformant text and must not be read as Dutch /œy/.
    assert transcribe("puiri", "srn") == "puiɾi"
    assert transcribe("puirisopo", "srn") == "puiɾisopo"


def test_uw_is_a_vowel_plus_glide_not_a_dutch_long_y():
    assert transcribe("kapuwa", "srn") == "kapuwa"
    assert transcribe("antruwa", "srn") == "antɾuwa"
    assert transcribe("masuwa", "srn") == "masuwa"


def test_the_two_spellings_of_one_word_are_not_both_transcribed():
    # ⟨luku⟩ is the 1986 spelling and is handled; ⟨loekoe⟩ is the same word in
    # the pre-1986 spelling and is deliberately outside this spec. If a later
    # change makes both work, it belongs in a separate pre-1986 variant spec,
    # not in this table — see the boundary note in srn.json.
    assert transcribe("luku", "srn") == "luku"
    assert transcribe("loekoe", "srn") != "luku"
