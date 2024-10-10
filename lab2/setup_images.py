from icrawler.builtin import GoogleImageCrawler
import os
import shutil

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