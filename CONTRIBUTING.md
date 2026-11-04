# Contributing

Read [AGENTS.md](AGENTS.md) first. It holds the repository map, the setup,
the hard rules and the checks to run before a push. The detail pages are in
[docs/contributing/](docs/contributing/spec_authoring.md).

## Language data

Specs live in `orthography2ipa/data/*.json`. Read
[docs/contributing/spec_authoring.md](docs/contributing/spec_authoring.md) and
[docs/contributing/citations.md](docs/contributing/citations.md)
before you add or change a grapheme map, an allophone rule or a dialect. The
fields are in [`orthography2ipa/data/SCHEMA.md`](orthography2ipa/data/SCHEMA.md).

## Branch model

- All work targets `dev`. Never commit to `dev` or `master` directly. Open a
  pull request from a feature branch.
- Releases flow from `dev` to an alpha pre-release to `master` (stable),
  driven by the shared `gh-automations` reusable workflows.
- Commit messages follow Conventional Commits (`feat:`, `fix:`, `feat!:`,
  `docs:`, `chore:`). The prefix or the pull request label drives the
  semantic version bump. Never edit `orthography2ipa/version.py` by hand.
- Open a pull request as a draft. Mark it ready for review when CI is green.

## Tests

Run the suite in a venv inside the checkout before you open a pull request:

```bash
unset VIRTUAL_ENV
uv venv --python 3.11 .venv
uv pip install --python .venv --prerelease=allow -e '.[test]'
PYTHONPATH=$PWD .venv/bin/python -m pytest tests
```

If you changed only a spec, `scripts/which_tests.py --lang <code>` names the
test files that assert on it. Run those while you work, and run the full
suite before you push.
