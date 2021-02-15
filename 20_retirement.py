# dp, dfs 두가지 가능 -> dp로 한번 풀어볼것

N = int(input())

paylist = []
graphlist = []
for i in range(N):
    inlist = list(map(int, input().split()))
    graphrow = []
    nextstart = inlist[0] + i
    if nextstart < N:
        for j in range(nextstart, N):
            graphrow.append(j)
    graphlist.append(graphrow)
    if nextstart <= N:
        paylist.append(inlist[1])
    else:
        paylist.append(0)

maxval = -1000000000

def recursive_dfs(cost, root):
    global maxval
    if len(graphlist[root]) == 0:
        cost += paylist[root]
        maxval = max(cost, maxval)
        return
    cost += paylist[root]
    for item in graphlist[root]:
        recursive_dfs(cost, item)
    return

for i in range(N):
    recursive_dfs(0, i)

print(maxval)