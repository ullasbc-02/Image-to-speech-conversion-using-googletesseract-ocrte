import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'F:\Programfiles\Tessarct\tesseract.exe'
from PIL import Image

img = Image.open('img.png')
text = tess.image_to_string(img)

print(text)
