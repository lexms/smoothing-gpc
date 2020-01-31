import cv2
import numpy as np
from skimage.util import random_noise

img = cv2.imread('image_target/imtarget.jpg')

img_noise = random_noise(img, mode='s&p',amount=0.3)

img_noise = np.array(255*img_noise, dtype = 'uint8')

img_noise_path = 'image_test/test_noise_added.jpg'

cv2.imwrite(img_noise_path,img_noise)