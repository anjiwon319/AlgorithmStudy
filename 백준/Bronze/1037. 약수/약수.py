len = int(input())
divisior = input().split(' ')

# divisior 리스트 내의 값을 int로 타입 변경 
divisior = list(map(int, divisior))

# 약수들을 오름차순으로 정렬
divisior.sort()
print(divisior[0] * divisior[-1])