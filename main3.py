import cv2
import imutils
img=cv2.imread('a.jpeg')
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threImg=cv2.threshold(grayscale,120,255,cv2.THRESH_BINARY)[1]
cv2.imwrite('threImg.jpeg',threImg)