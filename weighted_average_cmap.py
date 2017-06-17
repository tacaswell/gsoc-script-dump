import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import numpy as np
from pylab import rcParams
import matplotlib.colors as colors

cdict = {'red':   ((0.0, 0.0, 1.0),
                   (1.0, 1.0, 1.0)),
         'blue':  ((0.0, 0.0, 1.0),
                   (1.0, 1.0, 1.0)),
         'green': ((0.0, 0.0, 1.0),
                   (1.0, 0.0, 1.0))}

cmap3 = colors.LinearSegmentedColormap('my_colormap', cdict, 256)

cdict = {'red':   ((0.0, 0.0, 1.0),
                   (1.0, 0.0, 0.0)),
         'blue':  ((0.0, 0.0, 1.0),
                   (1.0, 0.0, 1.0)),
         'green': ((0.0, 0.0, 1.0),
                   (1.0, 1.0, 1.0))}

cmap4 = colors.LinearSegmentedColormap('my_colormap', cdict, 256)
# rcParams['figure.figsize'] = 4, 4
# Choose colormap
cmap = cmap4
cmap1 = cmap3

# Get the colormap colors
cmap_size = cmap.N
alpha_size = cmap.N

my_cmap = cmap(np.arange(cmap_size))
my_cmap1 = cmap1(np.arange(cmap_size))

bivariate_cm = [np.array([my_cmap[i], ]*alpha_size) for i in range(cmap_size)]

fract = 0.5
for color, bb in zip(my_cmap1, range(256)):
    for cc in range(256):
        for aa in range(4):
                bivariate_cm[cc][bb][aa] = (bivariate_cm[cc][bb][aa] - color[aa]) * fract + color[aa]

print bivariate_cm[0][0]
print bivariate_cm[255][0]
print bivariate_cm[0][255]
print bivariate_cm[255][255]

fig, axes = plt.subplots()

axes.imshow(bivariate_cm, origin='lower')
axes.set_title('colorbar')

axes.set_xticks([])
axes.set_yticks([])
# ax.set_axis_off()

plt.tight_layout()
plt.show()
