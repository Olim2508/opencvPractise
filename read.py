import cv2 as cv

# img = cv.imread('resources/photos/cat.jpeg')
#
# cv.imshow('Cat', img)
#
# cv.waitKey(0)


# Reading videos
capture = cv.VideoCapture('resources/videos/dog.mp4')

while True:
    is_true, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
