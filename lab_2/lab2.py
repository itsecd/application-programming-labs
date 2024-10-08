import argparse

import image_crawler
import image_iterator


def parse() -> tuple[str, str, str]:
    """
    Parses the search keyword, the name of the directory
    where the downloaded images will be saved and the name of the annotation.

    :return: A list containing the keyword, the name of the directory and the name of the annotation
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "keyword",
        type=str,
        help="search keyword (image class)"
    )
    parser.add_argument(
        "save_dir",
        type=str,
        help="the path to the folder to save"
    )
    parser.add_argument(
        "annotation_file",
        type=str,
        help="the path to the annotation"
    )
    args = parser.parse_args()
    return args.keyword, args.save_dir, args.annotation_file


def main() -> None:
    """
    The main program.
    """
    keyword, save_dir, annotation_file = parse()

    crawler = image_crawler.ImageCrawler(keyword, save_dir, 1000)
    crawler.download_images()
    annotation_file = crawler.create_annotation(annotation_file)

    iterator = image_iterator.ImageIterator(annotation_file)
    for image_path in iterator:
        print(image_path)


if __name__ == "__main__":
    main()
