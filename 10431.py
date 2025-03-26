p = int(input())
for i in range(p):
    l = list(map(int, input().split()))
    child=[]
    answer=0
    for j in range(1, len(l)):
        if j == 1:
            child.append(l[j])
        else:
            check = 0
            insertI=0
            for v in range(len(child)):
                if child[v] < l[j]:
                    continue
                else:
                    
                    answer += 1
                    check += 1
                    if check ==1:
                        insertI== v
                    
            if check ==0:
                child.append(l[j])
            else:
                child.insert(insertI, l[j])
    print(i+1, answer)

