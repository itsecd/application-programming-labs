import math
import argparse
import datetime
import re
# ввод через Terminal "python main.py data.txt"  или просто через запуск кода
def get_filename() -> str:
    """
    Получает имя файла, переданного в качестве аргумента командной строки.
    Return:
        str: Имя файла.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of your file')
    args = parser.parse_args()
    return args.filename

def read_filename(filename: str) -> str:
    """
    Читает содержимое файла с заданным именем.

    Args:
        filename (str): Имя файла.

    Returns:
        str: Содержимое файла.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def Amount(text: str) -> int:
    """
    Подсчитывает количество людей от 30 до 40.
    Arg:
        text (str): Текст, в котором необходимо выполнить поиск.
    Return:
        int: Количество людей от 30 до 40.
    pattern:
        в формате дата.месяц.год
    """
    pattern = r"\d\d.\d\d.\d\d\d\d"
    numbers = re.findall(pattern, text)
    count = 0
    for i in numbers:
        birthday = datetime.datetime.now() - datetime.datetime.strptime(i, "%d.%m.%Y")
        if 30 <= (birthday.days / 365) <= 40:
            count += 1
    return count

def main() -> None:
    filename = get_filename()
    text = read_filename(filename)
    print(f"Количество людей от 30 до 40: {Amount(text)}")
if __name__ == "__main__":
    main()