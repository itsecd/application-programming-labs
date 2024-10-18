import csv
import os
import os.path as op


def create_csvfile(dir_name: str, annotation_file: str) -> None:
    """
    Creating csv-file with annotation
    :param dir_name: name of directory with pictures
    :param annotation_file: name of file to save annotation
    :return:
    """
    with open(annotation_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Absolute path", "relative path"])
        list_of_pictures = os.listdir(dir_name)
        for i in list_of_pictures:
            a = op.abspath(op.join(dir_name, i))
            r = op.relpath(op.join(dir_name, i), start=".")
            writer.writerow([a, r])
