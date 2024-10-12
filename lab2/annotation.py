import csv
import os

def annotation_creation(dir_name:str,annotation_file: str) -> None:
    """
    Функция создает аннотацию, создаётся csv файл, записывается заголовок ('Relative path', 'Absolute path') и заносятся относительный и абсолютный пути.
    :param dir_name: директория с изображениями
    :param annotation_file:csv файл для аннотации
    :return: None
    """
    with open(annotation_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Relative path', 'Absolute path'])
        for filename in os.listdir(dir_name):
            rel_path=os.path.relpath(os.path.join(dir_name,filename),start=dir_name)
            abs_path=os.path.abspath(os.path.join(dir_name,filename))
            writer.writerow([rel_path,abs_path])
