import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()
# arr = [[False]*N for _ in range(N)]
N = int(sys.stdin.readline()) #map(int, sys.stdin.readline().split())

arr = [['*']*N for _ in range(N)]

def f(n):
    n = int(n)
    if n < 3:
        return
    for k in range(int(N/n)):
        for l in range(int(N/n)):
            for i in range(int(n/3)):
                for j in range(int(n/3)):
                    x = int(n/3) + n*(k) + int(i)
                    y = int(n/3) + n*(l) + int(j)
                    # print(x, y)
                    arr[x][y] = ' '
            # arr[int(n/3) + int(i)][int(n/3) + int(j)] = ' '
            # arr[int(n/3) + int(i)][int(n/3) + int(j)] = ' '
    f(n/3)
    

def _print():
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end='')
        print()
        

f(N)
_print()