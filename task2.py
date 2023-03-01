#  Требуется найти в массиве из случайных чисел(от 1 до n) 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

list_len = int(input("Длинна массива: "))
my_list = [randint(0,9) for i in range(list_len)]
print(my_list)
x = int(input("Введите искомое число для сравнения: "))
diff = abs(my_list[0] - x)
res = my_list[0]
for i in range(list_len):
    temp = abs(my_list[i] - x)
    if temp < diff:
        diff = temp
        res = my_list[i]

print(res)
