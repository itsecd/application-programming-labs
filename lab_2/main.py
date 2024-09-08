from tqdm import tqdm
from time import sleep
import argparse

from images import download_images
from dir2csv import dir2csv
from imgiterator import ImgIterator

error_text = "[{func_name}] Error: {err_txt}"
count_images = 50

def _parse_arguments():
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Download target images",
        epilog="o:" 
    )
    parser.add_argument("keyword", type=str, help="What do you want search.")
    parser.add_argument("dir", type=str, help="Path to end directory.")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = _parse_arguments()

    try:
        root_dir = download_images(args.keyword, count_images, dir=args.dir)
    except Exception as e:
        print(error_text.format(func_name="download_images", err_txt=e.text))
        exit()

    try:
        dir2csv(root_dir, csv_name=args.keyword)
    except Exception as e:
        print(error_text.format(func_name="dir2csv", err_txt=e.text))
        exit()

    img_iterator = ImgIterator(args.keyword)

    print(f"Rel. and abs. pathes for images with \"{args.keyword}\":")
    
    with tqdm(range(count_images), desc="Total") as pbar:
        for rel_path, abs_path in img_iterator:
            sleep(0.15)

            pbar.write(rel_path + " " + abs_path)
            pbar.update(1)

    