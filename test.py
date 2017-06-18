import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_aspect("equal")

# create the legend:
cax = ax
cp1 = np.linspace(0, 1, 256)
cp2 = np.linspace(0, 1, 256)
Cp1, Cp2 = np.meshgrid(cp1, cp2)
C0 = np.zeros_like(Cp1)
# make RGB image, p1 to red channel, p2 to blue channel
Legend = np.dstack((Cp1, C0, Cp2))
# parameters range between 0 and 1
cax.imshow(Legend, origin="lower", extent=[0,1,0,1])
cax.set_xlabel("p1")
cax.set_ylabel("p2")
cax.set_title("2D cmap legend", fontsize=10)

plt.show()