import cv2
import matplotlib.pyplot as plt

from numpy import ndarray


def dimensioning(path_image:str) -> None:
    """
    Функция вывода высоты и ширины изображения
    :param path_image: путь к изображению
    :return: None
    """
    img = cv2.imread(path_image)
    height, width, channels=img.shape
    print(f"Высота изображения: {height}, Ширина изображения: {width}")


def grayscale_image(image: ndarray)->ndarray:
    """
    Функция преобразования цветного изображения в полутоновое
    :param image:массив с цветными пикселями(изображение)
    :return:новый массив с пикселями серого цвета
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def save_grayscale_image(gr_im: ndarray,path_gr_im: str)->None:
    """
    Функция сохранения нового изображения
    :param gr_im: полутоновое изображение
    :param path_gr_im:путь для создания нового изображения
    :return: None
    """
    cv2.imwrite(path_gr_im, gr_im)


def image_output(image: ndarray,gr_image: ndarray)->None:
    """
    Функция вывода исходного изображения и измененного
    :param image: массив с цветными пикселями(изображение)
    :param gr_image: массив с серыми пикселями(полутоновое изображение)
    :return: None
    """
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title('Исходное изображение')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(gr_image)
    plt.title('Обработанное изображение')
    plt.axis('off')
    plt.tight_layout()
    plt.show()