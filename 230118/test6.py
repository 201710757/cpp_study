import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline()) #map(int, sys.stdin.readline().split())


def h(n, s, e, sub):
    if n == 1:
        print(s, e)
        return
    
    h(n-1, s, sub, e)
    print(s, e)
    h(n-1, sub, e, s)
print(2**N - 1)
h(N, 1, 3, 2)