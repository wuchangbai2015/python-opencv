import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
cv2.rectangle(img,(350,0),(500,128),(0,255,0),3)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)#定义frame的大小
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()






