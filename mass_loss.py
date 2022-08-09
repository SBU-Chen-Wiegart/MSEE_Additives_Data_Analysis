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

IN_PATH = r'/media/karenchen-wiegart/20210321_FXI_backup/20210321_FXI_Backup/cropped_new_segmentation'


if __name__ == '__main__':
    
    files = sorted(listdir(IN_PATH))
    
    masses = np.zeros(len(files))
    
    # assumes scans are in sequential order in folder
    for i, scan in enumerate(files):
        im3d = io.imread(f'{IN_PATH}/{scan}')
        im3d = segmentation.crop3d(im3d, crop_size=2)
                
        # seg_im = segmentation.seg_3d(im3d, 'Gaussian', 3, crop_im=(True), plot_seg=(True))
        masses[i] = np.count_nonzero(im3d)
        
    print(masses)
    
    rel_masses = masses / masses[0]
    plt.plot(rel_masses)
    plt.show()