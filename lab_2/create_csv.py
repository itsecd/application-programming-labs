import csv
import os

def create_annotation(dir_path: str, filename:str) -> None:
    """
    The function creates annotation file with relative and absolute path of images
    :param dir_path: path to working directory
    :param filename: name of annotation
    :return: None
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Relative path', 'Absolute path'])

        for item in os.listdir(dir_path):
            absolute_path = os.path.abspath(os.path.join(dir_path, item))
            relative_path = os.path.relpath(item, start=dir_path)
            writer.writerow([relative_path, absolute_path])