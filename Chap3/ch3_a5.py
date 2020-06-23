import numpy as np
import cv2

img = cv2.imread("tomato2.jpg",1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
res, thresh = cv2.threshold(hsv[:,:,0], 25, 255, cv2.THRESH_BINARY_INV)
# Hue value threshold of range 0 to 25 which is range of Red!

cv2.imshow("THRESH", thresh)


edges = cv2.Canny(img,100,70)
cv2.imshow("Canny",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
