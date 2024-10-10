import argparse
import re


def get_file_name() -> str:
    """
    считывание имени файл из командной строки
    :return: имя файла
    """
    parser = argparse.ArgumentParser()  # создание экземпляра парсера
    parser.add_argument('filename', type=str, help='name of file')  # добавление позиционного аргумента командной строки
    args = parser.parse_args().filename  # парсинг аргументов
    return args


def read_file(namefile: str) -> str:
    """
    считывает все содержимое файла в одну строку
    :param namefile: имя файла
    :return:
        - text если нет ошибок
        - пустой список если есть ошибки, связанные с файлом
    """
    try:
        with open(namefile, mode='r', encoding="utf-8") as file:
            text = file.read()
            return text
    except Exception as e:
        print(f"Error: {e}")
        return []


def split_questionnaires(lines: str) -> list[str]:
    """
    Разделяет текст анкет на отдельные анкеты.
    :param lines: Строка, содержащая текст анкет
    :return: split_text
    """
    pattern = r'\d+\)\s*'
    split_text = re.split(pattern, lines, maxsplit=0)
    return split_text


def search_by_template(split_text: list[str]) -> list[str]:
    """
    Ищет анкеты по шаблону
    :param split_text: список анкет
    :return: found_list
    """
    pattern = r'Фамилия: Иванов[а]?'
    found_list = list()
    for questionnaire in split_text:
        if re.search(pattern, questionnaire):
            found_list.append(questionnaire)
    return found_list


def print_questionnaire(found_list: list[str]) -> None:
    """
    Вывод нужных анкет
    :param found_list: список нужных анкет
    :return: None
    """
    for questionnaire in found_list:
        print(questionnaire)
    print()


def main():
    namefile = get_file_name()
    text = read_file(namefile)
    questionnaires = split_questionnaires(text)
    ivanovs_list = search_by_template(questionnaires)
    print_questionnaire(ivanovs_list)


if __name__ == "__main__":
    main()