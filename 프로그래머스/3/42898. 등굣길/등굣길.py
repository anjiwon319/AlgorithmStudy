def solution(m, n, puddles):
    answer = 0
    
    W = [[-1 for _ in range(m)] for _ in range(n)]
    W[0][0] = 0

    for y in range(1, n):
        W[y][0] = 1
    for x in range(1, m):
        W[0][x] = 1

    for x, y in puddles:
        W[y-1][x-1] = 0
        if y == 1:
            for i in range(x, m):
                W[0][i] = 0
        if x == 1:
            for j in range(y, n):
                W[j][0] = 0
        
    return way(W, m-1, n-1)


def way(W, x, y):
    if W[y][x] < 0:
        W[y][x] = (way(W, x, y-1) + way(W, x-1, y)) % 1000000007
        return W[y][x]
    return W[y][x]