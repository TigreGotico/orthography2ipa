# Contributing

## Adding or improving language data

Language/dialect specs live under `orthography2ipa/data/*.json`. See
[`docs/adding_a_language.md`](docs/adding_a_language.md) for the schema,
inheritance model, and quality-tier expectations before submitting new
grapheme→IPA mappings, allophone rules, or dialect profiles.

## Branch model

- All work targets `dev`. Never commit to `dev` or `master` directly — open a
  pull request from a feature branch.
- Releases flow `dev` → alpha pre-release → `master` (stable), driven by the
  shared `gh-automations` reusable workflows.
- Commit messages follow the Conventional Commits format (`feat:`, `fix:`,
  `feat!:` / `BREAKING CHANGE:`, `docs:`, `chore:`, ...). The commit prefix
  (or PR label) drives the semantic version bump — never hand-edit
  `orthography2ipa/version.py`.
- Open pull requests as drafts and keep them draft until CI is green;
  mark ready for review only once the automated checks pass.

## Tests

Run the suite before opening a PR:

```bash
pytest tests
```
