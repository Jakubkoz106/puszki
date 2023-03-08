from PIL import Image
import pytesseract
import os
import cv2
import numpy as np




# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 1)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 180, 360)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  #sciezka do tesseract


path1 = '../zdjeciaWyniki'
myListZdjecia = os.listdir(path1)
for path in myListZdjecia:
    img = cv2.imread(path1+"/"+path)


    img = get_grayscale(img)    # paramtery do komentowania lub nie czasem lepiej czyta bez ich uzycia lub odwrotnie

    img = thresholding(img)    # paramtery do komentowania lub nie czasem lepiej czyta bez ich uzycia lub odwrotnie



    with open("../tekstWyniki/"+path.split("/")[-1][0:-3]+"txt", 'w',encoding="utf-8") as f:
        e = pytesseract.image_to_string(img, lang='pol')
        print(e)
        #f.write(e)
        f.write("\n ------------------------------------- \n")
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        f.write(pytesseract.image_to_string(img, lang='pol'))


