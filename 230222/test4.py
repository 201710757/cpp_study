import sys
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

# n, r = map(int, sys.stdin.readline().split())

N = int(input())
board = list(map(int, sys.stdin.readline().split()))

print(board)

max_len = -987654321
arr = []
h = 0
t = N-1

arr.append(board[h])
arr.append(board[t])
while True:
    pass
    


# def f():
#     for i in range(1, N):
#         for j in range(i+1):
#             board[i][j] += board[i-1][j] if j==0 else \
#                             board[i-1][j-1] if j==i else \
#                             max(board[i-1][j-1], board[i-1][j])
            
#     return max(board[-1])


# print(f())

# 1, 2, 3, 4, 5                 5 4 3 2 1