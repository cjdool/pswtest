import sys
from collections import deque

S = int(sys.stdin.readline())
queue = deque([(1,0,0)])
visited = {1, 0}

while queue:
    curcnt, curclip, curtime = queue.popleft()

    if curcnt == S:
        print(curtime)
        break

    if (curcnt, curcnt) not in visited:
        queue.append((curcnt, curcnt, curtime + 1))
        visited.add((curcnt, curcnt))
    if curclip != 0 and (curcnt + curclip, curclip) not in visited:
        queue.append((curcnt + curclip, curclip, curtime + 1))
        visited.add((curcnt+curclip, curclip))
    if curcnt - 1 >= 0 and (curcnt-1, curclip) not in visited:
        queue.append((curcnt - 1, curclip, curtime + 1))
        visited.add((curcnt-1, curclip))

'''        
ch = [[-1]*(S+1) for i in range(S+1)]  # x -> curcnt y -> curclip

queue = deque()
queue.append([1, 0])
ch[1][0] = 0

while queue:
    x, y = queue.popleft()

    if ch[x][x] == -1:  # clip copy
        ch[x][x] = ch[x][y] + 1
        queue.append([x, x])
    if x+y <= S and ch[x+y][y] == -1:  # clip paste
        ch[x+y][y] = ch[x][y] + 1
        queue.append([x+y, y])
    if x-1 >= 0 and ch[x-1][y] == -1:  # emote delete
        ch[x-1][y] = ch[x][y] + 1
        queue.append([x-1, y])

r = ch[S][1]
for i in range(1,S):
    if ch[S][i] != -1:
        r = min(r, ch[S][i])
print(r)
'''