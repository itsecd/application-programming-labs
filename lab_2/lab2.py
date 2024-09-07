import argparse
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler, FlickrImageCrawler

parser = argparse.ArgumentParser()
parser.add_argument("keyword", type=str, help="search keyword (image class)")
parser.add_argument("path", type=str, help="the path to the folder to save")
args = parser.parse_args()
path = args.path
keyword = args.keyword

google_crawler = GoogleImageCrawler(storage={"root_dir" : path})
google_crawler.crawl(keyword=keyword, max_num=1000)

bing_crawler = BingImageCrawler(storage={"root_dir" : path})
bing_crawler.crawl(keyword=keyword, max_num=1000)
