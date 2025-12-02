"""
Generate code_table.py with named Code constants.

This script generates code_table.py.
Run this script to regenerate code_table.py from constants.py.

Usage:
    python tools/gen_code_table.py
"""

import ast
from pathlib import Path


def load_codecs_from_file():
    """Load CODECS dict from constants.py without importing."""
    constants_path = Path(__file__).parent.parent / "multicodec" / "constants.py"
    content = constants_path.read_text()

    # Find and extract the CODECS dictionary
    tree = ast.parse(content)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "CODECS":
                    # Safely evaluate the dictionary
                    codecs_source = ast.get_source_segment(content, node.value)
                    return ast.literal_eval(codecs_source)
    raise ValueError("CODECS not found in constants.py")


def name_to_const(name: str) -> str:
    """Convert codec name to Python constant name.

    Examples:
        sha2-256 -> SHA2_256
        dag-cbor -> DAG_CBOR
        bls12_381-g1-pub -> BLS12_381_G1_PUB
    """
    # Replace hyphens and dots with underscores, then uppercase
    const = name.upper().replace("-", "_").replace(".", "_")
    # Ensure it starts with a letter or underscore (valid Python identifier)
    if const[0].isdigit():
        const = "_" + const
    return const


def generate_code_table(CODECS: dict) -> str:
    """Generate the code_table.py content."""
    lines = [
        "# Code generated from constants.py; DO NOT EDIT MANUALLY.",
        "#",
        "# To regenerate, run: python tools/gen_code_table.py",
        "#",
        "# These constants provide type-safe Code values for all known multicodecs,",
        "# allowing usage like:",
        "#     from multicodec import SHA2_256",
        "#     code = SHA2_256  # Code object for sha2-256",
        "#",
        "# Instead of:",
        "#     from multicodec import Code",
        "#     code = Code(0x12)",
        "",
        "from __future__ import annotations",
        "",
        "from .code import Code",
        "",
    ]

    # Group codecs by category based on their names
    categories = {
        "multihash": [],
        "multiaddr": [],
        "ipld": [],
        "serialization": [],
        "multiformat": [],
        "key": [],
        "namespace": [],
        "other": [],
    }

    # Pattern lists for categorization
    multihash_patterns = [
        "sha",
        "keccak",
        "blake",
        "md4",
        "md5",
        "ripemd",
        "murmur",
        "identity",
        "x11",
        "kangaroo",
        "sm3",
        "skein",
        "poseidon",
        "bmt",
        "dbl-sha",
    ]
    multiaddr_patterns = [
        "ip4",
        "ip6",
        "tcp",
        "udp",
        "dns",
        "sctp",
        "dccp",
        "quic",
        "ws",
        "http",
        "p2p",
        "onion",
        "garlic",
        "tls",
        "unix",
        "thread",
        "udt",
        "utp",
        "sni",
        "noise",
        "shs",
        "certhash",
        "webrtc",
        "memory",
        "scion",
        "plaintextv2",
    ]
    ipld_patterns = [
        "cid",
        "raw",
        "dag-",
        "libp2p-key",
        "git-raw",
        "torrent",
        "leofcoin",
        "eth-",
        "bitcoin",
        "zcash",
        "stellar",
        "decred",
        "dash",
        "swarm-manifest",
        "swarm-feed",
        "beeson",
        "swhid",
    ]
    serialization_patterns = [
        "protobuf",
        "cbor",
        "rlp",
        "bencode",
        "json",
        "messagepack",
        "car",
        "ipns-record",
        "x509",
        "ssz",
    ]
    key_patterns = [
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
    ]
    namespace_patterns = [
        "path",
        "ns",
        "lbry",
        "streamid",
        "zeronet",
        "dnslink",
        "skynet",
        "arweave",
        "subspace",
        "kumandra",
        "docid",
    ]

    for name, info in sorted(CODECS.items(), key=lambda x: x[1]["prefix"]):
        const_name = name_to_const(name)
        prefix = info["prefix"]

        # Categorize based on name patterns
        if any(h in name for h in multihash_patterns):
            categories["multihash"].append((const_name, prefix, name))
        elif any(a in name for a in multiaddr_patterns):
            categories["multiaddr"].append((const_name, prefix, name))
        elif any(c in name for c in ipld_patterns):
            categories["ipld"].append((const_name, prefix, name))
        elif any(s in name for s in serialization_patterns):
            categories["serialization"].append((const_name, prefix, name))
        elif name in ["multicodec", "multihash", "multiaddr", "multibase", "varsig"]:
            categories["multiformat"].append((const_name, prefix, name))
        elif any(k in name for k in key_patterns):
            categories["key"].append((const_name, prefix, name))
        elif any(n in name for n in namespace_patterns):
            categories["namespace"].append((const_name, prefix, name))
        else:
            categories["other"].append((const_name, prefix, name))

    # Generate constants for each category
    all_names = []

    for category, items in categories.items():
        if not items:
            continue
        lines.append(f"# {category.title()}")
        for const_name, prefix, name in items:
            lines.append(f"{const_name}: Code = Code(0x{prefix:02x})  # {name}")
            all_names.append(const_name)
        lines.append("")

    # Generate __all__
    lines.append("__all__ = [")
    for name in sorted(all_names):
        lines.append(f'    "{name}",')
    lines.append("]")

    return "\n".join(lines)


def main():
    CODECS = load_codecs_from_file()
    output_path = Path(__file__).parent.parent / "multicodec" / "code_table.py"
    content = generate_code_table(CODECS)
    output_path.write_text(content)
    print(f"Generated {output_path}")
    print(f"Total constants: {len(CODECS)}")


if __name__ == "__main__":
    main()
