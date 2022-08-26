import cv2 as cv

img = cv.imread('resources/photos/cat.jpeg')
cv.imshow('Cat', img)


# resize
resized = cv.resize(img, (500, 500))
cv.imshow('Resized', resized)

cv.waitKey(0)
