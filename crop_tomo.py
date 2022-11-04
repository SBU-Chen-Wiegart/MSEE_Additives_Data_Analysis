"""
File: crop_tomo
Name: Charles Clark
-------------------
Reads in 3D tomography from h5 files and crop to desired range (x, y, and z)
Output images saved as 3D tif files in out_path directory

"""
import numpy as np
import h5py
from skimage import io
from os.path import exists

in_path = 'E:/20210321_FXI_Backup/'
out_path = 'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/20210321_cropped_aligned_old/crop_only/'

x_min, x_max = 300, 300+695
y_min, y_max = 270, 270+710
z_min, z_max = 300, 701

first_scan = 92121
last_scan = 92122

scans = np.arange(first_scan, last_scan)

# loop over scans to be processed
if __name__ == '__main__':
    for i in scans:
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
