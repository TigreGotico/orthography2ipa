# Command line

The package installs one command, `orthography2ipa`. Each subcommand takes `--json` for output that a program can read. The blocks below are the real `--help` output. The top-level description prints the number of registered languages, shown here as N.

`scripts/gen_reference_docs.py` writes this page. Do not edit it by hand.

## `orthography2ipa`

    usage: orthography2ipa [-h] [--version]
                           {list,info,transcribe,distance,validate} ...

    Grapheme-to-IPA mappings and phonological tools for N languages.

    positional arguments:
      {list,info,transcribe,distance,validate}
        list                List available language codes or families.
        info                Show details for a language code.
        transcribe          Transcribe text to IPA.
        distance            Compute phonological distance between two languages.
        validate            Validate language spec JSON files against the schema.

    options:
      -h, --help            show this help message and exit
      --version             Print version and exit.

## `orthography2ipa list`

    usage: orthography2ipa list [-h] [--families] [--family FAMILY] [--json]

    options:
      -h, --help       show this help message and exit
      --families       Group codes by language family.
      --family FAMILY  Filter codes to a single family (e.g. Romance).
      --json           Output as JSON.

## `orthography2ipa info`

    usage: orthography2ipa info [-h] [--json] [--graphemes] [--allophones] code

    positional arguments:
      code          A BCP-47 or ISO-639-3 language code.

    options:
      -h, --help    show this help message and exit
      --json        Output full spec as JSON.
      --graphemes   Print only the grapheme→IPA map.
      --allophones  Print only the allophone map.

## `orthography2ipa transcribe`

    usage: orthography2ipa transcribe [-h] [--search {greedy,beam}]
                                      [--beam-width BEAM_WIDTH]
                                      [--dialect-profile DIALECT_PROFILE] [--json]
                                      code text

    positional arguments:
      code                  A BCP-47 or ISO-639-3 language code.
      text                  The word or phrase to transcribe.

    options:
      -h, --help            show this help message and exit
      --search {greedy,beam}
                            Candidate search: best path per word (greedy, default)
                            or keep a beam of alternatives (beam).
      --beam-width BEAM_WIDTH, --beam BEAM_WIDTH
                            Beam width for --search beam (default: 8).
      --dialect-profile DIALECT_PROFILE
                            Dialect transform profile applied to the final IPA.
      --json                Output as JSON.

## `orthography2ipa distance`

    usage: orthography2ipa distance [-h] [--json] code1 code2

    positional arguments:
      code1       The first language code.
      code2       The second language code.

    options:
      -h, --help  show this help message and exit
      --json      Output as JSON.

## `orthography2ipa validate`

    usage: orthography2ipa validate [-h] [--json] [code]

    positional arguments:
      code        Validate a single language code (default: all specs).

    options:
      -h, --help  show this help message and exit
      --json      Output the validation report as JSON.

---
[← Python API](api.md) · [Home](../index.md) · [Tokenizer →](../tokenizer.md)
