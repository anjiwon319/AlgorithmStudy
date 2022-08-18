# Greatest Common Divisior & Least Common Multiple

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 공약수 구하기(common divisor)
def get_cd(n, m):
    cd = []
    small = n if n < m else m
    for i in range(1, small+1):
        if n % i == 0 and m % i == 0:
            cd.append(i)
    return cd

# gcd(최대공약수) 구하기
cd = get_cd(n, m)
gcd = cd[-1]

# lcm(최소공배수) 구하기
lcm = gcd * (n//gcd) * (m//gcd)

print(f"{gcd}\n{lcm}")