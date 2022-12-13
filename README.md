# MSEE_Additives_Data_Analysis
Collection of Python scripts for analyzing MSEE additives data. Many scripts can be used for more general analysis of 3D image data, especially tomography data such as that from FXI beamline of NSLS-II.

Most scripts follow similar format:  
`IN_PATH` (or `in_path`) = directory containing series of files/images to be processed  
`OUT_PATH` (or `out_path`) = directory where processed files/images will be saved  
The script then loops over all files in the IN_PATH directory, performs processing, and saves output to OUT_PATH.  
Scripts are intended to be ran in spyder with figures plotted in console window. Otherwise many figure windows may pop-up during processing. 

## Example workflow
`crop_tomo.py` &rarr; `align3D.py` &rarr; `segmentation.py` &rarr; `Contour.py`  
`crop_tomo.py` first reads reconstructed tomography data from h5 files, crops to specified range, and saves outputs 3D tif files.  
`align3D.py` uses Mingyuan Ge's code to perform image alignment (a.k.a. volume registration) on cropped 3D images.  
`segmentation.py` segments data into material and non-material pixels based on image histogram. Outputs saved as binary images.  
`Contour.py` draws mask over sample to separate data into material, pores, and outer environment. Outputs saved as ternary images.

Volume loss for series of images can be calculated using `vol_loss.py` on the segmented binary images.  
Porosity can likewise be calculated using `porosity.py` on ternary images from `Contour.py`.

## Required packages
h5py  
numpy  
matplotlib  
pandas  
scipy  
scikit-image  
opencv  


#12/12/2022  Script from Xiaoyang

1. XANES plot: plotXANES_moltensalt_Additive.ipynb
2. TEM pixel Cr (or Ni) and O (or Cl) correlation: plot_at_correlation.py
3. extract 2D slices
