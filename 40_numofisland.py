import sys
sys.setrecursionlimit(10000)


def basic_dfs(curx, cury, cnt):
    if smeb[curx][cury] == 0:
        visited[curx][cury] = True
        return cnt

    if not visited[curx][cury]:
        visited[curx][cury] = True
        cnt += 1
        if curx != h-1:
            cnt = basic_dfs(curx+1, cury, cnt)
        if curx != h-1 and cury != w-1:
            cnt = basic_dfs(curx+1, cury+1, cnt)
        if cury != w-1:
            cnt = basic_dfs(curx, cury+1, cnt)
        if cury != w-1 and curx != 0:
            cnt = basic_dfs(curx-1, cury+1, cnt)
        if curx != 0:
            cnt = basic_dfs(curx-1, cury, cnt)
        if curx != 0 and cury != 0:
            cnt = basic_dfs(curx-1, cury-1, cnt)
        if cury != 0:
            cnt = basic_dfs(curx, cury-1, cnt)
        if cury != 0 and curx != h-1:
            cnt = basic_dfs(curx+1, cury-1, cnt)
    return cnt


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    smeb = []
    visited = []
    for _ in range(h):
        smeb.append(list(map(int, sys.stdin.readline().split())))
        visited.append([False]*w)

    housenum = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and smeb[i][j] != 0:
                temphouse = basic_dfs(i, j, 0)
                housenum.append(temphouse)

    print(len(housenum))

'''
# up, right, down, left, up-right, down-right, down-left, up-left
dxs = (0, 1, 0, -1, 1, 1, -1, -1)
dys = (1, 0, -1, 0, 1, -1, -1, 1)

def DFS(x1, y1):
    maps[y1][x1] = 0
    stack = [(x1, y1)]

    while stack:
        x, y = stack.pop()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue

            if maps[ny][nx]:
                maps[ny][nx] = 0
                stack.append((nx, ny))

answers = []

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    maps = []

    for i in range(h):
        l = list(map(int, input().split()))
        maps.append(l)

    num = 0

    for y in range(h):
        for x in range(w):
            if maps[y][x]:
                DFS(x, y)
                num += 1

    answers.append(num)


for num in answers:
    print(num)
    
'''