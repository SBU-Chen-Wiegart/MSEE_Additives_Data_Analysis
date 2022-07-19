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

def find_mid(im):
    return int(im.shape[0] / 2)

def crop3d(im):
    """
    crops 3d image to middle 10 slices
    """
    mid_pt = find_mid(im)
    return im[mid_pt - 5: mid_pt + 5]

def find_threshold(im2d, return_hist=False):
    """
    finds threshold of 2d image from histogram
    """
    histogram, bin_edges = np.histogram(im2d, bins=256)
    valleys = signal.find_peaks(-histogram, prominence=(1000), distance=10)[0]  # edit parameters if getting too many
    
    threshold = 0 
    if valleys.size == 1:
        threshold = bin_edges[0:-1][valleys[0]]
    if valleys.size == 2:
        threshold = bin_edges[0:-1][valleys[1]]
    if valleys.size > 2:
        print("change find_peaks parameters")

    if return_hist:
        return threshold, histogram, bin_edges
    else:
        return threshold



def seg_3d(image3d, image_filter, filter_size, crop_im=False, plot_seg=False):
    """
    Perform thresholding segmentation on 3d image. Threhold is determined from
    histogram of middle slice from 3d image.
    """
    
    if crop_im:
        image3d = crop3d(image3d)
        
    if image_filter.lower() == 'median':
        image3d = ndimage.median_filter(image3d, size=filter_size)
    elif image_filter.lower() == 'mean':
        image3d = ndimage.generic_filter(image3d, np.mean, size=filter_size)
    elif image_filter.lower() == 'gaussian':
        image3d = ndimage.gaussian_filter(image3d, sigma=filter_size)
    else:
        print('Invalid filter. Currently supported: median, mean, gaussian.')
      
    mid_pt = find_mid(image3d)
    mid_slice = image3d[mid_pt]    
    
    threshold, hist, bin_edges = find_threshold(mid_slice, return_hist=True)

    seg_image = np.where(image3d > threshold, 1, 0)     
    
    if plot_seg:
        fig = plt.figure(figsize=[12, 4])
        ax1 = fig.add_subplot(131)
        ax2 = fig.add_subplot(132)
        ax3 = fig.add_subplot(133)
        
        fig.suptitle(f'{image_filter}, size={filter_size}')
        
        ax1.imshow(image3d[mid_pt], cmap='gray')

        ax2.plot(bin_edges[0:-1], hist)
        ax2.axvline(x=threshold, c='r')
        
        ax3.imshow(seg_image[mid_pt], cmap='gray')
        
        plt.show()
        
    return seg_image
        
    

if __name__ == '__main__':
    scan_list = [92067, 92107, 92132]
    files = listdir(IN_PATH)
    
    for scan in files:
        if any(str(scan_id) in scan for scan_id in scan_list):
            image3d = io.imread(f'{IN_PATH}/{scan}')
            
            x = seg_3d(image3d, image_filter='Mean', filter_size=5, crop_im=True, plot_seg=True)

