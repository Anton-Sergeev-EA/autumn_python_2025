#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время
# последнего выполнения
import functools
import datetime
import atexit
from typing import Callable, Any

# Словарь для хранения статистики: ключ — имя функции, значение — (счётчик, последнее время вызова).
_call_stats = {}



def count_calls(func: Callable) -> Callable:
    """
    Декоратор, подсчитывающий количество вызовов функции и фиксирующий время последнего вызова.
    При завершении программы статистика записывается в debug.log.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Увеличиваю счётчик вызовов.
        if func.__name__ not in _call_stats:
            _call_stats[func.__name__] = [0, None]
        _call_stats[func.__name__][0] += 1

        # Фиксирую текущее время как время последнего вызова.
        _call_stats[func.__name__][1] = datetime.datetime.now()

        # Вызываю оригинальную функцию.
        return func(*args, **kwargs)

    return wrapper



def _write_stats_to_log() -> None:
    """
    Записывает собранную статистику в файл debug.log при завершении программы.
    Формат: Название функции, кол-во вызовов, дата-время последнего выполнения.
    """
    with open("debug.log", "a", encoding="utf-8") as f:
        for func_name, (count, last_time) in _call_stats.items():
            if last_time is not None:
                # Форматируем дату как ДД.ММ.ГГГГ ЧЧ:ММ
                time_str = last_time.strftime("%d.%m.%Y %H:%M")
                f.write(f"{func_name}, {count}, {time_str}\n")



# Регистрирую функцию записи лога при выходе из программы.
atexit.register(_write_stats_to_log)



# --- Пример использования ---

@count_calls
def render(data: str) -> None:
    print(f!Rendering: {data}")

@count_calls
def show(item: str) -> None:
    print(f!Showing: {item}")

@count_calls
def process(x: int, y: int) -> int:
    return x + y



if __name__ == "__main__":
    # Имитирую вызовы функций.
    render("page1")
    render("page2")
    show("widget")
    process(1, 2)
    render("page3")
    show("dialog")
