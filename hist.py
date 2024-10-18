import matplotlib.pyplot as plt

import cv2
from numpy import ndarray


def histogram_creation(img: ndarray)-> ndarray:
    """
    Функция создает гистограмму цветного изображения
    :param img:массив из пикселей(цветное изображение в формате rgb)
    :return:гистограмма по всем каналам,содержащая количество пикселей для каждого из 256 уровней яркости
    """
    hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])
    hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])
    hist=hist_r+hist_g+hist_b
    return hist


def histogram_drawing(histogram: ndarray) -> None:
    """
    Функция рисует гистограмму на основе переданного массива
    :param histogram:массив с количеством пикселей для каждого уровня яркости(0-255)
    :return: None
    """
    plt.figure(figsize=(10, 5))
    plt.plot(histogram)
    plt.xlim([0, 256])
    plt.title('Гистограмма изображения')
    plt.xlabel('Интенсивность пикселей')
    plt.ylabel('Количество пикселей')
    plt.show()