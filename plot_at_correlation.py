# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 14:38:59 2022

@author: xiaoy
"""

from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import os
from skimage.measure import profile_line
import matplotlib.patches as patches
import pandas as pd
import glob

path = 'C://Research//2020_xiaoyang//MoltenSalt//manuscript_prep//additives//TEM//Correlation_study//Cr-rich region//'
os.chdir(path)

files = glob.glob(path+'1521*.tif')
new = np.zeros([len(files),864,640])
ele1 = []
for f in range(len(files)):
    img = io.imread(files[f])
    name = os.path.splitext(os.path.basename(files[f]))[0]
    new[f] = img
    ele1.append(name)    
print(ele1)


total = new.sum(axis=0)
ratio = np.zeros([len(files),864,640])
for n in range(new.shape[0]):
    ratio[n] = np.divide(new[n],total)
    
    
    
Cl = ratio[0].flatten()
Cr = ratio[1].flatten()
Ni = ratio[4].flatten()
O = ratio[5].flatten()
#----------------------------Cr-rich region------------------------

xstart =4
w = 25
ystart=121
h=7

Cl = ratio[0,ystart:ystart+h,xstart:xstart+w].flatten()
Cr = ratio[1,ystart:ystart+h,xstart:xstart+w].flatten()
Ni = ratio[4,ystart:ystart+h,xstart:xstart+w].flatten()
O = ratio[5,ystart:ystart+h,xstart:xstart+w].flatten()

fig2, ax = plt.subplots(1,2,figsize=(8,10))
#fig2.tight_layout()

ax[0].plot(Cr,Cl,'.',markersize=18,color='red');ax[0].set_xlabel('Cr atomic ratio');ax[0].set_ylabel('Cl atomic ratio');ax[0].tick_params(axis='both',labelsize=20)
ax[1].plot(Cr,O,'.',markersize=18,color='red');ax[1].set_xlabel('Cr atomic ratio');ax[1].set_ylabel('O atomic ratio');ax[1].tick_params(axis='both',labelsize=20)

#-------------------------------Ni-rich region--------------------
xstart = 367
w = 32
ystart=43
h=5
Cl = ratio[0,ystart:ystart+h,xstart:xstart+w].flatten()
Cr = ratio[1,ystart:ystart+h,xstart:xstart+w].flatten()
Ni = ratio[4,ystart:ystart+h,xstart:xstart+w].flatten()
O = ratio[5,ystart:ystart+h,xstart:xstart+w].flatten()


fig2, ax = plt.subplots(1,2,figsize=(8,8))
#fig2.tight_layout()

ax[0].plot(Cr,Cl,'.',markersize=18,color='green');ax[0].set_xlabel('Ni atomic ratio');ax[0].set_ylabel('Cl atomic ratio');ax[0].tick_params(axis='both',labelsize=20)
ax[1].plot(Cr,O,'.',markersize=18,color='green');ax[1].set_xlabel('Ni atomic ratio');ax[1].set_ylabel('O atomic ratio');ax[1].tick_params(axis='both',labelsize=20)
#ax[1,0].plot(Ni,Cl,'.',markersize=8);ax[1,0].set_xlabel('Ni atomic ratio');ax[1,0].set_ylabel('Cl atomic ratio')
#ax[1,1].plot(Ni,O,'.',markersize=8);ax[1,1].set_xlabel('Ni atomic ratio');ax[1,1].set_ylabel('O atomic ratio')



  
    
