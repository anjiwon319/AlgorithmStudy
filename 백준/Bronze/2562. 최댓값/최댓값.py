# 2562 최댓값 찾기

numbers = []
for i in range(9):
    numbers.append(int(input()))

max = 0
idx = 0
for i in range(9):
    if(numbers[i] > max):
        max = numbers[i]
        idx = i

print(max, idx+1)
