import numpy as np
import math
import cv2

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



def psnr(img1, img2):
    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def main():
    #load image
    im1_path = 'image_test/fruit_20p_noise.jpg'
    img1 = cv2.imread(im1_path, 0)
    
    #run filter
    filter_size = 3
    removed_noise = median_filter(img1, filter_size)

    #save image
    im_recover = 'image_out/recover_median.jpg'
    img_recover = cv2.imwrite(im_recover,removed_noise)


    im_target_path = 'image_target/fruit.jpg'
    img_target = cv2.imread(im_target_path, 0)

    psnrxx = psnr(img_recover,img_target)
    print (psnrxx)

main()

