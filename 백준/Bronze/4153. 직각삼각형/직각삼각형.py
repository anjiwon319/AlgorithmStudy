# 직각삼각형 (a right triangle)
import sys
# 빠른 입력을 위한 코드
input = sys.stdin.readline

legs = []
# 입력값 받기
while True:
    legs.append(list(map(int, input().split())))
    if legs[-1][0] == 0:
        del legs[-1]
        break

for i in legs:
    a = sorted(i)[0]
    b = sorted(i)[1]
    c = sorted(i)[2]
    # 직각 삼각형 확인 조건 : 가장 큰 변(c)의 제곱이 나머지 변(a, b)의 제곱합과 같다
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")
