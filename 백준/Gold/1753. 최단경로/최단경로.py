import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(graph, start):
    n = len(graph)
    distances = [INF] * n
    distances[start] = 0

    q =[(0, start)]
    while q:
        current_distance, current_node = heapq.heappop(q)
        if current_distance > distances[current_node] : continue
        for neighbor, weight in graph[current_node]:
            distance = weight + current_distance
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                heapq.heappush(q, (distance, neighbor))
    return distances

v, e = map(int, input().split())
graph = {i:set() for i in range(v)}
start = int(input())
start -= 1

for i in range(e):
    source, destination, weight = map(int, input().split())
    source -= 1
    destination -= 1
    graph[source].add((destination, weight))

graph = {i:list(graph[i]) for i in range(v)}

shortest_distance = dijkstra(graph, start)
for distance in shortest_distance:
    if distance > v*10:
        print("INF")
    else:
        print(distance)