import numpy as np
import cv2

img = cv2.imread('demo1.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xff

if k==27: 
	cv2.destroyAllWindows() # wait for ESC key to exit
elif k == ord('s'):
	cv2.imwrite('demo1.1.png',img) # wait for 's' key to save and exit

cv2.destoryAllWindows()

