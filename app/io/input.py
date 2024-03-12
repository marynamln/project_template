def input_text():
    """
    Text input from the console.

    Returns:
        str: Inputted text.
    """
    text = input("Input text: ")
    return text


def read_file(file_path):
    """
    Reading from a file using built-in python capabilities.

    Args:
        file_path (str): path of the file from which the reading takes place.

    Returns:
        str: Text from file.
    """
    with open(file_path, "r") as file:
        text = file.read()
    return text


def read_file_pandas(file_path):
    """
    Reading from a file using the pandas library.

    Args:
        file_path (str): path of the file from which the reading takes place.
    """
    pass
