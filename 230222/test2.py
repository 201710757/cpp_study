import sys
import itertools
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

# n, r = map(int, sys.stdin.readline().split())

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# print(board)


def f():
    for i in range(1, N):
        board[i][0] += min(board[i-1][1], board[i-1][2])
        board[i][1] += min(board[i-1][0], board[i-1][2])
        board[i][2] += min(board[i-1][1], board[i-1][0])
    return min(board[-1])


# def f():
#     result = []

#     for idx in range(3):
#         res = [board[0][idx]]
#         f_idx = idx
#         for i in range(1, N):
#             for _idx in range(3):
#                 if f_idx != _idx:
#                     f_idx = _idx
#                     res.append(board[i][_idx])
#                     break
#         print(res)
#         result.append(sum(res))
#     return min(result)

print(f())