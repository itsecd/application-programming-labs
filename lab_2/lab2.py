import argparse
from icrawler.builtin import BingImageCrawler

parser = argparse.ArgumentParser()
parser.add_argument("keyword", type=str, help="search keyword (image class)")
parser.add_argument("path", type=str, help="the path to the folder to save")
args = parser.parse_args()

google_crawler = BingImageCrawler(storage={"root_dir" : args.path})
google_crawler.crawl(keyword=args.keyword, max_num=1000)
