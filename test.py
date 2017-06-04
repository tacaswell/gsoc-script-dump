import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import numpy as np
from pylab import rcParams

rcParams['figure.figsize'] = 4, 4
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

nrows = 4
x = y = np.linspace(-5, 5, nrows)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)/R

dx = abs(Z[0][1] - Z[0][0])
gx, gy = np.gradient(Z, dx, dx)

my_cmap = ListedColormap(bivariate_cm[0])

# fig, axes = plt.subplots(nrows=1)
# axes.imshow(Z, origin='lower')

normz = mpl.colors.Normalize(Z.min(), Z.max())
normgx = mpl.colors.Normalize(gx.min(), gx.max())

temp = Z
gx = np.array(normgx(gx)*255, dtype='int64')
Z = np.array(normz(Z)*255, dtype='int64')
print Z

def plot_color_gradients(nrows):
    colarr = bivariate_cm[255]
    for i in range(256):
        colarr[i][-1] = 0
    """
    for i in range(256):
        colarr[i] = bivariate_cm[i][255]
    print colarr[68]
    cmap = plt.cm.viridis

    # Get the colormap colors
    cmap_size = cmap.N
    alpha_size = cmap.N
    my_cmap = cmap(np.arange(cmap_size))

    for col1, col2 in zip(my_cmap, colarr):
        print str(col1) + " " + str(col2)
        for i in range(4):
            if col1[i] != col2[i]:
                print "HOAXXXXX"
    """
    fig, axes = plt.subplots(nrows=nrows)

    fig.subplots_adjust(top=0.999, bottom=0.001, left=0.001, right=0.999, hspace = 0.1, wspace = 0)

    for ax, zarr, gxarr, temparr in zip(axes, Z, gx, temp):
        idx = 0
        for zele, gxele in zip(zarr, gxarr):
            print zele, gxele
            gxele = 255
            if idx <= 0:
                colarr[idx] = bivariate_cm[zele][gxele]
            else:
                colarr[idx] = bivariate_cm[0][0]
            print colarr[idx]
            idx = idx+1

        my_cmap = ListedColormap(colarr)

        gradient = zarr
        gradient = np.vstack((gradient, gradient))
        ax.imshow(gradient, aspect='auto', cmap=my_cmap)
        break
    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

plot_color_gradients(nrows)

plt.show()
