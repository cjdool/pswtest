# 다시 풀것 dfs

N = int(input())
Alist = [int(x) for x in input().split()]
Olist = [int(x) for x in input().split()]
minval = 1000000000
maxval = -1000000000

def dfs(idx, ans):
    global maxval, minval

    if idx == N:
        maxval = max(maxval, ans)
        minval = min(minval, ans)
        return

    if Olist[0] > 0:
        Olist[0] -= 1
        dfs(idx+1, ans+Alist[idx])
        Olist[0] += 1
    if Olist[1] > 0:
        Olist[1] -= 1
        dfs(idx+1, ans-Alist[idx])
        Olist[1] += 1
    if Olist[2] > 0:
        Olist[2] -= 1
        dfs(idx+1, ans*Alist[idx])
        Olist[2] += 1
    if Olist[3] > 0:
        Olist[3] -= 1
        dfs(idx+1, int(ans/Alist[idx]))
        Olist[3] += 1


dfs(1, Alist[0])
print(maxval)
print(minval)
