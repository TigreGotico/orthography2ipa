"""Khiamniungan Naga (kix) — Patsho orthography, and syllable-final tone.

The reference forms are the Wiktionary Khiamniungan entries, whose
pronunciations are hand-written for the Patsho variety and mark tone with
Chao pitch numerals after the rime.
"""

import pytest

from orthography2ipa import G2P, get
from orthography2ipa.tone import dock_tone_marks


@pytest.fixture(scope="module")
def kix():
    return G2P("kix")


class TestToneDocking:
    """The mark rides the nucleus letter; IPA writes it after the rime."""

    def test_coda_precedes_the_mark(self):
        assert dock_tone_marks("mo³³ŋ") == "moŋ³³"

    def test_offglide_precedes_the_mark(self):
        assert dock_tone_marks("ha³³ɪ") == "haɪ³³"

    def test_offglide_and_coda_both_precede_the_mark(self):
        assert dock_tone_marks("hi³³am") == "hiam³³"

    def test_next_onset_stays_in_its_own_syllable(self):
        assert dock_tone_marks("hɛʊ³³moŋ³³") == "hɛʊ³³moŋ³³"

    def test_an_affricate_onset_is_not_split(self):
        assert dock_tone_marks("tɛ³³mtsʰoɪ³¹", ("ts", "tsʰ", "t", "s")) == \
            "tɛm³³tsʰoɪ³¹"

    def test_aspiration_stays_with_its_stop(self):
        assert dock_tone_marks("a³³mtʰo³³") == "am³³tʰo³³"

    def test_tone_letters_dock_too(self):
        assert dock_tone_marks("ma˥m") == "mam˥"

    def test_idempotent(self):
        once = dock_tone_marks("mo³³ŋ")
        assert dock_tone_marks(once) == once

    def test_untoned_input_is_untouched(self):
        assert dock_tone_marks("moŋ") == "moŋ"

    def test_hiatus_leaves_the_mark_on_its_own_nucleus(self):
        assert dock_tone_marks("a³³ɛ⁵⁵") == "a³³ɛ⁵⁵"


class TestKhiamniunganSpec:

    def test_tone_docking_is_declared(self):
        assert get("kix").tone_marks_syllable_final is True

    def test_no_voiced_plosives(self):
        # Thaam & Kevichüsa-Ezung (2023): the language does not exhibit
        # voiced plosives, and ⟨j⟩ spells the plain affricate /tʃ/.
        ipa = "".join(v[0] for v in get("kix").graphemes.values())
        assert not set("bdɡ") & set(ipa)

    def test_every_letter_of_the_orthography_maps(self):
        """No letter may contribute nothing — silent deletion is a defect."""
        kix = G2P("kix")
        bare = kix.transcribe_word("kā")
        for letter in "abdeghijklmnopstuvwy" + "üāēīōūǖáéíóúǘàèìòùǜâêîôûǎěǐǒǔǚ":
            got = kix.transcribe_word("k" + letter + "ā")
            assert len(got) > len(bare), f"{letter!r} vanished: {got!r}"


class TestKhiamniunganWords:
    """Gold: the Wiktionary Khiamniungan Naga entries (Patsho)."""

    @pytest.mark.parametrize("word,ipa", [
        ("Chīm", "tʃʰim³³"),
        ("Hāthòu", "ha³³tʰoʊ³¹"),
        ("Chāmthōi", "tʃʰam³³tʰoɪ³³"),
        ("Hēumōngmêi", "hɛʊ³³moŋ³³mɛɪ⁵²"),
        ("Hīamphái", "hiam³³pʰaɪ⁵⁵"),
        ("Jângphū", "tʃaŋ⁵²pʰu³³"),
        ("Chēunyúmóng", "tʃʰɛʊ³³ɲu⁵⁵moŋ⁵⁵"),
        ("Jāngtēmtshòi", "tʃaŋ³³tɛm³³tsʰoɪ³¹"),
        ("Chǖpòknyùshìeh", "tʃʰə³³pok³¹ɲu³¹ʃiɛʔ³¹"),
        ("Hēuphúhēu", "hɛʊ³³pʰu⁵⁵hɛʊ³³"),
    ])
    def test_word(self, kix, word, ipa):
        assert kix.transcribe_word(word) == ipa

    def test_j_is_the_plain_affricate(self, kix):
        assert kix.transcribe_word("Jīm").startswith("tʃi")

    def test_ch_is_the_aspirated_affricate(self, kix):
        assert kix.transcribe_word("Chīm").startswith("tʃʰi")

    def test_final_h_is_a_glottal_stop(self, kix):
        # ⟨tsah⟩ /tsaʔ/ against ⟨tsak⟩ /tsak/ (Thaam & Kevichüsa-Ezung 2023).
        assert kix.transcribe_word("tsāh") == "tsaʔ³³"
        assert kix.transcribe_word("tsāk") == "tsak³³"

    def test_initial_h_stays_a_fricative(self, kix):
        assert kix.transcribe_word("hāt").startswith("ha")

    def test_umlaut_u_is_schwa(self, kix):
        # ⟨wekü⟩ /wê.kə̄/, ⟨tsün⟩ /tsə̌n/ (Thaam & Kevichüsa-Ezung 2023).
        assert kix.transcribe_word("kǖ") == "kə³³"

    def test_untoned_umlaut_u_keeps_its_vowel(self, kix):
        # The bare letter is what their orthography writes: ⟨wekü⟩.
        assert kix.transcribe_word("wekü") == "wɛkə"

    def test_b_and_d_spell_the_voiceless_stops(self, kix):
        # Their orthography: ⟨bem⟩ /pēm/, ⟨tsad⟩ /ʦʌ̀t/. Neither letter
        # occurs in the Patsho data, so neither may vanish silently.
        assert kix.transcribe_word("bem") == "pɛm"
        assert kix.transcribe_word("tsad") == "tsat"

    def test_caron_keeps_the_vowel_and_takes_no_tone(self, kix):
        # The rising tone is described for Thang but never written in the
        # Patsho data, so no Chao value is assigned — but the vowel stays.
        assert kix.transcribe_word("sǎi") == "saɪ"

    def test_medial_ng_coda_is_a_known_docking_limitation(self, kix):
        # Maximal onset reads the ⟨ng⟩ of ⟨Lōngūlām⟩ as the next syllable's
        # onset, so the mark docks one segment early. The reference has
        # loŋ³³u³³lam³³. Pinned so the day the divider improves is visible.
        assert kix.transcribe_word("Lōngūlām") == "lo³³ŋu³³lam³³"
