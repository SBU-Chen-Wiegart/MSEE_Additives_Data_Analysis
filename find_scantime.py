# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:01:44 2022

@author: Chen-Wiegart
"""

import h5py
import time
import pandas as pd
import numpy as np
from os.path import exists

folder = 'E:/20210321_FXI_Backup/'
first_scan = 92064
last_scan = 92133
scanlist = np.arange(first_scan, last_scan+1, 1)
local_time_list = []
savefolder = 'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/'
for s in scanlist:
    filename = 'fly_scan_id_'+str(s)+'.h5'
    # check that scan exists before trying to extracting time
    if exists(folder + filename): 
        f = h5py.File(folder+filename, 'r')
        tt = f.get('scan_time')[()]
        tt_int = int(tt)
        local_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tt_int)))
        print(local_time)
        local_time_list.append(local_time)
    # if scan does not exists write N/A to csv
    else:
        local_time_list.append('N/A')
pd = pd.DataFrame(zip(scanlist,local_time_list),columns=['scan','local time'])
pd.to_csv(savefolder + '20210321_scan_time.csv')


