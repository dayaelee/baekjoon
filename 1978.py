n = int(input())

nlist = []

nlist = list(map(int, input().split()))

count = 0
for i in range(0, len(nlist)):
    j = 1
    if nlist[i] == 1 or nlist[i] == 0:
        pass
    elif nlist[i] == 2 or nlist[i] == 3 or nlist[i] ==5 :
        count= count+1
    else:
        while 1:
            if j+1==1001:
                count = count+1
                break
            else:
                if j == 1:
                    j = j+1
                    pass
                else:
                    if nlist[i] % j == 0:
                        if j== nlist[i]:
                            count= count+1
                            break
                        else:
                            pass
                            break
                    else:
                        j=j+1
print(count)