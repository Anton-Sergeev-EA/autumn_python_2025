# todo: Исправить ошибку в коде игры: from lesson_5.code import ya_kube
# Основные исправления: Добавлена обработка исключений при работе с файлами;
# Исправлен режим записи файла на ‘a’ (append); Добавлен перенос строки при
# сохранении; Добавлена инициализация переменной list_word в функции
# start_game; Исправлено отображение маски; Добавлена проверка на выход из
# цикла при отгадывании слова; Добавлена обработка ввода букв в нижнем
# регистре.

from lesson_5.code import ya_kube
import random
import uuid
import datetime
from lesson_5.code.db import DICT_DEFENITION_WORD

name = input("Введите имя: ")


def print_menu():
    print("""
       1. Начать игру
       2. Сохранить игру
       3. Загрузить игру
       4. Выход из игры
       5. Настройки
    """)


print_menu()
num = int(input("Пункт меню: "))


def generate_key() -> str:
    keys = list(DICT_DEFENITION_WORD.keys())
    random.shuffle(keys)
    return keys.pop()


def save_game(id_session, word, mask):
    # Исправлен режим записи файла на 'a' (append)
    with open("save_game.csv", "a") as f:
        dt = datetime.datetime.now()
        mask = "".join(mask)
        save_str = f"{dt}|{id_session}|{name}|{word}|{mask}\n"  # Добавлен перенос строки
        f.write(save_str)
    print("Сохранил игру!")


def load_game():
    try:
        with open("save_game.csv", "r") as f:
            list_str = f.readlines()
            indx = 0
            found = False
            for csv_str in list_str:
                if name in csv_str:
                    print(f"{indx}) {csv_str.strip()}")
                    found = True
                    indx += 1
            if not found:
                print("Сохранений не найдено!")
                return
            
            indx_load = int(input("Введите номер: "))
            sg = list_str[indx_load].split("|")
            key = sg[3]
            mask = sg[4]
            session_uuid = sg[1]
            print(
                f"Загружаю сессию: {session_uuid}, слово: {key}, маска: {list(mask)}")
            start_game(session_uuid, key.strip(), list(mask))
    except FileNotFoundError:
        print("Файл сохранений не найден!")
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")


def start_game(session_uuid, key, mask):
    list_word = list(key)  # Добавлена инициализация list_word
    print(DICT_DEFENITION_WORD[key])
    print("".join(mask))  # Исправлено отображение маски
    
    while '#' in mask:
        alfa = input("Введите букву: ").lower()  # Приведено к нижнему регистру
        if alfa == "2":
            print("Сохранение игры!")
            save_game(session_uuid, key, mask)
            continue  # Добавлен continue для продолжения цикла
        
        for i in range(len(list_word)):
            if alfa == list_word[i]:
                mask[i] = alfa
        print("".join(mask))  # Исправлено отображение маски
        
        if '#' not in mask:
            print("Поздравляем! Вы угадали слово!")
            break


match num:
    case 1:
        key = generate_key()
        list_word = list(key)
        mask = ['#'] * len(key)
        session_uuid = uuid.uuid4()
        start_game(session_uuid, key, mask)
    case 2:
        print("Функция сохранения")
        # Здесь можно добавить логику сохранения текущей игры
    case 3:
        load_game()
    case 4:
        print(f"Спасибо {name} за игру! Заходи еще!")
    case 5:
        print("Настройки")
        # Здесь можно добавить логику настроек
    case _:
        print("Неверный выбор")
