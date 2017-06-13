import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import numpy as np
from pylab import rcParams

#rcParams['figure.figsize'] = 4, 4
# Choose colormap
cmap = plt.cm.viridis

# Get the colormap colors
cmap_size = cmap.N
alpha_size = cmap.N
my_cmap = cmap(np.arange(cmap_size))
alpha_val = np.linspace(0, 1, alpha_size)

bivariate_cm = [np.array([my_cmap[i], ]*alpha_size) for i in range(cmap_size)]

for arr in bivariate_cm:
    arr[:, -1] = alpha_val

nrows = 256
x = y = np.linspace(-5, 5, nrows)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)/R

dx = abs(Z[0][1] - Z[0][0])

gx = np.load('surface_pressure.npy')
Z = np.load('air_temperature.npy')

# fig, axes = plt.subplots(nrows=1)
# axes.imshow(Z, origin='lower')

normz = mpl.colors.Normalize(Z.min(), Z.max())
normgx = mpl.colors.Normalize(gx.min(), gx.max())

gx = np.array(normgx(gx)*255, dtype='int64')
Z = np.array(normz(Z)*255, dtype='int64')
print Z
print Z.min()
print Z.max()

print gx.min()
print gx.max()
colarr = np.ones(shape=Z.shape + (4,))

def plot_color_gradients(nrows, G):
    jdx = 0
    for zarr, gxarr in zip(Z, gx):
        idx = 0
        for zele, gxele in zip(zarr, gxarr):
            # print zele, gxele
            if G < 0:
                colarr[jdx][idx] = bivariate_cm[zele][gxele]
            else:
                colarr[jdx][idx] = bivariate_cm[zele][G]
            # print bivariate_cm[zele][gxele]
            idx = idx+1
        jdx = jdx+1


fig, axes = plt.subplots(ncols=3, nrows=2)

axes[0][0].imshow(Z, cmap='viridis')
axes[0][1].imshow(gx, cmap='viridis')

plot_color_gradients(nrows, 255)
axes[1][0].imshow(colarr)

plot_color_gradients(nrows, -1)
axes[1][1].imshow(colarr)

axes[1][2].imshow(bivariate_cm, origin='lower')

plt.show()
