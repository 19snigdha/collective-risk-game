
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d

import matplotlib.pyplot as plt


# fig = plt.figure()
# ax = plt.axes(projection='3d')

# X = [194,179,146,177,92,174,187,175,160]
# Y = [0,0,0.5,0.5,1,1,0,0.5,1]
# Z = np.array(Z)
# Z = Z.reshape((len(X), len(Y)))

# ax.contour3D(X, Y, Z, 50, cmap='binary')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')

fig = plt.figure()

ax = plt.axes(projection='3d')


PX1 = [194,179,146,177,92,174,187,175,160]
#PX2 = [200,185,38,179,118,181,192,118,156]
Y = [0,0,0.5,0.5,1,1,0,0.5,1]
Z = [0.1,0.9,0.1,0.9,0.1,0.9,0.5,0.5,0.5]

ax.scatter(PX1,Y,Z,c='r',marker='o')

ax.set_xlabel('Monetory Unit')
ax.set_ylabel('Risk Probability')
ax.set_zlabel('Cooperation Probability')

plt.show()