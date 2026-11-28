"""Chinese region and script tags name a spec (#2799)."""
import pytest

from orthography2ipa import get, resolve
from orthography2ipa.json_loader import available_json_codes

# CLDR 49 territoryInfo: yue is 90% of Hong Kong and 86% of Macau; zh_Hant is 95% of Taiwan.
CASES = {
    "zh-HK": "yue", "zh-MO": "yue", "zh-Hant-HK": "yue", "zh-Hans-HK": "yue",
    "zh-Hant-MO": "yue", "zh-hk": "yue",
    "zh-TW": "zh", "zh-Hant": "zh", "zh-Hant-TW": "zh", "cmn-TW": "zh",
}


@pytest.mark.parametrize("tag, spec", sorted(CASES.items()))
def test_a_chinese_tag_resolves_to_its_spec(tag, spec):
    assert resolve(tag) == spec
    assert get(tag).code == spec


def test_every_target_has_a_spec_file():
    assert set(CASES.values()) <= set(available_json_codes())
