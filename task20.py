#todo: Выведите все строки данного файла в обратном порядке, допишите их в
# этот же файл. Для этого считайте список всех строк при помощи
# метода readlines().
# Открываем файл в режиме чтения

with open('inverted_sort.txt', 'r') as file:
    lines = file.readlines()
reversed_lines = lines[::-1]

with open('inverted_sort.txt', 'a') as file:
    file.write('\n')
    for line in reversed_lines:
        file.write(line.rstrip('\n') + '\n')
