import cv2
import numpy as np
img1=cv2.imread('demo1.jpg')
img2=cv2.imread('demo2.jpg')
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
#cv2.imshow('demo1',demo1)
#cv2.imshow('demo2',demo2)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()