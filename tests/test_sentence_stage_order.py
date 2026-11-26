"""The sentence stages run in the order of IR spec §3.1: the spec's
``sandhi_rules`` (S11), then the sentence rescorers (H6), then the host sandhi
(H7). Catalan assimilates a word-final /n/ to the place of a following velar:
«tant que» is [taŋ kə]."""
from orthography2ipa import G2P, Pipeline, SandhiPlugin, SentenceRescorer


class Spy(SentenceRescorer):
    def __init__(self):
        self.seen = []

    def rescore(self, word, context):
        self.seen.append(context.this_word_ipa)
        return context.this_word_ipa


def test_the_sentence_rescorers_read_the_output_of_the_sandhi_rules():
    spy = Spy()
    G2P("ca", sentence_rescorer=spy).transcribe("tant que")
    assert spy.seen[0] == "ˈtaŋ"
    assert G2P("ca").transcribe("tant") == "ˈtan"


class SandhiSpy(SandhiPlugin):
    def __init__(self):
        self.seen = []

    def apply(self, words, surfaces, pausal, lang):
        self.seen = list(words)
        return list(words)


def test_the_host_sandhi_reads_the_output_of_the_sandhi_rules():
    spy = SandhiSpy()
    G2P("ca", pipeline=Pipeline(sandhi=spy)).transcribe("tant que")
    assert spy.seen[0] == "ˈtaŋ"
