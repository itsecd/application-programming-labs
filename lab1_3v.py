import argparse
import datetime
import re
import os


def parse_arguments() -> str:
    """
    Получает имя файла с данными из аргументов командной строки.
    """
    parser = argparse.ArgumentParser(description="Скрипт для подсчета людей по дням рождения.")
    parser.add_argument('file', type=str, help='Имя входного файла с данными')
    return parser.parse_args().file


def read_file_content(file_path: str) -> str:
    """
    Загружает содержимое файла.
    Parameter (file_path): Путь к файлу.
    Return: Содержимое файла.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл '{file_path}' не найден.")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise RuntimeError(f"Ошибка при чтении файла '{file_path}': {e}")


def extract_birthdays(text: str) -> list:
    """
    Извлекает дни рождения из текстового файла.
    Parameter (text): Исходный текст, содержащий информацию о людях.
    Return: Список дней рождения в формате "DD.MM.YYYY".
    """
    return re.findall(r"\d{2}\.\d{2}\.\d{4}", text)


def count_age_group(birthdays: list) -> int:
    """
    Подсчитывает количество людей в возрасте от 30 до 40 лет.
    Parameter (birthdays): Список дней рождения.
    Return: Количество людей в заданном возрастном диапазоне.
    """
    current_date = datetime.datetime.now()
    c = 0
    for birthday in birthdays:
        try:
            birth_date = datetime.datetime.strptime(birthday, '%d.%m.%Y')
            age = (current_date - birth_date).days / 365
            if 30 <= age <= 40:
                c += 1
        except ValueError:
            print(f"Некорректная дата: {birthday}")
            continue
    return c


def main():
    try:
        file_name = parse_arguments()
        content = read_file_content(file_name)
        birthdays = extract_birthdays(content)
        result_count = count_age_group(birthdays)
        print(result_count)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
