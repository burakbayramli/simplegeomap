import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import shapefile

def plot_country():

    sf = shapefile.Reader("TM_WORLD_BORDERS-0.3.shp", encoding = "ISO8859-1")
    r = sf.records()
    countries = sf.shapes()
    for idx in range(len(countries)):
        country = countries[idx]
        name = r[idx]
        bounds = list(country.parts) + [len(country.points)]
        plt.xlim(20,50)
        plt.ylim(20,50)
        for previous, current in zip(bounds, bounds[1:]):    
            geo = [[x[0],x[1]] for x in country.points[previous:current]]
            if len(geo) < 1: continue
            geo = np.array(geo)
            if geo.shape[0] > 0:
                plt.plot(geo[:,0],geo[:,1],'b')
                
    plt.savefig('out1.png')


plot_country()


                
