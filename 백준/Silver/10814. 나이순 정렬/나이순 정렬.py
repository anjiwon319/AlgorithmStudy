# 나이순 정렬

import sys
# 빠른 입력
input = sys.stdin.readline

n = int(input())
 
# dictionary(members) -> {age : [name, name, ...], ..}
members = {}
for i in range(n):
    age, name = input().split()
    age = int(age)
    if age in members:
        members[age].append(name)
    else:
        members[age] = [name]

# 나이순으로 정렬한 뒤 가입한 순서에 따라 출력
for age in sorted(members.keys()):
    for name in members[age]:
        print(age, name)