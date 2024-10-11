import os
import sys
from icrawler.builtin import BingImageCrawler


def download_image(dir_name: str,keyw: str,val: int) -> None:
    """
    Функция выполняет установку изображения с помощью BingImageCrawler, перед этим создает директорий(если необходимо) и очищает директорий(если необходимо)
    :param dir_name: директория, в которую мы сохраняем изображения
    :param keyw: ключевое слово
    :param val: кол-во изображений для скачивания
    :return: None
    """
    if not(os.path.isdir(dir_name)):
        os.mkdir(dir_name)
    for filename in os.listdir(dir_name):
        file_path = os.path.join(dir_name, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    try:
        google_crawler = BingImageCrawler(
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': dir_name,"backend": "FileSystem"})
        google_crawler.crawl(keyword=keyw, max_num=val)
        downloaded_images = len(os.listdir(dir_name))
        if downloaded_images < val:
            print(f"Загружено изображений: {downloaded_images}. Ожидалось: {val}.")
        else:
            print(f"Все {downloaded_images} изображений успешно загружены.")
    except Exception as e:
        print(f"Ошибочный путь к папке с изображениями: {e} ")