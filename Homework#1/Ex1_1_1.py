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
    # нет действительных корней(имеет два комплексных)
    real_part = (-b) / (2*a)
    imaginary_part = ((-discriminant)**0.5) / (2*a)
    print(f"Уравнение {Equation} не имеет действительных корней:")
    print(f"Уравнение {Equation} имеет два комплексных корня:")
    print(f"y1 = {y1}, y2 = {y2}:")
    print(f"y1 = {real_part} + {imaginary_part}i")
    print(f"y2 = {real_part} - {imaginary_part}i")