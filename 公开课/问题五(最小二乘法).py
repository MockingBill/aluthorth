import numpy as np
import scipy as sp
from scipy.optimize import leastsq

# 输入样本标签Y
Yi = np.array([432.742149922, 472.748708522, 389.278264178, 426.840054216, 499.817123563, 536.369395034, 578.187152618,
               618.187792969, 599.061184525, 646.430869067])
# 输入样本特征X
Xi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# 初始值
p0 = [0, 0, 0, 0]
# 要预测的特征X
prediction_x = 11


# 基函数
def func(p, x):
    k,b = p
    return k*x+b


# 误差函数
def error(p, x, y):
    return func(p, x) - y


# 封装
Para = leastsq(error, p0, args=(Xi, Yi))
# 预测
print('预测' + str(prediction_x) + '的值为:', func(Para[0], prediction_x))
