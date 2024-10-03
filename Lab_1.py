import argparse
import re
import os


def file_name() -> str:
    """
    Пользователь вводит название файла и искомое имя через командную строку
    :return: название файла и искомое имя
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help='Имя файла')
    parser.add_argument('human_name', type=str, help='Имя искомого человека')
    return parser.parse_args()


def open_file(file_path: str) -> str:
    """
    Считывает данные из файла
    :param file_path: путь к файлу
    :return: данные из файла
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл '{file_path}' не найден")
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            text = file.read()
            return text
    except Exception as e:
        raise RuntimeError(f"Ошибка при чтении файла '{file_path}': {e}")



def search_count_name(human_name: str, text: str) -> int:
    """
    поиск кол-во имён, совпадающих с введенным пользователем
    :param human_name: имя, введенное пользователем
    :param text: данные в виде строки
    :return: кол-во имён, совпадающих с введенным пользователем
    """
    return len(re.findall(human_name,text))


def print_count(c: int):
    """
    выводит кол-во имён, совпадающих с введенным пользователем
    :param c: кол-во имён, совпадающих с введенным пользователем
    :return: none
    """
    print(c)


def main():
    """
    поочередно используем функции
    :return: none
    """
    try:
        args = file_name()
        text = open_file(args.file_name)
        count = search_count_name(args.human_name, text)
        print_count(count)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()




