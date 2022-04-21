from pygeodesy.sphericalNvector import LatLon, perimeterOf, meanOf
import matplotlib.pyplot as plt
import numpy as np
import shapefile
import pandas as pd

def preprocess_GSHHS():

    files = [("lake","/tmp/gshhg-shp-2.3.7/GSHHS_shp/f/GSHHS_f_L2.shp"),
             ("river1","/tmp/gshhg-shp-2.3.7/WDBII_shp/f/WDBII_river_f_L02.shp"),
             ("river2","/tmp/gshhg-shp-2.3.7/WDBII_shp/f/WDBII_river_f_L03.shp"),
             ("river3","/tmp/gshhg-shp-2.3.7/WDBII_shp/f/WDBII_river_f_L04.shp")
    ]
    
    res = []
    for type,file in files:
        print (file)
        sf = shapefile.Reader(file)
        r = sf.records()
        countries = sf.shapes()

        print (len(countries))
        for idx in range(len(countries)):
            country = countries[idx]
            name = r[idx]
            print (name)
            print (len(country.parts))
            bounds = list(country.parts) + [len(country.points)]
            for (previous, current) in zip(bounds, bounds[1:]):
                geo = [[x[1],x[0]] for x in country.points[previous:current]]
                if len(geo) < 1: continue
                latlons = [LatLon(a[0],a[1]) for a in geo]
                per = np.round(perimeterOf(latlons, radius=6371),2)
                mid = meanOf(latlons)
                res.append([mid.lat,mid.lon,per,type,geo])

    df = pd.DataFrame(res)
    df.columns = ['lat','lon','perimeter','type','polygon']
    df.to_csv('/tmp/lake_river.csv',index=None)


if __name__ == "__main__": 
    
    preprocess_GSHHS()
    
