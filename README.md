# Python OOP Assignment

This repository contains solutions for 20 Python Object-Oriented Programming (OOP) tasks, covering concepts like `self`, `cls`, public/private/protected variables, inheritance, abstraction, decorators, static/class methods, MRO, custom exceptions, and more.

---

## Table of Contents

- [1. Using self](#1-using-self)
- [2. Using cls](#2-using-cls)
- [3. Public Variables and Methods](#3-public-variables-and-methods)
- [4. Class Variables and Class Methods](#4-class-variables-and-class-methods)
- [5. Static Variables and Static Methods](#5-static-variables-and-static-methods)
- [6. Constructors and Destructors](#6-constructors-and-destructors)
- [7. Access Modifiers: Public, Private, and Protected](#7-access-modifiers-public-private-and-protected)
- [8. The super() Function](#8-the-super-function)
- [9. Abstract Classes and Methods](#9-abstract-classes-and-methods)
- [10. Instance Methods](#10-instance-methods)
- [11. Class Methods](#11-class-methods)
- [12. Static Methods](#12-static-methods)
- [13. Composition](#13-composition)
- [14. Aggregation](#14-aggregation)
- [15. Method Resolution Order (MRO) and Diamond Inheritance](#15-method-resolution-order-mro-and-diamond-inheritance)
- [16. Function Decorators](#16-function-decorators)
- [17. Class Decorators](#17-class-decorators)
- [18. Property Decorators](#18-property-decorators)
- [19. callable() and __call__()](#19-callable-and-__call__)
- [20. Creating a Custom Exception](#20-creating-a-custom-exception)

---

## 1. Using self
Created a `Student` class using `self` to initialize attributes `name` and `marks` through a constructor. A method `display()` prints the student details.

## 2. Using cls
Created a `Counter` class to track how many objects are created using a class variable and a `@classmethod`.

## 3. Public Variables and Methods
Built a `Car` class with a public variable `brand` and a public method `start()` accessible outside the class.

## 4. Class Variables and Class Methods
Developed a `Bank` class with a class variable `bank_name` and a class method `change_bank_name()` to change it.

## 5. Static Variables and Static Methods
Created `MathUtils` with a static method `add(a, b)` that performs addition without using class or instance variables.

## 6. Constructors and Destructors
Designed a `Logger` class that prints messages when an object is created and destroyed.

## 7. Access Modifiers: Public, Private, and Protected
Made an `Employee` class with public (`name`), protected (`_salary`), and private (`__ssn`) attributes.

## 8. The super() Function
Implemented inheritance where `Teacher` class inherits from `Person` and uses `super()` to call the parent constructor.

## 9. Abstract Classes and Methods
Utilized the `abc` module to define an abstract class `Shape` with an abstract method `area()`, and implemented it in `Rectangle`.

## 10. Instance Methods
Built a `Dog` class with instance variables and an instance method `bark()`.

## 11. Class Methods
Created a `Book` class to track the number of books using a class method `increment_book_count()`.

## 12. Static Methods
Developed a `TemperatureConverter` class with a static method `celsius_to_fahrenheit()`.

## 13. Composition
Used composition by embedding an `Engine` object inside a `CarWithEngine` class.

## 14. Aggregation
Showed aggregation through `Department` and `EmployeeAgg` classes where the `Employee` exists independently.

## 15. Method Resolution Order (MRO) and Diamond Inheritance
Demonstrated MRO with classes `A`, `B`, `C`, and `D`, where `D` inherits from both `B` and `C`.

## 16. Function Decorators
Built a decorator `log_function_call` to log a message before executing a function.

## 17. Class Decorators
Created a class decorator `add_greeting` to dynamically add a `greet()` method to a class.

## 18. Property Decorators
Designed a `Product` class with a private attribute `_price` using `@property`, `@setter`, and `@deleter`.

## 19. callable() and __call__()
Made a `Multiplier` class implementing `__call__()` to allow objects to behave like functions.

## 20. Creating a Custom Exception
Defined a custom exception `InvalidAgeError` and raised it from a `check_age(age)` function if `age < 18`.

---

## How to Run

1. Make sure you have **Python 3.x** installed.
2. Save the code into a file named `assignment.py
