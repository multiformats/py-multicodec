"""Tests for curated top-level named codec constant exports."""

import multicodec
from multicodec import (
    CIDV1,
    DAG_CBOR,
    DAG_JSON,
    DAG_PB,
    ED25519_PUB,
    IDENTITY,
    IP4,
    IP6,
    LIBP2P_PEER_RECORD,
    RAW,
    SECP256K1_PUB,
    SHA1,
    SHA2_256,
    SHA2_512,
    SHA3_256,
    SHA3_512,
    TCP,
    UDP,
    Code,
)

CURATED_CONSTANTS = [
    (IDENTITY, 0x00, "identity"),
    (SHA1, 0x11, "sha1"),
    (SHA2_256, 0x12, "sha2-256"),
    (SHA2_512, 0x13, "sha2-512"),
    (SHA3_256, 0x16, "sha3-256"),
    (SHA3_512, 0x14, "sha3-512"),
    (DAG_PB, 0x70, "dag-pb"),
    (DAG_CBOR, 0x71, "dag-cbor"),
    (DAG_JSON, 0x129, "dag-json"),
    (RAW, 0x55, "raw"),
    (CIDV1, 0x01, "cidv1"),
    (IP4, 0x04, "ip4"),
    (IP6, 0x29, "ip6"),
    (TCP, 0x06, "tcp"),
    (UDP, 0x111, "udp"),
    (ED25519_PUB, 0xED, "ed25519-pub"),
    (SECP256K1_PUB, 0xE7, "secp256k1-pub"),
    (LIBP2P_PEER_RECORD, 0x301, "libp2p-peer-record"),
]


def test_curated_constants_are_code_instances():
    for const, prefix, name in CURATED_CONSTANTS:
        assert isinstance(const, Code)
        assert int(const) == prefix
        assert const.name == name


def test_curated_constants_in_all():
    for const, _prefix, _name in CURATED_CONSTANTS:
        names = [n for n in multicodec.__all__ if getattr(multicodec, n, None) is const]
        assert len(names) == 1, f"Expected one __all__ entry for {const}"
