# Создаю базу данных (список словарей) пользователей.
users = [
    {'login': 'Piter', 'age': 23, 'group': "admin"},
    {'login': 'Ivan', 'age': 10, 'group': "guest"},
    {'login': 'Dasha', 'age': 30, 'group': "master"},
    {'login': 'Fedor', 'age': 13, 'group': "guest"}
]

# Определяю функцию фильтрации с тремя типами сортировки.
def filter_users(users, sort_type, criteria):
    # 1. Фильтрация по возрасту.
    if sort_type == 1:
        filtered = [user for user in users if user['age'] > criteria]
    # 2. Фильтрация по первой букве логина.
    elif sort_type == 2:
        filtered = [user for user in users if
                    user['login'].startswith(criteria)]
    # 3. Фильтрация по группе.
    elif sort_type == 3:
        filtered = [user for user in users if user['group'] == criteria]
    else:
        return "Неверный тип сортировки"
    
    return filtered


def main():
    print("Выберите тип сортировки:")
    print("1. По возрасту")
    print("2. По первой букве")
    print("3. По группе")
    
    try:
        sort_type = int(input("тип сортировки: "))
        
        if sort_type == 1:
            criteria = int(input("Введите минимальный возраст: "))
        elif sort_type == 2:
            criteria = input("Введите первую букву логина: ").capitalize()
        elif sort_type == 3:
            criteria = input("Введите название группы: ")
        else:
            print("Неверный тип сортировки")
            return
        
        result = filter_users(users, sort_type, criteria)
        
        for user in result:
            print(
                f"Пользователь: '{user['login']}' возраст {user['age']} лет, группа '{user['group']}'")
    
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректные данные.")


if __name__ == "__main__":
    main()
