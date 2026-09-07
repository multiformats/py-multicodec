"""Top-level package for py-multicodec."""

__author__ = """Dhruv Baldawa"""
__email__ = "dhruv@dhruvb.com"
__version__ = "1.0.0"

# Core Code type
from .code import (
    RESERVED_END,
    RESERVED_START,
    Code,
    is_reserved,
    known_codes,
)

# Curated named codec constants (full set: multicodec.code_table)
from .code_table import (
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
)

# Exceptions
from .exceptions import (
    CodecError,
    DecodeError,
    EncodeError,
    MulticodecError,
    UnknownCodecError,
)

# Original multicodec functions
from .multicodec import add_prefix, extract_prefix, get_codec, get_prefix, is_codec, remove_prefix

# Serialization support
from .serialization import (
    Codec,
    JSONCodec,
    RawCodec,
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

__all__ = [
    # Named codec constants (curated)
    "CIDV1",
    "DAG_CBOR",
    "DAG_JSON",
    "DAG_PB",
    "ED25519_PUB",
    "IDENTITY",
    "IP4",
    "IP6",
    "LIBP2P_PEER_RECORD",
    "RAW",
    # Constants
    "RESERVED_END",
    "RESERVED_START",
    "SECP256K1_PUB",
    "SHA1",
    "SHA2_256",
    "SHA2_512",
    "SHA3_256",
    "SHA3_512",
    "TCP",
    "UDP",
    # Code type
    "Code",
    # Serialization base classes
    "Codec",
    "CodecError",
    "DecodeError",
    "EncodeError",
    # Built-in codecs
    "JSONCodec",
    # Exceptions
    "MulticodecError",
    "RawCodec",
    "UnknownCodecError",
    # Original functions
    "add_prefix",
    "decode",
    # Serialization functions
    "encode",
    "extract_prefix",
    "get_codec",
    "get_prefix",
    "get_registered_codec",
    "is_codec",
    "is_codec_registered",
    "is_reserved",
    "json_codec",
    "known_codes",
    "list_registered_codecs",
    "raw_codec",
    "register_codec",
    "remove_prefix",
    "unregister_codec",
]
