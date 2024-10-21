def multiplicative_congruential_method(N, a, m, X0):
    sequence = []
    X = X0

    for _ in range(N):
        # Генерация нового значения
        X = (a * X) % m
        sequence.append(X)

    return sequence


N = 6
a = 265
m = 129
X0 = 122
sequence_congruential = multiplicative_congruential_method(N, a, m, X0)
print("Мультипликативный конгруэнтный метод:", sequence_congruential)
