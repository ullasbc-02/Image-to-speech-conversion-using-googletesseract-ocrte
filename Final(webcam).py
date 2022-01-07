import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'F:\Programfiles\Tessarct\tesseract.exe'
from PIL import Image

from gtts import gTTS
import os

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
count=0

while(True):# Capture frame-by-frame
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',frame)
  cv2.imwrite("frame%d.jpg" % count, frame)
  # count=+1
  if cv2.waitKey(2): #& 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()

img = Image.open('frame0.jpg')
textname = tess.image_to_string(img)
print(textname)


# Language we want to use
language = 'en' #es,fr
# lang='co.in' #ld

output = gTTS(text=textname, lang=language, slow=False)

output.save("output.mp3")
# fh.close()

# Play the converted file
os.system("start output.mp3")

#remove the image
os.remove("F:\PycharmProjects\Image_to_speech\\frame0.jpg")

