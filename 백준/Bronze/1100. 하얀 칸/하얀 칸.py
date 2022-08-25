# 하얀 칸

import sys
input =sys.stdin.readline

count = 0
# 8x8의 체스판
for i in range(8):
    start = 0
    line = input()[:-1]
    if i % 2 != 0:
        start = 1
    for j in range(start, 8, 2):
        if line[j] == 'F':
            count += 1

print(count)