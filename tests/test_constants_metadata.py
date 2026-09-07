"""Smoke tests for enriched CODECS metadata from update-table.py."""

from multicodec.constants import CODE_TABLE, CODECS, NAME_TABLE


def test_codecs_include_csv_metadata_keys():
    sample = CODECS["sha2-256"]
    assert sample["prefix"] == 0x12
    assert sample["tag"] == "multihash"
    assert sample["status"] in {"permanent", "draft", "deprecated"}
    assert "description" in sample


def test_identity_preserves_description():
    sample = CODECS["identity"]
    assert sample["prefix"] == 0x00
    assert sample["tag"] == "multihash"
    assert sample["status"] == "permanent"
    assert "binary" in sample["description"]


def test_name_and_code_tables_still_use_prefix():
    assert NAME_TABLE["sha2-256"] == 0x12
    assert CODE_TABLE[0x12] == "sha2-256"
