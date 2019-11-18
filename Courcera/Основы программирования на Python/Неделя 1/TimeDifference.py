# Даны два момента времени в пределах одних и тех же суток. 
# Для каждого момента указан час, минута и секунда. Известно, 
# что второй момент времени наступил не раньше первого.
# Определите сколько секунд прошло между двумя моментами времени.
# Формат ввода
# Программа на вход получает шесть целых чисел через перевод строки. 
# Первые три целых числа соответствуют часам, минутам и секундам 
# первого момента, следующие три числа соответствуют второму моменту.
# Часы задаются числом от 0 до 23 включительно. Минуты и секунды —
# от 0 до 59.
# Формат вывода
# Выведите число секунд между этими моментами времени.

# Тест 1
# Входные данные:
# 1
# 1
# 1
# 2
# 2
# 2

# Вывод программы:
# 3661

print("Количество часов для t1:")
h1 = int(input())
print("Количество минут для t1:")
m1 = int(input())
print("Количество секунд для t1:")
s1 = int(input())
print("Количество часов для t2:")
h2 = int(input())
print("Количество минут для t2:")
m2 = int(input())
print("Количество часов для t2:")
s2 = int(input())
time1 = (h1 * 3600) + (m1 * 60) + s1
time2 = (h2 * 3600) + (m2 * 60) + s2
print("Разница во времени равна", time2 - time1)
