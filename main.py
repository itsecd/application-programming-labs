import argparse
import re
def file_name()->str:
    """
    Пользователь вводит название файла через командную строку
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help='Имя файла')
    args = parser.parse_args()
    return args.file_name
def open_file(namefile: str) -> str:
    """
    Считываем данные из файла
    :param namefile:название файла
    :return:данные в виде строки из файла
    """
    with open(namefile,"r", encoding="utf-8") as file:
        text = file.read()
    return text
def split_text(text: str) -> list[str]:
    """
    Разделяем по анкетам
    :param text: наши данные в виде строки
    :return: список из анкет по отдельности
    """
    pattern=r'\d{1,2}\)'
    container=re.split(pattern,text)
    return container
def profile_search(container: list):
    """
    Если находим нужные-печатаем
    :param container: список анкет по отдельности
    :return:ничего не возвращаем, печатаем анкеты, удовлетворяющие условию второго варианта
    """
    c=0
    for i in container:
        if re.search(r'\+7 927',i):
            c+=1
            print(str(c)+')')
            print(i.strip())
def main():
    """
    Используем наши функции
    :return:
    """
    filename=file_name()
    text=open_file(filename)
    container = split_text(text)
    profile_search(container)
if __name__ == "__main__":
    main()