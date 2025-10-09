# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
X = 10
Y = 15
Z = 2

maximum = max(X, Y, Z)
# Ответ:
print(maximum)
# Наибольшее число 15

# Пример:
X = 77
Y = 9
Z = 130

if X > Y:
    if X > Z:
        maximum = X
    else:
        maximum = Z
else:
    if Y > Z:
        maximum = Y
    else:
        maximum = Z
# Ответ:
print("Наибольшее число:", maximum)
# Наибольшее число 130

# Задачу решить без функций max и прочих.
# Значение переменных может меняться