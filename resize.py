from skimage.transform import resize
import PIL
from PIL import Image
import numpy as np

def resized(image):
    img = image 
    resizedImage = img.resize((540, 860), PIL.Image.ANTIALIAS)
    resizedImage.save('step2.png')
    print("resize")
    
resized(PIL.Image.open("step1.png"))



