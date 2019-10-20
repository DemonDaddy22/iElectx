import cv2
import numpy as np
import PIL 
from PIL import Image

im=PIL.Image.open("test.jpg")
def filter(image):
    img = image
    arr = np.array(img)
    dilated_img = cv2.cv2.dilate(arr[:,:,1], np.ones((7, 7), np.uint8))
    bg_img = cv2.cv2.medianBlur(dilated_img, 21)
    
    diff_img = 255 - cv2.cv2.absdiff(arr[:,:,1], bg_img) #preserve edges
    norm_img = cv2.cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.cv2.NORM_MINMAX, dtype=cv2.cv2.CV_8UC1)

    im=Image.fromarray(norm_img)
    im.save('step1.png')
    print("blur")

filter(im)