def check_file_existence_using_os(file_path: str) -> bool:
    """
    Check if a file or directory exists at the specified path using os.

    Args:
        file_path (str): The path to the file or directory.

    Returns:
        bool: True if the file or directory exists, False otherwise

    >>> check_file_existence_using_os("lorem.txt")
    True
    >>> check_file_existence_using_os("non_existent_lorem.txt")
    False
    """

    import os

    return os.path.exists(file_path)


def check_file_existence_using_pathlib(file_path: str) -> bool:
    """
    Check if a file or directory exists using pathlib.

    Args:
        file_path (str): The path to the file or directory.

    Returns:
        bool: True if the file or directory exists, False otherwise

    >>> check_file_existence_using_pathlib("lorem.txt")
    True
    >>> check_file_existence_using_pathlib("non_existent_lorem.txt")
    False
    """

    from pathlib import Path

    return Path(file_path).exists()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
