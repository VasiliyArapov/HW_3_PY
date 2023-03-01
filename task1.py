# Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

list_len = int(input("Длинна массива: "))
my_list = [randint(0,9) for i in range(list_len)]
print(my_list)
x = int(input("Введите число для поиска в массиве: "))
count = 0
for i in range(list_len):
    if my_list[i] == x:
        count += 1

print(count)
