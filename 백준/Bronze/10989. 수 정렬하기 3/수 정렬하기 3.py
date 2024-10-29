import sys

input = sys.stdin.readline

n = int(input())
num_counter = {}

for _ in range(n):
    num = int(input())

    if num in num_counter:
        num_counter[num] += 1
    else:
        num_counter[num] = 1

for key, value in sorted(num_counter.items()):
    for _ in range(value):
        print(key)
