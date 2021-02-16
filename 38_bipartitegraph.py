import sys

def checkbipart(graph, num):
    visited = [False] * num
    color = [0] * num
    for i in range(num):
        if not visited[i]:
            visited[i] = True
            color[0] = 1
            queue = [i]

            while len(queue) != 0:
                cur = queue.pop(0)
                for item in graph[cur]:
                    if not visited[item]:
                        color[item] = -1 * color[cur]
                        visited[item] = True
                        queue.append(item)
                    else:
                        if color[item] == color[cur]:
                            return False

    return True


K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    rellist = [[] for _ in range(V)]
    for i in range(E):
        u, v = map(int, sys.stdin.readline().split())
        rellist[u-1].append(v-1)
        rellist[v-1].append(u-1)
    if checkbipart(rellist, V):
        print('YES')
    else:
        print('NO')