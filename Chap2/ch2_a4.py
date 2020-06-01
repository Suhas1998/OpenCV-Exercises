import numpy as np
import cv2

image = cv2.imread("thrash.png")
cv2.imshow("Original", image)

blur = cv2.GaussianBlur(image,(3,3),0)
cv2.imshow("Blurred", blur)


kernel = np.ones((3,3), 'uint8')

dilate = cv2.dilate(image,kernel,iterations = 1)
erosion = cv2.erode(image,kernel,iterations = 1)

cv2.imshow("Diluted", dilate)
cv2.imshow("erosion", erosion)


cv2.waitKey(0)
cv2.destroyAllWindows()
