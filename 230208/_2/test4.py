import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

def _gcd(x ,y):
    if y == 0:
        return x
    else:
        return _gcd(y, x%y)
N = int(input())

res = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    gcd = _gcd(a, b)

    res.append(int(a*b / gcd))

for r in res:
    print(r)

