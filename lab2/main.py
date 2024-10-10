
from arg_parser import arg_parcer
from imgiterator import ImgIterator
from make_annotation import make_annotation
from setup_images import setup_images


COUNT = 1000


def main() -> int:
    args = arg_parcer()
    data = ''
    try:
        setup_images(args[0], args[1], COUNT)
        make_annotation(args[1], args[2])
    except Exception:
        print("Wrong directory's PATH or csv file")

    myy = ImgIterator(args[2])
    for item in myy:
        print(item)

    return 0


if "__main__" == __name__:
    main()
