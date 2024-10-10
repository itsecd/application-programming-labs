import argparse

DEFAULT_DIR_PATH = "images"
DEFAULT_CSV_PATH = "annotation.csv"


def arg_parcer() -> tuple:
    """
    Parce args from command line
    :return: Class Object Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "object_on_photo",
        type=str,
        help="Object on images.")
    parser.add_argument(
                        "-d",
                        "--dirpath",
                        type=str,
                        default=DEFAULT_DIR_PATH,
                        help="Current PATH to directory where will be save images.")
    parser.add_argument(
                        "-c",
                        "--csvpath",
                        type=str,
                        default=DEFAULT_CSV_PATH,
                        help="Current PATH to csv file with PATHs to all images.")
    args_like_fields = parser.parse_args()
    args = (args_like_fields.object_on_photo, args_like_fields.dirpath, args_like_fields.csvpath)

    return args
