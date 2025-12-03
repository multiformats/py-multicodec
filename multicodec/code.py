"""
Multicodec Code type and core functionality.

This module provides:
- Code class for type-safe codec handling
- ReservedStart and ReservedEnd constants
- KnownCodes() function to list all registered codes
"""

from __future__ import annotations

from .constants import CODE_TABLE, NAME_TABLE

# ReservedStart is the (inclusive) start of the reserved range of codes that
# are safe to use for internal purposes.
RESERVED_START: int = 0x300000

# ReservedEnd is the (inclusive) end of the reserved range of codes that are
# safe to use for internal purposes.
RESERVED_END: int = 0x3FFFFF


class Code:
    """
    Code describes an integer reserved in the multicodec table.

    This class provides:
    - Type-safe codec handling
    - String conversion (name lookup)
    - Set from string (name or hex number)
    - Tag lookup

    Example:
        >>> code = Code(0x12)
        >>> str(code)
        'sha2-256'
        >>> code = Code.from_string("sha2-256")
        >>> int(code)
        18
    """

    __slots__ = ("_value",)

    def __init__(self, value: int) -> None:
        """Initialize a Code with an integer value."""
        if not isinstance(value, int):
            raise TypeError(f"Code value must be an integer, got {type(value).__name__}")
        if value < 0:
            raise ValueError("Code value must be non-negative")
        self._value = value

    @classmethod
    def from_string(cls, text: str) -> Code:
        """
        Create a Code from a string, interpreting it as a multicodec name or number.

        The input string can be the name or number for a known code. A number can be
        in decimal or hexadecimal format (with 0x prefix).

        Numbers in the reserved range 0x300000-0x3FFFFF are also accepted.

        :param str text: The codec name or number
        :return: A Code instance
        :rtype: Code
        :raises ValueError: If the text is not a valid codec
        """
        # Try parsing as a number first (cheap operation)
        try:
            n = int(text, 0)  # base 0 allows decimal, hex (0x), octal (0o), binary (0b)
            code = cls(n)
            # Accept if in reserved range
            if RESERVED_START <= n <= RESERVED_END:
                return code
            # Accept if known code
            if n in CODE_TABLE:
                return code
        except ValueError:
            pass

        # Try matching by name
        if text in NAME_TABLE:
            return cls(NAME_TABLE[text])

        raise ValueError(f'unknown multicodec: "{text}"')

    def set(self, text: str) -> None:
        """
        Set the code from a string.

        :param str text: The codec name or number
        :raises ValueError: If the text is not a valid codec
        """
        new_code = Code.from_string(text)
        self._value = new_code._value

    def __int__(self) -> int:
        """Return the integer value of the code."""
        return self._value

    def __index__(self) -> int:
        """Support using Code in contexts that require an integer index."""
        return self._value

    def __str__(self) -> str:
        """
        Return the string name of the code.

        Returns the codec name if known, otherwise returns the hex representation.
        """
        if self._value in CODE_TABLE:
            return CODE_TABLE[self._value]
        return f"Code(0x{self._value:x})"

    def __repr__(self) -> str:
        """Return a detailed representation of the code."""
        if self._value in CODE_TABLE:
            return f"Code({CODE_TABLE[self._value]!r}, 0x{self._value:x})"
        return f"Code(0x{self._value:x})"

    def __eq__(self, other: object) -> bool:
        """Check equality with another Code or integer."""
        if isinstance(other, Code):
            return self._value == other._value
        if isinstance(other, int):
            return self._value == other
        return NotImplemented

    def __hash__(self) -> int:
        """Return hash of the code value."""
        return hash(self._value)

    def __lt__(self, other: Code | int) -> bool:
        """Compare less than."""
        if isinstance(other, Code):
            return self._value < other._value
        if isinstance(other, int):
            return self._value < other
        return NotImplemented

    def __le__(self, other: Code | int) -> bool:
        """Compare less than or equal."""
        if isinstance(other, Code):
            return self._value <= other._value
        if isinstance(other, int):
            return self._value <= other
        return NotImplemented

    def __gt__(self, other: Code | int) -> bool:
        """Compare greater than."""
        if isinstance(other, Code):
            return self._value > other._value
        if isinstance(other, int):
            return self._value > other
        return NotImplemented

    def __ge__(self, other: Code | int) -> bool:
        """Compare greater than or equal."""
        if isinstance(other, Code):
            return self._value >= other._value
        if isinstance(other, int):
            return self._value >= other
        return NotImplemented

    @property
    def name(self) -> str:
        """Return the codec name, or '<unknown>' if not found."""
        return CODE_TABLE.get(self._value, "<unknown>")

    def tag(self) -> str:
        """
        Return the tag for this codec.

        Tags categorize codecs (e.g., "multihash", "multiaddr", "ipld", etc.)
        """
        return _get_tag(self._value)


def _get_tag(code: int) -> str:
    """Get the tag for a codec code (mirrors go-multicodec's Tag() method)."""
    name = CODE_TABLE.get(code, "")

    # CID
    if name in ("cidv1", "cidv2", "cidv3"):
        return "cid"

    # Encryption
    if name in ("aes-gcm-256",):
        return "encryption"

    # Filecoin
    if name in ("fil-commitment-unsealed", "fil-commitment-sealed"):
        return "filecoin"

    # Hash (non-multihash)
    if name in (
        "murmur3-x64-64",
        "murmur3-32",
        "murmur3-128",
        "crc32",
        "crc64-ecma",
        "crc64-nvme",
        "murmur3-x64-128",
        "sha256a",
        "xxh-32",
        "xxh-64",
        "xxh3-64",
        "xxh3-128",
    ):
        return "hash"

    # Holochain
    if "holochain" in name:
        return "holochain"

    # IPLD
    if name in (
        "cbor",
        "raw",
        "dag-pb",
        "dag-cbor",
        "libp2p-key",
        "git-raw",
        "torrent-info",
        "torrent-file",
        "blake3-hashseq",
        "leofcoin-block",
        "leofcoin-tx",
        "leofcoin-pr",
        "dag-jose",
        "dag-cose",
        "eth-block",
        "eth-block-list",
        "eth-tx-trie",
        "eth-tx",
        "eth-tx-receipt-trie",
        "eth-tx-receipt",
        "eth-state-trie",
        "eth-account-snapshot",
        "eth-storage-trie",
        "eth-receipt-log-trie",
        "eth-receipt-log",
        "bitcoin-block",
        "bitcoin-tx",
        "bitcoin-witness-commitment",
        "zcash-block",
        "zcash-tx",
        "stellar-block",
        "stellar-tx",
        "decred-block",
        "decred-tx",
        "dash-block",
        "dash-tx",
        "swarm-manifest",
        "swarm-feed",
        "beeson",
        "dag-json",
        "swhid-1-snp",
        "json",
        "rdfc-1",
        "json-jcs",
    ):
        return "ipld"

    # Key
    if any(
        k in name
        for k in (
            "-pub",
            "-priv",
            "secp256k1",
            "bls12_381",
            "x25519",
            "ed25519",
            "p256",
            "p384",
            "p521",
            "ed448",
            "x448",
            "sr25519",
            "rsa",
            "sm2",
            "mlkem",
            "jwk",
        )
    ):
        return "key"

    # Libp2p
    if name in ("libp2p-peer-record", "libp2p-relay-rsvp"):
        return "libp2p"

    # Multiaddr
    if name in (
        "ip4",
        "tcp",
        "dccp",
        "ip6",
        "ip6zone",
        "ipcidr",
        "dns",
        "dns4",
        "dns6",
        "dnsaddr",
        "sctp",
        "udp",
        "p2p-webrtc-star",
        "p2p-webrtc-direct",
        "p2p-stardust",
        "p2p-circuit",
        "udt",
        "utp",
        "unix",
        "thread",
        "p2p",
        "https",
        "onion",
        "onion3",
        "garlic64",
        "garlic32",
        "tls",
        "sni",
        "noise",
        "shs",
        "quic",
        "quic-v1",
        "webtransport",
        "certhash",
        "ws",
        "wss",
        "p2p-websocket-star",
        "http",
        "http-path",
        "webrtc-direct",
        "webrtc",
        "plaintextv2",
        "scion",
        "memory",
    ):
        return "multiaddr"

    # Multiformat
    if name in ("multicodec", "multihash", "multiaddr", "multibase", "varsig"):
        return "multiformat"

    # Multihash
    if any(
        h in name
        for h in (
            "identity",
            "sha1",
            "sha2-",
            "sha3-",
            "shake-",
            "keccak-",
            "blake2b-",
            "blake2s-",
            "blake3",
            "dbl-sha2-",
            "md4",
            "md5",
            "bmt",
            "ripemd-",
            "x11",
            "kangarootwelve",
            "sm3-",
            "poseidon-",
            "skein",
        )
    ):
        return "multihash"

    # Namespace
    if name in (
        "path",
        "lbry",
        "streamid",
        "ipld-ns",
        "ipfs-ns",
        "swarm-ns",
        "ipns-ns",
        "zeronet",
        "dnslink",
        "skynet-ns",
        "arweave-ns",
        "subspace-ns",
        "kumandra-ns",
    ):
        return "namespace"

    # Serialization
    if name in (
        "protobuf",
        "rlp",
        "bencode",
        "messagepack",
        "car",
        "car-index-sorted",
        "car-multihash-index-sorted",
        "ipns-record",
        "x509-certificate",
        "ssz",
    ):
        return "serialization"

    # Transport
    if name in (
        "transport-bitswap",
        "transport-graphsync-filecoinv1",
        "transport-ipfs-gateway-http",
    ):
        return "transport"

    # Varsig
    if name in (
        "nonstandard-sig",
        "es256k",
        "bls12_381-g1-sig",
        "bls12_381-g2-sig",
        "eddsa",
        "eip-191",
        "es256",
        "es384",
        "es512",
        "rs256",
    ):
        return "varsig"

    # Zeroxcert
    if name in ("zeroxcert-imprint-256",):
        return "zeroxcert"

    return "<unknown>"


# Cache for known codes list
_known_codes: list[Code] | None = None


def known_codes() -> list[Code]:
    """
    Return a list of all codes registered in the multicodec table.

    The returned list should be treated as read-only.

    :return: List of all known Code objects
    :rtype: list[Code]
    """
    global _known_codes
    if _known_codes is None:
        _known_codes = [Code(code) for code in sorted(CODE_TABLE.keys())]
    return _known_codes


def is_reserved(code: int | Code) -> bool:
    """
    Check if a code falls within the reserved range.

    The reserved range (0x300000-0x3FFFFF) is designated for internal
    and experimental use.

    :param code: The codec code to check
    :return: True if the code is in the reserved range
    :rtype: bool
    """
    if isinstance(code, Code):
        code = int(code)
    return RESERVED_START <= code <= RESERVED_END
