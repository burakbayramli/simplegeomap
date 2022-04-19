import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from geotiff import GeoTiff 

def plot_elevation(clat,clon,zoom):

    tiff_file = "alwdgg.tif"

    from pygeodesy.sphericalNvector import LatLon
    MAX = 20
    CENTER_DIST = (40000. / MAX)*(zoom)
    print (CENTER_DIST)
    p1 = LatLon(clat,clon)
    EARTH_RAD = 6371
    upright = p1.destination (CENTER_DIST, bearing=45, radius=EARTH_RAD)
    lowleft = p1.destination (CENTER_DIST, bearing=225, radius=EARTH_RAD)

    area_box = ((lowleft.lon, lowleft.lat),(upright.lon,upright.lat))
    print (area_box)

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

zoom=0.5
clat,clon=39.06084392603182, 34.274201977299
plot_elevation(clat,clon,zoom)

