import sys

M = int(input())
S = set([])

for i in range(M):
    order = sys.stdin.readline().strip().split()

    op = order[0]
    if len(order) == 1:
        if op == 'all':
            S = set([x for x in range(1,21)])
        else:
            S = set()
        continue

    val = int(order[1])

    if op == 'add':
        S.add(val)
    elif op == 'remove':
        if val in S:
            S.remove(val)
    elif op == 'check':
        print(1 if val in S else 0)
    elif op == 'toggle':
        if val in S:
            S.remove(val)
        else:
            S.add(val)