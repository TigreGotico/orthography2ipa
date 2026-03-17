"""tashkeel — Optional ONNX-based Arabic diacritizer.

Requires ``onnxruntime`` (available via ``pip install orthography2ipa[arabic]``).
If not installed, the plugin falls back to undiacritized input.
"""
from __future__ import annotations

__all__ = ["TashkeelDiacritizer"]


class TashkeelDiacritizer:
    """Wrapper for ONNX-based Arabic diacritization model.

    This is a placeholder for future integration. The actual ONNX model
    and inference logic will be added when the model is available.
    """

    def __init__(self) -> None:
        try:
            import onnxruntime  # noqa: F401
            self._available = True
        except ImportError:
            self._available = False

    def diacritize(self, text: str) -> str:
        """Add diacritics to undiacritized Arabic text.

        Returns input unchanged if ONNX model is not available.
        """
        if not self._available:
            return text
        # TODO: Load and run ONNX model for diacritization
        return text
