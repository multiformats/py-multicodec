#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `multicodec` package."""

import pytest

from multicodec import add_prefix, remove_prefix, get_codec
from multicodec.constants import CODECS


@pytest.fixture(scope='module', params=CODECS.items())
def sample(request):
    return request.param


def test_verify_prefix_complete(sample):
    data = b'testbytesbuffer'
    multicodec, prefix_int = sample[0], sample[1]['prefix']
    prefixed_data = add_prefix(multicodec, data)

    assert get_codec(prefixed_data) == multicodec
    assert remove_prefix(prefixed_data) == data
