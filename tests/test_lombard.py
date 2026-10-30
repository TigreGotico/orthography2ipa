"""Lombard (`lmo`) accented-vowel series: regression pins for the Ticinese
grave/acute series and the classical-Milanese circumflex series.

The circumflex series is the load-bearing part of this file. The classical
Milanese source (it.wikipedia.org/wiki/Ortografia_milanese_classica,
'Accenti' section, citing Porta ed. Isella 1982) states plain o is already
pronounced [u] in Milanese and that circumflex marks 'very closed timbre and
long duration'; applied to an already-[u] vowel that gives [uː], not [oː].
The two attested circumflex-o words in the WikiPron gold ('rasô', 'resô')
both realize as plain /u/ with no length, so ô is mapped to /u/ here, not
/o/, /oː/ or /uː/. â is mapped to plain /a/: the source's worked circumflex
examples are ô and û, not â (which falls only under a trailing 'ecc.'), and
the gold is a coin flip on length for â ('citâ'/'çitâ' show /aː/; 'jâld' and
'tajâ' show no length across six lines), so no length is asserted.

These words were verified to fail against the pristine (pre-fix) lmo.json
that mapped accented vowels either to /oː/ (ô) or left them unmapped.

Also covers two follow-up fixes: the missing ü/üü umlaut mapping (classical
Milanese spelling of the same front rounded vowel plain 'u' denotes), and
the new `lmo-x-milanese` entry, which models the classical Milanese source's
circumflex rule literally instead of `lmo`'s gold-fit reading.
"""
from orthography2ipa import transcribe


def test_grave_acute_series_still_correct():
    # Grave = open timbre, acute = closed timbre (Ticinese/Salvioni 1907);
    # this series was already correct and untouched by this fix.
    assert transcribe("abdicà", "lmo") == "abdika"
    assert transcribe("Giòrgio", "lmo") == "ɡiɔrɡio"


def test_circumflex_o_is_plain_u_not_long_o():
    # rasô/resô: gold is plain /u/, no length, for both attested words.
    assert transcribe("rasô", "lmo") == "rasu"
    assert transcribe("resô", "lmo") == "resu"


def test_circumflex_a_is_plain_a_not_long():
    # jâld/tajâ show no length in the gold; â is not asserted as long.
    assert transcribe("jâld", "lmo") == "jald"
    assert transcribe("tajâ", "lmo") == "taja"


def test_circumflex_e_keeps_length_from_single_attestation():
    # paês is the only gold word with ê; it does show length, and this
    # matches the source's stated circumflex-length rule, but n=1 is thin
    # evidence and the spec notes say so explicitly.
    assert transcribe("paês", "lmo") == "paeːs"


def test_u_umlaut_is_front_rounded_y_not_dropped():
    # ü/üü are the classical-Milanese umlaut spelling of the same front
    # rounded vowel plain 'u' denotes (/y/, /yː/). All six ü-words in the
    # WikiPron gold realize the letter as /y/; before this fix ü was absent
    # from the grapheme table and silently dropped instead. ('paüra' has a
    # long /yː/ in the gold that this mapping does not reproduce.)
    assert transcribe("lüganega", "lmo") == "lyɡaneɡa"
    assert transcribe("paüra", "lmo") == "payra"
    assert transcribe("süpa", "lmo") == "sypa"


def test_milanese_entry_applies_source_circumflex_rule_literally():
    # lmo-x-milanese models the classical-Milanese source's own stated
    # circumflex rule (closed+long timbre) rather than lmo's gold-fit
    # reading: ô is /oː/, not the plain /u/ lmo ships to match the
    # WikiPron gold's two attested circumflex-o words.
    assert transcribe("rasô", "lmo-x-milanese") == "rasoː"
    assert transcribe("resô", "lmo-x-milanese") == "resoː"
    assert transcribe("jâld", "lmo-x-milanese") == "jaːld"


def test_milanese_entry_inherits_grave_acute_and_umlaut_from_lmo():
    # The two entries share phonology outside the circumflex series; this
    # must come through *_base inheritance, not a duplicated table.
    assert transcribe("abdicà", "lmo-x-milanese") == "abdika"
    assert transcribe("Giòrgio", "lmo-x-milanese") == "ɡiɔrɡio"
    assert transcribe("süpa", "lmo-x-milanese") == "sypa"
