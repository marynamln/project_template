def output_text(text):
    """
    Outputs text to the console.

    Args:
        text (str): the text to output to the console.
    """
    print(text)


def write_to_file(file_path, text):
    """
    Writes text to a file using Python's built-in capabilities.

    Args:
        file_path (str): the path to the file where you want to write the text.
        text (str): the text to be written to the file.
    """
    with open(file_path, "w") as file:
        file.write(text)
