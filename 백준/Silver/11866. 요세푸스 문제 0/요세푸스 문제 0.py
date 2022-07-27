# 요세푸스 문제 0
# n, k 입력을 받고, 1 ~ n 숫자를 갖는 number 리스트 생성
n, k = map(int, input().split(' '))
numbers = list(range(1, n+1))

# 처음 제거되는 k번째 사람을 number 리스트에서 pop 하여 josephus 리스트에 추가
index = k - 1
josephus = [numbers.pop(index)]

# 이후에도 number 리스트에서 k번째 사람을 pop 하여 josephus 리스트에 추가하는 작업 반복
for i in range(n-1, 0, -1):
    index = (index + k - 1) % i
    josephus.append(numbers.pop(index))

# 출력 형식 맞춰주기
josephus = str(josephus)
print('<' + josephus[1:-1] + '>')