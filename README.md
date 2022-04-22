# SimpleGeoMap

Given a center latitude, longitude and a zoom level simply plot all
country boundaries, rivers, lakes, elevation contour lines that fit on
the map, using offline data. This package is self-contained, it does
not need net connectivity to get its data.

Each land feature can be enabled through its API call. 

## Installation

`pip install simplegeomap`

## How To Use

```python
import matplotlib.pyplot as plt
import simplegeomap

clat,clon=41,14

simplegeomap.plot_countries(clat,clon,zoom)

simplegeomap.plot_water(clat,clon,zoom)

simplegeomap.plot_elevation(clat,clon,zoom)

plt.savefig('map.png')
```

Regions can be plotted by passing polygon points in an N x 2 numpy array to the
`plot_region` call.


## Datafiles, Preprocessing

Country Border Datafile comes from [here](https://thematicmapping.org/downloads/world_borders.php)

Lake data from [NOAA](https://www.ngdc.noaa.gov/mgg/shorelines/data/gshhg/latest/)

[Cities](https://github.com/dr5hn/countries-states-cities-database/blob/master/csv/cities.csv)

In order to regenerate the water data from its raw sources, see
`util.preprocess_GSHHS`, assuming the data is unzipped under `/tmp` it
will recreate the datafile.


