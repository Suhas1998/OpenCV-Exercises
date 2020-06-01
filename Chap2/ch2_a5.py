import numpy as np
import cv2

img = cv2.imread("messi5.jpg",1)
cv2.imshow("Original", img)

# Scaling
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img_stretch = cv2.resize(img, (400,400))

cv2.imshow("Half Image",img_half)
cv2.imshow("Stretched Image",img_stretch)

# Rotation
M = cv2.getRotationMatrix2D((0,0), -15,1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

