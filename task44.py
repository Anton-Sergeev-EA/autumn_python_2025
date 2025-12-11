#  1. Реализовать класса DB - синглтон. Экземляр класса(подключение) к PostgreSQL должно быть единственным.
#  2. Реализовать фабрику, которая создает модели различных производителей.

from abc import ABC, abstractmethod
import psycopg2
from psycopg2 import pool


# Singleton для подключения к PostgreSQL.
class DB:
    _instance = None
    _connection_pool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)
            # Создаем пул соединений (1 соединение для Singleton).
            cls._connection_pool = psycopg2.pool.SimpleConnectionPool(
                1, 1,  # minconn=1, maxconn=1 - только одно соединение.
                dbname="sergeev_database",
                user="sergeev_user",
                password="sergeev_password",
                host="localhost",
                port="5432"
            )
        return cls._instance

    def get_connection(self):
        """Получить соединение из pull."""
        return self._connection_pool.getconn()

    def return_connection(self, conn):
        """Вернуть соединение в pull."""
        self._connection_pool.putconn(conn)

    def close_all_connections(self):
        """Закрыть все соединения."""
        self._connection_pool.closeall()


# Абстрактный класс с абстрактными методами.
class CarABC(ABC):
    @abstractmethod
    def sold(self):
        """Автомобиль продан."""
        pass

    @abstractmethod
    def discount(self):
        """Скидка на автомобиль."""
        pass


# Конкретный класс Car.
class Car(CarABC):
    def __init__(self, brand, model):
        """Инициализация атрибутов brand и model"""
        self.brand = brand
        self.model = model

    def sold(self):
        """Автомобиль продан."""
        print(f"Автомобиль {self.brand} {self.model} продан")

    def discount(self):
        """Скидка на автомобиль."""
        print(f"На автомобиль {self.brand} {self.model} скидка 5%")

    def __repr__(self):
        """Dunder‑метод."""
        return f"Car(brand='{self.brand}', model='{self.model}')"


# Фабрика для создания автомобилей.
class CarFactory:
    @staticmethod
    def make_lada():
        """Метод для создания автомобиля Lada."""
        return Car("Lada", "Vesta")

    @staticmethod
    def make_mercedes():
        """Метод для создания автомобиля Mercedes."""
        return Car("Mercedes", "E-Class")

    @staticmethod
    def make_toyota():
        """Метод для создания Toyota."""
        return Car("Toyota", "Camry")

    @staticmethod
    def create_car(brand, model=None):
        """Универсальный метод создания автомобиля."""
        if brand.lower() == "lada":
            return CarFactory.make_lada()
        elif brand.lower() == "mercedes":
            return CarFactory.make_mercedes()
        elif brand.lower() == "toyota":
            return CarFactory.make_toyota()
        else:
            return Car(brand, model or "Unknown")


# Демонстрация использования.
if __name__ == "__main__":
    # Использование Singleton DB.
    db1 = DB()
    db2 = DB()
    print(f"Это один и тот же объект DB: {db1 is db2}")

    # Получаем соединение с DB.
    conn = db1.get_connection()

    # Используем фабрику для создания автомобилей.
    lada = CarFactory.make_lada()
    mercedes = CarFactory.make_mercedes()
    toyota = CarFactory.make_toyota()

    print("\nСозданные автомобили:")
    print(lada)
    print(mercedes)
    print(toyota)

    print("\nМетоды автомобилей:")
    lada.sold()
    mercedes.discount()

    # Универсальный метод создания.
    bmw = CarFactory.create_car("BMW", "X5")
    print(f"\nСоздан через универсальный метод: {bmw}")

    # Возвращаем соединение в pull.
    db1.return_connection(conn)

    # Закрываем все соединения при завершении.
    db1.close_all_connections()