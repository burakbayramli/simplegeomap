from pygeodesy.sphericalNvector import LatLon
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import shapefile

def plot_country3(clat,clon,zoom=7):

    MAX = 20    
    CENTER_DIST = (40000. / MAX)*(zoom+1)
    xlims = (clon+(-180./MAX)*zoom, clon+(180./MAX)*zoom)
    ylims = (clat+(-90./MAX)*zoom, clat+(90./MAX)*zoom)
    p1 = LatLon(clat, clon)

    sf = shapefile.Reader("TM_WORLD_BORDERS-0.3.shp", encoding = "ISO8859-1")
    r = sf.records()
    countries = sf.shapes()
    for idx in range(len(countries)):
        country = countries[idx]
        name = r[idx]
        lat,lon = name[10],name[9] # middle point of country
        p2 = LatLon(lat, lon)
        d = p1.distanceTo(p2)/1000.0
        if d > CENTER_DIST: continue # skip if a country is too far        
        bounds = list(country.parts) + [len(country.points)]
        plt.xlim(xlims)
        plt.ylim(ylims)
        for previous, current in zip(bounds, bounds[1:]):    
            geo = [[x[0],x[1]] for x in country.points[previous:current]]
            if len(geo) < 1: continue
            geo = np.array(geo)
            if geo.shape[0] > 0:
                plt.plot(geo[:,0],geo[:,1],'b')
                
    plt.savefig('out1.png')

plot_country3(10,30,3)
