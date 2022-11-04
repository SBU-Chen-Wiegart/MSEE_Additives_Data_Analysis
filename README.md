# MSEE_Additives_Data_Analysis
Collection of Python scripts for analyzing MSEE additives data. Many scripts can be used for more general analysis of 3D image data, especially tomography data such as that from FXI beamline of NSLS-II.

Most scripts follow similar format:  
`IN_PATH` (or `in_path`) = directory containing series of files/images to be processed  
`OUT_PATH` (or `out_path`) = directory where processed files/images will be saved  
The script then loops over all files in the IN_PATH directory, performs processing, and saves output to OUT_PATH.  
Scripts are intended to be ran in spyder with figures plotted in console window. Otherwise many figure windows may pop-up during processing. 


Required packages:
h5py  
numpy  
matplotlib  
pandas  
scipy  
scikit-image  
opencv  
