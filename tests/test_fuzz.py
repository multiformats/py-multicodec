"""Property-based / fuzz tests for parsing helpers.

These tests assert that malformed or random input raises documented
exceptions (or returns a bool) rather than crashing with unexpected errors.
"""

from hypothesis import given
from hypothesis import strategies as st

from multicodec import Code, extract_prefix, get_codec, is_codec


@given(st.binary(max_size=100))
def test_extract_prefix_never_crashes(data: bytes) -> None:
    """extract_prefix should raise ValueError, not crash."""
    try:
        extract_prefix(data)
    except ValueError:
        pass


@given(st.binary(max_size=100))
def test_get_codec_never_crashes(data: bytes) -> None:
    try:
        get_codec(data)
    except ValueError:
        pass


@given(st.text(max_size=100))
def test_code_from_string_never_crashes(text: str) -> None:
    try:
        Code.from_string(text)
    except ValueError:
        pass


@given(st.text(max_size=100))
def test_is_codec_never_crashes(text: str) -> None:
    result = is_codec(text)
    assert isinstance(result, bool)
