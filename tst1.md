

```python
import pygeodesy
print(pygeodesy. __version__)
```

```text
21.08.31
```



```python
import simplemap

clat,clon=10,30
plt = simplemap.plot_countries(clat,clon,3)
plt.plot(clon,clat,'rd')
plt.savefig('out1.png')
```

```text
Out[1]: [<matplotlib.lines.Line2D at 0x7f7e4de55e80>]
```





