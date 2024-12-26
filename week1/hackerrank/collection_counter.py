from collections import Counter

x = int(input())
shoe_sizes = list(map(int, input().split()))

N = int(input())

shoe_inventory = Counter(shoe_sizes)

earnings = 0

for _ in range(N):
    size, price = map(int, input().split())
    if shoe_inventory[size] > 0:
        earnings += price
        shoe_inventory[size] -= 1
print(earnings)