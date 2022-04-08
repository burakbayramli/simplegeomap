import pandas as pd
import numpy as np
from skimage.measure import block_reduce
import random, itertools
from geotiff import GeoTiff 
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

tiff_file = "/home/burak/Downloads/dem_geotiff/DEM_geotiff/alwdgg.tif"

#area_box = ((25,34), (46,43))
area_box = ((41,37), (44,39))



g = GeoTiff(tiff_file, crs_code=4326, as_crs=4326,  band=0)
arr = g.read_box(area_box)
arr = np.flip(arr,axis=0)
print (arr.shape)

X = np.linspace(area_box[0][0],area_box[1][0],arr.shape[1])
Y = np.linspace(area_box[0][1],area_box[1][1],arr.shape[0])

X,Y = np.meshgrid(X,Y)

if arr.shape[1]>100:
    NX,NY=15,20
    np.random.seed(0)
    idx = np.random.choice(range(X.shape[0]*X.shape[1]),size=NX*NY)
    X2 = X.flatten()[idx].reshape(NX,NY)
    Y2 = Y.flatten()[idx].reshape(NX,NY)
    arr2 = arr.flatten()[idx].reshape(NX,NY)
    rbfi = Rbf(X2,Y2,arr2)
else:
    rbfi = Rbf(X,Y,arr)
    
arrhat = rbfi(X,Y)
arrhat[arrhat<0] = 0.0
CS=plt.contour(X,Y,arrhat,levels=[500,1000,2000,2500,3000])
plt.clabel(CS, fontsize=10, inline=1)
plt.savefig('out4.png')
