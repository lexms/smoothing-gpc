import numpy as np
import math
import cv2

def psnr(img1, img2):

    mse = np.mean( (img1 - img2) ** 2 ) #validated with sklearn metrics    
    print ('mse: ',mse)

    if mse == 0:
        return 100
    PIXEL_MAX = np.max(img1)
    PIXEL_MIN = np.min(img1)
    data_range = PIXEL_MAX - PIXEL_MIN
    print('data_range: ',data_range)
    return 10 * np.log10((data_range ** 2) / mse)

def main():
    
    #open recover
    img_recover2_path = 'image_out/recover_median.jpg'
    img_recover2 = cv2.imread(img_recover2_path, 0)

    #open target
    im_target_path = 'image_target/fruit.jpg'
    img_target = cv2.imread(im_target_path, 0)

    psnr_scratch = psnr(img_target, img_recover2)
    print ('psnr scratch: ',psnr_scratch)


    from sklearn.metrics import mean_squared_error
    mselib = mean_squared_error(img_target,img_recover2)
    print('mselib: ', mselib)

    from skimage.metrics import peak_signal_noise_ratio
    psnr_library = peak_signal_noise_ratio(img_target,img_recover2)
    print('psnr lib: ',psnr_library)
main()