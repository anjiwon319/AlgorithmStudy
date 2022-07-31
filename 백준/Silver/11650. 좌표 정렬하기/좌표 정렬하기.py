# 좌표 정렬하기

len = int(input())
dots = []

for i in range(len):
    x, y = map(int, input().split())
    dots.append((x, y))

# sort로 다중 조건 정렬해서 출력 (x 우선 정렬 후 y 정렬)
dots.sort(key = lambda x : (x[0], x[1]))

# 출력 형식에 맞게 출력
for i in range(len):
    print(f"{dots[i][0]} {dots[i][1]}")