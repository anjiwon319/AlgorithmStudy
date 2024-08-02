n = int(input())
scores = list(map(int, input().split()))
M = max(scores)

for i in range(n):
    scores[i] = scores[i] / M

mean = sum(scores) / n * 100
print(mean)
