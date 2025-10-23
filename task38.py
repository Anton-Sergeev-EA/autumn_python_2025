# todo: Класс "Заказ". Создайте класс Order (Заказ). Внутри он хранит список
#  экземпляров Product (из предыдущей задачи 37). Реализуйте свойство
#  total_price,  которое вычисляет общую стоимость заказа на основе цен всех
#  товаров в списке. Реализуйте методы add_product(product) и
#  remove_product(product) для управления списком.

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = None
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value

class Order:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        """Добавляет товар в заказ"""
        if isinstance(product, Product):
            self._products.append(product)
        else:
            raise ValueError("Можно добавлять только экземпляры класса Product")

    def remove_product(self, product):
        """Удаляет товар из заказа"""
        if product in self._products:
            self._products.remove(product)
        else:
            raise ValueError("Товар не найден в заказе")

    @property
    def total_price(self):
        """Вычисляет общую стоимость заказа"""
        return sum(product.price for product in self._products)

# Пример использования
book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()

order.add_product(book)
order.add_product(pen)

print(f"Общая стоимость: {order.total_price}")  # 12

# Дополнительные проверки
order.remove_product(book)
print(f"Общая стоимость после удаления книги: {order.total_price}")  # 2
