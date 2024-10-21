def modified_neumann_method(N, R0, R1):
    sequence = [R0, R1]

    for _ in range(N - 2):
        # Умножаем оба предыдущих числа на 10000 для перехода к целым числам
        r0 = int(sequence[-2] * 10000)
        r1 = int(sequence[-1] * 10000)
        # Складываем предыдущие два числа и берем последние 4 цифры
        new_value = (r0 + r1) % 10000
        # Нормализуем результат обратно в диапазон (0, 1)
        new_value = new_value / 10000.0
        sequence.append(new_value)

    return sequence


N = 6
R0 = 0.5836
R1 = 0.2176
sequence_mod_neumann = modified_neumann_method(N, R0, R1)
print("Модифицированный метод Неймана:", sequence_mod_neumann)
