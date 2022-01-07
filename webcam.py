import numpy as np
import cv2
cap = cv2.VideoCapture(0)
count=0
while(True):
# Capture frame-by-frame
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',frame)
  cv2.imwrite("frame%d.jpg" % count, frame)
  # count=+1
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
# When everything done, release the apture
cap.release()
cv2.destroyAllWindows()