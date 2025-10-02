# todo: Преобразуйте переменную age и foo в число.
age = "23"
age_number = int(age)
print(f"Преобразованное значение age: {age_number} (тип: {type(age_number)})")

foo = "23abc"
number_str = '' # Создаем пустую строку для накопления цифр.
for char in foo: # Проходим по каждому символу в строке foo.
    if char.isdigit(): # Проверяем, является ли текущий символ цифрой.
        number_str += char # Если символ - цифра, добавляем его к нашей строке.
    else:
        break # Как только встречаем нецифровой символ - прерываем цикл.
        
number = int(number_str) if number_str else 0
""" Преобразуем полученную строку в число. Если number_str не пустая -
преобразуем в int. Если пустая -возвращаем 0."""

print(f"Результат: {number} (тип: {type(number)})")

# Преобразуйте переменную age в Boolean
age = "123abc"
Booleanage = bool(age)
print(Booleanage)

# Преобразуйте переменную flag в Boolean
flag = 1
Booleanages = bool(flag)
print(Booleanages)

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
boolean_str_one = bool(str_one)
boolean_str_two = bool(str_two)
print(boolean_str_one, boolean_str_two)

# Преобразуйте значение 0 и 1 в Boolean
number_0 = 0
number_1 = 1
boolean_0 = bool(number_0)
boolean_1 = bool(number_1)
print(boolean_0, boolean_1)

# Преобразуйте False в строку
boolean = False
str_value = str(boolean)
print(type(str_value))
