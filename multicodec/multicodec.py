import varint

from .constants import NAME_TABLE, CODE_TABLE


class Multicodec:
    def __init__(self, codecs={}):
        NAME_TABLE_ = {name: value['prefix'] for name, value in codecs.items()}
        CODE_TABLE_ = {value['prefix']: name for name, value in codecs.items()}
        self.__NAME_TABLE = {
            **NAME_TABLE,
            **NAME_TABLE_
        }
        self.__CODE_TABLE = {
            **CODE_TABLE,
            **CODE_TABLE_
        }

    def extract_prefix(self, bytes_):
        """
        Extracts the prefix from multicodec prefixed data

        :param bytes bytes_: multicodec prefixed data
        :return: prefix for the prefixed data
        :rtype: bytes
        :raises ValueError: when incorrect varint is provided
        """
        try:
            return varint.decode_bytes(bytes_)
        except TypeError:
            raise ValueError('incorrect varint provided')


    def get_prefix(self, multicodec):
        """
        Returns prefix for a given multicodec

        :param str multicodec: multicodec codec name
        :return: the prefix for the given multicodec
        :rtype: byte
        :raises ValueError: if an invalid multicodec name is provided
        """
        try:
            prefix = varint.encode(self.__NAME_TABLE[multicodec])
        except KeyError:
            raise ValueError('{} multicodec is not supported.'.format(multicodec))
        return prefix


    def add_prefix(self, multicodec, bytes_):
        """
        Adds multicodec prefix to the given bytes input

        :param str multicodec: multicodec to use for prefixing
        :param bytes bytes_: data to prefix
        :return: prefixed byte data
        :rtype: bytes
        """
        prefix = self.get_prefix(multicodec)
        return b''.join([prefix, bytes_])


    def remove_prefix(self, bytes_):
        """
        Removes prefix from a prefixed data

        :param bytes bytes_: multicodec prefixed data bytes
        :return: prefix removed data bytes
        :rtype: bytes
        """
        prefix_int = self.extract_prefix(bytes_)
        prefix = varint.encode(prefix_int)
        return bytes_[len(prefix):]


    def get_codec(self, bytes_):
        """
        Gets the codec used for prefix the multicodec prefixed data

        :param bytes bytes_: multicodec prefixed data bytes
        :return: name of the multicodec used to prefix
        :rtype: str
        """
        prefix = self.extract_prefix(bytes_)
        try:
            return self.__CODE_TABLE[prefix]
        except KeyError:
            raise ValueError('Prefix {} not present in the lookup table'.format(prefix))


    def is_codec(self, name):
        """
        Check if the codec is a valid codec or not

        :param str name: name of the codec
        :return: if the codec is valid or not
        :rtype: bool
        """
        return name in self.__NAME_TABLE
