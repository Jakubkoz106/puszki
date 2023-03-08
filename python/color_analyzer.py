import cv2
import numpy as np
import os
import shutil

def color_analyzer(file_name):
    img = cv2.imread(str(file_name))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    area_all_value = img.shape[0] * img.shape[1]

    #kolory
    colors_range = {"black": [np.array([0, 0, 0]), np.array([180, 255, 60])],
                    "yellow": [np.array([25, 80 ,20]), np.array([35,255,255])],
                    "green": [np.array([40, 80 ,20]), np.array([70,255,255])],
                    "blue": [np.array([80, 80, 20]), np.array([135, 255, 255])],
                    "purple": [np.array([140, 80, 20]), np.array([155, 255, 255])],
                    "pink": [np.array([155, 80, 20]), np.array([170, 255, 255])],
                    "red": [np.array([173, 80, 20]), np.array([180,255,255])],
                    "white": [np.array([0, 0, 195]), np.array([180, 60, 255])]}

    colors_percent = {}

    for color in colors_range.items():
        mask = cv2.inRange(hsv, color[1][0], color[1][1])
        area = cv2.countNonZero(mask)
        colors_percent[color[0]] = (area/area_all_value)*100
        #cv2.imshow("image", cv2.resize(mask, (960, 540)))
        #cv2.waitKey(0)

    print(file_name + " " + str(colors_percent))

    return colors_percent


def for_each_jpg(path):
    file_paths = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if name.endswith(".jpg"):
                file_paths.append(os.path.join(root, name))

    return file_paths


def create_color_dirs(path, color_names):
    for color_name in color_names:
        dir_path = os.path.join(path, color_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)



if __name__ == "__main__":
    try:
        path_to_dir_with_photos = "..\\zdjeciaWyniki"
        file_paths = for_each_jpg(path_to_dir_with_photos)

        data = []
        for path in file_paths:
            data.append([path, color_analyzer(path)])

        path_to_dst_dir = "..\\posortowane_wzgledem_kolorow"
        if not os.path.exists(path_to_dst_dir):
            os.mkdir(path_to_dst_dir)

        create_color_dirs(path_to_dst_dir, data[0][1])

        for i in range(0, len(data)):
            for color in data[i][1]:
                if data[i][1][color] > 30:
                    dst_path = os.path.join(path_to_dst_dir, color, os.path.basename(data[i][0]))
                    if not os.path.exists(dst_path):
                        shutil.copy(data[i][0], dst_path)


    except Exception as err:
        print(err)

    else:
        print("The program ran without exceptions!")

    finally:
        print("The program ended correctly!")


class MyError(Exception):
    def __init__(self, p1):
        self.parametr1 = p1

    def __str__(self):
        return "Exception: " + self.parametr1
