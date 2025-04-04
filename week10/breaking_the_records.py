#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    high_score = scores[0]  # First game score as initial high score
    low_score = scores[0]   # First game score as initial low score
    high_count = 0
    low_count = 0

    for score in scores[1:]:  # Start checking from the second game
        if score > high_score:
            high_score = score  # Update high score
            high_count += 1  # Increase high record count
        elif score < low_score:
            low_score = score  # Update low score
            low_count += 1  # Increase low record count

    return [high_count, low_count]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
