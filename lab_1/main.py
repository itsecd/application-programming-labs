import argparse
from collections import Counter
import re


def get_filename() -> str:
    """
    Получает имя файла из аргументов командной строки
    :return: строку, которая была передана как аргумент командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str)
    args = parser.parse_args()
    return args.file_name


def read(filename: str) -> str:
    """
    Читает файл
    :param filename: имя файла
    :return: данные из файла в виде строки
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text=file.read()
        return text
    except:
        raise FileNotFoundError("File not found.")


def extract_names(text: str) -> list:
    """
    Извлекает имена с использованием регулярных выражений
    :param text: данные из файла
    :return: список имен
    """
    pattern = r'Имя:\s*([а-яА-Я]+)'
    return re.findall(pattern, text)


def get_most_common_name(names: list):
    """
    Определяет имя, которое чаще всего встречается
    :param names: список имен
    :return: самое распространенное имя и его количество повторений
    """
    name_counter = Counter(names)
    return name_counter.most_common(1)


def main():
    try:
        filename = get_filename()
        text = read(filename)
        names = extract_names(text)
        most_common_name = get_most_common_name(names)
        print(most_common_name)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()