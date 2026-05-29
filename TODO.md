# TODO — orthography2ipa

## Future work

- [ ] Bundle a neural Arabic diacritizer (tashkeel) ONNX model and wire it into `orthography2ipa/plugins/tashkeel.py` (load via `huggingface_hub`, decode predicted harakat onto the consonant skeleton).
- [ ] Populate phonology for metadata-only stubs that still carry no graphemes/allophones (e.g. `oc` and other ancestry placeholders).
