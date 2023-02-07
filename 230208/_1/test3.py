
import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

r = 'right'
w = 'wrong'
res = []
while True:
    _x, _y, _z = map(int, sys.stdin.readline().split())

    arr = sorted([_x,_y,_z])
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2:
        res.append(r)
    else:
        res.append(w)

for r in res:
    print(r)