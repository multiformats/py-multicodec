import varint

from .constants import NAME_TABLE, CODE_TABLE


class Multicodec(object):
    @classmethod
    def get_prefix(cls, multicodec):
        try:
            prefix = varint.encode(NAME_TABLE[multicodec])
        except KeyError:
            raise ValueError('{} multicodec is not supported.'.format(multicodec))
        return prefix

    @classmethod
    def add_prefix(cls, multicodec, bytes_):
        # @TODO: add type checking for bytes
        prefix = cls.get_prefix(multicodec)
        return b''.join([prefix, bytes_])

    @classmethod
    def extract_prefix(cls, bytes_):
        return varint.decode_bytes(bytes_)

    @classmethod
    def remove_prefix(cls, bytes_):
        prefix_int = cls.extract_prefix(bytes_)
        prefix = varint.encode(prefix_int)
        return bytes_[len(prefix):]

    @classmethod
    def get_codec(cls, bytes_):
        prefix = cls.extract_prefix(bytes_)
        try:
            return CODE_TABLE[prefix]
        except KeyError:
            raise ValueError('Prefix {} not present in the lookup table'.format(prefix))


def get_prefix(multicodec):
    return Multicodec.get_prefix(multicodec)


def add_prefix(multicodec, bytes_):
    return Multicodec.add_prefix(multicodec, bytes_)


def remove_prefix(bytes_):
    return Multicodec.remove_prefix(bytes_)


def extract_prefix(bytes_):
    return Multicodec.extract_prefix(bytes_)


def get_codec(bytes_):
    return Multicodec.get_codec(bytes_)


def is_codec(name):
    return name in NAME_TABLE
