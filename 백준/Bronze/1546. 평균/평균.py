n = int(input())
scores = list(map(int, input().split()))
M = max(scores)
scores = [score/M for score in scores]
mean = sum(scores) / n * 100
print(mean)
