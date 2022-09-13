# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:49:39 2022

@author: clark
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% load data
IN_PATH = 'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/results'
OUT_PATH = 'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/vol-loss_porosity_plots'
fn1 = '20210321_porosity_vol-loss_trimmed.xlsx'
df1 = pd.read_excel(f'{IN_PATH}/{fn1}')

fn2 = '20210709_porosity_vol-loss_trimmed.xlsx'
df2 = pd.read_excel(f'{IN_PATH}/{fn2}')

#%% organize data
time_5050 = df1['time']
porosity_5050 = df1['porosity']
rel_vol_5050 = df1['rel_vol']
vol_5050 = np.array(df1['vol'])

time_eutectic = df2['time']
porosity_eutectic = df2['porosity']
rel_vol_eutectic = df2['rel_vol']
vol_eutectic = np.array(df2['vol'])

#%% set plot parameters
plt.rc('axes', labelsize=18, titlesize=21)
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)

#%% plot vol-loss
plt.rc('lines', markersize=12)

plt.figure(figsize=[10,8])
plt.title('50:50 $KCl$-$MgCl_2$, 1wt.% $EuCl_3$')
plt.xlabel('Time (min)')
plt.ylabel('Vol Remaining (%)')
plt.plot(time_5050, rel_vol_5050*100, '.', c='r')
plt.savefig(f'{OUT_PATH}/50-50_vol-loss.tif', format='tif')
plt.show()

plt.figure(figsize=[10,8])
plt.title('Eutectic $KCl$-$MgCl_2$, 1wt.% $EuCl_3$')
plt.xlabel('Time (min)')
plt.ylabel('Vol Remaining (%)')
plt.plot(time_eutectic, rel_vol_eutectic*100, '.', c='k')
plt.savefig(f'{OUT_PATH}/Eutectic_vol-loss.tif', format='tif')
plt.show()

plt.figure(figsize=[10,8])
plt.xlabel('Time (min)')
plt.ylabel('Vol Remaining (%)')
plt.plot(time_5050, rel_vol_5050*100, '.', c='r', label='50:50 $KCl$-$MgCl_2$')
plt.plot(time_eutectic, rel_vol_eutectic*100, '.', c='k', label='eutectic $KCl$-$MgCl_2$')
plt.legend(fontsize=15)
plt.savefig(f'{OUT_PATH}/comparison_vol-loss.tif', format='tif')
plt.show()
#%% plot porosity
plt.rc('lines', markersize=10, markeredgewidth=2)

plt.figure(figsize=[10,8])
plt.title('50:50 $KCl$-$MgCl_2$, 1wt.% $EuCl_3$')
plt.xlabel('Time (min)')
plt.ylabel('Porosity (%)')
plt.ylim([0,25])
plt.plot(time_5050, porosity_5050*100, 'x', c='r')
plt.savefig(f'{OUT_PATH}/50-50_porosity.tif', format='tif')
plt.show()


plt.figure(figsize=[10,8])
plt.title('Eutectic $KCl$-$MgCl_2$, 1wt.% $EuCl_3$')
plt.xlabel('Time (min)')
plt.ylabel('Porosity (%)')
plt.ylim([0,30])
plt.plot(time_eutectic, porosity_eutectic*100, 'x', c='k')
plt.savefig(f'{OUT_PATH}/Eutectic_porosity.tif', format='tif')
plt.show()

plt.figure(figsize=[10,8])
plt.xlabel('Time (min)')
plt.ylabel('Porosity (%)')
plt.plot(time_5050, porosity_5050*100, 'x', c='r', label='50:50 $KCl$-$MgCl_2$')
plt.plot(time_eutectic, porosity_eutectic*100, 'x', c='k', label='eutectic $KCl$-$MgCl_2$')
plt.legend(fontsize=15)
plt.ylim([0,30])
plt.savefig(f'{OUT_PATH}/comparison_porosity.tif', format='tif')
plt.show()

