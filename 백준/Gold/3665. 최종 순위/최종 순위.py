import sys
import heapq

input = sys.stdin.readline

def kahn(graph, in_degree, n):
    min_heap = []
    result = []

    for node in range(1, n + 1):
        if in_degree[node] == 0:
            heapq.heappush(min_heap, node)

    while min_heap:
        current = heapq.heappop(min_heap)
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(min_heap, neighbor)

    if len(result) != n:
        return "IMPOSSIBLE"

    return result


test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    last_rank = list(map(int, input().split()))

    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[last_rank[i]].append(last_rank[j])
            in_degree[last_rank[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        if b in graph[a]:
            graph[a].remove(b)
            in_degree[b] -= 1
            graph[b].append(a)
            in_degree[a] += 1
        else:
            graph[b].remove(a)
            in_degree[a] -= 1
            graph[a].append(b)
            in_degree[b] += 1

    result = kahn(graph, in_degree, n)

    # 결과 출력
    if result == "IMPOSSIBLE":
        print(result)
    else:
        print(*result)