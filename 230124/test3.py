import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

arr = []

def f(x, y):
    if len(arr) == 0:
        arr.append([x,y])
    
    
    return sum(arr) + n

# N, M = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))

# generator of 256 = 245
# generator of 216 = 198 and 207

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

res = []
for a in arr:
    idx = 1
    for _a in arr:
        if _a == a:
            continue
        if a[0] < _a[0] and a[1] < _a[1]:
            idx += 1
    res.append(idx)
# print(res)

for idx,a in enumerate(res):
    if idx == len(res)-1:
        print(res[-1])
    else:
        print(a, end =' ')

# _arr = sorted(arr, key=lambda x:-x[0])
# res = []
# idx = 1
# cap = 0

# res.append(idx)
# for i in range(1, N):
#     if _arr[i][1] > _arr[i-1][1] and _arr[i][0] < _arr[i-1][0]:
#         cap += 1
#     else:
#         idx += cap
#         cap = 0
#         idx += 1
#     res.append(idx)

# rres = []
# # for a in arr:
# #     rres.append(res[_arr.index(a)])

# for a in arr:
#     if a == arr[-1]:
#         print(res[_arr.index(a)])
#     else:
#         print(res[_arr.index(a)], end =' ')


# print(rres)

# print(_arr.index([55,185]))

# print(res) if res != 987654321 else print(0)