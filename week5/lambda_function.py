# Regular function
def add(a, b):
    return a + b


# Lambda function
add_lambda = lambda a, b: a + b

print("Regular function", add(2, 3))
print(" Lambda function", add_lambda(2, 3))


# 1. Lambda with map(): This function applies a lambda function to each item in iterable
numbers1 = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers1)
print("Lambda with map()", list(squares))

# 2. Lambda with filter(): This function filters items in iterable based on condition.
numbers2 = [1, 2, 3, 4, 5, 6, 7]
even_numbers = filter(lambda x: x % 2 == 0, numbers2)
print("Lambda with filter()", list(even_numbers))

# 3. Lambda with reduce(): This function reduces a sequence into a single value.
from functools import reduce
numbers3 = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, numbers3)
print("Lambda with reduce()", product)

# 4. Sorting with Lambda
students = [('abc', 85), ('efg', 90), ('hij', 80)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorting with Lambda", sorted_students)

# 5. Lambda in List comprehensions: Lambda functions can be used within list comprehensions for
# concise transformations.
numbers4 = [1, 2, 3, 4]
doubled = [(lambda x: x * 2)(x) for x in numbers4]
print("List comprehensions", doubled)



