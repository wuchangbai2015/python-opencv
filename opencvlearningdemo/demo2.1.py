import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while cap.isOpened():
	#capture frame-by-frame
	ret , img = cap.read()
	img = cv2.flip(img, 1)
	#our operation on the frame come here
	gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
	#display the resulting frame
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF ==ord('q'): #按q键退出
		break
#when everything done , release the capture
cap.release()
cv2.destroyAllWindows()

