"""External (cross-word) word-final /s/ sandhi in European Portuguese.

A word-final coda /s/ (which surfaces [ʃ] in isolation and before a voiceless
consonant via the coda 'chiado') undergoes two cross-word sandhi processes:

- **Voicing assimilation before a VOICED consonant** → post-alveolar [ʒ]
  (``PT_CODA_S_VOICING``): as bocas → [ˈɐʒ ˈbɔkɐʃ], os dois → [ˈoʒ ˈdojʃ].
  A following *voiceless* consonant keeps [ʃ] (estás feliz → [eˈʃtaʃ fɨˈliʃ]).
- **Voicing before a VOWEL** → [z]/[ʒ] (``PT_FINAL_S_PREVOCALIC_VOICE``), whose
  place of articulation splits dialectally:

- **Standard [z]** — the North (Porto, Braga), Lisbon and the neutral centre
  (Coimbra, though Coimbra is variable). Base rule ``PT_FINAL_S_PREVOCALIC_VOICE``.
- **Post-alveolar [ʒ]** — the SOUTH (Algarve, strongest/categorical) and the
  Azores (São Miguel). The Algarve realises word-final /s/ as [ʒ] categorically
  (via its positional word_final map), so it surfaces [ʒ] prevocalically too;
  São Miguel (pt-PT-x-acores) applies its *prevocalic* [ʒ] only before a vowel (a
  re-declared sandhi override), keeping [ʃ] before a voiceless consonant or pause;
  before a voiced consonant the inherited voicing-assimilation rule still gives [ʒ].

Sources: standard [z] — Mateus & d'Andrade (2000: ch.2); Wikipedia 'Portuguese
phonology' (bons amigos [bõz ɐˈmiɣuʃ]; coda sibilant is [ʒ] before a voiced
consonant, [ʃ] before a voiceless one). Southern/Azorean [ʒ] — Portuguese With
Leo, 'The 8 accents' (native-speaker, https://www.youtube.com/watch?v=pitj0XxYO7I);
Lisbon and the North are explicitly [z], not [ʒ]. See the spec notes for the
honesty caveat that a page-pinned academic source for the prevocalic-[ʒ]
specifically was not located.
"""
from orthography2ipa.g2p import G2P


class TestStandardZ:
    """base pt-PT, North (porto) and Lisbon: prevocalic /s/ → alveolar [z]."""

    def test_base_estas_a_ver_z(self):
        assert G2P("pt-PT").transcribe("estás a ver") == "eˈʃtaz ˈɐ ˈvɛɾ"

    def test_base_os_amigos_z(self):
        assert G2P("pt-PT").transcribe("os amigos") == "ˈoz ɐˈmiɡuʃ"

    def test_porto_z(self):
        # Northern [z]; v→b is the inherited Porto betacism
        assert G2P("pt-PT-x-porto").transcribe("estás a ver") == "eˈʃtaz ˈɐ ˈbɛɾ"

    def test_lisbon_z_not_palatal(self):
        # Lisbon is standard [z], NOT [ʒ]
        out = G2P("pt-PT-x-lisbon").transcribe("estás a ver")
        assert out == "eˈʃtaz ˈɐ ˈvɛɾ"
        assert "ʃtaʒ" not in out

    def test_before_voiceless_consonant_stays_hush(self):
        # Before a VOICELESS consonant the coda /s/ keeps [ʃ] (no assimilation).
        for loc in ("pt-PT", "pt-PT-x-porto", "pt-PT-x-lisbon"):
            assert G2P(loc).transcribe("estás só") == "eˈʃtaʃ ˈsɔ"

    def test_before_voiced_consonant_voices_to_palatal(self):
        # Voicing assimilation: coda /s/ -> [ʒ] before a voiced consonant (PT_CODA_S_VOICING).
        for loc in ("pt-PT", "pt-PT-x-porto", "pt-PT-x-lisbon"):
            assert G2P(loc).transcribe("estás bem") == "eˈʃtaʒ ˈbɛm"

    def test_as_bocas_voices_before_b(self):
        assert G2P("pt-PT").transcribe("as bocas") == "ˈɐʒ ˈbɔkɐʃ"

    def test_os_dois_voices_before_d(self):
        assert G2P("pt-PT").transcribe("os dois") == "ˈoʒ ˈdojʃ"

    def test_voiceless_initial_does_not_voice(self):
        assert G2P("pt-PT").transcribe("estás feliz") == "eˈʃtaʃ fɨˈliʃ"

    def test_single_word_unchanged(self):
        for loc in ("pt-PT", "pt-PT-x-porto", "pt-PT-x-lisbon"):
            assert G2P(loc).transcribe("estás") == "eˈʃtaʃ"


class TestSouthernPalatal:
    """Algarve (categorical) and São Miguel/Azores (prevocalic): /s/ → [ʒ]."""

    def test_algarve_prevocalic_palatal(self):
        out = G2P("pt-PT-x-algarve").transcribe("estás a ver")
        assert out == "eˈʃtaʒ ˈɐ ˈvɛɾ"
        assert "ʃtaʒ" in out

    def test_algarve_word_final_palatal_categorical(self):
        # Algarve generalises [ʒ] to all word-final positions (via positional map)
        assert G2P("pt-PT-x-algarve").transcribe("estás") == "eˈʃtaʒ"
        assert G2P("pt-PT-x-algarve").transcribe("estás bem") == "eˈʃtaʒ ˈbɛm"

    def test_acores_prevocalic_palatal(self):
        out = G2P("pt-PT-x-acores").transcribe("estás a ver")
        assert out == "eˈʃtaʒ ˈɐ ˈvɛɾ"
        assert "ʃtaʒ" in out

    def test_acores_stays_hush_before_voiceless_consonant_and_pause(self):
        # São Miguel: [ʃ] before a VOICELESS consonant and in isolation.
        assert G2P("pt-PT-x-acores").transcribe("estás só") == "eˈʃtaʃ ˈsɔ"
        assert G2P("pt-PT-x-acores").transcribe("estás") == "eˈʃtaʃ"

    def test_acores_voices_before_voiced_consonant(self):
        # The general EP voicing-assimilation (PT_CODA_S_VOICING, inherited) still
        # applies before a voiced consonant: coda /s/ -> [ʒ].
        assert G2P("pt-PT-x-acores").transcribe("estás bem") == "eˈʃtaʒ ˈbɛm"


class TestSouthVsStandardDiverge:
    def test_south_palatal_vs_north_lisbon_z(self):
        ver = lambda loc: G2P(loc).transcribe("estás a ver")
        assert "ʃtaʒ" in ver("pt-PT-x-algarve")
        assert "ʃtaʒ" in ver("pt-PT-x-acores")
        assert "ʃtaz" in ver("pt-PT-x-porto")
        assert "ʃtaz" in ver("pt-PT-x-lisbon")
        assert "ʃtaz" in ver("pt-PT")


class TestRuleDeclaration:
    def test_base_rule_present_and_z(self):
        for loc in ("pt-PT", "pt-PT-x-porto", "pt-PT-x-lisbon"):
            spec = G2P(loc).spec
            rule = next(r for r in spec.sandhi_rules
                        if r.id == "PT_FINAL_S_PREVOCALIC_VOICE")
            assert rule.transform == "z", loc

    def test_acores_override_palatal(self):
        spec = G2P("pt-PT-x-acores").spec
        rule = next(r for r in spec.sandhi_rules
                    if r.id == "PT_FINAL_S_PREVOCALIC_VOICE")
        assert rule.transform == "ʒ"

    def test_coda_s_voicing_right_context_tolerates_stress(self):
        # The consonant-triggered voicing rule must fire on a stress-initial word,
        # so its right_context has to admit an optional leading [ˈˌ] stress mark.
        for loc in ("pt-PT", "pt-PT-x-porto", "pt-PT-x-lisbon"):
            spec = G2P(loc).spec
            rule = next(r for r in spec.sandhi_rules if r.id == "PT_CODA_S_VOICING")
            assert rule.transform == "ʒ", loc
            assert rule.right_context.startswith("^[ˈˌ]?"), loc
