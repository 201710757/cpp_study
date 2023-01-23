import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

_max = -987654321

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or j == k or i == k:
                continue
            pick = arr[i] + arr[j] + arr[k]
            if pick <= M and _max < pick:
                _max = pick
        



print(_max)