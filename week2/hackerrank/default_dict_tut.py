# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


def find_word_indices():
    n, m = map(int, input().split())
    group_A = defaultdict(list)

    for i in range(1, n + 1):
        word = input().strip()
        group_A[word].append(i)

    for _ in range(m):
        word = input().strip()
        if word in group_A:
            print(" ".join(map(str, group_A[word])))
        else:
            print(-1)


find_word_indices()