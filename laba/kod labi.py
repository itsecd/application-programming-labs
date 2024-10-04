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
    :param data: Список анкет.
    :return: Количество анкет мужчин.
    """
    try:
        pattern = "Пол: Мужской"
        counter = re.findall(pattern, data)
        return len(counter)
    except Exception as exc:
        print(exc)


def get_path() -> str:
    """
    Получение пути к файлу из консоли.
    :return: Путь к файлу.
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("file_path", type = str,
                            help = "Path to the file with questionnaires")
        args = parser.parse_args()
        return args.file_path
    except Exception as exc:
        print(exc)


def main() -> None:
    """
    Выводит количество анкет мужчин в файле по введенному в консоли адресу
    :return: Количество анкет мужчин.
    """
    try:
        path = get_path()
        file_data = read_file(path)
        count = count_men(file_data)
        print(f"Количество анкет мужчин в списке = {count}")
    except Exception as exc:
        print(exc)


if __name__ == '__main__':

    main()