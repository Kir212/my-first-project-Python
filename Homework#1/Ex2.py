#  Сделать список в обратном поряде


my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
# my_list[:] - создает полную копию списка
#[::-1] - указывает, что копирование нужно выполнять в обратном порядке

print(f"Список в обратном порядке {reversed_list}:")


# Способ 2: Использование метода reverse() (изменяет исходный список)
my_list_copy = my_list.copy()  # Создаем копию, чтобы не изменять исходный список
my_list_copy.reverse()
print("Способ 2:", my_list_copy)

# Способ 3: Использование функции reversed()
reversed_list = list(reversed(my_list))
print("Способ 3:", reversed_list)

# Способ 4: Использование цикла
reversed_list = []
for i in range(len(my_list)-1, -1, -1):
    reversed_list.append(my_list[i])
print("Способ 4:", reversed_list)