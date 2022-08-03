# ACM Hotel
import sys

input = sys.stdin.readline
n = int(input())

def findRoomNumber(h, w, n):
    YY = n % h
    XX = n // h
    if YY == 0:
        YY = h
    else:
        XX += 1
    return f"{YY}{XX:02d}"

for i in range(n):
    h, w, n = map(int, input().split())
    print(findRoomNumber(h, w, n))
