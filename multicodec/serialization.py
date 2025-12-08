"""
Serialization module for multicodec.

This module provides a codec interface for serializing and deserializing data
with multicodec prefixes. It includes built-in codecs for common formats:
- JSON: Structured data serialization
- Raw: Pass-through codec for binary data

The design follows a similar pattern to js-multiformats and rust-multicodec,
providing a clean interface for encoding/decoding operations.

Example usage:
    >>> from multicodec.serialization import json_codec, raw_codec, encode, decode
    >>> # Using JSON codec
    >>> data = {"hello": "world"}
    >>> encoded = json_codec.encode(data)
    >>> decoded = json_codec.decode(encoded)
    >>> assert decoded == data
    >>>
    >>> # Using the generic encode/decode with codec name
    >>> encoded = encode("json", {"key": "value"})
    >>> decoded = decode(encoded)
"""

from __future__ import annotations

import json
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

import varint

from .constants import CODE_TABLE
from .exceptions import CodecError, DecodeError, EncodeError, UnknownCodecError

# Type variable for codec data types
T = TypeVar("T")


class Codec(ABC, Generic[T]):
    """
    Abstract base class for multicodec serialization codecs.

    A codec provides methods to encode data to bytes and decode bytes back
    to data. Each codec is identified by its multicodec name and code.

    Subclasses must implement:
    - name: The multicodec name (e.g., 'json', 'raw')
    - code: The multicodec code (e.g., 0x0200 for json)
    - _encode: Transform data to bytes (without prefix)
    - _decode: Transform bytes to data (without prefix)
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the multicodec name for this codec."""
        ...

    @property
    @abstractmethod
    def code(self) -> int:
        """Return the multicodec code for this codec."""
        ...

    @abstractmethod
    def _encode(self, data: T) -> bytes:
        """
        Encode data to bytes without the multicodec prefix.

        :param data: Data to encode
        :return: Encoded bytes without prefix
        :raises EncodeError: If encoding fails
        """
        ...

    @abstractmethod
    def _decode(self, data: bytes) -> T:
        """
        Decode bytes to data, assuming no multicodec prefix.

        :param data: Bytes to decode (without prefix)
        :return: Decoded data
        :raises DecodeError: If decoding fails
        """
        ...

    def encode(self, data: T) -> bytes:
        """
        Encode data to bytes with multicodec prefix.

        :param data: Data to encode
        :return: Multicodec-prefixed encoded bytes
        :raises EncodeError: If encoding fails
        """
        try:
            encoded = self._encode(data)
            prefix = varint.encode(self.code)
            return prefix + encoded
        except EncodeError:
            raise
        except Exception as e:
            raise EncodeError(f"Failed to encode with {self.name}: {e}") from e

    def decode(self, data: bytes) -> T:
        """
        Decode multicodec-prefixed bytes to data.

        :param data: Multicodec-prefixed bytes to decode
        :return: Decoded data
        :raises DecodeError: If decoding fails or codec mismatch
        """
        try:
            # Extract and verify the prefix
            prefix_int = varint.decode_bytes(data)
            if prefix_int != self.code:
                expected_name = CODE_TABLE.get(prefix_int, f"0x{prefix_int:x}")
                raise DecodeError(
                    f"Codec mismatch: expected {self.name} (0x{self.code:x}), got {expected_name} (0x{prefix_int:x})"
                )

            # Remove prefix and decode
            prefix_bytes = varint.encode(prefix_int)
            payload = data[len(prefix_bytes) :]
            return self._decode(payload)
        except DecodeError:
            raise
        except Exception as e:
            raise DecodeError(f"Failed to decode with {self.name}: {e}") from e

    def decode_raw(self, data: bytes) -> T:
        """
        Decode bytes without expecting a multicodec prefix.

        :param data: Raw bytes to decode (no prefix)
        :return: Decoded data
        :raises DecodeError: If decoding fails
        """
        try:
            return self._decode(data)
        except DecodeError:
            raise
        except Exception as e:
            raise DecodeError(f"Failed to decode raw data with {self.name}: {e}") from e

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name={self.name!r}, code=0x{self.code:x})>"


class JSONCodec(Codec[Any]):
    """
    JSON codec for encoding/decoding JSON-serializable data.

    Uses the standard library json module with UTF-8 encoding.
    The multicodec code for JSON is 0x0200.

    Example:
        >>> codec = JSONCodec()
        >>> encoded = codec.encode({"hello": "world"})
        >>> decoded = codec.decode(encoded)
        >>> assert decoded == {"hello": "world"}
    """

    @property
    def name(self) -> str:
        return "json"

    @property
    def code(self) -> int:
        return 0x0200  # json multicodec code

    def _encode(self, data: Any) -> bytes:
        """Encode data as JSON bytes."""
        try:
            return json.dumps(data, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        except (TypeError, ValueError) as e:
            raise EncodeError(f"Data is not JSON serializable: {e}") from e

    def _decode(self, data: bytes) -> Any:
        """Decode JSON bytes to Python object."""
        try:
            return json.loads(data.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            raise DecodeError(f"Invalid JSON data: {e}") from e


class RawCodec(Codec[bytes]):
    """
    Raw codec for pass-through binary data.

    This codec performs no transformation on the data, useful for
    binary data that should be stored as-is with a multicodec prefix.
    The multicodec code for raw is 0x55.

    Example:
        >>> codec = RawCodec()
        >>> data = b"binary data"
        >>> encoded = codec.encode(data)
        >>> decoded = codec.decode(encoded)
        >>> assert decoded == data
    """

    @property
    def name(self) -> str:
        return "raw"

    @property
    def code(self) -> int:
        return 0x55  # raw multicodec code

    def _encode(self, data: bytes) -> bytes:
        """Pass through bytes unchanged."""
        if not isinstance(data, bytes):
            raise EncodeError(f"RawCodec expects bytes, got {type(data).__name__}")
        return data

    def _decode(self, data: bytes) -> bytes:
        """Pass through bytes unchanged."""
        return data


# Singleton codec instances for convenience
json_codec = JSONCodec()
raw_codec = RawCodec()


# Codec registry for dynamic codec lookup
_codec_registry: dict[str, Codec[Any]] = {
    "json": json_codec,
    "raw": raw_codec,
}


def register_codec(codec: Codec[Any]) -> None:
    """
    Register a custom codec in the global registry.

    :param codec: The codec instance to register
    :raises ValueError: If codec name is already registered
    """
    if codec.name in _codec_registry:
        raise ValueError(f"Codec '{codec.name}' is already registered")
    _codec_registry[codec.name] = codec


def unregister_codec(name: str) -> None:
    """
    Unregister a codec from the global registry.

    :param name: The codec name to unregister
    :raises KeyError: If codec is not registered
    """
    if name not in _codec_registry:
        raise KeyError(f"Codec '{name}' is not registered")
    del _codec_registry[name]


def get_registered_codec(name: str) -> Codec[Any]:
    """
    Get a registered codec by name.

    :param name: The codec name
    :return: The codec instance
    :raises UnknownCodecError: If codec is not registered
    """
    try:
        return _codec_registry[name]
    except KeyError:
        raise UnknownCodecError(f"Codec '{name}' is not registered") from None


def list_registered_codecs() -> list[str]:
    """
    List all registered codec names.

    :return: List of registered codec names
    """
    return list(_codec_registry.keys())


def encode(codec_name: str, data: Any) -> bytes:
    """
    Encode data using a registered codec by name.

    :param codec_name: Name of the codec to use (e.g., 'json', 'raw')
    :param data: Data to encode
    :return: Multicodec-prefixed encoded bytes
    :raises UnknownCodecError: If codec is not registered
    :raises EncodeError: If encoding fails
    """
    codec = get_registered_codec(codec_name)
    return codec.encode(data)


def decode(data: bytes, codec_name: str | None = None) -> Any:
    """
    Decode multicodec-prefixed data.

    If codec_name is provided, uses that specific codec (and verifies prefix matches).
    If codec_name is None, auto-detects codec from the prefix.

    :param data: Multicodec-prefixed bytes to decode
    :param codec_name: Optional codec name to use for decoding
    :return: Decoded data
    :raises UnknownCodecError: If codec is not registered
    :raises DecodeError: If decoding fails or codec mismatch
    """
    if codec_name is not None:
        codec = get_registered_codec(codec_name)
        return codec.decode(data)

    # Auto-detect codec from prefix
    try:
        prefix_int = varint.decode_bytes(data)
    except TypeError as e:
        raise DecodeError(f"Invalid varint prefix: {e}") from e

    codec_name_detected = CODE_TABLE.get(prefix_int)
    if codec_name_detected is None:
        raise DecodeError(f"Unknown codec prefix: 0x{prefix_int:x}")

    if codec_name_detected not in _codec_registry:
        raise UnknownCodecError(
            f"Codec '{codec_name_detected}' (0x{prefix_int:x}) is not registered. "
            f"Available codecs: {list_registered_codecs()}"
        )

    return _codec_registry[codec_name_detected].decode(data)


def is_codec_registered(name: str) -> bool:
    """
    Check if a codec is registered.

    :param name: The codec name to check
    :return: True if codec is registered, False otherwise
    """
    return name in _codec_registry


__all__ = [
    # Base classes
    "Codec",
    # Exceptions
    "CodecError",
    "DecodeError",
    "EncodeError",
    "JSONCodec",
    # Built-in codecs
    "RawCodec",
    "UnknownCodecError",
    # Generic functions
    "decode",
    "encode",
    "get_registered_codec",
    "is_codec_registered",
    # Codec instances
    "json_codec",
    "list_registered_codecs",
    "raw_codec",
    # Registry functions
    "register_codec",
    "unregister_codec",
]
