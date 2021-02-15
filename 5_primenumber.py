def isprime (a):
    if a < 2:
        return False
    if a % 2 == 0 and a != 2:
        return False
    i = 3
    while i*i <= a:
        if a % i == 0:
            return False
        i+=2
    return True


N = int(input())
instr = input()
inlist = instr.split()
inlist = [int(x) for x in inlist]
cnt = 0

for item in inlist:
    if isprime(item):
        cnt+=1

print(cnt)
