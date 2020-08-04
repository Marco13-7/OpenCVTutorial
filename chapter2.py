import cv2
import numpy as np
print("Package Imported")

img = cv2.imread("Resources/GT3.jpg")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (3,3),0)
imgCanny = cv2. Canny(img , 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2.imshow("Output", imgEroded)
cv2.waitKey(0)


