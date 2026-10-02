"""Optional performance benchmarks for core multicodec operations.

Run with:
    pytest tests/test_benchmarks.py --benchmark-only
"""

import pytest

from multicodec import Code, add_prefix, extract_prefix, get_codec, known_codes

BENCH_DATA = b"\x12" + b"\xab" * 32  # sha2-256 prefixed data


@pytest.mark.benchmark
def test_bench_code_construction(benchmark):
    benchmark(Code, 0x12)


@pytest.mark.benchmark
def test_bench_code_from_string(benchmark):
    benchmark(Code.from_string, "sha2-256")


@pytest.mark.benchmark
def test_bench_code_tag(benchmark):
    code = Code(0x12)
    benchmark(code.tag)


@pytest.mark.benchmark
def test_bench_add_prefix(benchmark):
    benchmark(add_prefix, "sha2-256", b"\xab" * 32)


@pytest.mark.benchmark
def test_bench_get_codec(benchmark):
    benchmark(get_codec, BENCH_DATA)


@pytest.mark.benchmark
def test_bench_extract_prefix(benchmark):
    benchmark(extract_prefix, BENCH_DATA)


@pytest.mark.benchmark
def test_bench_known_codes(benchmark):
    benchmark(known_codes)
