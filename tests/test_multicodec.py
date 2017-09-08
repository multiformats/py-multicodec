#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `multicodec` package."""

import pytest

from multicodec import add_prefix, remove_prefix, get_codec, extract_prefix
from multicodec.constants import CODECS


@pytest.mark.parametrize('multicodec,prefix', CODECS.items())
def test_verify_prefix_complete(multicodec, prefix):
    data = b'testbytesbuffer'
    prefix_int = prefix['prefix']
    prefixed_data = add_prefix(multicodec, data)

    assert get_codec(prefixed_data) == multicodec
    assert remove_prefix(prefixed_data) == data
    assert extract_prefix(prefixed_data) == prefix_int
