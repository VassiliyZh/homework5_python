# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 
def sum_number(a, b):
    if b == 0:
        return a
    return sum_number(a + 1, b - 1)

print(sum_number(int(input('Введите число a: ')), int(input('Введите число b: '))))
# 3  4
# 4  3
# 5  2
# 6  1
# 7  0