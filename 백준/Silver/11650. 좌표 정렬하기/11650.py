# 좌표 정렬하기

len = int(input())
dots = []

for i in range(len):
    x, y = map(int, input().split())
    dots.append((x, y))

# sort로 다중 조건 정렬해서 출력 (x 우선 정렬 후 y 정렬) -> 방법1
# dots.sort(key = lambda x : (x[0], x[1]))

# sort 사용해서 y 먼저 정렬 후, x 정렬 -> 방법2
# dots.sort(key = lambda x : x[1])
# dots.sort(key = lambda x : x[0])

# for문 사용해서 y 먼저 정렬 후, x 정렬 -> 방법3
for i in range(len-1):
    for j in range(1, len):
        if dots[j-1][1] > dots[j][1]:
            tmp = dots[j]
            dots[j] = dots[j-1]
            dots[j-1] = tmp

for i in range(len-1):
    for j in range(1, len):
        if dots[j-1][0] > dots[j][0]:
            tmp = dots[j]
            dots[j] = dots[j-1]
            dots[j-1] = tmp

# 출력 형식에 맞게 출력
for i in range(len):
    print(f"{dots[i][0]} {dots[i][1]}")