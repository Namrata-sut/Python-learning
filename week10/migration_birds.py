import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    return max(set(arr), key=arr.count)


# def migratoryBirds(arr):
#     # Initial count is zero
#     count = 0
#
#     # Iterate over the list
#     for val in arr:
#
#         # If num is equal to 3
#         if val == 3:
#             # Increase the counter
#             count += 1
#
#     print(count)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTP/UT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
