# orthography2ipa: Documentation

**[index.md](index.md) is the front door.** It states what the library is,
where its accuracy limits are, and it holds the reading order for every page
here. Every other page links its neighbours in a footer, so you can read the
set in order or jump in anywhere.

`orthography2ipa` measures how languages relate to each other across
independent axes (phonological, reading, spelling, script, genealogical,
temporal, geographic), and converts orthography to IPA from the same
per-language data: cited JSON specs with no trained weights, covering hundreds
of languages plus classification-only clade nodes. Run
`len(orthography2ipa.available_codes())` and
`len(orthography2ipa.available_codes(include_clades=True))` for the live
counts.

```python
import orthography2ipa as o2i
from orthography2ipa.distance import grapheme_divergence, spelling_divergence

o2i.transcribe("olá mundo", "pt")   # 'oˈla ˈmũdu'

gl, glr = o2i.get("gl"), o2i.get("gl-x-reintegrado")
grapheme_divergence(gl, glr).mean_ipa_distance   # 0.0233: they read alike
spelling_divergence(gl, glr).mean_distance       # 0.0659: they are written differently
```

The authoring reference for a spec JSON file is
[`orthography2ipa/data/SCHEMA.md`](../orthography2ipa/data/SCHEMA.md).
