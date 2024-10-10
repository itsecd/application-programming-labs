import argparse
import re


def parse_file_argument() -> str:
    """
    Извлекает имя файла из аргументов командной строки
    с помощью модуля 'argparse'.
    :return: Имя файла
    """
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('filepath', type=str, help='Путь к файлу для обработки')
    args = argument_parser.parse_args()
    return args.filepath


def load_file_content(filepath: str) -> str:
    """
    Читает содержимое указанного файла.
    :param filepath: Имя файла для чтения
    :return: Содержимое файла в виде строки
    """
    with open(filepath, "r", encoding="UTF-8") as file:
        return file.read()


def count_male_profiles(text: str) -> int:
    """
    Использует регулярные выражения для поиска всех профилей мужчин
    и подсчёта их количества.
    :param text: Содержимое файла
    :return: Количество мужских профилей
    """
    male_profiles = re.findall(r"Пол:\s*Мужской", text)
    return len(male_profiles)


def run_analysis():
    filepath = parse_file_argument()
    content = load_file_content(filepath)
    male_count = count_male_profiles(content)
    print("Количество мужских профилей в файле:", male_count)


if __name__ == "__main__":
    run_analysis()
