"""Tests for scripts/restore_wikipron_orthography.py.

The dangerous failure mode is cross-language contamination: a Wiktionary
page holds one section per language, and a page-wide match would write
another language's orthography into the gold. ``Adam`` is the worked
example — English ``Adam``, Ewe ``Ádàm``, Hausa ``Adàm`` and Old English
``Adam`` all live on it. These run offline against fixture wikitext and
fixture render output.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import restore_wikipron_orthography as rwo  # noqa: E402


ADAM_WIKITEXT = """{{also|Appendix:Variations of "adam"}}
==English==
===Proper noun===
{{en-prop|s}}

==Ewe==
===Proper noun===
{{head|ee|proper noun|head=Ádàm}}

==Hausa==
===Proper noun===
{{ha-proper noun|m|Adàm}}

==Old English==
===Proper noun===
{{ang-proper noun|m|head=Adam}}
"""

ADAM_HTML = (
    '<strong class="Latn headword" lang="en">Adam</strong>'
    '<strong class="Latn headword" lang="ee">Ádàm</strong>'
    '<strong class="Latn headword" lang="ha">Adàm</strong>'
    '<strong class="Latn headword" lang="ang">Adam</strong>'
)


def _render(_title):
    return ADAM_HTML


def test_section_scoping_picks_the_target_language():
    section = rwo.language_section(ADAM_WIKITEXT, "Ewe")
    assert "head=Ádàm" in section
    assert "en-prop" not in section
    assert "ha-proper noun" not in section


def test_absent_section_is_none():
    assert rwo.language_section(ADAM_WIKITEXT, "Yoruba") is None


def test_ewe_restores_its_own_headword_not_english():
    restored, outcome = rwo.restore_word(
        "Adam", ADAM_WIKITEXT, "Ewe", "ee", _render)
    assert (restored, outcome) == ("Ádàm", "restored")


def test_hausa_headword_is_not_imported_into_ewe():
    """The Hausa display form ``Adàm`` shares Adam's skeleton too.

    A page-wide reader would happily return it for Ewe. Both the
    wikitext section cut and the ``lang`` attribute filter must keep it
    out.
    """
    heads = rwo.rendered_headwords(ADAM_HTML, "ee")
    assert heads == {"Ádàm"}
    assert "Adàm" not in heads


def test_language_without_a_restoration_is_uncovered():
    """Old English displays the bare title: nothing to restore."""
    restored, outcome = rwo.restore_word(
        "Adam", ADAM_WIKITEXT, "Old English", "ang", _render)
    assert restored is None
    assert outcome == "no_headword"


def test_missing_section_reported_not_guessed():
    restored, outcome = rwo.restore_word(
        "Adam", ADAM_WIKITEXT, "Yoruba", "yo", _render)
    assert (restored, outcome) == (None, "no_section")


def test_conflicting_headwords_are_refused():
    html = ('<strong class="Latn headword" lang="ee">Ádàm</strong>'
            '<strong class="Latn headword" lang="ee">Àdam</strong>')
    restored, outcome = rwo.restore_word(
        "Adam", ADAM_WIKITEXT, "Ewe", "ee", lambda _t: html)
    assert (restored, outcome) == (None, "conflict")


def test_skeleton_gate_discards_a_different_base_form():
    html = '<strong class="Latn headword" lang="ee">Evà</strong>'
    restored, outcome = rwo.restore_word(
        "Adam", ADAM_WIKITEXT, "Ewe", "ee", lambda _t: html)
    assert (restored, outcome) == (None, "skeleton_mismatch")


def test_skeleton_strips_only_combining_marks():
    assert rwo.skeleton("Ádàm") == "Adam"
    assert rwo.skeleton("hëlfen") == "helfen"
    # Middle High German umlauts are separate letters, not restorations
    assert rwo.skeleton("hüten") == "huten"


def test_output_is_nfc():
    restored, _ = rwo.restore_word("Adam", ADAM_WIKITEXT, "Ewe", "ee", _render)
    import unicodedata
    assert restored == unicodedata.normalize("NFC", restored)


def test_middle_high_german_takes_its_own_section_not_old_high_german():
    """``helfen`` carries a gmh headword and a goh one with a macron.

    The Old High German form ``hëlfēn`` differs from the Middle
    High German ``hëlfen``; reading the page instead of the section
    would import the wrong one.
    """
    wikitext = (
        "==German==\n{{de-verb|helfen}}\n"
        "==Middle High German==\n{{gmh-verb|hëlfen<half,geholfen>}}\n"
        "==Old High German==\n{{head|goh|verb form|head=hëlfēn}}\n")
    html = ('<strong class="Latn headword" lang="de">helfen</strong>'
            '<strong class="Latn headword" lang="gmh">hëlfen</strong>'
            '<strong class="Latn headword" lang="goh">hëlfēn</strong>')
    restored, outcome = rwo.restore_word(
        "helfen", wikitext, "Middle High German", "gmh", lambda _t: html)
    assert (restored, outcome) == ("hëlfen", "restored")


def test_positional_headword_template_is_still_a_render_candidate():
    """``{{ee-proper noun|Àfɔ̀fìlɛ́}}`` carries the head positionally.

    Restricting candidate detection to ``head=`` would skip the page and
    under-report coverage, so any argument sharing the title's skeleton
    makes the page worth rendering.
    """
    section = "\n===Proper noun===\n{{ee-proper noun|Àfɔ̀fiɛ́}}\n"
    assert rwo.worth_rendering("Afɔfiɛ", section, "ee")


def test_positional_head_scoping_is_as_strict_as_head_scoping():
    """A positional head in another language's section stays out.

    ``{{ha-proper noun|m|Adàm}}`` carries its headword positionally and
    shares Adam's skeleton, so a candidate scan that forgot to cut the
    page down to the target section would take it for an Ewe
    restoration.
    """
    hausa_only = ("==English==\n{{en-prop|s}}\n"
                  "==Hausa==\n{{ha-proper noun|m|Adàm}}\n"
                  "==Ewe==\n{{head|ee|proper noun}}\n")
    section = rwo.language_section(hausa_only, "Ewe")
    assert rwo.headword_args(section, "ee") == {"proper noun"}
    assert not rwo.worth_rendering("Adam", section, "ee")
    # and the whole page, read without scoping, would have offered it
    assert "Adàm" in rwo.headword_args(hausa_only, "ha")


def test_registered_languages_are_keyed_by_the_wikipron_file_prefix():
    """One key per language, not per scrape file.

    Broad and narrow scrapes of a language share page titles, so they
    share one restoration and one set of renders.
    """
    assert {"ewe", "gmh", "yor", "heb"} <= set(rwo.LANGS)
    assert all("_" not in key for key in rwo.LANGS)


def test_the_wiktionary_code_is_not_assumed_to_be_the_file_prefix():
    """``ewe`` scrapes are tagged ``ee`` in Wiktionary's templates."""
    assert rwo.LANGS["ewe"] == ("Ewe", "ee")
    assert rwo.LANGS["yor"] == ("Yoruba", "yo")
    assert rwo.LANGS["nya"] == ("Chichewa", "ny")


def test_every_restorable_language_is_screened_as_affected():
    """A language is never restored on a hunch; the screen gates it."""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                    "scripts"))
    import wikipron_mirror

    for lang in rwo.LANGS:
        verdict = wikipron_mirror.SCREEN[lang][0]
        assert verdict in ("confirmed", "confirmed_empirical"), (lang, verdict)
