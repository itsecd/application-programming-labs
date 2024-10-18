import argparse

import cv2
import numpy as np
import OpenCV
import plt


def create_parser()->tuple:
    """
    Gets a path to original image and a path where image-result will be downloaded
    :return: Tuple of twp strings
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('original_image',type=str,help="the name of the original image")
    parser.add_argument('final_image',type=str,help="The name of the image-result")
    args = parser.parse_args()
    return args.original_image, args.final_image


def print_size(img:np.ndarray)->None:
    """
    Prints current size of the image and a number of channels
    :param img: image you need to find a size of
    """
    height, width, channels = img.shape
    print(f"Высота: {height}, ширина: {width}")


def main():
    img1, img2 = create_parser()

    try:
        image = cv2.imread(img1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        f_image = cv2.cvtColor(OpenCV.get_inverted_img(image),cv2.COLOR_RGB2BGR)
        OpenCV.save_inverted_img(f_image,img2)

        print_size(image)
        plt.show_graph(OpenCV.get_histogram(image))
        plt.show_images(image, f_image)
    except Exception as e:
        print(f"An error occurred while accessing the directory: {e} ")


if __name__=="__main__":
    main()