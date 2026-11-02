<!--
AI disclosure: if a model wrote any part of this change, keep the line below
as the first line of the description, with the exact model name. Delete it
when no model was involved.
-->
> AI disclosure: written by <model name and id>, auto-generated, not human-reviewed.

## What changed

<!-- One or two sentences: what changed and why. -->

## What the reviewer must decide

<!-- The question you need answered. Write "nothing" when the change only fixes a bug. -->

## Board rows

<!--
A change that moves board rows it does not own, such as a harness or engine
change, names them on a line of its own that starts with the Board-Rows key.
Examples: "Board-Rows: mr/wikipron, xh/kaikki", or "Board-Rows: all - <reason>"
when the change rescored the whole board. scripts/check_board_not_reverting.py
checks that line against the rows the merge moves, and a line it cannot parse
is an error. Write "No board rows move" when that is true.
-->
No board rows move.

## Spec checklist

<!-- Delete this section when no file in orthography2ipa/data/ changed. -->

- [ ] Every new mapping cites a source I opened, with the page, in `sources` and `notes`.
- [ ] Wikipedia and Ciberdúvidas appear only as extra sources.
- [ ] No reference set written by a model or pinned to this engine is called gold.
- [ ] Each new `graphemes` key is an orthographic unit, not an n-gram or a cartesian product.
- [ ] Context is in the rule layer, not in extra keys.
- [ ] `quality` is honest.
- [ ] I ran `scripts/which_tests.py --lang <code>` and every file it names passes.
- [ ] I ran the board guards in `docs/contributing/board.md`.

## Tests

<!-- The commands you ran and their pass, fail and skip counts. -->
