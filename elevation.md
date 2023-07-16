# Elevation Data

The data for this feature is contained in seperate data files for each
"tile". The tiles are shown here,

https://www.ngdc.noaa.gov/mgg/topo/gltiles.html

In order to generate the required npz files download all files in on
zip, extract zip under /tmp, then run `preprocess_GLOBE`, place the
resulting npz file under the `simplegeomap` directory under your
`site-packages` and the code should run without problems.

