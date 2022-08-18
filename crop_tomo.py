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

in_path = r'/media/karenchen-wiegart/Lijie3/20210709_FXI_MSEE+/'
out_path = r'/media/karenchen-wiegart/Lijie3/20210709_FXI_MSEE+/cropped/'

x_min, x_max = 300, 1000
y_min, y_max = 300, 1000
z_min, z_max = 300, 800

# loop over scans to be processed
if __name__ == '__main__':
    for i in range(100011, 100013+1):
        scan_id = str(i)
        fn = in_path + 'recon_scan_' + scan_id + '_bin1.h5'
        
        # check that reconstructed scan exists
        if exists(fn):
            file = h5py.File(fn, 'r')  # load .h5 file
                    
            # crop scan
            img = file.get('img')[z_min:z_max, y_min:y_max, x_min:x_max] 
            img = np.array(img)  # convert to numpy array (of floats)
    
            io.imsave(out_path + 'recon_' + scan_id + '_cropped.tif', img)
        else:
            print("error")
