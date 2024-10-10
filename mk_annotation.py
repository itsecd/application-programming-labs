import csv
import os

def create_annotation(imgdir: str, csv_path: str) -> None:
    """
    Creates annotation (.csv file) with absolute and relative paths to images
    :param imgdir: Directory with images
    :param csv_path: .csv file that is used to write annotation
    """
    with open(csv_path, mode='w', newline='', encoding='utf-8') as annotation_file:
        writer = csv.writer(annotation_file)
        headers = ['Relative path', 'Absolute path']
        writer.writerow(headers)

        for file in os.listdir(imgdir):
            relative_path = os.path.relpath(file, start=imgdir)
            absolute_path = os.path.abspath(file)
            writer.writerow([relative_path, absolute_path])
