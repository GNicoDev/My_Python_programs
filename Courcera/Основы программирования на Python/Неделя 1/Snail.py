# Улитка ползет по вертикальному шесту высотой H метров, 
# поднимаясь за день на A метров, а за ночь спускаясь на 
# B метров. На какой день улитка доползет до вершины шеста?
# Формат ввода
# Программа получает на вход целые H, A, B. Гарантируется,
# что A > B ≥ 0.
# Формат вывода
# Программа должна вывести одно натуральное число.

# Тест 1
# Входные данные:
# 10
# 3
# 2

# Вывод программы:
# 8

print("Высота вертикального шеста:")
h = int(input())
print("Метры вверх за день:")
a = int(input())
print("Метры вниз за день")
b = int(input())
print("Номер дня", int(1 + (h - b - 1) / (a - b)))
