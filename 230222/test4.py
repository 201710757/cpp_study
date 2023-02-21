import sys
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

# n, r = map(int, sys.stdin.readline().split())

N = int(input())
board = list(map(int, sys.stdin.readline().split()))

# print(board)


normal = [b for b in board]
reverse = [board[len(board)-idx-1] for idx in range(len(board))]


cache_norm = [1 for _ in range(len(board))]
cache_reverse = [1 for _ in range(len(board))]

for i in range(len(board)):
    for j in range(i):
        if normal[i] > normal[j]:
            cache_norm[i] = max(cache_norm[i], cache_norm[j]+1)
        if reverse[i] > reverse[j]:
            cache_reverse[i] = max(cache_reverse[i], cache_reverse[j]+1)
res = [cache_norm[i] + cache_reverse[len(cache_norm)-1-i] - 1 for i in range(len(cache_norm))]

# print(res)
print(max(res))
# print(normal, reverse)





# print(normal, reverse)
    


# def f():
#     for i in range(1, N):
#         for j in range(i+1):
#             board[i][j] += board[i-1][j] if j==0 else \
#                             board[i-1][j-1] if j==i else \
#                             max(board[i-1][j-1], board[i-1][j])
            
#     return max(board[-1])


# print(f())

# 1, 2, 3, 4, 5                 5 4 3 2 1