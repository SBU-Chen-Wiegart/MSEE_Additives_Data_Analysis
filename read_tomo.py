"""
File: read_tomo
Name: Charles Clark
-------------------
Reads in tomography data and converts middle slice to image file
"""
import numpy as np
import h5py
from skimage import io, exposure
import matplotlib.pyplot as plt
from os.path import exists

# loop over scans to be processed
for i in range(99925, 100010+1):
    scan_id = str(i)
    fn = 'E:/XIAOYANG_Proposal_307818/recon_scan_' + scan_id + '_bin1.h5'
    
    # check that reconstructed scan exists
    if exists(fn):
        file = h5py.File(fn, 'r')  # load .h5 file
                
        img = file.get('img')[500, :, :]  # get 500th slice of 3D image
        img = np.array(img)  # convert to numpy array (of floats)
        
        # convert image to array of 8bit uints, and perform contrast stretching
        p2,p98 = np.percentile(img, (2,98)) # use percentile scaling to avoid influence from outlier pixels
        img_rescale = exposure.rescale_intensity(img, in_range=(p2,p98), out_range=(0,255)).astype(np.uint8)
        
        plt.imshow(img_rescale, cmap='gray')
        
        io.imsave('EuCl3_in-situ/20210709/' + scan_id + '.tif', img_rescale)

