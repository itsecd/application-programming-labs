import re
import argparse


def get_filepath() -> str:

    #function gets file path from cmd
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='your filepath')
    args = parser.parse_args()
    return args.filepath


def read_file(file_path: str) -> str:
    #function reads file into string using file path
    with open(file_path, 'r', encoding='utf-8') as file:
        text: str = file.read()
        return text


def split_forms(text: str) -> list[str]:
    #function splits string into list_of_strings
    pattern = r'\d+[)]'
    text.strip()
    list_of_forms: list[str] = re.split(pattern, text)
    return list_of_forms


def print_moscow(list_of_forms: list[str]):
    #function prints all forms with Москва in it
    for form in list_of_forms:
        if 'Москва' in form:
            print(form.strip(), '\n')


def main() -> None:
    try:
        filepath = get_filepath()
        text = read_file(filepath)
        list_of_forms = split_forms(text)
        print_moscow(list_of_forms)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
