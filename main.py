from image import *
from input import value_input
from hist import *


def main():
    path_im=value_input().path_image
    path_new_im=value_input().path_new_image
    try:
        img = cv2.imread(path_im)
        dimensioning(path_im)
        histogram_drawing(histogram_creation(img))
        new_im=grayscale_image(img)
        save_grayscale_image(new_im, path_new_im)
        image_output(img,new_im)
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()