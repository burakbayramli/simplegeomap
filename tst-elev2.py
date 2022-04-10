import pandas as pd
import numpy as np
from skimage.measure import block_reduce
import random, itertools
from geotiff import GeoTiff 
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

tiff_file = "alwdgg.tif"

#area_box = ((25,34), (46,45))
#area_box = ((41,37), (44,39))
area_box = ((44,39), (45,40))


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
    print (np.max(arr.flatten()))
    idx = np.random.choice(range(X.shape[0]*X.shape[1]),size=NX*NY)
    X2 = X.flatten()[idx].reshape(NX,NY)
    Y2 = Y.flatten()[idx].reshape(NX,NY)
    arr2 = arr.flatten()[idx].reshape(NX,NY)
    rbfi = Rbf(X2,Y2,arr2)
else:
    print (np.max(arr.flatten()))
    rbfi = Rbf(X,Y,arr)
    
arrhat = rbfi(X,Y)
arrhat[arrhat<0] = 0.0
#CS=plt.contour(X,Y,arrhat,levels=[500,1000,2000,2500,3000,4000])
#CS=plt.contour(X,Y,arrhat,levels=[3000,4000])
CS=plt.contour(X,Y,arrhat)
plt.clabel(CS, fontsize=10, inline=1)
#plt.plot(44.31390310047508,39.69575835416715,'rd')
plt.plot(44.300984817675946,39.702322460701524,'rd')
plt.savefig('out4.png')
