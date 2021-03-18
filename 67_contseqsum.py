import sys

n = int(sys.stdin.readline())
inlist = list(map(int, sys.stdin.readline().split()))

ans = [0] * n
ans[0] = inlist[0]
for i in range(1,n):
    ans[i] = max(inlist[i], inlist[i]+ans[i-1])
print(max(ans))


'''
prevlst = inlist
maxval = max(inlist)

for i in range(1, n):
    curlst = []
    for j in range(n-i):
        curlst.append(inlist[j] + prevlst[j+1])
    prevlst = curlst
    maxval = max(maxval, max(curlst))

print(maxval)
'''
