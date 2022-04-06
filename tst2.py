import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import shapefile

def plot_country2(clat,clon,zoom=7):

    MAX = 20
    xlims = (clon+(-180./MAX)*zoom, clon+(180./MAX)*zoom)
    ylims = (clat+(-90./MAX)*zoom, clat+(90./MAX)*zoom)

    sf = shapefile.Reader("TM_WORLD_BORDERS-0.3.shp", encoding = "ISO8859-1")
    r = sf.records()
    countries = sf.shapes()
    for idx in range(len(countries)):
        country = countries[idx]
        name = r[idx]
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


plot_country2(10,30,3)
