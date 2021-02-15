#다시 풀것 Dynamic Programming
def getcase(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return getcase(num-1) + getcase(num-2) + getcase(num-3)


T = int(input())

inlist = []
for i in range(T):
    inlist.append(int(input()))

for item in inlist:
    print(getcase(item))
