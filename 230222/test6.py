import sys
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

# n, r = map(int, sys.stdin.readline().split())

N = int(input())
# board = list(map(int, sys.stdin.readline().split()))
    
cnt = 0
res = [0 for _ in range(N+1)]

for i in range(2, N+1):
    res[i] = res[i-1] + 1

    if i % 3 == 0:
        res[i] = min(res[i], res[i//3] + 1)
    if i % 2 == 0:
        res[i] = min(res[i], res[i//2] + 1)
print(res[N])

