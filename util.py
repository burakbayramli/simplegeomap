from pygeodesy.sphericalNvector import LatLon
import matplotlib.pyplot as plt
import numpy as np
import shapefile
import pandas as pd

def preprocess_GSHHS_f_L2():

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
            geo = [[x[1],x[0]] for x in country.points[previous:current]]
            if len(geo) < 1: continue
            nvecs = np.array([LatLon(a[0],a[1]).toNvector() for a in geo])
            mid = nvecs.mean().toLatLon()
            res.append([mid.lat,mid.lon,geo])

    df = pd.DataFrame(res)
    df.columns = ['lat','lon','polygon']
    df.to_csv('/tmp/GSHHS_f_L2.csv',index=None)


if __name__ == "__main__": 
    
    preprocess_GSHHS_f_L2()
    
