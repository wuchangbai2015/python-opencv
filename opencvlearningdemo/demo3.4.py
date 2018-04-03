import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



