import argparse
import re


def get_filename() -> str:
    """принимаем имя файла"""
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='your file name pls')
    args = parser.parse_args()

    return args.filename


def open_file(filename: str) -> str:
    """"открываем файл"""
    with open(filename, "r", encoding="UTF-8") as file:
        text = file.read()
    return text


def search_for_quest(text: str) -> list[str]:
    """ищем анкеты удовлетворяющих условию"""
    patern = r'\d+\)\n'
    split = re.split(patern, text, maxsplit=0)
    result = []
    for quest in split:
        if "Москва" in quest:
            result.append(quest)
        else:
            continue
    return result


def print_quest(sort_text: list[str]) -> None:
    """"вывод анкет"""
    print("\n")
    for quest in sort_text:
        print(quest)
    return None


def main() -> None:
    try:
        filename = get_filename()
        text = open_file(filename)
        print_quest(search_for_quest(text))
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()