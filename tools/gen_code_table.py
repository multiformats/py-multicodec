"""
Generate code_table.py with named Code constants.

This script generates code_table.py.
Run this script to regenerate code_table.py from constants.py.

Usage:
    python tools/gen_code_table.py
"""

from __future__ import annotations

import ast
from collections import defaultdict
from pathlib import Path
from typing import Any


def load_codecs_from_file() -> dict[str, dict[str, Any]]:
    """Load CODECS dict from constants.py without importing."""
    constants_path = Path(__file__).parent.parent / "multicodec" / "constants.py"
    content = constants_path.read_text()

    # Find and extract the CODECS dictionary (Assign or AnnAssign)
    tree = ast.parse(content)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "CODECS":
                    codecs_source = ast.get_source_segment(content, node.value)
                    return eval(codecs_source)
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.target.id == "CODECS" and node.value is not None:
                codecs_source = ast.get_source_segment(content, node.value)
                return eval(codecs_source)
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


def categorize(name: str, info: dict[str, Any]) -> str:
    """Return the category key for a codec using CSV tag metadata.

    Tags of ``none`` or missing/empty tags are grouped under ``other``.
    """
    tag = info.get("tag") or "other"
    if tag in ("", "none"):
        return "other"
    return str(tag)


def generate_code_table(CODECS: dict[str, dict[str, Any]]) -> str:
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

    categories: dict[str, list[tuple[str, int, str]]] = defaultdict(list)

    for name, info in sorted(CODECS.items(), key=lambda x: int(x[1]["prefix"])):
        const_name = name_to_const(name)
        prefix = int(info["prefix"])
        category = categorize(name, info)
        categories[category].append((const_name, prefix, name))

    # Stable output order: known common tags first, then remaining sorted
    preferred = [
        "multihash",
        "multiaddr",
        "ipld",
        "serialization",
        "multiformat",
        "key",
        "namespace",
        "cid",
        "other",
    ]
    ordered_cats = [c for c in preferred if c in categories]
    ordered_cats.extend(sorted(c for c in categories if c not in preferred))

    all_names: list[str] = []

    for category in ordered_cats:
        items = categories[category]
        if not items:
            continue
        lines.append(f"# {category}")
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


def main() -> None:
    CODECS = load_codecs_from_file()
    output_path = Path(__file__).parent.parent / "multicodec" / "code_table.py"
    content = generate_code_table(CODECS)
    output_path.write_text(content + "\n")
    print(f"Generated {output_path}")
    print(f"Total constants: {len(CODECS)}")


if __name__ == "__main__":
    main()
