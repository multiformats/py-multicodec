import varint

from .constants import NAME_TABLE, CODE_TABLE, PRIVATE_RANGE


def extract_prefix(bytes_):
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


def get_prefix(multicodec):
    """
    Returns prefix for a given multicodec

    :param str / int multicodec: str for multicodec name, int if you wish to use a private code
    :return: the prefix for the given multicodec
    :rtype: byte
    :raises ValueError: if an invalid multicodec name is provided
    """
    if is_private_codec(multicodec):
        return varint.encode(multicodec)

    try:
        prefix = varint.encode(NAME_TABLE[multicodec])
    except KeyError:
        raise ValueError('{} multicodec is not supported.'.format(multicodec))
    return prefix


def add_prefix(multicodec, bytes_):
    """
    Adds multicodec prefix to the given bytes input

    :param str / int multicodec: str for multicodec to use for prefixing, int if you wish to use a private code
    :param bytes bytes_: data to prefix
    :return: prefixed byte data
    :rtype: bytes
    """
    prefix = get_prefix(multicodec)
    return b''.join([prefix, bytes_])


def remove_prefix(bytes_):
    """
    Removes prefix from a prefixed data

    :param bytes bytes_: multicodec prefixed data bytes
    :return: prefix removed data bytes
    :rtype: bytes
    """
    prefix_int = extract_prefix(bytes_)
    prefix = varint.encode(prefix_int)
    return bytes_[len(prefix):]


def get_codec(bytes_):
    """
    Gets the codec used for prefix the multicodec prefixed data

    :param bytes bytes_: multicodec prefixed data bytes
    :return: name of the multicodec used to prefix, int codec if it is part of private space
    :rtype: str / int
    """
    prefix = extract_prefix(bytes_)
    if is_private_codec(prefix):
        return prefix

    try:
        return CODE_TABLE[prefix]
    except KeyError:
        raise ValueError('Prefix {} not present in the lookup table'.format(prefix))


def is_private_codec(codec):
    """
    Check if the codec is within the private range or not

    :param int codec: codec to check for permitted to use under private space
    :return: True if the codec lies within the private usage range, False otherwise
    :rtype: bool
    """
    if isinstance(codec, int) and PRIVATE_RANGE[0] <= codec <= PRIVATE_RANGE[1]:
        return True
    return False


def is_codec(name):
    """
    Check if the codec is a valid codec or not

    :param str name: name of the codec
    :return: if the codec is valid or not
    :rtype: bool
    """
    return name in NAME_TABLE
