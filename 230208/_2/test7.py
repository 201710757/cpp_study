import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

def fac(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

# arr = list(map(int, sys.stdin.readline().split()))
n, r = map(int, sys.stdin.readline().split())

print(int(fac(n) / (fac(n-r) * fac(r))))
