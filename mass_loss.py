# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:38:34 2022

@author: clark
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from os import listdir, chdir
import segmentation
from glob import glob

IN_PATH = r'/media/karenchen-wiegart/Lijie3/20210709_FXI_MSEE+/segmentation'
OUT_PATH = r'/media/karenchen-wiegart/Lijie3/20210709_FXI_MSEE+'
chdir(IN_PATH)

if __name__ == '__main__':
    
    files = sorted(glob('*.tif'))
    
    masses = np.zeros(len(files))
    scans = np.zeros(len(files))
    
    # assumes scans are in sequential order in folder
    for i, fn in enumerate(files):
        scan_id = [int(s) for s in fn.split('_') if s.isdigit()][0]
        
        scans[i] = scan_id
        
        im3d = io.imread(f'{IN_PATH}/{fn}')
        im3d = segmentation.crop3d(im3d, crop_size=200)
                
        # seg_im = segmentation.seg_3d(im3d, 'Gaussian', 3, crop_im=(True), plot_seg=(True))
        masses[i] = np.count_nonzero(im3d)
        
    print(masses)
    
    rel_masses = masses / masses[0]
    plt.plot(rel_masses, 'o')
    plt.show()
    
    scans_mass = np.column_stack((scans, masses, rel_masses))
    np.savetxt(f'{OUT_PATH}/mass_loss.txt', scans_mass, fmt=['%d','%d','%.18e'], delimiter=', ', header='scan, mass, rel_mass')
    
    
    