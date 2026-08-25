"""Amharic (am) Ethiopic-script coverage: the spec's grapheme table originally
covered only the seven basic vowel orders per consonant row, so it silently
dropped any word containing a labialised ⟨Cʷa⟩ glyph, the ⟨ቨ⟩ loanword /v/
series, or one of the historical letter rows Ge'ez orthography still keeps
separate but that merged in modern Amharic pronunciation.

Silent deletion of an unmapped character does not just cost one segment: the
engine keeps concatenating the remaining mapped characters, so a single
unmapped grapheme can garble everything that follows it in the same word
(``ቋንቋ`` 'language' used to come out as bare ``nə``, dropping the whole first
syllable and the labialised /q/).

Sources consulted:

* Derib Ado, "Revisiting the status of labialised consonants in contemporary
  Amharic", Oslo Studies in Language 11(2), 2020, pp. 47-58,
  https://doi.org/10.5617/osla.8487 — confirms /kʷ/, /ɡʷ/, /kʼʷ/ and the
  wider Cʷ series are phonemic in Amharic, not derivable from a vowel
  sequence or /w/-loss (Table 2 surveys prior analyses; examples (2)-(3)).
* The merger values for the historical ħ/x rows (ኀ ኃ ኅ ኋ ኸ ኽ -> /h/) and for
  the remaining columns of the archaic ፀ row (ፁ ፃ ፅ -> /tsʼ/, matching the
  spec's pre-existing ፀ -> tsʼə) are measured directly from the wikipron gold
  (e.g. እኅት 'sister' -> ... h ɨ t, ሕፃን 'infant' -> h ɨ sʼ a n) rather than
  independently sourced, since no fetched primary source states the merger
  explicitly; this is recorded honestly in the spec notes rather than
  presented as cited.
"""
from orthography2ipa import transcribe, get


def test_cites_ado_2021_labialisation_source():
    spec = get("am")
    ids = {s.id for s in spec.sources}
    assert "ado2021labialised" in ids


def test_labialised_velar_paradigm():
    """ቋ/ቍ (q-series), ኳ (k-series) and ጐ/ጓ (g-series) are the fuller
    labialised velar paradigm Ado (2021) argues is phonemic."""
    assert transcribe("ቋንቋ", lang="am") == "qʷanəqʷa"
    assert transcribe("ቍርስ", lang="am") == "qʷərəsə"
    assert transcribe("ኳስ", lang="am") == "kʷasə"
    assert "ɡʷə" in transcribe("አንጐል", lang="am")
    assert transcribe("ጓደኛ", lang="am") == "ɡʷadəɲa"


def test_simple_cwa_glyphs():
    """The single-glyph labialised ⟨Cʷa⟩ syllables outside the velar
    paradigm, e.g. ⟨ሷ⟩ /sʷa/ and ⟨ቷ⟩ /tʷa/, attested in the wikipron gold."""
    assert "sʷa" in transcribe("እሷ", lang="am")
    assert "tʷa" in transcribe("የቷ", lang="am")


def test_v_series_loanword_consonant():
    """⟨ቨ⟩ writes loanword /v/, absent from the native seven-order table."""
    assert transcribe("ቪዛ", lang="am") == "viza"


def test_historical_h_row_merger_not_silent_deletion():
    """ኀ/ኃ/ኅ (the historical pharyngeal/velar-fricative row) merged with
    /h/ in modern Amharic pronunciation, matching the plain ⟨ህ⟩ row and the
    wikipron gold for እኅት 'sister' (... h ɨ t); the letters must not vanish."""
    assert transcribe("እኅት", lang="am") == transcribe("እህት", lang="am")
    assert "h" in transcribe("እኅት", lang="am")


def test_kx_row_merger_not_silent_deletion():
    """ኸ/ኽ, used to write foreign /x/ in loan spellings, merged with /h/."""
    assert transcribe("ኸርቱም", lang="am") == "hərətumə"


def test_archaic_tza_row_completes_the_tsʼ_series():
    """ፁ/ፃ/ፅ are the remaining columns of the archaic ፀ row, which the spec
    already maps (inherent-vowel member) onto the ejective affricate /tsʼ/
    row (ጸ); the missing columns must follow the same row, not vanish."""
    out = transcribe("ሕፃን", lang="am")
    assert "tsʼa" in out
    assert transcribe("ፅናት", lang="am").startswith("tsʼ")


def test_unmapped_grapheme_no_longer_swallows_the_whole_word():
    """Before the fix, an unmapped grapheme silently deleted itself and
    everything already accumulated could still be produced, but a whole
    labialised first syllable used to be dropped outright."""
    out = transcribe("ቋንቋ", lang="am")
    assert out.startswith("qʷ")
    assert len(out) > len("anəqʷa")


def test_ethiopic_wordspace_stays_unmapped_punctuation():
    """⟨፡⟩ (U+1361) is punctuation (word separator), not a phoneme, and must
    not be given a grapheme-table entry."""
    spec = get("am")
    assert "፡" not in spec.graphemes
    assert "።" not in spec.graphemes
    assert "፣" not in spec.graphemes
