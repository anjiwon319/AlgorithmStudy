n, k = map(int, input().split(' '))
k = k - 1
list = list(range(1, n+1))
josephus = [list.pop(k)]
index = k
for i in range(n-1, 0, -1):
    index = (index + k) % i
    josephus.append(list.pop(index))

josephus = str(josephus)
josephus = josephus.replace('[', '<')
josephus = josephus.replace(']', '>')
print(josephus)