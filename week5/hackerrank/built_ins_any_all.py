# Task
# You are given a space separated list of integers. If all the integers are positive,
# then you need to check if any integer is a palindromic integer.
N = int(input())
nums = list(map(int, input().split()))
print(all(int(i) > 0 for i in nums) and any(str(i) == str(i)[::-1] for i in nums))

nums_list = []
for i in range(N):
    input_data = int(input())
    nums_list.append(input_data)

for i in nums:
    if int(i) > 0 and str(i) == str(i)[::-1]:
        print(True)
