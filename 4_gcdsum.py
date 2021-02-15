def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(input())
retlist = []
for i in range(t):
    instr = input()
    inlist = instr.split()
    n = int(inlist[0])
    retsum = 0
    for j in range(n-1):
        for k in range(j+1, n):
            retsum += gcd(int(inlist[j+1]), int(inlist[k+1]))
    retlist.append(retsum)
for item in retlist:
    print(item)