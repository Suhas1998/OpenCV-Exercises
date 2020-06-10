import numpy as np
import cv2

img = cv2.imread("sudoku.png",0)

height,width = img.shape[0:2]

cv2.imshow("Original", img)

# ret, thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
# cv2.imshow("Basic Threshold", thresh_basic)

thresh_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 65, 1)
cv2.imshow("Adaptive Threshold", thresh_adapt1)


kernel = np.ones((3,3), 'uint8')

dilate = cv2.dilate(thresh_adapt,kernel,iterations = 1)


cv2.imshow("Diluted", dilate1)


cv2.waitKey(0)
cv2.destroyAllWindows()


