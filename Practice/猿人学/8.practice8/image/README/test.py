import cv2 as cv


img = cv.imread("./test.png",0)

cv.imshow("haha", img)
k = cv.waitKey(0)