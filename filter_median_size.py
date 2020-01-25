import numpy as np
import cv2
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


def log10(x):
    numerator = tf.math.log(x)
    denominator = tf.math.log(tf.constant(10, dtype=numerator.dtype))
    return numerator / denominator


def psnr(im1, im2):
    img_arr1 = np.array(im1).astype('float32')
    img_arr2 = np.array(im2).astype('float32')
    mse = tf.reduce_mean(tf.math.squared_difference(img_arr1, img_arr2))
    psnr = tf.constant(255**2, dtype=tf.float32)/mse
    result = tf.constant(10, dtype=tf.float32)*log10(psnr)
    with tf.Session():
        result = result.eval()
    return result

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