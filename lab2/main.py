import argparse
from argparse import Namespace
import csv
from icrawler.builtin import GoogleImageCrawler
import os
import re
import shutil

DEFAULT_DIR_PATH = "images"
DEFAULT_CSV_PATH = "annotation.csv"
COUNT = 1000


def setup_images(object_on_photo: str, path_to_folder: str, count: int) -> None:
    """
    Setup images to folder
    :param object_on_photo: object which will be on images
    :param path_to_folder: current PATH to folder,where will be store images
    :param count: max count of images
    :return: None
    """
    if os.path.exists(path_to_folder):
        shutil.rmtree(path_to_folder)
        os.mkdir(path_to_folder)
    else:
        os.mkdir(path_to_folder)

    google_crawler = GoogleImageCrawler(
        storage={'root_dir': path_to_folder},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4)
    google_crawler.crawl(keyword=object_on_photo, max_num=count)


def make_annotation(path_to_folder: str, path_to_annotation: str) -> None:
    """
    Func is making annotation with current and global PATHs images
    :param path_to_folder: PATH to folder where images saved
    :param path_to_annotation: PATH to csv file
    :return: None
    """
    list_images = os.listdir(path_to_folder)
    data_to_annotation = []
    for i in range(len(list_images)):
        current_dir = os.path.dirname(os.path.abspath(list_images[i]))
        absolute_path = f"{current_dir}\\{path_to_folder}\\{list_images[i]}"
        current_path = f"{path_to_folder}\\{list_images[i]}"
        data_element = [str(i), current_path, absolute_path]
        data_to_annotation.append(data_element)

    if os.path.exists(path_to_annotation):
        os.remove(path_to_annotation)

    with open(path_to_annotation, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_to_annotation)  # запись всех строк


class MyIterator:
    def __init__(self, collection: list):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.collection):
            item = self.collection[self.index]
            self.index += 1
            normalized_items = re.split(",", item)
            normalized_items[2] = normalized_items[2][:-1]
            return normalized_items
        else:
            raise StopIteration


def open_file(path_to_file: str) -> list[str]:
    """
    Func is opening file
    :param path_to_file: PATH to file,which will be open
    :return: data from file in list[str]
    """
    with open(path_to_file, 'r') as file:
        data = file.readlines()
    return data


def arg_parcer() -> Namespace:
    """
    Parce args from command line
    :return: Class Object Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "object_on_photo",
        type=str,
        help="Object on images.")
    parser.add_argument(
                        "-d",
                        "--dirpath",
                        type=str,
                        default=DEFAULT_DIR_PATH,
                        help="Current PATH to directory where will be save images.")
    parser.add_argument(
                        "-c",
                        "--csvpath",
                        type=str,
                        default=DEFAULT_CSV_PATH,
                        help="Current PATH to csv file with PATHs to all images.")
    return parser.parse_args()


def main() -> int:
    args = arg_parcer()
    data = ''
    try:
        setup_images(args.object_on_photo, args.dirpath, COUNT)
        make_annotation(args.dirpath, args.csvpath)
    except Exception:
        print("Wrong directory's PATH or csv file")

    try:
        data = open_file(args.csvpath)
    except FileNotFoundError:
        print("Incorrect file name or PATH")

    myy = MyIterator(data)
    for item in myy:
        print(item)

    return 0


if "__main__" == __name__:
    main()
