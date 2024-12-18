if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        user_input = input().split()
        cmd = user_input[0]
        arg = user_input[1:]
        if cmd == 'insert':
            my_list.insert(int(arg[0]), int(arg[1]))
        elif cmd == 'print':
            print(my_list)
        elif cmd == 'remove':
            my_list.remove(int(arg[0]))
        elif cmd == 'append':
            my_list.append(int(arg[0]))
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()


    # my_list[1] = N-1
    # print(my_list)
    # my_list.remove(N-1)
    # my_list.append(N-1)
    # my_list.sort()
    # print(my_list)
    # my_list.pop()
    # my_list.reverse
    # print(my_list)

