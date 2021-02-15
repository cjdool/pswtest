heightlist = []

for i in range(9):
    heightlist.append(int(input()))

flag = 0

for i in heightlist:
    templist = heightlist[:]
    templist.remove(i)
    for j in templist:
        templist2 = templist[:]
        templist2.remove(j)
        if sum(templist2) == 100:
            templist2.sort()
            for i in templist2:
                print(i)
            flag = 1
            break
    if flag == 1:
        break