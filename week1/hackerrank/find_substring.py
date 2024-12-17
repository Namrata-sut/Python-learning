def count_substring(string, sub_string):
    for i in range(0, len(string)):
        if sub_string:
            print()
    return

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)