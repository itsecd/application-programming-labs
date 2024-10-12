import os

from icrawler.builtin import BingImageCrawler


def download_images(keyword: str, number: int, imgdir: str) -> None:
    """
    This function downloads images from Bing using given keyword and directory. Also, it clears the directory every time you launch script.
    :param keyword: Search keyword
    :param number: Number of images that you want to download
    :param imgdir: Directory to save images
    """
    if not(os.path.isdir(imgdir)):
        os.mkdir(imgdir)
    for filename in os.listdir(imgdir):
        os.remove(os.path.join(imgdir, filename))
    my_crawler = BingImageCrawler(
    storage={"root_dir": imgdir, "backend": "FileSystem"},
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=4)
    my_crawler.crawl(keyword=keyword, max_num=number)
