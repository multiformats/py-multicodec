import csv
import os

from multicodec.constants import CODE_TABLE, CODECS, NAME_TABLE


def load_csv(path):
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {k.strip(): v.strip() for k, v in row.items()}


def test_spec_table_completeness():
    """Every entry in table.csv should be in CODECS, and no extra entries should exist."""
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "multicodec-spec", "table.csv")

    csv_names = set()
    for row in load_csv(csv_path):
        name = row["name"]
        tag = row["tag"]
        code_str = row["code"]

        if tag == "none":
            continue

        csv_names.add(name)
        code_int = int(code_str, 16)

        assert name in NAME_TABLE, f"Missing codec from spec: {name} ({code_str})"
        assert NAME_TABLE[name] == code_int, f"Code mismatch for {name}: expected {code_int}, got {NAME_TABLE[name]}"
        assert code_int in CODE_TABLE, f"Missing code from CODE_TABLE: {code_int} ({name})"
        assert CODE_TABLE[code_int] == name, (
            f"Name mismatch for {code_int}: expected {name}, got {CODE_TABLE[code_int]}"
        )
        assert name in CODECS, f"Missing codec from CODECS: {name}"
        assert CODECS[name]["prefix"] == code_int, (
            f"Prefix mismatch for {name} in CODECS: expected {code_int}, got {CODECS[name]['prefix']}"
        )

    # Verify no extra entries exist in CODECS that aren't in the CSV
    for name in CODECS:
        assert name in csv_names, f"Extra codec in CODECS not in spec: {name}"
