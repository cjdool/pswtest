import sys

N, M = map(int, sys.stdin.readline().split())
rellist = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    rellist[u].append(v)
    rellist[v].append(u)


def bfs(root):
    queue = [root]
    while queue:
        cur = queue.pop(0)
        for item in rellist[cur]:
            if visited[item] == 0:
                visited[item] = 1
                queue.append(item)

    return


cc = 0
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cc += 1

print(cc)
