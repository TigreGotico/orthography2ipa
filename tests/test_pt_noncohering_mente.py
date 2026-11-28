"""The European Portuguese suffix -mente is a stress domain of its own.

Booij (2004, review of Vigário 2003, Journal of Portuguese Linguistics 3,
p. 178): "the suffix -mente [...] is non-cohering, that is, form[s] a
prosodic word of [its] own [...] a separate domain of stress assignment,
which blocks the application of phonological rules that typically apply to
stressless vowels". The suffix attaches to the feminine form (bela-mente,
same page, after Vigário p. 221), so the base keeps the vowel of its own
stress, the [ɔ] of -osa included.

The segments are the WikiPron pt-PT rows (en.wiktionary, Portugal), which
write no stress marks. The marks follow the two domains: a secondary mark on
the base, the main mark on the suffix.
"""
import json
import subprocess
from pathlib import Path

import pytest

from orthography2ipa import G2P
from orthography2ipa.ir import layout
from orthography2ipa.ir.compiler import build_ir

LUA = Path(__file__).resolve().parent.parent / "scripts" / "ir_lua_cli.lua"

# word, WikiPron pt-PT segments
ADVERBS = [
    ("claramente", "klaɾɐmẽtɨ"),
    ("belamente", "bɛlɐmẽtɨ"),
    ("milagrosamente", "milɐɡɾɔzɐmẽtɨ"),
    ("gostosamente", "ɡuʃtɔzɐmẽtɨ"),
]

# Words where ⟨mente⟩ is not the suffix, and a base that ends in a consonant.
JOINED = [
    ("mente", "mẽtɨ"),
    ("demente", "dɨmẽtɨ"),
    ("semente", "sɨmẽtɨ"),
    ("clemente", "klɨmẽtɨ"),
    ("comente", "kumẽtɨ"),
    ("felizmente", "fɨliʒmẽtɨ"),
]

# The subjunctive of -mentar verbs with a vowel before ⟨ment⟩: one stress
# domain, so the pretonic vowels reduce.
VERB_FORMS = [
    ("testamente", "tɨʃtɐˈmẽtɨ"),
    ("recomente", "ʁɨkuˈmẽtɨ"),
    ("casamente", "kɐzɐˈmẽtɨ"),
]


def _plain(ipa):
    return ipa.replace("ˈ", "").replace("ˌ", "")


@pytest.fixture(scope="module")
def g2p():
    return G2P("pt-PT")


@pytest.mark.parametrize("word,gold", ADVERBS)
def test_the_base_keeps_the_vowel_of_its_own_stress(g2p, word, gold):
    assert _plain(g2p.transcribe_word(word)) == gold


@pytest.mark.parametrize("word,gold", JOINED)
def test_a_word_that_is_not_base_plus_mente_stays_one_domain(g2p, word, gold):
    ipa = g2p.transcribe_word(word)
    assert _plain(ipa) == gold
    assert "ˌ" not in ipa


@pytest.mark.parametrize("word,gold", VERB_FORMS)
def test_a_mentar_verb_form_stays_one_domain(g2p, word, gold):
    assert g2p.transcribe_word(word) == gold


def test_the_base_takes_the_secondary_mark_and_the_suffix_the_main_mark(g2p):
    assert g2p.transcribe_word("claramente") == "ˌklaɾɐˈmẽtɨ"
    assert g2p.transcribe("fala claramente") == "ˈfalɐ ˌklaɾɐˈmẽtɨ"


def test_the_first_candidate_is_the_transcription(g2p):
    assert g2p.word_candidates("belamente") == [g2p.transcribe_word("belamente")]


def test_lua_reads_the_two_domains(tmp_path):
    ir = tmp_path / "pt-PT.json"
    ir.write_text(json.dumps(layout.encode(build_ir("pt-PT"))), encoding="utf-8")
    words = [w for w, _ in ADVERBS + JOINED]
    stdin = "".join(" ".join(str(ord(c)) for c in w) + "\n" for w in words)
    proc = subprocess.run(["luajit", str(LUA), str(ir), "1"], input=stdin,
                          capture_output=True, text=True, check=True)
    lua = ["".join(chr(int(x)) for x in line.split()) for line in proc.stdout.splitlines()]
    g2p = G2P("pt-PT")
    assert lua == [g2p.transcribe_word(w) for w in words]
    assert lua[0] == "ˌklaɾɐˈmẽtɨ"
