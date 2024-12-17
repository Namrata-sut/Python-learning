def mutate_string(string, position, character):
    # solution 1
    # string = string[:position] + character + string[position+1:]

    # solution 2
    l_str = list(string)
    l_str[position] = character
    string = "".join(l_str)
    return string


if __name__ == '__main__':
    string = input()
    i, c = input().split()
    new_string = mutate_string(string, int(i), c)
    print(new_string)
