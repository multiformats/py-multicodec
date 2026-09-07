#!/usr/bin/env python3

import csv
import os
import sys
from collections import OrderedDict
from textwrap import dedent

# This is relative to where this script resides
# Though you can also define an absolute path
DEFAULT_OUTPUT_DIR = "../multicodec"

# The header of the generated files
HEADER = """\
# THIS FILE IS GENERATED, DO NO EDIT MANUALLY
# For more information see the README.md

from __future__ import annotations

from typing import Any, cast

"""

FOOTER = """\

NAME_TABLE: dict[str, int] = {
    name: cast(int, value["prefix"]) for name, value in CODECS.items()
}
CODE_TABLE: dict[int, str] = {
    cast(int, value["prefix"]): name for name, value in CODECS.items()
}
"""


def padded_hex(hexstring: str) -> str:
    """Creates a padded (starting with a 0 if odd) hex string"""
    number = int(hexstring, 16)
    hexbytes = f"{number:x}"
    if len(hexbytes) % 2:
        prefix = "0x0"
    else:
        prefix = "0x"
    return prefix + hexbytes


def unique_code(codecs):
    """Returns a list where every code exists only one.

    The first item in the list is taken
    """
    seen = []
    unique = []
    for codec in codecs:
        if "code" in codec:
            if codec["code"] in seen:
                continue
            else:
                seen.append(codec["code"])
        unique.append(codec)
    return unique


def escape_py_str(value: str) -> str:
    """Escape a string for embedding in a double-quoted Python literal."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


# Preserve the order from earlier versions. New tags are appended
parsed = OrderedDict(
    [
        ("serialization", []),
        ("multiformat", []),
        ("multihash", []),
        ("multiaddr", []),
        ("ipld", []),
        ("namespace", []),
        ("key", []),
        ("holochain", []),
    ]
)

multicodec_reader = csv.DictReader(sys.stdin, skipinitialspace=True)
for row in multicodec_reader:
    code = padded_hex(row["code"])
    name_const = row["name"].upper().replace("-", "_")
    name_human = row["name"]
    tag = row["tag"]
    status = row.get("status", "") or ""
    description = row.get("description", "") or ""
    value = {
        "const": name_const,
        "human": name_human,
        "code": code,
        "tag": tag,
        "status": status,
        "description": description,
    }
    if tag not in parsed:
        parsed[tag] = []

    parsed[tag].append(value)

tools_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(tools_dir, DEFAULT_OUTPUT_DIR)

print_file = os.path.join(output_dir, "constants.py")
with open(print_file, "w") as ff:
    ff.write(HEADER)
    ff.write("CODECS: dict[str, dict[str, Any]] = {\n")
    for _tagindex, (tag, codecs) in enumerate(parsed.items()):
        ff.write(f"    # {tag}\n")
        unique = unique_code(codecs)
        for codec in unique:
            entry = dedent(
                f"""\
                "{codec["human"]}": {{
                    "prefix": {codec["code"]},
                    "tag": "{escape_py_str(codec.get("tag", ""))}",
                    "status": "{escape_py_str(codec.get("status", ""))}",
                    "description": "{escape_py_str(codec.get("description", ""))}",
                }},
                """
            )
            for line in entry.splitlines():
                ff.write("    " + line + "\n")
    ff.write("}\n")
    ff.write(FOOTER)
