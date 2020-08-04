import cv2
import numpy as np

img = cv2.imread("Resources/GT3.jpg")
print(img.shape)

imgResize = cv2.resize(img,(1000, 500))
print(imgResize.shape)

imgCropped = img[200:700,200:500]
cv2.imshow("Output", imgCropped)
cv2.waitKey(0)