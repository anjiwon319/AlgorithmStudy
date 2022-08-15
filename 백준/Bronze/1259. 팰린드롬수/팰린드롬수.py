# 펠린드롬수

import sys
input = sys.stdin.readline

while True:
    palindrome = True
    n = int(input())
    if n == 0:
        break # while 문 탈출
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-(i+1)]:
            palindrome = False
    print('yes' if palindrome else 'no')