def extract_numbers_using_character_class(s: str):
    """
    Given a sentence, find and extract all the numbers within that sentence.

    >>> text: str = "The year 2024 has 366 days, and a standard week has 7 days. This recipe requires 2 cups of sugar and 1 cup of flour."; extract_numbers_using_character_class(text)
    ['2024', '366', '7', '2', '1']
    """
    import re

    prog = re.compile("[0-9]+")
    return prog.findall(s)


def extract_numbers_using_digit_sequence(text: str):
    """
    Given a sentence, find and extract all the numbers within that sentence.

    >>> text: str = "The year 2024 has 366 days, and a standard week has 7 days. This recipe requires 2 cups of sugar and 1 cup of flour."; extract_numbers_using_digit_sequence(text)
    ['2024', '366', '7', '2', '1']
    """
    import re

    prog = re.compile("\d+")
    return prog.findall(text)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
