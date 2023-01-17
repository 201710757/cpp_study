import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()
A, K = map(int, sys.stdin.readline().split()) #map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
tmp = [False]*len(arr)
res = []
def merge_sort(p, r):
    if p < r:
        q = int((p+r) / 2)
        merge_sort(p, q)
        merge_sort(q+1, r)
        merge(p, q, r)
        
def merge(p, q, r):
    i = p
    j = q + 1
    t = 0

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
            t += 1
        else:
            tmp[t] = arr[j]
            j += 1
            t += 1
    
    while i<=q:
        # print(t, i)
        tmp[t] = arr[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = arr[j]
        t += 1
        j += 1
    i = p
    t = 0

    while i <= r:
        arr[i] = tmp[t]
        res.append(tmp[t])
        i +=1
        t += 1
        # print(arr)
        


merge_sort(0, len(arr)-1)
print(res[K-1]) if len(res) >= K else print(-1)