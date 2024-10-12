from annotation import annotation_creation
from value_input import value_input
from download import download_image
from iterator import ImageIterator


def main() -> None:
    try:
        args = value_input()
        download_image(args.dir_name, args.keyw, args.value)
        annotation_creation(args.dir_name, args.annotation_file)
        iterator = ImageIterator(args.annotation_file)
        for img in iterator:
            print(img)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    main()
