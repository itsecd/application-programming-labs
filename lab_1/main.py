import argparse
import re

def get_filename() -> str:
    """
    Получает имя файла, переданного в качестве аргумента командной строки.

    Returns:
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
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def kolichestvo_myzikov(text: str) -> int:
    """
    Подсчитывает количество вхождений слова "Мужской" в заданном тексте.

    Args:
        text (str): Текст, в котором необходимо выполнить поиск.

    Returns:
        int: Количество вхождений слова "Мужской".
    """
    pattern = r"\bМужской\b"
    return len(re.findall(pattern, text))

if __name__ == "__main__":
    filename = get_filename()
    text = read_filename(filename)
    print(f"количество мужиков: {kolichestvo_myzikov(text)}")