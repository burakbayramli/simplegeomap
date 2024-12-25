import matplotlib.pyplot as plt, os, numpy as np
import zipfile, csv, io, simplegeomap as sm

tmp = "/tmp"
if "TMPDIR" in os.environ: tmp = os.environ['TMPDIR']

def test_main():
    print ('test main')
    clat,clon = 40.5886754166493, 29.913405195349764
    zoom = 0.1
    fig, ax = plt.subplots() 
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    sm.plot_water(clat,clon,zoom=zoom,ax=ax)
    ax.plot(clon,clat,'rd')
    plt.savefig(tmp + '/out1.jpg')

def test_elev1():
    print ('test elev1')
    clat,clon=39, 35; zoom = 1.0
    fig, ax = plt.subplots() 
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    sm.plot_elevation(clat,clon,zoom=zoom,ax=ax)
    plt.savefig(tmp + '/out2.jpg')

def test_elev2():
    print ('test elev2')
    plt.figure()
    fig, ax = plt.subplots() 
    clat,clon = 39, 43; zoom = 0.12
    sm.plot_elevation(clat,clon,zoom=zoom,ax=ax)
    ax.plot(clon,clat,'rd')
    ax.plot(44.302573784228805,39.703693452167236,'rd')
    ax.plot(43.87012512474575,39.35428959913199,'rd')
    plt.savefig(tmp + '/out3.jpg')
    
def test_elev3():
    print ('test elev3')
    plt.figure()
    fig, ax = plt.subplots() 
    clat,clon=40.933112491070595, 29.117705476265918; zoom = 0.02
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax)
    sm.plot_elevation(clat,clon,zoom=zoom,levels=[50,100,130,150,180,200],ax=ax)
    #sm.plot_elevation(clat,clon,zoom=zoom,ax=ax)
    plt.savefig(tmp + '/out4.jpg')

def test_elev4():
    print ('test elev4')
    #clat,clon = 39.703693452167236,44.302573784228805
    clat,clon = 41.0843,29.03588
    print ('before cache')
    res = sm.elev_at(clat,clon)
    print (res)
    print ('after cache')
    res = sm.elev_at(clat,clon)
    print (res)
    
def test_cities():
    print ('test cities')
    for i,city in enumerate(['new york city','chicago']):
        c = sm.find_city(city,"United States")
        if (len(c)==1): print (c)
    for i,city in enumerate(['souda','chalkidona']):
        c = sm.find_city(city,"Greece")
        if (len(c)==1): print (c)

def test_country_color():
    print ('test country color')
    plt.figure()
    d = sm.get_country_name_iso3()
    print (d['Turkey'], d['Greece'])
    clat,clon = 40.5886754166493, 29.913405195349764
    zoom = 2.0
    colors = {"TUR": "red", "GRC": "yellow"}
    sm.plot_countries(clat,clon,zoom,country_color=colors)
    plt.savefig(tmp + '/out5.jpg')

def test_subplot1():
    print ('test subplot1')
    zoom = 1
    fig, ax = plt.subplots(2)
    sm.plot_countries(40,20,zoom=zoom,ax=ax[0])
    sm.plot_countries(40,30,zoom=zoom,ax=ax[1])
    plt.savefig(tmp + '/out6.jpg')

def test_continent():
    print ('test continent')
    zoom = 20
    sm.plot_continents(0,0,20)
    plt.savefig(tmp + '/out7.jpg')
        
def test_force_inc():
    print ('test force inc')
    zoom = 0.5
    sm.plot_countries(49,36,zoom=zoom,force_include=['RUS'])
    plt.savefig(tmp + '/out8.jpg')

def test_color():
    print ('test color')
    fig, ax = plt.subplots()
    sm.plot_countries(40,29,zoom=1,incolor='papayawhip',outcolor='azure',ax=ax)
    plt.savefig(tmp + '/out9-1.jpg')

def test_lines():
    pts = np.array([[40,10],[43,10], [43,15]])
    fig, ax = plt.subplots()
    sm.plot_countries(clat=40,clon=10,ax=ax,zoom=1.0)
    sm.plot_line(pts,ax,color='red')
    plt.savefig(tmp + '/out10-1.jpg')
    fig, ax = plt.subplots()
    sm.plot_countries(clat=40,clon=10,ax=ax,zoom=1.0)
    sm.plot_poly(pts,ax,color='red')
    plt.savefig(tmp + '/out10-2.jpg')

def test_ukr():
    clat,clon = 48, 35
    zoom = 1.0
    fig, ax = plt.subplots() 
    sm.plot_countries(clat,clon,zoom=zoom,ax=ax,force_include=['RUS'])
    sm.plot_water(clat,clon,zoom=zoom,ax=ax)
    plt.savefig('/tmp/sm_09.jpg',quality=40)    
    
        
if __name__ == "__main__":

    # test_main()
    # test_elev1()
    # test_elev2()
    # test_elev3()
    # test_elev4()
    # test_cities()
    # test_country_color()
    # test_subplot1()
    # test_continent()
    # test_force_inc()
    # test_color()
    # test_lines()
    test_ukr()
        
