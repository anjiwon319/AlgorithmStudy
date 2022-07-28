# 덩치
'''
원래 문제에서 말하는 덩치가 크다는 건 몸무게와 키가 모두 커야함을 의미
키는 크지만 몸무게가 같은 경우 또는 반대일 경우 덩치가 크다고 판단하지 않음
따라서 해당 코드는 키는 크지만 몸무게가 같은 경우를 덩치가 크다고 판단했을 때의 등수 계산을 출력하는 코드임
'''
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
        if height[j] >= height[i] and weight[j] >= weight[i]:
            # i와 j의 덩치가 같을 때
            if height[j] == height[i] and weight[j] == weight[i]:
                continue
            k += 1
        # 덩치를 비교할 수 없거나 i보다 j의 덩치가 작을 때
        else:
            continue
    grade.append(k)

# 출력 양식에 맞게 출력하기
print(str(grade)[1:-1].replace(',', ''))