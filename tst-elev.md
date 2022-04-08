
36,26 sol alt
42, 44 sag ust 


```python
from geotiff import GeoTiff 
import matplotlib.pyplot as plt

tiff_file = "/home/burak/Downloads/dem_geotiff/DEM_geotiff/alwdgg.tif"

area_box = ((26,36), (46,43))

g = GeoTiff(tiff_file, crs_code=4326, as_crs=4326,  band=0)
arr = g.read_box(area_box)
arr = np.flip(arr,axis=0)
print (arr.shape)

X = np.linspace(area_box[0][0],area_box[1][0],239)
Y = np.linspace(area_box[0][1],area_box[1][1],83)
X,Y = np.meshgrid(X,Y)

CS=plt.contour(X,Y,arr,levels=[2000,3000])
plt.clabel(CS, fontsize=10, inline=1)
plt.savefig('out4.png')
```

```text
(83, 239)
```










