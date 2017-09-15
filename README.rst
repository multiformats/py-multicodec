py-multicodec
-------------

.. image:: https://img.shields.io/pypi/v/py-multicodec.svg
        :target: https://pypi.python.org/pypi/py-multicodec

.. image:: https://img.shields.io/travis/multiformats/py-multicodec.svg
        :target: https://travis-ci.org/multiformats/py-multicodec

.. image:: https://codecov.io/gh/multiformats/py-multicodec/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/multiformats/py-multicodec

.. image:: https://readthedocs.org/projects/py-multicodec/badge/?version=latest
        :target: https://py-multicodec.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/multiformats/py-multicodec/shield.svg
     :target: https://pyup.io/repos/github/multiformats/py-multicodec/
     :alt: Updates


`Multicodec <https://github.com/multiformats/multicodec>`_ implementation in Python

``multicodec`` *is a self-describing multiformat*, it wraps other formats with a tiny bit of self-description.

A multicodec identifier is both a varint and the code identifying the following data, this means that the most
significant bit of every multicodec code is reserved to signal the continuation.

You can check `the table here <https://github.com/multiformats/multicodec/blob/7c57cd4477e391d27b8d7cc0995da9e674434ffb/table.csv>`_ for the list of supported codecs by ``py-multicodec``.

* Free software: MIT license
* Documentation: https://py-multicodec.readthedocs.io.


Installation
============

.. code-block:: shell

    $ pip install py-multicodec


Sample Usage
============

.. code-block:: python

    >>> from multicodec import add_prefix, remove_prefix, get_codec
    >>> # adding a prefix to existing data
    >>> add_prefix('sha2-256', 'EiC5TSe5k00')
    b'\x12EiC5TSe5k00'
    >>> # removing prefix from prefixed data
    >>> remove_prefix(b'\x12EiC5TSe5k00')
    EiC5TSe5k00
    >>> # get codec used to prefix the prefixed data
    >>> get_codec(b'\x12EiC5TSe5k00')
    'sha2-256'
