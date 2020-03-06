import numpy as np
import matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)


def func(k, b):
    return (k * 1 + b - 432.742149922) ** 2 + (k * 2 + b - 472.748708522) ** 2 + (k * 3 + b - 389.278264178) ** 2 + (
                k * 4 + b - 426.840054216) ** 2 + (k * 5 + b - 499.817123563) ** 2 + (
                       k * 6 + b - 536.369395034) ** 2 + (k * 7 + b - 578.187152618) ** 2 + (
                       k * 8 + b - 618.187792969) ** 2 + (k * 9 + b - 599.061184525) ** 2 + (
                       k * 10 + b - 646.430869067) ** 2


Z_array = []
for i in X:
    kk = []
    for j in Y:
        kk.append(func(i, j))
    Z_array.append(kk)

print(Z_array)
print('-'*20)
print(Z)
# ax.plot_wireframe(X, Y, np.array(Z_array), rstride=10, cstride=10)
# plt.show()
