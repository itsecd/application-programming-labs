import argparse
import re


def get_file() -> str:
    """

    Получает имя файла из командной строки.

    Return:
    str: Имя файла.

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of your file')
    args = parser.parse_args()
    return args.filename


def read_file(filename: str) -> str:
    """

    Читает содержимое файла с заданным именем.

    Arg:
    filename (str): Имя файла.

    Return:
    str: Содержимое файла.

    """
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{filename}' не найден.")


def find_female_names(content: str) -> set:
    """

    Находит все женские имена, в заданном тексте.

    Arg:
    content (str): Текст, в котором нужно выполнить поиск.

    Return:
    set: Множество женских имен.

    """
    pattern = r'Имя: ([А-Яа-я]+)\s*Пол: Женский'
    matches = re.findall(pattern, content)
    female_names = find_names_start_a(matches)
    return female_names


def find_names_start_a(matches: list) -> set:
    """

    Находит все имена, начинающиеся с буквы А в заданном списке имен.

    Arg:
    matches (list): Список имен.

    Return:
    set: Множество имен, начинающихся с буквы А.

    """
    female_names = {name for name in matches if (name.startswith('А') or name.startswith('а'))}
    return female_names


def print_female_names(names: set) -> None:
    """

    Выводит все найденные женские имена, начинающиеся с буквы А.

    Arg:
    names (set): Множество женских имен, начинающихся с буквы А.

    """
    if names:
        print("Женские имена, начинающиеся с буквы А:")
        for name in names:
            print(name)
    else:
        print("Нет женских имен, начинающихся с буквы А.")


def main() -> None:
    try:
        filename = get_file()
        file_content = read_file(filename)
        female_names = find_female_names(file_content)
        print_female_names(female_names)
    except ValueError as exc:
        print(f"Ошибка: {exc}")


if __name__ == '__main__':
    main()