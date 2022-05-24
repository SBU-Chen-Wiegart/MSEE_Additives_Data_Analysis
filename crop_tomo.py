"""
File: read_tomo
Name: Charles Clark
-------------------
Reads in 3D tomography data and crop to desired range (x, y and z)
"""
import numpy as np
import h5py
from skimage import io, exposure
import matplotlib.pyplot as plt
from os.path import exists

in_path = 'E:/XIAOYANG_Proposal_307818/recon_scan_'
out_path = 'EuCl3_in-situ/20210709/cropped_charles'

# loop over scans to be processed
for i in range(99925, 100010+1):
    scan_id = str(i)
    fn = in_path + scan_id + '_bin1.h5'
    
    # check that reconstructed scan exists
    if exists(fn):
        file = h5py.File(fn, 'r')  # load .h5 file
                
        img = file.get('img')[300:700, 300:1000, 300:1000]  # get 500th slice of 3D image
        img = np.array(img)  # convert to numpy array (of floats)

        io.imsave(out_path + 'recon' + scan_id + 'cropped.tif', img)

