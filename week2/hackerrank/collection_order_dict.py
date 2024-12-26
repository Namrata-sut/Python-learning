# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
products = OrderedDict()

for _ in range(n):
    item_name, space, price = input().rpartition(" ")
    products[item_name] = products.get(item_name, 0) + int(price)

for item, price in products.items():
    print(item, price)
