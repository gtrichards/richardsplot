import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import palettable
import richardsplot as rplot

x = np.random.random(size=1000)*6000+3000
y = np.random.normal(loc=0,scale=0.25,size=1000)*1.0e-17

ind = np.argsort(x)
xplot = x[ind]
yplot = y[ind]/1.0e-17

plt.figure(figsize=(8,8))
plt.xlim(3000,9000)
#plt.ylim(-1,1)
plt.xlabel("Wavelength ($\mu$m)")
plt.ylabel("Flux Density ($10^{-17}$ ergs s$^{-1}$ cm$^{-2}$ \AA$^{-1}$)")
plt.plot(xplot,yplot,color=rplot.csdark[2],label="Test1")
#plt.show()
plt.tight_layout(pad=0.1)
plt.savefig("testplot1.pdf")
