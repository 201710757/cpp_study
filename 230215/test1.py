import sys
import itertools
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

n, r = map(int, sys.stdin.readline().split())
ans = itertools.permutations([(i+1) for i in range(n)], r)

for a in ans:
    if len(a) <= 1:
        print(a[0])
    else:
        for _a in a:
            print(_a, end=' ')
        print()
