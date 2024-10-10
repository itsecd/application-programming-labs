from icrawler.builtin import GoogleImageCrawler

base_dir = "images"
little_dir = "images"

def download_images(keyword: str, num: int, dir: str = little_dir) -> str:
    """
    Function for downloading images from Google using icrawler.

    Parameters:
    keyword (str): what are you search.
    num (int): number of photos you want download.
    dir (str): directory to save. Default: "images/images_{keyword}"

    Returns:
    str: path to directory where files save.
    """

    if dir.startswith( ("C:", ".") ):
        root_dir = dir
    else:
        root_dir = f"{base_dir}\\{dir}"
        if dir == little_dir: root_dir += f"_{keyword}"
        
    google_crawler = GoogleImageCrawler(
        storage={"root_dir": root_dir},
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4
    )

    google_crawler.crawl(keyword=keyword, max_num=num)

    return root_dir
