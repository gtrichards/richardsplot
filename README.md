# richardsplot #

Matplotlib plotting standards for Gordon Richards' group

### Setup ###

```
% pip install richardsplot
```

### Usage ###

In your Python script, add

```
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import palettable
import richardsplot as rplot

```

Your `rcParams` variable will change to meet the standards.


Some matplotlib color cycles are also defined. To use them, do something like one of the following:

```
plt.plot(x,y,color=rplot.csdark[2])
```
or
```
ax.set_color_cycle(rplot.csdark)
```

Where `ax` is the matplotlib axis instance of interest.


For documentation on Palettable see:
https://jiffyclub.github.io/palettable/#finding-palettes


If you want to suggest changes to the default parameters, first edit your own version and remake the test plots (currently just testplot1.py):
```
> python testplot1.py
```
then compare your new figure to testplot1.pdf and let me know why you think that your new version is better.

Please contribute additional test plots.
