import json

import pytest
from pydantic import ValidationError

from orthography2ipa.schema import validate_spec_file

MINIMAL = {"code": "xx-x-test", "name": "Test", "script": "Latin"}


def _write(tmp_path, **keys):
    path = tmp_path / "xx-x-test.json"
    path.write_text(json.dumps({**MINIMAL, **keys}))
    return path


def test_the_deprecated_parent_key_validates(tmp_path):
    assert validate_spec_file(_write(tmp_path, parent="pt")).parent == "pt"


def test_inherits_and_parent_together_are_refused(tmp_path):
    with pytest.raises(ValidationError, match="both inherits and"):
        validate_spec_file(_write(tmp_path, parent="pt", inherits="pt"))
