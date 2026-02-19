"""Japanese (ja) — grapheme→IPA and allophone mappings.

Sources:
- Okada, H. (1999). Japanese. *Handbook of the IPA*.
- Vance, T.J. (2008). *The Sounds of Japanese*.
- Labrune, L. (2012). *The Phonology of Japanese*.

Conventions:
- Hiragana as primary keys; katakana equivalents share the same phonemes.
- Yōon (拗音) digraphs included as linguistically standard combinations.
- Moraic nasal ⟨ん⟩ mapped to archiphoneme /N/.
"""
from orthography2ipa.types import LanguageSpec

GRAPHEMES = {
    # --- Basic mora (vowels) ---
    "あ": ["a"], "い": ["i"], "う": ["ɯ"], "え": ["e"], "お": ["o"],

    # --- K-row ---
    "か": ["ka"], "き": ["ki"], "く": ["kɯ"], "け": ["ke"], "こ": ["ko"],
    "が": ["ɡa"], "ぎ": ["ɡi"], "ぐ": ["ɡɯ"], "げ": ["ɡe"], "ご": ["ɡo"],

    # --- S-row ---
    "さ": ["sa"], "し": ["ɕi"], "す": ["sɯ"], "せ": ["se"], "そ": ["so"],
    "ざ": ["za"], "じ": ["dʑi"], "ず": ["zɯ"], "ぜ": ["ze"], "ぞ": ["zo"],

    # --- T-row ---
    "た": ["ta"], "ち": ["tɕi"], "つ": ["tsɯ"], "て": ["te"], "と": ["to"],
    "だ": ["da"], "ぢ": ["dʑi"], "づ": ["dzɯ"], "で": ["de"], "ど": ["do"],

    # --- N-row ---
    "な": ["na"], "に": ["ɲi"], "ぬ": ["nɯ"], "ね": ["ne"], "の": ["no"],

    # --- H-row ---
    "は": ["ha"], "ひ": ["çi"], "ふ": ["ɸɯ"], "へ": ["he"], "ほ": ["ho"],
    "ば": ["ba"], "び": ["bi"], "ぶ": ["bɯ"], "べ": ["be"], "ぼ": ["bo"],
    "ぱ": ["pa"], "ぴ": ["pi"], "ぷ": ["pɯ"], "ぺ": ["pe"], "ぽ": ["po"],

    # --- M-row ---
    "ま": ["ma"], "み": ["mi"], "む": ["mɯ"], "め": ["me"], "も": ["mo"],

    # --- Y-row ---
    "や": ["ja"], "ゆ": ["jɯ"], "よ": ["jo"],

    # --- R-row ---
    "ら": ["ɾa"], "り": ["ɾi"], "る": ["ɾɯ"], "れ": ["ɾe"], "ろ": ["ɾo"],

    # --- W-row ---
    "わ": ["wa"], "を": ["o"],

    # --- Moraic nasal ---
    "ん": ["N"],  # archiphoneme: [m, n, ŋ, ɴ, ɯ̃] by context

    # --- Sokuon (gemination) ---
    "っ": ["Q"],  # archiphoneme: doubles following consonant

    # --- Chōon (long vowel, katakana) ---
    "ー": ["ː"],

    # --- Yōon digraphs (C + small ya/yu/yo) ---
    "きゃ": ["kʲa"], "きゅ": ["kʲɯ"], "きょ": ["kʲo"],
    "ぎゃ": ["ɡʲa"], "ぎゅ": ["ɡʲɯ"], "ぎょ": ["ɡʲo"],
    "しゃ": ["ɕa"], "しゅ": ["ɕɯ"], "しょ": ["ɕo"],
    "じゃ": ["dʑa"], "じゅ": ["dʑɯ"], "じょ": ["dʑo"],
    "ちゃ": ["tɕa"], "ちゅ": ["tɕɯ"], "ちょ": ["tɕo"],
    "にゃ": ["ɲa"], "にゅ": ["ɲɯ"], "にょ": ["ɲo"],
    "ひゃ": ["ça"], "ひゅ": ["çɯ"], "ひょ": ["ço"],
    "びゃ": ["bʲa"], "びゅ": ["bʲɯ"], "びょ": ["bʲo"],
    "ぴゃ": ["pʲa"], "ぴゅ": ["pʲɯ"], "ぴょ": ["pʲo"],
    "みゃ": ["mʲa"], "みゅ": ["mʲɯ"], "みょ": ["mʲo"],
    "りゃ": ["ɾʲa"], "りゅ": ["ɾʲɯ"], "りょ": ["ɾʲo"],

    # --- Katakana equivalents (same phonemes, included for lookup) ---
    "ア": ["a"], "イ": ["i"], "ウ": ["ɯ"], "エ": ["e"], "オ": ["o"],
    "カ": ["ka"], "キ": ["ki"], "ク": ["kɯ"], "ケ": ["ke"], "コ": ["ko"],
    "サ": ["sa"], "シ": ["ɕi"], "ス": ["sɯ"], "セ": ["se"], "ソ": ["so"],
    "タ": ["ta"], "チ": ["tɕi"], "ツ": ["tsɯ"], "テ": ["te"], "ト": ["to"],
    "ナ": ["na"], "ニ": ["ɲi"], "ヌ": ["nɯ"], "ネ": ["ne"], "ノ": ["no"],
    "ハ": ["ha"], "ヒ": ["çi"], "フ": ["ɸɯ"], "ヘ": ["he"], "ホ": ["ho"],
    "マ": ["ma"], "ミ": ["mi"], "ム": ["mɯ"], "メ": ["me"], "モ": ["mo"],
    "ヤ": ["ja"], "ユ": ["jɯ"], "ヨ": ["jo"],
    "ラ": ["ɾa"], "リ": ["ɾi"], "ル": ["ɾɯ"], "レ": ["ɾe"], "ロ": ["ɾo"],
    "ワ": ["wa"], "ヲ": ["o"],
    "ン": ["N"], "ッ": ["Q"],

    "ガ": ["ɡa"], "ギ": ["ɡi"], "グ": ["ɡɯ"], "ゲ": ["ɡe"], "ゴ": ["ɡo"],
    "ザ": ["za"], "ジ": ["dʑi"], "ズ": ["zɯ"], "ゼ": ["ze"], "ゾ": ["zo"],
    "ダ": ["da"], "ヂ": ["dʑi"], "ヅ": ["dzɯ"], "デ": ["de"], "ド": ["do"],
    "バ": ["ba"], "ビ": ["bi"], "ブ": ["bɯ"], "ベ": ["be"], "ボ": ["bo"],
    "パ": ["pa"], "ピ": ["pi"], "プ": ["pɯ"], "ペ": ["pe"], "ポ": ["po"],
}

ALLOPHONES = {
    # Stops / affricates
    "k": ["k"], "ɡ": ["ɡ", "ŋ"],  # [ŋ] medially in some dialects
    "t": ["t"], "d": ["d"],
    "p": ["p"], "b": ["b"],
    "tɕ": ["tɕ"], "dʑ": ["dʑ", "ʑ"],  # [ʑ] medially
    "ts": ["ts"], "dz": ["dz", "z"],

    # Fricatives
    "s": ["s"], "z": ["z"],
    "ɕ": ["ɕ"],
    "ç": ["ç"],
    "ɸ": ["ɸ"],
    "h": ["h", "ɦ"],  # [ɦ] between voiced segments

    # Nasals
    "m": ["m"], "n": ["n"], "ɲ": ["ɲ"],
    "N": ["m", "n", "ŋ", "ɴ", "ɯ̃"],  # moraic nasal: varies by context

    # Liquid
    "ɾ": ["ɾ", "l", "ɺ"],  # lateral/tap free variation

    # Glides
    "j": ["j"], "w": ["w", "β̞"],

    # Vowels
    "a": ["a"], "i": ["i"], "ɯ": ["ɯ", "ɯ̥"],  # devoiced
    "e": ["e"], "o": ["o"],
}

SPECS = {
    "ja": LanguageSpec(
        code="ja",
        name="Japanese",
        family="Japonic",
        script="Kana",
        graphemes=GRAPHEMES,
        allophones=ALLOPHONES,
        notes=(
            "Standard Tokyo Japanese. Moraic structure: each kana = one mora. "
            "Vowel devoicing of /i, ɯ/ between voiceless consonants is "
            "systematic. Moraic nasal /N/ and geminate /Q/ are archiphonemes."
        ),
    ),
}
