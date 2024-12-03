import sys
import heapq

input = sys.stdin.readline

def dijkstra(graph, start):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    q = [(0, start)]

    while q:
        current_distance, current_node = heapq.heappop(q)
        if current_distance > distances[current_node]: continue
        for neighbor, time in graph[current_node]:
            distance = time + current_distance
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                heapq.heappush(q, (distance, neighbor))
    return distances

n, m, x = map(int, input().split())
x -= 1 
ways = [[] for _ in range(n)]

for i in range(m):
    source, destination, time = map(int, input().split())
    source -= 1
    destination -= 1
    ways[source].append((destination, time))

back2home_paths = dijkstra(ways, x)
for i in range(n):
    if i != x:
        go2home_paths = dijkstra(ways, i)
        back2home_paths[i] += go2home_paths[x]
print(max(back2home_paths))