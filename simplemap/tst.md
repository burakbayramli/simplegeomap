

```python
import simplemap
#clat,clon=10,30
clat,clon=39.06084392603182, 34.274201977299; zoom = 1.0
#clat,clon=40.074983672293875, 29.247377603127884; zoom = 0.3

simplemap.plot_countries(clat,clon,zoom)
#simplemap.plot_water(clat,clon,zoom)
simplemap.plot_elevation(clat,clon,zoom)
plt.plot(clon,clat,'rd')
plt.savefig('out1.png')
```

```text
2000.0
((20.27992724851315, 25.455316274188682), (54.24260864298383, 50.25456117787088))
(297, 406)
```





