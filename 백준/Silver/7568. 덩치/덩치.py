# 덩치

# 입력값 받기
n = int(input())
height = []
weight = []
for i in range(n):
    a, b = map(int, input().split(' '))
    height.append(a)
    weight.append(b)

# 등수 계산하기
grade = []
for i in range(n):
    k = 1
    for j in range(n):
        # i 보다 j의 덩치가 크거나 같을 때
        if height[j] > height[i] and weight[j] > weight[i]:
            k += 1
        # 덩치를 비교할 수 없거나 i보다 j의 덩치가 작을 때
        else:
            continue
    grade.append(k)

print(str(grade)[1:-1].replace(',', ''))