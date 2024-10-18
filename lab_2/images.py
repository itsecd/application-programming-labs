import os

from icrawler.builtin import GoogleImageCrawler

def download_images(keyword: str, maximum:int, directory: str) -> None:
    """
    The function creates a new directory if it doesn't exist and downloads images to this directory
    :param keyword: image type
    :param maximum: how many images need to be downloaded
    :param directory: path to download images
    :return: None
    """
    if not (os.path.isdir(directory)):
        os.mkdir(directory)

    google_crawler = GoogleImageCrawler(
        storage={'root_dir': directory},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4
    )
    google_crawler.crawl(keyword=keyword, max_num=maximum)