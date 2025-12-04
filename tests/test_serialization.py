#!/usr/bin/env python
"""Tests for serialization module."""

import pytest

from multicodec import (
    Codec,
    CodecError,
    DecodeError,
    EncodeError,
    JSONCodec,
    MulticodecError,
    RawCodec,
    UnknownCodecError,
    decode,
    encode,
    get_registered_codec,
    is_codec_registered,
    json_codec,
    list_registered_codecs,
    raw_codec,
    register_codec,
    unregister_codec,
)


class JSONCodecTestCase:
    """Tests for the JSONCodec class."""

    def test_codec_properties(self):
        """Test codec name and code properties."""
        codec = JSONCodec()
        assert codec.name == "json"
        assert codec.code == 0x0200

    def test_encode_simple_dict(self):
        """Test encoding a simple dictionary."""
        codec = JSONCodec()
        data = {"hello": "world"}
        encoded = codec.encode(data)
        # Should have prefix (0x0200 as varint) + JSON bytes
        assert encoded.startswith(b"\x80\x04")  # varint for 0x0200
        assert b"hello" in encoded
        assert b"world" in encoded

    def test_encode_decode_roundtrip(self):
        """Test encoding and decoding preserves data."""
        codec = JSONCodec()
        test_cases = [
            {"hello": "world"},
            [1, 2, 3, 4, 5],
            {"nested": {"key": "value"}, "list": [1, 2, 3]},
            "simple string",
            123,
            123.456,
            True,
            False,
            None,
        ]
        for data in test_cases:
            encoded = codec.encode(data)
            decoded = codec.decode(encoded)
            assert decoded == data, f"Failed for {data}"

    def test_encode_unicode(self):
        """Test encoding Unicode data."""
        codec = JSONCodec()
        data = {"emoji": "🎉", "chinese": "你好", "arabic": "مرحبا"}
        encoded = codec.encode(data)
        decoded = codec.decode(encoded)
        assert decoded == data

    def test_encode_non_serializable_raises(self):
        """Test encoding non-JSON-serializable data raises EncodeError."""
        codec = JSONCodec()
        with pytest.raises(EncodeError) as excinfo:
            codec.encode({"func": lambda x: x})
        assert "not JSON serializable" in str(excinfo.value)

    def test_decode_invalid_json_raises(self):
        """Test decoding invalid JSON raises DecodeError."""
        codec = JSONCodec()
        # Create a properly prefixed but invalid JSON payload
        prefix = b"\x80\x04"  # varint for 0x0200
        invalid_json = prefix + b"not valid json"
        with pytest.raises(DecodeError) as excinfo:
            codec.decode(invalid_json)
        assert "Invalid JSON data" in str(excinfo.value)

    def test_decode_wrong_codec_raises(self):
        """Test decoding with wrong codec prefix raises DecodeError."""
        codec = JSONCodec()
        # Use raw codec prefix (0x55)
        raw_prefixed = b"\x55" + b'{"hello": "world"}'
        with pytest.raises(DecodeError) as excinfo:
            codec.decode(raw_prefixed)
        assert "Codec mismatch" in str(excinfo.value)

    def test_decode_raw(self):
        """Test decoding without prefix using decode_raw."""
        codec = JSONCodec()
        raw_json = b'{"hello": "world"}'
        decoded = codec.decode_raw(raw_json)
        assert decoded == {"hello": "world"}

    def test_repr(self):
        """Test codec string representation."""
        codec = JSONCodec()
        repr_str = repr(codec)
        assert "JSONCodec" in repr_str
        assert "json" in repr_str
        assert "0x200" in repr_str


class RawCodecTestCase:
    """Tests for the RawCodec class."""

    def test_codec_properties(self):
        """Test codec name and code properties."""
        codec = RawCodec()
        assert codec.name == "raw"
        assert codec.code == 0x55

    def test_encode_bytes(self):
        """Test encoding bytes."""
        codec = RawCodec()
        data = b"binary data"
        encoded = codec.encode(data)
        # Should have prefix (0x55 as varint) + raw bytes
        assert encoded.startswith(b"\x55")
        assert encoded[1:] == data

    def test_encode_decode_roundtrip(self):
        """Test encoding and decoding preserves data."""
        codec = RawCodec()
        test_cases = [
            b"hello world",
            b"\x00\x01\x02\x03",
            b"",
            bytes(range(256)),
        ]
        for data in test_cases:
            encoded = codec.encode(data)
            decoded = codec.decode(encoded)
            assert decoded == data, f"Failed for {data!r}"

    def test_encode_non_bytes_raises(self):
        """Test encoding non-bytes data raises EncodeError."""
        codec = RawCodec()
        with pytest.raises(EncodeError) as excinfo:
            codec.encode("not bytes")  # type: ignore
        assert "expects bytes" in str(excinfo.value)

    def test_decode_wrong_codec_raises(self):
        """Test decoding with wrong codec prefix raises DecodeError."""
        codec = RawCodec()
        # Use JSON codec prefix (0x0200)
        json_prefixed = b"\x80\x04" + b"some data"
        with pytest.raises(DecodeError) as excinfo:
            codec.decode(json_prefixed)
        assert "Codec mismatch" in str(excinfo.value)

    def test_repr(self):
        """Test codec string representation."""
        codec = RawCodec()
        repr_str = repr(codec)
        assert "RawCodec" in repr_str
        assert "raw" in repr_str
        assert "0x55" in repr_str


class SingletonCodecsTestCase:
    """Tests for singleton codec instances."""

    def test_json_codec_instance(self):
        """Test json_codec is a JSONCodec instance."""
        assert isinstance(json_codec, JSONCodec)
        assert json_codec.name == "json"

    def test_raw_codec_instance(self):
        """Test raw_codec is a RawCodec instance."""
        assert isinstance(raw_codec, RawCodec)
        assert raw_codec.name == "raw"


class CodecRegistryTestCase:
    """Tests for codec registry functions."""

    def test_list_registered_codecs(self):
        """Test listing registered codecs."""
        codecs = list_registered_codecs()
        assert "json" in codecs
        assert "raw" in codecs

    def test_is_codec_registered(self):
        """Test checking if codec is registered."""
        assert is_codec_registered("json")
        assert is_codec_registered("raw")
        assert not is_codec_registered("nonexistent")

    def test_get_registered_codec(self):
        """Test getting registered codec."""
        codec = get_registered_codec("json")
        assert isinstance(codec, JSONCodec)

    def test_get_unregistered_codec_raises(self):
        """Test getting unregistered codec raises UnknownCodecError."""
        with pytest.raises(UnknownCodecError) as excinfo:
            get_registered_codec("nonexistent")
        assert "not registered" in str(excinfo.value)

    def test_register_custom_codec(self):
        """Test registering a custom codec."""

        class CustomCodec(Codec[str]):
            @property
            def name(self) -> str:
                return "custom"

            @property
            def code(self) -> int:
                return 0x9999

            def _encode(self, data: str) -> bytes:
                return data.encode("utf-8")

            def _decode(self, data: bytes) -> str:
                return data.decode("utf-8")

        codec = CustomCodec()
        try:
            register_codec(codec)
            assert is_codec_registered("custom")
            assert get_registered_codec("custom") is codec
        finally:
            # Clean up
            unregister_codec("custom")

    def test_register_duplicate_raises(self):
        """Test registering duplicate codec raises ValueError."""
        with pytest.raises(ValueError) as excinfo:
            register_codec(json_codec)
        assert "already registered" in str(excinfo.value)

    def test_unregister_codec(self):
        """Test unregistering a codec."""

        class TempCodec(Codec[str]):
            @property
            def name(self) -> str:
                return "temp"

            @property
            def code(self) -> int:
                return 0x8888

            def _encode(self, data: str) -> bytes:
                return data.encode()

            def _decode(self, data: bytes) -> str:
                return data.decode()

        codec = TempCodec()
        register_codec(codec)
        assert is_codec_registered("temp")
        unregister_codec("temp")
        assert not is_codec_registered("temp")

    def test_unregister_nonexistent_raises(self):
        """Test unregistering nonexistent codec raises KeyError."""
        with pytest.raises(KeyError) as excinfo:
            unregister_codec("nonexistent")
        assert "not registered" in str(excinfo.value)


class GenericEncodeDecodeTestCase:
    """Tests for generic encode/decode functions."""

    def test_encode_with_json(self):
        """Test generic encode with JSON codec."""
        data = {"key": "value"}
        encoded = encode("json", data)
        assert encoded.startswith(b"\x80\x04")

    def test_encode_with_raw(self):
        """Test generic encode with raw codec."""
        data = b"binary data"
        encoded = encode("raw", data)
        assert encoded.startswith(b"\x55")

    def test_encode_unknown_codec_raises(self):
        """Test encoding with unknown codec raises UnknownCodecError."""
        with pytest.raises(UnknownCodecError):
            encode("nonexistent", {"data": "value"})

    def test_decode_with_codec_name(self):
        """Test decode with explicit codec name."""
        encoded = encode("json", {"hello": "world"})
        decoded = decode(encoded, "json")
        assert decoded == {"hello": "world"}

    def test_decode_auto_detect(self):
        """Test decode with auto-detection."""
        # JSON
        json_encoded = encode("json", {"hello": "world"})
        json_decoded = decode(json_encoded)
        assert json_decoded == {"hello": "world"}

        # Raw
        raw_encoded = encode("raw", b"binary data")
        raw_decoded = decode(raw_encoded)
        assert raw_decoded == b"binary data"

    def test_decode_unknown_prefix_raises(self):
        """Test decoding unknown prefix raises DecodeError."""
        # Use an unknown prefix
        unknown_data = b"\xff\xff\xff\x07" + b"some data"  # Large unknown prefix
        with pytest.raises(DecodeError) as excinfo:
            decode(unknown_data)
        assert "Unknown codec prefix" in str(excinfo.value)

    def test_decode_unregistered_codec_raises(self):
        """Test decoding with unregistered codec raises UnknownCodecError."""
        # Use a valid multicodec prefix that's not registered (e.g., cbor = 0x51)
        import varint as varint_lib

        cbor_prefix = varint_lib.encode(0x51)  # cbor codec
        data = cbor_prefix + b"\xa1\x65hello\x65world"  # some CBOR-ish data
        with pytest.raises(UnknownCodecError) as excinfo:
            decode(data)
        assert "not registered" in str(excinfo.value)

    def test_decode_invalid_varint_raises(self):
        """Test decoding invalid varint raises DecodeError."""
        with pytest.raises(DecodeError) as excinfo:
            decode(b"\xff")  # Invalid varint
        assert "Invalid varint prefix" in str(excinfo.value)


class ExceptionsTestCase:
    """Tests for exception hierarchy."""

    def test_exception_hierarchy(self):
        """Test exception inheritance."""
        assert issubclass(CodecError, MulticodecError)
        assert issubclass(EncodeError, CodecError)
        assert issubclass(DecodeError, CodecError)
        assert issubclass(UnknownCodecError, CodecError)
        assert issubclass(MulticodecError, Exception)

    def test_encode_error_message(self):
        """Test EncodeError message."""
        err = EncodeError("test error")
        assert str(err) == "test error"

    def test_decode_error_message(self):
        """Test DecodeError message."""
        err = DecodeError("test error")
        assert str(err) == "test error"

    def test_unknown_codec_error_message(self):
        """Test UnknownCodecError message."""
        err = UnknownCodecError("test error")
        assert str(err) == "test error"


class EdgeCasesTestCase:
    """Tests for edge cases."""

    def test_empty_json_object(self):
        """Test encoding/decoding empty JSON object."""
        codec = JSONCodec()
        encoded = codec.encode({})
        decoded = codec.decode(encoded)
        assert decoded == {}

    def test_empty_json_array(self):
        """Test encoding/decoding empty JSON array."""
        codec = JSONCodec()
        encoded = codec.encode([])
        decoded = codec.decode(encoded)
        assert decoded == []

    def test_empty_raw_bytes(self):
        """Test encoding/decoding empty bytes."""
        codec = RawCodec()
        encoded = codec.encode(b"")
        decoded = codec.decode(encoded)
        assert decoded == b""

    def test_large_json_data(self):
        """Test encoding/decoding large JSON data."""
        codec = JSONCodec()
        data = {"items": list(range(10000))}
        encoded = codec.encode(data)
        decoded = codec.decode(encoded)
        assert decoded == data

    def test_large_raw_data(self):
        """Test encoding/decoding large raw data."""
        codec = RawCodec()
        data = bytes(range(256)) * 1000
        encoded = codec.encode(data)
        decoded = codec.decode(encoded)
        assert decoded == data

    def test_deeply_nested_json(self):
        """Test encoding/decoding deeply nested JSON."""
        codec = JSONCodec()
        # Create deeply nested structure
        data: dict = {"level": 0}
        current = data
        for i in range(1, 50):
            current["nested"] = {"level": i}
            current = current["nested"]
        encoded = codec.encode(data)
        decoded = codec.decode(encoded)
        assert decoded == data
