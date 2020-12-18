import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

data = pd.read_csv('data_coordinate.csv', encoding='utf-8')
x = data["X坐标"]
y = data["Y坐标"]
z = data["类别"]

area = (30*np.random.rand(10))**2
for i in range(len(x)):
    if z[i] == 0:
        plt.scatter(x[i], y[i], c='b', s=16, alpha=0.5, marker='.')
    elif z[i] == 1:
        plt.scatter(x[i], y[i], c='c', s=16, alpha=0.5, marker='*')
    elif z[i] == 2:
        plt.scatter(x[i], y[i], c='g', s=16, alpha=0.5, marker='^')
    elif z[i] == 3:
        plt.scatter(x[i], y[i], c='k', s=16, alpha=0.5, marker=',')
    elif z[i] == 4:
        plt.scatter(x[i], y[i], c='m', s=16, alpha=0.5, marker='o')
    elif z[i] == 5:
        plt.scatter(x[i], y[i], c='r', s=16, alpha=0.5, marker='v')
    elif z[i] == 6:
        plt.scatter(x[i], y[i], c='w', s=16, alpha=0.5, marker='^')
    else:
        plt.scatter(x[i], y[i], c='y', s=16, alpha=0.5, marker='<')


plt.show()
