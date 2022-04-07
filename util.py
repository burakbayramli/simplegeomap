from pygeodesy.sphericalNvector import LatLon
import matplotlib.pyplot as plt
import numpy as np
import shapefile
import pandas as pd

sf = shapefile.Reader("/home/burak/Downloads/GSHHS_f_L2.shp")
r = sf.records()
countries = sf.shapes()

print (len(countries))
res = []
for idx in range(len(countries)):
    country = countries[idx]
    name = r[idx]
    print (name)
    print (len(country.parts))
    bounds = list(country.parts) + [len(country.points)]
    for (previous, current) in zip(bounds, bounds[1:]):
        geo = [[x[0],x[1]] for x in country.points[previous:current]]
        if len(geo) < 1: continue
        geo = np.array(geo)
        print (len(geo))
        
