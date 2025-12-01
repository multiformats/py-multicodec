"""Top-level package for py-multicodec."""

__author__ = """Dhruv Baldawa"""
__email__ = "dhruv@dhruvb.com"
__version__ = "0.2.1"

from .multicodec import add_prefix, extract_prefix, get_codec, get_prefix, is_codec, remove_prefix

__all__ = [
    "add_prefix",
    "extract_prefix",
    "get_codec",
    "get_prefix",
    "is_codec",
    "remove_prefix",
]
