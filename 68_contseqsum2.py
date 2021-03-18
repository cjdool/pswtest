import sys

n = int(sys.stdin.readline())
inlist = list(map(int, sys.stdin.readline().split()))

ans = [[0, 0] for x in range(n)]
ans[0][0] = inlist[0]
maxval = -100000000
if n == 1:
    print(inlist[0])
else:
    for i in range(1,n):
        ans[i][0] = max(inlist[i], inlist[i]+ans[i-1][0])
        ans[i][1] = max(ans[i-1][0], inlist[i]+ans[i-1][1])
        maxval = max(max(ans[i]), maxval)
    print(maxval)

# -5, -6, -7, -8 인경우 일때 때문에 maxval = inlist[0] or 0 으로 두기 풀가능