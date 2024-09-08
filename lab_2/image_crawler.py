from icrawler.builtin import GoogleImageCrawler
import os
import csv

class ImageCrawler:
    def __init__(self, keyword, save_dir, num_images):
        self.keyword = keyword
        self.save_dir = save_dir
        self.num_images = num_images
        self.crawler = GoogleImageCrawler(
            storage={"root_dir" : save_dir},
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4
        )

    def download_images(self):
        self.crawler.crawl(keyword=self.keyword, max_num=self.num_images)

    def create_annotation(self):
        images = sorted(os.listdir(self.save_dir))
        with open("annotation.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Absolute path", "Relative path"])
            for image in images:
                abs_path = os.path.abspath(os.path.join(self.save_dir, image))
                rel_path = os.path.join(self.save_dir, image)
                writer.writerow([abs_path, rel_path])
            return file.name