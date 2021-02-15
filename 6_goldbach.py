def isprime(number):
    if number < 2:
        return False
    if number % 2 == 0 and number != 2:
        return False
    i = 3
    while i*i <= number:
        if number % i == 0:
            return False
        i+=2
    return True


def getoddprime(number): # a가 가장 작은것
    for i in range(3, number, 2):
        if isprime(i):
            if isprime(number-i):
                return i
    return 0


retlist = []
while True:
    n = int(input())
    if n == 0:
        break
    a = getoddprime(n)
    if a != 0:
        retlist.append('%d = %d + %d' % (n, a, n-a))
    else:
        retlist.append("Goldbach's conjecture is wrong.")


for retstr in retlist:
    print(retstr)