from collections import deque


def bfs(graph, root):
    visited = [root]
    queue = deque([root])

    while len(queue) != 0:
        cur = queue.popleft()
        for item in graph[cur]:
            if item not in visited:
                visited.append(item)
                queue.append(item)
    return visited


def checkbipart(graph):

    return False

K = int(input())
caselist = []
for _ in range(K):
    V, E = map(int, input().split())
    rellist = [[] for _ in range(V)]
    for i in range(E):
        u, v = map(int, input().split())
        rellist[u-1].append(v-1)
        rellist[v-1].append(u-1)
    caselist.append(rellist)

for case in caselist:
    if checkbipart(case):
        print('YES')
    else:
        print('NO')