# 음계

import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
# count = 0 : 'ascending'
count = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        continue
    else:
        count += 1

if count == 0:
    print('ascending')
elif count == len(numbers) -1:
    print('descending')
else:
    print('mixed')