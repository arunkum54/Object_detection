import cv2
import imutils
img=cv2.imread('a.jpeg')
resize=imutils.resize(img,width=20)
cv2.imwrite('resize.jpeg',resize)
