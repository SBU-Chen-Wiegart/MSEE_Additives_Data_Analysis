# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:29:29 2022

@author: clark
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from os import listdir
from scipy import signal, ndimage

# from normalize_count import rescale

IN_PATH = r'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/20210321_cropped_aligned'
OUT_PATH = r'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/segmentation_results'

if __name__ == '__main__':
    scan_list = [92067, 92107, 92132]
    files = listdir(IN_PATH)
    
    for scan in files:
        if any(str(scan_id) in scan for scan_id in scan_list):
            image3d = io.imread(f'{IN_PATH}/{scan}')
            image3d = ndimage.median_filter(image3d, size=3)  # takes forever
            
            mid_slice = int(image3d.shape[0] / 2)
            im = image3d[mid_slice]
            # im = ndimage.median_filter(im, size=6)
            
            plt.imshow(im, cmap='gray')
            plt.show()            
            
            histogram, bin_edges = np.histogram(im, bins=256)

            plt.plot(bin_edges[0:-1], histogram)
            
            
            valleys = signal.find_peaks(-histogram, prominence=(1000), distance=10)[0]  # edit parameters if getting too many
            for v in valleys:
                plt.axvline(x=bin_edges[0:-1][v], c='k')
                
            plt.show()
            
            threshold = 0 
            if valleys.size == 1:
                threshold = bin_edges[0:-1][valleys[0]]
            if valleys.size == 2:
                threshold = bin_edges[0:-1][valleys[1]]

            seg_3d = np.where(image3d > threshold, image3d, 0)
            plt.imshow(seg_3d[mid_slice], cmap='gray')
            plt.show()