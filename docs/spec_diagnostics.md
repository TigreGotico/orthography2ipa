# Spec diagnostics

Regenerate with `PYTHONPATH=$PWD python3 scripts/spec_diagnostics.py`. Three mechanical signals separate a spec that is wrong from a spec that is merely imprecise: gold characters its grapheme table cannot consume, which the engine deletes before a rule can see them; inheritance that crosses a language-family boundary; and a table that matches another language almost pair for pair. None is proof on its own. Each points at a spec worth reading before any rule in it is refined.

Of 7659 specs, 414 have a cached gold to measure against, and 299 of those leave at least one gold character unmapped.

A language scored on several gold datasets is reported here **per dataset**, not unioned. Unioning inflates the count (a character can be unmapped in one corpus only) and blends unrelated problems — one dataset's loanword letters with another's diacritic gaps — into a single misleading figure. The `combined_*` fields in the JSON output keep the union for reference, but every ranking below and every row you might prioritise off of is per dataset.

## Ranked by unmapped gold characters (per dataset)

- **ja** (Japanese) / `vox_communis` — 1268 of 1419 gold characters unmapped, hitting 67.5% of 5000 scanned words; own table 305 graphemes, resolved 305; worst per 0.4273; n 158050
  - unmapped: `一 丁 七 万 丈 三 上 下 不 与 世 両 並 中 丸 丹 主 久 之 乗 九 乱 乳 乾 亀 了 予 争 事 二 互 五 井 亡 交 京 亭 人 今 介 仏 仕 他 付 代 令 以 仰 件 任 企 伊 伏 休 会 伝 伸 位 低 住`
  - chain: parent=jpx [Japonic]
  - no stress block reachable
- **ja** (Japanese) / `ipadict` — 1120 of 1269 gold characters unmapped, hitting 73.2% of 5000 scanned words; own table 305 graphemes, resolved 305; worst per 0.4273; n 158050
  - unmapped: `× α ※ ← ↑ → ↓ △ ○ ◎ 〃 々 〆 〇 〒 ゝ ヵ ヶ ・ 一 丁 七 万 三 上 下 不 世 両 並 中 丸 主 丼 久 乍 乗 乱 乳 亀 了 事 二 互 五 井 亡 交 人 仁 介 仏 仕 他 付 仝 代 令 以 仲`
  - chain: parent=jpx [Japonic]
  - no stress block reachable
- **am** (Amharic) / `vox_communis` — 36 of 229 gold characters unmapped, hitting 13.9% of 5000 scanned words; own table 211 graphemes, resolved 211; worst per 0.3813; n 5841
  - unmapped: `ሏ ሟ ሯ ሷ ቋ ቧ ቨ ቪ ቫ ቬ ቭ ቮ ቷ ቿ ኀ ኃ ኅ ኋ ኗ ኟ ኳ ኸ ኽ ዟ ዷ ጇ ጓ ጧ ጿ ፁ ፃ ፅ ፏ ፡ ። ፣`
  - chain: parent=sem-x-ethiopic [Afro-Asiatic > Semitic]
  - no stress block reachable
- **en-GB** (British English (RP)) / `wikipron` — 31 of 57 gold characters unmapped, hitting 2.9% of 5000 scanned words; own table 83 graphemes, resolved 83; worst per 0.3001; n 154939
  - unmapped: `' á â ã ä å æ ç é ê ë í ñ ó ö ú ü ā ă č ē ę ě ī ł œ ś ş ș ț ʼ`
  - chain: parent=enm [Indo-European > Germanic > Northwest Germanic > West Germanic]
- **ab** (Abkhaz) / `wikipron` — 20 of 59 gold characters unmapped, hitting 25.2% of 206 scanned words; own table 67 graphemes, resolved 67; worst per 0.4563; n 32345
  - unmapped: `' ь ҙ ә ԡ ԣ ԫ ԭ ꚁ ꚃ ꚅ ꚇ ꚉ ꚋ ꚍ ꚏ ꚑ ꚓ ꚕ ꚗ`
  - chain: parent=x-clade-abkh1242 [?]
  - no stress block reachable
- **cy** (Welsh) / `wikipron` — 16 of 44 gold characters unmapped, hitting 1.5% of 5000 scanned words; own table 40 graphemes, resolved 40; worst per 0.2985; n 37830
  - unmapped: `' k v x z à á é ë ï ò ö ü ý ẃ ỳ`
  - chain: parent=xbr [Indo-European > Celtic > Brythonic]
  - no stress block reachable
- **wbk** (Waigali) / `wikipron` — 15 of 48 gold characters unmapped, hitting 46.1% of 154 scanned words; own table 41 graphemes, resolved 41; worst per 0.2022; n 153
  - unmapped: `v ã ä ë ö ü ć ň ř ũ ǖ ̃ ̣ ṅ ẽ`
  - chain: parent=x-clade-indo1320 [Indo-European]
  - no stress block reachable
- **cy** (Welsh) / `vox_communis` — 13 of 41 gold characters unmapped, hitting 5.0% of 5000 scanned words; own table 40 graphemes, resolved 40; worst per 0.2985; n 37830
  - unmapped: `' k q v x z ¬ á ä é ï ñ ö`
  - chain: parent=xbr [Indo-European > Celtic > Brythonic]
  - no stress block reachable
- **yo** (Yoruba) / `wikipron` — 13 of 38 gold characters unmapped, hitting 3.0% of 4937 scanned words; own table 56 graphemes, resolved 56; worst per 0.6341; n 9328
  - unmapped: `c z ɔ ɛ ̀ ́ ̂ ̄ ̌ ḿ ị ộ ụ`
  - chain: parent=nic [Atlantic-Congo]
  - no stress block reachable
- **am** (Amharic) / `wikipron` — 12 of 158 gold characters unmapped, hitting 5.2% of 478 scanned words; own table 211 graphemes, resolved 211; worst per 0.3813; n 5841
  - unmapped: `ሷ ቋ ቍ ቪ ቷ ኅ ኳ ጐ ጓ ፃ ፅ ፡`
  - chain: parent=sem-x-ethiopic [Afro-Asiatic > Semitic]
  - no stress block reachable
- **ess** (Central Siberian Yupik) / `northeuralex` — 12 of 36 gold characters unmapped, hitting 27.4% of 814 scanned words; own table 29 graphemes, resolved 29; worst per 0.1074; n 814
  - unmapped: `̌ б д е ж о ц ч ш щ ь ӽ`
  - chain: parent=x-clade-eski1264 [?]
  - no stress block reachable
- **fi** (Finnish) / `wikipron` — 12 of 38 gold characters unmapped, hitting 1.1% of 5000 scanned words; own table 62 graphemes, resolved 62; worst per 0.0609; n 274968
  - unmapped: `' q x á å é ú ü ă š ž ș`
  - chain: parent=x-clade-finn1317 [Uralic]
- **kok** (Konkani) / `kaikki` — 12 of 65 gold characters unmapped, hitting 0.4% of 835 scanned words; own table 70 graphemes, resolved 70; worst per 0.224; n 830
  - unmapped: `g y õ ಂ ಜ ಣ ನ ಪ ರ ು ೆ ೊ`
  - chain: parent=sa [Indo-European > Indo-Iranian > Indo-Aryan]
  - no stress block reachable
- **kw** (Cornish) / `wikipron` — 12 of 35 gold characters unmapped, hitting 4.2% of 648 scanned words; own table 31 graphemes, resolved 31; worst per 0.2521; n 602
  - unmapped: `c à â è ë ò ÿ ɐ ᵹ ꝺ ꝿ ꞇ`
  - chain: parent=xbr [Indo-European > Celtic > Brythonic]
  - no stress block reachable
- **li** (Limburgish) / `wikipron` — 12 of 41 gold characters unmapped, hitting 33.6% of 1128 scanned words; own table 114 graphemes, resolved 114; worst per 0.3819; n 987
  - unmapped: `' ä é ë ï ü ą ǫ ̈ ̩ ͜ ṣ`
  - chain: parent=x-clade-germ1287 [Indo-European]
  - no stress block reachable
- **pox** (Polabian) / `wikipron` — 12 of 46 gold characters unmapped, hitting 53.3% of 321 scanned words; own table 40 graphemes, resolved 40; worst per 0.3204; n 314
  - unmapped: `x ă ď ŕ ť ʒ ́ ̇ ̯ ḿ ṕ ’`
  - chain: parent=x-clade-west2792 [Indo-European > Balto-Slavic > Slavic]
  - no stress block reachable
- **my** (Burmese) / `wikipron` — 11 of 59 gold characters unmapped, hitting 2.9% of 5000 scanned words; own table 231 graphemes, resolved 231; worst per 0.1926; n 7941
  - unmapped: `့ း ္ ် ျ ြ ှ ၍ ၏ ၐ ၑ`
  - chain: parent=sit [Sino-Tibetan]
  - no stress block reachable
- **phl** (Phalura) / `wikipron` — 11 of 43 gold characters unmapped, hitting 29.6% of 2240 scanned words; own table 46 graphemes, resolved 46; worst per 0.3287; n 2173
  - unmapped: `f q x ã č ĩ š ǰ ɣ ́ ẓ`
  - chain: parent=iir [Indo-European > Indo-Iranian]
  - no stress block reachable
- **ale** (Aleut) / `northeuralex` — 10 of 27 gold characters unmapped, hitting 62.3% of 896 scanned words; own table 30 graphemes, resolved 30; worst per 0.3993; n 1014
  - unmapped: `' b c f p r v í ǵ ́`
  - chain: parent=x-clade-eski1264 [?]
  - no stress block reachable
- **eu** (Basque (Euskara)) / `ipa_childes` — 10 of 32 gold characters unmapped, hitting 5.0% of 3969 scanned words; own table 35 graphemes, resolved 35; worst per 0.0984; n 82505
  - unmapped: `c q v w y á é í ó ú`
  - chain: parent=xaq [Vasconic]
  - no stress block reachable

## Ranked by share of gold words that lose a character (per dataset)

The character count above treats a rare loan letter and a missing nasal vowel series alike. This ordering weights each spec/dataset pair by how much of that dataset's own gold the deletion actually touches.

- **fpe** (Fernando Po Creole English) / `wikipron` — 95.4% of 261 scanned words lose at least one character; unmapped `á é í ó ú ́`; worst per 0.365
- **mhr** (Eastern Mari) / `northeuralex` — 85.2% of 992 scanned words lose at least one character; unmapped `́`; worst per 0.1736
- **nhg** (Tetelcingo Nahuatl) / `wikipron` — 76.7% of 305 scanned words lose at least one character; unmapped `b d f j r ö ā ̱`; worst per 0.2367
- **nhx** (Isthmus-Mecayapan Nahuatl) / `wikipron` — 76.7% of 146 scanned words lose at least one character; unmapped `r z á é í ñ ó ʼ ̱ ꞌ`; worst per 0.1913
- **ja** (Japanese) / `ipadict` — 73.2% of 5000 scanned words lose at least one character; unmapped `× α ※ ← ↑ → ↓ △ ○ ◎ 〃 々 〆 〇 〒 ゝ ヵ ヶ ・ 一 丁 七 万 三 上 下 不 世 両 並`; worst per 0.4273
- **ja** (Japanese) / `vox_communis` — 67.5% of 5000 scanned words lose at least one character; unmapped `一 丁 七 万 丈 三 上 下 不 与 世 両 並 中 丸 丹 主 久 之 乗 九 乱 乳 乾 亀 了 予 争 事 二`; worst per 0.4273
- **ale** (Aleut) / `northeuralex` — 62.3% of 896 scanned words lose at least one character; unmapped `' b c f p r v í ǵ ́`; worst per 0.3993
- **shn** (Shan) / `wikipron` — 62.0% of 2607 scanned words lose at least one character; unmapped `ဵ ် ျ ြ ွ ႀ ႂ ႃ ႅ ႆ`; worst per 0.3348
- **cnk** (Khumi Chin) / `wikipron` — 61.1% of 350 scanned words lose at least one character; unmapped `c q x ä ö ü`; worst per 0.502
- **ar-TN** (Tunisian Arabic) / `arabic_tts` — 60.0% of 20 scanned words lose at least one character; unmapped `، ؟`; worst per 0.3059
- **ar-TN** (Tunisian Arabic) / `gold20_arabic` — 60.0% of 20 scanned words lose at least one character; unmapped `، ؟`; worst per 0.3059
- **ar-JO** (Jordanian Arabic (Ammani)) / `arabic_tts` — 55.0% of 20 scanned words lose at least one character; unmapped `، ؟`; worst per 0.3718
- **ar-JO** (Jordanian Arabic (Ammani)) / `gold20_arabic` — 55.0% of 20 scanned words lose at least one character; unmapped `، ؟`; worst per 0.3718
- **ar-SD** (Sudanese Arabic) / `arabic_tts` — 55.0% of 20 scanned words lose at least one character; unmapped `، ؟`; worst per 0.0274
- **ar-SD** (Sudanese Arabic) / `gold20_arabic` — 55.0% of 20 scanned words lose at least one character; unmapped `، ؟`; worst per 0.0274
- **pox** (Polabian) / `wikipron` — 53.3% of 321 scanned words lose at least one character; unmapped `x ă ď ŕ ť ʒ ́ ̇ ̯ ḿ ṕ ’`; worst per 0.3204
- **ady** (Adyghe) / `northeuralex` — 50.3% of 928 scanned words lose at least one character; unmapped `́ в ь`; worst per 0.1684
- **ar-AE** (Emirati Arabic) / `arabic_tts` — 50.0% of 20 scanned words lose at least one character; unmapped `، ؟`; worst per 0.0441
- **ar-AE** (Emirati Arabic) / `gold20_arabic` — 50.0% of 20 scanned words lose at least one character; unmapped `، ؟`; worst per 0.0441
- **cic** (Chickasaw) / `wikipron` — 48.7% of 394 scanned words lose at least one character; unmapped `e v á í ó ̠ ̱ ꞌ`; worst per 0.1028

## Tables asserted from another language

A spec's closest table twin among the specs it does not declare as a base. A ratio near 1 means the table was taken from that language rather than written for this one; the notes then describe a language the data never encodes.

- **acm** (Mesopotamian Arabic, Afro-Asiatic > Semitic > Central Semitic) — graphemes ayl 1.0, allophones none; declares parent=x-clade-cent2236 [Afro-Asiatic > Semitic]; worst per 0.4249
- **ayl** (Libyan Arabic, Afro-Asiatic > Semitic > Central Semitic) — graphemes acm 1.0, allophones none; declares parent=ar-x-maghrebi [Afro-Asiatic > Semitic > Central Semitic]; worst per 0.3799
- **koi** (Komi-Permyak, Uralic) — graphemes kv 1.0, allophones none; declares parent=x-clade-ural1272 [?]; worst per 0.092
- **kv** (Komi, Uralic) — graphemes koi 1.0, allophones none; declares parent=x-clade-ural1272 [?]; worst per 0.157
- **mqs** (West Makian, North Halmahera) — graphemes tft 1.0, allophones none; declares parent=x-clade-nort2923 [?]; worst per 0.0495
- **nap** (Neapolitan, Indo-European > Italic > Romance > Italo-Romance) — graphemes it-IT-x-puglia 0.854, allophones it-IT-x-abruzzo 1.0; declares parent=x-clade-italorom [Indo-European > Italic > Romance]; worst per 0.2792
- **tft** (Ternate, North Halmahera) — graphemes mqs 1.0, allophones none; declares parent=x-clade-nort2923 [?]; worst per 0.1041
- **it-IT** (Italian, Indo-European > Italic > Romance > Italo-Romance) — graphemes co 0.634, allophones nap 0.979; declares parent=x-clade-italorom [Indo-European > Italic > Romance]; worst per 0.2341
- **tzm** (Central Atlas Tamazight, Afro-Asiatic > Berber) — graphemes zgh 0.971, allophones none; declares parent=ber-x-kabyle-atlas [Afro-Asiatic > Berber]; worst per 0.016
- **ban** (Balinese, Austronesian) — graphemes min 0.871, allophones su 0.963; declares parent=x-clade-aust1307 [?]; worst per 0.163
- **ia** (Interlingua, Constructed) — graphemes io 0.833, allophones ie 0.963; declares (standalone); worst per 0.0646
- **rw** (Kinyarwanda, Atlantic-Congo > Bantu) — graphemes lua 0.8, allophones lua 0.963; declares parent=x-clade-narr1281 [Atlantic-Congo]; worst per 0.1388
- **su** (Sundanese, Austronesian > Malayo-Polynesian) — graphemes kge 0.893, allophones ban 0.963; declares parent=x-clade-mala1545 [Austronesian]; worst per 0.0969
- **iba** (Iban, Austronesian > Malayo-Polynesian) — graphemes lmy 0.957, allophones ban 0.889; declares parent=x-clade-mala1545 [Austronesian]; worst per 0.1655
- **lmy** (Lamboya, Austronesian > Malayo-Polynesian) — graphemes iba 0.957, allophones none; declares parent=x-clade-mala1545 [Austronesian]; worst per 0.1695
- **syc** (Classical Syriac, Afro-Asiatic > Semitic > Central Semitic) — graphemes tru 0.957, allophones none; declares parent=x-clade-cent2236 [Afro-Asiatic > Semitic]; worst per 0.4353
- **tru** (Turoyo, Afro-Asiatic > Semitic > Central Semitic) — graphemes syc 0.957, allophones none; declares parent=x-clade-cent2236 [Afro-Asiatic > Semitic]; worst per 0.4799
- **ceb** (Cebuano, Austronesian > Malayo-Polynesian) — graphemes pam 0.913, allophones pam 0.955; declares parent=x-clade-mala1545 [Austronesian]; worst per 0.1058
- **pam** (Kapampangan, Austronesian > Malayo-Polynesian) — graphemes war 0.952, allophones ceb 0.955; declares parent=x-clade-mala1545 [Austronesian]; worst per 0.2861
- **de-DE** (German, Indo-European > Germanic > Northwest Germanic > West Germanic) — graphemes nds 0.736, allophones nds 0.953; declares parent=x-clade-west2793 [Indo-European > Germanic > Northwest Germanic]; worst per 0.3948

## Ranked by cross-family inheritance

- **new** (Newar, Sino-Tibetan) — parent=x-clade-sino1245 [?]; graphemes_base=hi [Indo-European > Indo-Iranian > Indo-Aryan] CROSS-FAMILY; per 0.0282; 0 unmapped gold chars (union across datasets)

## Declared inventory contradicting emitted output

- **ii** (Nuosu) — declares 74 phonemes it never emits, emits 1165 it never declares; chain: parent=x-clade-sino1245 [?]
- **nmn** (ǃXóõ) — declares 103 phonemes it never emits, emits 163 it never declares; chain: parent=x-clade-tuuu1241 [?]
- **bax** (Bamun) — declares 7 phonemes it never emits, emits 118 it never declares; chain: parent=x-clade-atla1278 [?]
- **mag** (Magahi) — declares 30 phonemes it never emits, emits 89 it never declares; chain: parent=x-clade-indo1321 [Indo-European > Indo-Iranian]; graphemes_base=hi [Indo-European > Indo-Iranian > Indo-Aryan]; allophones_base=hi [Indo-European > Indo-Iranian > Indo-Aryan]
- **lbe** (Lak) — declares 94 phonemes it never emits, emits 23 it never declares; chain: parent=x-clade-nakh1245 [?]
- **kbd** (Kabardian) — declares 85 phonemes it never emits, emits 18 it never declares; chain: parent=x-clade-abkh1242 [?]
- **bfj** (Bafanji) — declares 30 phonemes it never emits, emits 70 it never declares; chain: parent=x-clade-atla1278 [?]
- **udm** (Udmurt) — declares 37 phonemes it never emits, emits 58 it never declares; chain: parent=x-clade-ural1272 [?]
- **lez** (Lezgian) — declares 80 phonemes it never emits, emits 14 it never declares; chain: parent=x-clade-nakh1245 [?]
- **new** (Newar) — declares 20 phonemes it never emits, emits 73 it never declares; chain: parent=x-clade-sino1245 [?]; graphemes_base=hi [Indo-European > Indo-Iranian > Indo-Aryan] CROSS-FAMILY
- **yuc** (Yuchi) — declares 34 phonemes it never emits, emits 46 it never declares; chain: (standalone)
- **skr** (Saraiki) — declares 56 phonemes it never emits, emits 22 it never declares; chain: parent=x-clade-indo1321 [Indo-European > Indo-Iranian]
- **inh** (Ingush) — declares 53 phonemes it never emits, emits 22 it never declares; chain: parent=x-clade-nakh1245 [?]
- **nb** (Norwegian Bokmål) — declares 21 phonemes it never emits, emits 54 it never declares; chain: parent=no [Indo-European > Germanic > Northwest Germanic > North Germanic]; graphemes_base=no [Indo-European > Germanic > Northwest Germanic > North Germanic]; allophones_base=no [Indo-European > Germanic > Northwest Germanic > North Germanic]
- **tsb** (Tsamai) — declares 47 phonemes it never emits, emits 27 it never declares; chain: parent=x-clade-afro1255 [?]
- **sje** (Pite Sami) — declares 15 phonemes it never emits, emits 58 it never declares; chain: parent=x-clade-ural1272 [?]
- **bot** (Bongo) — declares 6 phonemes it never emits, emits 66 it never declares; chain: parent=x-clade-cent2225 [?]
- **dsq** (Tadaksahak) — declares 64 phonemes it never emits, emits 7 it never declares; chain: parent=x-clade-song1307 [?]
- **hig** (Kamwe) — declares 7 phonemes it never emits, emits 64 it never declares; chain: parent=x-clade-afro1255 [?]
- **dim** (Dime) — declares 64 phonemes it never emits, emits 6 it never declares; chain: parent=x-clade-sout2845 [?]

## Full table

Every spec that is scored on the board, plus any spec flagged by a signal above. Specs with neither a gold nor a flag carry no evidence either way and are left to the JSON output. `gold chars` and `unmapped` here are the union across every gold dataset the spec is scored on — use the per-dataset sections above before prioritising a row off this table.

code | family | own graphemes | gold chars (union) | unmapped (union) | words hit (union) | stress | cross-family | twin | rows | n | per
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
ja | Japonic | 305 | 1825 | 1669 | 70.4% | no | 0 |  | 2 | 158050 | 0.4273
am | Afro-Asiatic > Semitic | 211 | 234 | 38 | 13.1% | no | 0 | ti 0.825 | 2 | 5841 | 0.3813
en-GB | Indo-European > Germanic > Northwest Germanic > West Germanic | 83 | 57 | 31 | 3.3% | yes | 0 | gul 0.313 | 3 | 154939 | 0.3001
cy | Indo-European > Celtic > Brythonic | 40 | 49 | 21 | 7.4% | no | 0 | wlm 0.6 | 3 | 37830 | 0.2985
ab | Abkhaz-Adyge | 67 | 62 | 20 | 1.0% | no | 0 | uby 0.378 | 2 | 32345 | 0.4563
nb | Indo-European > Germanic > Northwest Germanic > North Germanic | 37 | 45 | 16 | 0.7% | yes | 0 | nn 0.405 | 3 | 16070 | 0.3871
wbk | Indo-European > Indo-Iranian | 41 | 48 | 15 | 46.1% | no | 0 | pal 0.634 | 1 | 153 | 0.2022
yo | Atlantic-Congo | 56 | 49 | 13 | 1.6% | no | 0 | guw 0.304 | 2 | 9328 | 0.6341
en-US | Indo-European > Germanic > Northwest Germanic > West Germanic | 7 | 38 | 12 | 5.7% | yes | 0 |  | 4 | 290127 | 0.3666
ess | Eskimo-Aleut | 29 | 36 | 12 | 27.4% | no | 0 | ckt 0.483 | 1 | 814 | 0.1074
fi | Uralic > Finnic | 62 | 38 | 12 | 0.5% | yes | 0 | ang 0.468 | 3 | 274968 | 0.0609
kok | Indo-European > Indo-Iranian > Indo-Aryan | 70 | 65 | 12 | 0.4% | no | 0 | kru 0.729 | 1 | 830 | 0.224
kw | Indo-European > Celtic > Brythonic | 31 | 35 | 12 | 4.2% | no | 0 | yol 0.706 | 1 | 602 | 0.2521
li | Indo-European > Germanic | 114 | 41 | 12 | 33.6% | no | 0 | nl 0.289 | 1 | 987 | 0.3819
pox | Indo-European > Balto-Slavic > Slavic > West Slavic | 40 | 46 | 12 | 53.3% | no | 0 | dsb 0.7 | 1 | 314 | 0.3204
eu | Vasconic | 35 | 33 | 11 | 1.9% | no | 0 | lad 0.6 | 4 | 82505 | 0.0984
my | Sino-Tibetan | 231 | 59 | 11 | 2.9% | no | 0 |  | 1 | 7941 | 0.1926
nl | Indo-European > Germanic > Northwest Germanic > West Germanic | 60 | 43 | 11 | 0.7% | yes | 0 | af 0.783 | 4 | 197753 | 0.2706
phl | Indo-European > Indo-Iranian | 46 | 43 | 11 | 29.6% | no | 0 | snk 0.565 | 1 | 2173 | 0.3287
ale | Eskimo-Aleut | 30 | 29 | 10 | 56.4% | no | 0 | ctd 0.581 | 2 | 1014 | 0.3993
lad | Indo-European > Italic > Romance > Ibero-Romance | 35 | 33 | 10 | 15.2% | no | 0 | aot 0.686 | 1 | 131 | 0.1397
lb | Indo-European > Germanic > Northwest Germanic > West Germanic | 42 | 35 | 10 | 5.2% | no | 0 | gml 0.571 | 1 | 3893 | 0.3576
nhx | Uto-Aztecan | 25 | 29 | 10 | 76.7% | no | 0 | nhg 0.72 | 1 | 145 | 0.1913
shn | Tai-Kadai | 31 | 41 | 10 | 62.0% | no | 0 |  | 1 | 2604 | 0.3348
smn | Uralic | 31 | 41 | 10 | 27.5% | no | 0 | se 0.806 | 1 | 1055 | 0.16
chb | Chibchan | 22 | 28 | 9 | 19.0% | no | 0 | ojp 0.545 | 1 | 99 | 0.1313
et | Uralic > Finnic | 27 | 36 | 9 | 1.0% | yes | 0 | vro 0.857 | 3 | 48943 | 0.2769
fa | Indo-European > Indo-Iranian > Iranian | 47 | 56 | 9 | 0.4% | no | 0 | lrc 0.702 | 2 | 16974 | 0.3943
fr-FR | Indo-European > Italic > Romance > Gallo-Romance | 92 | 46 | 9 | 6.0% | no | 0 | nrf 0.62 | 2 | 255160 | 0.0925
gwd | Afro-Asiatic | 33 | 34 | 9 | 9.9% | no | 0 | ssn 0.765 | 1 | 976 | 0.0481
lou | Indo-European > Italic > Romance | 36 | 37 | 9 | 12.2% | no | 0 | mfe 0.778 | 1 | 262 | 0.1953
mt | Afro-Asiatic > Semitic > Central Semitic | 30 | 37 | 9 | 5.3% | no | 0 | vo 0.633 | 2 | 24235 | 0.3056
nn | Indo-European > Germanic > Northwest Germanic > North Germanic | 42 | 38 | 9 | 0.5% | yes | 0 | sv 0.552 | 2 | 4922 | 0.2648
bbl | Nakh-Daghestanian | 37 | 43 | 8 | 34.0% | yes | 0 | lzz 0.919 | 1 | 414 | 0.3228
cic | Muskogean | 22 | 25 | 8 | 48.7% | yes | 0 | cho 0.833 | 1 | 394 | 0.1028
ckt | Chukotko-Kamchatkan | 26 | 31 | 8 | 13.9% | no | 0 | ess 0.483 | 1 | 993 | 0.0972
fy | Indo-European > Germanic > Northwest Germanic > West Germanic | 57 | 37 | 8 | 0.4% | yes | 0 | stq 0.526 | 2 | 11772 | 0.3243
haw | Austronesian > Malayo-Polynesian | 18 | 26 | 8 | 3.5% | no | 0 | mi 0.8 | 1 | 2145 | 0.0127
hi | Indo-European > Indo-Iranian > Indo-Aryan | 69 | 66 | 8 | 1.3% | no | 0 | bho 0.725 | 2 | 42853 | 0.2765
hil | Austronesian > Malayo-Polynesian | 20 | 27 | 8 | 4.9% | no | 0 | pam 0.952 | 1 | 466 | 0.0966
irk | Afro-Asiatic | 46 | 32 | 8 | 25.0% | no | 0 | bas 0.609 | 1 | 1117 | 0.201
kaw | Austronesian | 31 | 36 | 8 | 33.4% | no | 0 | ban 0.742 | 1 | 924 | 0.1472
lut | Salishan | 30 | 35 | 8 | 45.0% | yes | 0 | brx-x-proto-boro-garo 0.567 | 1 | 135 | 0.2259
nhg | Uto-Aztecan | 24 | 25 | 8 | 76.7% | no | 0 | nhx 0.72 | 1 | 295 | 0.2367
ps | Indo-European > Indo-Iranian > Iranian | 49 | 54 | 8 | 1.9% | no | 0 | bal 0.612 | 1 | 1075 | 0.2453
quz | Quechuan | 33 | 27 | 8 | 13.2% | no | 0 | aot 0.667 | 1 | 1853 | 0.3549
scn | Indo-European > Italic > Romance > Italo-Romance | 48 | 35 | 8 | 7.8% | no | 0 | it-IT-x-calabria 0.878 | 1 | 1396 | 0.1944
yrk | Uralic | 39 | 44 | 8 | 5.0% | yes | 0 | sia 0.821 | 2 | 1311 | 0.3852
arn | Araucanian | 27 | 30 | 7 | 4.3% | no | 0 | wes 0.741 | 1 | 1269 | 0.0112
bcl | Austronesian > Malayo-Polynesian | 28 | 28 | 7 | 0.9% | no | 0 | min 0.774 | 1 | 4793 | 0.0652
car | Cariban | 30 | 36 | 7 | 31.6% | yes | 0 | mwe 0.633 | 2 | 1423 | 0.35
ceb | Austronesian > Malayo-Polynesian | 23 | 27 | 7 | 7.2% | no | 0 | pam 0.913 | 1 | 3895 | 0.1058
ilo | Austronesian > Malayo-Polynesian | 23 | 27 | 7 | 6.4% | no | 0 | pam 0.913 | 1 | 931 | 0.1272
kab | Afro-Asiatic > Berber | 65 | 42 | 7 | 2.2% | no | 0 | ber 0.523 | 1 | 54545 | 0.2071
klj | Turkic | 33 | 39 | 7 | 47.7% | yes | 0 | slr 0.909 | 1 | 155 | 0.2995
ktz | Kxa | 81 | 30 | 7 | 10.4% | no | 0 | ngh 0.472 | 1 | 134 | 0.3464
mr | Indo-European > Indo-Iranian > Indo-Aryan | 73 | 70 | 7 | 0.4% | no | 0 | kok 0.699 | 2 | 21205 | 0.3063
nap | Indo-European > Italic > Romance > Italo-Romance | 42 | 28 | 7 | 7.8% | no | 0 | it-IT-x-puglia 0.854 | 1 | 198 | 0.2792
orv | Indo-European > Balto-Slavic > Slavic | 38 | 38 | 7 | 12.5% | no | 0 | rue 0.737 | 1 | 609 | 0.2203
rgn | Indo-European > Italic > Romance | 39 | 40 | 7 | 16.9% | no | 0 | vec 0.707 | 1 | 261 | 0.327
sdc | Indo-European > Italic > Romance | 31 | 29 | 7 | 24.7% | no | 0 | lld 0.774 | 1 | 321 | 0.1865
sq | Indo-European > Albanian | 36 | 34 | 7 | 0.2% | no | 0 | nup 0.611 | 2 | 16613 | 0.1432
srn | English Creole | 31 | 29 | 7 | 3.2% | no | 0 | bcl 0.71 | 1 | 702 | 0.045
sv | Indo-European > Germanic > Northwest Germanic > North Germanic | 58 | 36 | 7 | 0.3% | yes | 0 | da 0.619 | 4 | 50864 | 0.3717
tk | Turkic | 30 | 37 | 7 | 1.1% | yes | 0 | gag 0.806 | 2 | 6305 | 0.358
yol | Indo-European > Germanic > Northwest Germanic > West Germanic | 34 | 31 | 7 | 5.5% | no | 0 | kw 0.706 | 1 | 1972 | 0.3876
ast | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 57 | 38 | 6 | 0.7% | yes | 0 | an 0.845 | 1 | 4167 | 0.0505
bdq | Austroasiatic | 43 | 35 | 6 | 27.3% | yes | 0 | ts 0.477 | 1 | 198 | 0.3363
cnk | Sino-Tibetan | 34 | 28 | 6 | 61.1% | no | 0 | aot 0.912 | 1 | 342 | 0.502
cri | Indo-European > Italic > Romance > Ibero-Romance | 35 | 24 | 6 | 46.2% | no | 0 | aoa 0.722 | 1 | 13 | 0.2147
ddo | Nakh-Daghestanian | 41 | 32 | 6 | 19.5% | no | 0 | itl 0.366 | 1 | 871 | 0.109
dlm | Indo-European > Italic > Romance | 32 | 27 | 6 | 13.9% | no | 0 | rm 0.781 | 1 | 180 | 0.2476
es-ES | Indo-European > Italic > Romance > Ibero-Romance | 61 | 39 | 6 | 0.2% | yes | 0 | an 0.721 | 3 | 609092 | 0.0813
fpe | Indo-European > Germanic > Northwest Germanic > West Germanic | 31 | 31 | 6 | 95.4% | no | 0 | nfr 0.938 | 1 | 261 | 0.365
gl | Indo-European > Italic > Romance > Ibero-Romance | 74 | 36 | 6 | 0.7% | yes | 0 | ast 0.649 | 2 | 55603 | 0.0804
hr | Indo-European > Balto-Slavic > Slavic > South Slavic | 30 | 33 | 6 | 0.2% | no | 0 | bs 0.9 | 2 | 31238 | 0.3
is | Indo-European > Germanic > Northwest Germanic > North Germanic | 48 | 38 | 6 | 3.1% | yes | 0 | ofs 0.314 | 3 | 74841 | 0.3582
itl | Chukotko-Kamchatkan | 41 | 42 | 6 | 16.9% | no | 0 | ket 0.463 | 1 | 603 | 0.054
kl | Eskimo-Aleut | 25 | 27 | 6 | 0.5% | no | 0 | bi 0.72 | 1 | 1580 | 0.1765
liv | Uralic | 39 | 44 | 6 | 13.4% | yes | 0 | sgs 0.641 | 2 | 3522 | 0.1173
lmo | Indo-European > Italic > Romance > Italo-Romance | 27 | 41 | 6 | 5.9% | no | 0 | egl 0.519 | 1 | 406 | 0.2917
lmy | Austronesian > Malayo-Polynesian | 22 | 24 | 6 | 19.3% | no | 0 | iba 0.957 | 1 | 129 | 0.1695
mak | Austronesian | 25 | 28 | 6 | 7.1% | yes | 0 | gor 0.923 | 1 | 832 | 0.0206
pag | Austronesian > Malayo-Polynesian | 25 | 26 | 6 | 16.6% | no | 0 | ceb 0.88 | 1 | 227 | 0.1277
pam | Austronesian > Malayo-Polynesian | 21 | 25 | 6 | 3.8% | no | 0 | war 0.952 | 1 | 860 | 0.2861
ppl | Uto-Aztecan | 18 | 20 | 6 | 18.7% | no | 0 | yua 0.722 | 1 | 185 | 0.1322
si | Indo-European > Indo-Iranian > Indo-Aryan | 68 | 69 | 6 | 2.5% | no | 0 |  | 1 | 386 | 0.1394
sia | Uralic > Saami | 39 | 40 | 6 | 7.7% | no | 0 | evn 0.821 | 1 | 179 | 0.3686
su | Austronesian > Malayo-Polynesian | 27 | 29 | 6 | 0.5% | no | 0 | kge 0.893 | 1 | 396 | 0.0969
bjb | Pama-Nyungan | 26 | 17 | 5 | 2.2% | no | 0 | kld 0.615 | 1 | 136 | 0.1021
bo | Sino-Tibetan | 146 | 57 | 5 | 0.2% | no | 0 | dz 0.479 | 1 | 1564 | 0.3785
de-x-alemannic | Indo-European > Germanic > Northwest Germanic > West Germanic | 34 | 33 | 5 | 2.1% | yes | 0 | gwr 0.324 | 1 | 448 | 0.1734
ga | Indo-European > Celtic > Goidelic | 45 | 28 | 5 | 1.0% | yes | 0 | gd 0.356 | 2 | 11227 | 0.2989
hu | Uralic | 60 | 36 | 5 | 1.2% | yes | 0 | non 0.55 | 2 | 79325 | 0.0996
id | Austronesian | 32 | 30 | 5 | 0.2% | yes | 0 | min 0.906 | 3 | 41129 | 0.1312
it-IT | Indo-European > Italic > Romance > Italo-Romance | 71 | 37 | 5 | 2.6% | yes | 0 | co 0.634 | 1 | 4583 | 0.2341
ket | Yeniseian | 40 | 35 | 5 | 26.5% | no | 0 | gld 0.5 | 1 | 793 | 0.3457
nci | Uto-Aztecan | 0 | 25 | 5 | 0.8% | no | 0 |  | 1 | 839 | 0.1198
non | Indo-European > Germanic > Northwest Germanic > North Germanic | 51 | 39 | 5 | 3.5% | no | 0 | ofs 0.667 | 1 | 270 | 0.2365
pl | Indo-European > Balto-Slavic > Slavic > West Slavic | 44 | 37 | 5 | 0.1% | yes | 0 | szl 0.705 | 3 | 212105 | 0.2465
sga | Indo-European > Celtic | 49 | 28 | 5 | 0.3% | yes | 0 | mga 0.731 | 1 | 3700 | 0.0889
sjd | Uralic > Saami | 52 | 49 | 5 | 0.4% | yes | 0 | sia 0.75 | 2 | 1765 | 0.259
sl | Indo-European > Balto-Slavic > Slavic > South Slavic | 32 | 30 | 5 | 0.1% | no | 0 | hr 0.875 | 2 | 11742 | 0.3555
slr | Turkic | 32 | 35 | 5 | 31.6% | yes | 0 | klj 0.909 | 1 | 752 | 0.285
sw | Atlantic-Congo > Bantu | 35 | 28 | 5 | 0.5% | yes | 0 | rw 0.771 | 3 | 96949 | 0.3494
ur | Indo-European > Indo-Iranian > Indo-Aryan | 62 | 47 | 5 | 0.4% | no | 0 | pa-PK 0.629 | 1 | 6296 | 0.3077
uz | Turkic | 30 | 30 | 5 | 0.2% | yes | 0 | wes 0.833 | 2 | 78228 | 0.2458
aa | Afro-Asiatic > Cushitic | 31 | 26 | 4 | 0.3% | no | 0 | hay 0.774 | 1 | 1713 | 0.2151
acm | Afro-Asiatic > Semitic > Central Semitic | 44 | 34 | 4 | 26.9% | no | 0 | ayl 1.0 | 1 | 97 | 0.4249
af | Indo-European > Germanic > Northwest Germanic > West Germanic | 57 | 35 | 4 | 0.5% | no | 0 | nl-NL 0.649 | 1 | 2076 | 0.3615
ar | Afro-Asiatic > Semitic > Central Semitic | 16 | 48 | 4 | 0.1% | yes | 0 | acm 0.023 | 5 | 885708 | 0.3774
ar-SA-x-hejaz | Afro-Asiatic > Semitic > Central Semitic | 44 | 45 | 4 | 0.6% | yes | 0 | ayl 0.068 | 4 | 1959 | 0.3412
ar-SY | Afro-Asiatic > Semitic > Central Semitic | 4 | 48 | 4 | 3.7% | yes | 0 |  | 4 | 461 | 0.3895
ckb | Indo-European > Indo-Iranian > Iranian | 35 | 38 | 4 | 0.3% | no | 0 | sdh 0.8 | 2 | 27112 | 0.2607
de-DE | Indo-European > Germanic > Northwest Germanic > West Germanic | 61 | 34 | 4 | 1.3% | yes | 0 | nds 0.736 | 2 | 802642 | 0.3948
fo | Indo-European > Germanic > Northwest Germanic > North Germanic | 62 | 33 | 4 | 0.1% | yes | 0 | no 0.274 | 1 | 2957 | 0.1674
gu | Indo-European > Indo-Iranian > Indo-Aryan | 61 | 62 | 4 | 0.3% | no | 0 |  | 1 | 4082 | 0.1842
ht | French Creole | 31 | 29 | 4 | 0.5% | no | 0 | mfe 0.806 | 1 | 1691 | 0.0302
hy | Indo-European > Armenic | 39 | 42 | 4 | 0.8% | no | 0 | hyw 0.65 | 2 | 44405 | 0.1027
jam | English Creole | 34 | 27 | 4 | 4.2% | no | 0 | rhg 0.824 | 2 | 2251 | 0.2764
kas | Indo-European > Indo-Iranian > Indo-Aryan | 56 | 58 | 4 | 5.9% | no | 0 | bal 0.661 | 1 | 683 | 0.3231
ku | Indo-European > Indo-Iranian > Iranian | 31 | 35 | 4 | 0.3% | no | 0 | zza 0.765 | 1 | 2147 | 0.144
mh | Austronesian | 45 | 27 | 4 | 0.8% | no | 0 | uba 0.133 | 1 | 947 | 0.1182
ms | Austronesian | 0 | 29 | 4 | 6.0% | yes | 0 |  | 2 | 33102 | 0.1305
niv | Nivkh | 51 | 44 | 4 | 5.7% | no | 0 | sjd 0.654 | 2 | 1457 | 0.2767
pa | Indo-European > Indo-Iranian > Indo-Aryan | 61 | 58 | 4 | 0.3% | no | 0 |  | 2 | 5363 | 0.4454
pms | Indo-European > Italic > Romance > Italo-Romance | 19 | 30 | 4 | 37.6% | no | 0 | egl 0.474 | 1 | 899 | 0.1652
pt-PT | Indo-European > Italic > Romance > Ibero-Romance | 26 | 42 | 4 | 0.1% | yes | 0 | kea 0.295 | 5 | 166427 | 0.2477
ru | Indo-European > Balto-Slavic > Slavic > East Slavic | 36 | 37 | 4 | 0.2% | yes | 0 | myv 0.694 | 5 | 470125 | 0.3572
sc | Indo-European > Italic > Romance > Southern Romance | 43 | 31 | 4 | 1.5% | no | 0 | vec 0.698 | 1 | 703 | 0.063
sjs | Afro-Asiatic > Berber | 34 | 37 | 4 | 3.9% | no | 0 | shy 0.882 | 1 | 845 | 0.0467
sk | Indo-European > Balto-Slavic > Slavic > West Slavic | 61 | 47 | 4 | 0.2% | yes | 0 | dsb 0.443 | 2 | 31837 | 0.1346
tl | Austronesian | 27 | 30 | 4 | 2.3% | no | 0 | ban 0.786 | 1 | 25857 | 0.1179
tn | Atlantic-Congo > Bantu | 38 | 25 | 4 | 1.0% | no | 0 | zom 0.526 | 1 | 2271 | 0.4003
tr | Turkic | 29 | 34 | 4 | 0.6% | yes | 0 | gag 0.839 | 3 | 61340 | 0.1372
wa | Indo-European > Italic > Romance | 54 | 39 | 4 | 0.3% | no | 0 | pcd 0.556 | 1 | 2348 | 0.1443
yi | Indo-European > Germanic > Northwest Germanic > West Germanic | 50 | 39 | 4 | 8.4% | yes | 0 | he 0.212 | 1 | 4051 | 0.2042
ace | Austronesian | 29 | 28 | 3 | 29.4% | no | 0 | mad 0.733 | 1 | 267 | 0.1102
ady | Abkhaz-Adyge | 64 | 34 | 3 | 50.3% | no | 0 | kbd 0.812 | 1 | 928 | 0.1684
ar-EG | Afro-Asiatic > Semitic > Central Semitic | 25 | 47 | 3 | 2.2% | yes | 0 | acm 0.023 | 4 | 648 | 0.3692
ar-MA | Afro-Asiatic > Semitic > Central Semitic | 13 | 45 | 3 | 1.3% | yes | 0 | sdh 0.029 | 4 | 1877 | 0.3026
ar-x-gulf | Afro-Asiatic > Semitic > Central Semitic | 44 | 43 | 3 | 1.9% | yes | 0 | ug 0.159 | 3 | 654 | 0.4273
as | Indo-European > Indo-Iranian > Indo-Aryan | 64 | 64 | 3 | 1.9% | no | 0 | ctg 0.375 | 2 | 8309 | 0.2436
bn | Indo-European > Indo-Iranian > Indo-Aryan | 61 | 61 | 3 | 0.0% | no | 0 | as 0.625 | 2 | 36788 | 0.3162
ca-x-balear | Indo-European > Italic > Romance | 3 | 40 | 3 | 1.9% | yes | 0 |  | 1 | 160 | 0.136
ce | Nakh-Daghestanian | 43 | 30 | 3 | 7.3% | no | 0 | kum 0.674 | 1 | 461 | 0.2541
cho | Muskogean | 24 | 22 | 3 | 12.3% | no | 0 | cic 0.833 | 1 | 138 | 0.4167
cop | Afro-Asiatic > Egyptian | 34 | 33 | 3 | 3.5% | no | 0 |  | 1 | 591 | 0.3667
el | Indo-European > Hellenic | 64 | 38 | 3 | 0.1% | yes | 0 | pnt 0.516 | 2 | 25091 | 0.2653
enm | Indo-European > Germanic > Northwest Germanic > West Germanic | 44 | 28 | 3 | 24.0% | no | 0 | goh 0.568 | 1 | 6466 | 0.2981
gld | Tungusic | 36 | 33 | 3 | 21.8% | no | 0 | ket 0.5 | 1 | 887 | 0.1532
grc | Indo-European > Hellenic | 67 | 60 | 3 | 0.8% | no | 0 | el-CY 0.254 | 1 | 58095 | 0.148
guw | Atlantic-Congo | 39 | 34 | 3 | 0.4% | no | 0 | fon 0.718 | 1 | 595 | 0.4311
ha | Afro-Asiatic > Chadic | 53 | 33 | 3 | 0.5% | no | 0 | dbq 0.509 | 2 | 5576 | 0.534
km | Austroasiatic | 374 | 74 | 3 | 0.4% | yes | 0 |  | 2 | 9889 | 0.3335
kv | Uralic | 74 | 37 | 3 | 0.5% | no | 0 | koi 1.0 | 1 | 906 | 0.157
ky | Turkic | 34 | 36 | 3 | 11.6% | yes | 0 | alt 0.829 | 2 | 11478 | 0.2217
lg | Atlantic-Congo > Bantu | 32 | 27 | 3 | 13.6% | no | 0 | gog 0.875 | 1 | 103344 | 0.1107
lij | Indo-European > Italic > Romance > Italo-Romance | 96 | 46 | 3 | 0.2% | yes | 0 | nrf 0.406 | 2 | 4233 | 0.1157
lt | Indo-European > Balto-Slavic > Eastern Baltic | 35 | 35 | 3 | 0.1% | no | 0 | ltg 0.649 | 2 | 29411 | 0.3906
ml | Dravidian | 72 | 74 | 3 | 0.4% | no | 0 |  | 2 | 15928 | 0.2893
ngh | Tuu | 89 | 35 | 3 | 1.2% | no | 0 | ktz 0.472 | 1 | 263 | 0.2616
ny | Atlantic-Congo > Bantu | 47 | 28 | 3 | 0.5% | no | 0 | ts 0.66 | 1 | 1564 | 0.3431
or | Indo-European > Indo-Iranian > Indo-Aryan | 62 | 63 | 3 | 0.2% | no | 0 |  | 2 | 14134 | 0.2689
osp | Indo-European > Italic > Romance | 32 | 29 | 3 | 0.6% | yes | 0 | nov 0.688 | 1 | 667 | 0.1605
osx | Indo-European > Germanic > Northwest Germanic > West Germanic | 31 | 23 | 3 | 8.8% | no | 0 | goh 0.763 | 1 | 243 | 0.3918
pt-BR | Indo-European > Italic > Romance > Ibero-Romance | 23 | 41 | 3 | 0.2% | yes | 0 | lfn 0.348 | 7 | 193495 | 0.3896
ro-RO | Indo-European > Italic > Romance > Eastern Romance | 41 | 34 | 3 | 6.1% | no | 0 | rup 0.634 | 2 | 74686 | 0.2644
sr | Indo-European > Balto-Slavic > Slavic > South Slavic | 60 | 60 | 3 | 0.1% | no | 0 | mk 0.467 | 2 | 13462 | 0.3298
stq | Indo-European > Germanic > Northwest Germanic > West Germanic | 52 | 29 | 3 | 9.3% | no | 0 | frr 0.868 | 1 | 818 | 0.373
te | Dravidian | 63 | 66 | 3 | 0.9% | no | 0 |  | 1 | 5101 | 0.099
tg | Indo-European > Indo-Iranian > Iranian | 36 | 38 | 3 | 0.5% | no | 0 | alt 0.778 | 1 | 3245 | 0.0296
ulw | Misumalpan | 20 | 20 | 3 | 17.5% | yes | 0 | mdh 0.85 | 1 | 102 | 0.0888
vi | Austroasiatic | 891 | 89 | 3 | 0.1% | no | 0 | mtq 0.024 | 2 | 73374 | 0.5596
wau | Arawakan | 24 | 19 | 3 | 37.7% | no | 0 | ulw 0.625 | 1 | 146 | 0.2968
yux | Yukaghir | 34 | 27 | 3 | 11.8% | no | 0 | sia 0.769 | 1 | 242 | 0.2975
zza | Indo-European > Indo-Iranian > Iranian | 34 | 34 | 3 | 0.9% | no | 0 | diq 0.765 | 1 | 196 | 0.3606
ang | Indo-European > Germanic > Northwest Germanic > West Germanic | 55 | 26 | 2 | 1.6% | no | 0 | ofs 0.745 | 1 | 54696 | 0.2103
ar-AE | Afro-Asiatic > Semitic > Central Semitic | 0 | 40 | 2 | 50.0% | yes | 0 |  | 2 | 40 | 0.0441
ar-BH | Afro-Asiatic > Semitic > Central Semitic | 0 | 40 | 2 | 45.0% | yes | 0 |  | 2 | 40 | 0.041
ar-DZ | Afro-Asiatic > Semitic > Central Semitic | 23 | 40 | 2 | 29.3% | yes | 0 | sdh 0.029 | 3 | 41 | 0.7143
ar-IQ | Afro-Asiatic > Semitic > Central Semitic | 37 | 40 | 2 | 30.8% | yes | 0 | arb 0.126 | 3 | 52 | 0.2907
ar-IQ-x-qeltu | Afro-Asiatic > Semitic > Central Semitic | 1 | 38 | 2 | 23.1% | yes | 0 |  | 3 | 52 | 0.3417
ar-JO | Afro-Asiatic > Semitic > Central Semitic | 2 | 46 | 2 | 0.7% | yes | 0 |  | 4 | 2566 | 0.3718
ar-KW | Afro-Asiatic > Semitic > Central Semitic | 0 | 40 | 2 | 30.0% | yes | 0 |  | 2 | 40 | 0.0237
ar-LB | Afro-Asiatic > Semitic > Central Semitic | 71 | 36 | 2 | 30.0% | yes | 0 | arb 0.004 | 2 | 40 | 0.0258
ar-LY | Afro-Asiatic > Semitic > Central Semitic | 37 | 35 | 2 | 39.1% | yes | 0 | sdh 0.027 | 3 | 46 | 0.2042
ar-MR | Afro-Asiatic > Semitic > Central Semitic | 45 | 37 | 2 | 27.6% | yes | 0 | arb 0.126 | 3 | 54 | 0.3988
ar-NG | Afro-Asiatic > Semitic > Central Semitic | 33 | 33 | 2 | 30.4% | yes | 0 | acm 0.023 | 3 | 46 | 0.2444
ar-OM | Afro-Asiatic > Semitic > Central Semitic | 34 | 38 | 2 | 45.0% | yes | 0 | ayl 0.136 | 2 | 40 | 0.0077
ar-PS | Afro-Asiatic > Semitic > Central Semitic | 3 | 39 | 2 | 31.8% | yes | 0 |  | 3 | 44 | 0.1667
ar-QA | Afro-Asiatic > Semitic > Central Semitic | 0 | 39 | 2 | 25.0% | yes | 0 |  | 2 | 40 | 0.0264
ar-SA-x-najd | Afro-Asiatic > Semitic > Central Semitic | 22 | 40 | 2 | 18.9% | yes | 0 | ayl 0.068 | 3 | 65 | 0.1491
ar-SA-x-qassim | Afro-Asiatic > Semitic > Central Semitic | 2 | 41 | 2 | 26.9% | yes | 0 |  | 3 | 52 | 0.1327
ar-SA-x-rijal-alma | Afro-Asiatic > Semitic > Central Semitic | 21 | 40 | 2 | 29.2% | yes | 0 | arb 0.042 | 3 | 48 | 0.2454
ar-SA-x-sharqiyya | Afro-Asiatic > Semitic > Central Semitic | 1 | 38 | 2 | 34.8% | yes | 0 |  | 3 | 46 | 0.1944
ar-SD | Afro-Asiatic > Semitic > Central Semitic | 26 | 37 | 2 | 55.0% | yes | 0 | ayl 0.045 | 2 | 40 | 0.0274
ar-TD | Afro-Asiatic > Semitic > Central Semitic | 36 | 36 | 2 | 30.0% | yes | 0 | ayl 0.136 | 2 | 40 | 0.0346
ar-TN | Afro-Asiatic > Semitic > Central Semitic | 33 | 37 | 2 | 49.0% | yes | 0 | arb 0.13 | 3 | 49 | 0.3059
ar-YE | Afro-Asiatic > Semitic > Central Semitic | 42 | 39 | 2 | 32.7% | yes | 0 | arb 0.13 | 3 | 55 | 0.1802
ar-x-levantine | Afro-Asiatic > Semitic > Central Semitic | 38 | 37 | 2 | 35.0% | yes | 0 | ayl 0.045 | 2 | 40 | 0.0105
ar-x-maghrebi | Afro-Asiatic > Semitic > Central Semitic | 44 | 36 | 2 | 35.0% | yes | 0 | sdh 0.068 | 2 | 40 | 0.0044
ar-x-mashriqi | Afro-Asiatic > Semitic > Central Semitic | 43 | 39 | 2 | 35.0% | yes | 0 | ckb 0.07 | 2 | 40 | 0.0175
ar-x-peninsular | Afro-Asiatic > Semitic > Central Semitic | 42 | 40 | 2 | 35.0% | yes | 0 | acm 0.114 | 2 | 40 | 0.0122
arb | Afro-Asiatic > Semitic > Central Semitic | 239 | 45 | 2 | 25.0% | yes | 0 | ayl 0.163 | 2 | 40 | 0.019
av | Nakh-Daghestanian | 56 | 36 | 2 | 2.5% | no | 0 | lbe 0.786 | 1 | 954 | 0.099
br | Indo-European > Celtic > Brythonic | 43 | 29 | 2 | 0.8% | yes | 0 | mfe 0.628 | 1 | 803 | 0.3499
ca | Indo-European > Italic > Romance | 4 | 39 | 2 | 0.4% | yes | 0 |  | 4 | 145702 | 0.2576
crs | Indo-European > Italic > Romance > Gallo-Romance | 28 | 24 | 2 | 0.2% | no | 0 | nga 0.828 | 1 | 1874 | 0.2114
da | Indo-European > Germanic > Northwest Germanic > North Germanic | 63 | 31 | 2 | 0.4% | yes | 0 | sv 0.619 | 2 | 6564 | 0.4626
dar | Nakh-Daghestanian | 53 | 34 | 2 | 5.8% | no | 0 | av 0.714 | 1 | 1056 | 0.0691
enf | Uralic | 57 | 34 | 2 | 0.5% | no | 0 | sel 0.702 | 1 | 838 | 0.0892
evn | Tungusic | 39 | 36 | 2 | 4.5% | yes | 0 | sia 0.821 | 2 | 1277 | 0.2447
ext-PT-x-barrancos | Indo-European > Italic > Romance > Ibero-Romance | 25 | 36 | 2 | 1.4% | yes | 0 | aoa 0.167 | 3 | 1538 | 0.2801
fax | Indo-European > Italic > Romance > Ibero-Romance | 58 | 31 | 2 | 1.2% | no | 0 | pt-BR-x-sul 0.81 | 1 | 655 | 0.1044
gul | Indo-European > Germanic > Northwest Germanic > West Germanic | 33 | 25 | 2 | 4.9% | no | 0 | yol 0.676 | 1 | 207 | 0.4674
he | Afro-Asiatic > Semitic > Central Semitic | 113 | 40 | 2 | 1.3% | yes | 0 |  | 2 | 2905 | 0.362
hsb | Indo-European > Balto-Slavic > Slavic > West Slavic | 36 | 35 | 2 | 0.0% | yes | 0 | dsb 0.919 | 2 | 6928 | 0.3177
iba | Austronesian > Malayo-Polynesian | 23 | 23 | 2 | 1.4% | no | 0 | lmy 0.957 | 1 | 571 | 0.1655
kld | Pama-Nyungan | 21 | 15 | 2 | 2.1% | yes | 0 | ulw 0.667 | 1 | 515 | 0.055
kn | Dravidian | 64 | 66 | 2 | 0.1% | no | 0 |  | 1 | 1706 | 0.2689
lbe | Nakh-Daghestanian | 53 | 33 | 2 | 0.6% | no | 0 | av 0.786 | 1 | 1048 | 0.0387
lez | Nakh-Daghestanian | 43 | 32 | 2 | 1.8% | no | 0 | dar 0.698 | 1 | 969 | 0.1329
lv | Indo-European > Balto-Slavic > Eastern Baltic | 33 | 34 | 2 | 0.2% | yes | 0 | sgs 0.788 | 1 | 1213 | 0.1901
lzz | Kartvelian | 34 | 35 | 2 | 10.5% | no | 0 | ka 0.941 | 1 | 262 | 0.2017
mfe | Indo-European > Italic > Romance | 30 | 26 | 2 | 0.9% | no | 0 | ht 0.806 | 1 | 206 | 0.1238
mwl | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 12 | 34 | 2 | 0.7% | yes | 0 | lfn 0.182 | 3 | 1215 | 0.1317
nio | Uralic | 55 | 30 | 2 | 6.8% | no | 0 | enf 0.649 | 1 | 1024 | 0.0972
nv | Athabaskan-Eyak-Tlingit | 64 | 33 | 2 | 0.9% | no | 0 | xsl 0.356 | 1 | 989 | 0.2514
oji | Algic | 26 | 21 | 2 | 5.9% | no | 0 | bdr 0.593 | 1 | 136 | 0.3108
pt-PT-x-viana | Indo-European > Italic > Romance > Ibero-Romance | 2 | 38 | 2 | 4.2% | yes | 0 |  | 2 | 24 | 0.3655
rif | Afro-Asiatic > Berber | 50 | 40 | 2 | 22.8% | no | 0 | zen 0.48 | 1 | 1533 | 0.0929
rw | Atlantic-Congo > Bantu | 35 | 26 | 2 | 7.7% | no | 0 | lua 0.8 | 1 | 381086 | 0.1388
se | Uralic > Saami | 29 | 31 | 2 | 0.3% | no | 0 | smn 0.806 | 1 | 4125 | 0.2749
sid | Afro-Asiatic > Cushitic | 37 | 27 | 2 | 7.7% | no | 0 | om 0.784 | 1 | 297 | 0.0731
srs | Athabaskan-Eyak-Tlingit | 36 | 23 | 2 | 3.6% | no | 0 | fmp 0.639 | 1 | 137 | 0.1773
ug | Turkic | 42 | 34 | 2 | 35.0% | no | 0 | sdh 0.5 | 2 | 43147 | 0.1285
vep | Uralic | 28 | 30 | 2 | 10.9% | no | 0 | vro 0.929 | 1 | 1004 | 0.2065
war | Austronesian > Malayo-Polynesian | 21 | 21 | 2 | 1.3% | no | 0 | pam 0.952 | 1 | 380 | 0.1478
ain | Ainu | 28 | 21 | 1 | 0.7% | yes | 0 | bcl 0.679 | 1 | 858 | 0.02
akk | Afro-Asiatic > Semitic | 34 | 32 | 1 | 1.3% | no | 0 | phn 0.824 | 1 | 671 | 0.0144
an | Indo-European > Italic > Romance > Ibero-Romance | 58 | 31 | 1 | 0.1% | yes | 0 | ast 0.845 | 1 | 902 | 0.058
apw | Athabaskan-Eyak-Tlingit | 123 | 36 | 1 | 0.7% | no | 0 | xsl 0.398 | 1 | 147 | 0.3076
az | Turkic | 32 | 33 | 1 | 0.4% | yes | 0 | klj 0.909 | 1 | 434 | 0.244
ban | Austronesian | 28 | 22 | 1 | 5.0% | no | 0 | min 0.871 | 1 | 299 | 0.163
bg | Indo-European > Balto-Slavic > Slavic > South Slavic | 37 | 30 | 1 | 0.0% | no | 0 | orv 0.711 | 1 | 18447 | 0.198
bua | Mongolic | 44 | 35 | 1 | 0.6% | yes | 0 | sia 0.727 | 2 | 1314 | 0.3605
co | Indo-European > Italic > Romance > Italo-Romance | 48 | 28 | 1 | 0.2% | no | 0 | it-IT-x-abruzzo 0.938 | 1 | 459 | 0.1955
dsb | Indo-European > Balto-Slavic > Slavic > West Slavic | 37 | 35 | 1 | 0.0% | yes | 0 | hsb 0.919 | 1 | 2010 | 0.1487
dum | Indo-European > Germanic > Northwest Germanic > West Germanic | 37 | 24 | 1 | 0.4% | yes | 0 | gml 0.622 | 1 | 197 | 0.2776
eo | Constructed | 28 | 29 | 1 | 0.0% | yes | 0 | ist 0.75 | 2 | 64490 | 0.0328
fro | Indo-European > Italic > Romance | 39 | 29 | 1 | 0.1% | no | 0 | cbk-zam 0.59 | 1 | 663 | 0.2738
gd | Indo-European > Celtic > Goidelic | 40 | 26 | 1 | 0.3% | yes | 0 | ga 0.356 | 1 | 3719 | 0.3202
gv | Indo-European > Celtic > Goidelic | 40 | 26 | 1 | 2.2% | no | 0 | aot 0.6 | 1 | 690 | 0.3631
huu | Huitotoan | 30 | 25 | 1 | 0.2% | no | 0 | ctd 0.613 | 1 | 437 | 0.035
kca | Uralic | 50 | 34 | 1 | 0.1% | no | 0 | sel 0.691 | 1 | 863 | 0.0232
kix | Sino-Tibetan | 60 | 44 | 1 | 0.1% | no | 0 | ts 0.35 | 1 | 4240 | 0.0788
ko | Koreanic | 118 | 1056 | 1 | 0.0% | no | 0 |  | 2 | 68570 | 0.2319
krl | Uralic > Finnic | 9 | 28 | 1 | 0.2% | yes | 0 | vot 0.538 | 1 | 641 | 0.0519
kwk | Wakashan | 79 | 36 | 1 | 0.9% | no | 0 | irk 0.304 | 1 | 116 | 0.007
kxd | Austronesian > Malayo-Polynesian | 30 | 22 | 1 | 0.3% | no | 0 | min 0.903 | 1 | 318 | 0.0235
lo | Tai-Kadai | 66 | 54 | 1 | 0.1% | no | 0 |  | 1 | 2308 | 0.3632
lsi | Sino-Tibetan | 53 | 25 | 1 | 1.4% | no | 0 | aot 0.453 | 1 | 96 | 0.4727
mch | Cariban | 20 | 21 | 1 | 7.2% | no | 0 | ppl 0.7 | 1 | 1746 | 0.3011
mdf | Uralic | 35 | 33 | 1 | 0.3% | no | 0 | myv 0.714 | 1 | 330 | 0.2212
mdh | Austronesian > Malayo-Polynesian | 20 | 20 | 1 | 1.9% | no | 0 | lmy 0.864 | 1 | 205 | 0.0793
mhr | Uralic > Mari | 72 | 36 | 1 | 85.2% | no | 0 | udm 0.611 | 1 | 992 | 0.1736
mi | Austronesian > Malayo-Polynesian | 20 | 20 | 1 | 0.2% | no | 0 | haw 0.8 | 1 | 1003 | 0.0719
mnc | Tungusic | 29 | 26 | 1 | 0.1% | no | 0 |  | 1 | 1205 | 0.1411
mns | Uralic | 64 | 34 | 1 | 10.7% | yes | 0 | kca 0.609 | 1 | 992 | 0.1024
mrj | Uralic > Mari | 40 | 38 | 1 | 2.4% | no | 0 | alt 0.725 | 1 | 1018 | 0.0075
mwl-x-sendim | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 5 | 28 | 1 | 0.9% | yes | 0 |  | 3 | 110 | 0.3258
nmy | Sino-Tibetan | 132 | 59 | 1 | 0.3% | no | 0 | zom 0.159 | 1 | 354 | 0.1091
nrf | Indo-European > Italic > Romance > Gallo-Romance | 92 | 38 | 1 | 2.1% | no | 0 | fr-FR 0.62 | 1 | 143 | 0.2557
ota | Turkic | 41 | 30 | 1 | 3.8% | no | 0 | lrc 0.659 | 1 | 161 | 0.3536
pbv | Austroasiatic | 37 | 23 | 1 | 4.0% | no | 0 | gul 0.568 | 1 | 101 | 0.3358
pdc | Indo-European > Germanic | 37 | 24 | 1 | 0.6% | no | 0 | gul 0.514 | 1 | 405 | 0.335
pt-AO | Indo-European > Italic > Romance > Ibero-Romance | 2 | 37 | 1 | 0.0% | yes | 0 |  | 2 | 53171 | 0.2499
pt-BR-x-caipira | Indo-European > Italic > Romance > Ibero-Romance | 57 | 33 | 1 | 3.9% | yes | 0 | fax 0.793 | 2 | 51 | 0.3147
pt-BR-x-rj | Indo-European > Italic > Romance > Ibero-Romance | 57 | 37 | 1 | 0.0% | yes | 0 | fax 0.793 | 2 | 53167 | 0.1901
pt-BR-x-sp | Indo-European > Italic > Romance > Ibero-Romance | 57 | 37 | 1 | 0.0% | yes | 0 | fax 0.793 | 2 | 53167 | 0.1796
pt-MZ | Indo-European > Italic > Romance > Ibero-Romance | 4 | 37 | 1 | 0.0% | yes | 0 |  | 2 | 53167 | 0.1699
pt-PT-x-lisbon | Indo-European > Italic > Romance > Ibero-Romance | 2 | 39 | 1 | 0.0% | yes | 0 |  | 5 | 53253 | 0.2921
pt-PT-x-minho | Indo-European > Italic > Romance > Ibero-Romance | 3 | 35 | 1 | 6.9% | yes | 0 |  | 2 | 29 | 0.3181
pt-PT-x-porto | Indo-European > Italic > Romance > Ibero-Romance | 2 | 40 | 1 | 2.3% | yes | 0 |  | 4 | 82 | 0.4227
pt-TL | Indo-European > Italic > Romance > Ibero-Romance | 6 | 37 | 1 | 0.0% | yes | 0 |  | 2 | 53167 | 0.3643
sa | Indo-European > Indo-Iranian > Indo-Aryan | 65 | 60 | 1 | 0.3% | no | 0 | mai 0.754 | 1 | 9796 | 0.3089
sah | Turkic | 50 | 32 | 1 | 0.0% | no | 0 | xal 0.68 | 2 | 12227 | 0.2492
sce | Mongolic | 31 | 26 | 1 | 12.4% | no | 0 | nhb 0.677 | 1 | 168 | 0.3655
sms | Uralic > Saami | 60 | 39 | 1 | 0.1% | yes | 0 | bs 0.4 | 2 | 1174 | 0.22
tru | Afro-Asiatic > Semitic > Central Semitic | 23 | 24 | 1 | 2.6% | no | 0 | syc 0.957 | 1 | 168 | 0.4799
tzm | Afro-Asiatic > Berber | 34 | 33 | 1 | 0.1% | no | 0 | zgh 0.971 | 1 | 658 | 0.016
uk | Indo-European > Balto-Slavic > Slavic > East Slavic | 43 | 35 | 1 | 0.0% | yes | 0 | rue 0.698 | 3 | 103312 | 0.2672
vo | Constructed | 28 | 29 | 1 | 0.4% | no | 0 | ban 0.786 | 1 | 442 | 0.0185
wlm | Indo-European > Celtic > Brythonic | 30 | 23 | 1 | 0.2% | yes | 0 | gml 0.645 | 1 | 403 | 0.2498
xaa | Afro-Asiatic > Semitic > Central Semitic | 0 | 39 | 1 | 10.0% | yes | 0 |  | 1 | 20 | 0.0
xal | Mongolic | 45 | 34 | 1 | 4.4% | no | 0 | sah 0.68 | 1 | 318 | 0.2813
ykg | Yukaghir | 45 | 28 | 1 | 0.4% | no | 0 | bua 0.556 | 1 | 813 | 0.3616
za | Tai-Kadai | 37 | 27 | 1 | 0.7% | no | 0 | zom 0.378 | 1 | 1682 | 0.2124
aii | Afro-Asiatic > Semitic > Central Semitic | 22 | 22 | 0 |  | no | 0 | syc 0.864 | 1 | 4836 | 0.3765
aot | Sino-Tibetan | 33 | 21 | 0 |  | no | 0 | cnk 0.912 | 1 | 181 | 0.1367
ar-SA-x-dawasir | Afro-Asiatic > Semitic > Central Semitic | 1 | 16 | 0 |  | yes | 0 |  | 1 | 5 | 0.08
ar-SA-x-tihama-qahtan | Afro-Asiatic > Semitic > Central Semitic | 4 | 25 | 0 |  | yes | 0 |  | 1 | 16 | 0.1084
ast-PT-x-guadramil | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 0 | 24 | 0 |  | yes | 0 |  | 1 | 20 | 0.0
ast-PT-x-medieval | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 15 | 24 | 0 |  | yes | 0 | pov 0.2 | 1 | 20 | 0.0
ast-PT-x-rionor | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 52 | 24 | 0 |  | yes | 0 | pt-BR-x-sul 0.684 | 1 | 20 | 0.0
ayl | Afro-Asiatic > Semitic > Central Semitic | 44 | 28 | 0 |  | no | 0 | acm 1.0 | 1 | 156 | 0.3799
ba | Turkic | 60 | 41 | 0 |  | yes | 0 | kk 0.6 | 2 | 70699 | 0.4047
bbn | Austronesian > Malayo-Polynesian | 22 | 18 | 0 |  | no | 0 | lmy 0.909 | 1 | 194 | 0.0689
be | Indo-European > Balto-Slavic > Slavic > East Slavic | 110 | 33 | 0 |  | no | 0 | mhr 0.309 | 2 | 160758 | 0.1276
ca-x-occidental | Indo-European > Italic > Romance | 1 | 37 | 0 |  | yes | 0 |  | 1 | 160 | 0.0822
ca-x-valencia | Indo-European > Italic > Romance | 0 | 36 | 0 |  | yes | 0 |  | 1 | 160 | 0.0677
crk | Algic | 17 | 17 | 0 |  | yes | 0 | atj 0.789 | 1 | 159 | 0.3174
cs | Indo-European > Balto-Slavic > Slavic > West Slavic | 56 | 37 | 0 |  | yes | 0 | sk 0.639 | 1 | 44148 | 0.068
csb | Indo-European > Balto-Slavic > Slavic > West Slavic | 39 | 34 | 0 |  | yes | 0 | szl 0.78 | 1 | 2825 | 0.1663
cv | Turkic | 37 | 27 | 0 |  | yes | 0 | alt 0.703 | 1 | 6779 | 0.1264
dng | Sino-Tibetan > Sinitic | 56 | 36 | 0 |  | no | 0 | bua 0.286 | 1 | 269 | 0.4087
dv | Indo-European > Indo-Iranian > Indo-Aryan | 51 | 50 | 0 |  | no | 0 |  | 2 | 18309 | 0.0891
dz | Sino-Tibetan | 132 | 53 | 0 |  | no | 0 |  | 1 | 230 | 0.3392
ee | Atlantic-Congo | 126 | 36 | 0 |  | no | 0 | gen 0.262 | 1 | 247 | 0.4445
egy | Afro-Asiatic > Egyptian | 25 | 25 | 0 |  | no | 0 | khq 0.538 | 1 | 2185 | 0.0183
es-AR | Indo-European > Italic > Romance > Ibero-Romance | 4 | 22 | 0 |  | yes | 0 |  | 1 | 29 | 0.0138
es-MX | Indo-European > Italic > Romance > Ibero-Romance | 3 | 29 | 0 |  | yes | 0 |  | 1 | 595885 | 0.0397
ett | Tyrsenian | 26 | 26 | 0 |  | no | 0 |  | 1 | 207 | 0.1444
gmh | Indo-European > Germanic > Northwest Germanic | 42 | 29 | 0 |  | yes | 0 | enm 0.523 | 1 | 1516 | 0.2938
gml | Indo-European > Germanic > Northwest Germanic > West Germanic | 31 | 22 | 0 |  | yes | 0 | rhg 0.719 | 1 | 143 | 0.4547
gn | Tupian | 39 | 36 | 0 |  | yes | 0 | tpw 0.59 | 2 | 4611 | 0.1675
got | Indo-European > Germanic > East Germanic | 32 | 24 | 0 |  | no | 0 |  | 1 | 1816 | 0.0667
gwc | Indo-European > Indo-Iranian > Indo-Aryan | 68 | 34 | 0 |  | no | 0 | pa-PK 0.544 | 1 | 165 | 0.417
hrx | Indo-European > Germanic > Northwest Germanic | 75 | 29 | 0 |  | yes | 0 | nds 0.453 | 1 | 2002 | 0.0821
hts | Hadza | 64 | 30 | 0 |  | no | 0 | lus 0.375 | 1 | 329 | 0.0224
ia | Constructed | 30 | 25 | 0 |  | no | 0 | io 0.833 | 1 | 443 | 0.0646
inh | Nakh-Daghestanian | 53 | 31 | 0 |  | no | 0 | lbe 0.642 | 1 | 284 | 0.1632
io | Constructed | 29 | 26 | 0 |  | yes | 0 | ia 0.833 | 1 | 6815 | 0.0974
izh | Uralic > Finnic | 6 | 27 | 0 |  | yes | 0 |  | 1 | 7886 | 0.0092
jv | Austronesian | 31 | 22 | 0 |  | no | 0 | su 0.774 | 1 | 96 | 0.218
ka | Kartvelian | 33 | 33 | 0 |  | no | 0 | lzz 0.941 | 1 | 79887 | 0.2337
kgp | Nuclear-Macro-Je | 28 | 27 | 0 |  | no | 0 | yrl 0.516 | 1 | 106 | 0.2351
ki | Atlantic-Congo | 27 | 21 | 0 |  | no | 0 | nnb 0.704 | 1 | 1025 | 0.3972
kk | Turkic | 40 | 40 | 0 |  | yes | 0 | tt 0.875 | 2 | 2117 | 0.3858
koi | Uralic | 74 | 30 | 0 |  | no | 0 | kv 1.0 | 1 | 229 | 0.092
kru | Dravidian | 59 | 45 | 0 |  | no | 0 | bho 0.797 | 1 | 187 | 0.1947
mcm | Indo-European > Italic > Romance > Ibero-Romance | 30 | 25 | 0 |  | yes | 0 | kcn 0.853 | 1 | 33 | 0.1146
mga | Indo-European > Celtic > Goidelic | 52 | 23 | 0 |  | yes | 0 | sga 0.731 | 1 | 328 | 0.0594
mic | Algic | 24 | 16 | 0 |  | no | 0 | war 0.708 | 1 | 203 | 0.2922
mk | Indo-European > Balto-Slavic > Slavic > South Slavic | 31 | 31 | 0 |  | no | 0 | orv 0.658 | 1 | 10750 | 0.0221
mn | Mongolic | 70 | 35 | 0 |  | no | 0 | dng 0.243 | 2 | 19120 | 0.2054
mqs | North Halmahera | 23 | 22 | 0 |  | no | 0 | tft 1.0 | 1 | 790 | 0.0495
mtq | Austroasiatic | 95 | 65 | 0 |  | no | 0 | bdq 0.284 | 1 | 194 | 0.3412
mwl-x-ifanes | Indo-European > Italic > Romance > Ibero-Romance > Asturleonese | 0 | 26 | 0 |  | yes | 0 |  | 3 | 26 | 0.5
mww | Hmong-Mien | 66 | 26 | 0 |  | no | 0 | lus 0.242 | 1 | 489 | 0.0107
myv | Uralic | 32 | 32 | 0 |  | no | 0 | yux 0.765 | 1 | 6442 | 0.0944
nds | Indo-European > Germanic > Northwest Germanic > West Germanic | 72 | 35 | 0 |  | yes | 0 | de-DE 0.736 | 1 | 308 | 0.2231
ne | Indo-European > Indo-Iranian > Indo-Aryan | 62 | 58 | 0 |  | no | 0 | awa 0.597 | 1 | 2052 | 0.1191
new | Sino-Tibetan | 42 | 51 | 0 |  | no | 1 | mr 0.26 | 1 | 416 | 0.0282
nup | Atlantic-Congo | 30 | 24 | 0 |  | no | 0 | bom 0.844 | 1 | 393 | 0.3979
oc | Indo-European > Italic > Romance > Gallo-Romance | 68 | 34 | 0 |  | yes | 0 | ca-x-medieval 0.529 | 1 | 675 | 0.1283
olo | Uralic | 28 | 27 | 0 |  | no | 0 | vro 0.857 | 1 | 278 | 0.0801
om | Afro-Asiatic > Cushitic | 37 | 26 | 0 |  | no | 0 | sid 0.784 | 1 | 13380 | 0.1001
pcc | Tai-Kadai | 114 | 26 | 0 |  | no | 0 | kdx 0.228 | 1 | 153 | 0.0038
pjt | Pama-Nyungan | 26 | 18 | 0 |  | no | 0 | dec 0.462 | 1 | 125 | 0.0027
pqm | Algic | 18 | 18 | 0 |  | no | 0 | yua 0.778 | 1 | 151 | 0.1759
pt-BR-x-bahia | Indo-European > Italic > Romance > Ibero-Romance | 57 | 29 | 0 |  | yes | 0 | fax 0.793 | 1 | 20 | 0.0
pt-BR-x-brasilia | Indo-European > Italic > Romance > Ibero-Romance | 57 | 29 | 0 |  | yes | 0 | fax 0.793 | 1 | 20 | 0.0
pt-BR-x-ce | Indo-European > Italic > Romance > Ibero-Romance | 57 | 29 | 0 |  | yes | 0 | fax 0.793 | 1 | 20 | 0.0
pt-BR-x-fluminense | Indo-European > Italic > Romance > Ibero-Romance | 57 | 31 | 0 |  | yes | 0 | fax 0.793 | 1 | 20 | 0.0
pt-BR-x-mg | Indo-European > Italic > Romance > Ibero-Romance | 57 | 33 | 0 |  | yes | 0 | fax 0.793 | 1 | 20 | 0.0
pt-BR-x-norte | Indo-European > Italic > Romance > Ibero-Romance | 57 | 32 | 0 |  | yes | 0 | fax 0.793 | 1 | 20 | 0.0
pt-BR-x-pr | Indo-European > Italic > Romance > Ibero-Romance | 57 | 31 | 0 |  | yes | 0 | fax 0.793 | 1 | 20 | 0.0
pt-BR-x-recife | Indo-European > Italic > Romance > Ibero-Romance | 57 | 30 | 0 |  | yes | 0 | fax 0.793 | 1 | 20 | 0.0
pt-BR-x-sul | Indo-European > Italic > Romance > Ibero-Romance | 57 | 31 | 0 |  | yes | 0 | fax 0.81 | 1 | 20 | 0.0
pt-CV | Indo-European > Italic > Romance > Ibero-Romance | 4 | 30 | 0 |  | yes | 0 |  | 1 | 20 | 0.0
pt-GW | Indo-European > Italic > Romance > Ibero-Romance | 4 | 29 | 0 |  | yes | 0 |  | 1 | 20 | 0.0
pt-MO | Indo-European > Italic > Romance > Ibero-Romance | 2 | 30 | 0 |  | yes | 0 |  | 1 | 20 | 0.0
pt-PT-x-acores | Indo-European > Italic > Romance > Ibero-Romance | 1 | 34 | 0 |  | yes | 0 |  | 3 | 51 | 0.3261
pt-PT-x-alentejo | Indo-European > Italic > Romance > Ibero-Romance | 3 | 33 | 0 |  | yes | 0 |  | 4 | 56 | 0.3
pt-PT-x-alfena | Indo-European > Italic > Romance > Ibero-Romance | 3 | 32 | 0 |  | yes | 0 |  | 2 | 21 | 0.326
pt-PT-x-algarve | Indo-European > Italic > Romance > Ibero-Romance | 2 | 32 | 0 |  | yes | 0 |  | 3 | 53 | 0.3712
pt-PT-x-aveiro | Indo-European > Italic > Romance > Ibero-Romance | 3 | 33 | 0 |  | yes | 0 |  | 2 | 26 | 0.3056
pt-PT-x-beira | Indo-European > Italic > Romance > Ibero-Romance | 3 | 37 | 0 |  | yes | 0 |  | 3 | 36 | 0.4327
pt-PT-x-braga | Indo-European > Italic > Romance > Ibero-Romance | 2 | 31 | 0 |  | yes | 0 |  | 1 | 20 | 0.0
pt-PT-x-coimbra | Indo-European > Italic > Romance > Ibero-Romance | 0 | 29 | 0 |  | yes | 0 |  | 1 | 20 | 0.0
pt-PT-x-madeira | Indo-European > Italic > Romance > Ibero-Romance | 3 | 36 | 0 |  | yes | 0 |  | 3 | 54 | 0.325
pt-PT-x-medieval | Indo-European > Italic > Romance > Ibero-Romance | 23 | 24 | 0 |  | yes | 0 | lfn 0.348 | 1 | 20 | 0.0
pt-PT-x-sao-miguel | Indo-European > Italic > Romance > Ibero-Romance | 3 | 33 | 0 |  | yes | 0 |  | 2 | 32 | 0.3917
pt-PT-x-terceira | Indo-European > Italic > Romance > Ibero-Romance | 0 | 30 | 0 |  | yes | 0 |  | 2 | 30 | 0.2345
pt-PT-x-trasosmontes | Indo-European > Italic > Romance > Ibero-Romance | 2 | 33 | 0 |  | yes | 0 |  | 2 | 26 | 0.3317
pt-ST | Indo-European > Italic > Romance > Ibero-Romance | 4 | 29 | 0 |  | yes | 0 |  | 1 | 20 | 0.0
pt-UY | Indo-European > Italic > Romance > Ibero-Romance | 4 | 30 | 0 |  | yes | 0 |  | 1 | 20 | 0.0
roa-x-galaicopt | Indo-European > Italic > Romance > Ibero-Romance | 54 | 23 | 0 |  | yes | 0 | pt-BR-x-sul 0.737 | 1 | 20 | 0.0
sel | Uralic | 55 | 33 | 0 |  | no | 0 | enf 0.702 | 1 | 886 | 0.0342
skr | Indo-European > Indo-Iranian > Indo-Aryan | 51 | 36 | 0 |  | no | 0 | bal 0.706 | 1 | 309 | 0.2869
so | Afro-Asiatic > Cushitic | 34 | 24 | 0 |  | no | 0 | rhg 0.794 | 1 | 230 | 0.5567
syc | Afro-Asiatic > Semitic > Central Semitic | 22 | 22 | 0 |  | no | 0 | tru 0.957 | 1 | 96 | 0.4353
szl | Indo-European > Balto-Slavic > Slavic > West Slavic | 41 | 34 | 0 |  | yes | 0 | csb 0.78 | 1 | 2377 | 0.2148
ta | Dravidian | 50 | 47 | 0 |  | no | 0 |  | 2 | 146030 | 0.3757
tet | Austronesian > Malayo-Polynesian | 36 | 28 | 0 |  | yes | 0 | kcn 0.75 | 1 | 55 | 0.0683
tew | Kiowa-Tanoan | 115 | 31 | 0 |  | no | 0 | ee 0.175 | 1 | 106 | 0.0
tft | North Halmahera | 23 | 22 | 0 |  | no | 0 | mqs 1.0 | 1 | 293 | 0.1041
th | Tai-Kadai | 165 | 70 | 0 |  | no | 0 |  | 2 | 40641 | 0.4581
tkl | Austronesian > Malayo-Polynesian | 20 | 20 | 0 |  | no | 0 | to 0.864 | 1 | 340 | 0.0497
tpw | Tupian | 38 | 33 | 0 |  | yes | 0 | gn 0.59 | 1 | 372 | 0.0951
tt | Turkic | 39 | 36 | 0 |  | yes | 0 | kk 0.875 | 1 | 22220 | 0.3708
twf | Kiowa-Tanoan | 118 | 48 | 0 |  | no | 0 | kwk 0.169 | 1 | 135 | 0.024
uby | Abkhaz-Adyge | 90 | 45 | 0 |  | no | 0 | ab 0.378 | 1 | 1317 | 0.0247
udm | Uralic | 72 | 36 | 0 |  | no | 0 | koi 0.703 | 1 | 973 | 0.211
vot | Uralic > Finnic | 13 | 28 | 0 |  | yes | 0 | krl 0.538 | 1 | 2832 | 0.0898
wiy | Algic | 44 | 33 | 0 |  | no | 0 | lkt 0.477 | 1 | 151 | 0.0662
xh | Atlantic-Congo > Bantu | 82 | 27 | 0 |  | yes | 0 | zu 0.561 | 1 | 887 | 0.3781
xsl | Athabaskan-Eyak-Tlingit | 87 | 36 | 0 |  | no | 0 | apw 0.398 | 1 | 146 | 0.0273
ycl | Sino-Tibetan | 44 | 24 | 0 |  | no | 0 | sce 0.341 | 1 | 111 | 0.0108
zh | Sino-Tibetan > Sinitic | 347 | 27 | 0 |  | no | 0 | kdx 0.072 | 1 | 4718 | 0.2882
zom | Sino-Tibetan | 32 | 20 | 0 |  | no | 0 | cnk 0.912 | 1 | 134 | 0.528
zu | Atlantic-Congo > Bantu | 66 | 26 | 0 |  | yes | 0 | nd 0.682 | 1 | 1754 | 0.2311

---
[← Ranking error](ranking_error.md) · [Home](index.md) · [Finding a language's phonology documentation →](languages/index.md)
