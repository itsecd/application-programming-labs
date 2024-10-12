import argparse

import ImageCrawler
import ImageIterator


def create_parser()->tuple:
    """
        User enters the word for which the ImageCrawler will be played
        and the name of the file where images will be downloaded
        :return: the keyword and the name of the file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str,help="What do you want to search")
    parser.add_argument('save_dir',type=str,help="Where to download the images")
    parser.add_argument('csv_file',type=str,help="The name of annotation file")
    args = parser.parse_args()
    return args.keyword, args.save_dir, args.csv_file


def main():
    create_parser()
    keyword, save_dir, csv_file = create_parser()

    try:
        ImageCrawler.clear_dir(save_dir)
        ImageCrawler.get_images(keyword, save_dir)
        ImageCrawler.annotation(ImageCrawler.get_files(save_dir),save_dir, csv_file)

        my_iter = ImageIterator.Iterator(csv_file)
        for item in my_iter:
            print(item)
    except Exception as e:
        print(f"An error occurred while accessing the directory: {e} ")


if __name__ == "__main__":
    main()


