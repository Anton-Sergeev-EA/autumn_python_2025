#todo: Написать программу, которая считывает два числа и выводит их сумму,
# разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат
# возведения в степень.

def get_number(prompt):
    """Функция для безопасного ввода числа"""
    while True:
        try:
            # Сначала пытаемся преобразовать в float
            number = float(input(prompt))
            # Если дробной части нет, возвращаем int
            if number.is_integer():
                return int(number)
            return number
        except ValueError:
            print("Ошибка! Введите корректное число.")


def main():
    a = get_number("Введите первое число: ")
    b = get_number("Введите второе число: ")
    
    sum_result = a + b
    diff_result = a - b
    mult_result = a * b
    div_result = a / b if b != 0 else "Деление на ноль!"
    int_div_result = a // b if b != 0 else "Деление на ноль!"
    mod_result = a % b if b != 0 else "Деление на ноль!"
    
    try:
        pow_result = a ** b
    except OverflowError:
        pow_result = "Результат слишком большой для вычисления"
    
    print("\nРезультаты вычислений:")
    print(f"{a} + {b} = {sum_result}")
    print(f"{a} - {b} = {diff_result}")
    print(f"{a} * {b} = {mult_result}")
    print(f"{a} / {b} = {div_result}")
    print(f"{a} // {b} = {int_div_result}")
    print(f"{a} % {b} = {mod_result}")
    print(f"{a} ** {b} = {pow_result}")


if __name__ == "__main__":
    main()
