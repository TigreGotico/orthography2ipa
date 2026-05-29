"""tashkeel — optional ONNX-based Arabic diacritizer.

Modern Standard Arabic is usually written without short-vowel diacritics
(*harakat*). Restoring them (*tashkeel*) is a prerequisite for accurate
grapheme-to-phoneme transcription, because the same consonant skeleton maps
to different pronunciations depending on the omitted vowels.

This module exposes :class:`TashkeelDiacritizer`, a thin wrapper intended to
run a neural diacritization model via ``onnxruntime`` (available through
``pip install orthography2ipa[arabic]``). The model and its tokenizer are not
yet bundled, so the diacritizer currently returns its input unchanged and the
rule-based :class:`~orthography2ipa.plugins.arabic_g2p.ArabicG2PPlugin` falls
back to transcribing whatever diacritics are already present in the text.

Wiring in a model requires three model-specific pieces: the ONNX graph, the
input character-to-id vocabulary, and the harakat decoding scheme for the
output logits. Once those are settled the inference call slots into
:meth:`TashkeelDiacritizer.diacritize`.
"""
from __future__ import annotations

__all__ = ["TashkeelDiacritizer"]


class TashkeelDiacritizer:
    """Wrapper for an ONNX-based Arabic diacritization model.

    The wrapper degrades gracefully: if ``onnxruntime`` is unavailable, or no
    model has been wired in, :meth:`diacritize` returns its input unchanged.
    """

    def __init__(self) -> None:
        try:
            import onnxruntime  # noqa: F401
            self._available = True
        except ImportError:
            self._available = False
        # Future: load the ONNX session and tokenizer vocabulary here, e.g.
        #   from huggingface_hub import hf_hub_download
        #   path = hf_hub_download(repo_id=..., filename="model.onnx")
        #   self._session = onnxruntime.InferenceSession(path)
        self._session = None

    @property
    def available(self) -> bool:
        """True when a model is loaded and ready to diacritize."""
        return self._available and self._session is not None

    def diacritize(self, text: str) -> str:
        """Restore short-vowel diacritics on undiacritized Arabic text.

        Returns the input unchanged when no model is loaded.
        """
        if not self.available:
            return text
        # Future: tokenize ``text``, run ``self._session``, decode the
        # predicted harakat back onto the consonant skeleton.
        return text
