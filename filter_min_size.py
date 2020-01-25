import numpy as np
from PIL import Image
import cv2

def min_filter(data, filter_size):
    height = data.shape[0]
    width = data.shape[1]

    for i in np.arange(3, height-3):
        for j in np.arange(3, width-3):
            min = 255
            for k in np.arange(-3, 4):
                for l in np.arange(-3, 4):
                    a = data.item(i+k, j+l)
                    if a < min:
                        min = a
            b = min
            data.itemset((i,j), b)

    return data


def main():
    img = Image.open("image_test/Noisy-image-Gaussian-noise-with-mean-and-variance-0005.png").convert("L")
    arr = np.array(img)
    removed_noise = min_filter(arr, 3) 
    img = Image.fromarray(removed_noise)
    img.show()


main()