import sys
import itertools
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]


board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
pos = []
N = 0

# def check_square(x, y):
#     check = [0 for _ in range(10)]

#     for i in range(int(x/3)*3, int(x/3)*3 + 3):
#         for j in range(int(y/3)*3, int(y/3)*3 + 3):
            
#             check[board[i][j]] += 1

#     for c in check:
#         if c >1 or c == 0:
#             return False

#     return True
def check_square(x, y, num):
    check = []

    for i in range(int(x/3)*3, int(x/3)*3 + 3):
        for j in range(int(y/3)*3, int(y/3)*3 + 3):
            check.append(board[i][j])
            # check[i*3 + j] += 1

    if num in check:
        return False

    return True

# def check_horizontal(x, y):
#     check = [0 for _ in range(10)]

#     for i in range(9):
#         check[board[x][i]] += 1

#     for c in check:
#         if c >1 or c == 0:
#             return False

#     return True

def check_horizontal(x, y, num):
    check = []

    for i in range(9):
        check.append(board[x][i])

    if num in check:
        return False

    return True

# def check_vertical(x, y):
#     check = [0 for _ in range(10)]

#     for i in range(9):
#         check[board[i][y]] += 1

#     for c in check:
#         if c >1 or c == 0:
#             return False

#     return True
def check_vertical(x, y, num):
    check = []

    for i in range(9):
        check.append(board[i][y])

    if num in check:
        return False

    return True

def checking(x, y, num):
    # print(check_square(x, y, num) , check_horizontal(x, y, num) , check_vertical(x, y, num))
    return check_square(x, y, num) and check_horizontal(x, y, num) and check_vertical(x, y, num)

'''
# def check_square():
#     for base_x in [0, 3, 6]:
#         for base_y in [0, 3, 6]:
#             check = [0 for _ in range(10)]

#             for i in range(3):
#                 for j in range(3): 
#                     check[board[base_x + i][base_y + j]] += 1

#             for c in check:
#                 if c >1 or c == 0:
#                     return False
#     return True

# def check_horizontal():
#     for x in range(9):
#         check = [0 for _ in range(10)]

#         for i in range(9):
#             check[board[x][i]] += 1

#         for c in check:
#             if c >1 or c == 0:
#                 return False

#     return True

# def check_vertical():
#     for y in range(9):
#         check = [0 for _ in range(10)]

#         for i in range(9):
#             check[board[i][y]] += 1

#         for c in check:
#             if c >1 or c == 0:
#                 return False

#     return True

# def checking():
#     # print(check_square(x, y) , check_horizontal(x, y) , check_vertical(x, y))
#     return check_square() and check_horizontal() and check_vertical()
'''


def dfs(n):
    # for i in range(9):
    #     for j in range(9):
    #         print(board[i][j], end = ' ')
    #     print()
    x, y = pos[n]
    # print(n, N)
    if n == N-1:
        print()
        for i in range(9):
            for j in range(9):
                print(board[i][j], end = ' ')
            print()

        # print("res")
        # for x,y in pos:
        #     print(x, y, board[x][y])

        import sys
        sys.exit(0)
        return

    else:
        # if board[x][y] == 0:
        for i in range(9):
            
            if checking(x, y, i+1):
                board[x][y] = i+1

                dfs(n+1)

                board[x][y] = 0
            # pos.append([x,y])
            
        
        # dfs(x, y)


for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            pos.append([i, j])

N = len(pos)

dfs(0)

