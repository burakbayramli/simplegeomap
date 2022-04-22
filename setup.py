import setuptools

setuptools.setup(
    name='simplegeomap',    
    version='0.0.1',
    description="Simple offline map plot utility, for country borders, elevation, water",
    long_description="Given lat,lon,zoom level simply plot all country boundaries, rivers, lakes, elevation contour lines that fit on the map, using offline data",
    long_description_content_type="text/markdown",    
    install_requires=['pandas','pygeodesy','matplotlib','numpy','pyshp'],
    include_package_data=True,
    url="https://github.com/burakbayramli/simplegeomap",
    author="Burak Bayramli",
    package_data={
        "": ["*.dbf", "*.shp","*.zip","*.tif"]
    },
    packages=setuptools.find_packages(),
 )
