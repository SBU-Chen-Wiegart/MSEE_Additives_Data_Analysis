"""
File: read_tomo
Name: Charles Clark
-------------------
Reads in 3D tomography data and crop to desired range (x, y, and z)
"""
import numpy as np
import h5py
from skimage import io, exposure
import matplotlib.pyplot as plt
from os.path import exists

in_path = 'H:/XIAOYANG_Proposal_307818/'
out_path = 'H:/XIAOYANG_Proposal_307818/cropped_charles/'

x_min, x_max = 300, 1000
y_min, y_max = 300, 1000
z_min, z_max = 300, 700

# loop over scans to be processed
for i in range(99925, 100010+1):
    scan_id = str(i)
    fn = in_path + 'recon_scan_' + scan_id + '_bin1.h5'
    
    # check that reconstructed scan exists
    if exists(fn):
        file = h5py.File(fn, 'r')  # load .h5 file
                
        # crop scan
        img = file.get('img')[z_min:z_max, y_min:y_max, x_min:x_max] 
        img = np.array(img)  # convert to numpy array (of floats)

        io.imsave(out_path + 'recon_' + scan_id + '_cropped.tif', img)

