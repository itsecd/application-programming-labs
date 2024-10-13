import argparse
import cv2

from image import display, overlay_images, show_hist

PRFX = "[!]"
ERRMSG = PRFX + " " + "Some error: {e}" 

def _print_error(err_msg: str = "") -> None:
    """
    Print error text and exit programm.

    Parameters:
    err_msg (str): Error message.
    """
    print( ERRMSG.format(e=err_msg) )
    exit()

def _parse_arguments() -> list:
    """
    Function for get arguments from cli.

    Returns:
    list: List of arguments.
    """
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Programm gets 2 image files from stdout and transparency and adds these images using transparency.",
        epilog="o:" 
    )
    parser.add_argument("img_main", type=str, help="Main image.")
    parser.add_argument("img_overlay", type=str, help="Overlay image.")
    parser.add_argument("trn", type=int, help="TRaNsparency: value from 0 to 100.")
    parser.add_argument("-f", "--force", action="store_true", help="Force using resize \
                         overlay image if it size not match with main image.")
    parser.add_argument("-o", "--output", type=str, help="Saveing path")
    
    return parser.parse_args()


def main() -> None:
    args = _parse_arguments()
    
    try:
        img_main = cv2.imread(args.img_main)
        img_overlay = cv2.imread(args.img_overlay)
    except Exception as e:
        _print_error(e)

    if img_main is None or img_overlay is None:
        _print_error("Please check images paths.")

    for img, img_name in zip( (img_main, img_overlay), (args.img_main, args.img_overlay) ):
        print(f"{img_name} sizes: {img.shape}, {img.size}b")
        try:
            show_hist(img, img_name)
        except Exception as e:
            _print_error(e)

    try:
        result = overlay_images(img_main, img_overlay, args.trn, force=args.force)
    except ValueError as e:
        _print_error(e)
    
    display(result, f"[{args.img_main.split("\\")[-1]}] + {args.img_overlay.split("\\")[-1]}")

    if args.output:
        try:
            cv2.imwrite(args.output, result)
        except:
            _print_error("Enter correct path!")

        print(f"Saved to {args.output}")

if __name__ == "__main__":
    main()

