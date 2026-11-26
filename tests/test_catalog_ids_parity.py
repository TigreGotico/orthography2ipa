"""The spec files keep their catalog ids until linguatag holds them all.

The atlas, explorer, locations, family and Glottolog check scripts read
``linguatag.catalog_ids``. Each id a spec file declares must equal it.
"""
import glob
import json
import os

import pytest
from linguatag import catalog_ids

DATA = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")
FIELDS = ("glottolog_code", "wikidata_qid")


def _declared():
    for path in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            raw = json.load(fh)
        for field in FIELDS:
            if raw.get(field):
                yield raw["code"], field, raw[field]


def test_every_declared_id_matches_linguatag():
    wrong = [(code, field, value, catalog_ids(code).get(field, "absent"))
             for code, field, value in _declared()
             if catalog_ids(code).get(field) != value]
    assert not wrong, wrong


@pytest.mark.parametrize("code, field, value", [
    ("pt-PT", "glottolog_code", "port1283"),
    ("pt-PT", "wikidata_qid", "Q5146"),
    ("yol", "glottolog_code", "yola1237"),
])
def test_known_ids(code, field, value):
    assert catalog_ids(code)[field] == value
