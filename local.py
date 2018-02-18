#!/usr/bin/env python

import numpy as np
import cv2, sys

cap = cv2.VideoCapture(1)

frames = []

while(True):
    ret, frame = cap.read()
    cv2.imshow('video',frame)
    frames.append(frame)
    sys.stdout.write( frm.tostring() )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# saving as image
# cv2.imwrite("save.png",frames[4])

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
