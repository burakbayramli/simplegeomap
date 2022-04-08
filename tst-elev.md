

```python
import numpy as np

X = np.array(range(20)).reshape(4,5)
print (X)
Y = np.array(range(20,40)).reshape(4,5)
print (Y)
Z = np.array(range(100,120)).reshape(4,5)
print (Z)
print ('\n')
idx = np.random.choice(range(X.shape[0]*X.shape[1]),size=2*3)
X = X.flatten()[idx].reshape(2,3)
Y = Y.flatten()[idx].reshape(2,3)
Z = Z.flatten()[idx].reshape(2,3)
print (X)
print (Y)
print (Z)
```

```text
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
[[20 21 22 23 24]
 [25 26 27 28 29]
 [30 31 32 33 34]
 [35 36 37 38 39]]
[[100 101 102 103 104]
 [105 106 107 108 109]
 [110 111 112 113 114]
 [115 116 117 118 119]]


[[ 5 13 19]
 [ 7 13  2]]
[[25 33 39]
 [27 33 22]]
[[105 113 119]
 [107 113 102]]
```











