def lemer_method(N, R0, g):
    sequence = []
    x = R0

    for _ in range(N):
        # Генерация нового значения
        x = (g * x) % 1
        sequence.append(x)

    return sequence


N = 5
R0 = 0.585
g = 927
sequence_lemer = lemer_method(N, R0, g)
print("Метод Лемера:", sequence_lemer)
