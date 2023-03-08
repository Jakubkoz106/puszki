import os
import numpy as np
import cv2


def minHeight(path):
    myList = os.listdir(path)
    img = cv2.imread(f'{path}/{myList[0]}')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 100, 200)  # 0,025     dostosowac do tego

    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.morphologyEx(edges, cv2.MORPH_DILATE, kernel)

    img = cv2.resize(edges, (960, 540))
    #cv2.imshow('image', img)
    #cv2.waitKey(0)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    y = []
    for i in range(len(contours) - 1):
        for x in range(len(contours[i]) - 1):
            y.append(contours[i][x][0][1])
    return np.amin(y)


