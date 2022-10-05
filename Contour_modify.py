# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:36:14 2022

Based on code by Xiaoyin Zheng

Use convex hull method to draw contour map over sample region in 3D image data.
Contour map will be drawn over each cross-section in image stack.
Output will be saved in OUT_PATH as ternary image (region outside sample = 0,
sample material = 1, porous regions in sample = 2). 
"""

import cv2
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_otsu
import os
import glob
import scipy as sp

IN_PATH = r'/media/karenchen-wiegart/Lijie3/20210709_FXI_MSEE+/segmentation'
OUT_PATH = r'/media/karenchen-wiegart/Lijie3/20210709_FXI_MSEE+/masked'
# fn = r'seg_recon_92067_cropped.tif'
os.chdir(IN_PATH)

files = glob.glob('*.tif')


def crop3d(im, crop_size=100):
    """
    crops 3d image to middle number of slices specified 
    """
    mid_pt = int(im.shape[0] / 2)
    return im[mid_pt - int(crop_size/2): mid_pt + int(crop_size/2)]

         
def hull_convex(img_path, idx):
    
    img = io.imread(img_path)
    img = img[idx]
    # thresh = threshold_otsu(img)
    # ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    binary = img.copy()
    binary = binary.astype(np.uint8)
    plt.figure()
    plt.imshow(binary)
    
    contours, hierarchy = cv2.findContours(image=binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    # draw contours on the original image
    img_norm = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    image_copy =  img_norm.copy()
    
    # cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 0, 0), thickness=2, lineType=cv2.LINE_AA)
    
    # see the results
    # cv2.imshow('None approximation', image_copy)
    # cv2.waitKey(0)
    # cv2.imwrite('contours_none_image1.jpg', image_copy)
    # cv2.destroyAllWindows()
    # plt.imshow(image_copy-img_norm)
    
    # create hull array for convex hull points
    hull = []
    
    # calculate points for each contour
    for i in range(len(contours)):
        # creating convex hull object for each contour
        hull.append(cv2.convexHull(contours[i], False))
        
    # create an empty black image
    drawing = np.zeros((binary.shape[0], binary.shape[1]), np.uint8)
    
    # draw contours and hull points
    for i in range(len(contours)):
        # i = max_idx
        color_contours = (0, 255, 0) # green - color for contours
        color = (255, 0, 0) # blue - color for convex hull
        # draw ith contour
        # cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
        # draw ith convex hull object
        cv2.drawContours(drawing, hull, i, color, 1, 8)
        
    cv2.imshow('hull convex', drawing)
    
    # plt.figure()
    # plt.imshow(drawing+img_norm)
    
    # Find max contours
    max_idx = 0
    for i, contour in enumerate(contours):
        if len(contour)>len(contours[max_idx]):
            max_idx = i
    return hull, max_idx

def hull_convex_array(img):
    
    # thresh = threshold_otsu(img)
    # ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    # img = union.copy()
    binary = img.copy()
    binary = binary.astype(np.uint8)
    # plt.figure()
    # plt.imshow(binary)
    # plt.title('input')
    
    contours, hierarchy = cv2.findContours(image=binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    # draw contours on the original image
    img_norm = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    image_copy =  img_norm.copy()
    
    # cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 0, 0), thickness=2, lineType=cv2.LINE_AA)
    
    # see the results
    # cv2.imshow('None approximation', image_copy)
    # cv2.waitKey(0)
    # cv2.imwrite('contours_none_image1.jpg', image_copy)
    # cv2.destroyAllWindows()
    # plt.imshow(image_copy-img_norm)
    
    # create hull array for convex hull points
    hull = []
    
    # calculate points for each contour
    for i in range(len(contours)):
        # creating convex hull object for each contour
        hull.append(cv2.convexHull(contours[i], False))
        
    # create an empty black image
    drawing = np.zeros((binary.shape[0], binary.shape[1]), np.uint8)
    
    # draw contours and hull points
    for i in range(len(contours)):
        # i = max_idx
        color_contours = (0, 255, 0) # green - color for contours
        color = (255, 0, 0) # blue - color for convex hull
        # draw ith contour
        # cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
        # draw ith convex hull object
        cv2.drawContours(drawing, hull, i, color, 1, 8)
        
    cv2.imshow('hull convex', drawing)
    
    # plt.figure()
    # plt.imshow(drawing+img_norm)
    
    # Find max contours
    max_idx = 0
    for i, contour in enumerate(contours):
        if len(contour)>len(contours[max_idx]):
            max_idx = i
    return hull, max_idx


if __name__=='__main__':

    iter_num = 4    

    for fn in files:
        print(fn)
        binary = io.imread(fn)   # This should be a binary image
        mask_3d = np.zeros(binary.shape)
        
        for i in range(binary.shape[0]):
            
            # first contour iteration
            hull1, max_idx1 = hull_convex(fn, i)
            drawing = np.zeros((binary.shape[1], binary.shape[2]), np.uint8)
            cv2.drawContours(drawing, hull1, max_idx1, (255,0,0), 1, 8)
            drawing_filled = sp.ndimage.binary_fill_holes(drawing)
            
            
            # Draw max contour
            # drawing is the contour
            for j in range(iter_num):
                
                
                union = drawing_filled + binary[i]
                union = union>0
                union = sp.ndimage.binary_fill_holes(union)
                union = np.int8(union)
                
                # second contour
                hull1, max_idx1 = hull_convex_array(union)
                drawing = np.zeros((binary.shape[1], binary.shape[2]), np.uint8)
                cv2.drawContours(drawing, hull1, max_idx1, (255,0,0), 1, 8)
                drawing_filled = sp.ndimage.binary_fill_holes(drawing)
                
                temp = drawing_filled + binary[i]
                
                plt.figure()
                plt.imshow(temp)
                
                # plt.figure()
                # plt.imshow(drawing_filled)
                
                # plt.figure()
                # plt.imshow(binary[i])
            
            mask_3d[i] = drawing_filled
        
        # io.imsave('mask_3d.tiff', np.float32(mask_3d))
        masked_im = np.float32(mask_3d+binary)
        scan_id = [int(s) for s in fn.split('_') if s.isdigit()][0]
        io.imsave(f'{OUT_PATH}/{scan_id}_mask_3d_overlap.tiff', masked_im)
        
