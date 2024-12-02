import sys
import heapq

input = sys.stdin.readline

def dijkstra(graph, start):
    n = len(graph)
    costs = [INF] * (n+1)
    costs[start] = 0

    q = [(0, start)]
    while q:
        current_cost, current_city = heapq.heappop(q)
        if current_cost > costs[current_city]: continue
        for neighbor, weight in graph[current_city]:

            cost = current_cost + weight
            if costs[neighbor] > cost:
                costs[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))

    return costs


n = int(input())
m = int(input())

INF = float('inf')

cities = {i:[] for i in range(1, n+1)}

for _ in range(m):
    source, destination, cost = map(int, input().split())
    cities[source].append((destination, cost))

source, destination = map(int, input().split())
shortest_cost = dijkstra(cities, source)
print(shortest_cost[destination])
