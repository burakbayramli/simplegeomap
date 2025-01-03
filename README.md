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

clat,clon=41,14; zoom = 1.0

simplegeomap.plot_countries(clat,clon,zoom)

simplegeomap.plot_water(clat,clon,zoom)

simplegeomap.plot_elevation(clat,clon,zoom)

plt.savefig('map.jpg',quality=30)
```

![](map.jpg)

Regions can be plotted by passing polygon points in an N x 2 numpy array to the
`plot_region` call. This call assumes the last point connects to the first point,
hence creating a closed region. If we want the points to represent a curve/line,
without the end connecting to its beginning, then `plot_line` can be used.

## Datafiles, Preprocessing

Preprocessing when necessary has already been executed, their result
are already placed inside the package. Listed below are sources, steps
just in case, if one wants to preprocess with different parameters, so on.

Country Border Datafile comes from [here](https://thematicmapping.org/downloads/world_borders.php)

For water regions the lake/river data from [NOAA](https://www.ngdc.noaa.gov/mgg/shorelines/data/gshhg/latest/)
was used.

In order to regenerate the water file from its raw sources, see
`util.preprocess_GSHHS`, assuming the data is unzipped under `/tmp` it
will recreate the datafile.

[Cities](https://github.com/dr5hn/countries-states-cities-database/blob/master/csv/cities.csv).
The only addition here was a new column for asciified city names using
`import unidecode; unidecode.unidecode(..)`. 

Elevation Data is taken from NOAA, datafile is from [here](https://www.ngdc.noaa.gov/mgg/topo/gltiles.html)
download "all files in on zip", extract zip under /tmp, then run `util.preprocess_GLOBE`.
GLOBE means Global Land One-kilometer Base Elevation, meaning the resolution of
each grid is 1 km square.

## Links

[Programming Articles on Python, IT](https://burakbayramli.github.io/dersblog/sk/)

[Linear Algebra, Calculus](https://burakbayramli.github.io/dersblog/)

