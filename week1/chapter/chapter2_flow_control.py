# comparison operators
# boolean operators
# mixing comparison and boolean
# if elif else conditions
# while, for loops
# break continue statements
# random, sys standard libraries

# if else
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')

# if elif else
name = 'Carol'
age = 89
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 200:
    print('Unlike you, Alice is not an undead, immortal vampire.')
else:
    print('You are neither Alice nor a little kid.')

# while loop
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

name = ''
while name != 'Namrata':
    print('Please type your name.')
    name = input()
print('Thank you!')

# break statement
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# continue statement
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
num_of_guests = int(input())
if num_of_guests:
    print('Be sure to have enough room for all your guests.')
print('Done')

# for loop
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# equivalent to above
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

# Starting, Stopping, and Stepping to range()
for i in range(0, 10, 2):
    print(i)
for i in range(5, -1, -1):
    print(i)

# random standard library
import random
for i in range(5):
    print(random.randint(1, 10))

# sys standard library
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

# # 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings!
# # if anything else is stored in spam.
print("Give greetings: ")
spam = int(input())
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")

# 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program
# that prints the numbers 1 to 10 using a while loop.
for num in range(1, 11):
    print(num)

num = 1
while num <= 10:
    print(num)
    num+=1

