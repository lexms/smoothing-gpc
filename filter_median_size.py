import numpy as np
from PIL import Image
import tensorflow as tf

def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = np.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final


def psnr():
    # Read images from file.
    im1 = tf.io.decode_png('image_test/Noisy-image-Gaussian-noise-with-mean-and-variance-0005.png')
    im2 = tf.io.decode_png('image_out/recover_median.png')
    # Compute PSNR over tf.uint8 Tensors.
    psnr1 = tf.image.psnr(im1, im2, max_val=255)
    return (psnr1)

def main():
    img = Image.open("image_test/Noisy-image-Gaussian-noise-with-mean-and-variance-0005.png").convert("L")
    arr = np.array(img)
    filter_size = 3
    removed_noise = median_filter(arr, filter_size) 
    img = Image.fromarray(removed_noise)
    img = img.convert('L')
    img.save('image_out/recover_median.png', 'png')


    #img.show() 


main()
psnr()
