import cv2 as cv

img = cv.imread('Photos/cat.jpg')

def rescaleFrame(frame, scale=0.75):
    # images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    #live videos
    capture.set(3,width)
    capture.set(4,height)

# Reading videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    resized_frame = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video resized', resized_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


resized_image = rescaleFrame(img)

cv.imshow('Image', img)

cv.imshow('Resized image', resized_image)

cv.waitKey(0)