import re
from datetime import datetime
import argparse

def get_filename() -> str:
    """
    Получение имени файла, переданного в качестве аргумента командной ст.
    Returns:
         str: Имя файла
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help = 'name of your file')
    args = parser.parse_args()
    return args.filename

def read_file(filename: str) -> str:
    """
    Читает содержимое файл с заданным именем.
    Args:
        filename(str): Имя файла
    Returns:
        str: Содержимое файла

    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def c_of_30_40(text: str) -> int:
    """
    Считает количество человек, возраст который лежит от 30 до 40 лет.
    Args:
        text(str): Текст, в котором выполняется подсчет
    Returns:
        int: количество человек возрастом 30-40
    """
    c = 0
    pattern = r'\d+[.]\d+[.]\d+'
    dates = re.findall(pattern, text)
    for i in range(0, len(dates)):
        birthdate = datetime.strptime(dates[i], "%d.%m.%Y")
        today = datetime.today()
        age = today.year - birthdate.year  - ((today.month, today.day) < (birthdate.month, birthdate.day))
        if (30 <= age <= 40):
            c+=1
    return c

if __name__ == "__main__":
    filename = get_filename()
    text = read_file(filename)
    k = c_of_30_40(text)
    print("Количество чел возрастом 30-40 = ", k)
