import matplotlib.pyplot as plt
import numpy as np
import random
from math import *

n = 1
N = 5000

def f(phi):
    return sqrt((11 + n) * cos(phi) ** 2 + (11 - n) * sin(phi) ** 2)


X = [f(phi)*cos(phi) for phi in np.arange(0, 2 * pi, 0.0001)]
Y = [f(phi)*sin(phi) for phi in np.arange(0, 2 * pi, 0.0001)]
a = abs(max(X) - min(X))
b = abs(max(Y) - min(Y))

x = [0]*(N+1)
y = [0]*(N+1)
pp = [0]*(N+1)
ff = [0]*(N+1)

for i in range(1, N + 1):
    x[i] = random.uniform(0, 2*a)
    y[i] = random.uniform(0, 2*b)
    x[i] = x[i] - a
    y[i] = y[i] - b
    pp[i] = sqrt(x[i]**2 + y[i]**2)

outside = []
inside = []

for i in range(1, N + 1):
    if (x[i] > 0):
        ff[i] = atan(y[i]/x[i])
    else:
        if (x[i] < 0):
            ff[i] = atan(y[i]/x[i]) + pi
        else:
            if (y[i] > 0):
                ff[i] = pi/2
            else:
                ff[i] = 3*pi/2

for i in range(1, N + 1):
    if (pp[i] < f(ff[i])):
        inside.append((x[i], y[i]))
    else:
        outside.append((x[i], y[i]))


m = len(inside)
s = m/N * a * b * 4

print(N, 'точек. Приблизительная площадь S =', round(s, 4))

exact_value = 21*pi/2
print('Точное значение площади:', round(exact_value, 4))
absolute_error = abs(s - exact_value)
print('Абсолютная погрешность:', round(absolute_error, 4))
print('Относительная погрешность:', round(absolute_error / exact_value, 4))

plt.scatter(*zip(*outside), s=5, color='red')
plt.scatter(*zip(*inside), s=5, color='green')
plt.gca().add_patch(plt.Rectangle(((min(X), max(Y))), a, -b, fill=False, linewidth=2))
plt.plot(X, Y, linewidth=2, color='black')
plt.show()