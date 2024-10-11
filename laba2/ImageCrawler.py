from icrawler.builtin import GoogleImageCrawler
import csv
import os


def get_images(keyword: str, save_dir: str)->None:
    """
    Downloads images based on keyword to the file save_dir
    :param keyword: word on the basis of which the function will download the images
    :param save_dir: the name of the file where images will be downloaded
    """
    icrawler = GoogleImageCrawler(storage={'root_dir': save_dir})
    icrawler.crawl(keyword=keyword, max_num=100)


def clear_dir(directory:str)->None:
    """
    Clears the file where images will be saved if this file is not empty
    :param directory: the name of the file
    """
    if os.path.isdir(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else: pass


def get_files(save_dir: str)->list:
    """
    Adds the name of the uploaded images to the list
    :param save_dir: the name of the file where images were uploaded
    :return: the list of the image names
    """
    image_data = []
    for root, dirs, files in os.walk(save_dir):
        for file in files:
            if file.endswith(".png") or file.endswith("jpg"):
                image_data.append(file)
    return image_data


def annotation(files: list, save_dir: str)->None:
    """
    Creates an annotation
    :param files: the list af image names
    :param save_dir: the name of the file where images were saved
    """
    with open('data.csv',mode='w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Absolute path", "Relative path"])
        directory = []
        for i in range(len(files)):
            absolute = os.path.abspath(os.path.join(save_dir, files[i]))
            directory.append(absolute)
            relative = os.path.relpath(absolute, start=".")
            directory.append(relative)
            writer.writerow(directory)
            directory.clear()