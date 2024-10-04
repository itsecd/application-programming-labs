import argparse
import re

def read_file(path: str) -> str:
    """
    Чтение содержимого файла.
    :param path: Строковый путь к файлу.
    :return: Содержимое файла в виде строки.
    """
    try:
        file = open(path, 'r', encoding='utf-8')
        file_contents = file.read()
        file.close()
        return file_contents
    except Exception as exc:
        print(exc)


def count_men(data: str) -> int:
    """
    Подсчет количества анкет мужчин в списке.
    :param data: Список.
    :return: Количество анкет мужчин.
    """
    try:
        pattern = "Пол: Мужской"
        counter = re.findall(pattern, data)
        return len(counter)
    except Exception as exc:
        print(exc)

def main(path: str) -> None:
    """
    Выводит количество анкет мужчин в файле по данному адресу
    :param path: Путь к файлу с анкетами.
    :return: Количество анкет мужчин.
    """
    try:
        file_data = read_file(path)
        count = count_men(file_data)
        print(f"Количество анкет мужчин в списке = {count}")
    except Exception as exc:
        print(exc)

if __name__ == '__main__':

    main("data.txt")

"""
file = open("data.txt", "r", encoding='utf-8')
text = file.read()
file.close()
pattern = "Пол: Мужской"
man_count = re.findall(pattern, text)
print(len(man_count))


strings = file.readline()
print(text)

"""