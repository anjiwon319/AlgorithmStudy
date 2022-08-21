# find prime number

import sys
input = sys.stdin.readline

num_count = int(input())
numbers = list(map(int, input().split()))
non_prime_count = 0

for i in numbers:
    if i == 1:
        non_prime_count +=1
    for j in range(2, i):
        if i % j == 0:
            non_prime_count += 1
            break
print(num_count - non_prime_count)