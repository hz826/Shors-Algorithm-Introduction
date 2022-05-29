import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from simple_number_theory import *

Q = 8

def f(x, y) :
    # return (1/np.sqrt(Q) if y == 1 else 0)
    return (1/np.sqrt(Q) if y == qpow(3, x, 7) else 0)

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

# fake data
_x = np.arange(Q**2)
_y = np.arange(Q)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

ax1.get_proj = lambda: np.dot(Axes3D.get_proj(ax1), np.diag([1, 1/Q, 1, 1]))

ax1.set_xticks(x)
ax1.set_yticks(y)

# print(x)
# print(y)
z = [f(x[i], y[i]) for i in range(len(x))]

bottom = np.zeros_like(z)
width = depth = 0.9
ax1.bar3d(x-width/2, y-depth/2, bottom, width, depth, z, shade=True)
plt.show()