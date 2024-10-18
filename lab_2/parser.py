import argparse

def get_arguments() -> argparse.Namespace:
    """
    The function parses arguments from terminal
    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('keyword', type=str, help='what kind of images you want to download')
    parser.add_argument('-d', '--dir', type=str, help='path to dir')
    parser.add_argument('-f', '--file', type=str, help='path to annotation file')
    parser.add_argument('-n', '--num', type=int, help='how many images do you want to download')

    args = parser.parse_args()

    return args