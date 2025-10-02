#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название
#   соответствующего времени года ("зима", "весна" и т.д.)

def get_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Ошибка: неверный номер месяца"

try:
    month = int(input("Введите номер месяца: "))
    print(get_season(month))
except ValueError:
    print("Ошибка: введите целое число")