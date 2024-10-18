import argparse
from download_image import download_images
import ImageIterator
from make_csv import create_csvfile


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
