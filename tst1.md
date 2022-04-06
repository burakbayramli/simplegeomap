

```python
import simplemap

clat,clon=10,30
plt = simplemap.plot_countries(clat,clon,3)
plt.plot(clon,clat,'rd')
plt.savefig('out1.png')
```


