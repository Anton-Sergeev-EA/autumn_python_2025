#todo: Числа в буквы. Замените числа, написанные через пробел, на буквы.
# Не числа не изменять.
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
# Создаем словарь соответствия букв числам

number_to_letter = {
    8: 'h',
    5: 'e',
    12: 'l',
    15: 'o',
    0: ' ',
    23: 'w',
    18: 'r',
    4: 'd'
}


def numbers_to_letters(input_string):
    parts = input_string.split()
    result = []
    for part in parts:
        try:
            number = int(part)
            if number in number_to_letter:
                result.append(number_to_letter[number])
            else:
                result.append(str(number))
        except ValueError:
            result.append(part)
    return ''.join(result)

print(numbers_to_letters("8 5 12 12 15"))
print(numbers_to_letters("8 5 12 12 15 , 0 23 15 18 12 4 !"))
