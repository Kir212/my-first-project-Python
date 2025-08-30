import math

#y^2-12y+20=0
Equation = "y^2-12y+20=0"
a = 1
b = -12
c = 20

#Находим D
discriminant = b**2 - 4*a*c

#проверка
if discriminant > 0:
    # два действительных корня
    y1 = (-b + discriminant**0.5) / (2*a)
    y2 = (-b - discriminant**0.5) / (2*a)
    print(f"Уравнение {Equation} имеет два действительных корня:")
    print(f"y1 = {y1}, y2 = {y2}:")

elif discriminant == 0:
    # один действительный корень
    y = (-b ) / (2*a)
    print(f"Уравнение {Equation} имеет один действительный корень:")
    print(f"y = {y}:")

else:
    # нет действительных корней(имеет два комплесных)
    real_part = (-b) / (2*a)
    imaginary_part = ((-discriminant)**0.5) / (2*a)
    print(f"Уравнение {Equation} не имеет действительных корней:")
    print(f"Уравнение {Equation} имеет два комплексных корня:")
    print(f"y1 = {real_part} + {imaginary_part}i")
    print(f"y2 = {real_part} - {imaginary_part}i")
    



#z^2-17y+72=0
Equation = "z^2-17y+72=0"
a = 1
b = 17
c = 72

#Находим D
discriminant = b**2 - 4*a*c

#проверка
if discriminant > 0:
    # два действительных корня
    z1 = (-b + discriminant**0.5) / (2*a)
    z2 = (-b - discriminant**0.5) / (2*a)
    print(f"Уравнение {Equation} имеет два действительных корня:")
    print(f"z1 = {z1}, z2 = {z2}:")

elif discriminant == 0:
    # один действительный корень
    z = (-b ) / (2*a)
    print(f"Уравнение {Equation} имеет один действительный корень:")
    print(f"z = {z}:")

else:
    # нет действительных корней(имеет два комплесных)
    real_part = (-b) / (2*a)
    imaginary_part = ((-discriminant)**0.5) / (2*a)
    print(f"Уравнение {Equation} не имеет действительных корней:")
    print(f"Уравнение {Equation} имеет два комплексных корня:")
    print(f"z1 = {real_part} + {imaginary_part}i")
    print(f"z2 = {real_part} - {imaginary_part}i")


#x^2-7x-44=0
Equation = "x^2-7x-44=0"
a = 1
b = -7
c = -44

#Находим D
discriminant = b**2 - 4*a*c

#проверка
if discriminant > 0:
    # два действительных корня
    x1 = (-b + discriminant**0.5) / (2*a)
    x2 = (-b - discriminant**0.5) / (2*a)
    print(f"Уравнение {Equation} имеет два действительных корня:")
    print(f"x1 = {x1}, x2 = {x2}:")

elif discriminant == 0:
    # один действительный корень
    x = (-b ) / (2*a)
    print(f"Уравнение {Equation} имеет один действительный корень:")
    print(f"x = {x}:")

else:
    # нет действительных корней(имеет два комплесных)
    real_part = (-b) / (2*a)
    imaginary_part = ((-discriminant)**0.5) / (2*a)
    print(f"Уравнение {Equation} не имеет действительных корней:")
    print(f"Уравнение {Equation} имеет два комплексных корня:")
    print(f"x1 = {real_part} + {imaginary_part}i")
    print(f"x2 = {real_part} - {imaginary_part}i")


#y^2+9y+8=0
Equation = "y^2+9y+8=0"
a = 1
b = 9
c = 8

#Находим D
discriminant = b**2 - 4*a*c

#проверка
if discriminant > 0:
    # два действительных корня
    y1 = (-b + discriminant**0.5) / (2*a)
    y2 = (-b - discriminant**0.5) / (2*a)
    print(f"Уравнение {Equation} имеет два действительных корня:")
    print(f"y1 = {y1}, y2 = {y2}:")

elif discriminant == 0:
    # один действительный корень
    y = (-b ) / (2*a)
    print(f"Уравнение {Equation} имеет один действительный корень:")
    print(f"y = {y}:")

else:
    # нет действительных корней(имеет два комплесных)
    real_part = (-b) / (2*a)
    imaginary_part = ((-discriminant)**0.5) / (2*a)
    print(f"Уравнение {Equation} не имеет действительных корней:")
    print(f"Уравнение {Equation} имеет два комплексных корня:")
    print(f"y1 = {real_part} + {imaginary_part}i")
    print(f"y2 = {real_part} - {imaginary_part}i")


#b^2-2b-63=0
Equation = "b^2-2b-63=0"
a = 1
b = -2
c = -63

#Находим D
discriminant = b**2 - 4*a*c

#проверка
if discriminant > 0:
    # два действительных корня
    b1 = (-b + discriminant**0.5) / (2*a)
    b2 = (-b - discriminant**0.5) / (2*a)
    print(f"Уравнение {Equation} имеет два действительных корня:")
    print(f"b1 = {b1}, b2 = {b2}:")

elif discriminant == 0:
    # один действительный корень
    b = (-b ) / (2*a)
    print(f"Уравнение {Equation} имеет один действительный корень:")
    print(f"b = {b}:")

else:
    # нет действительных корней(имеет два комплесных)
    real_part = (-b) / (2*a)
    imaginary_part = ((-discriminant)**0.5) / (2*a)
    print(f"Уравнение {Equation} не имеет действительных корней:")
    print(f"Уравнение {Equation} имеет два комплексных корня:")
    print(f"b1 = {real_part} + {imaginary_part}i")
    print(f"b2 = {real_part} - {imaginary_part}i")


import cmath

def solve_equation():
    print("Решение уравнения (x² - 8)² + 4(x² - 8) - 5 = 0")
    print("=" * 50)
    
    # Шаг 1: Решаем t² + 4t - 5 = 0
    a = 1
    b = 4
    c = -5
    
    # Вычисляем дискриминант
    discriminant = b**2 - 4*a*c
    
    print(f"Дискриминант D = {discriminant}")
    
    # Находим корни для t
    t1 = (-b + math.sqrt(discriminant)) / (2*a)
    t2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    print(f"t₁ = {t1}, t₂ = {t2}")
    
    # Шаг 2: Решаем уравнения для x
    solutions = []
    
    # Для t1 = 1: x² - 8 = 1 → x² = 9
    x1 = math.sqrt(9)
    x2 = -math.sqrt(9)
    solutions.extend([x1, x2])
    
    # Для t2 = -5: x² - 8 = -5 → x² = 3
    x3 = math.sqrt(3)
    x4 = -math.sqrt(3)
    solutions.extend([x3, x4])
    
    # Выводим решения
    print("\nРешения уравнения:")
    for i, x in enumerate(solutions, 1):
        print(f"x{i} = {x}")
    
    # Проверка решений
    print("\nПроверка решений:")
    for x in solutions:
        # Вычисляем значение выражения (x² - 8)² + 4(x² - 8) - 5
        result = (x**2 - 8)**2 + 4*(x**2 - 8) - 5
        print(f"При x = {x}: ({x}² - 8)² + 4({x}² - 8) - 5 = {result}")

# Запускаем решение
solve_equation()
