# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:19:57 2022

@author: crclark
"""

import h5py
import numpy as np
import pandas as pd
from os.path import exists

IN_PATH = 'I:/20210321_FXI_Backup/'

first_scan = 92064
last_scan = 92133
scanlist = np.arange(first_scan, last_scan+1, 1)

OUT_PATH = 'I:/20210321_FXI_Backup/'

rotcen_list = []

for s in scanlist:
    filename = 'recon_scan_'+str(s)+'_bin1.h5'
    if exists(f'{IN_PATH}{filename}'):
        f = h5py.File(f'{IN_PATH}{filename}', 'r')
        rotcen = f.get('rot_cen')[()]
        rotcen_list.append(rotcen)
        
    else:
        rotcen_list.append('')
        
df = pd.DataFrame(zip(scanlist, rotcen_list),columns=['scan','rot_cen'])
df.to_csv(OUT_PATH + '20210321_rotcen.csv')
