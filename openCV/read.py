from turtle import color
import cv2 as cv
import numpy as np
videoCapture = cv.VideoCapture('videos/bolt_test_pothole.mp4')
prevCircle = None
def dist(x1, y1, x2, y2): return (x1-x2)**2 + (y1-y2)**2


while True:
    ret, frame = videoCapture.read()
    if not ret:
        break
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(grayFrame, (17, 17), 0)
    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT,
                              1.2, 1000, param1=100, param2=26, minRadius=25, maxRadius=100)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for (x, y, r) in circles[0, :]:
            cv.circle(frame, (x, y), 1, (0, 100, 100), 3)
            cv.circle(frame, (x, y),
                      r, (0, 100, 100), 3)
    cv.imshow("circles", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv.destroyAllWindows()
