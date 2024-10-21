import numpy as np
import matplotlib.pyplot as plt
import math

# Данные (x, y) - экспериментальные точки
x = np.array([3, 5, 7, 9, 11, 13])
y = np.array([3.5, 4.4, 5.7, 6.1, 6.5, 7.3])

# 1.1 Линейная функция
def linear_func(x, a, b):
    return a * x + b

# 1.2 Степенная функция
def power_func(x, a, b):
    return b * np.power(x, a)

# 1.3 Показательная функция
def exp_func(x, a, b):
    return b * np.exp(a * x)

# 1.4 Квадратичная функция
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# 1. Реализация метода наименьших квадратов для линейной функции
def linear_fit(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum([xi**2 for xi in x])
    sum_xy = sum([xi * yi for xi, yi in zip(x, y)])

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b = (sum_y - a * sum_x) / n
    return a, b

# 2. Реализация для степенной функции
def power_fit(x, y):
    log_x = [math.log(xi) for xi in x]
    log_y = [math.log(yi) for yi in y]
    a, log_b = linear_fit(log_x, log_y)
    b = math.exp(log_b)
    return a, b

# 3. Реализация для показательной функции
def exp_fit(x, y):
    log_y = [math.log(yi) for yi in y]
    a, log_b = linear_fit(x, log_y)
    b = math.exp(log_b)
    return a, b

# 4. Реализация для квадратичной функции
def quadratic_fit(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x_squared = sum([xi**2 for xi in x])
    sum_x_cubed = sum([xi**3 for xi in x])
    sum_x_fourth = sum([xi**4 for xi in x])
    sum_y = sum(y)
    sum_xy = sum([xi * yi for xi, yi in zip(x, y)])
    sum_x_squared_y = sum([xi**2 * yi for xi, yi in zip(x, y)])

    A = [
        [sum_x_fourth, sum_x_cubed, sum_x_squared],
        [sum_x_cubed, sum_x_squared, sum_x],
        [sum_x_squared, sum_x, n]
    ]
    B = [sum_x_squared_y, sum_xy, sum_y]

    a, b, c = np.linalg.solve(A, B)
    return a, b, c

# Функции для вычисления погрешности по каждой модели
def calculate_linear_error(x, y, a, b):
    return np.sum((a * x + b - y) ** 2)

def calculate_power_error(x, y, a, b):
    return np.sum((b * np.power(x, a) - y) ** 2)

def calculate_exp_error(x, y, a, b):
    return np.sum((b * np.exp(a * x) - y) ** 2)

def calculate_quadratic_error(x, y, a, b, c):
    return np.sum((a * x**2 + b * x + c - y) ** 2)

# Аппроксимация методом наименьших квадратов для каждой функции
params_linear = linear_fit(x, y)
params_power = power_fit(x, y)
params_exp = exp_fit(x, y)
params_quadratic = quadratic_fit(x, y)

# Округление параметров до 0.01
params_linear = np.round(params_linear, 2)
params_power = np.round(params_power, 2)
params_exp = np.round(params_exp, 2)
params_quadratic = np.round(params_quadratic, 2)

# Построение графиков
x_range = np.linspace(min(x), max(x), 100)

y_linear = linear_func(x_range, *params_linear)
y_power = power_func(x_range, *params_power)
y_exp = exp_func(x_range, *params_exp)
y_quadratic = quadratic_func(x_range, *params_quadratic)

# Вычисление погрешности для каждой функции
linear_error = calculate_linear_error(x, y, *params_linear)
power_error = calculate_power_error(x, y, *params_power)
exp_error = calculate_exp_error(x, y, *params_exp)
quadratic_error = calculate_quadratic_error(x, y, *params_quadratic)

# Вывод параметров и ошибок
print(f"Линейная функция: y = {params_linear[0]} * x + {params_linear[1]}")
print(f"Погрешность (линейная): {linear_error:.4f}\n")

print(f"Степенная функция: y = {params_power[1]} * x^{params_power[0]}")
print(f"Погрешность (степенная): {power_error:.4f}\n")

print(f"Показательная функция: y = {params_exp[1]} * exp({params_exp[0]} * x)")
print(f"Погрешность (показательная): {exp_error:.4f}\n")

print(f"Квадратичная функция: y = {params_quadratic[0]} * x^2 + {params_quadratic[1]} * x + {params_quadratic[2]}")
print(f"Погрешность (квадратичная): {quadratic_error:.4f}\n")

# Построение графиков
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='black', label='Экспериментальные данные')

plt.plot(x_range, y_linear, label=f'Линейная (Погрешность={linear_error:.4f})', color='blue')
plt.plot(x_range, y_power, label=f'Степенная (Погрешность={power_error:.4f})', color='green')
plt.plot(x_range, y_exp, label=f'Показательная (Погрешность={exp_error:.4f})', color='red')
plt.plot(x_range, y_quadratic, label=f'Квадратичная (Погрешность={quadratic_error:.4f})', color='purple')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Аппроксимация методом наименьших квадратов')
plt.grid(True)
plt.show()
