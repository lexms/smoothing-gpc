import numpy as np
import cv2

img = cv2.imread('image_test/fruit_20p_noise.jpg', 0)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

for i in np.arange(3, height-3):
    for j in np.arange(3, width-3):
        min = 255
        for k in np.arange(-3, 4):
            for l in np.arange(-3, 4):
                a = img.item(i+k, j+l)
                if a < min:
                    min = a
        b = min
        img_out.itemset((i,j), b)

cv2.imwrite('image_out/recover_min_n.jpg', img_out)

cv2.imshow('image',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()