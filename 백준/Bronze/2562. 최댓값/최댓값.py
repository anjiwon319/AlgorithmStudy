# 2562 최댓값 찾기

numbers = []
for i in range(9):
    numbers.append(int(input()))
    
max = sorted(numbers)[-1]

print(f"{max} {numbers.index(max)+1}")