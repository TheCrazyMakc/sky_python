class Dog:
    def __init__(self, name, age):
        self.name = name  # Атрибуты объекта
        self.age = age

dog = Dog("Бобик", 3)
print(dog.name)  # Бобик


# Атрибуты класса vs Атрибуты экземпляра
    # Атрибуты класса — общие для всех объектов.
    # Атрибуты экземпляра — уникальные для каждого объекта.
class Car:
    wheels = 4  # Атрибут класса (общий)

    def __init__(self, brand):
        self.brand = brand  # Атрибут экземпляра

print(Car.wheels)  # 4 (доступ через класс)
my_car = Car("Toyota")
print(my_car.brand)  # Toyota (доступ через объект)

# Методы
# ① Обычные методы (принимают self)
class Dog:
    def bark(self):
        print("Гав!")

dog = Dog()
dog.bark()  # Гав!


# ② Статические методы (@staticmethod)
# Не требуют self, работают как обычные функции внутри класса.
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(2, 3))  # 5 (вызов без создания объекта)


# ③ Методы класса (@classmethod)
# Работают с классом, а не с объектом. Принимают cls вместо self.
class Car:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

print(Car.get_count())  # 0


# 5. Наследование
# Позволяет создавать дочерние классы на основе родительских.
class Animal:
    def eat(self):
        print("Ест")

class Cat(Animal):  # Наследуем от Animal
    def meow(self):
        print("Мяу")

cat = Cat()
cat.eat()  # Ест (унаследованный метод)
cat.meow()  # Мяу


# 6. Полиморфизм
# Переопределение методов родительского класса.
class Animal:
    def sound(self):
        print("Звук")

class Dog(Animal):
    def sound(self):  # Переопределяем метод
        print("Гав")

dog = Dog()
dog.sound()  # Гав (вместо "Звук")


# 8. Магические методы (__method__)
# Специальные методы для переопределения поведения объектов.
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):  # Вызывается при print(book)
        return f"Книга: {self.title}"

book = Book("Война и мир")
print(book)  # Книга: Война и мир


# 9. Композиция (Включение объектов)
# Создание сложных объектов из простых.
class Engine:
    def start(self):
        print("Двигатель запущен")

class Car:
    def __init__(self):
        self.engine = Engine()  # Композиция

car = Car()
car.engine.start()  # Двигатель запущен
___________________________________________________________________________________

# 1. Базовый синтаксис класса
class НазваниеКласса:
    # Атрибуты класса (данные)
    attribute = "Значение"

    # Методы (функции класса)
    def method(self):
        print("Это метод класса")

class Dog:
    # Атрибут класса (общий для всех собак)
    species = "Canis lupus familiaris"

    # Метод __init__ (конструктор) — вызывается при создании объекта
    def __init__(self, name, age):
        self.name = name  # Атрибут экземпляра
        self.age = age    # Атрибут экземпляра

    # Метод экземпляра
    def bark(self):
        print(f"{self.name} говорит: Гав-гав!")

# 2. Как создать объект (экземпляр класса)?
# Создаём объект класса Dog
my_dog = Dog(name="Бобик", age=3)

# Обращаемся к атрибутам
print(my_dog.name)   # Бобик
print(my_dog.age)    # 3
print(my_dog.species)  # Canis lupus familiaris

# Вызываем метод
my_dog.bark()  # Бобик говорит: Гав-гав!

# 3. Основные компоненты класса
# __init__ — конструктор
#    Вызывается автоматически при создании объекта.
#    Нужен для инициализации атрибутов.
#    self — ссылка на сам объект (обязательный первый аргумент).
def __init__(self, name, age):
    self.name = name  # Создаём атрибут name
    self.age = age    # Создаём атрибут age

# Атрибуты экземпляра (уникальные для каждого объекта):
self.name = "Бобик"  # Разные у разных собак

# Атрибуты класса (общие для всех объектов):
species = "Canis lupus familiaris"  # Одинаковые у всех собак

# Методы (функции класса)
#    Все методы принимают self первым аргументом.
#    Могут работать с атрибутами объекта.
def bark(self):
    print(f"{self.name} лает!")


# 4. Пример: класс Car (Машина)
class Car:
    # Атрибут класса
    wheels = 4

    # Конструктор
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # Начальный пробег

    # Метод для увеличения пробега
    def drive(self, km):
        self.mileage += km
        print(f"Машина проехала {km} км. Общий пробег: {self.mileage} км")

    # Метод для вывода информации
    def info(self):
        print(f"{self.brand} {self.model} ({self.year}), пробег: {self.mileage} км")

# Использование:
my_car = Car("Toyota", "Corolla", 2020)
my_car.drive(150)  # Машина проехала 150 км. Общий пробег: 150 км
my_car.info()      # Toyota Corolla (2020), пробег: 150 км

# 5. Наследование (Inheritance)
class ElectricCar(Car):  # Наследуемся от Car
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)  # Вызываем конструктор родителя
        self.battery_capacity = battery_capacity  # Добавляем новый атрибут

    # Переопределяем метод drive
    def drive(self, km):
        print(f"Едем на электричестве! Пробег увеличен на {km} км")
        self.mileage += km

# Использование:
tesla = ElectricCar("Tesla", "Model S", 2023, 100)
tesla.drive(300)  # Едем на электричестве! Пробег увеличен на 300 км
tesla.info()      # Tesla Model S (2023), пробег: 300 км

# Итог
    # Класс — это шаблон для создания объектов.
    # __init__ — конструктор, вызывается при создании объекта.
    # Атрибуты — переменные внутри класса (self.name).
    # Методы — функции внутри класса (def bark(self):).
    # Наследование позволяет расширять функциональность (class Child(Parent):).