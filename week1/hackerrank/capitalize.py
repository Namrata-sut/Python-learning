import re
# Complete the solve function below.
def solve(s):
    split_s = re.split(r"\s", s)
    capitalized_s = [word.capitalize() for word in split_s]
    result = " ".join(capitalized_s)
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()
