import csv
import os
from collections.abc import Iterator
from pathlib import Path

import pytest

from multicodec.constants import CODE_TABLE, CODECS, NAME_TABLE

SPEC_TABLE_CSV = Path(__file__).resolve().parent.parent / "multicodec-spec" / "table.csv"


def load_csv(path: Path) -> Iterator[dict[str, str]]:
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {k.strip(): v.strip() for k, v in row.items()}


def test_spec_table_completeness() -> None:
    """Every entry in table.csv should be in CODECS, and no extra entries should exist."""
    if not SPEC_TABLE_CSV.is_file():
        message = "multicodec-spec submodule is not initialised; run: git submodule update --init --recursive"
        if os.environ.get("CI"):
            pytest.fail(message)
        pytest.skip(message)

    csv_names: set[str] = set()
    row_mismatches: list[str] = []

    for row in load_csv(SPEC_TABLE_CSV):
        name = row["name"]
        tag = row["tag"]
        status = row.get("status", "")
        description = row.get("description", "")
        code_str = row["code"]
        csv_names.add(name)
        code_int = int(code_str, 16)

        if name not in NAME_TABLE:
            row_mismatches.append(f"Missing codec from spec: {name} ({code_str})")
            continue

        if NAME_TABLE[name] != code_int:
            row_mismatches.append(f"Code mismatch for {name}: expected {code_int}, got {NAME_TABLE[name]}")

        if code_int not in CODE_TABLE:
            row_mismatches.append(f"Missing code from CODE_TABLE: {code_int} ({name})")
        elif CODE_TABLE[code_int] != name:
            row_mismatches.append(f"Name mismatch for {code_int}: expected {name}, got {CODE_TABLE[code_int]}")

        if name not in CODECS:
            row_mismatches.append(f"Missing codec from CODECS: {name}")
            continue

        codec = CODECS[name]
        if codec["prefix"] != code_int:
            row_mismatches.append(f"Prefix mismatch for {name} in CODECS: expected {code_int}, got {codec['prefix']}")
        if codec["tag"] != tag:
            row_mismatches.append(f"Tag mismatch for {name}: expected {tag!r}, got {codec['tag']!r}")
        if codec["status"] != status:
            row_mismatches.append(f"Status mismatch for {name}: expected {status!r}, got {codec['status']!r}")
        if codec["description"] != description:
            row_mismatches.append(
                f"Description mismatch for {name}: expected {description!r}, got {codec['description']!r}"
            )

    # Verify no extra entries exist in CODECS that aren't in the CSV
    extra_codecs = sorted(name for name in CODECS if name not in csv_names)
    if extra_codecs:
        row_mismatches.append("Extra codecs in CODECS not in spec: " + ", ".join(extra_codecs))

    table_mismatches: list[str] = []
    if set(NAME_TABLE) != set(CODECS):
        only_name = sorted(set(NAME_TABLE) - set(CODECS))
        only_codecs = sorted(set(CODECS) - set(NAME_TABLE))
        if only_name:
            table_mismatches.append(f"NAME_TABLE keys not in CODECS: {', '.join(only_name)}")
        if only_codecs:
            table_mismatches.append(f"CODECS keys not in NAME_TABLE: {', '.join(only_codecs)}")

    if set(CODE_TABLE.values()) != set(CODECS):
        code_table_names = set(CODE_TABLE.values())
        only_code_table = sorted(code_table_names - set(CODECS))
        only_codecs_from_table = sorted(set(CODECS) - code_table_names)
        if only_code_table:
            table_mismatches.append(f"CODE_TABLE values not in CODECS: {', '.join(only_code_table)}")
        if only_codecs_from_table:
            table_mismatches.append(f"CODECS names missing from CODE_TABLE values: {', '.join(only_codecs_from_table)}")

    if len(CODE_TABLE) != len(CODECS):
        table_mismatches.append(f"CODE_TABLE length ({len(CODE_TABLE)}) != CODECS length ({len(CODECS)})")

    all_mismatches = row_mismatches + table_mismatches
    if all_mismatches:
        report = "\n".join(all_mismatches)
        pytest.fail(f"Spec table compliance failures ({len(all_mismatches)}):\n{report}")
