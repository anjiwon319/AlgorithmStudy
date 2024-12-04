import sys

input = sys.stdin.readline
INF = float('inf')

def bellman_ford(edges, start):
    n = len(edges) - 1
    distances = [(-1)*INF] * (n+1)
    distances[start] = 0
    path = [0 for _ in range(n+1)]
    for i in range(n):
        for j in range(1, n+1):
            for destination, weight in edges[j]:
                if distances[j] + weight > distances[destination]:
                    distances[destination] = distances[j] + weight
                    path[destination] = j
                    if i == n - 1: distances[destination] = INF

    if distances[n] == INF:
        return [], True
    
    result = []
    cur_node = n
    while cur_node != start:
        result.append(cur_node)
        cur_node = path[cur_node]
    result.append(start)
    result.reverse()

    return result, False


n, m = map(int, input().split())
ways = [[] for _ in range(n+1)]

for _ in range(m):
    source, destination, weight = map(int, input().split())
    ways[source].append((destination, weight))

shortest_paths, is_cycle = bellman_ford(ways, 1)
if is_cycle:
    print(-1)
else:
    print(*shortest_paths, sep=" ")