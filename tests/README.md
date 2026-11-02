# Tests

The suite runs with pytest from the repository root. `tests/pytest.ini` sets
the markers (`slow`, `linguistic`) and turns an unknown variant subtag
warning into an error. `tests/conftest.py` holds session fixtures for common
specs.

```bash
PYTHONPATH=$PWD .venv/bin/python -m pytest tests
PYTHONPATH=$PWD .venv/bin/python -m pytest $(PYTHONPATH=$PWD .venv/bin/python scripts/which_tests.py --lang fi)
```

`scripts/which_tests.py` names the files that assert on one spec, or on the
specs a branch changed. A family file that passes does not prove that a
`test_cited_rules_*.py` file for the same language passes, so run every file
it names.

## What the files cover

| Files | Cover |
|---|---|
| `test_all_languages.py`, `test_language_integrity.py`, `test_data_quality.py` | Every spec: structure, inheritance and the `production` tier guard |
| `test_sources.py`, `test_catalog_crossrefs.py` | Citations and identifiers |
| `test_cited_rules_*.py` | One cited rule per case, asserted apart from the family files |
| Family and language files, such as `test_celtic.py` or `test_arabic_*.py` | The phonology of one family or one language |
| `test_allophone_rules.py`, `test_stress*.py`, `test_ipa_lattice.py`, `test_rescorer.py`, `test_sandhi.py` | Engine behaviour |
| `test_check_*.py`, `test_compare_systems.py`, `test_thin_row_marker.py` | The benchmark board and its guards |
| `test_docs_prose.py` | The prose lint over every page under `docs/` |
| `test_schema_documents_loader_keys.py` | Every key `json_loader.py` reads is named in `SCHEMA.md` |

`tests/data/` holds small fixtures that the tests and the `ep_dialects` gold
read. Never put a corpus there.

## Burn-down lists

Some tests skip the specs or pages on a list that predates the test:
`_WIKIPEDIA_ONLY_SOURCES_BURNDOWN` in `test_sources.py` and
`_DOCS_PROSE_RATCHET` in `test_docs_prose.py`. A list may only shrink.
`scripts/check_board_not_reverting.py` fails a merge that grows one.
