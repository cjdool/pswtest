from itertools import combinations

testcase = []

while True:
    inlist = input().split()

    if inlist[0] == '0':
        break

    testcase.append(inlist)

for case in testcase:
    k = case[0]
    S = case[1:]
    odx = list(combinations(S, 6))
    for item in odx:
        print(' '.join(item))
    print()
