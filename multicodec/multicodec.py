import varint
from six import int2byte

from .constants import NAME_TABLE, CODE_TABLE


class Multicodec(object):
    @classmethod
    def add_prefix(cls, multicodec, bytes_):
        # @TODO: add type checking for bytes
        try:
            prefix = varint.encode(NAME_TABLE[multicodec])
        except KeyError:
            raise ValueError('{} multicodec is not supported.'.format(multicodec))

        return b''.join([prefix, bytes_])

    @classmethod
    def _extract_prefix(cls, bytes_):
        return varint.decode_bytes(bytes_)

    @classmethod
    def remove_prefix(cls, bytes_):
        prefix_int = cls._extract_prefix(bytes_)
        prefix = varint.encode(prefix_int)
        return bytes_[len(prefix):]

    @classmethod
    def get_codec(cls, bytes_):
        prefix = cls._extract_prefix(bytes_)
        try:
            return CODE_TABLE[prefix]
        except KeyError:
            raise ValueError('Prefix {} not present in the lookup table'.format(prefix))


def add_prefix(multicodec, bytes_):
    return Multicodec.add_prefix(multicodec, bytes_)


def remove_prefix(bytes_):
    return Multicodec.remove_prefix(bytes_)


def get_codec(bytes_):
    return Multicodec.get_codec(bytes_)
