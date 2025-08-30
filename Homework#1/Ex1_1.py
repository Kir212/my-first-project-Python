import math

# Коэффициенты квадратного уравнения y² - 12y + 20 = 0
a = 1
b = -12
c = 20

# Вычисляем дискриминант
discriminant = b**2 - 4*a*c

print(f"Уравнение: {a}y² + {b}y + {c} = 0")
print(f"Дискриминант D = {discriminant}")

# Проверяем значение дискриминанта
if discriminant > 0:
    # Два действительных корня
    y1 = (-b + math.sqrt(discriminant)) / (2*a)
    y2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Уравнение имеет два действительных корня:")
    print(f"y₁ = {y1}")
    print(f"y₂ = {y2}")
elif discriminant == 0:
    # Один действительный корень
    y = -b / (2*a)
    print(f"Уравнение имеет один действительный корень:")
    print(f"y = {y}")
else:
    # Два комплексных корня
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print(f"Уравнение имеет два комплексных корня:")
    print(f"y₁ = {real_part} + {imaginary_part}i")
    print(f"y₂ = {real_part} - {imaginary_part}i")

# Проверка решения
print("\nПроверка:")
if discriminant >= 0:
    # Для действительных корней
    if discriminant > 0:
        roots = [y1, y2]
    else:
        roots = [y]
    
    for i, root in enumerate(roots, 1):
        result = a*root**2 + b*root + c
        print(f"Для y_{i} = {root}: {a}*{root}² + {b}*{root} + {c} = {result}")
else:
    print("Для комплексных корней проверка требует дополнительных вычислений")