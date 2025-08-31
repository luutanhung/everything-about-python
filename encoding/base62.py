def base62_encode(num: str) -> str:
    """Encodes a positive number into a Base62 string.

    Base62 encoding is a way to represent a number using 62 unique characters:
    0-9, a-z, and A-Z. This is useful for creating short, URL-friendly identifiers.

    Args:
        num: The positive integer to encode.

    Returns:
        The Base62 encoded string.

    Raises:
        TypeError: If `num` is not a positive integer.

    Examples:
        >>> base62_encode(1234567890)
        '1ly7vk'
        >>> base62_encode(61)
        'Z'
        >>> base62_encode(0)
        '0'
    """

    import string

    if not isinstance(num, int) or num < 0:
        raise TypeError("Input must be a non-negative integer.")

    chars: list[str] = string.digits + string.ascii_letters

    if num == 0:
        return chars[0]
    base62: list[str] = []
    while num > 0:
        num, remainder = divmod(num, 62)
        base62.append(chars[remainder])
    return "".join(reversed(base62))


def base62_decode(s: str) -> int:
    """Decodes a base62 encoded string into a positive integer.

    Base62 encoding uses a set of 62 characters (0-9, a-z, A-Z) to represent a number. This function
    reverses that process, converting the string back into its original integer value.

    rgs:
        s: The Base62 encoded string to decode.

    Returns:
        The decoded integer.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string contains characters not in the Base62 set.

    Examples:
        >>> base62_decode("1ly7vk")
        1234567890
        >>> base62_decode("Z")
        61
        >>> base62_decode("0")
        0
    """

    import string

    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    chars: list[str] = string.digits + string.ascii_letters
    char_mp = {chr: i for i, chr in enumerate(chars)}
    num: int = 0
    for chr in s:
        num = num * 62 + char_mp[chr]
    return num


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
