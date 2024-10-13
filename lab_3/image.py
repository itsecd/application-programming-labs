import cv2
from matplotlib import pyplot as plt
from numpy import ndarray

def display(img: ndarray, frame_name: str = "OpenCV Image") -> None:
    """
    Shows cv2's image.

    Parameters:
    img (ndarry): Input image.
    frame_name (str): Frame's name.
    """
    h, w = img.shape[0:2]

    new_h = 700
    new_w = int( new_h * (w / h) )

    img = cv2.resize( img, (new_w, new_h) )

    cv2.namedWindow(frame_name, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(frame_name, img)
    cv2.waitKey(0)

def get_hist(img: ndarray, channel: int) -> ndarray:
    """
    Returns hist for image for specify channel.

    Parameters:
    img (ndarry): Input image.
    channel (int): One channel of 0, 1, 2.

    Returns:
    ndarray: Output hist.
    """
    
    if channel > 2 or channel < 0:
        raise ValueError("Argument channel must be between 0 and 2 (includes)!")

    return cv2.calcHist([img], [channel], None, [256], [0, 256])


def show_hist(img: ndarray, hist_name: str = "Image") -> None:
    """
    Show hist for image 'img' using matplotlib.

    Parameters:
    img (ndarray): Input image.
    """
    colors = ("blue", "green", "red", "black")
    legend = (*map(lambda s: s.capitalize() + " channel", colors[:-1]), "Summary")

    hist = None
    for channel, color in zip( (0, 1, 2), colors[:-1] ):
        current_hist = get_hist(img, channel)
        if hist is None:
            hist = current_hist
        else:
            hist += current_hist
        plt.plot(current_hist, color=color)

    plt.plot(hist, color=colors[-1])
    plt.ylabel("Pixels count")
    plt.xlabel("Pixels range")

    plt.legend(legend)

    plt.title(f"{hist_name} Histogram")
    plt.show()


def overlay_images(img_main: ndarray, img_overlay: ndarray, trn: int, force: bool = True) -> ndarray:
    """
    Overlay 2 images.

    Parameters:
    img_main (ndarray): Main image.
    img_overlay (ndarray): Overlay image.
    trn (ing): Transparency value in percentage between 0 and 100.
    force (bool): Force resize img_overlay if it size don't match.

    Returns:
    ndarray: Result added image.
    """
    if trn > 100 or trn < 0:
        raise ValueError("Percentage must be between 0 and 100!")

    trn_result = 1 - trn / 100

    if not force and (img_main.shape[:2] != img_overlay.shape[:2]):
        raise ValueError(f"Sizes don't match: {img_main.shape[:2]} and {img_overlay.shape[:2]}")
    elif force:
        img_overlay = cv2.resize(img_overlay, (img_main.shape[1], img_main.shape[0]))
        
    img_result = cv2.addWeighted(img_main, 1 - trn_result, img_overlay, trn_result, 0)

    return img_result
