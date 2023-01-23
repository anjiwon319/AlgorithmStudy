# 1247 - 부호

import sys
input = sys.stdin.readline # 빠른 입력

for _ in range(3):
    n = int(input())
    total = 0
    for i in range(n):
        total += int(input())
    
    if total > 0:
        print("+")
    elif total <0:
        print("-")
    else:
        print("0")