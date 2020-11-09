#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `multicodec` package."""

import pytest
import varint

from multicodec import Multicodec
from multicodec.constants import CODECS


INVALID_CODECS = (
    ('abc', 0x02),
    ('def', 0xfffff),
    ('deadbeef', 0xdeadbeef),
)


@pytest.mark.parametrize('multicodec,prefix', CODECS.items())
def test_verify_prefix_complete(multicodec, prefix):
    mc = Multicodec()
    data = b'testbytesbuffer'
    prefix_int = prefix['prefix']
    prefixed_data = mc.add_prefix(multicodec, data)

    assert mc.is_codec(multicodec)
    assert mc.get_codec(prefixed_data) == multicodec
    assert mc.remove_prefix(prefixed_data) == data
    assert mc.extract_prefix(prefixed_data) == prefix_int


@pytest.mark.parametrize('multicodec,_', INVALID_CODECS)
def test_get_prefix_invalid_prefix(multicodec, _):
    mc = Multicodec()
    with pytest.raises(ValueError) as excinfo:
        mc.get_prefix(multicodec)
    assert 'multicodec is not supported' in str(excinfo.value)


@pytest.mark.parametrize('_,prefix', INVALID_CODECS)
def test_get_codec_invalid_prefix(_, prefix):
    mc = Multicodec()
    prefix_bytes = varint.encode(prefix)
    with pytest.raises(ValueError) as excinfo:
        mc.get_codec(prefix_bytes)
    assert 'not present in the lookup table' in str(excinfo.value)


@pytest.mark.parametrize('multicodec,_', INVALID_CODECS)
def test_is_codec_invalid_prefix(multicodec, _):
    mc = Multicodec()
    assert not mc.is_codec(multicodec)


def test_extract_prefix_invalid_varint():
    mc = Multicodec()
    with pytest.raises(ValueError) as excinfo:
        mc.extract_prefix(b'\xff')
    assert 'incorrect varint provided' in str(excinfo.value)
