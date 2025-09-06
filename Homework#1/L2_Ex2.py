# Определение функции search_substr с двумя параметрами: subst (подстрока) и st (строка для поиска)
def search_substr(subst, st):
   
    if subst.lower() in st.lower(): # Проверяем, содержится ли подстрока subst в строке st без учета регистра
        return "Есть контакт!" # Если подстрока найдена, возвращаем сообщение "Есть контакт!"
    else:
        return "Мимо!" # Если подстрока не найдена, возвращаем сообщение "Мимо!"

text = "hello", "Hello World"
print(f"Подстрока:{text[0]}, Строка: {text[1]}")# text[0] - первый элемент кортежа ("hello"), text[1] - второй элемент кортежа ("Hello World")
print(search_substr(text[0], text[1])) # Вызов функции search_substr с передачей первого и второго элемента кортежа в качестве аргументов

print(f" ")

text = "cat", "Dog and mouse"
print(f"Подстрока:{text[0]}, Строка: {text[1]}")
print(search_substr(text[0], text[1]))

