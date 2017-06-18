import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import numpy as np

# Choose colormap
cmap = plt.cm.plasma

# Get the colormap colors
cmap_size = cmap.N
alpha_size = cmap.N
my_cmap = cmap(np.arange(cmap_size))
alpha_val = np.linspace(0.3, 1, alpha_size)

bivariate_cm = [np.array([my_cmap[i], ]*alpha_size) for i in range(cmap_size)]

for arr in bivariate_cm:
    arr[:, -1] = alpha_val

nrows = 256
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

fig, ax = plt.subplots()
ax.imshow(bivariate_cm, origin='lower')
ax.set_xticks([])
ax.set_yticks([])

plt.show()
