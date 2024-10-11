import argparse
import re


def get_filename() -> str:
    """
    Получает имя файла из аргументов командной строки.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help='Input the name of file: ')
    return parser.parse_args().file_name


def read_file(file_name: str) -> str:
    """
    Считывает содержимое файла.
    :param file_name: имя файла
    :return: содержимое файла
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")


def find_female_names(text: str) -> list:
    """
    Ищет все уникальные женские имена.
    :param text: текст с информацией о людях
    :return: список уникальных женских имен
    """
    female_names = set()
    match_profile = re.findall(r'Имя: (\w+)\nПол: Женский', text)
    for name in match_profile:
        female_names.add(name)
    return list(female_names)


def find_female_names_starting_with_a(female_names: list) -> list:
    """
    Ищет женские имена, начинающиеся с буквы "А".
    :param female_names: список уникальных женских имен
    :return: список уникальных женских имен, начинающихся с буквы "А"
    """
    names_starting_with_a = list()
    for name in female_names:
        if name.startswith('А'):
            names_starting_with_a.append(name)
    return names_starting_with_a


def main():
    try:
        file_name = get_filename()
        text = read_file(file_name)
        female_names = find_female_names(text)
        res = find_female_names_starting_with_a(female_names)
        print(res)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
