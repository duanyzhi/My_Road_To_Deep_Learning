import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)   # 100个点

y = 3*x + 5   # 标准的直线方程


def wgn(x, snr):   # 加入高斯白噪声
    snr = 10**(snr/10.0)
    xpower = np.sum(x**2)/len(x)
    npower = xpower / snr
    return np.random.randn(len(x)) * np.sqrt(npower)

n = wgn(y, 6)   # 根据信号产生6dBz信噪比的噪声

y_anr = y + n   # 输出系统的噪声信号


plt.plot(x, y_anr, "ks")   # 画出分布图
plt.xlabel('x')
plt.ylabel('y')
plt.table
plt.show()


