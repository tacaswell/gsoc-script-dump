from matplotlib import cm
from matplotlib.colors import makeMappingArray, rgb_to_hsv, hsv_to_rgb
import numpy as np
import matplotlib.pyplot as plt

seisbar = cm.get_cmap('RdBu')

ncolours = 256
seis_array = makeMappingArray(ncolours, seisbar)
np.shape(seis_array)

color_arr = seis_array[np.newaxis, :]
color_arr = color_arr[:, :, :-1]

colour_roll = np.rollaxis(color_arr, 1)
seis_rgb_mtx = np.tile(colour_roll, (256, 1))
np.shape(seis_rgb_mtx)

seis_hsv = rgb_to_hsv(seis_rgb_mtx)
hues, lightness = np.mgrid[0:1:256j, 0:1.0:256j]
seis_hsv[:, :, 2] *= lightness

RGB = hsv_to_rgb(seis_hsv)

fig = plt.figure(figsize=(4, 5))
ax = fig.add_subplot(111, axisbg='k')
ax.imshow(RGB, origin="lower", extent=[0, 1, 0, 1])

plt.show()
