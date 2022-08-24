import copy 
import sys
input = sys.stdin.readline

N = int(input())
# board = np.zeros([N,N])
board = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     tmp = input().split()
#     for j, data in enumerate(tmp):
#         board[i][j] = int(data)

def up(board):
    for j in range(N):
        select = 0
        for i in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[select][j] == 0:
                    board[select][j] = tmp
                    
                elif board[select][j]  == tmp:
                    board[select][j] *= 2
                    select += 1
                    
                else:
                    select += 1
                    board[select][j] = tmp
    return board

def down(board):
    for j in range(N):
        select = N - 1
        for i in range(N-2):
            if board[N - 2 - i+1][j]:
                tmp = board[N - 2 - i+1][j]
                board[N - 2 - i+1][j] = 0
                
                if board[select][j] == 0:
                    board[select][j] = tmp
                    
                elif board[select][j]  == tmp:
                    board[select][j] *= 2
                    select -= 1
                    
                else:
                    select -= 1
                    board[select][j] = tmp
    return board

def left(board):
    for i in range(N):
        select = 0
        for j in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][select] == 0:
                    board[i][select] = tmp
                elif board[i][select]  == tmp:
                    board[i][select] *= 2
                    select += 1
                else:
                    select += 1
                    board[i][select]= tmp
    return board
    
def right(board):
    for i in range(N):
        select = N -1
        for j in range(N-2):
            if board[N-2-i+1][j]:
                tmp = board[N-2-i+1][j]
                board[N-2-i+1][j] = 0
                if board[N-2-i+1][select] == 0:
                    board[N-2-i+1][select] = tmp
                elif board[N-2-i+1][select]  == tmp:
                    board[N-2-i+1][select] *= 2
                    select -= 1
                else:
                    select -= 1
                    board[N-2-i+1][select]= tmp
    return board

def dfs(board, cnt):
    if cnt == 5:
        return max(map(max, board))
        
    return max(dfs(up(copy.deepcopy(board)), cnt + 1), \
        dfs(down(copy.deepcopy(board)), cnt + 1), \
            dfs(left(copy.deepcopy(board)), cnt + 1), \
                dfs(right(copy.deepcopy(board)), cnt + 1))

print(dfs(board, 0))