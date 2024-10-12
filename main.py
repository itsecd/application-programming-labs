import argparse

from downloader import download_images
from imgiterator import ImageIterator
from mk_annotation import create_annotation


def get_args() -> tuple[str, int, str, str]:
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
    return arguments.keyword, arguments.number, arguments.imgdir, arguments.annotation_file


def main() -> None:
    keyword, number, imgdir, annotation_file = get_args()
    try:
        download_images(keyword, number, imgdir)
        create_annotation(imgdir,annotation_file)
        my_iterator = ImageIterator(annotation_file)
        for item in my_iterator:
            print(item)
    except Exception as e:
        print(f"Something went wrong: {e} ")
if __name__ == "__main__":
    main()
