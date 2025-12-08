"""
Exception classes for multicodec.

This module defines the exception hierarchy for multicodec operations,
providing specific error types for different failure modes.
"""


class MulticodecError(Exception):
    """Base exception for all multicodec-related errors."""

    pass


class CodecError(MulticodecError):
    """Base exception for codec-related errors."""

    pass


class EncodeError(CodecError):
    """Raised when encoding fails."""

    pass


class DecodeError(CodecError):
    """Raised when decoding fails."""

    pass


class UnknownCodecError(CodecError):
    """Raised when an unknown codec is requested."""

    pass


__all__ = [
    "CodecError",
    "DecodeError",
    "EncodeError",
    "MulticodecError",
    "UnknownCodecError",
]
