import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001

queue = deque([N])
visited[N] = 1

while queue:
    x = queue.popleft()

    if x == K:
        print(visited[x]-1)
        break

    nx = 2*x
    while nx <= 100000 and visited[nx] != visited[x]:
        if 0 <= nx <= 100000 and visited[nx] == 0:
            visited[nx] = visited[x]
            queue.append(nx)
        nx = 2*nx

    for nx in [x+1, x-1]:
        if 0 <= nx <= 100000 and visited[nx] == 0:
            visited[nx] = visited[x] + 1
            queue.append(nx)

'''
문제에 버그가 있는거 같음

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001

queue = deque([N])
visited[N] = 1

while queue:
    x = queue.popleft()

    if x == K:
        print(visited[x]-1)
        break

    nx = 2*x
    if 0 <= nx <= 100000 and visited[nx] == 0:
        visited[nx] = visited[x]
        queue.append(nx)

    for nx in [x+1, x-1]:
        if 0 <= nx <= 100000 and visited[nx] == 0:
            visited[nx] = visited[x] + 1
            queue.append(nx)
'''