# richardsplot #

Matplotlib plotting standards for Gordon Richards' group

### Setup ###

```
#!bash
pip install richardsplot
```

### Usage ###

In Python, whenever `matplotlib` is being used, do

```
#!python
import richardsplot
```

Your `rcParams` variable will change to meet the standards.

Some matplotlib color cycles are also defined. To use them, do one of the following:

```
#!python
ax.set_color_cycle(richardsplot.csdark)
ax.set_color_cycle(richardsplot.cspurple)
ax.set_color_cycle(richardsplot.csorange)
```

Where `ax` is the matplotlib axis instance of interest.


For documentation on Palettable see:
https://jiffyclub.github.io/palettable/#finding-palettes
