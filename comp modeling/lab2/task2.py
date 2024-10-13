from math import *
import matplotlib.pyplot as plt
import numpy as np
import random

n = 1
N = 5000

def f(x):
    return sqrt(11 - n * sin(x)*sin(x))

a = 5
b = 4

x=[0]*(N+1)
y=[0]*(N+1)
outside = []
inside = []

for i in range (1, N+1):
    x[i] = random.uniform(0,a)
    y[i] = random.uniform(0,b)
    if (y[i] < f(x[i])):
        inside.append((x[i],y[i]))
    else:
        outside.append((x[i],y[i]))

M = len(inside)
s = M/N*a*b

print(N, 'точек. Приблизительная площадь S =', round(s, 4))

exact_value = 16.17845801094261
print('Точное значение площади:', round(exact_value, 4))
absolute_error = abs(s - exact_value)
print('Абсолютная погрешность:', round(absolute_error, 4))
print('Относительная погрешность:', round(absolute_error / exact_value, 4))

plt.scatter(*zip(*inside), s=5, color='green')
plt.scatter(*zip(*outside), s=5, color='red')
X = np.arange(0.01, a, 0.0001)
plt.plot(X, [f(x) for x in X], linewidth=2.7, color='black')
plt.show()