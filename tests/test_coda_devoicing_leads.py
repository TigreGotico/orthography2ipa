"""Engine lead: true syllable-coda obstruent devoicing needs a syllabifier.

Final-devoicing languages (German, Dutch, Czech, Polish, Russian, West
Frisian, Saterland Frisian, Low German, Turkish) neutralise voiced
obstruents in the syllable coda. The specs model the safe, position-derivable
half of that neutralisation with a ``word_final`` positional override, which
the beam reaches reliably. The other half — a coda obstruent that is
*pre-consonantal but word-internal* (German ⟨Magd⟩ [maːkt], the ⟨g⟩ closing
the only syllable before ⟨d⟩) — cannot be modelled correctly with the two
position keys the beam derives:

  * ``word_final`` does not cover it (the obstruent is not word-final);
  * ``before_consonant`` over-covers it: it also fires on an obstruent that
    opens the *next* syllable's onset cluster (German ⟨Adler⟩ [ˈaːdlɐ], the
    ⟨d⟩ heterosyllabic onset of ⟨-dler⟩), where the obstruent must stay
    voiced, and it cannot express regressive voicing assimilation (the coda
    obstruent assimilates to the *following* obstruent's voicing, so a voiced
    cluster keeps voicing).

Correctly resolving pre-consonantal coda devoicing therefore needs the
syllabifier — i.e. an allophone rule keyed on ``syllable_position: "coda"``
plus voicing-assimilation context — not a positional grapheme override. Until
that lands, the inert ``coda`` positional entries these specs once carried
have been removed (they never fired) rather than converted to a
``before_consonant`` override that would mis-devoice onset clusters.
"""
import pytest

from orthography2ipa import transcribe


def test_word_final_obstruent_devoicing_is_covered():
    """The position-derivable half works: word-final /d/ → [t]."""
    assert transcribe("Rad", "de-DE").endswith("t")
    assert transcribe("город", "ru").endswith("t")


def test_onset_cluster_obstruent_stays_voiced():
    """The safety constraint that rules out a blanket ``before_consonant``
    devoicing override: a heterosyllabic onset ⟨d⟩ must NOT devoice."""
    # Adler = [ˈaːdlɐ]: the ⟨d⟩ opens the second syllable, stays voiced.
    assert "d" in transcribe("Adler", "de-DE")


@pytest.mark.xfail(
    strict=True,
    reason="pre-consonantal word-internal coda devoicing (Magd -> [maːkt]) "
           "needs the syllabifier: word_final under-covers it and "
           "before_consonant would over-devoice onset clusters (Adler). "
           "Model it as a syllable_position:'coda' allophone rule with "
           "voicing assimilation, not a positional grapheme override.",
)
def test_preconsonantal_coda_obstruent_devoices():
    """German ⟨Magd⟩: coda ⟨g⟩ before ⟨d⟩ should devoice to [k] ([maːkt])."""
    ipa = transcribe("Magd", "de-DE")
    assert "k" in ipa and "ɡ" not in ipa
