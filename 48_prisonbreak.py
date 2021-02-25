import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
tmap = []
visited = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
startx = 0
starty = 0
for i in range(R):
    temp = list(sys.stdin.readline().strip())
    tmap.append(temp)
    visited.append([-1]*C)
    if 'S' in temp:
        startx = i
        for j in range(C):
            if temp[j] == 'S':
                starty = j

queue = deque([(startx, starty)])
visited[startx][starty] = 0
timemap = [tmap]
pos = True

def makenextmap(currentmap):




while queue:
    x, y = queue.popleft()
    curtime = visited[x][y]

    if tmap[x][y] == 'D':
        pos = False
        print(curtime)
        break

    if curtime+1 >= len(timemap): # 2초 -> 3초 자료 필요 -> 최소 4길이 보
        curmap = timemap[curtime]
        nextmap = makenextmap(curmap)
        timemap.append(nextmap)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < R and 0<= ny < C:







if pos:
    print('KAKTUS')
