import sys
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

# n, r = map(int, sys.stdin.readline().split())

N = int(input())
# board = list(map(int, sys.stdin.readline().split()))



tile = [0 for _ in range(1000001)]

tile[1] = 1
tile[2] = 2
tile[3] = 3

'''
tile[1] = 1; // 1
tile[2] = 2; // 00 11
tile[3] = 3; // 001 100 111 | 000(x)
tile[4] = 5; // 0011 0000 1001 1100 1111
'''


for i in range(4,N+1):
    tile[i] = (tile[i-1] + tile[i-2]) % 15746

print(tile[N])