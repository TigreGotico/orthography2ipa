"""The ``vowel_phone`` bit of the IR character table is phonematcher's ``is_vowel_phone``."""
import phonematcher
import pytest

from orthography2ipa import feats

from orthography2ipa.ir.compiler import CB, build_ir

VOWEL_PHONE = 1 << CB["vowel_phone"]


@pytest.mark.parametrize("code", ["vi-VN", "pt-PT", "es-ES", "kab", "zh-CN"])
def test_the_bit_is_phonematchers_vowel_test_for_every_character(code):
    wrong = [chr(cp) for cp, bits in build_ir(code)["chars"].items()
             if bool(bits & VOWEL_PHONE) != phonematcher.is_vowel_phone(chr(cp))]
    assert wrong == []


def test_a_precomposed_vowel_letter_has_the_bit():
    assert build_ir("vi-VN")["chars"][ord("á")] & VOWEL_PHONE


@pytest.mark.parametrize("phone, vowel", [("a", True), ("p", False), ("ɚ", False)])
def test_the_old_name_in_feats_warns_at_the_caller_and_keeps_its_value(phone, vowel):
    # The vendored table has no ɚ, so the old name keeps answering False.
    for _ in range(2):
        with pytest.warns(DeprecationWarning, match="phonematcher.is_vowel_phone") as caught:
            assert feats.is_vowel_phone(phone) is vowel
        assert caught[0].filename == __file__
