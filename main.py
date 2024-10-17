import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np


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


def get_size(img:np.ndarray)->None:
    """
    Prints current size of the image and a number of channels
    :param img: image you need to find a size of
    """
    height, width, channels = img.shape
    print(f"Высота: {height}, ширина: {width}")


def get_histogram(img:np.ndarray)->np.ndarray:
    """
    Gets a histogram of the picture
    :param img: image whose histogram you need to find
    :return: histogram of the image
    """
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist(img_gray,[0],None,[256],[0,256])
    return hist


def get_graph(hist: np.ndarray)->None:
    """
    Builds a graph of histogram, that was found in get_histogram()
    :param hist: histogram of the image
    """
    plt.plot(hist)
    plt.title('Image histogram')
    plt.xlabel('brightness')
    plt.ylabel('number of pixels')
    plt.show()


def get_inverted_img(img:np.ndarray, f_img:np.ndarray)->np.ndarray:
    """
    Inverts the colors of the specified image
    :param img: the image whose colors need to be inverted
    :param f_img: the path where inverted image will be downloaded
    :return: inverted image
    """
    cv2.imwrite(str(f_img),cv2.bitwise_not(img))
    return cv2.bitwise_not(img)


def get_images(img:np.ndarray, f_img:np.ndarray)->None:
    """
    Displays the two pictures: originals and with inverted colors
    :param img: original image
    :param f_img: inverted image
    """
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Original Image")
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.title("Inverted Image")
    plt.imshow(f_img)
    plt.axis('off')

    plt.show()




def main():
    img1, img2 = create_parser()

    try:
        image = cv2.imread(img1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        f_image = cv2.cvtColor(get_inverted_img(image,img2),cv2.COLOR_RGB2BGR)

        get_size(image)
        get_graph(get_histogram(image))
        get_images(image, f_image)
    except Exception as e:
        print(f"An error occurred while accessing the directory: {e} ")


if __name__=="__main__":
    main()