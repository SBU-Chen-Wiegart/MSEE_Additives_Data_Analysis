# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:28:39 2022

@author: Chen-Wiegart
"""


import pandas as pd
from skimage import io
import numpy as np
import os
path = r'D:\Xiaoyang\Additive_moltensalt\process\crop_image'
os.chdir(path)

file = r'79755_x250_y300_w750_h750_z300-850.tif'
img = io.imread(rf'{path}\{file}')
sli_list = np.arange(0,501,100)

for s in sli_list:
    img_slice = img[s]
    io.imsave(f'{file}_sli{s}.tif',img_slice)


#---------------------For x and y ---------------
img_slice = img[:,:,325]   #yz
io.imsave(f'{file}_x325.tif',img_slice)
img_slice2 = img[:,325,:]  #xz
io.imsave(f'{file}_y325.tif',img_slice2)
