import cv2 as cv
import numpy as np

img = cv.imread('resources/photos/park.jpeg')
cv.imshow('Park', img)


def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)


# -x --> left
# -y --> up
# x --> right
# y --> down
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)


cv.waitKey(0)
