import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

x,y = map(int, sys.stdin.readline().split())

print(min(abs(x), abs(y), abs(w-x), abs(h-y)))

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


