import re

T = int(input())
for _ in range(T):
    try:
        regex = input()
        a = (re.compile(regex))
        print(bool(a))
    except re.error:
        print('False')