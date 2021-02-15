instr = input()
inlist = instr.split()
A = int(inlist[0])
B = int(inlist[1])

if B > A:
    A, B = B, A

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return int(a*b/gcd(a, b))

print(gcd(A, B))
print(lcm(A, B))