import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

def f(n):
    arr = list(map(int, str(n)))
    
    return sum(arr) + n

# N, M = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))



N = int(sys.stdin.readline())
cnt = 0
i = 0
while True:
    i += 1
    # n = list(map(int, str(i)))
    n = str(i)
    if '666' in n:
        cnt += 1
    if cnt == N:
        print(i)
        break

