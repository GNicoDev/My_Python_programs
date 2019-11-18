# В этой задаче необходимо проверить, 
# делится ли число A на число B нацело. Использовать можно 
# только арифметические операции, использование любых видов ветвлений, 
# функций и т.п. запрещено.
# Формат ввода
# Вводятся два натуральных числа A и B.
# Формат вывода
# Выведите "YES", если A кратно B и "NO" в противном случае.

# Тест 1
# Входные данные:
# 10
# 5
# Вывод программы:
# YES

# Тест 2
# Входные данные:
# 10
# 3
# Вывод программы:
# NO

print("Введите делимое:")
a = int(input())
print("Введите делитель:")
b = int(input())
c = a % b
d = c == 0
print('YES' * int(d), 'NO' * int(1 - d), sep='')
