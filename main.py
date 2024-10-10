import argparse
import os

from downloader import download_images
from imgiterator import ImageIterator
from mk_annotation import create_annotation


def get_args() -> argparse.Namespace:
    """
    Reads arguments from terminal
    :return: Arguments

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="Keyword of search request")
    parser.add_argument("-n", "--number", type=int, help="Number of images that you want to download")
    parser.add_argument("-d", "--imgdir", type=str, help="Path to the folder, where you want to save images")
    parser.add_argument("-f", "--annotation_file", type=str, help="Path to the annotation file")
    arguments = parser.parse_args()
    return arguments


def main() -> None:
    args = get_args()
    try:
        download_images(args.keyword, args.number, args.imgdir)
        create_annotation(args.imgdir,args.annotation_file)
        my_iterator = ImageIterator(args.annotation_file)
    except Exception as e:
        print(f"Something went wrong: {e} ")
    for item in my_iterator:
        print(item)
if __name__ == "__main__":
    main()
