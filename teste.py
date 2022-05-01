import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib as mpl

import numpy as np
import matplotlib.pyplot


fig = plt.figure()
ax = plt.axes(projection='3d')

zline = [0, 1, 2, 3, 4, 5]
xline = [0, 1, 2, 3, 4, 5]
yline = [0, 1, 2, 3, 4, 5]

ax.plot3D(xline, yline, zline, 'gray')

plt.show()