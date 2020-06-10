import numpy as np
import cv2

img = cv2.imread("face_grid.png", 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h= hsv[:,:,0]
s= hsv[:,:,1]
v= hsv[:,:,2]

hsv_split = np.concatenate((h,s,v), axis = 1)
cv2.imshow("HSV Channels", hsv_split)

ret, min_sat = cv2.threshold(s,40,255,cv2.THRESH_BINARY)
cv2.imshow("Sat Filter", min_sat)

ret, max_hue = cv2.threshold(h,15,255,cv2.THRESH_BINARY_INV)
cv2.imshow("HUE Filter", max_hue)

finalAnd = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("Final And",finalAnd)

finalOr = cv2.bitwise_or(min_sat, max_hue)
cv2.imshow("Final Or",finalOr)

cv2.imshow("Original", img)

cv2.waitKey(0);
cv2.destroyAllWindows()
