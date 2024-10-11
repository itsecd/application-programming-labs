import argparse
import re

def get_filename() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    return parser.parse_args().filename


def read_file(filename: str) -> str:
    with open(filename, "r", encoding='utf-8') as file:
        return file.read()


def kolichestvo_myzikov(text: str) -> int:

   # Подсчитывает количество анкет мужчин в тексте.
    pattern = r"Пол:\s*Мужской"
    return len(re.findall(pattern, text))

if __name__ == "__main__":
    filename = get_filename()
    text = read_file(filename)
    print(f"Количество анкет мужчин: {kolichestvo_myzikov(text)}")