instr = input()
inlist = instr.split()
E = int(inlist[0])  # 15
S = int(inlist[1])  # 28
M = int(inlist[2])  # 19

for y in range(286):
    if (28*y + S - E) % 15 == 0:
        if (28*y + S - M) % 19 == 0:
            print(28*y+S)
            break
