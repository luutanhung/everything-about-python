def base62_encode(num: str) -> str:
    """
    >>> base62_encode(1234567890)
    '1ly7vk'
    """

    import string

    chars: list[str] = string.digits + string.ascii_letters

    if num == 0:
        return chars[0]
    base62: list[str] = []
    while num > 0:
        num, remainder = divmod(num, 62)
        base62.append(chars[remainder])
    return "".join(reversed(base62))


def base62_decode(s: str) -> int:
    """
    >>> base62_decode("1ly7vk")
    1234567890
    """

    import string

    chars: list[str] = string.digits + string.ascii_letters
    char_mp = {chr: i for i, chr in enumerate(chars)}
    num: int = 0
    for chr in s:
        num = num * 62 + char_mp[chr]
    return num


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
