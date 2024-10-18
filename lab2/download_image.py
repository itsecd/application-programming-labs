from icrawler.builtin import BingImageCrawler


def download_images(dir_name: str, request: str, maximum: int) -> None:
    """
    Downloading images with using icrawler
    :param dir_name: name of directory to save pictures
    :param request: keyword for search
    :param maximum: desired count of pictures
    :return:
    """
    google_crawler = BingImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': dir_name})

    google_crawler.crawl(keyword=request, max_num=maximum)
