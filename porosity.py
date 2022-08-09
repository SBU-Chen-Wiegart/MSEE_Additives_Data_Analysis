#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:16:38 2022

@author: Charles Clark
"""
import numpy as np
from glob import glob
from skimage import io
import os

IN_PATH = r'/media/karenchen-wiegart/20210321_FXI_backup/20210321_FXI_Backup/cropped_seg_masked'
os.chdir(IN_PATH)


def crop3d(im, crop_size=100):
    """
    crops 3d image to middle number of slices specified 
    """
    mid_pt = int(im.shape[0] / 2)
    return im[mid_pt - int(crop_size/2): mid_pt + int(crop_size/2)]


if __name__ == '__main__':
    files = sorted(glob('*.tiff'))
    
    porosity = np.zeros(len(files))
    scan = np.zeros(len(files))
    
    
    for i, fn in enumerate(files):
        scan_id = [int(s) for s in fn.split('_') if s.isdigit()][0]
        
        scan[i] = scan_id
        
        im3d = io.imread(fn)  # cropped and masked image
        
        im3d = crop3d(im3d, crop_size=400)
        
        material = np.count_nonzero(im3d==2)
        pores = np.count_nonzero(im3d==1)
        porosity[i] = pores / (material + pores)
        
    scan_porosity = np.vstack((scan, porosity)).T
    np.savetxt('porosities.txt', scan_porosity, fmt=['%d','%.18e'], delimiter=', ', header='scan, porosity')
    