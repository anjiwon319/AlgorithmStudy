import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    applicants = []
    passer = 1

    for i in range(n):
        applicants.append(tuple(map(int, input().split())))

    applicants.sort(key=lambda x : x[0])
    threshold = applicants[0][1]
    for i in range(1, n):
        if applicants[i][1] < threshold:
            passer += 1
            threshold = applicants[i][1]

    print(passer)
