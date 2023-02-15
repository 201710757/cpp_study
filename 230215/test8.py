import sys
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
team = [0 for _ in range(21)]

global _min
_min = 987654321

def dfs(n, s):
    global _min

    if n == N//2:
        start = 0
        link = 0

        for i in range(N):
            if team[i] == 1:
                for j in range(N):
                    if team[j] == 1: start += board[i][j]
            elif team[i] == 0:
                for j in range(N):
                    if team[j] == 0: link += board[i][j]

        sc = abs(start - link)
        if _min > sc: _min = sc

        return
    
    for i in range(s, N):
        team[i] = 1
        dfs(n+1, i+1)
        team[i] = 0



dfs(0, 0)
print(int(_min))

