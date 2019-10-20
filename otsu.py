from skimage import data, exposure, img_as_float
import warnings
import utils
import numpy as np
import PIL
from PIL import Image

def threshold_otsu(image, nbins=256):
 
    if len(image.shape) > 2 and image.shape[-1] in (3, 4):
        msg = "threshold_otsu is expected to work correctly only for " \
              "grayscale images; image shape {0} looks like an RGB image"
        warnings.warn(msg.format(image.shape))

    if image.min() == image.max():
        raise ValueError("threshold_otsu is expected to work with images "
                         "having more than one color. The input image seems "
                         "to have just one color {0}.".format(image.min()))

    hist, bin_centers = exposure.histogram(image.ravel(), nbins, source_range='image')
    hist = hist.astype(float)

    weight1 = np.cumsum(hist)
    weight2 = np.cumsum(hist[::-1])[::-1]
    
    mean1 = np.cumsum(hist * bin_centers) / weight1
    mean2 = (np.cumsum((hist * bin_centers)[::-1]) / weight2[::-1])[::-1]

    variance12 = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

    idx = np.argmax(variance12) #within class variance
    threshold1 = bin_centers[:-1][idx]
    print("otsu")
    return threshold1

img = PIL.Image.open("step4.png")
arr = np.array(img)
print(threshold_otsu(arr))
