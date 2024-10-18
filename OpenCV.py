import cv2
import numpy as np


def get_histogram(img:np.ndarray)->np.ndarray:
    """
    Gets a histogram of the picture
    :param img: image whose histogram you need to find
    :return: histogram of the image
    """
    hist = cv2.calcHist(img,[0],None,[256],[0,256])
    return hist


def get_inverted_img(img:np.ndarray)->np.ndarray:
    """
    Inverts the colors of the specified image
    :param img: the image whose colors need to be inverted
    :return: image-result
    """
    return cv2.bitwise_not(img)


def save_inverted_img(img:np.ndarray, f_img:str)->None:
    """
    Saves the image-result to directory f_img
    :param img: image
    :param f_img: save-directory
    """
    cv2.imwrite(f_img,img)


