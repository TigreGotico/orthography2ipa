# Forcing a pronunciation

Some words are not transcribable from their spelling, and no rule will ever make
them so — a brand name, a proper noun, an acronym, a loanword a speaker says in a
way the orthography does not predict. For these the caller *already knows* the
answer and needs a way to say it.

That way is SSML's `<phoneme>`, which every TTS frontend already speaks:

```python
>>> from orthography2ipa import G2P
>>> G2P("pt-PT").transcribe('olá <phoneme ph="ˈɡuɡɫ">Google</phoneme> mundo')
'oˈla ˈɡuɡɫ ˈmũdu'
```

`alphabet` is optional; when given it must be `ipa`. Text with no markup is
untouched, so a caller who has never heard of `<phoneme>` pays nothing.

## Both halves are load-bearing

* **`ph`** — the IPA. It replaces the rules entirely; nothing is derived.
* **the element's text** — the *spelling*. Not decoration: cross-word rules read
  the orthography, because whether a word carries a case ending is a fact about
  the page and cannot be recovered from its IPA. The `-in` of قَاضٍ is an ending;
  the `-in` of مُؤْمِن is the word. A bare bracket escape carrying only IPA would
  throw the spelling away and break sandhi.

It is also not re-stressed. `ph` is the pronunciation, mark and all: a caller who
wrote `ˈmiːtinɡ` has placed the stress, and one who wrote no mark has said the word
carries none. Re-deriving stress from the spelling would overrule the very thing
being forced.

## Where it sits

A forced reading is the top of a ladder the engine already had:

```
<phoneme ph="…">  >  spec word_exceptions  >  caller's lexicon  >  the rules
```

Every tier answers the same question — *what is this word's IPA?* — and everything
downstream (cross-word sandhi, `confidence == 1.0`) is indifferent to which tier
answered. This adds a tier; it does not add a pipeline.

Markup is read *before* normalization, so a `normalize` plugin — a diacritizer, a
number expander — never sees a tag. It is handed the plain runs and nothing else,
which is the only text it has any business rewriting.

## The inventory is still the law

`ph` is checked against the spec's declared phoneme inventory, and an undeclared
symbol is an error. This is what makes the feature safe rather than a hole in it: a
TTS frontend builds its embedding table from the declared inventory *before*
training, so a symbol appearing only at inference has no vector, and every word
carrying it is mispronounced permanently and silently.

The case that matters is the loanword. English *meeting* is not [ˈmiːtɪŋ] in Saudi
Arabic — it is nativised, and /ɪ/ and /ŋ/ are not Arabic phonemes:

```python
>>> G2P("ar-SA-x-najd").transcribe('<phoneme ph="ˈmiːtɪŋ">meeting</phoneme>')
MarkupError: <phoneme ph='ˈmiːtɪŋ'> uses ['ɪ'], which the ar-SA-x-najd spec does not declare.
```

Give the nativised reading instead — /ŋ/ surfaces as [nɡ], and every symbol is then
one the spec declares:

```python
>>> G2P("ar-SA-x-najd").transcribe(
...     'عِنْدِي <phoneme ph="ˈmiːtinɡ">meeting</phoneme> السَّاعَة')
'ˈʕindiː ˈmiːtinɡ asˈsaːʕa'
```

The inventory is a claim about the phonology, so it discriminates between varieties
that really do differ. MSA declares /q/ and /dʒ/ and no /ɡ/ — /ɡ/ is a Gulf reflex
of qāf — so the *same* nativised reading is refused for `ar` and accepted for
`ar-SA-x-najd`. That is the check working, not fighting you.

A caller who genuinely means to emit a phoneme outside the inventory says so:

```python
>>> G2P("ar-SA-x-najd", allow_undeclared_phonemes=True).transcribe(
...     '<phoneme ph="ˈmiːtɪŋ">meeting</phoneme>')
'ˈmiːtɪŋ'
```

That is an explicit choice, made in code, that anyone reading the call site can
see — which is the whole distinction this library draws. But a standing claim about
the phonology belongs in the spec, where it can be read, cited and diffed.

## Related

A lexicon does the same job for a *list* of words rather than one occurrence, and
is supplied by the caller — nothing is bundled. See
[`data_model.md`](data_model.md).
