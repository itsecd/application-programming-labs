import matplotlib.pyplot as plt
import numpy as np


def show_graph(hist: np.ndarray)->None:
    """
    Builds a graph of histogram, that was found in get_histogram()
    :param hist: histogram of the image
    """
    plt.plot(hist)
    plt.title('Image histogram')
    plt.xlabel('brightness')
    plt.ylabel('number of pixels')
    plt.show()


def show_images(img:np.ndarray, f_img:np.ndarray)->None:
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