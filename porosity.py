#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Measures porosity of a segmented and masked dataset, saves output as txt file
assumes material region = 2, and porous regions = 1 in masked image

Created on Tue Aug  9 13:16:38 2022

@author: Charles Clark
"""
import numpy as np
import pandas as pd
from glob import glob
from skimage import io
import os

IN_PATH = r'/media/karenchen-wiegart/Lijie3/20210709_FXI_MSEE+/masked'
OUT_PATH = r'/media/karenchen-wiegart/Lijie3/20210709_FXI_MSEE+/'
os.chdir(IN_PATH)


def crop3d(im, crop_size=200):
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
        print(fn)
        scan_id = [int(s) for s in fn.split('_') if s.isdigit()][0]
        
        scan[i] = scan_id
        
        im3d = io.imread(fn)  # cropped and masked image
        
        im3d = crop3d(im3d, crop_size=200)
        
        material = np.count_nonzero(im3d==2)
        pores = np.count_nonzero(im3d==1)
        porosity[i] = pores / (material + pores)
        
    scan_porosity = np.column_stack((scan, porosity))
    # np.savetxt(f'{OUT_PATH}/porosities.txt', scan_porosity, fmt=['%d','%.18e'], delimiter=', ', header='scan, porosity')
    
    df = pd.DataFrame(scan_porosity, columns=['scan','porosity'])
    df = df.sort_values('scan', axis=0)
    print(df)
    df.to_csv(f'{OUT_PATH}/porosity.txt', index=None, sep=' ')
    