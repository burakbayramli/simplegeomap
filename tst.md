

```python
import simplemap
#clat,clon=10,30
clat,clon=39.06084392603182, 34.274201977299
plt = simplemap.plot_countries(clat,clon,1)
plt.plot(clon,clat,'rd')
plt.savefig('out1.png')
plt.clf()
```






