def neumann_method(N, R0):
    sequence = []
    r = R0

    for _ in range(N):
        # Умножаем r на 10000 для перехода к целому числу
        r = int(r * 10000)
        # Возводим в квадрат
        squared = r ** 2
        # Берем средние 4 цифры
        middle_digits = (squared // 100) % 10000
        # Нормализуем результат обратно в диапазон (0, 1)
        r = middle_digits / 10000.0
        sequence.append(r)

    return sequence

N = 6
R0 = 0.583
sequence_neumann = neumann_method(N, R0)
print("Метод Неймана:", sequence_neumann)
