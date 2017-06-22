import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.colors as colors
# rcParams['figure.figsize'] = 4, 4
# Choose colormap

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
cmap1 = cmap4
cmap = cmap3

# Get the colormap colors
cmap_size = cmap.N
alpha_size = cmap.N

my_cmap = cmap(np.arange(cmap_size))
my_cmap1 = cmap1(np.arange(cmap_size))

bivariate_cm = [np.array([my_cmap[i], ]*alpha_size) for i in range(cmap_size)]

weight1 = 2
weight2 = 2

fract = 0.5
for color, bb in zip(my_cmap1, range(256)):
    for cc in range(256):
        for aa in range(4):
                bivariate_cm[cc][bb][aa] = (bivariate_cm[cc][bb][aa] - color[aa]) * fract + color[aa]

print bivariate_cm[0][0]
print bivariate_cm[255][0]
print bivariate_cm[0][255]
print bivariate_cm[255][255]
"""
for aa in range(256):
    sat = 0
    for bb in range(256):
        temp = bivariate_cm[aa][bb][:-1]
        sat += 0.0001
        hsv = colors.rgb_to_hsv(temp)
        hsv[1] = hsv[1] + sat
        temp = colors.hsv_to_rgb(hsv)
        bivariate_cm[aa][bb][0] = temp[0]
        bivariate_cm[aa][bb][1] = temp[1]
        bivariate_cm[aa][bb][2] = temp[2]
"""

nrows = 256
x = y = np.linspace(-5, 5, nrows)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)/R
# Z = np.sin(X) * np.sin(Y)
dx = abs(X[0][1] - X[0][0])
gx, gy = np.gradient(Z, dx, dx)

my_cmap = ListedColormap(bivariate_cm[0])

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
                colarr[jdx][idx] = bivariate_cm[zele][gxele]
            else:
                colarr[jdx][idx] = bivariate_cm[zele][G]
            # print bivariate_cm[zele][gxele]
            idx = idx+1
        jdx = jdx+1


fig, axes = plt.subplots(ncols=2, nrows=1)

"""
axes[0][0].imshow(Z, origin='lower')
axes[0][0].set_title('plot of Z = sin(R)/R where R = sqrt(X^2 + Y^2)')

axes[0][1].imshow(gx, origin='lower')
axes[0][1].set_title('plot of gradient of gx = sin(R)/R with X')
"""

plot_color_gradients(nrows, -1)
axes[0].imshow(colarr, origin='lower')
axes[0].set_title('sin(R)/R plot with 2d cmap')

axes[1].imshow(bivariate_cm, origin='lower')
axes[1].set_title('colorbar')

for ax in axes.flat:
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.set_axis_off()

plt.tight_layout()
plt.show()
