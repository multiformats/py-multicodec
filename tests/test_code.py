#!/usr/bin/env python
"""Tests for Code type."""

import pytest

from multicodec import RESERVED_END, RESERVED_START, Code, is_reserved, known_codes


class CodeTestCase:
    """Tests for Code type."""

    def test_code_from_int(self):
        """Test creating Code from integer."""
        code = Code(0x12)
        assert int(code) == 0x12
        assert str(code) == "sha2-256"

    def test_code_from_string_name(self):
        """Test Code.from_string with codec name."""
        code = Code.from_string("sha2-256")
        assert int(code) == 0x12

    def test_code_from_string_hex(self):
        """Test Code.from_string with hex number."""
        code = Code.from_string("0x12")
        assert int(code) == 0x12
        assert str(code) == "sha2-256"

    def test_code_from_string_decimal(self):
        """Test Code.from_string with decimal number."""
        code = Code.from_string("18")
        assert int(code) == 0x12

    def test_code_from_string_reserved(self):
        """Test Code.from_string with reserved range number."""
        code = Code.from_string("0x300001")
        assert int(code) == 0x300001

    def test_code_from_string_invalid(self):
        """Test Code.from_string with invalid input."""
        with pytest.raises(ValueError) as excinfo:
            Code.from_string("nonexistent-codec")
        assert "unknown multicodec" in str(excinfo.value)

    def test_code_set(self):
        """Test Code.set method."""
        code = Code(0)
        code.set("sha2-256")
        assert int(code) == 0x12

    def test_code_string_known(self):
        """Test str(Code) for known codec."""
        code = Code(0x12)
        assert str(code) == "sha2-256"

    def test_code_string_unknown(self):
        """Test str(Code) for unknown codec."""
        code = Code(0xDEADBEEF)
        assert "0xdeadbeef" in str(code).lower()

    def test_code_repr(self):
        """Test repr(Code)."""
        code = Code(0x12)
        assert "sha2-256" in repr(code)
        assert "0x12" in repr(code)

    def test_code_equality(self):
        """Test Code equality."""
        code1 = Code(0x12)
        code2 = Code(0x12)
        code3 = Code(0x13)
        assert code1 == code2
        assert code1 != code3
        assert code1 == 0x12
        assert code1 != 0x13

    def test_code_comparison(self):
        """Test Code comparison operators."""
        code1 = Code(0x12)
        code2 = Code(0x13)
        assert code1 < code2
        assert code1 <= code2
        assert code2 > code1
        assert code2 >= code1
        assert code1 < 0x13
        assert code1 <= 0x12

    def test_code_hash(self):
        """Test Code is hashable."""
        code = Code(0x12)
        code_set = {code}
        assert Code(0x12) in code_set

    def test_code_name_property(self):
        """Test Code.name property."""
        code = Code(0x12)
        assert code.name == "sha2-256"

        unknown = Code(0xDEADBEEF)
        assert unknown.name == "<unknown>"

    def test_code_tag(self):
        """Test Code.tag() method."""
        # Multihash
        code = Code(0x12)  # sha2-256
        assert code.tag() == "multihash"

        # Multiaddr
        code = Code(0x04)  # ip4
        assert code.tag() == "multiaddr"

        # CID
        code = Code(0x01)  # cidv1
        assert code.tag() == "cid"

        # IPLD
        code = Code(0x55)  # raw
        assert code.tag() == "ipld"


class ReservedRangeTestCase:
    """Tests for reserved range constants and functions."""

    def test_reserved_constants(self):
        """Test RESERVED_START and RESERVED_END constants."""
        assert RESERVED_START == 0x300000
        assert RESERVED_END == 0x3FFFFF

    def test_is_reserved_in_range(self):
        """Test is_reserved returns True for codes in range."""
        assert is_reserved(RESERVED_START)
        assert is_reserved(RESERVED_END)
        assert is_reserved(0x300001)
        assert is_reserved(0x350000)

    def test_is_reserved_out_of_range(self):
        """Test is_reserved returns False for codes outside range."""
        assert not is_reserved(0x12)
        assert not is_reserved(0x00)
        assert not is_reserved(RESERVED_START - 1)
        assert not is_reserved(RESERVED_END + 1)

    def test_is_reserved_with_code_object(self):
        """Test is_reserved with Code object."""
        assert is_reserved(Code(RESERVED_START))
        assert not is_reserved(Code(0x12))


class KnownCodesTestCase:
    """Tests for known_codes function."""

    def test_known_codes_returns_list(self):
        """Test known_codes returns a list."""
        codes = known_codes()
        assert isinstance(codes, list)
        assert len(codes) > 0

    def test_known_codes_contains_code_objects(self):
        """Test known_codes contains Code objects."""
        codes = known_codes()
        assert all(isinstance(c, Code) for c in codes)

    def test_known_codes_contains_common_codecs(self):
        """Test known_codes contains common codecs."""
        codes = known_codes()
        code_values = [int(c) for c in codes]
        assert 0x12 in code_values  # sha2-256
        assert 0x00 in code_values  # identity
        assert 0x55 in code_values  # raw

    def test_known_codes_is_sorted(self):
        """Test known_codes returns sorted list."""
        codes = known_codes()
        code_values = [int(c) for c in codes]
        assert code_values == sorted(code_values)

    def test_known_codes_same_instance(self):
        """Test known_codes returns cached list."""
        codes1 = known_codes()
        codes2 = known_codes()
        assert codes1 is codes2


class CodeTableConstantsTestCase:
    """Tests for code_table named constants."""

    def test_named_constants_exist(self):
        """Test that named constants are importable."""
        from multicodec.code_table import (
            IDENTITY,
            SHA2_256,
        )

        assert SHA2_256 is not None
        assert IDENTITY is not None

    def test_named_constants_are_code_objects(self):
        """Test that named constants are Code instances."""
        from multicodec.code_table import DAG_CBOR, IDENTITY, SHA2_256

        assert isinstance(SHA2_256, Code)
        assert isinstance(IDENTITY, Code)
        assert isinstance(DAG_CBOR, Code)

    def test_named_constants_values(self):
        """Test that named constants have correct values."""
        from multicodec.code_table import (
            DAG_CBOR,
            DAG_PB,
            DNS,
            IDENTITY,
            IP4,
            RAW,
            SHA2_256,
            TCP,
        )

        assert int(IDENTITY) == 0x00
        assert int(SHA2_256) == 0x12
        assert int(IP4) == 0x04
        assert int(TCP) == 0x06
        assert int(DNS) == 0x35
        assert int(RAW) == 0x55
        assert int(DAG_PB) == 0x70
        assert int(DAG_CBOR) == 0x71

    def test_named_constants_string_representation(self):
        """Test that named constants have correct string names."""
        from multicodec.code_table import DAG_CBOR, IDENTITY, SHA2_256

        assert str(IDENTITY) == "identity"
        assert str(SHA2_256) == "sha2-256"
        assert str(DAG_CBOR) == "dag-cbor"

    def test_named_constants_can_be_used_in_comparisons(self):
        """Test that named constants work in comparisons."""
        from multicodec.code_table import SHA2_256

        code = Code(0x12)
        assert code == SHA2_256
        assert SHA2_256 == code
        assert SHA2_256 == 0x12

    def test_named_constants_can_be_used_in_sets(self):
        """Test that named constants can be used in sets."""
        from multicodec.code_table import DAG_CBOR, SHA2_256

        code_set = {SHA2_256, DAG_CBOR}
        assert Code(0x12) in code_set
        assert Code(0x71) in code_set
        assert Code(0x99) not in code_set

    def test_blake_variants_exist(self):
        """Test that BLAKE2 variants are defined."""
        from multicodec.code_table import BLAKE2B_256, BLAKE2S_256, BLAKE3

        assert int(BLAKE3) == 0x1E
        assert int(BLAKE2B_256) == 0xB220
        assert int(BLAKE2S_256) == 0xB260

    def test_multiaddr_constants(self):
        """Test multiaddr constants."""
        from multicodec.code_table import (
            DNS,
            DNS4,
            DNS6,
            DNSADDR,
            HTTP,
            HTTPS,
            IP4,
            IP6,
            QUIC,
            TCP,
            UDP,
            WS,
            WSS,
        )

        assert int(IP4) == 0x04
        assert int(IP6) == 0x29
        assert int(TCP) == 0x06
        assert int(UDP) == 0x0111
        assert int(DNS) == 0x35
        assert int(DNS4) == 0x36
        assert int(DNS6) == 0x37
        assert int(DNSADDR) == 0x38
        assert int(QUIC) == 0x01CC
        assert int(WS) == 0x01DD
        assert int(WSS) == 0x01DE
        assert int(HTTP) == 0x01E0
        assert int(HTTPS) == 0x01BB

    def test_key_constants(self):
        """Test key constants."""
        from multicodec.code_table import (
            ED25519_PRIV,
            ED25519_PUB,
            SECP256K1_PUB,
            X25519_PUB,
        )

        assert int(SECP256K1_PUB) == 0xE7
        assert int(X25519_PUB) == 0xEC
        assert int(ED25519_PUB) == 0xED
        assert int(ED25519_PRIV) == 0x1300
