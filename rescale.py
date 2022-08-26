import cv2 as cv


# img = cv.imread('resources/photos/cat_large.jpeg')
# cv.imshow('Cat', img)


def rescale_frame(frame, scale=0.75):
    """For Images, Videos and live videos"""
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_res(width, height):
    """Live video"""
    capture.set(3, width)
    capture.set(4, height)


# reading videos
capture = cv.VideoCapture('resources/videos/dog.mp4')

while True:
    is_true, frame = capture.read()

    frame_resized = rescale_frame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()