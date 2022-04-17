from scipy.ndimage import gaussian_filter
import pandas as pd
import numpy as np
from skimage.measure import block_reduce
import random, itertools
from geotiff import GeoTiff 
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

tiff_file = "alwdgg.tif"

area_box = ((25,34), (46,43))

g = GeoTiff(tiff_file, crs_code=4326, as_crs=4326,  band=0)
arr = g.read_box(area_box)
arr = np.flip(arr,axis=0)
print (arr.shape)
arr[arr<0.0] = 0.0

X = np.linspace(area_box[0][0],area_box[1][0],arr.shape[1])
Y = np.linspace(area_box[0][1],area_box[1][1],arr.shape[0])

X,Y = np.meshgrid(X,Y)

arr = gaussian_filter(arr, sigma=1.5)

CS=plt.contour(X,Y,arr,cmap=plt.cm.Reds)
plt.clabel(CS, fontsize=10, inline=1)
plt.savefig('out4.png')
