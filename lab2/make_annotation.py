import csv
import os

def make_annotation(path_to_folder: str, path_to_annotation: str) -> None:
    """
    Func is making annotation with current and global PATHs images
    :param path_to_folder: PATH to folder where images saved
    :param path_to_annotation: PATH to csv file
    :return: None
    """
    list_images = os.listdir(path_to_folder)
    data_to_annotation = []
    for i in range(len(list_images)):
        current_dir = os.path.dirname(os.path.abspath(list_images[i]))
        absolute_path = os.path.join(current_dir, path_to_folder, list_images[i])
        current_path = os.path.join(path_to_folder, list_images[i])
        data_element = [str(i), current_path, absolute_path]
        data_to_annotation.append(data_element)

    if os.path.exists(path_to_annotation):
        os.remove(path_to_annotation)

    with open(path_to_annotation, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_to_annotation)  # запись всех строк