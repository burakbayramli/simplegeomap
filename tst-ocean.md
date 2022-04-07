

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

