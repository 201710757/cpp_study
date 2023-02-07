
import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
x = []
y = []
for _ in range(3):
    _x, _y = map(int, sys.stdin.readline().split())
    if _x not in x:
        x.append(_x)
    else:
        x.remove(_x)

    if _y not in y:
        y.append(_y)
    else:
        y.remove(_y)

print(x[0], y[0])

    




# _max = -987654321

# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             if i == j or j == k or i == k:
#                 continue
#             pick = arr[i] + arr[j] + arr[k]
#             if pick <= M and _max < pick:
#                 _max = pick
        



# print(_max)


