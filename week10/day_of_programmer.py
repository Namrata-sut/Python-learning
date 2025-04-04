#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    leap: bool = None
    if year < 1918:
        leap = year % 4 == 0
    elif year > 1918:
        leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    else:
        return "26.09.1918"

    if leap:
        StartDate = "01/01/" + str(year)
        Date = datetime.strptime(StartDate, "%m/%d/%Y")
        EndDate = Date + timedelta(days=256)
        result = EndDate.strftime("%d.%m.%Y")
        return result
    else:
        StartDate = "01/01/" + str(year)
        Date = datetime.strptime(StartDate, "%m/%d/%Y")
        EndDate = Date + timedelta(days=255)
        result = EndDate.strftime("%d.%m.%Y")
        return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
