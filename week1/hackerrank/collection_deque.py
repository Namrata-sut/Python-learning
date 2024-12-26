# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    command = input().split()
    operation = command[0]
    # value = command[1]

    if operation == "append":
        d.append(command[1])
    elif operation == "pop":
        d.pop()
    elif operation == "popleft":
        d.popleft()
    elif operation == "appendleft":
        d.appendleft(command[1])

for item in d:
    print(item, end=" ")
