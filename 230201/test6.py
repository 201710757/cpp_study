import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()



N, M = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
s1 = set()
s2 = set()

arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))
for a in arr1:
    s1.add(a)

for a in arr2:
    s2.add(a)

print(len(s1 - s2) + len(s2 - s1))


# M = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# for a in arr:
#     if a in s:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

# # _max = -987654321

# # for i in range(N):
# #     for j in range(N):
# #         for k in range(N):
# #             if i == j or j == k or i == k:
# #                 continue
# #             pick = arr[i] + arr[j] + arr[k]
# #             if pick <= M and _max < pick:
# #                 _max = pick
        



# # print(_max)


