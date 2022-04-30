from pygeodesy.sphericalNvector import LatLon
import pandas as pd, zipfile, sys, os, csv, io
import matplotlib.pyplot as plt
import numpy as np, json, shapefile
from scipy.ndimage import gaussian_filter
from .geotiff import GeoTiff

MAX = 20

def plot_water(clat,clon,zoom):
    data_dir = os.path.dirname(__file__)
    
    CENTER_DIST = (40000. / MAX)*(zoom+1)
    
    with zipfile.ZipFile(data_dir + '/lake_river.zip', 'r') as z:
        df =  pd.read_csv(z.open('lake_river.csv'))

    #df = df[df['type'] == 'lake']
    #df = df[df['perimeter'] > 100]
    p1 = LatLon(clat,clon) 
    dist = df.apply(lambda x: p1.distanceTo(LatLon(x['lat'],x['lon']))/1000.0, axis=1)
    df2 = df[dist < CENTER_DIST]
    for idx,row in df2.iterrows():
        geo = np.array(json.loads(row['polygon']))
        plt.fill(geo[:,1],geo[:,0],'blue',alpha=0.4)
   
def plot_countries(clat,clon,zoom=7,outcolor='lightblue'):

    data_dir = os.path.dirname(__file__)
    
    CENTER_DIST = (40000. / MAX)*(zoom+1)
    xlims = (clon+(-180./MAX)*zoom, clon+(180./MAX)*zoom)
    ylims = (clat+(-90./MAX)*zoom, clat+(90./MAX)*zoom)
    p1 = LatLon(clat, clon)
    plt.axes().set_facecolor(color=outcolor)
    sf = shapefile.Reader(data_dir + "/TM_WORLD_BORDERS-0.3.shp", encoding = "ISO8859-1")
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
                plt.fill(geo[:,0],geo[:,1],'lightyellow',alpha=0.5)
                plt.plot(geo[:,0],geo[:,1],'b')


def plot_elevation(clat,clon,zoom):

    data_dir = os.path.dirname(__file__)
    tiff_file = data_dir + "/alwdgg.tif"

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
    arr = arr + 1000.0 # every height seems to be this much lower

    X = np.linspace(area_box[0][0],area_box[1][0],arr.shape[1])
    Y = np.linspace(area_box[0][1],area_box[1][1],arr.shape[0])

    X,Y = np.meshgrid(X,Y)

    arr = gaussian_filter(arr, sigma=1.0)

    CS=plt.contour(X,Y,arr,cmap=plt.cm.binary)
    plt.clabel(CS, fontsize=10, inline=1)

def plot_line(regarr,color='black',linestyle='solid'):
    plt.plot(regarr[:,1],regarr[:,0],color=color,linestyle=linestyle)
       
def plot_region(regarr,color='lightgray',alpha=0.5):
    plt.fill(regarr[:,1],regarr[:,0],color=color,alpha=alpha)

def find_city(name,country):
    data_dir = os.path.dirname(__file__)
    zip_file    = zipfile.ZipFile(data_dir + '/cities.zip')
    items_file  = zip_file.open('cities.csv')
    items_file  = io.TextIOWrapper(items_file)
    rd = csv.reader(items_file)
    headers = {k: v for v, k in enumerate(next(rd))}
    res = []
    for row in rd:
        if name in row[headers['name']].lower() and \
           country==row[headers['country_name']].lower(): res.append(row)

    return res
    
       
if __name__ == "__main__": 
    
    clat,clon=39.06084392603182, 34.274201977299; zoom = 1.0
    plot_countries(clat,clon,zoom)
    #plot_water(clat,clon,zoom)
    plot_elevation(clat,clon,zoom)
    plt.plot(clon,clat,'rd')
    plt.savefig('out1.png')
