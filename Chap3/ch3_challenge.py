import numpy as np
import cv2
import random


img = cv2.imread("fuzzy.png", 1)
cv2.imshow("Original image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)

ret, thresh = cv2.threshold(blur,150,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5), 'uint8')
dilated = cv2.dilate(thresh, kernel, iterations =1 )
eroded = cv2.erode(dilated,kernel,iterations = 5)
cv2.imshow("Binary", eroded)

contours, hierarchy = cv2.findContours(eroded,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

filtered = []
for c in contours:
  if cv2.contourArea(c) < 1000: continue;
  filtered.append(c)

print(len(contours))

objects = np.zeros([img.shape[0],img.shape[1],3], 'uint8')

for c in filtered:
  col = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
  cv2.drawContours(objects, [c], -1, col, -1 )

  area = cv2.contourArea(c)
  perimeter = cv2.arcLength(c, True)

  print("Area: {}, Perimeter: {}".format(area,perimeter))

cv2.imshow("Final Image", objects)



cv2.waitKey(0)
cv2.destroyAllWindows(0)
