from collections import Counter

def top_three_chars(s): # Определение функции top_three_chars с параметром s (строка)

    s_without_spaces = s.replace(' ', '') # Удаление всех пробелов из строки s методом replace()

    counter = Counter(s_without_spaces) # Создание объекта Counter для подсчета частоты символов в строке без пробелов

    most_common = counter.most_common(3) # Получение списка из 3 наиболее часто встречающихся символов с их количеством

    return most_common # Возврат результата работы функции


input_text = "Макс собирался поужинать в ресторане «Соль бемоль»" # Создание переменной input_text с текстом для анализа
result = top_three_chars(input_text) # Вызов функции top_three_chars с передачей текста и сохранение результата

print("Наиболее часто встречающиеся 3 символа")
print(f"в тексте: {input_text}:")
print(result)

print("")

print("Три наиболее часто встречающихся символа:")
for char, count in result: # Цикл для перебора результатов: распаковка каждого кортежа на символ и количество
    print(f"Символ '{char}': {count} раз(а)") # Форматированный вывод каждого символа и его количества встречаемости