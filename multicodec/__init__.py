"""Top-level package for py-multicodec."""

__author__ = """Dhruv Baldawa"""
__email__ = "dhruv@dhruvb.com"
__version__ = "0.2.1"

# Core Code type
from .code import (
    RESERVED_END,
    RESERVED_START,
    Code,
    is_reserved,
    known_codes,
)

# Original multicodec functions
from .multicodec import add_prefix, extract_prefix, get_codec, get_prefix, is_codec, remove_prefix

__all__ = [
    "RESERVED_END",
    # Constants
    "RESERVED_START",
    # Code type
    "Code",
    # Original functions
    "add_prefix",
    "extract_prefix",
    "get_codec",
    "get_prefix",
    "is_codec",
    "is_reserved",
    # Functions
    "known_codes",
    "remove_prefix",
]
