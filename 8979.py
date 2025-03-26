n, k = map(int, input().split())
tmp=[]
for i in range(n):
    check = list(map(int, input().split()))
    tmp.append(check)
tmp.sort(key = lambda x: (-x[1], -x[2], -x[3]))
# print(tmp)
rank=1
check = 1

if len(tmp)==2:
    if tmp[0][1]== tmp[1][1] and tmp[0][2]== tmp[1][2] and tmp[0][3]== tmp[1][3]:
        print(1)
    else:
        for j in range(0, len(tmp)):
            if len(tmp)==2:
                if tmp[j][0]==k:
                    print(rank)
                else:
                    rank+=1

else:
    for j in range(1, len(tmp)):
        # print('rank', rank)
        if j ==1:
            if tmp[0][0]==k:
                print(rank)
                break
            else:
                if tmp[j-1][1]== tmp[j][1] and tmp[j-1][2]== tmp[j][2] and tmp[j-1][3]== tmp[j][3]:
                    check+=1
                    pass
                else:
                    if check > 1:
                        rank+=check
                        check = 1
                    else:
                        rank+=1

                if tmp[j][0]==k:
                    print(rank)
                    break
        else: 
            if tmp[j-1][1]== tmp[j][1] and tmp[j-1][2]== tmp[j][2] and tmp[j-1][3]== tmp[j][3]:
                    check+=1
                    pass
            else:
                if check > 1:
                    rank+=check
                    check = 1
                else:
                    rank+=1
            if tmp[j][0]==k:
                print(rank)
                break