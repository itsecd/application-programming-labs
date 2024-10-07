import argparse
import datetime
import re
import os

def parse_arguments() -> str:
    """
    Извлекает путь к файлу из аргументов командной строки.
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('input_file', type=str, help='Путь к файлу с днями рождения')
    return arg_parser.parse_args().input_file

def load_file_content(file_path: str) -> str:
    """
    Считывает содержимое файла.
    параметры (file_path): Путь к файлу.
    возвращает: Содержимое файла в виде строки.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Указанный файл '{file_path}' не найден.")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except OSError as err:
        raise RuntimeError(f"Ошибка при открытии файла '{file_path}': {err}")

def find_birthdays(data: str) -> list:
    """
    Ищет дни рождения в тексте.
    Parameter (data): Текстовый контент для поиска.
    Return: Список строк с датами рождения в формате "DD.MM.YYYY".
    """
    return re.findall(r"\d{2}\.\d{2}\.\d{4}", data)

def count_people_in_age_range(birthdays: list, age_min: int = 30, age_max: int = 40) -> int:
    """
    Подсчитывает количество людей в заданном возрастном диапазоне.
    параметр (birthdays): Список дней рождения.
    параметр (age_min): Нижняя граница возраста.
    параметр (age_max): Верхняя граница возраста.
    возвращает: Количество людей в диапазоне.
    """
    current_date = datetime.datetime.now()
    count = 0

    for birthday in birthdays:
        try:
            birth_date = datetime.datetime.strptime(birthday, '%d.%m.%Y')
            age = (current_date - birth_date).days / 365
            if age_min <= age <= age_max:
                count += 1
        except ValueError:
            print(f"Неверный формат даты: {birthday}")
            continue

    return count

def run():
    """
    Основная функция программы.
    """
    try:
        file_path = parse_arguments()
        file_content = load_file_content(file_path)
        birth_dates = find_birthdays(file_content)
        result = count_people_in_age_range(birth_dates)
        print(f"Количество людей в возрасте от 30 до 40 лет: {result}")
    except Exception as error:
        print(f"Произошла ошибка: {error}")

if __name__ == "__main__":
    run()
