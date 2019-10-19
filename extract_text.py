from PIL import Image 
import string
import pytesseract

def extract(image):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
    t = pytesseract.image_to_string(Image.open(img))
    print(t)
    a1=[]
    s=""
    for i in range(len(t)):
        if(t[i]==' ' or t[i]=="\n"):
            a1.append(s)
            s = ""
        else:
            s = s+t[i]
    print(a1)

img = 'step4.png'
extract(img)

