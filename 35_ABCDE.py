inlist = list(map(int, input().split()))
N = inlist[0]
M = inlist[1]
rellist = [[] for x in range(N)]

for i in range(M):
    rel = list(map(int, input().split()))
    rellist[rel[0]].append(rel[1])
    rellist[rel[1]].append(rel[0])

flag = False


def dfs(idx, cnt, visited=[]):
    global flag
    visited.append(idx)
    if cnt >= 4:
        flag = True
    else:
        for item in rellist[idx]:
            if not item in visited:
                dfs(item, cnt+1, visited)
                visited.remove(item)
    return


for i in range(N):
    if flag is False:
        dfs(i, 0, [])

print(1 if flag else 0)