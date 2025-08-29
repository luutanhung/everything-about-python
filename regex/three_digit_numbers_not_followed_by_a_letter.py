from typing import Optional


def not_followed_by_a_letter(text: str = None) -> Optional[list]:
    """
    Given a block of text, find and extract all three-digit numbers that are not immediately followed by a letter.

    >>> not_followed_by_a_letter("Item numbers are 101, 202, and 303b. The product codes are B-456, Z-987. The years are 2023, 1999, and 1888. A single part is 500. A special case is 777X.")
    ['101', '202', '456', '987', '500']
    """
    import re

    prog = re.compile(r"\b\d{3}\b")
    return prog.findall(text)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
