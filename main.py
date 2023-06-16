import cv2
img=cv2.imread('a.jpeg')
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayImg.jpeg",grayImg)
cv2.imshow("Original",img)
cv2.imshow("GrayIamge",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()