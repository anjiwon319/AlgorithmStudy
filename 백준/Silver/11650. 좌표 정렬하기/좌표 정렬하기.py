# 좌표 정렬하기

len = int(input())
dots = []

for i in range(len):
    x, y = map(int, input().split())
    dots.append((x, y))

# sort 사용해서 y 먼저 정렬 후, x 정렬 -> 방법2
dots.sort(key = lambda x : x[1])
dots.sort(key = lambda x : x[0])

# 출력 형식에 맞게 출력
for i in range(len):
    print(f"{dots[i][0]} {dots[i][1]}")