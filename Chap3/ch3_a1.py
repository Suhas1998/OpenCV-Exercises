import numpy as np
import cv2

bw = cv2.imread("sudoku.png",0);
height,width = bw.shape[0:2]

binary = np.zeros([height, width,1],'uint8')

cv2.imshow("Original BW", bw)

thresh = 85

for row in range(0,height):
  for col in range(0,width):
    if(bw[row][col] > 85):
      binary[row][col] = 255

cv2.imshow("Slow binary",binary)

ret, thresh = cv2.threshold(bw, thresh, 255, cv2.THRESH_BINARY)

cv2.imshow("CV2 binary",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
