from icrawler.builtin import GoogleImageCrawler
import os
import csv


class ImageCrawler:
    """
    A class for creating a crawler object.
    """
    def __init__(self, keyword: str, save_dir: str, num_images: int) -> None:
        """
        Sets all necessary attributes for the ImageCrawler object.

        :param keyword: The word to be searched for
        :param save_dir: The directory where the images will be saved
        :param num_images: Maximum number of images to download
        """
        self.keyword = keyword
        self.save_dir = save_dir
        self.num_images = num_images
        self.crawler = GoogleImageCrawler(
            storage={"root_dir": save_dir},
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4
        )

    def download_images(self) -> None:
        """
        Downloads images based on a given keyword.
        """
        self.crawler.crawl(keyword=self.keyword, max_num=self.num_images)

    def create_annotation(self) -> str:
        """
        Creates a csv annotation for downloaded files.

        :return: The name of the file with the annotation
        """
        images = sorted(os.listdir(self.save_dir))
        with open("annotation.csv",
                  mode="w",
                  newline="",
                  encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Absolute path", "Relative path"])
            for image in images:
                abs_path = os.path.abspath(os.path.join(self.save_dir, image))
                rel_path = os.path.join(self.save_dir, image)
                writer.writerow([abs_path, rel_path])
            return file.name
