# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:49:39 2022

@author: clark
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% load data
IN_PATH = 'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ'
OUT_PATH = 'C:/Users/clark/OneDrive - Stony Brook University/Documents/Karen/Molten Salt/EuCl3_in-situ/mass-loss_porosity_plots'
fn1 = '20210321_porosity_mass-loss.xlsx'
df1 = pd.read_excel(f'{IN_PATH}/{fn1}')

fn2 = '20210709_porosity_mass-loss.xlsx'
df2 = pd.read_excel(f'{IN_PATH}/{fn2}')
df2 = df2.iloc[1:, :]  # drop scan 99925

#%% organize data
time_5050 = df1['time']
porosity_5050 = df1['porosity']
# rel_mass = df['rel_mass']
mass_5050 = np.array(df1['mass'])
rel_mass_5050 = mass_5050 / mass_5050[0]

time_eutectic = df2['time']
porosity_eutectic = df2['porosity']
# rel_mass = df['rel_mass']
mass_eutectic = np.array(df2['mass'])
rel_mass_eutectic = mass_eutectic / mass_eutectic[0]

#%% set plot parameters
plt.rc('axes', labelsize=18, titlesize=21)
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)

#%% plot mass-loss
plt.rc('lines', markersize=12)

plt.figure(figsize=[10,8])
plt.title('50:50 $KCl$-$MgCl_2$, 1wt.% $EuCl_3$')
plt.xlabel('Time (min)')
plt.ylabel('Mass Remaining (%)')
plt.plot(time_5050, rel_mass_5050*100, '.', c='r')
plt.savefig(f'{OUT_PATH}/50-50_mass-loss.tif', format='tif')
plt.show()

plt.figure(figsize=[10,8])
plt.title('Eutectic $KCl$-$MgCl_2$, 1wt.% $EuCl_3$')
plt.xlabel('Time (min)')
plt.ylabel('Mass Remaining (%)')
plt.plot(time_eutectic, rel_mass_eutectic*100, '.', c='k')
plt.savefig(f'{OUT_PATH}/Eutectic_mass-loss.tif', format='tif')
plt.show()

plt.figure(figsize=[10,8])
plt.xlabel('Time (min)')
plt.ylabel('Mass Remaining (%)')
plt.plot(time_5050, rel_mass_5050*100, '.', c='r', label='50:50 $KCl$-$MgCl_2$')
plt.plot(time_eutectic, rel_mass_eutectic*100, '.', c='k', label='eutectic $KCl$-$MgCl_2$')
plt.legend(fontsize=15)
plt.savefig(f'{OUT_PATH}/comparison_mass-loss.tif', format='tif')
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

