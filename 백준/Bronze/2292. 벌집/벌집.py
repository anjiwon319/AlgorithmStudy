# 벌집
import sys
input = sys.stdin.readline
n = int(input())

k = 0
while n > 1 + (k*(k+1)/2)*6:
    k += 1
print(k + 1)


