import re
import argparse

def get_info():
    """
    Запрашиваем необходимую информацию у
    пользователя.

    :file - имя файла
    :name - искомое имя
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = str, help = 'File name')
    parser.add_argument('name', type = str, help = 'Name')
    args = parser.parse_args()

    return args

def file_read(filename: str) -> str:
    """
    Считываем файл.

    :filename - имя файла
    """
    file = open(filename, "r", encoding = "utf-8")
    readed_file = file.read()
    file.close()

    return readed_file

def main_func(name: str, file: str) -> int:
    """
    Основная функция, считающая
    количество анкет с именем, совпадающим с
    введенным пользователем.
    
    :name - имя, введенное пользователем
    :file - файл, в котором будем считать количество
    анкет с введенным именем
    """
    ankets = re.findall(f'Имя: {name}\s', file)
    count = len(ankets)

    return count

def main():
    try:
        file = file_read(get_info().file)
        name = get_info().name

        print(f'Количество анкет с именем {name}: {main_func(name, file)}')
    except:
        print("Invalid file name")

if __name__ == '__main__':
    main()    

