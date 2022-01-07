import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'F:\Programfiles\Tessarct\tesseract.exe'
from PIL import Image

from gtts import gTTS
import os

img = Image.open('img_1.png')
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