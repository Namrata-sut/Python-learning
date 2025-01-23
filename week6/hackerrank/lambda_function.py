# Task
# Input Format:
# One line of input: an integer N.
#
# Output Format:
# A list on a single line containing the cubes of the first N fibonacci numbers.
#
# Sample Input
# 5
#
# Sample Output
# [0, 1, 1, 8, 27]

cube = lambda x: x * x * x


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_num = [0, 1]
    for i in range(2, n):
        fib_num.append(fib_num[i - 1] + fib_num[i - 2])
    return fib_num


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
