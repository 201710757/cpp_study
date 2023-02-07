import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

def _gcd(x ,y):
    if y == 0:
        return x
    else:
        return _gcd(y, x%y)
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))


A = []
B = []

main = arr[0]
for a in arr[1:]:
    gcd = _gcd(main, a)
    A.append(int(main / gcd))
    B.append(int(a / gcd))
for i in range(len(A)):
    print(A[i], end='')
    print('/', end='')
    print(B[i])