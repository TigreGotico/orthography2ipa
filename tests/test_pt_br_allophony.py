"""Brazilian Portuguese post-lexical allophony (Workstream P, task P2).

The ``pt-BR`` base spec declares ``allophone_rules`` modelling the
best-documented BP post-lexical process for the base variety (Barbosa &
Albano 2004, JIPA illustration; Câmara Jr. 1970):

* **Final unstressed vowel raising** — the near-close [ɪ]/[ʊ] the positional
  map selects word-finally is realised as the standard BP close [i]/[u]
  (gato → [ˈɡatu], leite → [ˈlejti]).

Affrication of /t d/ before front vowels is modelled *pre-lexically*
(``positional_graphemes`` ``before_i``); it is deliberately NOT duplicated
in ``allophone_rules``. These tests pin: raising fires word-final only and
only on the reduced vowels (so conservative dialects that retain a final
[e]/[o] are untouched); the ``apply_allophony`` toggle recovers the broad
form; and grapheme-⟨i⟩ affrication still fires via the positional map.
"""
import json
import re
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa import get_syllabifier
from orthography2ipa.g2p import G2P


# ─── Final unstressed vowel raising ────────────────────────────────────

@pytest.mark.parametrize("word,expected_final", [
    ("gato", "u"),    # /o/# → [u]
    ("leite", "i"),   # /e/# → [i]
    ("verde", "i"),   # /e/# → [i]
    ("dia", "ɐ"),     # final -a is NOT raised (reduces to [ɐ], unchanged)
])
def test_final_vowel_raising(word, expected_final):
    assert G2P("pt-BR").transcribe_word(word).endswith(expected_final)


def test_final_raising_word_final_only():
    # Only the word edge raises: "gota" keeps a stressed [o] and reduces the
    # final /a/ to [ɐ] — no interior raising.
    out = G2P("pt-BR").transcribe_word("gota")
    assert out.startswith("ˈɡo")
    assert out.endswith("ɐ")


def test_raising_targets_reduced_vowel_only():
    # The rule targets the reduced [ɪ]/[ʊ], never underlying /e o/, so a
    # dialect that retains a final [e] would be untouched. On the base the
    # reduced vowel is present, so raising applies.
    assert G2P("pt-BR").transcribe_word("gato").endswith("u")


def test_raising_recovered_by_broad_toggle():
    # apply_allophony=False yields the broad/pre-lexical near-close vowel.
    assert G2P("pt-BR").transcribe_word("gato").endswith("u")
    assert G2P("pt-BR", apply_allophony=False).transcribe_word(
        "gato").endswith("ʊ")


# ─── Affrication of /t d/ before ⟨i⟩ (pre-lexical / positional) ─────────

@pytest.mark.parametrize("word,affricate", [
    ("tio", "t͡ʃ"),
    ("dia", "d͡ʒ"),
    ("partido", "t͡ʃ"),
    ("Abundio", "d͡ʒ"),
])
def test_affrication_before_orthographic_i(word, affricate):
    assert affricate in G2P("pt-BR").transcribe_word(word)


def test_affrication_not_before_non_high_vowel():
    # /t d/ before a back/low vowel stay plain stops.
    assert "t͡ʃ" not in G2P("pt-BR").transcribe_word("gato")
    assert G2P("pt-BR").transcribe_word("dado").startswith("ˈdad")


# ─── wikipron-gold-derived passing words ───────────────────────────────

@pytest.mark.parametrize("word,fragment", [
    ("Abundio", "d͡ʒi"),     # gold abũdʒiu — /d/ affricates before [i]
    ("partido", "ɾˈt͡ʃidu"),   # /t/ affricates before [i]; final /o/ raises
    ("gato", "ɡatu"),        # final raising
])
def test_gold_derived_words(word, fragment):
    assert fragment in G2P("pt-BR").transcribe_word(word)


# ─── coda vowel nasalisation (retained in Brazilian Portuguese) ─────────
# BP keeps the general-Portuguese coda-nasal → nasal-vowel process
# (Mateus & d'Andrade 2000: ch.2; Barbosa & Albano 2004). A vowel before a
# CODA ⟨m/n⟩ nasalises (tilde U+0303 from the positional m/n slot); an
# INTERVOCALIC (onset) nasal leaves the vowel oral.

TILDE = "̃"


def test_br_declares_the_nasal_raise_rules():
    from orthography2ipa import get
    ids = [r.id for r in get("pt-BR").allophone_rules]
    # the word-final nasal-diphthong glide rules and the raised-final-e
    # affrication rules now lead the list; the nasal-raise trio follows.
    assert ids[:6] == [
        "BR_FINAL_EM_GLIDE", "BR_FINAL_ENS_GLIDE", "BR_FINAL_AM_GLIDE",
        "BR_AFFRIC_T_RAISED", "BR_AFFRIC_D_RAISED", "PT_NASAL_A_RAISE"]
    assert [i for i in ids if i.startswith("PT_NASAL")][:3] == [
        "PT_NASAL_A_RAISE", "PT_NASAL_E_RAISE", "PT_NASAL_O_RAISE"]
    # the BR final-raising rules are preserved after the nasal rules
    assert "BR_RAISE_FINAL_E" in ids and "BR_RAISE_FINAL_O" in ids


@pytest.mark.parametrize("word,expected", [
    ("campo", "ˈkɐ̃pu"),
    ("sim", "ˈsĩ"),
    ("bom", "ˈbõ"),
    ("mundo", "ˈmũdu"),
    ("cantar", "kɐ̃ˈtaɾ"),
    ("fim", "ˈfĩ"),
    ("tempo", "ˈtẽpu"),
])
def test_br_coda_nasalisation(word, expected):
    import unicodedata
    got = unicodedata.normalize("NFC", G2P("pt-BR").transcribe_word(word))
    assert got == unicodedata.normalize("NFC", expected)


def _nfd_br(word):
    import unicodedata
    return unicodedata.normalize("NFD", G2P("pt-BR").transcribe_word(word))


@pytest.mark.parametrize("word,expected", [
    # Barbosa & Albano (2004: 229): a stressed vowel nasalises before a
    # heterosyllabic nasal consonant: cima [ˈsĩmɐ], sama [ˈsɐ̃mɐ], soma [ˈsõmɐ].
    ("cima", "ˈsĩmɐ"), ("soma", "ˈsõmɐ"), ("cama", "ˈkɐ̃mɐ"),
    ("ano", "ˈɐ̃nu"), ("fome", "ˈfõmi"), ("ganho", "ˈɡɐ̃ɲu"),
])
def test_br_stressed_vowel_nasalised_before_onset_nasal(word, expected):
    import unicodedata
    got = unicodedata.normalize("NFC", G2P("pt-BR").transcribe_word(word))
    assert got == unicodedata.normalize("NFC", expected)


def test_br_pretonic_vowel_oral_before_onset_nasal():
    # Barbosa & Albano (2004: 229): a pretonic vowel nasalises only before
    # /N/ or /ɲ/ (ganhar [gɐ̃ˈɲaɾ]); before an onset /m n/ it stays oral.
    for word in ("camada", "lunar", "lua"):
        out = _nfd_br(word)
        assert TILDE not in out, (word, out)
    assert _nfd_br("ganhar").startswith("ɡɐ" + TILDE)


def test_br_no_double_tilde():
    for word in ("campo", "sim", "bom", "mundo", "cantar", "tempo"):
        out = _nfd_br(word)
        assert TILDE + TILDE not in out, (word, out)


def test_br_nh_digraph_unbroken():
    # ⟨nh⟩ stays one palatal nasal; the stressed vowel before it is nasalised
    # (Barbosa & Albano 2004: 228, ganho [ˈɡɐ̃ɲʊ]).
    out = _nfd_br("banho")
    assert "ɲ" in out and "n" + "ɲ" not in out and out.count(TILDE) == 1, out


def test_br_final_es_os_raising_feeds_affrication():
    """The final unstressed ⟨-es/-os⟩ ending raises to [i]/[u], and the raise
    feeds /t d/ affrication on a two-pass allophone run (allophone_passes=2).

    ``estes`` [ˈest͡ʃis] cannot surface from a single pass: the affrication
    reads the vowel BEFORE the raise on the first pass, so it needs the second.
    """
    import unicodedata
    g = G2P("pt-BR")

    def _t(w):
        return unicodedata.normalize("NFC", g.transcribe_word(w))

    assert g.spec.allophone_passes == 2
    assert _t("estes") == "ˈest͡ʃis"
    assert _t("dentes") == unicodedata.normalize("NFC", "ˈdẽt͡ʃis")
    assert _t("pontes") == unicodedata.normalize("NFC", "ˈpõt͡ʃis")
    assert _t("verdes") == "ˈveɾd͡ʒis"     # /d/ affrication
    assert _t("gatos") == "ˈɡatus"          # -os → -us
    assert _t("pires") == "ˈpiɾis"


def test_br_final_raising_is_gated():
    """The raise fires only on an UNSTRESSED final vowel before a word-final
    ⟨s⟩: a stressed monosyllable and a medial ⟨s⟩+consonant are left alone."""
    g = G2P("pt-BR")
    # stressed -ês/-ás keep their mid/low vowel (no raise, no affrication)
    assert g.transcribe_word("três") == "ˈtɾes"
    assert g.transcribe_word("mês") == "ˈmes"
    # medial ⟨s⟩ before a consonant is not the ending
    assert g.transcribe_word("festa") == "ˈfestɐ"
    assert g.transcribe_word("vespa") == "ˈvespɐ"
    assert g.transcribe_word("gosto") == "ˈɡostu"


def test_br_conservative_dialects_raise_without_affrication():
    """A dental (non-palatalising) dialect still raises the ending but keeps
    /t d/ dental — a single pass suffices, so it stays at allophone_passes=1."""
    for lect in ("pt-BR-x-caipira", "pt-BR-x-sul"):
        g = G2P(lect)
        assert g.spec.allophone_passes == 1
        out = g.transcribe_word("dentes")
        assert out.endswith("is") and "t͡ʃ" not in out, (lect, out)


# ─── Sibilants: no medieval apico-alveolar leak ────────────────────────
#
# BP has a single plain alveolar sibilant pair /s z/ (Barbosa & Albano 2004:
# 228, consonant chart: saca [ˈsakɐ] / zaca [ˈzakɐ], Alveolar column). The
# apico-alveolar [s̺ z̺] belongs to the Galician-Portuguese four-sibilant
# system that ``roa-x-galaicopt`` and ``pt-PT-x-medieval`` model, and to the
# northern EP dialects that retain it (``pt-PT-x-minho`` and siblings). It
# must not reach a modern spec through inheritance.

@pytest.mark.parametrize("word", [
    "isso",      # ⟨ss⟩ digraph
    "passou",
    "nessa",
    "você",      # ⟨c⟩ before ⟨e⟩
    "cidade",    # ⟨c⟩ before ⟨i⟩
    "cinco",
    "carroça",   # ⟨ç⟩
])
def test_no_apicoalveolar_sibilant(word):
    out = G2P("pt-BR").transcribe_word(word)
    assert "s̺" not in out and "z̺" not in out, out


@pytest.mark.parametrize("lang,word", [
    ("pt-PT-x-medieval", "cidade"),   # the ancestor the value belongs to
    ("pt-PT-x-minho", "cidade"),      # declares positional ⟨c⟩ → [s̺]
    ("pt-PT-x-trasosmontes", "isso"), # declares ⟨ss⟩ → [s̺]
])
def test_northern_ep_keeps_apicoalveolar(lang, word):
    # The northern EP dialects declare the apico-alveolar deliberately
    # (pt-PT notes: "some northern/insular dialects keep an apico-alveolar
    # [s̺] in coda, which is a dialect delta and not modelled in the base").
    # Correcting pt-BR must not reach them, and must not reach the medieval
    # ancestor where the four-sibilant system is the point.
    assert "s̺" in G2P(lang).transcribe_word(word)


# ─── ⟨ss⟩ and ⟨rr⟩ are digraphs, not geminates ─────────────────────────
#
# Portuguese has no contrastive consonant length. ⟨ss⟩ spells /s/ between
# vowels where a single ⟨s⟩ would be /z/, and ⟨rr⟩ spells the strong rhotic
# (Barbosa & Albano 2004: 228, carro [ˈkaʁu] vs caro [ˈkaɾu]). Both are
# declared digraphs, so neither yields a doubled segment and there is no
# geminate for a collapse pass to remove.

@pytest.mark.parametrize("word,expected", [
    ("isso", "ˈisu"),
    ("carro", "ˈkaʁu"),
    ("caro", "ˈkaɾu"),
])
def test_digraphs_yield_one_segment(word, expected):
    assert G2P("pt-BR").transcribe_word(word) == expected


# ─── ⟨w⟩ is transcribed, not deleted ───────────────────────────────────
#
# ⟨w⟩ occurs only in loans and names but is not silent: it is [w] in English
# loans and [v] in Germanic names. Without a grapheme entry the letter was
# dropped outright (web → [ˈeb], show → [ˈsu]).

@pytest.mark.parametrize("word", ["web", "show", "wagner", "wilson"])
def test_w_is_not_deleted(word):
    out = G2P("pt-BR").transcribe_word(word)
    assert "w" in out or "v" in out, out


# ─── Coda /S/ voicing, strong /r/ after a coda, epenthesis ─────────────────


@pytest.mark.parametrize("word,expected", [
    # Barbosa & Albano (2004: 229): coda /S/ "tends to assimilate the voicing
    # of the following sound".
    ("mesmo", "ˈmezmu"), ("desde", "ˈdezd͡ʒi"), ("rasgar", "ʁazˈɡaɾ"),
    ("festa", "ˈfestɐ"),
])
def test_br_coda_s_voices_before_voiced_consonant(word, expected):
    assert G2P("pt-BR").transcribe_word(word) == expected


@pytest.mark.parametrize("word", ["honra", "genro", "Israel"])
def test_br_strong_r_after_coda(word):
    # Cristófaro Silva (2025: 240, 243): after a coda consonant the rhotic is
    # the strong one (honra, Israel), never the tap.
    out = G2P("pt-BR").transcribe_word(word)
    assert "ʁ" in out and "ɾ" not in out, out


def test_br_onset_cluster_keeps_tap():
    # The tap of an onset cluster is not after a coda: três [ˈtɾes].
    assert G2P("pt-BR").transcribe_word("três") == "ˈtɾes"


@pytest.mark.parametrize("word,expected", [
    # Barbosa & Albano (2004: 227): epenthesis breaks two-obstruent sequences
    # with [i]; Collischonn (2004: 67-68): pretonic 69 %, advogado type 89 %.
    ("advogado", "ad͡ʒivoˈɡadu"), ("obter", "obiˈteɾ"), ("absurdo", "abiˈsuɾdu"),
])
def test_br_pretonic_epenthesis(word, expected):
    assert G2P("pt-BR").transcribe_word(word) == expected


def test_br_no_epenthesis_after_stressed_vowel():
    # Collischonn (2004: 67): post-tonic epenthesis is a minority (24 %).
    assert G2P("pt-BR").transcribe_word("pacto") == "ˈpaktu"


@pytest.mark.parametrize("word,expected", [
    # Barbosa & Albano (2004: 229-230): the post-stressed oral vowels are
    # [ɪ ɐ ʊ e̞]; an unstressed final ⟨a⟩ is [ɐ] also before the plural ⟨-s⟩.
    ("casas", "ˈkazɐs"), ("falas", "ˈfalɐs"), ("gás", "ˈɡas"), ("atrás", "aˈtɾas"),
])
def test_br_final_as_reduces(word, expected):
    assert G2P("pt-BR").transcribe_word(word) == expected


# ─── Regional children take the pt-BR syllables ─────────────────────────

def _br_children():
    data = Path(orthography2ipa.__file__).parent / "data"
    return sorted(
        path.stem for path in data.glob("pt-BR-x-*.json")
        if json.loads(path.read_text("utf-8")).get("graphemes_base") == "pt-BR")


BR_CHILDREN = _br_children()


def test_br_children_are_found():
    assert len(BR_CHILDREN) == 12


@pytest.mark.parametrize("lang", BR_CHILDREN)
def test_br_child_uses_the_pt_br_syllabifier(lang):
    # A child reads the pt-BR grapheme table, so it takes the pt-BR syllables:
    # pac.to, op.ção. The stress gate of BR_EPENTHESIS reads that split.
    parent = get_syllabifier("pt-BR")
    assert parent is not None
    assert get_syllabifier(lang) is parent


@pytest.mark.parametrize("lang", BR_CHILDREN)
def test_br_child_epenthesis_follows_the_parent(lang):
    # The cluster after the stressed vowel keeps its consonants, and the mark
    # stays on the stressed syllable: pacto [ˈpaktu], not [paˈkitu].
    g2p = G2P(lang)
    assert re.fullmatch(r"ˈpak.?tu", g2p.transcribe_word("pacto"))
    assert re.fullmatch(r"ˈap.?tu", g2p.transcribe_word("apto"))
    assert re.search(r"ˈpaktɐ$", g2p.transcribe_word("compacta"))
    # The pretonic cluster takes the epenthetic [i], which is unstressed:
    # opção [opiˈsɐ̃w̃] (Barbosa & Albano 2004: 227).
    assert re.fullmatch(r"[oɔu]piˈsɐ̃w̃", g2p.transcribe_word("opção"))


# ─── pt-UY keeps final ⟨-as⟩ ────────────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("casas", "ˈkazas"), ("andas", "ˈɐ̃das"), ("frutas", "ˈfɾutas"),
])
def test_pt_uy_switches_off_final_as_reduction(word, expected):
    assert G2P("pt-UY").transcribe_word(word) == expected


# ─── Final ⟨-as⟩ reduction is post-stressed only ────────────────────────

@pytest.mark.parametrize("lang", ["pt-BR", "pt-BR-x-sp", "pt-BR-x-rj"])
@pytest.mark.parametrize("word", ["as", "às"])
def test_br_clitic_as_is_not_reduced(lang, word):
    # Barbosa & Albano (2004: 229-230) state the vowel set of the post-stressed
    # position. The article as and the contraction às have no stress of their
    # own, so they have no post-stressed syllable.
    assert G2P(lang).transcribe_word(word) in ("as", "aʃ")


def test_br_clitic_as_in_a_sentence():
    assert G2P("pt-BR").transcribe("as casas às três") == "as ˈkazɐs as ˈtɾes"
