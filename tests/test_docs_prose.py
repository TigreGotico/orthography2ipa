"""Prose quality of the documentation set, held by a ratchet that only shrinks.

Every page under ``docs/`` is linted by ``scripts/ste_lint.py`` in its
STE-flavoured mode: sentence and paragraph caps, active voice, verb
discipline and the slop rules, with the dictionary lockdown relaxed so the
text keeps natural range. Strict mode is for procedures and safety text,
where a controlled vocabulary is worth losing voice over; a reference manual
read end to end is not that, and strict mode would report hundreds of
violations no one intends to act on.

A page whose path is in ``_DOCS_PROSE_RATCHET`` predates this gate and is
allowed to fail. The list may only ever shrink. Nothing but that rule holds
it down, so two further tests carry it: an entry naming a page that now
passes must be deleted, and an entry naming a page that no longer exists must
be deleted too. Growth is caught outside the suite, by
``scripts/check_board_not_reverting.py``, which reads the list off the merge
result — a branch that resurrects entries makes this suite greener, not
redder, so the suite cannot police its own list.

The generated pages (``comparison.md``, ``spec_diagnostics.md``,
``scoreboard.md``, ``lexicon_scoreboard.md``, ``espeak_agreement.md``) are
linted like any other. Excluding them would leave the longest and most-read
pages permanently unmeasured, and their prose is real prose — it just lives
in ``scripts/compare_systems.py``, ``scripts/spec_diagnostics.py``,
``scripts/benchmark.py``, ``scripts/build_en_lexicon.py`` and
``scripts/espeak_agreement.py``. Fixing one of these means editing the
generator and regenerating the page.
"""
import glob
import importlib.util
import os

import pytest

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DOCS_DIR = os.path.join(_ROOT, "docs")

#: Pages that fail the flavoured threshold and are waiting to be rewritten.
#: MAY ONLY SHRINK. Do not add a page here to make a red build green: a page
#: not on this list is required to pass.
#:
#: comparison.md and spec_diagnostics.md are generated; their prose is fixed
#: in scripts/compare_systems.py and scripts/spec_diagnostics.py respectively,
#: then the page is regenerated.
_DOCS_PROSE_RATCHET = frozenset({
    "docs/allophony.md",
    "docs/comparison.md",
    "docs/gold_composition.md",
    "docs/gold_defects.md",
    "docs/known_limitations.md",
    "docs/languages/ar-IQ.md",
    "docs/languages/ar-maghrebi-yemeni-sudanese.md",
    "docs/languages/ar-x-levantine.md",
    "docs/languages/egy.md",
    "docs/languages/en-GB.md",
    "docs/languages/ext-PT-x-barrancos.md",
    "docs/languages/fo.md",
    "docs/languages/fr-FR.md",
    "docs/languages/germanic.md",
    "docs/languages/ha.md",
    "docs/languages/index.md",
    "docs/languages/it-IT.md",
    "docs/languages/kab.md",
    "docs/languages/mn.md",
    "docs/languages/pt-PT-x-viana.md",
    "docs/languages/pt-TL.md",
    "docs/languages/pt-UY.md",
    "docs/languages/slavic.md",
    "docs/languages/th.md",
    "docs/languages/vi.md",
    "docs/languages/yo.md",
    "docs/link-audit.md",
    "docs/ranking_error.md",
    "docs/spec_diagnostics.md",
})


def _load_linter():
    """The vendored STE linter, imported from scripts/ by path.

    scripts/ is not a package, and the linter is a standalone file kept in
    step with the ste-writing skill it came from.
    """
    path = os.path.join(_ROOT, "scripts", "ste_lint.py")
    spec = importlib.util.spec_from_file_location("ste_lint", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ste_lint = _load_linter()


def _docs_pages():
    """Every markdown page under docs/, as repository-relative paths."""
    pattern = os.path.join(_DOCS_DIR, "**", "*.md")
    return sorted(os.path.relpath(p, _ROOT).replace(os.sep, "/")
                  for p in glob.glob(pattern, recursive=True))


def _report(page):
    with open(os.path.join(_ROOT, page), encoding="utf-8") as fh:
        return ste_lint.lint(fh.read(), "flavored")


_PAGES = _docs_pages()


@pytest.mark.parametrize("page", _PAGES, ids=_PAGES)
def test_docs_page_prose(page: str) -> None:
    """A documentation page must pass the STE-flavoured threshold."""
    if page in _DOCS_PROSE_RATCHET:
        pytest.skip(f"{page}: pre-existing prose violations, tracked in the "
                    f"ratchet list (_DOCS_PROSE_RATCHET)")
    report = _report(page)
    assert report["pass"], (
        f"{page}: {report['per100w']} violations per 100 words "
        f"(threshold 2.0), {report['violations']}. Rewrite the prose with the "
        f"ste-writing skill; do NOT add the page to _DOCS_PROSE_RATCHET, which "
        f"may only shrink."
    )


@pytest.mark.parametrize("page", sorted(_DOCS_PROSE_RATCHET), ids=sorted(_DOCS_PROSE_RATCHET))
def test_ratchet_entry_still_needed(page: str) -> None:
    """A ratchet entry whose page now passes must be removed from the list."""
    if not os.path.exists(os.path.join(_ROOT, page)):
        pytest.fail(f"{page} is on _DOCS_PROSE_RATCHET but does not exist. "
                    f"Remove the entry.")
    report = _report(page)
    assert not report["pass"], (
        f"{page} now passes the prose gate at {report['per100w']} violations "
        f"per 100 words. Remove it from _DOCS_PROSE_RATCHET so it stays fixed."
    )
