"""Cited claims for the Southern Quechua varieties.

Each assertion below is a claim a source makes, not a snapshot of current
output: Cusco (quz) keeps the three-way laryngeal contrast and the uvular
STOP series, Ayacucho (quy) has neither the marked series nor the stop —
its ⟨q⟩ is the fricative /χ/. Both lower /a i u/ to [ɑ ɛ ɔ] next to a
uvular, which is why the trivocalic alphabet needs no ⟨e o⟩ letters.
"""
import orthography2ipa as o2i


def test_cusco_and_ayacucho_are_distinct_specs():
    """Both are individual languages; `qu` is only a structural stub, so the
    macrolanguage collapse must not swallow either code."""
    assert o2i.get("quz").code == "quz"
    assert o2i.get("quy").code == "quy"


def test_cusco_has_the_three_way_laryngeal_contrast():
    """Wikipedia, Cusco Quechua: plain / aspirated / ejective stops and
    affricates, written ⟨p ph p'⟩, ⟨ch chh ch'⟩ etc."""
    g = o2i.get("quz").graphemes
    assert g["p"] == ["p"] and g["ph"] == ["pʰ"] and g["p'"] == ["pʼ"]
    assert g["ch"] == ["tʃ"] and g["chh"] == ["tʃʰ"] and g["ch'"] == ["tʃʼ"]
    assert g["q"] == ["q"] and g["qh"] == ["qʰ"] and g["q'"] == ["qʼ"]


def test_ayacucho_lacks_the_marked_series_and_has_a_uvular_fricative():
    """Wikipedia, Ayacucho Quechua: no aspirated or ejective stops, and
    ⟨q⟩ is /χ/ rather than /q/."""
    g = o2i.get("quy").graphemes
    assert g["q"] == ["χ"]
    for absent in ("ph", "p'", "th", "t'", "chh", "ch'", "kh", "k'", "qh", "q'"):
        assert absent not in g


def test_the_ejective_and_aspirate_digraphs_tokenize_as_one_segment():
    """⟨ch'⟩ is one segment, not /tʃ/ + a stray apostrophe, and ⟨ph⟩ is not
    /p/+/h/ — the maximal-munch tokenizer must prefer the longer key."""
    quz = o2i.G2P("quz")
    assert quz.transcribe_word("ch'aska") == "tʃʼaska"
    assert quz.transcribe_word("phuyu") == "pʰuju"


def test_vowels_lower_next_to_a_uvular_in_both_varieties():
    """Wikipedia (both articles): /a i u/ → [ɑ ɛ ɔ] adjacent to a uvular.
    ⟨qusqu⟩ 'Cusco' lowers on both sides of each uvular; ⟨llaqta⟩ 'town'
    lowers the /a/ that precedes one."""
    assert o2i.G2P("quz").transcribe_word("qusqu") == "qɔsqɔ"
    assert o2i.G2P("quy").transcribe_word("qusqu") == "χɔsχɔ"
    assert o2i.G2P("quz").transcribe_word("llaqta") == "ʎɑqta"
    assert o2i.G2P("quy").transcribe_word("llaqta") == "ʎɑχta"


def test_a_plain_vowel_stays_unlowered_away_from_uvulars():
    """The lowering is conditioned, not a blanket vowel-quality claim:
    ⟨wasi⟩ 'house' has no uvular and keeps [a] and [i]."""
    assert o2i.G2P("quz").transcribe_word("wasi") == "wasi"
    assert o2i.G2P("quy").transcribe_word("wasi") == "wasi"


def test_the_palatal_letters_are_single_segments():
    """⟨ll⟩ /ʎ/ and ⟨ñ⟩ /ɲ/, as in ⟨ñan⟩ 'road'."""
    quz = o2i.get("quz").graphemes
    assert quz["ll"] == ["ʎ"] and quz["ñ"] == ["ɲ"]
    assert o2i.G2P("quz").transcribe_word("ñan") == "ɲan"


def test_the_rhotic_differs_between_the_two_varieties():
    """Cusco's consonant table gives a tap, Ayacucho's a trill."""
    assert o2i.get("quz").graphemes["r"] == ["ɾ"]
    assert o2i.get("quy").graphemes["r"] == ["r"]


def test_cusco_carries_the_spanish_loan_consonants():
    """Running text is full of Spanish loans that spell ⟨b d g f⟩; without
    the keys the engine drops the letter and returns a short word, so
    ⟨sunbiru⟩ 'hat' (< sombrero) must keep its ⟨b⟩ regardless of the loan
    consonants' phonemic status. Cusihuamán (1976), cited via Wikipedia
    (Cusco Quechua), says sustained borrowing from Spanish may have made
    /b d ɡ f/ phonemic for Cusco speakers, monolinguals included."""
    g = o2i.get("quz").graphemes
    assert g["b"] == ["b"] and g["d"] == ["d"]
    assert g["g"] == ["ɡ"] and g["f"] == ["f"]
    assert o2i.G2P("quz").transcribe_word("sunbiru") == "sunbiɾu"


def test_ayacucho_does_not_carry_the_loan_consonants():
    """The loan series is claimed for Cusco on a Cusco source; quy is left
    as its own source describes it."""
    g = o2i.get("quy").graphemes
    for absent in ("b", "d", "g", "f"):
        assert absent not in g


def test_the_quechua_childes_gold_is_scored_against_cusco():
    """IPA-CHILDES qu-PE is a Cusco-Collao corpus — its official-alphabet
    words spell aspirates and ejectives, which Ayacucho has neither of — and
    `qu` is a declared structural stub with no phonology, so the row must
    resolve to `quz`."""
    import importlib.util
    import pathlib
    path = pathlib.Path(__file__).resolve().parent.parent / "scripts" / "benchmark.py"
    spec = importlib.util.spec_from_file_location("_bench_qu", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod._IPA_CHILDES_FOLDERS["quz"] == "qu-PE"
    assert "qu" not in mod._IPA_CHILDES_FOLDERS
    assert o2i.get("qu").quality == "stub"
