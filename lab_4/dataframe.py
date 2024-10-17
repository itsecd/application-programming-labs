from cv2 import imread
from matplotlib import pyplot as plt
import pandas as pd

def init_df(filename: str) -> pd.DataFrame:
    """
    Initializes a DataFrame from a csv file.
    Columns abberviation used:
    RP - Relative Path
    AP - Absolete Path
    H - Height
    W - Width
    CH - CHannel
    S - Size (== area)

    Parameters:
    filename (str): path to file.

    Returns:
    pd.DataFrame: pandas DataFrame object.
    """
    LABELS = ("RP", "AP", "H", "W", "CH", "S")

    df = pd.read_csv(filename, names=list(LABELS))

    for idx in range( len(df) ):
        path = df.at[idx, "AP"]
        img = imread(path)
        sizes = None

        if img is None:
            df.drop(index=idx, inplace=True)
            continue

        sizes = img.shape + (img.shape[0] * img.shape[1], )
        df.loc[idx, LABELS[2:]] = sizes
    
    return df.reset_index(drop=True)


def filter_df(df: pd.DataFrame, max_height: float, max_width: float) -> pd.DataFrame:
    """
    Filters DataFrame.

    Parameters:
    df (pd.DataFrame): pandas DataFrame object.
    max_height (float): maximum height.
    max_width (float): maximum width.

    Returns:
    pd.DataFrame: pandas DataFrame object.
    """
    return df[(df.H <= max_height) & (df.W <= max_width)]

def show_s_dist(df: pd.DataFrame) -> None:
    """
    Show size distribution graph using matplotlib.

    Parameters:
    df (pd.DataFrame): pandas DataFrame object.
    """
    df.hist(column="S")

    plt.xlabel("Pixels")
    plt.ylabel("Count")
    plt.title("Area Distribution Graph")
    plt.show()
