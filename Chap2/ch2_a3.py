import numpy as np
import cv2

color = cv2.imread("butterfly.jpg", 1)

gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg", gray)

b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

# Using the gray values for the transperancy!
height,width,channels = color.shape
white = np.empty([height,width],'uint8')


rgba = cv2.merge((b,g,r,np.subtract(white, gray)))
cv2.imwrite("rgba.png", rgba)

