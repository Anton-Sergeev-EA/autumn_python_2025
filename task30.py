# todo: Вы работаете с данными цен товаров, которые приходят в разном
#  формате. Создайте список числовых значений цен,  игнорируя некорректные
#  записи. Все цены переведите в рубли. Задачу следует решить с
#  использованием списковых включений.


COURSES = {
    'USD': 90,
    'EUR': 100,
    'JPY': 0.7
}

def convert_to_rub(price_str):
    try:
        if '₽' in price_str:
            return float(price_str.replace('₽', '').strip())
        
        for currency in COURSES:
            if currency in price_str:
                amount = float(price_str.replace(currency, '').strip())
                return amount * COURSES[currency]
        
        return float(price_str)
    
    except (ValueError, TypeError):
        return None


prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99", "18.99", "N/A",
          "¥5000"]

rub_prices = [price for price in (convert_to_rub(p) for p in prices) if price is not None]

print(rub_prices)

