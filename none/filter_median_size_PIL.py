import numpy as np
from PIL import Image
import math
from skimage.metrics import peak_signal_noise_ratio

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
    img1 = np.array(img1)
    img2 = np.array(img2)

    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


def main():
    #load image
    im1_path = 'image_test/fruit_20p_noise.jpg'
    img1 = Image.open(im1_path).convert("L")
    img1_arr = np.array(img1)
    
    #run filter
    filter_size = 3
    removed_noise = median_filter(img1_arr, filter_size)

    #save image
    img_recover_path = 'image_out/recover_median_pil.jpg'
    img_recover = Image.fromarray(removed_noise)
    img_recover = img_recover.convert('L')
    img_recover.save(img_recover_path, 'jpeg')

    #open target
    img_target_path = 'image_target/fruit.jpg'
    img_target = Image.open(img_target_path)
    
    psnr_result = psnr(img_recover,img_target)
    print (psnr_result)

    #img_recover2 = Image.open('image_out/recover_median.jpg')
    #img_recover2_arr = np.array(img_recover2)
    #psnr_library = peak_signal_noise_ratio(img_target_arr,img_recover2_arr)
    #print(psnr_library)

main()

