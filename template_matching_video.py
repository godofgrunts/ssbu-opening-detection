import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
template = cv2.imread('template.png',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
meth = 'cv2.TM_CCOEFF_NORMED'

while(True):
    ret, frame = cap.read()
    method = eval(meth)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    loc = np.where(res >= 0.90)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img,top_left, bottom_right, 100, 2)
        print('zap!')
        raise (NameError('Zap'))
    
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()