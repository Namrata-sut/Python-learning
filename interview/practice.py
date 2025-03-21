lst = [16, 30, 45, 81, 90]

first = lst[0]

# def second_max_item(lst: list):
#     sorted_lst = sorted(lst, reverse=True)
#     return sorted_lst[1]
#
#
# print(second_max_item(lst))

# def second_max_item(lst: list):
#     max = lst[0]
#     for i in range(len(lst)):
#         if lst[i] >= lst[i + 1]:
#             max = lst[i]
#     return max
#
# print(second_max_item(lst))

# name = "Namrata Sutar"
#
#
# def reverse_string(name:str):
#     return name[::-1]
#
#
# print(reverse_string(name))


name = "Namrata Sutar"


def reverse_string(name):
    if len(name) <= 1:
        return name
    return reverse_string(name[1:]) + name[0]


print(reverse_string(name))

dt = {
    "Raj": 27,
    "Piya": 28,
    "Amit": 30,
    "Ram": 24
}

lambda_fun = dict(sorted(dt.items(), key=lambda x: x[1]))
print(lambda_fun)

# 2000, 1500, 3500 = 5000
#
# post = 1 grp of 5 people
# put = add any add cost
# get = split 1 person
#


