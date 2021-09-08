import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
tmap = []
visited = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque([])
waterqueue = deque([])
startx = 0
starty = 0
for i in range(R):
    temp = list(sys.stdin.readline().strip())
    tmap.append(temp)
    visited.append([-1]*C)
    for j in range(C):
        if temp[j] == 'S':
            queue.append((i, j))
            startx = i
            starty = j
        if temp[j] == '*':
            waterqueue.append((i, j))


visited[startx][starty] = 0
timemap = [tmap]
pos = True

while queue:
    x, y = queue.popleft()
    curtime = visited[x][y]

    if tmap[x][y] == 'D':
        pos = False
        print(curtime)
        break

    if curtime >= len(timemap)-1:
        curmap = timemap[curtime]





        timemap.append(nextmap)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < R and 0<= ny < C:
            if visited[nx][ny] == -1 and (timemap[curtime+1][nx][ny] != '*' or timemap[curtime+1][nx][ny] != 'X'):
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


if pos:
    print('KAKTUS')
