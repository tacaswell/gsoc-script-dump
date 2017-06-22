import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np

name = ['air_temperature', 'surface_pressure', ' ', 'colorbar']

fig, ax = plt.subplots(2, 2)

air_temp = np.load('air_temperature.npy')
surf_pres = np.load('surface_pressure.npy')

norm_pres = colors.Normalize(surf_pres.min(), surf_pres.max())
norm_temp = colors.Normalize(air_temp.min(), air_temp.max())

air_temp = np.array(norm_temp(air_temp)*255, dtype='int64')
surf_pres = np.array(norm_pres(surf_pres)*255, dtype='int64')

ax[0][0].imshow(air_temp)
ax[0][1].imshow(surf_pres)

# create the legend:
cax = ax[1][1]
cp1 = np.linspace(0, 1, 256)
cp2 = np.linspace(0, 1, 256)
Cp1, Cp2 = np.meshgrid(cp1, cp2)
C0 = np.zeros_like(Cp1)
C3 = np.ones_like(Cp1) * 1
Legend = np.dstack((Cp2, Cp1, C0, C3))
cax.imshow(Legend, origin="lower")

colarr = np.ones(shape=air_temp.shape + (4,))

for ii in range(air_temp.shape[0]):
    for jj in range(air_temp.shape[1]):
        colarr[ii][jj] = Legend[air_temp[ii][jj]][surf_pres[ii][jj]]

ax[1][0].imshow(colarr)

for axes, titl in zip(ax.flat, name):
    axes.set_title(titl)
    axes.set_xticks([])
    axes.set_yticks([])

plt.show()