# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:29:29 2022

@author: clark
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from os import listdir, path
from scipy import signal, ndimage
from skimage.filters import threshold_minimum

# from normalize_count import rescale

IN_PATH = r'/media/karenchen-wiegart/20210321_FXI_backup/20210321_FXI_Backup/Charles/cropped_aligned_new'
OUT_PATH = r'/media/karenchen-wiegart/20210321_FXI_backup/20210321_FXI_Backup/Charles/cropped_new_segmentation'

def find_mid(im):
    return int(im.shape[0] / 2)

def crop3d(im, crop_size=300):
    """
    crops 3d image to middle number of slices specified 
    """
    mid_pt = find_mid(im)
    return im[mid_pt - int(crop_size/2): mid_pt + int(crop_size/2)]

def find_threshold(im2d, return_hist=False):
    """
    finds threshold of 2d image from histogram
    """
    histogram, bin_edges = np.histogram(im2d, bins=256)
    valleys = signal.find_peaks(-histogram, prominence=1000, distance=10)[0]  # edit parameters if getting too many
    
    threshold = 0 
    
    # # check found valleys
    # plt.plot(bin_edges[0:-1], histogram)
    # for v in valleys:
    #     plt.axvline(x=bin_edges[0:-1][v], c='r')
    # plt.show()
    # plt.clf()
    
    if valleys.size == 1:
        threshold = bin_edges[0:-1][valleys[0]]
    if valleys.size == 2:
        threshold = bin_edges[0:-1][valleys[1]]
    if valleys.size == 3:
        threshold = bin_edges[0:-1][valleys[2]]
    if valleys.size > 3:
        print("change find_peaks parameters")
    
    
    # threshold = threshold_minimum(im2d)

    if return_hist:
        return threshold, histogram, bin_edges
    else:
        return threshold



def seg_3d(image3d, image_filter, filter_size, crop_im=False, plot_seg=False, image_name=''):
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

    seg_image = np.where(image3d > threshold, 1.0, 0.0)     
    
    if plot_seg:
        fig = plt.figure(figsize=[12, 4])
        ax1 = fig.add_subplot(131)
        ax2 = fig.add_subplot(132)
        ax3 = fig.add_subplot(133)
        
        if image_name:
            fig.suptitle(f'{image_name}, {image_filter}, size={filter_size}')
        else:
            fig.suptitle(f'{image_filter}, size={filter_size}')
        
        ax1.imshow(image3d[mid_pt], cmap='gray')

        ax2.plot(bin_edges[0:-1], hist)
        ax2.axvline(x=threshold, c='r')
        
        ax3.imshow(seg_image[mid_pt], cmap='gray')
        
               
        if image_name:
            plt.savefig(f'{OUT_PATH}/{image_name}_segmentation.png', format='png')
        
        plt.show()
        
    return seg_image
        
    

if __name__ == '__main__':
    scan_list = list(np.arange(92079, 92079+1))
    files = sorted(listdir(IN_PATH))
    
    for scan in files:
        if any(str(scan_id) in scan for scan_id in scan_list) and ('aligned' in scan):
        # if ('99925' in scan) or ('aligned' in scan):
            image3d = io.imread(f'{IN_PATH}/{scan}')
            
            scan_name = path.splitext(scan)[0]  # remove file extension
            seg_image = seg_3d(image3d, image_filter='Gaussian', filter_size=3, crop_im=False, plot_seg=True, image_name=scan_name)
            
            io.imsave(f'{OUT_PATH}/seg_{scan}', np.float32(seg_image))
