"""
06_advanced_nlp.py — Advanced usage patterns and NLP integration scenarios.

Demonstrates:
- Building a simple phonemic transcription pipeline
- Comparing how words are transcribed across related languages
- Finding the phonologically closest language to a given one
- Cluster analysis using the distance matrix
- Building pronunciation dictionaries
- Cross-lingual phoneme alignment
"""

import orthography2ipa
from orthography2ipa.distance import (
    phonological_distance,
    pairwise_distances,
    segment_distance,
    inventory_distance,
)
from orthography2ipa.phonetok import PhonetokTokenizer
from typing import Dict, List, Tuple


# ════════════════════════════════════════════════════════════════════════
# Scenario 1: Phonemic Transcription Pipeline
# ════════════════════════════════════════════════════════════════════════

print("=" * 70)
print("SCENARIO 1: Phonemic Transcription Pipeline")
print("=" * 70)


def transcribe_word(word: str, lang_code: str, beam_width: int = 3) -> List[str]:
    """Return the top-N IPA transcriptions for a word in a given language."""
    spec = orthography2ipa.get(lang_code)
    tok = PhonetokTokenizer(spec)
    paths = tok.ipa_beam(word.lower(), beam_width=beam_width)
    return [p.ipa for p in paths]


# Transcribe a multilingual word list
words_by_lang = {
    "es": ["ciudad", "lluvia", "queso", "calle", "español"],
    "pt-BR": ["cidade", "chuva", "queijo", "rua", "português"],
    "fr": ["chat", "nuit", "eau", "ville", "français"],
    "it": ["città", "pioggia", "formaggio", "via", "italiano"],
    "de": ["Stadt", "Regen", "Käse", "Straße", "Deutsch"],
}

for lang_code, words in words_by_lang.items():
    spec = orthography2ipa.get(lang_code)
    print(f"\n  {spec.name}:")
    for word in words:
        transcriptions = transcribe_word(word, lang_code, beam_width=2)
        trans_str = "  |  ".join(f"/{t}/" for t in transcriptions)
        print(f"    {word:20s}  {trans_str}")


# ════════════════════════════════════════════════════════════════════════
# Scenario 2: International Words Across Languages
# ════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("SCENARIO 2: International Words Across Romance Languages")
print("=" * 70)

# These are cognates of similar Latin words across Romance
cognate_sets = [
    {
        "es": "ciudad",
        "pt": "cidade",
        "fr": "cite",
        "it": "città",
        "ca": "ciutat",
        "la": "civitatem",
    },
    {
        "es": "noche",
        "pt": "noite",
        "fr": "nuit",
        "it": "notte",
        "ca": "nit",
        "la": "noctem",
    },
]

for cognate_set in cognate_sets:
    la_word = cognate_set.get("la", "")
    print(f"\n  Cognate set (from Latin '{la_word}'):")
    for code, word in cognate_set.items():
        try:
            transcriptions = transcribe_word(word, code, beam_width=2)
            trans_str = "  |  ".join(f"/{t}/" for t in transcriptions[:2])
            spec = orthography2ipa.get(code)
            print(f"    {spec.name:25s}  {word:12s}  {trans_str}")
        except KeyError:
            pass


# ════════════════════════════════════════════════════════════════════════
# Scenario 3: Finding the Phonologically Closest Language
# ════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("SCENARIO 3: Finding Closest Language")
print("=" * 70)


def find_closest_languages(
    target_code: str,
    candidate_codes: List[str],
    top_n: int = 5
) -> List[Tuple[str, float]]:
    """Find the N phonologically closest languages to the target."""
    target = orthography2ipa.get(target_code)
    results = []
    for code in candidate_codes:
        if code == target_code:
            continue
        try:
            spec = orthography2ipa.get(code)
            d = phonological_distance(target, spec)
            results.append((code, d.combined))
        except KeyError:
            pass
    return sorted(results, key=lambda x: x[1])[:top_n]


# Languages to search through
search_pool = [
    "es", "es-419", "es-AR", "pt", "pt-BR", "fr", "it", "ca", "gl", "oc",
    "la", "ro", "an", "ast", "oc", "mwl", "en", "de", "nl", "sv", "ru", "ar",
]

for target in ["es", "fr", "de", "ar"]:
    print(f"\n  Closest to {orthography2ipa.get(target).name}:")
    closest = find_closest_languages(target, search_pool, top_n=5)
    for rank, (code, dist) in enumerate(closest, 1):
        try:
            spec = orthography2ipa.get(code)
            print(f"    {rank}. {spec.name:30s} [{code:15s}]  distance={dist:.3f}")
        except KeyError:
            pass


# ════════════════════════════════════════════════════════════════════════
# Scenario 4: Phoneme Inventory Analysis
# ════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("SCENARIO 4: Phoneme Inventory Analysis")
print("=" * 70)


def unique_phonemes(spec) -> set:
    """Extract all unique phonemes from a language spec."""
    phonemes = set()
    for ipa_list in spec.graphemes.values():
        for ipa in ipa_list:
            if ipa and ipa not in ("", "∅"):
                phonemes.add(ipa)
    return phonemes


def vowels(phonemes: set) -> set:
    """Filter to vowel-like segments."""
    vowel_chars = set("aeiouæœøɛɔɪʊəɐɑɨɵɯɞʌʏ")
    return {p for p in phonemes if any(c in vowel_chars for c in p) and len(p) <= 3}


def consonants(phonemes: set) -> set:
    return phonemes - vowels(phonemes)


# Analyze several languages
analyze_codes = ["es", "pt-BR", "fr", "de", "ar", "fi", "ja"]
print(f"\n  {'Language':25s}  {'Total':>6}  {'Vowels':>7}  {'Consonants':>11}  {'Unique to this lang':>20}")
print("  " + "-" * 76)

all_phonemes = {}
for code in analyze_codes:
    try:
        spec = orthography2ipa.get(code)
        ph = unique_phonemes(spec)
        all_phonemes[code] = ph
    except KeyError:
        pass

for code, ph in all_phonemes.items():
    spec = orthography2ipa.get(code)
    v = vowels(ph)
    c = consonants(ph)
    # Phonemes not found in any other language in this set
    others = set().union(*[p for k, p in all_phonemes.items() if k != code])
    unique = ph - others
    print(f"  {spec.name:25s}  {len(ph):>6}  {len(v):>7}  {len(c):>11}  {', '.join(list(unique)[:5]):>20}")


# ════════════════════════════════════════════════════════════════════════
# Scenario 5: Pronunciation Dictionary Builder
# ════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("SCENARIO 5: Pronunciation Dictionary Builder")
print("=" * 70)


def build_pronunciation_dict(
    words: List[str],
    lang_code: str,
    beam_width: int = 1
) -> Dict[str, str]:
    """Build a simple pronunciation dictionary for a word list."""
    spec = orthography2ipa.get(lang_code)
    tok = PhonetokTokenizer(spec)
    result = {}
    for word in words:
        paths = tok.ipa_beam(word.lower(), beam_width=beam_width)
        if paths:
            result[word] = "/" + paths[0].ipa + "/"
    return result


# Spanish word list
spanish_words = [
    "hola", "mundo", "casa", "gato", "perro", "libro", "mesa",
    "ciudad", "noche", "lluvia", "español", "gracias", "quiero",
]

print("\n  Spanish pronunciation dictionary:")
pron_dict = build_pronunciation_dict(spanish_words, "es")
for word, pron in pron_dict.items():
    print(f"    {word:20s}  {pron}")


# ════════════════════════════════════════════════════════════════════════
# Scenario 6: Cross-lingual Phoneme Alignment
# ════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("SCENARIO 6: Cross-Lingual Phoneme Correspondence")
print("=" * 70)


def find_phoneme_correspondences(
    spec_a, spec_b, threshold: float = 0.15
) -> List[Tuple[str, str, float]]:
    """
    For each phoneme in language A, find its nearest correspondent in language B.
    Returns pairs with distance below threshold.
    """
    ph_a = unique_phonemes(spec_a)
    ph_b = unique_phonemes(spec_b)

    correspondences = []
    for pa in sorted(ph_a):
        # Find nearest in B
        best_dist = float("inf")
        best_pb = None
        for pb in ph_b:
            d = segment_distance(pa, pb)
            if d < best_dist:
                best_dist = d
                best_pb = pb
        if best_dist <= threshold and best_pb and pa != best_pb:
            correspondences.append((pa, best_pb, best_dist))

    return sorted(correspondences, key=lambda x: x[2])


print("\n  Near-correspondent phonemes: Spanish ↔ French")
print(f"  (pairs with segment distance ≤ 0.15, excluding identity)")
es_spec = orthography2ipa.get("es")
fr_spec = orthography2ipa.get("fr")
corr = find_phoneme_correspondences(es_spec, fr_spec, threshold=0.12)
print(f"\n  {'ES phoneme':>12}  ↔  {'FR phoneme':12}  {'Distance':>9}")
print("  " + "-" * 44)
for pa, pb, d in corr[:15]:
    print(f"  /{pa:>10}/  ↔  /{pb:<10}/  {d:9.4f}")


print("\n  Near-correspondent phonemes: Spanish ↔ Arabic")
print("  (Arabic had a major adstrate influence on Spanish)")
ar_spec = orthography2ipa.get("ar")
corr_ar = find_phoneme_correspondences(es_spec, ar_spec, threshold=0.15)
print(f"\n  {'ES phoneme':>12}  ↔  {'AR phoneme':12}  {'Distance':>9}")
print("  " + "-" * 44)
for pa, pb, d in corr_ar[:12]:
    print(f"  /{pa:>10}/  ↔  /{pb:<10}/  {d:9.4f}")
