import cv2 as cv

img = cv.imread('resources/photos/park.jpeg')
cv.imshow('park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HCV', hsv)

cv.waitKey(0)
