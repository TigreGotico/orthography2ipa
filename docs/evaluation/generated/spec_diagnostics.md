# Spec diagnostics

<!-- agent-hint
covers: the gold characters each spec cannot map, the inheritance that crosses a family line, and the specs whose tables match another language
source: `scripts/spec_diagnostics.py`, the specs in `orthography2ipa/data/`, the gold cache in `.benchmark_cache/`
generated: yes, by `scripts/spec_diagnostics.py`. Edit the generator, not the page
verify: `PYTHONPATH=$PWD python -m pytest tests/test_spec_diagnostics.py`
see: `docs/guide/known_limitations.md`, `docs/evaluation/gold_defects.md`
-->

Regenerate with `PYTHONPATH=$PWD python3 scripts/spec_diagnostics.py`. Three mechanical signals separate a spec that is wrong from a spec that is merely imprecise: gold characters its grapheme table cannot consume, which the engine deletes before a rule can see them. Inheritance that crosses a language-family boundary. A table that matches another language almost pair for pair. None is proof on its own. Each points at a spec worth reading before any rule in it is refined.

Of 7679 specs, 496 have a cached gold to measure against, and 341 of those leave at least one gold character unmapped.

A language scored on several gold datasets is reported here **per dataset**, not unioned. Unioning inflates the count (a character can be unmapped in one corpus only). It also blends unrelated problems, such as the loanword letters of one dataset and the diacritic gaps of another, into a single misleading figure. The `combined_*` fields in the JSON output keep the union for reference, but every ranking below and every row you might prioritise off of is per dataset.

## Ranked by unmapped gold characters (per dataset)

- **ja** (Japanese) / `vox_communis`: 1268 of 1419 gold characters unmapped, hitting 67.5% of 5000 scanned words. Own table 305 graphemes, resolved 305, worst per 0.4273, n 158050.
  - unmapped: `一 丁 七 万 丈 三 上 下 不 与 世 両 並 中 丸 丹 主 久 之 乗 九 乱 乳 乾 亀 了 予 争 事 二 互 五 井 亡 交 京 亭 人 今 介 仏 仕 他 付 代 令 以 仰 件 任 企 伊 伏 休 会 伝 伸 位 低 住`
  - chain: inherits=jpx [Japonic]
  - no stress block reachable
- **ja** (Japanese) / `ipadict`: 1120 of 1269 gold characters unmapped, hitting 73.2% of 5000 scanned words. Own table 305 graphemes, resolved 305, worst per 0.4273, n 158050.
  - unmapped: `× α ※ ← ↑ → ↓ △ ○ ◎ 〃 々 〆 〇 〒 ゝ ヵ ヶ ・ 一 丁 七 万 三 上 下 不 世 両 並 中 丸 主 丼 久 乍 乗 乱 乳 亀 了 事 二 互 五 井 亡 交 人 仁 介 仏 仕 他 付 仝 代 令 以 仲`
  - chain: inherits=jpx [Japonic]
  - no stress block reachable
- **en-GB** (British English (RP)) / `wikipron`: 31 of 57 gold characters unmapped, hitting 2.9% of 5000 scanned words. Own table 84 graphemes, resolved 84, worst per 0.2959, n 158101.
  - unmapped: `' á â ã ä å æ ç é ê ë í ñ ó ö ú ü ā ă č ē ę ě ī ł œ ś ş ș ț ʼ`
  - chain: inherits=enm [Indo-European > Germanic > Northwest Germanic > West Germanic]
- **ab** (Abkhaz) / `wikipron`: 20 of 59 gold characters unmapped, hitting 25.2% of 206 scanned words. Own table 67 graphemes, resolved 67, worst per 0.2311, n 32345.
  - unmapped: `' ь ҙ ә ԡ ԣ ԫ ԭ ꚁ ꚃ ꚅ ꚇ ꚉ ꚋ ꚍ ꚏ ꚑ ꚓ ꚕ ꚗ`
  - chain: inherits=x-clade-abkh1242 [?]
  - no stress block reachable
- **cy** (Welsh) / `wikipron`: 16 of 44 gold characters unmapped, hitting 1.5% of 5000 scanned words. Own table 40 graphemes, resolved 40, worst per 0.2985, n 38123.
  - unmapped: `' k v x z à á é ë ï ò ö ü ý ẃ ỳ`
  - chain: inherits=xbr [Indo-European > Celtic > Brythonic]
  - no stress block reachable
- **wbk** (Waigali) / `wikipron`: 15 of 48 gold characters unmapped, hitting 46.1% of 154 scanned words. Own table 41 graphemes, resolved 41, worst per 0.2022, n 153.
  - unmapped: `v ã ä ë ö ü ć ň ř ũ ǖ ̃ ̣ ṅ ẽ`
  - chain: inherits=x-clade-indo1320 [Indo-European]
  - no stress block reachable
- **cy** (Welsh) / `vox_communis`: 13 of 41 gold characters unmapped, hitting 5.0% of 5000 scanned words. Own table 40 graphemes, resolved 40, worst per 0.2985, n 38123.
  - unmapped: `' k q v x z ¬ á ä é ï ñ ö`
  - chain: inherits=xbr [Indo-European > Celtic > Brythonic]
  - no stress block reachable
- **yo** (Yoruba) / `wikipron`: 13 of 38 gold characters unmapped, hitting 3.0% of 4937 scanned words. Own table 56 graphemes, resolved 56, worst per 0.6392, n 9328.
  - unmapped: `c z ɔ ɛ ̀ ́ ̂ ̄ ̌ ḿ ị ộ ụ`
  - chain: inherits=nic [Atlantic-Congo]
  - no stress block reachable
- **ess** (Central Siberian Yupik) / `northeuralex`: 12 of 36 gold characters unmapped, hitting 27.4% of 814 scanned words. Own table 29 graphemes, resolved 29, worst per 0.1074, n 814.
  - unmapped: `̌ б д е ж о ц ч ш щ ь ӽ`
  - chain: inherits=x-clade-eski1264 [?]
  - no stress block reachable
- **fi** (Finnish) / `wikipron`: 12 of 38 gold characters unmapped, hitting 1.1% of 5000 scanned words. Own table 62 graphemes, resolved 62, worst per 0.0609, n 274968.
  - unmapped: `' q x á å é ú ü ă š ž ș`
  - chain: inherits=x-clade-finn1317 [Uralic]
- **kok** (Konkani) / `kaikki`: 12 of 65 gold characters unmapped, hitting 0.4% of 835 scanned words. Own table 76 graphemes, resolved 76, worst per 0.2241, n 830.
  - unmapped: `g y õ ಂ ಜ ಣ ನ ಪ ರ ು ೆ ೊ`
  - chain: inherits=sa [Indo-European > Indo-Iranian > Indo-Aryan]
  - no stress block reachable
- **kw** (Cornish) / `wikipron`: 12 of 35 gold characters unmapped, hitting 4.2% of 648 scanned words. Own table 31 graphemes, resolved 31, worst per 0.2521, n 602.
  - unmapped: `c à â è ë ò ÿ ɐ ᵹ ꝺ ꝿ ꞇ`
  - chain: inherits=xbr [Indo-European > Celtic > Brythonic]
  - no stress block reachable
- **li** (Limburgish) / `wikipron`: 12 of 41 gold characters unmapped, hitting 33.6% of 1128 scanned words. Own table 120 graphemes, resolved 120, worst per 0.3099, n 987.
  - unmapped: `' ä é ë ï ü ą ǫ ̈ ̩ ͜ ṣ`
  - chain: inherits=x-clade-germ1287 [Indo-European]
- **my** (Burmese) / `wikipron`: 11 of 59 gold characters unmapped, hitting 2.9% of 5000 scanned words. Own table 231 graphemes, resolved 231, worst per 0.1926, n 7941.
  - unmapped: `့ း ္ ် ျ ြ ှ ၍ ၏ ၐ ၑ`
  - chain: inherits=sit [Sino-Tibetan]
  - no stress block reachable
- **eu** (Basque (Euskara)) / `ipa_childes`: 10 of 32 gold characters unmapped, hitting 5.0% of 3969 scanned words. Own table 35 graphemes, resolved 35, worst per 0.0984, n 82531.
  - unmapped: `c q v w y á é í ó ú`
  - chain: inherits=xaq [Vasconic]
- **lad** (Ladino (Judeo-Spanish)) / `wikipron`: 10 of 33 gold characters unmapped, hitting 15.2% of 145 scanned words. Own table 35 graphemes, resolved 35, worst per 0.1397, n 151.
  - unmapped: `c q á é í ó ú ü ĵ ḥ`
  - chain: inherits=es-ES-x-medieval [Indo-European > Italic > Romance > Ibero-Romance]
  - no stress block reachable
- **smn** (Inari Sami) / `northeuralex`: 10 of 41 gold characters unmapped, hitting 27.5% of 1055 scanned words. Own table 31 graphemes, resolved 31, worst per 0.16, n 1055.
  - unmapped: `' ñ ̣ ḋ ḥ ḷ ṃ ṇ ṛ ṿ`
  - chain: inherits=urj [Uralic]
  - no stress block reachable
- **chb** (Chibcha) / `wikipron`: 9 of 28 gold characters unmapped, hitting 19.0% of 121 scanned words. Own table 22 graphemes, resolved 22, worst per 0.1313, n 99.
  - unmapped: `d k l r v â ç ȩ ɣ`
  - chain: inherits=x-clade-chib1249 [?]
  - no stress block reachable
- **gwd** (Gawwada) / `wold`: 9 of 34 gold characters unmapped, hitting 9.9% of 976 scanned words. Own table 33 graphemes, resolved 33, worst per 0.0385, n 976.
  - unmapped: `c x z á í ú ħ ɲ ʤ`
  - chain: inherits=x-clade-afro1255 [?]
  - no stress block reachable
- **lou** (Louisiana Creole) / `wikipron`: 9 of 37 gold characters unmapped, hitting 12.2% of 262 scanned words. Own table 36 graphemes, resolved 36, worst per 0.1953, n 262.
  - unmapped: `' á æ ç ê ì ñ ô œ`
  - chain: inherits=x-clade-roma1334 [Indo-European > Italic]
  - no stress block reachable

## Ranked by share of gold words that lose a character (per dataset)

The character count above treats a rare loan letter and a missing nasal vowel series alike. This ordering weights each spec/dataset pair by how much of that dataset's own gold the deletion actually touches.

- **mhr** (Eastern Mari) / `northeuralex`: 85.2% of 992 scanned words lose at least one character. Unmapped `́`, worst per 0.1736.
- **nhg** (Tetelcingo Nahuatl) / `wikipron`: 76.7% of 305 scanned words lose at least one character. Unmapped `b d f j r ö ā ̱`, worst per 0.2367.
- **nhx** (Isthmus-Mecayapan Nahuatl) / `wikipron`: 75.3% of 146 scanned words lose at least one character. Unmapped `r z á é í ñ ó ̱ ꞌ`, worst per 0.1852.
- **ja** (Japanese) / `ipadict`: 73.2% of 5000 scanned words lose at least one character. Unmapped `× α ※ ← ↑ → ↓ △ ○ ◎ 〃 々 〆 〇 〒 ゝ ヵ ヶ ・ 一 丁 七 万 三 上 下 不 世 両 並`, worst per 0.4273.
- **ja** (Japanese) / `vox_communis`: 67.5% of 5000 scanned words lose at least one character. Unmapped `一 丁 七 万 丈 三 上 下 不 与 世 両 並 中 丸 丹 主 久 之 乗 九 乱 乳 乾 亀 了 予 争 事 二`, worst per 0.4273.
- **shn** (Shan) / `wikipron`: 61.9% of 2607 scanned words lose at least one character. Unmapped `ဵ ် ျ ြ ွ ႂ ႃ ႅ ႆ`, worst per 0.2985.
- **aeb-TN** (Tunisian Arabic) / `arabic_tts`: 60.0% of 20 scanned words lose at least one character. Unmapped `، ؟`, worst per 0.3059.
- **aeb-TN** (Tunisian Arabic) / `gold20_arabic`: 60.0% of 20 scanned words lose at least one character. Unmapped `، ؟`, worst per 0.3059.
- **apc-JO** (Jordanian Arabic (Ammani)) / `arabic_tts`: 55.0% of 20 scanned words lose at least one character. Unmapped `، ؟`, worst per 0.3451.
- **apc-JO** (Jordanian Arabic (Ammani)) / `gold20_arabic`: 55.0% of 20 scanned words lose at least one character. Unmapped `، ؟`, worst per 0.3451.
- **apd-SD** (Sudanese Arabic) / `arabic_tts`: 55.0% of 20 scanned words lose at least one character. Unmapped `، ؟`, worst per 0.1069.
- **apd-SD** (Sudanese Arabic) / `gold20_arabic`: 55.0% of 20 scanned words lose at least one character. Unmapped `، ؟`, worst per 0.1069.
- **ady** (Adyghe) / `northeuralex`: 50.3% of 928 scanned words lose at least one character. Unmapped `́ в ь`, worst per 0.1684.
- **afb-AE** (Emirati Arabic) / `arabic_tts`: 50.0% of 20 scanned words lose at least one character. Unmapped `، ؟`, worst per 0.0765.
- **afb-AE** (Emirati Arabic) / `gold20_arabic`: 50.0% of 20 scanned words lose at least one character. Unmapped `، ؟`, worst per 0.0765.
- **cic** (Chickasaw) / `wikipron`: 48.7% of 394 scanned words lose at least one character. Unmapped `e v á í ó ̠ ̱ ꞌ`, worst per 0.1028.
- **klj** (Khalaj) / `wikipron`: 47.7% of 155 scanned words lose at least one character. Unmapped `â ê î ñ ô û ̂`, worst per 0.2995.
- **cri** (Sãotomense (Forro / Santome)) / `primary_sources`: 46.2% of 13 scanned words lose at least one character. Unmapped `c h q ç é ó`, worst per 0.2147.
- **wbk** (Waigali) / `wikipron`: 46.1% of 154 scanned words lose at least one character. Unmapped `v ã ä ë ö ü ć ň ř ũ ǖ ̃ ̣ ṅ ẽ`, worst per 0.2022.
- **acx-OM** (Omani Arabic) / `arabic_tts`: 45.0% of 20 scanned words lose at least one character. Unmapped `، ؟`, worst per 0.1448.

## Tables asserted from another language

A spec's closest table twin among the specs it does not declare as a base. A ratio near 1 means the table was taken from that language rather than written for this one. The notes then describe a language the data never encodes.

- **koi** (Komi-Permyak, Uralic): graphemes kv 1.0, allophones none. Declares inherits=x-clade-ural1272 [?], worst per 0.092.
- **kv** (Komi, Uralic): graphemes koi 1.0, allophones none. Declares inherits=x-clade-ural1272 [?], worst per 0.157.
- **mqs** (West Makian, North Halmahera): graphemes tft 1.0, allophones none. Declares inherits=x-clade-nort2923 [?], worst per 0.0495.
- **nap** (Neapolitan, Indo-European > Italic > Romance > Italo-Romance): graphemes it-IT-x-abruzzo 0.854, allophones it-IT-x-abruzzo 1.0. Declares inherits=x-clade-italorom [Indo-European > Italic > Romance], worst per 0.2792.
- **tft** (Ternate, North Halmahera): graphemes mqs 1.0, allophones none. Declares inherits=x-clade-nort2923 [?], worst per 0.1041.
- **it-IT** (Italian, Indo-European > Italic > Romance > Italo-Romance): graphemes co 0.634, allophones nap 0.979. Declares inherits=x-clade-italorom [Indo-European > Italic > Romance], worst per 0.2353.
- **sa** (Sanskrit, Indo-European > Indo-Iranian > Indo-Aryan): graphemes vsn 0.859, allophones vsn 0.979. Declares inherits=x-clade-indo1321 [Indo-European > Indo-Iranian], worst per 0.0161.
- **tzm** (Central Atlas Tamazight, Afro-Asiatic > Berber): graphemes zgh 0.971, allophones none. Declares inherits=ber-x-kabyle-atlas [Afro-Asiatic > Berber], worst per 0.016.
- **es-ES-x-medieval** (Castilian, Indo-European > Italic > Romance > Ibero-Romance): graphemes an 0.81, allophones lad 0.968. Declares inherits=x-clade-iberrom [Indo-European > Italic > Romance], worst per 0.0438.
- **ban** (Balinese, Austronesian): graphemes min 0.871, allophones su 0.963. Declares inherits=x-clade-aust1307 [?], worst per 0.163.
- **rw** (Kinyarwanda, Atlantic-Congo > Bantu): graphemes lua 0.8, allophones lua 0.963. Declares inherits=x-clade-narr1281 [Atlantic-Congo], worst per 0.1388.
- **su** (Sundanese, Austronesian > Malayo-Polynesian): graphemes kge 0.893, allophones ban 0.963. Declares inherits=x-clade-mala1545 [Austronesian], worst per 0.0978.
- **mak** (Makasar, Austronesian): graphemes gor 0.962, allophones none. Declares inherits=poz [Austronesian], worst per 0.0194.
- **iba** (Iban, Austronesian > Malayo-Polynesian): graphemes lmy 0.957, allophones ban 0.889. Declares inherits=x-clade-mala1545 [Austronesian], worst per 0.1655.
- **lmy** (Lamboya, Austronesian > Malayo-Polynesian): graphemes iba 0.957, allophones none. Declares inherits=x-clade-mala1545 [Austronesian], worst per 0.1695.
- **ceb** (Cebuano, Austronesian > Malayo-Polynesian): graphemes ilo 0.913, allophones pam 0.955. Declares inherits=x-clade-mala1545 [Austronesian], worst per 0.1058.
- **pam** (Kapampangan, Austronesian > Malayo-Polynesian): graphemes hil 0.952, allophones ceb 0.955. Declares inherits=x-clade-mala1545 [Austronesian], worst per 0.2861.
- **de-DE** (German, Indo-European > Germanic > Northwest Germanic > West Germanic): graphemes nds 0.736, allophones nds 0.953. Declares inherits=x-clade-west2793 [Indo-European > Germanic > Northwest Germanic], worst per 0.3948.
- **nds** (Low German (Plattdeutsch), Indo-European > Germanic > Northwest Germanic > West Germanic): graphemes de-DE 0.736, allophones de-DE 0.953. Declares inherits=osx [Indo-European > Germanic > Northwest Germanic > West Germanic], worst per 0.2231.
- **hil** (Hiligaynon, Austronesian > Malayo-Polynesian): graphemes pam 0.952, allophones none. Declares inherits=x-clade-mala1545 [Austronesian], worst per 0.0966.

## Ranked by cross-family inheritance

- **ext-PT-x-barranco** (Barranquenho, Mixed Language): graphemes_base=pt-PT [Indo-European > Italic > Romance > Ibero-Romance] CROSS-FAMILY, allophones_base=pt-PT [Indo-European > Italic > Romance > Ibero-Romance] CROSS-FAMILY, positional_graphemes_base=pt-PT [Indo-European > Italic > Romance > Ibero-Romance] CROSS-FAMILY, word_exceptions_base=pt-PT [Indo-European > Italic > Romance > Ibero-Romance] CROSS-FAMILY. Per 0.2912, 0 unmapped gold chars (union across datasets).
- **new** (Newar, Sino-Tibetan): inherits=x-clade-sino1245 [?], graphemes_base=hi [Indo-European > Indo-Iranian > Indo-Aryan] CROSS-FAMILY. Per 0.0282, 0 unmapped gold chars (union across datasets).

## Declared inventory contradicting emitted output

- **ii** (Nuosu): declares 74 phonemes it never emits and emits 1165 it never declares. Chain: inherits=x-clade-sino1245 [?].
- **nmn** (ǃXóõ): declares 94 phonemes it never emits and emits 154 it never declares. Chain: inherits=x-clade-tuuu1241 [?].
- **bax** (Bamun): declares 7 phonemes it never emits and emits 118 it never declares. Chain: inherits=x-clade-atla1278 [?].
- **mag** (Magahi): declares 30 phonemes it never emits and emits 89 it never declares. Chain: inherits=x-clade-indo1321 [Indo-European > Indo-Iranian], graphemes_base=hi [Indo-European > Indo-Iranian > Indo-Aryan], allophones_base=hi [Indo-European > Indo-Iranian > Indo-Aryan].
- **lbe** (Lak): declares 94 phonemes it never emits and emits 23 it never declares. Chain: inherits=x-clade-nakh1245 [?].
- **kbd** (Kabardian): declares 85 phonemes it never emits and emits 18 it never declares. Chain: inherits=x-clade-abkh1242 [?].
- **bfj** (Bafanji): declares 30 phonemes it never emits and emits 70 it never declares. Chain: inherits=x-clade-atla1278 [?].
- **udm** (Udmurt): declares 37 phonemes it never emits and emits 58 it never declares. Chain: inherits=x-clade-ural1272 [?].
- **lez** (Lezgian): declares 80 phonemes it never emits and emits 14 it never declares. Chain: inherits=x-clade-nakh1245 [?].
- **new** (Newar): declares 20 phonemes it never emits and emits 73 it never declares. Chain: inherits=x-clade-sino1245 [?], graphemes_base=hi [Indo-European > Indo-Iranian > Indo-Aryan] CROSS-FAMILY.
- **yuc** (Yuchi): declares 34 phonemes it never emits and emits 46 it never declares. Chain: (standalone).
- **skr** (Saraiki): declares 56 phonemes it never emits and emits 22 it never declares. Chain: inherits=x-clade-indo1321 [Indo-European > Indo-Iranian].
- **nb** (Norwegian Bokmål): declares 22 phonemes it never emits and emits 54 it never declares. Chain: inherits=no [Indo-European > Germanic > Northwest Germanic > North Germanic], graphemes_base=no [Indo-European > Germanic > Northwest Germanic > North Germanic], allophones_base=no [Indo-European > Germanic > Northwest Germanic > North Germanic].
- **inh** (Ingush): declares 53 phonemes it never emits and emits 22 it never declares. Chain: inherits=x-clade-nakh1245 [?].
- **tsb** (Tsamai): declares 47 phonemes it never emits and emits 27 it never declares. Chain: inherits=x-clade-afro1255 [?].
- **sje** (Pite Sami): declares 15 phonemes it never emits and emits 58 it never declares. Chain: inherits=x-clade-ural1272 [?].
- **bot** (Bongo): declares 6 phonemes it never emits and emits 66 it never declares. Chain: inherits=x-clade-cent2225 [?].
- **dsq** (Tadaksahak): declares 64 phonemes it never emits and emits 7 it never declares. Chain: inherits=x-clade-song1307 [?].
- **hig** (Kamwe): declares 7 phonemes it never emits and emits 64 it never declares. Chain: inherits=x-clade-afro1255 [?].
- **dim** (Dime): declares 64 phonemes it never emits and emits 6 it never declares. Chain: inherits=x-clade-sout2845 [?].

## Full table

Every spec that is scored on the board, plus any spec flagged by a signal above. Specs with neither a gold nor a flag carry no evidence either way and are left to the JSON output. `gold chars` and `unmapped` here are the union across every gold dataset the spec is scored on. Use the per-dataset sections above before prioritising a row off this table.

code | family | own graphemes | gold chars (union) | unmapped (union) | words hit (union) | stress | cross-family | twin | rows | n | per
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
ja | Japonic | 305 | 1825 | 1669 | 70.4% | no | 0 |  | 2 | 158050 | 0.4273
en-GB | Indo-European > Germanic > Northwest Germanic > West Germanic | 84 | 57 | 31 | 3.3% | yes | 0 | enm-x-yola 0.333 | 3 | 158101 | 0.2959
cy | Indo-European > Celtic > Brythonic | 40 | 49 | 21 | 7.4% | no | 0 | wlm 0.6 | 3 | 38123 | 0.2985
ab | Abkhaz-Adyge | 67 | 62 | 20 | 1.0% | no | 0 | uby 0.4 | 2 | 32345 | 0.2311
nb | Indo-European > Germanic > Northwest Germanic > North Germanic | 37 | 45 | 16 | 0.7% | yes | 0 | nn 0.405 | 3 | 16070 | 0.3569
wbk | Indo-European > Indo-Iranian | 41 | 48 | 15 | 46.1% | no | 0 | pal 0.634 | 1 | 153 | 0.2022
yo | Atlantic-Congo | 56 | 49 | 13 | 1.6% | no | 0 | fpe 0.357 | 2 | 9328 | 0.6392
en-US | Indo-European > Germanic > Northwest Germanic > West Germanic | 7 | 38 | 12 | 5.7% | yes | 0 |  | 4 | 290136 | 0.3515
ess | Eskimo-Aleut | 29 | 36 | 12 | 27.4% | no | 0 | ckt 0.483 | 1 | 814 | 0.1074
fi | Uralic > Finnic | 62 | 38 | 12 | 0.5% | yes | 0 | ang 0.468 | 3 | 274968 | 0.0609
kok | Indo-European > Indo-Iranian > Indo-Aryan | 76 | 65 | 12 | 0.4% | no | 0 | kru 0.684 | 1 | 830 | 0.2241
kw | Indo-European > Celtic > Brythonic | 31 | 35 | 12 | 4.2% | no | 0 | hag 0.645 | 1 | 602 | 0.2521
li | Indo-European > Germanic | 120 | 41 | 12 | 33.6% | yes | 0 | nl-NL 0.283 | 1 | 987 | 0.3099
eu | Vasconic | 35 | 33 | 11 | 1.9% | yes | 0 | lad 0.6 | 5 | 82531 | 0.0984
my | Sino-Tibetan | 231 | 59 | 11 | 2.9% | no | 0 |  | 1 | 7941 | 0.1926
nl-NL | Indo-European > Germanic > Northwest Germanic > West Germanic | 66 | 43 | 11 | 0.7% | yes | 0 | af 0.515 | 4 | 197753 | 0.3817
lad | Indo-European > Italic > Romance > Ibero-Romance | 35 | 33 | 10 | 13.3% | no | 0 | aot 0.686 | 2 | 151 | 0.1397
smn | Uralic | 31 | 41 | 10 | 27.5% | no | 0 | se 0.806 | 1 | 1055 | 0.16
chb | Chibchan | 22 | 28 | 9 | 19.0% | no | 0 | gem-x-ingvaeon 0.545 | 1 | 99 | 0.1313
et | Uralic > Finnic | 27 | 36 | 9 | 1.0% | yes | 0 | vro 0.857 | 3 | 48943 | 0.2769
fa | Indo-European > Indo-Iranian > Iranian | 47 | 56 | 9 | 0.4% | no | 0 | lrc 0.702 | 2 | 16974 | 0.3943
gwd | Afro-Asiatic | 33 | 34 | 9 | 9.9% | no | 0 | ssn 0.794 | 1 | 976 | 0.0385
lou | Indo-European > Italic > Romance | 36 | 37 | 9 | 12.2% | no | 0 | mfe 0.778 | 1 | 262 | 0.1953
mt | Afro-Asiatic > Semitic > Central Semitic | 30 | 37 | 9 | 5.3% | no | 0 | mzs 0.633 | 2 | 24235 | 0.3056
nhx | Uto-Aztecan | 26 | 29 | 9 | 75.3% | no | 0 | nhn 0.7 | 1 | 145 | 0.1852
nn | Indo-European > Germanic > Northwest Germanic > North Germanic | 42 | 38 | 9 | 0.5% | yes | 0 | nap 0.548 | 2 | 4922 | 0.2596
shn | Tai-Kadai | 36 | 41 | 9 | 61.9% | no | 0 |  | 1 | 2604 | 0.2985
bbl | Nakh-Daghestanian | 42 | 43 | 8 | 21.1% | yes | 0 | lzz 0.81 | 1 | 414 | 0.279
cic | Muskogean | 22 | 25 | 8 | 48.7% | yes | 0 | cho 0.714 | 1 | 394 | 0.1028
ckt | Chukotko-Kamchatkan | 26 | 31 | 8 | 13.9% | no | 0 | ess 0.483 | 1 | 993 | 0.0972
fy | Indo-European > Germanic > Northwest Germanic > West Germanic | 57 | 37 | 8 | 0.4% | yes | 0 | frr 0.526 | 2 | 11772 | 0.3243
haw | Austronesian > Malayo-Polynesian | 18 | 26 | 8 | 3.5% | no | 0 | mi 0.8 | 1 | 2145 | 0.0127
hil | Austronesian > Malayo-Polynesian | 20 | 27 | 8 | 4.9% | no | 0 | pam 0.952 | 1 | 466 | 0.0966
irk | Afro-Asiatic | 46 | 32 | 8 | 25.0% | no | 0 | bas 0.609 | 1 | 1117 | 0.1898
kaw | Austronesian | 31 | 36 | 8 | 33.4% | no | 0 | ban 0.742 | 1 | 924 | 0.1472
lut | Salishan | 30 | 35 | 8 | 45.0% | yes | 0 | dzd 0.581 | 1 | 135 | 0.2259
nhg | Uto-Aztecan | 24 | 25 | 8 | 76.7% | no | 0 | nhx 0.692 | 1 | 295 | 0.2367
ps | Indo-European > Indo-Iranian > Iranian | 49 | 54 | 8 | 1.9% | no | 0 | bal 0.612 | 1 | 1075 | 0.2453
quz | Quechuan | 33 | 27 | 8 | 13.2% | no | 0 | aot 0.667 | 1 | 1853 | 0.3549
scn | Indo-European > Italic > Romance > Italo-Romance | 48 | 35 | 8 | 7.8% | no | 0 | it-IT-x-calabria 0.878 | 1 | 1396 | 0.1944
arn | Araucanian | 27 | 30 | 7 | 4.3% | no | 0 | wes 0.741 | 1 | 1269 | 0.0112
bcl | Austronesian > Malayo-Polynesian | 28 | 28 | 7 | 0.9% | no | 0 | min 0.774 | 1 | 4793 | 0.0652
car | Cariban | 30 | 36 | 7 | 31.6% | yes | 0 | bcl 0.633 | 2 | 1423 | 0.3116
ceb | Austronesian > Malayo-Polynesian | 23 | 27 | 7 | 7.2% | no | 0 | ilo 0.913 | 1 | 3895 | 0.1058
fr-FR | Indo-European > Italic > Romance > Gallo-Romance | 98 | 46 | 7 | 4.3% | no | 0 | nrf 0.592 | 2 | 255164 | 0.0848
hi | Indo-European > Indo-Iranian > Indo-Aryan | 72 | 66 | 7 | 1.2% | no | 0 | bho 0.722 | 2 | 42854 | 0.2759
ilo | Austronesian > Malayo-Polynesian | 23 | 27 | 7 | 6.4% | no | 0 | ceb 0.913 | 1 | 931 | 0.1272
kab | Afro-Asiatic > Berber | 65 | 42 | 7 | 2.2% | no | 0 | ber 0.523 | 1 | 54545 | 0.2071
klj | Turkic | 33 | 39 | 7 | 47.7% | yes | 0 | az 0.909 | 1 | 155 | 0.2995
ktz | Kxa | 81 | 30 | 7 | 10.4% | no | 0 | ngh 0.472 | 1 | 134 | 0.3464
nap | Indo-European > Italic > Romance > Italo-Romance | 42 | 28 | 7 | 7.8% | no | 0 | it-IT-x-abruzzo 0.854 | 1 | 198 | 0.2792
orv | Indo-European > Balto-Slavic > Slavic | 38 | 38 | 7 | 12.5% | no | 0 | rue 0.737 | 1 | 609 | 0.2203
rgn | Indo-European > Italic > Romance | 39 | 40 | 7 | 16.9% | no | 0 | vec 0.707 | 1 | 261 | 0.327
sdc | Indo-European > Italic > Romance | 31 | 29 | 7 | 24.7% | no | 0 | lld 0.774 | 1 | 321 | 0.1865
sq | Indo-European > Albanian | 36 | 34 | 7 | 0.2% | no | 0 | io 0.611 | 2 | 16613 | 0.1432
srn | English Creole | 31 | 29 | 7 | 3.2% | no | 0 | bcl 0.71 | 1 | 702 | 0.045
sv | Indo-European > Germanic > Northwest Germanic > North Germanic | 61 | 36 | 7 | 0.3% | yes | 0 | da 0.635 | 4 | 50864 | 0.3658
tk | Turkic | 31 | 37 | 7 | 1.1% | yes | 0 | gag 0.645 | 2 | 6305 | 0.2316
yrk | Uralic | 44 | 44 | 7 | 4.4% | yes | 0 | evn 0.682 | 2 | 1311 | 0.35
cri | Indo-European > Italic > Romance > Ibero-Romance | 35 | 24 | 6 | 46.2% | no | 0 | aoa 0.722 | 1 | 13 | 0.2147
ddo | Nakh-Daghestanian | 41 | 32 | 6 | 19.5% | no | 0 | itl 0.366 | 1 | 871 | 0.109
dlm | Indo-European > Italic > Romance | 32 | 27 | 6 | 13.9% | no | 0 | lld 0.781 | 1 | 180 | 0.2476
es-ES | Indo-European > Italic > Romance > Ibero-Romance | 61 | 39 | 6 | 0.2% | yes | 0 | ast 0.75 | 4 | 609112 | 0.0871
gl-ES | Indo-European > Italic > Romance > Ibero-Romance | 86 | 36 | 6 | 0.7% | yes | 0 | fax 0.535 | 3 | 55623 | 0.0986
hr | Indo-European > Balto-Slavic > Slavic > South Slavic | 30 | 33 | 6 | 0.2% | no | 0 | sl 0.875 | 2 | 31238 | 0.3
is | Indo-European > Germanic > Northwest Germanic > North Germanic | 53 | 38 | 6 | 3.1% | yes | 0 | ofs 0.34 | 3 | 74841 | 0.3397
itl | Chukotko-Kamchatkan | 41 | 42 | 6 | 16.9% | no | 0 | ess 0.439 | 1 | 603 | 0.054
kl | Eskimo-Aleut | 25 | 27 | 6 | 0.5% | no | 0 | bi 0.72 | 1 | 1580 | 0.1765
lmy | Austronesian > Malayo-Polynesian | 22 | 24 | 6 | 19.3% | no | 0 | iba 0.957 | 1 | 129 | 0.1695
mr | Indo-European > Indo-Iranian > Indo-Aryan | 79 | 70 | 6 | 0.1% | no | 0 | kok 0.696 | 2 | 21205 | 0.3064
pag | Austronesian > Malayo-Polynesian | 25 | 26 | 6 | 16.6% | no | 0 | ceb 0.88 | 1 | 227 | 0.1277
pam | Austronesian > Malayo-Polynesian | 21 | 25 | 6 | 3.8% | no | 0 | hil 0.952 | 1 | 860 | 0.2861
pox | Indo-European > Balto-Slavic > Slavic > West Slavic | 46 | 46 | 6 | 40.5% | no | 0 | dsb 0.63 | 1 | 314 | 0.2538
ppl | Uto-Aztecan | 18 | 20 | 6 | 18.7% | no | 0 | quy 0.722 | 1 | 185 | 0.1322
si | Indo-European > Indo-Iranian > Indo-Aryan | 68 | 69 | 6 | 2.5% | no | 0 |  | 1 | 386 | 0.1394
su | Austronesian > Malayo-Polynesian | 27 | 29 | 6 | 0.5% | no | 0 | kge 0.893 | 1 | 399 | 0.0978
ast | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 64 | 40 | 5 | 0.2% | yes | 0 | es-ES 0.75 | 2 | 4189 | 0.0696
bdq | Austroasiatic | 44 | 35 | 5 | 27.3% | yes | 0 | ts 0.477 | 1 | 198 | 0.3355
bjb | Pama-Nyungan | 26 | 17 | 5 | 2.2% | no | 0 | kld 0.615 | 1 | 136 | 0.1021
bo | Sino-Tibetan | 146 | 57 | 5 | 0.2% | no | 0 | dz 0.479 | 1 | 1564 | 0.386
de-x-alemanni | Indo-European > Germanic > Northwest Germanic > West Germanic | 34 | 33 | 5 | 2.1% | yes | 0 | gwr 0.324 | 1 | 448 | 0.1736
es-419 | Indo-European > Italic > Romance > Ibero-Romance | 3 | 39 | 5 | 0.2% | yes | 0 |  | 2 | 132208 | 0.0778
fa-x-enp | Indo-European > Indo-Iranian > Iranian | 11 | 44 | 5 | 0.4% | no | 0 | ps 0.122 | 1 | 9279 | 0.2381
ga | Indo-European > Celtic > Goidelic | 45 | 28 | 5 | 1.0% | yes | 0 | gd 0.333 | 2 | 11227 | 0.2989
hu | Uralic | 60 | 36 | 5 | 1.2% | yes | 0 | non 0.55 | 2 | 79325 | 0.0996
id | Austronesian | 32 | 30 | 5 | 0.2% | yes | 0 | min 0.906 | 3 | 41129 | 0.1312
it-IT | Indo-European > Italic > Romance > Italo-Romance | 71 | 37 | 5 | 2.6% | yes | 0 | co 0.634 | 1 | 4583 | 0.2353
lb | Indo-European > Germanic > Northwest Germanic > West Germanic | 50 | 35 | 5 | 0.5% | no | 0 | fue 0.46 | 1 | 3893 | 0.2412
liv | Uralic | 40 | 44 | 5 | 13.4% | yes | 0 | sgs 0.625 | 2 | 3522 | 0.1173
lmo | Indo-European > Italic > Romance > Italo-Romance | 29 | 41 | 5 | 4.9% | no | 0 | egl 0.483 | 1 | 406 | 0.2892
mak | Austronesian | 26 | 28 | 5 | 6.6% | yes | 0 | gor 0.962 | 1 | 832 | 0.0194
nci | Uto-Aztecan | 0 | 25 | 5 | 0.8% | no | 0 |  | 1 | 839 | 0.1198
non | Indo-European > Germanic > Northwest Germanic > North Germanic | 51 | 39 | 5 | 3.5% | no | 0 | ofs 0.667 | 1 | 270 | 0.2365
pa | Indo-European > Indo-Iranian > Indo-Aryan | 60 | 58 | 5 | 0.2% | no | 0 |  | 2 | 5363 | 0.4304
pl | Indo-European > Balto-Slavic > Slavic > West Slavic | 44 | 37 | 5 | 0.1% | yes | 0 | szl 0.705 | 3 | 212105 | 0.2465
sga | Indo-European > Celtic | 49 | 28 | 5 | 0.3% | yes | 0 | mga 0.731 | 1 | 3700 | 0.0888
sjd | Uralic > Saami | 56 | 49 | 5 | 0.4% | yes | 0 | sia 0.714 | 2 | 1767 | 0.2298
sl | Indo-European > Balto-Slavic > Slavic > South Slavic | 32 | 30 | 5 | 0.1% | no | 0 | hr 0.875 | 2 | 11742 | 0.3451
slr | Turkic | 32 | 35 | 5 | 31.6% | yes | 0 | klj 0.909 | 1 | 752 | 0.285
sw | Atlantic-Congo > Bantu | 36 | 28 | 5 | 0.5% | yes | 0 | ksb 0.611 | 3 | 96949 | 0.2539
ur | Indo-European > Indo-Iranian > Indo-Aryan | 62 | 47 | 5 | 0.4% | no | 0 | pnb-PK 0.629 | 1 | 6296 | 0.3077
uz | Turkic | 30 | 30 | 5 | 0.2% | yes | 0 | wes 0.833 | 2 | 78228 | 0.2458
aa | Afro-Asiatic > Cushitic | 31 | 26 | 4 | 0.3% | no | 0 | hay 0.774 | 1 | 1713 | 0.2151
acw-SA | Afro-Asiatic > Semitic > Central Semitic | 54 | 45 | 4 | 0.6% | yes | 0 | ar-x-maghrebi 0.741 | 4 | 1959 | 0.2877
ckb | Indo-European > Indo-Iranian > Iranian | 35 | 38 | 4 | 0.3% | no | 0 | sdh 0.8 | 2 | 27112 | 0.2607
de-DE | Indo-European > Germanic > Northwest Germanic > West Germanic | 61 | 34 | 4 | 1.3% | yes | 0 | nds 0.736 | 2 | 802642 | 0.3948
fo | Indo-European > Germanic > Northwest Germanic > North Germanic | 62 | 33 | 4 | 0.1% | yes | 0 | frr 0.274 | 1 | 2957 | 0.1674
gu | Indo-European > Indo-Iranian > Indo-Aryan | 61 | 62 | 4 | 0.3% | no | 0 |  | 1 | 4082 | 0.1842
ht | French Creole | 31 | 29 | 4 | 0.5% | no | 0 | crs 0.806 | 1 | 1691 | 0.0302
hy | Indo-European > Armenic | 39 | 42 | 4 | 0.8% | no | 0 | hyw 0.65 | 2 | 44405 | 0.1027
jam | English Creole | 36 | 27 | 4 | 4.2% | no | 0 | rhg 0.778 | 2 | 2251 | 0.2762
ket | Yeniseian | 45 | 35 | 4 | 16.8% | no | 0 | gld 0.422 | 1 | 793 | 0.2688
ku | Indo-European > Indo-Iranian > Iranian | 31 | 35 | 4 | 0.3% | no | 0 | diq 0.735 | 1 | 2147 | 0.144
mh | Austronesian | 41 | 27 | 4 | 0.8% | no | 0 | aks 0.146 | 1 | 947 | 0.1182
ms | Austronesian | 0 | 29 | 4 | 6.0% | yes | 0 |  | 2 | 33102 | 0.1305
pms | Indo-European > Italic > Romance > Italo-Romance | 19 | 30 | 4 | 37.6% | no | 0 | egl 0.474 | 1 | 899 | 0.1652
ru | Indo-European > Balto-Slavic > Slavic > East Slavic | 36 | 37 | 4 | 0.2% | yes | 0 | myv 0.694 | 5 | 470125 | 0.3573
sc | Indo-European > Italic > Romance > Southern Romance | 43 | 31 | 4 | 1.5% | no | 0 | vec 0.698 | 1 | 703 | 0.063
sjs | Afro-Asiatic > Berber | 34 | 37 | 4 | 3.9% | no | 0 | shy 0.882 | 1 | 845 | 0.0467
sk | Indo-European > Balto-Slavic > Slavic > West Slavic | 61 | 47 | 4 | 0.2% | yes | 0 | dsb 0.443 | 2 | 31837 | 0.1346
tl | Austronesian | 27 | 30 | 4 | 2.3% | no | 0 | ban 0.786 | 1 | 25857 | 0.1179
tn | Atlantic-Congo > Bantu | 40 | 25 | 4 | 1.0% | no | 0 | nso 0.55 | 1 | 2271 | 0.3953
tr | Turkic | 29 | 34 | 4 | 0.6% | yes | 0 | gag 0.839 | 3 | 61340 | 0.1372
wa | Indo-European > Italic > Romance | 54 | 39 | 4 | 0.3% | no | 0 | pcd 0.556 | 1 | 2348 | 0.1443
yi | Indo-European > Germanic > Northwest Germanic > West Germanic | 50 | 39 | 4 | 8.4% | yes | 0 | he 0.197 | 1 | 4051 | 0.2042
ace | Austronesian | 29 | 28 | 3 | 29.4% | no | 0 | mad 0.733 | 1 | 267 | 0.1102
ady | Abkhaz-Adyge | 64 | 34 | 3 | 50.3% | no | 0 | kbd 0.812 | 1 | 928 | 0.1684
am | Afro-Asiatic > Semitic | 286 | 234 | 3 | 8.7% | no | 0 | ti 0.535 | 2 | 5841 | 0.3296
ar | Afro-Asiatic > Semitic > Central Semitic | 16 | 48 | 3 | 0.1% | yes | 0 | acx-OM 0.294 | 5 | 885708 | 0.3774
as | Indo-European > Indo-Iranian > Indo-Aryan | 64 | 64 | 3 | 1.9% | no | 0 | ctg 0.375 | 2 | 8309 | 0.2451
ast-ES-x-leon | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 4 | 33 | 3 | 25.0% | yes | 0 |  | 1 | 20 | 0.0503
ast-x-cantabri | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 2 | 30 | 3 | 30.0% | yes | 0 |  | 1 | 20 | 0.0118
ast-x-pasiego | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 2 | 31 | 3 | 15.0% | yes | 0 |  | 1 | 20 | 0.1364
bn | Indo-European > Indo-Iranian > Indo-Aryan | 61 | 61 | 3 | 0.0% | no | 0 | as 0.625 | 2 | 36788 | 0.2398
ca-x-balear | Indo-European > Italic > Romance | 3 | 40 | 3 | 1.7% | yes | 0 |  | 2 | 180 | 0.136
ce | Nakh-Daghestanian | 43 | 30 | 3 | 7.3% | no | 0 | kum 0.674 | 1 | 461 | 0.2541
cop | Afro-Asiatic > Egyptian | 34 | 33 | 3 | 3.5% | no | 0 |  | 1 | 591 | 0.3667
gld | Tungusic | 36 | 33 | 3 | 21.8% | no | 0 | itl 0.439 | 1 | 887 | 0.1532
grc | Indo-European > Hellenic | 60 | 60 | 3 | 0.8% | no | 0 | el-CY 0.212 | 1 | 58093 | 0.1456
ha | Afro-Asiatic > Chadic | 53 | 33 | 3 | 0.5% | no | 0 | anc 0.509 | 2 | 5576 | 0.534
km | Austroasiatic | 374 | 74 | 3 | 0.4% | yes | 0 |  | 2 | 9889 | 0.3335
kv | Uralic | 74 | 37 | 3 | 0.5% | no | 0 | koi 1.0 | 1 | 906 | 0.157
ky | Turkic | 34 | 36 | 3 | 11.6% | yes | 0 | alt 0.829 | 2 | 11478 | 0.2217
lg | Atlantic-Congo > Bantu | 32 | 27 | 3 | 13.6% | no | 0 | gog 0.875 | 1 | 103344 | 0.1107
lij | Indo-European > Italic > Romance > Italo-Romance | 96 | 46 | 3 | 0.2% | yes | 0 | nrf 0.406 | 2 | 4233 | 0.1157
lt | Indo-European > Balto-Slavic > Eastern Baltic | 41 | 35 | 3 | 0.1% | no | 0 | ltg 0.585 | 2 | 29411 | 0.2706
ml | Dravidian | 72 | 74 | 3 | 0.4% | no | 0 |  | 2 | 15928 | 0.2623
ngh | Tuu | 89 | 35 | 3 | 1.2% | no | 0 | ktz 0.472 | 1 | 263 | 0.2616
niv | Nivkh | 57 | 44 | 3 | 0.8% | no | 0 | sjd 0.614 | 2 | 1457 | 0.2246
ny | Atlantic-Congo > Bantu | 64 | 28 | 3 | 0.5% | no | 0 | zu 0.485 | 1 | 1564 | 0.3119
or | Indo-European > Indo-Iranian > Indo-Aryan | 62 | 63 | 3 | 0.2% | no | 0 |  | 2 | 14134 | 0.2694
osp | Indo-European > Italic > Romance | 32 | 29 | 3 | 0.6% | yes | 0 | nov 0.688 | 1 | 667 | 0.1605
pt-PT | Indo-European > Italic > Romance > Ibero-Romance | 31 | 42 | 3 | 0.1% | yes | 0 | ast-PT-x-rionor 0.308 | 6 | 271962 | 0.2288
ro-RO | Indo-European > Italic > Romance > Eastern Romance | 41 | 34 | 3 | 6.1% | yes | 0 | rup 0.634 | 2 | 74686 | 0.2644
sr | Indo-European > Balto-Slavic > Slavic > South Slavic | 60 | 60 | 3 | 0.1% | no | 0 | mk 0.467 | 2 | 13462 | 0.3298
te | Dravidian | 63 | 66 | 3 | 0.9% | no | 0 |  | 1 | 5101 | 0.099
tg | Indo-European > Indo-Iranian > Iranian | 36 | 38 | 3 | 0.5% | no | 0 | alt 0.778 | 1 | 3245 | 0.0296
ulw | Misumalpan | 20 | 20 | 3 | 17.5% | yes | 0 | mdh 0.85 | 1 | 102 | 0.0888
vi | Austroasiatic | 891 | 89 | 3 | 0.1% | no | 0 | mtq 0.024 | 3 | 75849 | 0.5596
wau | Arawakan | 24 | 19 | 3 | 37.7% | no | 0 | ulw 0.625 | 1 | 146 | 0.2968
yux | Yukaghir | 35 | 27 | 3 | 11.8% | no | 0 | myv 0.771 | 1 | 242 | 0.2711
zza | Indo-European > Indo-Iranian > Iranian | 37 | 34 | 3 | 0.9% | no | 0 | klj 0.73 | 1 | 196 | 0.2464
acm-IQ | Afro-Asiatic > Semitic > Central Semitic | 37 | 40 | 2 | 30.8% | yes | 0 | aeb-TN 0.865 | 3 | 52 | 0.2907
acx-OM | Afro-Asiatic > Semitic > Central Semitic | 34 | 38 | 2 | 45.0% | yes | 0 | shu-TD 0.639 | 2 | 40 | 0.1448
aeb-TN | Afro-Asiatic > Semitic > Central Semitic | 36 | 37 | 2 | 49.0% | yes | 0 | acm-IQ 0.865 | 3 | 49 | 0.3059
afb | Afro-Asiatic > Semitic > Central Semitic | 52 | 43 | 2 | 1.7% | yes | 0 | mey-MR 0.654 | 3 | 654 | 0.3786
afb-AE | Afro-Asiatic > Semitic > Central Semitic | 0 | 40 | 2 | 50.0% | yes | 0 |  | 2 | 40 | 0.0765
afb-BH | Afro-Asiatic > Semitic > Central Semitic | 0 | 40 | 2 | 45.0% | yes | 0 |  | 2 | 40 | 0.1147
afb-KW | Afro-Asiatic > Semitic > Central Semitic | 0 | 40 | 2 | 30.0% | yes | 0 |  | 2 | 40 | 0.0912
afb-QA | Afro-Asiatic > Semitic > Central Semitic | 0 | 39 | 2 | 25.0% | yes | 0 |  | 2 | 40 | 0.1227
afb-SA-x-sharqiya | Afro-Asiatic > Semitic > Central Semitic | 1 | 38 | 2 | 34.8% | yes | 0 |  | 3 | 46 | 0.1944
an | Indo-European > Italic > Romance > Ibero-Romance | 58 | 32 | 2 | 0.5% | yes | 0 | es-ES-x-medieval 0.81 | 2 | 922 | 0.058
ang | Indo-European > Germanic > Northwest Germanic > West Germanic | 55 | 26 | 2 | 1.6% | no | 0 | ofs 0.745 | 1 | 54696 | 0.2103
apc | Afro-Asiatic > Semitic > Central Semitic | 38 | 37 | 2 | 35.0% | yes | 0 | ar-LY 0.868 | 2 | 40 | 0.0978
apc-JO | Afro-Asiatic > Semitic > Central Semitic | 8 | 46 | 2 | 0.7% | yes | 0 | arz-EG 0.182 | 4 | 2566 | 0.3451
apc-LB | Afro-Asiatic > Semitic > Central Semitic | 72 | 36 | 2 | 30.0% | yes | 0 | ar-LY 0.028 | 2 | 40 | 0.1062
apc-PS | Afro-Asiatic > Semitic > Central Semitic | 3 | 39 | 2 | 31.8% | yes | 0 |  | 3 | 44 | 0.1667
apc-SY | Afro-Asiatic > Semitic > Central Semitic | 17 | 48 | 2 | 2.4% | yes | 0 | arz-EG 0.273 | 4 | 461 | 0.3173
apd-SD | Afro-Asiatic > Semitic > Central Semitic | 26 | 37 | 2 | 55.0% | yes | 0 | arz-EG 0.667 | 2 | 40 | 0.1069
ar-IQ-x-qeltu | Afro-Asiatic > Semitic > Central Semitic | 1 | 38 | 2 | 23.1% | yes | 0 |  | 3 | 52 | 0.3417
ar-LY | Afro-Asiatic > Semitic > Central Semitic | 37 | 35 | 2 | 39.1% | yes | 0 | apc 0.868 | 3 | 46 | 0.2042
ar-SA-x-rijal-alma | Afro-Asiatic > Semitic > Central Semitic | 21 | 40 | 2 | 29.2% | yes | 0 | apc-JO 0.048 | 3 | 48 | 0.2454
ar-x-maghrebi | Afro-Asiatic > Semitic > Central Semitic | 45 | 36 | 2 | 35.0% | yes | 0 | acw-SA 0.741 | 2 | 40 | 0.1832
ar-x-mashriqi | Afro-Asiatic > Semitic > Central Semitic | 43 | 39 | 2 | 35.0% | yes | 0 | acw-SA 0.741 | 2 | 40 | 0.0568
ar-x-peninsul | Afro-Asiatic > Semitic > Central Semitic | 42 | 40 | 2 | 35.0% | yes | 0 | acx-OM 0.786 | 2 | 40 | 0.0405
arb | Afro-Asiatic > Semitic > Central Semitic | 245 | 45 | 2 | 25.0% | yes | 0 | ayl 0.849 | 2 | 40 | 0.0688
arq-DZ | Afro-Asiatic > Semitic > Central Semitic | 25 | 40 | 2 | 29.3% | yes | 0 | shu-NG 0.606 | 3 | 41 | 0.7143
ars-SA | Afro-Asiatic > Semitic > Central Semitic | 38 | 40 | 2 | 18.9% | yes | 0 | ayn-YE 0.524 | 3 | 65 | 0.0891
ars-SA-x-qassim | Afro-Asiatic > Semitic > Central Semitic | 3 | 41 | 2 | 26.9% | yes | 0 |  | 3 | 52 | 0.1327
ary-MA | Afro-Asiatic > Semitic > Central Semitic | 17 | 45 | 2 | 0.7% | yes | 0 | apd-SD 0.385 | 4 | 1878 | 0.3005
arz-EG | Afro-Asiatic > Semitic > Central Semitic | 33 | 47 | 2 | 2.1% | yes | 0 | apd-SD 0.667 | 4 | 648 | 0.3237
ast-x-leon | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 34 | 31 | 2 | 15.0% | yes | 0 | roa-x-galaico-pt 0.333 | 1 | 20 | 0.0856
ast-x-occident | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 9 | 32 | 2 | 10.0% | yes | 0 | gl-ES-x-eonavia 0.333 | 1 | 20 | 0.0656
ast-x-oriental | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 0 | 31 | 2 | 15.0% | yes | 0 |  | 1 | 20 | 0.0612
av | Nakh-Daghestanian | 56 | 36 | 2 | 2.5% | no | 0 | lbe 0.786 | 1 | 954 | 0.099
ayn-YE | Afro-Asiatic > Semitic > Central Semitic | 42 | 39 | 2 | 32.7% | yes | 0 | mey-MR 0.891 | 3 | 55 | 0.1802
br | Indo-European > Celtic > Brythonic | 52 | 29 | 2 | 0.3% | yes | 0 | mfe 0.519 | 1 | 803 | 0.3073
ca | Indo-European > Italic > Romance | 4 | 39 | 2 | 0.4% | yes | 0 |  | 5 | 145722 | 0.2565
ca-x-medieval | Indo-European > Italic > Romance | 50 | 30 | 2 | 10.0% | yes | 0 | mxi 0.655 | 1 | 20 | 0.0762
crs | Indo-European > Italic > Romance > Gallo-Romance | 28 | 24 | 2 | 0.2% | no | 0 | nga 0.828 | 1 | 1874 | 0.2114
da | Indo-European > Germanic > Northwest Germanic > North Germanic | 63 | 31 | 2 | 0.4% | yes | 0 | sv 0.635 | 2 | 6564 | 0.4476
dar | Nakh-Daghestanian | 53 | 34 | 2 | 5.8% | no | 0 | av 0.714 | 1 | 1056 | 0.0691
enf | Uralic | 57 | 34 | 2 | 0.5% | no | 0 | sel 0.702 | 1 | 838 | 0.0892
es-CL | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 2 | 15.0% | yes | 0 |  | 1 | 20 | 0.0176
es-PE-x-andino | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 2 | 20.0% | yes | 0 |  | 1 | 20 | 0.1037
evn | Tungusic | 39 | 36 | 2 | 4.5% | yes | 0 | yux 0.744 | 2 | 1277 | 0.2447
fax | Indo-European > Italic > Romance > Ibero-Romance | 58 | 33 | 2 | 1.2% | no | 0 | es-ES-x-medieval 0.776 | 2 | 675 | 0.0932
gul | Indo-European > Germanic > Northwest Germanic > West Germanic | 33 | 25 | 2 | 4.9% | no | 0 | aot 0.727 | 1 | 207 | 0.3341
hsb | Indo-European > Balto-Slavic > Slavic > West Slavic | 36 | 35 | 2 | 0.0% | yes | 0 | dsb 0.919 | 2 | 6928 | 0.3177
iba | Austronesian > Malayo-Polynesian | 23 | 23 | 2 | 1.4% | no | 0 | lmy 0.957 | 1 | 571 | 0.1655
kld | Pama-Nyungan | 21 | 15 | 2 | 2.1% | yes | 0 | ulw 0.667 | 1 | 515 | 0.055
kn | Dravidian | 64 | 66 | 2 | 0.1% | no | 0 |  | 1 | 1706 | 0.0161
lbe | Nakh-Daghestanian | 53 | 33 | 2 | 0.6% | no | 0 | av 0.786 | 1 | 1048 | 0.0387
lez | Nakh-Daghestanian | 43 | 32 | 2 | 1.8% | no | 0 | dar 0.698 | 1 | 969 | 0.1329
lv | Indo-European > Balto-Slavic > Eastern Baltic | 33 | 34 | 2 | 0.2% | yes | 0 | sgs 0.788 | 1 | 1213 | 0.1901
lzz | Kartvelian | 34 | 35 | 2 | 10.5% | no | 0 | ka 0.941 | 1 | 262 | 0.2017
mey-MR | Afro-Asiatic > Semitic > Central Semitic | 46 | 37 | 2 | 27.6% | yes | 0 | ayn-YE 0.891 | 3 | 54 | 0.3988
mfe | Indo-European > Italic > Romance | 30 | 26 | 2 | 0.9% | no | 0 | ht 0.806 | 1 | 206 | 0.1238
mxi | Indo-European > Italic > Romance | 55 | 30 | 2 | 25.0% | yes | 0 | es-ES-x-medieval 0.673 | 1 | 20 | 0.0432
nio | Uralic | 55 | 30 | 2 | 6.8% | no | 0 | enf 0.649 | 1 | 1024 | 0.0972
nv | Athabaskan-Eyak-Tlingit | 64 | 33 | 2 | 0.9% | no | 0 | xsl 0.356 | 1 | 989 | 0.2514
phl | Indo-European > Indo-Iranian | 55 | 43 | 2 | 0.0% | no | 0 | snk 0.527 | 1 | 2173 | 0.266
pt-BR | Indo-European > Italic > Romance > Ibero-Romance | 32 | 41 | 2 | 0.0% | yes | 0 | ast-PT-x-rionor 0.365 | 9 | 332108 | 0.3951
pt-PT-x-viana | Indo-European > Italic > Romance > Ibero-Romance | 2 | 38 | 2 | 4.2% | yes | 0 |  | 2 | 24 | 0.326
rif | Afro-Asiatic > Berber | 50 | 40 | 2 | 22.8% | no | 0 | zen 0.48 | 1 | 1533 | 0.0929
rw | Atlantic-Congo > Bantu | 35 | 26 | 2 | 7.7% | no | 0 | lua 0.8 | 1 | 381086 | 0.1388
se | Uralic > Saami | 29 | 31 | 2 | 0.3% | no | 0 | smn 0.806 | 1 | 4125 | 0.2749
shu-NG | Afro-Asiatic > Semitic > Central Semitic | 33 | 33 | 2 | 30.4% | yes | 0 | ar-LY 0.838 | 3 | 46 | 0.2444
shu-TD | Afro-Asiatic > Semitic > Central Semitic | 36 | 36 | 2 | 30.0% | yes | 0 | acm-IQ 0.838 | 2 | 40 | 0.1239
vep | Uralic | 28 | 30 | 2 | 10.9% | no | 0 | vro 0.929 | 1 | 1004 | 0.2065
war | Austronesian > Malayo-Polynesian | 21 | 21 | 2 | 1.3% | no | 0 | pam 0.952 | 1 | 380 | 0.1478
ain | Ainu | 28 | 21 | 1 | 0.7% | yes | 0 | bcl 0.679 | 1 | 858 | 0.02
ale | Eskimo-Aleut | 39 | 29 | 1 | 0.4% | no | 0 | ng 0.575 | 2 | 1014 | 0.2634
an-x-ansotano | Indo-European > Italic > Romance > Ibero-Romance | 0 | 30 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0649
an-x-belsetan | Indo-European > Italic > Romance > Ibero-Romance | 2 | 31 | 1 | 25.0% | yes | 0 |  | 1 | 20 | 0.0633
an-x-benasque | Indo-European > Italic > Romance > Ibero-Romance | 7 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.051
an-x-cheso | Indo-European > Italic > Romance > Ibero-Romance | 2 | 30 | 1 | 30.0% | yes | 0 |  | 1 | 20 | 0.052
an-x-chistau | Indo-European > Italic > Romance > Ibero-Romance | 2 | 31 | 1 | 25.0% | yes | 0 |  | 1 | 20 | 0.0555
an-x-occident | Indo-European > Italic > Romance > Ibero-Romance | 0 | 30 | 1 | 35.0% | yes | 0 |  | 1 | 20 | 0.055
an-x-oriental | Indo-European > Italic > Romance > Ibero-Romance | 7 | 30 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0858
an-x-tensino | Indo-European > Italic > Romance > Ibero-Romance | 0 | 30 | 1 | 25.0% | yes | 0 |  | 1 | 20 | 0.0611
apw | Athabaskan-Eyak-Tlingit | 123 | 36 | 1 | 0.7% | no | 0 | xsl 0.398 | 1 | 147 | 0.3076
az | Turkic | 32 | 33 | 1 | 0.4% | yes | 0 | klj 0.909 | 1 | 434 | 0.244
ban | Austronesian | 28 | 22 | 1 | 5.0% | no | 0 | min 0.871 | 1 | 299 | 0.163
bg | Indo-European > Balto-Slavic > Slavic > South Slavic | 37 | 30 | 1 | 0.0% | no | 0 | orv 0.711 | 1 | 18447 | 0.198
bua | Mongolic | 44 | 35 | 1 | 0.6% | yes | 0 | bxr 0.636 | 2 | 1314 | 0.3571
cho | Muskogean | 28 | 22 | 1 | 0.9% | no | 0 | cic 0.714 | 1 | 140 | 0.3381
co | Indo-European > Italic > Romance > Italo-Romance | 48 | 28 | 1 | 0.2% | no | 0 | it-IT-x-abruzzo 0.938 | 1 | 459 | 0.1955
dsb | Indo-European > Balto-Slavic > Slavic > West Slavic | 37 | 35 | 1 | 0.0% | yes | 0 | hsb 0.919 | 1 | 2010 | 0.1487
dum | Indo-European > Germanic > Northwest Germanic > West Germanic | 37 | 24 | 1 | 0.4% | yes | 0 | gml 0.676 | 1 | 197 | 0.2776
el | Indo-European > Hellenic | 90 | 38 | 1 | 0.0% | yes | 0 | pnt 0.765 | 2 | 25091 | 0.2653
eo | Constructed | 28 | 29 | 1 | 0.0% | yes | 0 | ist 0.75 | 2 | 64490 | 0.0328
es-AR | Indo-European > Italic > Romance > Ibero-Romance | 4 | 29 | 1 | 6.1% | yes | 0 |  | 2 | 49 | 0.0648
es-AR-x-cordoba | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 20.0% | yes | 0 |  | 1 | 20 | 0.0207
es-AR-x-cuyo | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0948
es-AR-x-litoral | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0608
es-AR-x-norte | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0721
es-AR-x-patagoni | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.1411
es-BO | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 1 | 5.0% | yes | 0 |  | 1 | 20 | 0.0757
es-BO-x-andino | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 1 | 5.0% | yes | 0 |  | 1 | 20 | 0.0776
es-BO-x-camba | Indo-European > Italic > Romance > Ibero-Romance | 3 | 28 | 1 | 5.0% | yes | 0 |  | 1 | 20 | 0.0512
es-CL-x-andino | Indo-European > Italic > Romance > Ibero-Romance | 3 | 27 | 1 | 5.0% | yes | 0 |  | 1 | 20 | 0.0795
es-CL-x-chilote | Indo-European > Italic > Romance > Ibero-Romance | 3 | 28 | 1 | 5.0% | yes | 0 |  | 1 | 20 | 0.062
es-CO | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 1 | 20.0% | yes | 0 |  | 1 | 20 | 0.012
es-CO-x-costa | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 20.0% | yes | 0 |  | 1 | 20 | 0.0228
es-CO-x-llanero | Indo-European > Italic > Romance > Ibero-Romance | 3 | 28 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0808
es-CO-x-pacifico | Indo-European > Italic > Romance > Ibero-Romance | 3 | 28 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.1524
es-CO-x-paisa | Indo-European > Italic > Romance > Ibero-Romance | 3 | 27 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0291
es-CO-x-santande | Indo-European > Italic > Romance > Ibero-Romance | 3 | 28 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0917
es-CO-x-valluno | Indo-European > Italic > Romance > Ibero-Romance | 3 | 28 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.1163
es-CR | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.146
es-CU | Indo-European > Italic > Romance > Ibero-Romance | 4 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0223
es-DO | Indo-European > Italic > Romance > Ibero-Romance | 4 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0643
es-EC | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0438
es-EC-x-andino | Indo-European > Italic > Romance > Ibero-Romance | 3 | 28 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0343
es-EC-x-costa | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0201
es-GQ | Indo-European > Italic > Romance > Ibero-Romance | 3 | 27 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0743
es-GT | Indo-European > Italic > Romance > Ibero-Romance | 3 | 28 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0797
es-HN | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0829
es-MX | Indo-European > Italic > Romance > Ibero-Romance | 3 | 31 | 1 | 0.1% | yes | 0 |  | 2 | 595905 | 0.0167
es-MX-x-costa | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0214
es-MX-x-norte | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0105
es-MX-x-yucatan | Indo-European > Italic > Romance > Ibero-Romance | 4 | 31 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0092
es-NI | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0189
es-PA | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0986
es-PE | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0866
es-PE-x-amazonia | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0718
es-PE-x-lima | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0102
es-PR | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0684
es-PY | Indo-European > Italic > Romance > Ibero-Romance | 3 | 31 | 1 | 20.0% | yes | 0 |  | 1 | 20 | 0.04
es-SV | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0248
es-UY | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 20.0% | yes | 0 |  | 1 | 20 | 0.066
es-VE | Indo-European > Italic > Romance > Ibero-Romance | 3 | 30 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0305
es-VE-x-andino | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0768
es-VE-x-llanero | Indo-European > Italic > Romance > Ibero-Romance | 3 | 31 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0909
es-VE-x-zulia | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.0622
ext | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 1 | 15.0% | yes | 0 |  | 1 | 20 | 0.048
gd | Indo-European > Celtic > Goidelic | 41 | 26 | 1 | 0.3% | yes | 0 | ga 0.333 | 1 | 3719 | 0.2774
gl-ES-x-reintegr | Indo-European > Italic > Romance > Ibero-Romance | 7 | 26 | 1 | 5.0% | yes | 0 |  | 1 | 20 | 0.1368
huu | Huitotoan | 30 | 25 | 1 | 0.2% | no | 0 | ctd 0.613 | 1 | 437 | 0.035
kca | Uralic | 50 | 34 | 1 | 0.1% | no | 0 | sel 0.691 | 1 | 863 | 0.0232
kix | Sino-Tibetan | 60 | 44 | 1 | 0.1% | no | 0 | ts 0.35 | 1 | 4240 | 0.0788
ko | Koreanic | 118 | 1056 | 1 | 0.0% | no | 0 |  | 2 | 68570 | 0.2319
krl | Uralic > Finnic | 9 | 28 | 1 | 0.2% | yes | 0 | vot 0.538 | 1 | 641 | 0.0519
kwk | Wakashan | 79 | 36 | 1 | 0.9% | no | 0 | irk 0.304 | 1 | 116 | 0.007
kxd | Austronesian > Malayo-Polynesian | 30 | 22 | 1 | 0.3% | no | 0 | min 0.903 | 1 | 318 | 0.0235
lo | Tai-Kadai | 66 | 54 | 1 | 0.1% | no | 0 |  | 1 | 2315 | 0.357
mch | Cariban | 29 | 21 | 1 | 1.8% | no | 0 | cab 0.759 | 1 | 1746 | 0.12
mdf | Uralic | 39 | 33 | 1 | 0.3% | no | 0 | myv 0.744 | 1 | 330 | 0.2112
mdh | Austronesian > Malayo-Polynesian | 20 | 20 | 1 | 1.9% | no | 0 | lmy 0.864 | 1 | 205 | 0.0793
mhr | Uralic > Mari | 72 | 36 | 1 | 85.2% | no | 0 | udm 0.611 | 1 | 992 | 0.1736
mi | Austronesian > Malayo-Polynesian | 20 | 20 | 1 | 0.2% | no | 0 | haw 0.8 | 1 | 1003 | 0.0719
mnc | Tungusic | 29 | 26 | 1 | 0.1% | no | 0 |  | 1 | 1205 | 0.1411
mns | Uralic | 64 | 34 | 1 | 10.7% | yes | 0 | kca 0.609 | 1 | 992 | 0.1024
mrj | Uralic > Mari | 40 | 38 | 1 | 2.4% | no | 0 | alt 0.725 | 1 | 1018 | 0.0075
mwl | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 20 | 34 | 1 | 0.2% | yes | 0 | lfn 0.273 | 3 | 1215 | 0.2289
nmy | Sino-Tibetan | 132 | 59 | 1 | 0.3% | no | 0 | aot 0.159 | 1 | 354 | 0.1091
nrf | Indo-European > Italic > Romance > Gallo-Romance | 92 | 38 | 1 | 2.1% | no | 0 | fr-FR 0.592 | 1 | 143 | 0.2557
pbv | Austroasiatic | 37 | 23 | 1 | 4.0% | no | 0 | aot 0.541 | 1 | 101 | 0.3358
pdc | Indo-European > Germanic | 37 | 24 | 1 | 0.6% | no | 0 | om 0.514 | 1 | 405 | 0.2729
pt-BR-x-caipira | Indo-European > Italic > Romance > Ibero-Romance | 57 | 33 | 1 | 3.9% | yes | 0 | fax 0.741 | 2 | 51 | 0.3331
pt-BR-x-rj | Indo-European > Italic > Romance > Ibero-Romance | 57 | 37 | 1 | 0.0% | yes | 0 | fax 0.759 | 2 | 53163 | 0.1694
pt-BR-x-sp | Indo-European > Italic > Romance > Ibero-Romance | 57 | 37 | 1 | 0.0% | yes | 0 | fax 0.759 | 2 | 53163 | 0.1589
pt-MZ | Indo-European > Italic > Romance > Ibero-Romance | 4 | 37 | 1 | 0.0% | yes | 0 |  | 2 | 53163 | 0.2095
pt-PT-x-lisbon | Indo-European > Italic > Romance > Ibero-Romance | 3 | 39 | 1 | 0.0% | yes | 0 |  | 5 | 53248 | 0.2682
pt-PT-x-minho | Indo-European > Italic > Romance > Ibero-Romance | 4 | 35 | 1 | 6.9% | yes | 0 |  | 2 | 29 | 0.283
pt-PT-x-porto | Indo-European > Italic > Romance > Ibero-Romance | 3 | 40 | 1 | 2.3% | yes | 0 |  | 4 | 82 | 0.3936
pt-TL | Indo-European > Italic > Romance > Ibero-Romance | 6 | 37 | 1 | 0.0% | yes | 0 |  | 2 | 53162 | 0.3632
sa | Indo-European > Indo-Iranian > Indo-Aryan | 68 | 60 | 1 | 0.3% | no | 0 | vsn 0.859 | 1 | 9796 | 0.0161
sah | Turkic | 50 | 32 | 1 | 0.0% | no | 0 | xal 0.68 | 2 | 12227 | 0.2492
sid | Afro-Asiatic > Cushitic | 38 | 27 | 1 | 1.0% | no | 0 | om 0.763 | 1 | 297 | 0.0622
sms | Uralic > Saami | 60 | 39 | 1 | 0.1% | yes | 0 | bs 0.4 | 2 | 1174 | 0.22
srs | Athabaskan-Eyak-Tlingit | 42 | 23 | 1 | 2.9% | no | 0 | fmp 0.548 | 1 | 137 | 0.1765
tzm | Afro-Asiatic > Berber | 34 | 33 | 1 | 0.1% | no | 0 | zgh 0.971 | 1 | 658 | 0.016
ug | Turkic | 34 | 34 | 1 | 0.0% | no | 0 | sdh 0.618 | 2 | 43147 | 0.0864
vo | Constructed | 28 | 29 | 1 | 0.4% | no | 0 | ban 0.786 | 1 | 442 | 0.0185
wlm | Indo-European > Celtic > Brythonic | 30 | 23 | 1 | 0.2% | yes | 0 | ia 0.633 | 1 | 403 | 0.2498
xaa | Afro-Asiatic > Semitic > Central Semitic | 0 | 39 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.1228
xal | Mongolic | 45 | 34 | 1 | 4.4% | no | 0 | sah 0.68 | 1 | 318 | 0.2813
ykg | Yukaghir | 45 | 28 | 1 | 0.4% | no | 0 | bua 0.622 | 1 | 813 | 0.3052
za | Tai-Kadai | 37 | 27 | 1 | 0.7% | no | 0 | ak 0.378 | 1 | 1682 | 0.2124
af | Indo-European > Germanic > Northwest Germanic > West Germanic | 66 | 35 | 0 |  | yes | 0 | frr 0.379 | 1 | 2076 | 0.1653
afb-SA-x-dawasir | Afro-Asiatic > Semitic > Central Semitic | 1 | 16 | 0 |  | yes | 0 |  | 1 | 5 | 0.08
aii | Afro-Asiatic > Semitic > Central Semitic | 23 | 22 | 0 |  | no | 0 | syc 0.826 | 1 | 4836 | 0.3758
akk | Afro-Asiatic > Semitic | 35 | 32 | 0 |  | no | 0 | phn 0.8 | 1 | 671 | 0.0123
aot | Sino-Tibetan | 33 | 21 | 0 |  | no | 0 | zom 0.909 | 1 | 181 | 0.1367
ar-SA-x-tihama-qahtan | Afro-Asiatic > Semitic > Central Semitic | 4 | 25 | 0 |  | yes | 0 |  | 1 | 16 | 0.1084
ast-PT-x-guadrami | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 0 | 24 | 0 |  | yes | 0 |  | 1 | 20 | 0.1491
ast-PT-x-medieval | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 15 | 24 | 0 |  | yes | 0 | pov 0.2 | 1 | 20 | 0.0442
ast-PT-x-rionor | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 52 | 24 | 0 |  | yes | 0 | pt-BR-x-bahia 0.667 | 1 | 20 | 0.2429
ast-x-sanabria | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 16 | 25 | 0 |  | yes | 0 | gl-ES-x-eonavia 0.25 | 1 | 20 | 0.1236
ayl | Afro-Asiatic > Semitic > Central Semitic | 229 | 28 | 0 |  | no | 0 | arb 0.849 | 1 | 156 | 0.3055
ba | Turkic | 60 | 41 | 0 |  | yes | 0 | kk 0.55 | 2 | 70699 | 0.4047
bbn | Austronesian > Malayo-Polynesian | 22 | 18 | 0 |  | no | 0 | lmy 0.909 | 1 | 194 | 0.0689
be | Indo-European > Balto-Slavic > Slavic > East Slavic | 110 | 33 | 0 |  | no | 0 | mhr 0.309 | 2 | 160758 | 0.1276
ca-x-occident | Indo-European > Italic > Romance | 1 | 37 | 0 |  | yes | 0 |  | 2 | 180 | 0.0822
ca-x-valencia | Indo-European > Italic > Romance | 0 | 36 | 0 |  | yes | 0 |  | 2 | 180 | 0.0677
cnk | Sino-Tibetan | 46 | 28 | 0 |  | no | 0 | myo 0.478 | 1 | 342 | 0.2608
crk | Algic | 17 | 17 | 0 |  | yes | 0 | atj 0.684 | 1 | 159 | 0.1871
cs | Indo-European > Balto-Slavic > Slavic > West Slavic | 56 | 37 | 0 |  | yes | 0 | sk 0.639 | 1 | 44148 | 0.068
csb | Indo-European > Balto-Slavic > Slavic > West Slavic | 39 | 34 | 0 |  | yes | 0 | szl 0.78 | 1 | 2825 | 0.1663
cv | Turkic | 37 | 27 | 0 |  | yes | 0 | alt 0.703 | 1 | 6779 | 0.1264
dga | Atlantic-Congo | 94 | 34 | 0 |  | no | 0 | nko 0.34 | 1 | 35 | 0.1143
dng | Sino-Tibetan > Sinitic | 56 | 36 | 0 |  | no | 0 | bua 0.268 | 1 | 269 | 0.4087
dv | Indo-European > Indo-Iranian > Indo-Aryan | 51 | 50 | 0 |  | no | 0 |  | 2 | 18309 | 0.0891
dz | Sino-Tibetan | 132 | 53 | 0 |  | no | 0 |  | 1 | 230 | 0.3392
ee | Atlantic-Congo | 126 | 36 | 0 |  | no | 0 | dga 0.317 | 1 | 247 | 0.4445
egy | Afro-Asiatic > Egyptian | 25 | 25 | 0 |  | no | 0 | fia 0.538 | 1 | 2185 | 0.0183
enm | Indo-European > Germanic > Northwest Germanic > West Germanic | 46 | 28 | 0 |  | no | 0 | ofs 0.549 | 1 | 6466 | 0.262
es-ES-x-andalusi-e | Indo-European > Italic > Romance > Ibero-Romance | 2 | 28 | 0 |  | yes | 0 |  | 1 | 20 | 0.0991
es-ES-x-andalusi-w | Indo-European > Italic > Romance > Ibero-Romance | 4 | 28 | 0 |  | yes | 0 |  | 1 | 20 | 0.0504
es-ES-x-canarias | Indo-European > Italic > Romance > Ibero-Romance | 4 | 29 | 0 |  | yes | 0 |  | 1 | 20 | 0.0
es-ES-x-cantabri | Indo-European > Italic > Romance > Ibero-Romance | 1 | 28 | 0 |  | yes | 0 |  | 1 | 20 | 0.027
es-ES-x-extremad | Indo-European > Italic > Romance > Ibero-Romance | 0 | 28 | 0 |  | yes | 0 |  | 1 | 20 | 0.0052
es-ES-x-medieval | Indo-European > Italic > Romance > Ibero-Romance | 54 | 28 | 0 |  | no | 0 | an 0.81 | 1 | 20 | 0.0438
es-ES-x-murcia | Indo-European > Italic > Romance > Ibero-Romance | 3 | 28 | 0 |  | yes | 0 |  | 1 | 20 | 0.0849
ett | Tyrsenian | 26 | 26 | 0 |  | no | 0 |  | 1 | 207 | 0.1444
eu-biscayan | Vasconic | 5 | 20 | 0 |  | no | 0 |  | 1 | 20 | 0.0935
eu-x-gipuzkoa | Vasconic | 0 | 21 | 0 |  | yes | 0 |  | 1 | 20 | 0.025
eu-x-lapurdi | Vasconic | 1 | 20 | 0 |  | yes | 0 |  | 1 | 20 | 0.0654
eu-x-nafarra-beherea | Vasconic | 1 | 21 | 0 |  | yes | 0 |  | 1 | 20 | 0.0226
eu-x-nafarra-garaia | Vasconic | 1 | 21 | 0 |  | no | 0 |  | 1 | 20 | 0.1107
eu-x-roncal | Vasconic | 1 | 20 | 0 |  | yes | 0 |  | 1 | 20 | 0.0453
eu-x-zuberera | Vasconic | 3 | 22 | 0 |  | yes | 0 |  | 1 | 20 | 0.0226
ext-PT-x-barranco | Mixed Language | 25 | 34 | 0 |  | yes | 4 | aoa 0.167 | 3 | 1538 | 0.2912
fpe | Indo-European > Germanic > Northwest Germanic > West Germanic | 38 | 31 | 0 |  | no | 0 | dag 0.605 | 1 | 261 | 0.0301
fro | Indo-European > Italic > Romance | 40 | 29 | 0 |  | no | 0 | cbk-PH 0.575 | 1 | 663 | 0.2363
gl-ES-x-central | Indo-European > Italic > Romance > Ibero-Romance | 0 | 27 | 0 |  | yes | 0 |  | 1 | 20 | 0.1143
gl-ES-x-eonavia | Indo-European > Italic > Romance > Ibero-Romance | 12 | 26 | 0 |  | yes | 0 | ast-x-sanabria 0.25 | 1 | 20 | 0.1015
gl-ES-x-occident | Indo-European > Italic > Romance > Ibero-Romance | 1 | 28 | 0 |  | yes | 0 |  | 1 | 20 | 0.0734
gl-ES-x-oriental | Indo-European > Italic > Romance > Ibero-Romance | 2 | 26 | 0 |  | yes | 0 |  | 1 | 20 | 0.069
gmh | Indo-European > Germanic > Northwest Germanic | 44 | 29 | 0 |  | yes | 0 | enm 0.478 | 1 | 1516 | 0.1022
gml | Indo-European > Germanic > Northwest Germanic > West Germanic | 32 | 22 | 0 |  | yes | 0 | rhg 0.719 | 1 | 143 | 0.2771
gn | Tupian | 39 | 36 | 0 |  | yes | 0 | tpn 0.59 | 2 | 4611 | 0.1675
got | Indo-European > Germanic > East Germanic | 32 | 24 | 0 |  | no | 0 |  | 1 | 1816 | 0.0667
gur | Atlantic-Congo | 43 | 34 | 0 |  | no | 0 | fod 0.767 | 1 | 111 | 0.2968
guw | Atlantic-Congo | 57 | 34 | 0 |  | no | 0 | kpe 0.632 | 1 | 595 | 0.4311
gv | Indo-European > Celtic > Goidelic | 58 | 26 | 0 |  | no | 0 | enm-x-yola 0.466 | 1 | 690 | 0.246
gwc | Indo-European > Indo-Iranian > Indo-Aryan | 68 | 34 | 0 |  | no | 0 | pnb-PK 0.544 | 1 | 165 | 0.417
he | Afro-Asiatic > Semitic > Central Semitic | 127 | 40 | 0 |  | yes | 0 |  | 2 | 2905 | 0.3554
hrx | Indo-European > Germanic > Northwest Germanic | 75 | 29 | 0 |  | yes | 0 | nds 0.453 | 1 | 2002 | 0.0821
hts | Hadza | 64 | 30 | 0 |  | no | 0 | lus 0.375 | 1 | 329 | 0.0224
hyw | Indo-European > Armenic | 40 | 39 | 0 |  | no | 0 |  | 1 | 17009 | 0.2709
ia | Constructed | 30 | 25 | 0 |  | no | 0 | io 0.833 | 1 | 443 | 0.0646
inh | Nakh-Daghestanian | 53 | 31 | 0 |  | no | 0 | lbe 0.642 | 1 | 284 | 0.1632
io | Constructed | 29 | 26 | 0 |  | yes | 0 | ia 0.833 | 1 | 6815 | 0.0974
izh | Uralic > Finnic | 6 | 27 | 0 |  | yes | 0 |  | 1 | 7886 | 0.0092
jv | Austronesian | 31 | 22 | 0 |  | no | 0 | su 0.774 | 1 | 99 | 0.2286
ka | Kartvelian | 33 | 33 | 0 |  | no | 0 | lzz 0.941 | 1 | 79887 | 0.2337
kgp | Nuclear-Macro-Je | 28 | 27 | 0 |  | no | 0 | yrl 0.516 | 1 | 106 | 0.2351
ki | Atlantic-Congo | 34 | 21 | 0 |  | no | 0 | aks 0.706 | 1 | 1025 | 0.3914
kk | Turkic | 40 | 40 | 0 |  | yes | 0 | tt 0.8 | 2 | 2117 | 0.182
koi | Uralic | 74 | 30 | 0 |  | no | 0 | kv 1.0 | 1 | 229 | 0.092
kru | Dravidian | 62 | 45 | 0 |  | no | 0 | bho 0.806 | 1 | 187 | 0.1947
lsi | Sino-Tibetan | 54 | 25 | 0 |  | no | 0 | aot 0.444 | 1 | 96 | 0.4222
mcm | Indo-European > Italic > Romance > Ibero-Romance | 30 | 25 | 0 |  | yes | 0 | kcn 0.853 | 1 | 33 | 0.1146
mga | Indo-European > Celtic > Goidelic | 52 | 23 | 0 |  | yes | 0 | sga 0.731 | 1 | 328 | 0.0594
mic | Algic | 30 | 16 | 0 |  | no | 0 | nnb 0.5 | 1 | 203 | 0.1114
mk | Indo-European > Balto-Slavic > Slavic > South Slavic | 31 | 31 | 0 |  | no | 0 | orv 0.658 | 1 | 10750 | 0.0221
mn | Mongolic | 70 | 35 | 0 |  | no | 0 | bua 0.243 | 2 | 19120 | 0.2077
mqs | North Halmahera | 23 | 22 | 0 |  | no | 0 | tft 1.0 | 1 | 790 | 0.0495
mtq | Austroasiatic | 95 | 65 | 0 |  | no | 0 | bdq 0.284 | 1 | 194 | 0.3412
mwl-x-ifanes | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 0 | 26 | 0 |  | yes | 0 |  | 3 | 26 | 0.625
mwl-x-sendim | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 4 | 28 | 0 |  | yes | 0 |  | 3 | 110 | 0.447
mww | Hmong-Mien | 66 | 26 | 0 |  | no | 0 | avi 0.242 | 1 | 489 | 0.0107
myv | Uralic | 32 | 32 | 0 |  | no | 0 | yux 0.771 | 1 | 6442 | 0.0944
nds | Indo-European > Germanic > Northwest Germanic > West Germanic | 72 | 35 | 0 |  | yes | 0 | de-DE 0.736 | 1 | 308 | 0.2231
ne | Indo-European > Indo-Iranian > Indo-Aryan | 65 | 58 | 0 |  | no | 0 | awa 0.615 | 1 | 2052 | 0.1191
new | Sino-Tibetan | 45 | 51 | 0 |  | no | 1 | mr 0.266 | 1 | 416 | 0.0282
nup | Atlantic-Congo | 30 | 24 | 0 |  | no | 0 | bom 0.844 | 1 | 393 | 0.3979
oc | Indo-European > Italic > Romance > Gallo-Romance | 68 | 34 | 0 |  | yes | 0 | ca-x-medieval 0.529 | 1 | 675 | 0.1283
oc-x-aranes | Indo-European > Italic > Romance > Gallo-Romance | 68 | 27 | 0 |  | yes | 0 | ca-x-medieval 0.5 | 1 | 20 | 0.0787
olo | Uralic | 28 | 27 | 0 |  | no | 0 | vep 0.857 | 1 | 278 | 0.0801
om | Afro-Asiatic > Cushitic | 37 | 26 | 0 |  | no | 0 | sid 0.763 | 1 | 519 | 0.1026
osx | Indo-European > Germanic > Northwest Germanic > West Germanic | 35 | 23 | 0 |  | no | 0 | goh 0.737 | 1 | 244 | 0.2786
ota | Turkic | 49 | 30 | 0 |  | no | 0 | fa 0.673 | 1 | 161 | 0.3536
pcc | Tai-Kadai | 114 | 26 | 0 |  | no | 0 | kdx 0.228 | 1 | 153 | 0.0038
pjt | Pama-Nyungan | 26 | 18 | 0 |  | no | 0 | dec 0.462 | 1 | 125 | 0.0027
pqm | Algic | 18 | 18 | 0 |  | no | 0 | pam 0.762 | 1 | 151 | 0.1759
pt-AO | Indo-European > Italic > Romance > Ibero-Romance | 2 | 36 | 0 |  | yes | 0 |  | 2 | 53164 | 0.2307
pt-BR-x-bahia | Indo-European > Italic > Romance > Ibero-Romance | 57 | 29 | 0 |  | yes | 0 | fax 0.759 | 1 | 20 | 0.1611
pt-BR-x-ce | Indo-European > Italic > Romance > Ibero-Romance | 57 | 29 | 0 |  | yes | 0 | fax 0.759 | 1 | 20 | 0.1181
pt-BR-x-fluminen | Indo-European > Italic > Romance > Ibero-Romance | 57 | 31 | 0 |  | yes | 0 | fax 0.759 | 1 | 20 | 0.0666
pt-BR-x-mg | Indo-European > Italic > Romance > Ibero-Romance | 57 | 33 | 0 |  | yes | 0 | fax 0.759 | 1 | 20 | 0.1146
pt-BR-x-norte | Indo-European > Italic > Romance > Ibero-Romance | 57 | 32 | 0 |  | yes | 0 | fax 0.759 | 1 | 20 | 0.1397
pt-BR-x-pr | Indo-European > Italic > Romance > Ibero-Romance | 57 | 31 | 0 |  | yes | 0 | fax 0.759 | 1 | 20 | 0.0922
pt-BR-x-recife | Indo-European > Italic > Romance > Ibero-Romance | 57 | 30 | 0 |  | yes | 0 | fax 0.759 | 1 | 20 | 0.1591
pt-BR-x-sul | Indo-European > Italic > Romance > Ibero-Romance | 57 | 31 | 0 |  | yes | 0 | fax 0.759 | 1 | 20 | 0.1331
pt-CV | Indo-European > Italic > Romance > Ibero-Romance | 4 | 30 | 0 |  | yes | 0 |  | 1 | 20 | 0.257
pt-GW | Indo-European > Italic > Romance > Ibero-Romance | 4 | 29 | 0 |  | yes | 0 |  | 1 | 20 | 0.3198
pt-MO | Indo-European > Italic > Romance > Ibero-Romance | 2 | 30 | 0 |  | yes | 0 |  | 1 | 20 | 0.1146
pt-PT-x-acores | Indo-European > Italic > Romance > Ibero-Romance | 1 | 34 | 0 |  | yes | 0 |  | 3 | 51 | 0.3066
pt-PT-x-alentejo | Indo-European > Italic > Romance > Ibero-Romance | 4 | 33 | 0 |  | yes | 0 |  | 4 | 56 | 0.3
pt-PT-x-alfena | Indo-European > Italic > Romance > Ibero-Romance | 4 | 32 | 0 |  | yes | 0 |  | 2 | 21 | 0.3042
pt-PT-x-algarve | Indo-European > Italic > Romance > Ibero-Romance | 3 | 32 | 0 |  | yes | 0 |  | 3 | 53 | 0.3175
pt-PT-x-aveiro | Indo-European > Italic > Romance > Ibero-Romance | 4 | 33 | 0 |  | yes | 0 |  | 2 | 26 | 0.2739
pt-PT-x-beira | Indo-European > Italic > Romance > Ibero-Romance | 4 | 37 | 0 |  | yes | 0 |  | 3 | 36 | 0.4327
pt-PT-x-braga | Indo-European > Italic > Romance > Ibero-Romance | 3 | 31 | 0 |  | yes | 0 |  | 1 | 20 | 0.0574
pt-PT-x-coimbra | Indo-European > Italic > Romance > Ibero-Romance | 0 | 29 | 0 |  | yes | 0 |  | 1 | 20 | 0.0541
pt-PT-x-madeira | Indo-European > Italic > Romance > Ibero-Romance | 3 | 36 | 0 |  | yes | 0 |  | 3 | 54 | 0.3002
pt-PT-x-medieval | Indo-European > Italic > Romance > Ibero-Romance | 30 | 24 | 0 |  | yes | 0 | ia 0.333 | 1 | 20 | 0.272
pt-PT-x-sao-miguel | Indo-European > Italic > Romance > Ibero-Romance | 3 | 33 | 0 |  | yes | 0 |  | 2 | 32 | 0.3917
pt-PT-x-terceira | Indo-European > Italic > Romance > Ibero-Romance | 0 | 30 | 0 |  | yes | 0 |  | 2 | 30 | 0.2179
pt-PT-x-tras-os-montes | Indo-European > Italic > Romance > Ibero-Romance | 2 | 33 | 0 |  | yes | 0 |  | 2 | 26 | 0.2985
pt-ST | Indo-European > Italic > Romance > Ibero-Romance | 4 | 29 | 0 |  | yes | 0 |  | 1 | 20 | 0.2796
pt-UY | Indo-European > Italic > Romance > Ibero-Romance | 4 | 30 | 0 |  | yes | 0 |  | 1 | 20 | 0.0802
roa-x-galaico-pt | Indo-European > Italic > Romance > Ibero-Romance | 54 | 23 | 0 |  | yes | 0 | pt-BR-x-bahia 0.719 | 1 | 20 | 0.1283
sce | Mongolic | 45 | 26 | 0 |  | no | 0 | nhb 0.444 | 1 | 168 | 0.064
sel | Uralic | 55 | 33 | 0 |  | no | 0 | enf 0.702 | 1 | 886 | 0.0342
sia | Uralic > Saami | 53 | 40 | 0 |  | no | 0 | sjd 0.714 | 1 | 179 | 0.0948
skr | Indo-European > Indo-Iranian > Indo-Aryan | 51 | 36 | 0 |  | no | 0 | bal 0.706 | 1 | 309 | 0.2869
so | Afro-Asiatic > Cushitic | 34 | 24 | 0 |  | no | 0 | rhg 0.794 | 1 | 230 | 0.5579
stq | Indo-European > Germanic > Northwest Germanic > West Germanic | 54 | 29 | 0 |  | yes | 0 | frr 0.815 | 1 | 818 | 0.1959
syc | Afro-Asiatic > Semitic > Central Semitic | 22 | 22 | 0 |  | no | 0 | tru 0.875 | 1 | 96 | 0.3707
szl | Indo-European > Balto-Slavic > Slavic > West Slavic | 41 | 34 | 0 |  | yes | 0 | csb 0.78 | 1 | 2377 | 0.2148
ta | Dravidian | 50 | 47 | 0 |  | no | 0 |  | 2 | 146030 | 0.3757
tet | Austronesian > Malayo-Polynesian | 36 | 28 | 0 |  | yes | 0 | kcn 0.75 | 1 | 55 | 0.0683
tew | Kiowa-Tanoan | 115 | 31 | 0 |  | no | 0 | fpe 0.2 | 1 | 106 | 0.0
tft | North Halmahera | 23 | 22 | 0 |  | no | 0 | mqs 1.0 | 1 | 293 | 0.1041
th | Tai-Kadai | 170 | 70 | 0 |  | no | 0 |  | 2 | 40925 | 0.4281
tkl | Austronesian > Malayo-Polynesian | 20 | 20 | 0 |  | no | 0 | to 0.864 | 1 | 340 | 0.0497
tpn | Tupian | 38 | 33 | 0 |  | yes | 0 | gn 0.59 | 1 | 372 | 0.0951
tru | Afro-Asiatic > Semitic > Central Semitic | 24 | 24 | 0 |  | no | 0 | syc 0.875 | 1 | 168 | 0.3607
tt | Turkic | 39 | 36 | 0 |  | yes | 0 | kk 0.8 | 1 | 22220 | 0.2455
twf | Kiowa-Tanoan | 118 | 48 | 0 |  | no | 0 | ha 0.169 | 1 | 135 | 0.024
uby | Abkhaz-Adyge | 90 | 45 | 0 |  | no | 0 | ab 0.4 | 1 | 1317 | 0.0247
udm | Uralic | 72 | 36 | 0 |  | no | 0 | koi 0.703 | 1 | 973 | 0.211
uk | Indo-European > Balto-Slavic > Slavic > East Slavic | 45 | 35 | 0 |  | yes | 0 | rue 0.667 | 3 | 103312 | 0.2665
vot | Uralic > Finnic | 13 | 28 | 0 |  | yes | 0 | krl 0.538 | 1 | 2832 | 0.0898
wiy | Algic | 44 | 33 | 0 |  | no | 0 | lkt 0.477 | 1 | 151 | 0.0164
xh | Atlantic-Congo > Bantu | 82 | 27 | 0 |  | yes | 0 | zu 0.561 | 1 | 888 | 0.3776
xsl | Athabaskan-Eyak-Tlingit | 87 | 36 | 0 |  | no | 0 | apw 0.398 | 1 | 146 | 0.0273
ycl | Sino-Tibetan | 44 | 24 | 0 |  | no | 0 | sce 0.333 | 1 | 111 | 0.0108
zh | Sino-Tibetan > Sinitic | 360 | 27 | 0 |  | no | 0 | kdx 0.072 | 1 | 4718 | 0.2879
zom | Sino-Tibetan | 32 | 20 | 0 |  | no | 0 | aot 0.909 | 1 | 134 | 0.4399
zu | Atlantic-Congo > Bantu | 66 | 26 | 0 |  | yes | 0 | nd 0.682 | 1 | 1754 | 0.2311

---
[← Lexicon-overlay scoreboard](lexicon_scoreboard.md) · [Home](../../index.md) · [Language pages →](../../languages/index.md)
