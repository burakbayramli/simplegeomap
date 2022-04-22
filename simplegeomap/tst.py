import simplegeomap
import matplotlib.pyplot as plt
clat,clon=39.06084392603182, 34.274201977299; zoom = 1.0
simplegeomap.plot_countries(clat,clon,zoom)
simplegeomap.plot_water(clat,clon,zoom)
simplegeomap.plot_elevation(clat,clon,zoom)
plt.plot(clon,clat,'rd')
plt.savefig('/tmp/out1.png')
