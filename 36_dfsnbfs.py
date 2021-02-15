from collections import deque

inlist = list(map(int, input().split()))
N = inlist[0]
M = inlist[1]
V = inlist[2] - 1
rellist = [[] for x in range(N)]

for i in range(M):
    rel = list(map(int, input().split()))
    rellist[rel[0]-1].append(rel[1]-1)
    rellist[rel[1]-1].append(rel[0]-1)


def basic_dfs(graph, root):
    visited = []
    stack = [root]

    while len(stack) != 0:
        cur = stack.pop()
        if cur not in visited:
            visited.append(cur)
            temp = sorted(graph[cur], reverse=True)
            for item in temp:
                stack.append(item)
    return visited


def basic_bfs(graph, root):
    visited = []
    queue = deque([root])

    while len(queue) != 0:
        cur = queue.popleft()
        if cur not in visited:
            visited.append(cur)
            temp = sorted(graph[cur])
            for item in temp:
                queue.append(item)
    return visited


dfsout = [x+1 for x in basic_dfs(rellist, V)]
bfsout = [x+1 for x in basic_bfs(rellist, V)]

print(*dfsout)
print(*bfsout)