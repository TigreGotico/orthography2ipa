"""⟨گ⟩ reads [ɡ] in Lebanese and Syrian, and it brings /ɡ/ with it.

Every other Arabic letter PR in this repository could say "no inventory grows", because the
phone was already reachable. **This one cannot.** `ar-LB` and `ar-SY` narrow the inherited
⟨ق⟩ to [ʔ] and [q] — the urban glottal reflex — and in doing so have no /ɡ/ at all, unlike
their `ar-x-levantine` parent and their `ar-PS` and `ar-JO` siblings.

So the inventory addition IS the claim, and these tests pin it as deliberate rather than
let it pass unremarked. What licenses it is the spec's own scoring gold, where all seven
⟨گ⟩ rows read [ɡ] and all seven are loanwords. The native reflex is untouched: قال is still
[ʔ]-initial here and a borrowed word still has its [ɡ].
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.inventory import emission_inventory, phoneme_inventory
from orthography2ipa.registry import get

READS = ["ar-LB", "ar-SY"]
UNCHANGED = ["ar-PS", "ar-JO"]


def _inventory(code):
    spec = get(code)
    return set(phoneme_inventory(spec)) | set(emission_inventory(spec))


@pytest.mark.parametrize("code", READS)
def test_the_letter_reads_g(code):
    assert "ɡ" in G2P(code).transcribe("بگب"), code


@pytest.mark.parametrize("code", READS)
def test_the_letter_deliberately_adds_g_to_the_inventory(code):
    """Stated, not slipped in beside a grapheme.

    A reader who sees /ɡ/ in this inventory should find a test saying it arrived on
    purpose and on what evidence — otherwise the next person to audit the spec cannot
    tell a cited loan phoneme from an accident.
    """
    assert "ɡ" in _inventory(code), code
    notes = get(code).notes
    assert "LOAN GRAPHEME گ" in notes, code
    assert "adds /ɡ/ to the inventory" in notes, code


@pytest.mark.parametrize("code", READS)
def test_the_native_qaf_reflex_is_untouched(code):
    """The claim is about loanwords only.

    Urban Lebanese and Damascene say [ʔ] for قال and still say [ɡ] in a borrowed word.
    A change that also gave ⟨ق⟩ a [ɡ] reading would satisfy every other assertion here
    and would be a different, unsourced claim about the native reflex.
    """
    assert G2P(code).transcribe("بقب") == "ˈbʔb", code
    assert "ɡ" not in get(code).graphemes["ق"], code


@pytest.mark.parametrize("code", UNCHANGED)
def test_siblings_without_gold_evidence_are_untouched(code):
    """ar-PS and ar-JO score against a different gold, which carries no ⟨گ⟩ row.

    They already have /ɡ/ from their own ⟨ق⟩, so mapping the letter there would be free
    and invisible — which is exactly why the absence is pinned. The evidence is
    variety-specific and so is the change.
    """
    assert "گ" not in get(code).graphemes, code
