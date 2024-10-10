import argparse
from tqdm import tqdm
from time import sleep

from dir2csv import dir2csv, default_name
from images import download_images, little_dir
from imgiterator import ImgIterator

def _parse_arguments() -> list:
    """
    Parse arguments from stdin in execution moment.

    Returns:
    list: list of the aruments
    """
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Download target images",
        epilog="o:" 
    )
    parser.add_argument("keyword", type=str, help="What do you want search.")
    parser.add_argument("-c", "--csv", type=str, default=default_name, help="Path to csv file.")
    parser.add_argument("-d" ,"--dir", type=str, default=little_dir, help="Path to end directory where images store.")
    parser.add_argument("-n", "--number", type=int, default=50, help="Number of downloading files.")
    
    return parser.parse_args()

def main():
    args = _parse_arguments()

    try:
        root_dir = download_images(args.keyword, args.number, dir=args.dir)
        result_path = dir2csv(root_dir, csv_path=args.csv)
    except Exception as e:
        print(f"Something strange: {e}")
        exit()

    img_iterator = ImgIterator(result_path)

    print(f"Rel. and abs. pathes for images with \"{args.keyword}\":")
    
    with tqdm(range(args.number), desc="Total") as pbar:
        for rel_path, abs_path in img_iterator:
            sleep(0.15)

            pbar.write(rel_path + " " + abs_path)
            pbar.update(1)
    

if __name__ == "__main__":
    main()
