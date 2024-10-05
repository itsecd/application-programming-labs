import argparse
import re


def get_filename() -> str:
    """принимаем имя файла"""
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', type=str, help='your file name pls')
        args = parser.parse_args()

        return args.filename
    except ValueError as exc:
        print(f"Error: {exc}")


def open_file(filename: str) -> str:
    """"открываем файл"""
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            text = file.read()
        return text
    except ValueError as exc:
        print(f"Error: {exc}")


def search_for_questionnaires(text: str) -> list[str]:
    """ищем нужные анкеты подходящие под условия"""
    pattern = r'\d+\)\n'
    split_text = re.split(pattern, text, maxsplit=0)
    sort_text = []

    for questionnaires in split_text:
        if "Иванов" in questionnaires:
            sort_text.append(questionnaires)
        elif "Иванова" in questionnaires:
            sort_text.append(questionnaires)
        else:
            continue
    return sort_text


def print_questionnaires(sort_text: list[str]) -> None:
    """"вывод анкет"""
    print("\n")
    for questionnaires in sort_text:
        print(questionnaires)
    return None


def main() -> None:
    filename = get_filename()
    text = open_file(filename)
    print_questionnaires(search_for_questionnaires(text))
    return None


if __name__ == "__main__":
    main()
