import varint

from .constants import CODE_TABLE, NAME_TABLE


def extract_prefix(bytes_: bytes) -> int:
    """
    Extracts the prefix from multicodec prefixed data

    :param bytes bytes_: multicodec prefixed data
    :return: prefix for the prefixed data
    :rtype: int
    :raises ValueError: when incorrect varint is provided
    """
    try:
        return varint.decode_bytes(bytes_)
    except TypeError as err:
        raise ValueError("incorrect varint provided") from err


def get_prefix(multicodec: str) -> bytes:
    """
    Returns prefix for a given multicodec

    :param str multicodec: multicodec codec name
    :return: the prefix for the given multicodec
    :rtype: bytes
    :raises ValueError: if an invalid multicodec name is provided
    """
    try:
        prefix = varint.encode(NAME_TABLE[multicodec])
    except KeyError as err:
        raise ValueError(f"{multicodec} multicodec is not supported.") from err
    return prefix


def add_prefix(multicodec: str, bytes_: bytes) -> bytes:
    """
    Adds multicodec prefix to the given bytes input

    :param str multicodec: multicodec to use for prefixing
    :param bytes bytes_: data to prefix
    :return: prefixed byte data
    :rtype: bytes
    """
    prefix = get_prefix(multicodec)
    return b"".join([prefix, bytes_])


def remove_prefix(bytes_: bytes) -> bytes:
    """
    Removes prefix from a prefixed data

    :param bytes bytes_: multicodec prefixed data bytes
    :return: prefix removed data bytes
    :rtype: bytes
    """
    prefix_int = extract_prefix(bytes_)
    prefix = varint.encode(prefix_int)
    return bytes_[len(prefix) :]


def get_codec(bytes_: bytes) -> str:
    """
    Gets the codec used for prefix the multicodec prefixed data

    :param bytes bytes_: multicodec prefixed data bytes
    :return: name of the multicodec used to prefix
    :rtype: str
    """
    prefix = extract_prefix(bytes_)
    try:
        return CODE_TABLE[prefix]
    except KeyError as err:
        raise ValueError(f"Prefix {prefix} not present in the lookup table") from err


def is_codec(name: str) -> bool:
    """
    Check if the codec is a valid codec or not

    :param str name: name of the codec
    :return: if the codec is valid or not
    :rtype: bool
    """
    return name in NAME_TABLE
