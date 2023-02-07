import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
res = ['factor', 'multiple', 'neither']

res = []
while True:
    _x, _y = map(int, sys.stdin.readline().split())
    if _x == 0 and _y == 0:
        break

    if _x >= _y and _x % _y == 0:
        res.append('multiple')
    elif _x <= _y and _y % _x == 0:
        res.append('factor')
    else:
        res.append('neither')

for r in res:
    print(r)