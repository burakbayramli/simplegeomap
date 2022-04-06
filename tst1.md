


```python
import shapefile
sf = shapefile.Reader("TM_WORLD_BORDERS-0.3.shp", encoding = "ISO8859-1")

r = sf.records()
countries = sf.shapes()
idx = 1
country = countries[idx]
crec = r[idx]
lat,lon = crec[10],crec[9]
bounds = list(country.parts) + [len(country.points)]
print (lat,lon)
```

```text
28.163 2.632
```







```python
import shapefile
sf = shapefile.Reader("TM_WORLD_BORDERS-0.3.shp", encoding = "ISO8859-1")

def plot_country(countries, idx,color='r'):
   country = countries[idx]
   name = r[idx]
   print (name)
   bounds = list(country.parts) + [len(country.points)]
   print (bounds)
   for previous, current in zip(bounds, bounds[1:]):    
       geo = [[x[0],x[1]] for x in country.points[previous:current]]
       if len(geo) < 1: continue
       geo = np.array(geo)
       if geo.shape[0] > 0:
           plt.plot(geo[:,0],geo[:,1],color)

r = sf.records()
countries = sf.shapes()

plot_country(countries, 2,'r')
plot_country(countries, 4,'b')

plt.savefig('out1.png')
```

```text
Record #2: ['AJ', 'AZ', 'AZE', 31, 'Azerbaijan', 8260, 8352021, 142, 145, 47.395, 40.43]
[0, 108, 118, 131, 859, 871]
Record #4: ['AM', 'AM', 'ARM', 51, 'Armenia', 2820, 3017661, 142, 145, 44.563, 40.534]
[0, 12, 395, 408, 418]
```









