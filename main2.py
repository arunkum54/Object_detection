import cv2
import imutils
img=cv2.imread('a.jpeg')
gaussianBlur=cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gaussian.jpeg",gaussianBlur)
