import argparse
import ImageCrawler
import ImageIterator


def create_parser():
    """
        User enters the word for which the ImageCrawler will be played
        and the name of the file where images will be downloaded
        :return: the keyword and the name of the file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str,help="What do you want to search")
    parser.add_argument('save_dir',type=str,help="Where to download the images")
    args = parser.parse_args()
    return args.keyword, args.save_dir

def main():
    create_parser()
    keyword, save_dir = create_parser()

    ImageCrawler.clear_dir(save_dir)
    ImageCrawler.get_images(keyword, save_dir)
    ImageCrawler.annotation(ImageCrawler.get_files(save_dir),save_dir)

    my_iter = ImageIterator.Iterator('data.csv')
    for item in my_iter:
        print(item)


if __name__ == "__main__":
    main()


