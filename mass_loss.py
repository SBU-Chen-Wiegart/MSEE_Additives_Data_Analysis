# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:38:34 2022

@author: clark
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from os import listdir
import segmentation

IN_PATH = r'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/20210321_cropped_aligned'


if __name__ == '__main__':
    
    files = listdir(IN_PATH)
    
    masses = np.zeros(len(files))
    
    # assumes scans are in sequential order in folder
    for i, scan in enumerate(files):
        im3d = io.imread(f'{IN_PATH}/{scan}')
        seg_im = segmentation.seg_3d(im3d, 'Gaussian', 3, crop_im=(True), plot_seg=(True))
        masses[i] = np.count_nonzero(seg_im)
        
    print(masses)
    
    rel_masses = masses / masses[0]
    plt.plot(rel_masses)
    plt.show()