# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 12:53:23 2022

@author: clark
"""
import numpy as np
import h5py
from skimage import io, exposure
import tifffile as tif
import matplotlib.pyplot as plt
from os.path import exists


def load_file(path, fn):
    if exists(path+fn):
        if fn.lower().endswith('h5'):
            file = h5py.File(path + fn, 'r')  # load .h5 file
    else:
        print('file not found')
    return file
    

def normalize(target, wf, df):
    return (target - df) / (wf - df)
    
def rescale(img):
    p2,p98 = np.percentile(img, (2,98)) # use percentile scaling to avoid influence from outlier pixels
    img_rescale = exposure.rescale_intensity(img, in_range=(p2,p98), out_range=(0,255)).astype(np.uint8)
    return img_rescale

if __name__ == '__main__':
    # loop over scans to be processed
    for i in range(99928, 99945+1):
        scan_id = str(i)
        in_path = 'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/count_scans/'
        out_path = in_path
        
        target_file = 'count_id_' + scan_id + '.h5'        
        wf_file = '99926_bkg_avg.tif'
        df_file = '99926_dark_avg.tif'
        
        wf = io.imread(in_path + wf_file)
        df = io.imread(in_path + df_file)
        
        target_h5 = h5py.File(in_path + target_file, 'r')
        target = np.array(target_h5.get('img'))
        
        norm_img = np.zeros(target.shape)
        for i, t in enumerate(target):
            norm_img[i] = normalize(t, wf, df)
        
        plt.imshow(target[0])
        plt.show()
        
        plt.imshow(norm_img[0])
        plt.show()
        
        norm_img = rescale(norm_img)
        io.imsave(out_path + f'{scan_id}_normalized_rescaled.tif', norm_img)
        
        