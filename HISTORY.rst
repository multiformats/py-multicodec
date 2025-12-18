History
=======

.. towncrier release notes start

py-multicodec v1.0.0 (2025-12-18)
---------------------------------

Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Fixed Read the Docs build failures by updating deprecated Sphinx settings and adding API documentation generation. (`#29 <https://github.com/multiformats/py-multicodec/issues/29>`__)


Features
~~~~~~~~

- Added Codec constants, List all codecs function and Reserved range support for Codec management. (`#23 <https://github.com/multiformats/py-multicodec/issues/23>`__)
- Added serialization with JSON/raw codecs, custom codec interface, encode/decode functions, and a dynamic codec registry. (`#25 <https://github.com/multiformats/py-multicodec/issues/25>`__)
- Updated codec table from official multicodec repository to include all 603 codecs (up from 460). This adds many previously missing codecs including hash functions (sha2-384, sha2-224, murmur3-x64 variants), encryption algorithms (aes-128/192/256, chacha variants), network protocols (noise, quic-v1, webrtc), and many others. Addresses gap analysis from discussion #1063. (`#31 <https://github.com/multiformats/py-multicodec/issues/31>`__)


Internal Changes - for py-multicodec Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Modernized repository infrastructure to use pyproject.toml, GitHub Actions CI/CD, Python 3.10+ support, ruff for linting/formatting, and pre-commit hooks. (`#21 <https://github.com/multiformats/py-multicodec/issues/21>`__)
- Dropped ``coverage`` and ``codecov`` references, no longer using it. (`#29 <https://github.com/multiformats/py-multicodec/issues/29>`__)
- Updated contributing docs and docs config with current release process. (`#35 <https://github.com/multiformats/py-multicodec/issues/35>`__)


0.1.3 (2018-10-20)
------------------

* Handle exception when the varint is invalid

0.1.0 (2017-09-03)
------------------

* First release on PyPI.
