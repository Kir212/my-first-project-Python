# Написать функцию, вычисляющее значение функции при х = 1.79
# y = [cos(eˣ) + ln(1+x)² + √(eᶜᵒˢˣ + sin²(πx)) + √(1/x) + cos(x²)]^sin x

import math
def calculate_function(x):
    # Вычисление первой части выражения: cos(e^x)
    part1 = math.cos(math.exp(x)) # math.exp(x) вычисляет e^x, math.cos вычисляет косинус
    print(f"cos(eˣ): {part1:.4f}")

    # Вычисление второй части выражения: ln(1+x)^2
    part2 = math.pow(math.log(1 + x), 2) # math.log вычисляет натуральный логарифм, math.pow возводит в степень
    print(f"ln(1+x)²: {part2:.4f}")
    
    # Вычисление третьей части выражения: √(e^cosx + sin^2(πx))
    part3 = math.sqrt(math.exp(math.cos(x)) + math.pow(math.sin(math.pi * x), 2))
    print(f"√(eᶜᵒˢˣ + sin²(πx)): {part3:.4f}")
    # math.cos(x) вычисляет косинус x, math.exp возводит e в степень
    # math.pi представляет число π, math.sin вычисляет синус
    # math.pow возводит sin(πx) в квадрат, math.sqrt вычисляет квадратный корень
    
    # Вычисление четвертой части выражения: √(1/x)
    part4 = math.sqrt(1 / x) # Деление 1 на x и извлечение квадратного корня
    print(f"√(1/x): {part4:.4f}")

    # Вычисление пятой части выражения: cos(x^2)
    part5 = math.cos(math.pow(x, 2)) # math.pow(x, 2) вычисляет x^2, math.cos вычисляет косинус
    print(f"cos(x²)]^sin x: {part5:.4f}")

    base = part1 + part2 + part3 + part4 + part5 # Суммирование всех пяти частей выражения

    result = math.pow(base, math.sin(x)) # math.sin вычисляет синус, math.pow возводит base в степень sin(x)

    return result # Возврат результата вычисления функции

x_value = 1.79
result = calculate_function(x_value)

print(f" ")
print(f"Значение функции при Х = {x_value}: {result:.4f}")