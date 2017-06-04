import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import numpy as np

# Choose colormap
cmap = plt.cm.inferno

# Get the colormap colors
cmap_size = cmap.N
alpha_size = cmap.N
my_cmap = cmap(np.arange(cmap_size))
alpha_val = np.linspace(0, 1, alpha_size)

bivariate_cm = [np.array([my_cmap[i], ]*alpha_size) for i in range(cmap_size)]

for arr in bivariate_cm:
    arr[:, -1] = alpha_val

# Make a figure and axes with dimensions as desired.
fig = plt.figure()

#  rect [left, bottom, width, height]
cmap_N = 256
fig_size = plt.rcParams['figure.figsize']
width = 0.0038

axes_arr = [fig.add_axes([width*(1+i), 0.05, width, 0.9]) for i in range(cmap_N)]

for ax, cmap in zip(axes_arr, bivariate_cm):
    my_cmap = ListedColormap(cmap)
    cb = mpl.colorbar.ColorbarBase(ax, cmap=my_cmap)
    cb.outline.set_visible(False)
    cb.set_ticks([])

plt.show()
