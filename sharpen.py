import PIL
from PIL import Image
from PIL import ImageEnhance
import numpy as np
def sharp_image(image):
    img = image 
    img = ImageEnhance.Sharpness(img).enhance(2)
    img.save('step3.png')
    print("sharpen")

sharp_image(PIL.Image.open("step2.png"))