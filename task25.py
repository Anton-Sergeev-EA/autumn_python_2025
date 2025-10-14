# todo: Шифр Цезаря. Задача. Считайте файл message.txt и зашифруйте  текст
#  шифром Цезаря, при этом символы первой строки файла должны циклически
#  сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
#  В этой задаче удобно считывать файл построчно, шифруя каждую строку в
#  отдельности. В каждой строчке содержатся различные символы. Шифровать
#  нужно только буквы кириллицы.

def encrypt_line(line, shift):
    alphabet_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    alphabet_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    
    shifted_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
    shifted_upper = alphabet_upper[shift:] + alphabet_upper[:shift]
    
    translation_table = str.maketrans(
        alphabet_lower + alphabet_upper,
        shifted_lower + shifted_upper
    )
    
    return line.translate(translation_table)


def main():
    try:
        with open('message.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        shift = 1
        
        encrypted_lines = []
        
        for line in lines:
            encrypted_line = encrypt_line(line, shift)
            encrypted_lines.append(encrypted_line)
            shift += 1
        
        for line in encrypted_lines:
            print(line, end='')
    
    except FileNotFoundError:
        print("Файл message.txt не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    main()
