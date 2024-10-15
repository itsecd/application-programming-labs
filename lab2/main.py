from icrawler.builtin import BingImageCrawler
import os.path as op
import os
import csv
import argparse
import ImageIterator


def get_input_info() -> tuple:
    """
    Parsing the arguments of command line
    :return: tuple of name od directory, request, name of annotation file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('name_dir', type=str, help='name dir')
    parser.add_argument('request', type=str, help='request')
    parser.add_argument('annotation_file', type=str, help='annotation_file')
    args = parser.parse_args()
    dir_name, request, annotation_file = args.name_dir, args.request, args.annotation_file
    return dir_name, request, annotation_file


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


def create_csvfile(dir_name: str, annotation_file: str) -> None:
    """
    Creating csv-file with annotation
    :param dir_name: name of directory with pictures
    :param annotation_file: name of file to save annotation
    :return:
    """
    with open(annotation_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Absolute path", "relative path"])
        list_of_pictures = os.listdir(dir_name)
        for i in list_of_pictures:
            a = op.abspath(op.join(dir_name, i))
            r = op.relpath(op.join(dir_name, i), start=".")
            writer.writerow([a, r])


def main():
    try:
        dir_name, request, annotation_file = get_input_info()
        download_images(dir_name, request, 1000)
        create_csvfile(dir_name, annotation_file)
        iterator = ImageIterator.ImageIterator(annotation_file)
        for i in iterator:
            print(i)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
