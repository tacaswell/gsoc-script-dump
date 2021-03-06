import cmocean
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import numpy as np
from pylab import rcParams

# rcParams['figure.figsize'] = 4, 4
# Choose colormap
cmap = cmocean.cm.phase
# cmap = plt.cm.hsv

# Get the colormap colors
cmap_size = cmap.N
alpha_size = cmap.N
my_cmap = cmap(np.arange(256))
alpha_val = np.linspace(0.2, 1, alpha_size)

bivariate_cm = [np.array([my_cmap[i], ]*alpha_size) for i in range(cmap_size)]

for arr in bivariate_cm:
    arr[:, -1] = alpha_val

nrows = 256
x = y = np.linspace(-5, 5, nrows)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)/R
# Z = np.sin(X) * np.sin(Y)
dx = abs(X[0][1] - X[0][0])
gx, gy = np.gradient(Z, dx, dx)

my_cmap = ListedColormap(bivariate_cm[0])

# fig, axes = plt.subplots(nrows=1)
# axes.imshow(Z, origin='lower')

normz = mpl.colors.Normalize(Z.min(), Z.max())
normgx = mpl.colors.Normalize(gx.min(), gx.max())

gx = np.array(normgx(gx)*255, dtype='int64')
gy = np.array(normgx(gy)*255, dtype='int64')
Z = np.array(normz(Z)*255, dtype='int64')

colarr = np.ones(shape=Z.shape + (4,))

def plot_color_gradients(nrows, G):
    jdx = 0
    for zarr, gxarr in zip(Z, gx):
        idx = 0
        for zele, gxele in zip(zarr, gxarr):
            # print zele, gxele
            if G < 0:
                colarr[jdx][idx] = bivariate_cm[gxele][zele]
            else:
                colarr[jdx][idx] = bivariate_cm[G][zele]
            # print bivariate_cm[zele][gxele]
            idx = idx+1
        jdx = jdx+1


fig, axes = plt.subplots(ncols=2, nrows=1)

"""
axes[0][0].imshow(Z, origin='lower')
axes[0][0].set_title('plot of Z = sin(R)/R where R = sqrt(X^2 + Y^2)')

axes[0][1].imshow(gx, origin='lower', cmap='PiYG')
axes[0][1].set_title('plot of gradient of sinc varying with X')
"""

plot_color_gradients(nrows, -1)
axes[0].imshow(colarr, origin='lower')
axes[0].set_title('alpha varying with sin(R)/R')

axes[1].imshow(bivariate_cm, origin='lower')
axes[1].set_title('cmocean.phase and alpha')

for ax in axes.flat:
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.set_axis_off()

plt.tight_layout()
plt.show()
