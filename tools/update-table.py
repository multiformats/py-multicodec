#!/usr/bin/env python3

import csv
import os
import sys
from collections import OrderedDict


# This is relative to where this script resides
# Though you can also define an absolute path
DEFAULT_OUTPUT_DIR = '../multicodec'

# The header of the generated files
HEADER = '''\
# THIS FILE IS GENERATED, DO NO EDIT MANUALLY
# For more information see the README.md

'''

FOOTER = '''\

NAME_TABLE = {name: value['prefix'] for name, value in CODECS.items()}
CODE_TABLE = {value['prefix']: name for name, value in CODECS.items()}
'''


def padded_hex(hexstring):
    """Creates a padded (starting with a 0 if odd) hex string"""
    number = int(row['code'], 16)
    hexbytes = '{:x}'.format(number)
    if len(hexbytes) % 2:
        prefix = '0x0'
    else:
        prefix = '0x'
    return prefix + hexbytes


def unique_code(codecs):
    """Returns a list where every code exists only one.

    The first item in the list is taken
    """
    seen = []
    unique = []
    for codec in codecs:
        if 'code' in codec:
            if codec['code'] in seen:
                continue
            else:
                seen.append(codec['code'])
        unique.append(codec)
    return unique


# Preserve the order from earlier versions. New tags are appended
parsed = OrderedDict([
    ('serialization', []),
    ('multiformat', []),
    ('multihash', []),
    ('multiaddr', []),
    ('ipld', []),
    ('namespace', []),
    ('key', []),
    ('holochain', []),
])

maxlen = 0

multicodec_reader = csv.DictReader(sys.stdin, skipinitialspace=True)
for row in multicodec_reader:
    code = padded_hex(row['code'])
    name_const = row['name'].upper().replace('-', '_')
    name_human = row['name']
    tag = row['tag']
    value = {
        'const': name_const,
        'human': name_human,
        'code': code
    }
    if tag not in parsed:
        parsed[tag] = []

    parsed[tag].append(value)

    if maxlen < len(name_human):
        maxlen = len(name_human)

tools_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(tools_dir, DEFAULT_OUTPUT_DIR)

print_file = os.path.join(output_dir, 'constants.py')
with open(print_file, 'w') as ff:
    ff.write(HEADER)
    ff.write('CODECS = {')
    for tagindex, (tag, codecs) in enumerate(parsed.items()):
        ff.write(f"\n    # {tag}\n")
        unique = unique_code(codecs)
        for codecindex, codec in enumerate(unique):
            name = "'{human}':".format(human=codec['human']).ljust(maxlen + 4)
            value = "{{'prefix': {code}, }},\n".format(code=codec['code'])
            ff.write('    ' + name + value)
    ff.write('}\n')
    ff.write(FOOTER)
