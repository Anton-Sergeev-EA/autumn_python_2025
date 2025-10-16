#todo: Взлом шифра. Вы знаете, что фраза зашифрована кодом цезаря с неизвестным
# сдвигом. Попробуйте все возможные сдвиги и расшифруйте фразу.
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

import string # Импортирую модуль string, который содержит различные
# строки-константы.

znaki = string.punctuation # Создаю переменную znaki, которая содержит все
# знаки препинания из модуля string.
shifr = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
# Задаю зашифрованный текст, который нужно расшифровать.
alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #
# Создаю список всех букв английского алфавита в нижнем регистре.

def decrypt(text, shift): # Определяю функцию decrypt для расшифровки текста.
    result = "" # Создаю пустую строку для результата.
    for char in text:  # Прохожу по каждому символу в тексте.
        # Если символ является знаком препинания или пробелом, добавляю его
        # без изменений.
        if char in znaki or char == " ":
            result += char
            continue # Перехожу к следующему символу.
        new_index = (alpa.index(char) - shift) % 26 # Нахожу новый индекс
        # буквы с учетом сдвига.
        result += alpa[new_index]  # Добавляю расшифрованную букву в результат.
    return result # Возвращаю расшифрованный текст.

for shift in range(1, 26): # Перебираю все возможные значения сдвига от 1 до
    # 25.
    decrypted_text = decrypt(shifr, shift) # Расшифровываю текст с текущим
    # значением сдвига.
    print(f"Сдвиг {shift}: {decrypted_text}")  # Вывожу результат с указанием
    # значения сдвига.
    
    # Проверяю, содержит ли расшифрованный текст известную фразу,
    # чтобы знать, что есть она.
    if "although that way may not be obvious at first unless you're dutch" in decrypted_text:
        print("\nНайден правильный сдвиг:", shift) # Если нашел правильный
        # сдвиг, вывожу информацию.
        print("Расшифрованный текст:", decrypted_text)
        break # Прекращаю поиск, так как нашел правильный сдвиг.
