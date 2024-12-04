import sys

input = sys.stdin.readline
INF = float('inf')

def bellman_ford(edges, start):
    n = len(edges)
    distances = [INF] * n
    distances[start] = 0
    is_negative_loop = False

    for _ in range(n-1):
        for i in range(n):
            for destination, weight in edges[i]:
                if distances[i] + weight < distances[destination]:
                    distances[destination] = distances[i] + weight
    
    for i in range(n):
        for destination, weight in edges[i]:
            if distances[i] + weight < distances[destination]:
                is_negative_loop = True
                break

    return distances, is_negative_loop


n, m = map(int, input().split())
ways = [[] for _ in range(n)]

for _ in range(m):
    source, destination, weight = map(int, input().split())
    source -= 1
    destination -=1
    ways[source].append((destination, weight))

shortest_paths, is_negative_loop = bellman_ford(ways, 0)
if is_negative_loop:
    print(-1)
else:
    for i in range(1, len(shortest_paths)):
        if shortest_paths[i] == INF:
            print(-1)
        else:
            print(shortest_paths[i])