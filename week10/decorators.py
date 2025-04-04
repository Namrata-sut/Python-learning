def decorator_func(fun):
    def wrapper(*args, **kwargs):
        print("Calling decorator.")
        fun(*args, **kwargs)
        print("Called decorator.")

    return wrapper


@decorator_func
def func(number: int):
    print(f"{number} Entered.")


func(123)


# A higher-order function that takes another function as an argument


def fun(f, x):
    return f(x)


def square(x):
    return x * x


res = fun(square, 5)
print(res)


# Types of Decorators
# 1. Function Decorators: The most common type of decorator, which takes a function as input and returns a new function.
def simple_decorator(fun):
    def wrapper():
        print("Before calling the function.")
        fun()
        print("After calling the function.")

    return wrapper


@simple_decorator
def greet():
    print("Hello, World!")


greet()


# 2. Method Decorators: Used to decorate methods within a class. They often handle special cases, such as the
# self argument for instance methods.
def method_decorator(fun):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = fun(self, *args, **kwargs)
        print("After method execution")
        return res

    return wrapper


class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")


obj = MyClass()
obj.say_hello()


# 3. Class Decorators
# Class decorators are used to modify or enhance the behavior of a class. Like function decorators, class
# decorators are applied to the class definition. They work by taking the class as an argument and returning
# a modified version of the class.
def fun(cls):
    cls.class_name = cls.__name__
    return cls


@fun
class Person:
    pass


print(Person.class_name)
