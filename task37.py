# todo: Класс "Товар" (Защита от отрицательной цены) Создайте класс Product.
#  У него есть свойства name (простая строка) и price. При установке цены
#  проверяйте, что она не отрицательная. Если пытаются установить
#  отрицательную  цену, устанавливайте 0.
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = None  # приватное свойство для хранения цены
        self.price = price  # используем сеттер для установки начальной цены

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # Проверяем, что значение не отрицательное
        if value < 0:
            self._price = 0
        else:
            self._price = value

# Пример использования
product = Product("Book", 10)
print(product.price)  # 10
product.price = -5
print(product.price)  # 0