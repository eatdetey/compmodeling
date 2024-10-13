import matplotlib.pyplot as plt
import numpy as np
import random
from statistics import *
from math import pi

n = 1
N = 1000
r = n

z = [0]*(2*N + 1)

for i in range (1, 2*N + 1):
    z[i] = random.uniform(0, 2*r)

x = [i for i in z]
y = [0]*(N + 1)
for j in range (1, N+1):
    y[j] = z[j+N]

outside = []
inside = []

for i in range (1, N + 1):
    if ((x[i] - r)**2 + (y[i] - r)**2 < r**2):
        inside.append((x[i], y[i]))
    else:
        outside.append((x[i], y[i]))

m = len(inside)
p = 4*m/N

print(N, 'точек. Вычисленное значение pi =', p)

print('Значение числа пи из бибиотеки math:', pi)
absolute_error = abs(p - pi)
print('Абсолютная погрешность:', round(absolute_error, 4))
print('Относительная погрешность:', round(absolute_error / pi, 4))

plt.scatter(*zip(*outside), s=7, color = 'red')
plt.scatter(*zip(*inside), s=7, color = 'green')
plt.gca().add_patch(plt.Rectangle((0, 0), 2 * r, 2 * r, fill=False, linewidth=2))
plt.gca().add_patch(plt.Circle((r, r), r, fill=False, linewidth=2, color = 'black'))
plt.axis('equal')
plt.show()