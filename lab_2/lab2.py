import argparse
import image_crawler
import image_iterator

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="search keyword (image class)")
    parser.add_argument("save_dir", type=str, help="the path to the folder to save")
    args = parser.parse_args()
    return args.keyword, args.save_dir

if __name__ == "__main__":
    keyword, save_dir = parse()

    crawler = image_crawler.ImageCrawler(keyword, save_dir, 1000)
    crawler.download_images()
    annotation_file = crawler.create_annotation()

    iterator = image_iterator.ImageIterator(annotation_file)
    for image_path in iterator:
        print(image_path)
