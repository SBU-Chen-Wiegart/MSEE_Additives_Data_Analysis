# -*- coding: utf-8 -*-
"""
Measures volume loss on a segmented dataset and saves output as txt file
Assumes non-materials region = 0  in segmented image

Created on Tue Jul 19 14:38:34 2022

@author: clark
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from skimage import io
from os import listdir, chdir
import segmentation
from glob import glob

IN_PATH = r'/media/karenchen-wiegart/Lijie3/20210709_FXI_MSEE+/segmentation'
OUT_PATH = r'/media/karenchen-wiegart/Lijie3/20210709_FXI_MSEE+'
chdir(IN_PATH)

if __name__ == '__main__':
    
    files = sorted(glob('*.tif'))
    
    vols = np.zeros(len(files))
    scans = np.zeros(len(files))
    
    # assumes scans are in sequential order in folder
    for i, fn in enumerate(files):
        print(fn)
        scan_id = [int(s) for s in fn.split('_') if s.isdigit()][0]
        
        scans[i] = scan_id
        
        im3d = io.imread(f'{IN_PATH}/{fn}')
        im3d = segmentation.crop3d(im3d, crop_size=200)
                
        # seg_im = segmentation.seg_3d(im3d, 'Gaussian', 3, crop_im=(True), plot_seg=(True))
        vols[i] = np.count_nonzero(im3d)
        
    print(vols)
    
    rel_vols = vols / vols[np.argmin(scans)]  # divide by vol of first scan to get relative vols
    plt.plot(rel_vols, 'o')
    plt.show()
    
    scans_vol = np.column_stack((scans, vols, rel_vols))
    # np.savetxt(f'{OUT_PATH}/vol_loss.txt', scans_vol, fmt=['%d','%d','%.18e'], delimiter=', ', header='scan, vol, rel_vol')
    df = pd.DataFrame(scans_vol, columns=['scan','vol','rel_vol'])
    df = df.sort_values('scan', axis=0)
    print(df)
    df.to_csv(f'{OUT_PATH}/vol_loss.txt', index=None, sep=' ')
    
    
    