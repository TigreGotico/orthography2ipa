"""Regression tests for rif (Tarifit / Riffian Berber) WOLD gold graphemes.

The rif spec models two conventions side by side: the everyday Berber Latin
alphabet, and the scholarly transliteration Maarten Kossmann uses in the WOLD
(World Loanword Database) Tarifiyt Berber chapter
(https://wold.clld.org/vocabulary/6), which is the benchmark gold for this
spec. Kossmann's table maps mostly to bare IPA plus a handful of ASCII-safe
stand-ins the era's IPA fonts lacked. These tests pin the WOLD-only graphemes
against gold words drawn straight from that dataset, so a future edit to
rif.json cannot silently break the mapping without a test going red.

Two of the fifteen mappings are the riskiest to get wrong: ç, which is NOT
the usual French/Turkish /s/ or /tʃ/ value but Kossmann's stand-in for /ɕ/,
and đ, which is /ð/ (not a retroflex or implosive /ɗ/ as in some other
Latin-based orthographies).
"""
import orthography2ipa


class TestWoldGraphemes:
    def test_c_cedilla_is_voiceless_alveolopalatal_fricative(self):
        # WOLD "açsum" (meat) -> Kossmann IPA "aɕsum": ç=ɕ, not tʃ/s/ʃ.
        assert orthography2ipa.transcribe("açsum", "rif") == "aɕsum"

    def test_d_stroke_is_voiced_dental_fricative(self):
        # WOLD "ižđi" (date palm) -> Kossmann IPA "iʒði": đ=ð.
        assert orthography2ipa.transcribe("ižđi", "rif") == "iʒði"

    def test_t_with_stroke_is_voiceless_dental_fricative(self):
        # WOLD "ŧizi" (mountain pass) -> Kossmann IPA "θizi": ŧ=θ.
        assert orthography2ipa.transcribe("ŧizi", "rif") == "θizi"

    def test_s_caron_is_voiceless_postalveolar_fricative(self):
        # WOLD "šař" (year) -> Kossmann IPA "ʃar": š=ʃ, ř=r.
        assert orthography2ipa.transcribe("šař", "rif") == "ʃar"

    def test_b_stroke_and_h_stroke(self):
        # WOLD "řəƀħā" (dust) -> Kossmann IPA "rəβħaː": ƀ=β, ħ=ħ, ā=aː.
        assert orthography2ipa.transcribe("řəƀħā", "rif") == "rəβħaː"
