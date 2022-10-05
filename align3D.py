# -*- coding: utf-8 -*-
"""
Mingyuan Ge's code for 3D volume registration.
Currently set up to sequentially perform image alignment/registration on 
directory containing a series of 3D images as tif files (e.g. reconstructed
tomography scans).

To use set in_path to directory containing images, and out_path to desired 
location for aligned images to be saved.
NOTE: Expects input images to be named in the following format:
    recon_{scan_id}_cropped.tif

Created on Thu Apr 14 04:20:49 2022

@author: 93969
"""


import os
# import pyxas
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

in_path = r'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/20210321_cropped_aligned_old/crop_only'
out_path = r'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/20210321_cropped_aligned_old'
os.chdir(in_path)

def idxmax(data):
   ndim = np.shape(data)
   #maxd = np.max(data)
   maxd = np.max(np.abs(data))
   #t1 = plt.mlab.find(np.abs(data) == maxd)
   t1 = np.argmin(np.abs((np.abs(data) - maxd)))
   idx = np.zeros([len(ndim),])
   for ii in range(len(ndim)-1):
       t1,t2 = np.modf(1.*t1/np.prod(ndim[(ii+1):]))
       idx[ii] = t2
       t1 *= np.prod(ndim[(ii+1):])
   idx[np.size(ndim)-1] = t1

   return maxd,idx

def align_img3D(img_ref, img, align_flag=1):
    #from scipy.fftpack import fftn, ifftn, fftshift, ifftshift
    from scipy.ndimage import shift
    img1f = np.fft.fftn(img_ref)
    img2f = np.fft.fftn(img)
    cc = np.fft.ifftn(img1f * np.conj(img2f))
    max1, loc1 = idxmax(cc)

    s = img_ref.shape
    s_2 = np.fix(np.array(s) / 2)
    shft = [0] * len(s)
    for i in range(len(s)):
        if loc1[i] > s_2[i]:
            shft[i] = loc1[i] - s[i]
        else:
            shft[i] = loc1[i]    
    if align_flag:
        img_shift = shift(img, shft, mode='constant', cval=0, order=1)
        return img_shift, shft[0], shft[1], shft[2]
    else:
        return shft[0], shft[1], shft[2]
    
# loop for scan alignment (first scan should be aligned "manually")
#%%
scans = np.arange(92078, 92079+1)
scan_list = [s for s in scans if os.path.exists(f'recon_{s}_cropped.tif')]

#%%
for ind, scan_id in enumerate(scan_list):
    if ind != 0:
        ref_scan = scan_list[ind-1]        
        #read the images
        img_ref = io.imread(f'{out_path}/recon_{ref_scan}_cropped_aligned.tif')
        img_moving = io.imread(f'recon_{scan_id}_cropped.tif')
            
        para = align_img3D(img_ref, img_moving, align_flag=1)
        img_aligned = para[0]
        img_dect = img_ref-img_aligned
        
        # Plotting
        i = 200
        plt.figure(figsize=(15,8))
        plt.subplot(131)
        plt.imshow(img_ref[i])
        plt.title('ref image')
        plt.subplot(132)
        plt.imshow(img_aligned[i])
        plt.title('moved image')
        plt.subplot(133)
        plt.imshow(img_dect[i])
        plt.title('subtraction')
        plt.savefig(f'{out_path}/{scan_id}_alignment')
        '''
        plt.subplot(134)
        plt.imshow(img_dect[i])
        plt.title('Subtraction')
        '''
        io.imsave(f'{out_path}/recon_{scan_id}_cropped_aligned.tif',img_aligned)