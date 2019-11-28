from PIL import Image 
import string
import pytesseract

def extract(image):
    pytesseract.pytesseract.tesseract_cmd = 'D:\\Softwares\\Tesseract-OCR\\tesseract'
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

# GET REQD INFO OF VOTER USING A FORM AN THEN VERIFYING THE INFO AGAINST THE INFO CONATINED IN FINAL ARRAY