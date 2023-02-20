import sys
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

# n, r = map(int, sys.stdin.readline().split())

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def f():
    for i in range(1, N):
        for j in range(i+1):
            board[i][j] += board[i-1][j] if j==0 else \
                            board[i-1][j-1] if j==i else \
                            max(board[i-1][j-1], board[i-1][j])
            
    return max(board[-1])


print(f())

