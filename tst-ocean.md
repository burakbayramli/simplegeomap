



```python
import simplemap
clat,clon=39.06084392603182, 34.274201977299
simplemap.plot_water(clat,clon,3,plt)
```

```python
import pandas as pd, zipfile
from pygeodesy.sphericalNvector import LatLon
with zipfile.ZipFile('/home/burak/Downloads/lake_river.zip', 'r') as z:
      df =  pd.read_csv(z.open('lake_river.csv'))

df = df[df['type'] == 'lake']
df = df[df['perimeter'] > 400]
clat,clon=39.06084392603182, 34.274201977299
p1 = LatLon(clat,clon) 
dist = df.apply(lambda x: p1.distanceTo(LatLon(x['lat'],x['lon']))/1000.0, axis=1)
print (dist)
```

```text
1       1466.055935
2       8836.976175
3       4480.322704
4       2239.420633
5       5053.736916
           ...     
6636    6767.882285
6637    8559.598930
6638    4304.898401
6639    4411.553947
6641    7025.123815
Length: 156, dtype: float64
```


```python
MAX = 20
zoom = 1
CENTER_DIST = (40000. / MAX)*(zoom+1)
df2 = df[dist < CENTER_DIST]
print (len(df))
print (len(df2))
```

```text
156
44
```




```python
import pandas as pd

df = pd.read_csv('/tmp/out.csv')
print (df.columns)
print (df.index)
```

```text
Index(['lat', 'lon', 'polygon'], dtype='object')
RangeIndex(start=0, stop=1, step=1)
```


```python
import json
coords = df.loc[0,'polygon']
print (type(coords))
coords = json.loads(coords)
print (type(coords))
print (coords[0])
```

```text
<class 'str'>
<class 'list'>
[18.145286, 145.762963]
```












```python
from pygeodesy.sphericalNvector import LatLon
import matplotlib.pyplot as plt
import numpy as np
import shapefile

sf = shapefile.Reader("/home/burak/Downloads/GSHHS_f_L2.shp")
r = sf.records()
countries = sf.shapes()
```

```python
print (len(countries))
idx = 5
country = countries[idx]
name = r[idx]
print (name)
print (len(country.parts))
```

```text
6660
Record #5: ['180510', 2, 'WDBII', 1, -1, 32732.9896601]
1
```

```python
print (len(countries))
idx = 1
name = r[idx]
print (name)
print (len(country.parts))
country = countries[idx]
bounds = list(country.parts) + [len(country.points)]
for (previous, current) in zip(bounds, bounds[1:]):
   geo = [[x[0],x[1]] for x in country.points[previous:current]]
   if len(geo) < 1: continue
   geo = np.array(geo)
   plt.fill(geo[:,0],geo[:,1],'lightblue',alpha=0.4)

plt.savefig('out2.png')
```

```text
6660
Record #1: ['180506', 2, 'WDBII', 0, -1, 397052.350619]
1
```















```python
from pygeodesy.sphericalNvector import LatLon
b = LatLon(45, 1), LatLon(45, 2), LatLon(46, 2), LatLon(46, 1)
nvecs = np.array([a.toNvector() for a in b])
print (nvecs)
mid = nvecs.mean().toLatLon()
print (mid.lat, mid.lon)
```

```text
[Nvector(0.707, 0.01234, 0.70711) Nvector(0.70668, 0.02468, 0.70711)
 Nvector(0.69424, 0.02424, 0.71934) Nvector(0.69455, 0.01212, 0.71934)]
45.50109067812444 1.5
<class 'pygeodesy.sphericalNvector.LatLon'>
(0.700656, 0.018347, 0.713264)
```



has good lake info
GSHHS_f_L2.shp

