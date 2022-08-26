import cv2 as cv
import numpy as np

blank = np.zeros((500, 500), dtype='uint8')
cv.imshow('Blank', blank)

img = cv.imread('resources/photos/cat.jpeg')
cv.imshow('Cat', img)

k = cv.waitKey(0)

if k == ord('s'):
    print('hello world')

