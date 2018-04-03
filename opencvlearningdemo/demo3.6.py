import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

