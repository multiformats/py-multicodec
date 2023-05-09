**This project is no longer maintained and has been archived.**


py-multicodec
-------------

.. image:: https://img.shields.io/pypi/v/py-multicodec.svg
        :target: https://pypi.python.org/pypi/py-multicodec

.. image:: https://img.shields.io/travis/multiformats/py-multicodec.svg?branch=master
        :target: https://travis-ci.org/multiformats/py-multicodec?branch=master

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
* Python versions: 3.5, 3.6


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

Updating the lookup table
==========================

Updating the lookup table is done with a script. The source of truth is the
`multicodec default table <https://github.com/multiformats/multicodec/blob/master/table.csv>`_.
Update the table with running:

.. code-block:: shell

    $ curl -X GET https://raw.githubusercontent.com/multiformats/multicodec/master/table.csv | ./tools/update-table.py
