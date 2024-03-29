"""
File: mid_slice
Name: Charles Clark
-------------------
Reads in tomography data and saves middle slice to image file
Good for getting initial visualization of a series of tomography scans
"""
import numpy as np
import h5py
from skimage import io, exposure
import matplotlib.pyplot as plt
from os.path import exists

IN_PATH = ''
OUT_PATH = ''

def middle_slice(filename):
    mid_pt = int(file['img'].shape[0] / 2)
    img = file.get('img')[mid_pt, :, :]  # get mid slice of 3D image
    img = np.array(img)  # convert to numpy array (of floats)
    
    # convert image to array of 8bit uints, and perform contrast stretching
    p2,p98 = np.percentile(img, (2,98)) # use percentile scaling to avoid influence from outlier pixels
    img_rescale = exposure.rescale_intensity(img, in_range=(p2,p98), out_range=(0,255)).astype(np.uint8)
    
    # plt.imshow(img_rescale, cmap='gray')
    
    io.imsave(f'{OUT_PATH}/{scan_id}.tif', img_rescale)

start_scan_id = 92121
stop_scan_id = 92121
# loop over scans to be processed
for i in range(start_scan_id, stop_scan_id+1):
    scan_id = str(i)
    
    fn = f'{IN_PATH}/recon_scan_{scan_id}_bin1.h5'
    
    # check that reconstructed scan exists
    if exists(fn):
        file = h5py.File(fn, 'r')  # load .h5 file
        middle_slice(fn)
    else: 
        print(f'no file found for scan {scan_id}')
        
    
        

