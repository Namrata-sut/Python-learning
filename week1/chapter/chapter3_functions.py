# function defination, calls, parameters, arguments, return values or expression
# addition of three numbers
def add_numbers(a, b, c):
    return a + b + c


a = int(input())
b = int(input())
c = int(input())
print(add_numbers(a, b, c))


# check number is even or odd
def is_even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


_number = int(input())
is_even_or_odd(number=_number)


# factorial of number
def factorial(n):
    if n == 0:
        return 1
    else:
        factorial_result = n * factorial(n - 1)
        return factorial_result


print(factorial(3))


# calculator: include addition, subtraction, multiplication, division
def calculator(operation, num1, num2):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2
    else:
        return "Please provide proper operation to perform on numbers."


#
operation = input()
num1 = int(input())
num2 = int(input())
print(calculator(operation, num1, num2))

"""Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print
 number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
 Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until
 the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later,
 using this sequence, you’ll arrive at 1! """
import sys


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


while True:
    try:
        number = int(input())
        result = collatz(number)
        print(result)
        if result == 1:
            sys.exit()
    except ValueError:
        print("Input number must be integer.")
