# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")

# 4. Class Variables and Class Methods
class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# 7. Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn           # Private

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# 13. Composition
class Engine:
    def start(self):
        print("Engine started.")

class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

# 14. Aggregation
class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

class EmployeeAgg:
    def __init__(self, name):
        self.name = name

# 15. MRO and Diamond Inheritance
class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B")

class C(A):
    def show(self):
        print("Show from C")

class D(B, C):
    pass

# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# 17. Class Decorators
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class PersonDecorated:
    def __init__(self, name):
        self.name = name

# 18. Property Decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

# Testing some of the classes:

if __name__ == "__main__":
    # 1
    s = Student("Alice", 95)
    s.display()

    # 2
    c1 = Counter()
    c2 = Counter()
    Counter.display_count()

    # 3
    car = Car("Toyota")
    print(car.brand)
    car.start()

    # 4
    b1 = Bank()
    b2 = Bank()
    print(b1.bank_name)
    Bank.change_bank_name("New Bank Name")
    print(b2.bank_name)

    # 5
    print(MathUtils.add(5, 7))

    # 6
    log = Logger()
    del log

    # 7
    emp = Employee("John", 50000, "123-45-6789")
    print(emp.name)
    print(emp._salary)
    # print(emp.__ssn) # AttributeError
    emp.show_info()

    # 8
    t = Teacher("Mr. Smith", "Math")
    print(t.name, t.subject)

    # 9
    rect = Rectangle(4, 5)
    print(rect.area())

    # 10
    dog = Dog("Buddy", "Labrador")
    dog.bark()

    # 11
    Book.increment_book_count()
    Book.increment_book_count()
    print(Book.total_books)

    # 12
    print(TemperatureConverter.celsius_to_fahrenheit(0))

    # 13
    eng = Engine()
    car_with_eng = CarWithEngine(eng)
    car_with_eng.start_engine()

    # 14
    emp2 = EmployeeAgg("Emma")
    dept = Department("HR", emp2)
    print(dept.employee.name)

    # 15
    d = D()
    d.show()

    # 16
    say_hello()

    # 17
    p = PersonDecorated("Jane")
    print(p.greet())

    # 18
    prod = Product(100)
    print(prod.price)
    prod.price = 200
    print(prod.price)
    del prod.price

    # 19
    mult = Multiplier(3)
    print(mult(10))
    print(callable(mult))

    # 20
    try:
        check_age(16)
    except InvalidAgeError as e:
        print(e)
