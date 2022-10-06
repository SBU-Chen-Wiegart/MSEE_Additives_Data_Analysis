# MSEE_Additives_Data_Analysis
Collection of Python scripts for analyzing MSEE additives data. Many scripts can be used for more general analysis of 3D image data, especially tomography data such as that from FXI beamline of NSLS-II.

Most scripts follow similar format:  
IN_PATH (or in_path) = directory containing series of images to be processed  
OUT_PATH (or out_path) = directory where processed images will be saved  
for loop over the scans/files within IN_PATH which processes each image  

Required packages:  
numpy  
matplotlib  
pandas  
scipy  
scikit-image  
opencv  
