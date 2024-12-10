import sys

input = sys.stdin.readline

def compute_lps(P):
    m = len(P)
    lps = [0] * m 
    j = 0

    for i in range(1, m):
        while j > 0 and P[i] != P[j]:
            j = lps[j-1]

        if P[i] == P[j]:
            j += 1
            lps[i] = j

    return lps


def kmp_search(T, P):
    n, m = len(T), len(P)
    lps = compute_lps(P)

    occurrences = []
    i = j = 0

    for i in range(n):
        while j > 0 and T[i] != P[j]:
            j = lps[j-1]

        if T[i] == P[j]:
            j += 1
            if j == m:
                occurrences.append(i-m+2)
                j = lps[j-1]
    return occurrences

    
T = input().rstrip()
P = input().rstrip()

result = kmp_search(T, P)

print(len(result))
if result:
    print(*result)