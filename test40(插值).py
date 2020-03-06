import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
import math

"""
牛顿插值法
插值的函数表为
xi           4，         5，            6，            7，           8，         
f(xi)   437084.22,    511812.73,   549242.26,    592063.64,    633024.30,  
"""
y = [i/1024 for i in [437084.22, 511812.73, 549242.26, 592063.64, 633024.30]]
X = [4, 5, 6, 7, 8]

f11 = y[1] - y[0]
f12 = y[2] - y[1]
f13 = y[3] - y[2]
f14 = y[4] - y[3]
print("一阶插商", f11, f12, f13)
f21 = (f12 - f11) / 2
f22 = (f13 - f12) / 2
f23 = (f14 - f13) / 2
print("二阶差商", f21, f22)
f31 = f22 - f21
f32 = f23 - f22
print("三阶差商", f31)
f41 = f32 - f31
print("四阶差商", f41)

from sympy import *

x = symbols('x')
Nx = y[0] + (x - X[0]) * f11 + (x - X[0]) * (x - X[1]) * f21 + (x - X[0]) * (x - X[1]) * (x - X[2]) * f31 + (
            x - X[0]) * (x - X[1]) * (x - X[2]) * (x - X[3]) * f41
y1 = [Nx.evalf(subs={x: 4}), Nx.evalf(subs={x: 5}), Nx.evalf(subs={x: 6}), Nx.evalf(subs={x: 7}, ),
      Nx.evalf(subs={x: 8}, )]
print(y1)
print(y)
y2=[Nx.evalf(subs={x: i}) for i in np.arange(X[0],X[-1]+2,0.1)]
plt.plot(X, y1, 'r.')
plt.plot(np.arange(X[0],X[-1]+2,0.1), y2, 'g-')
plt.plot(X, y, 'b.')
plt.show()




