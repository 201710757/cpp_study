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

_x, _y = map(int, sys.stdin.readline().split())

gcd = _gcd(_x, _y)
# while True:
#     r1 = _x % _y
#     if r1 == 0:
#         gcd = r3
#         break

#     r2 = _y % r1
#     if r2 == 0:
#         gcd = r1
#         break

#     r3 = r1 % r2
#     if r3 == 0:
#         gcd = r2
#         break
print(gcd)
print(int(_x*_y / gcd))