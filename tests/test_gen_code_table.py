"""Tests for tag-based categorization in gen_code_table."""

import importlib.util
from pathlib import Path

_SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "gen_code_table.py"
_SPEC = importlib.util.spec_from_file_location("gen_code_table", _SCRIPT)
assert _SPEC and _SPEC.loader
_MOD = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MOD)

categorize = _MOD.categorize
name_to_const = _MOD.name_to_const


def test_categorize_uses_tag_not_name_patterns():
    # Would be misclassified as multihash by old "sha" substring patterns
    assert categorize("sha2-256", {"prefix": 0x12, "tag": "multihash"}) == "multihash"
    assert categorize("iscc", {"prefix": 0xCC01, "tag": "softhash"}) == "softhash"
    assert categorize("nonce", {"prefix": 0x123B, "tag": "nonce"}) == "nonce"
    assert categorize("vlad", {"prefix": 0x1207, "tag": "vlad"}) == "vlad"


def test_categorize_none_and_missing_go_to_other():
    assert categorize("x", {"prefix": 1, "tag": "none"}) == "other"
    assert categorize("y", {"prefix": 2, "tag": ""}) == "other"
    assert categorize("z", {"prefix": 3}) == "other"


def test_name_to_const():
    assert name_to_const("sha2-256") == "SHA2_256"
    assert name_to_const("dag-cbor") == "DAG_CBOR"
