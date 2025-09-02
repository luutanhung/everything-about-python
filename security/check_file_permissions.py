def check_file_permissions(file_path: str) -> dict[str, bool]:
    """
    Checks the read, write, execute permissions of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary containing boolean values for permissions:
              {'readable': bool, 'writable': bool, 'executable': bool}

    Raises:
        FileNotFoundError: If the file does not exist.

    >>> permissions = check_file_permissions("lorem.txt")
    >>> permissions["readable"]
    True
    >>> permissions["writable"]
    True
    >>> permissions["executable"]
    False
    """
    import os

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    permissions: dict[str, bool] = {
        "readable": os.access(file_path, os.R_OK),
        "writable": os.access(file_path, os.W_OK),
        "executable": os.access(file_path, os.X_OK),
    }
    return permissions


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
