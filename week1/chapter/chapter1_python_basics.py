# Arithmetic operations with integers
print(3 + 4 * 5)  # Precedence * and then +. Output= 23
print((6 - 2) * ((8 + 2) / (4 - 2)))  # precedence: (), *, / Output = 20

# string operations
print("Namrata" + "Sutar")  # concatenation
print("Namrata" * 5)  # repetitiion

# Input and string manipulation
print('What is your favorite color? ')
favorite_color = input()
print('Nice color, ' + favorite_color + '!')
print('Length of your favorite color is: ', len(favorite_color))

# Age calculation with user input
print("How old are you? ")
user_age = input()
print('You will be ' + str(int(user_age) + 1) + ' in one years.')

# String and Numeric Type conversion
print(str(1))  # int to str
print(str(-5.45))  # float to str
print(int('67'))  # str to int
print(int('-234'))  # str to int
print(int(3.24))  # float to int
print(float('4.57'))  # str to float
print(float(20))  # int to float

# Boolean expressions and comparisons
print(5 > 3)
print(89 == 89)
print(30 != 35)
print(7 < 2 or 3 > 2)
print(10 > 5 and 2 <= 2)
