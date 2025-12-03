py-multicodec
-------------

.. image:: https://img.shields.io/pypi/v/py-multicodec.svg
        :target: https://pypi.python.org/pypi/py-multicodec

.. image:: https://github.com/multiformats/py-multicodec/actions/workflows/tox.yml/badge.svg?branch=master
        :target: https://github.com/multiformats/py-multicodec/actions/workflows/tox.yml

.. image:: https://codecov.io/gh/multiformats/py-multicodec/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/multiformats/py-multicodec

.. image:: https://readthedocs.org/projects/py-multicodec/badge/?version=stable
        :target: https://py-multicodec.readthedocs.io/en/stable/?badge=stable
        :alt: Documentation Status


`Multicodec <https://github.com/multiformats/multicodec>`_ implementation in Python

``multicodec`` *is a self-describing multiformat*, it wraps other formats with a tiny bit of self-description.

A multicodec identifier is both a varint and the code identifying the following data, this means that the most
significant bit of every multicodec code is reserved to signal the continuation.

You can check `the table here <https://github.com/multiformats/multicodec/blob/909e183da65818ecd1e672904980e53711da8780/table.csv>`_ for the list of supported codecs by ``py-multicodec``.

* Free software: MIT license
* Documentation: https://py-multicodec.readthedocs.io.
* Python versions: 3.10, 3.11, 3.12, 3.13, 3.14


Installation
============

.. code-block:: shell

    $ pip install py-multicodec


Sample Usage
============

.. code-block:: python

    >>> from multicodec import add_prefix, remove_prefix, get_codec
    >>> # adding a prefix to existing data
    >>> add_prefix('sha2-256', b'EiC5TSe5k00')
    b'\x12EiC5TSe5k00'
    >>> # removing prefix from prefixed data
    >>> remove_prefix(b'\x12EiC5TSe5k00')
    EiC5TSe5k00
    >>> # get codec used to prefix the prefixed data
    >>> get_codec(b'\x12EiC5TSe5k00')
    'sha2-256'

Code Management
===============

In addition to the basic prefix operations, py-multicodec provides type-safe codec
management functionality:

.. code-block:: python

    >>> from multicodec import Code, known_codes
    >>> from multicodec.code_table import SHA2_256, DAG_CBOR

    >>> # Use named constants for type-safe codec handling
    >>> code = SHA2_256
    >>> str(code)
    'sha2-256'
    >>> int(code)
    18

    >>> # Create Code from string (name or hex)
    >>> code = Code.from_string("sha2-256")
    >>> code = Code.from_string("0x12")  # hex also works

    >>> # List all known codecs
    >>> all_codes = known_codes()
    >>> len(all_codes)
    460

Updating the lookup table
==========================

Updating the lookup table is done with a script. The source of truth is the
`multicodec default table <https://github.com/multiformats/multicodec/blob/master/table.csv>`_.
Update the table with running:

.. code-block:: shell

    $ curl -X GET https://raw.githubusercontent.com/multiformats/multicodec/master/table.csv | ./tools/update-table.py
