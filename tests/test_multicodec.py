#!/usr/bin/env python
"""Tests for `multicodec` package."""

import pytest
import varint

from multicodec import add_prefix, extract_prefix, get_codec, get_prefix, is_codec, remove_prefix
from multicodec.constants import CODECS

INVALID_CODECS = (
    ("abc", 0x101),
    ("def", 0xFFFFF),
    ("deadbeef", 0xDEADBEEF),
)


@pytest.mark.parametrize("multicodec,prefix", CODECS.items())
def test_verify_prefix_complete(multicodec, prefix):
    data = b"testbytesbuffer"
    prefix_int = prefix["prefix"]
    prefixed_data = add_prefix(multicodec, data)

    assert is_codec(multicodec)
    assert get_codec(prefixed_data) == multicodec
    assert remove_prefix(prefixed_data) == data
    assert extract_prefix(prefixed_data) == prefix_int


@pytest.mark.parametrize("multicodec,_", INVALID_CODECS)
def test_get_prefix_invalid_prefix(multicodec, _):
    with pytest.raises(ValueError) as excinfo:
        get_prefix(multicodec)
    assert "multicodec is not supported" in str(excinfo.value)


@pytest.mark.parametrize("_,prefix", INVALID_CODECS)
def test_get_codec_invalid_prefix(_, prefix):
    prefix_bytes = varint.encode(prefix)
    with pytest.raises(ValueError) as excinfo:
        get_codec(prefix_bytes)
    assert "not present in the lookup table" in str(excinfo.value)


@pytest.mark.parametrize("multicodec,_", INVALID_CODECS)
def test_is_codec_invalid_prefix(multicodec, _):
    assert not is_codec(multicodec)


def test_extract_prefix_invalid_varint():
    with pytest.raises(ValueError) as excinfo:
        extract_prefix(b"\xff")
    assert "incorrect varint provided" in str(excinfo.value)
