from app.io.input import input_text, read_file
from app.io.output import output_text, write_to_file


def main():
    inputted_text = input_text()
    output_text(inputted_text)
    write_to_file(r"C:\Users\User\Desktop\python-for-big-data-and-data-science\project_template\data\output1.txt", inputted_text)

    text_from_file = read_file(r"C:\Users\User\Desktop\python-for-big-data-and-data-science\project_template\data\text.txt")
    output_text(text_from_file)
    write_to_file(r"C:\Users\User\Desktop\python-for-big-data-and-data-science\project_template\data\output2.txt", text_from_file)

if __name__ == "__main__":
    main()
