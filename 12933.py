# 울음 소리를 한 번 또는 그 이상 연속해서 내는 것

# quack이 끝나기전에 q가 나오면 다른 마리인 것.
# quack이 완벽하게 끝나고 또 quack이 완벽하게 끝나면 한마리로 침

tmp = []

s = input()

waitList=[]

check = 0

for i in s:
    if i == 'q':
        if waitList:
            where = waitList.pop()
            tmp[where] = 0
        else:
            tmp.append(0)
    elif i == 'u':
        try: 
            where = tmp.index(0)
        except ValueError: 
            check = 1
            break
        tmp[where]+=1
    elif i == 'a':
        try: 
            where = tmp.index(1)
        except ValueError: 
            check = 1
            break
        tmp[where]+=1
    elif i == 'c':
        try: 
            where = tmp.index(2)
        except ValueError: 
            check = 1
            break
        tmp[where]+=1
    elif i == 'k':
        try: 
            where = tmp.index(3)
        except ValueError: 
            check = 1
            break
        tmp[where]+=1
        waitList.append(where)
result = 0
if check ==1:
    print(-1)
else:
    for i in tmp:
        if i == 4:
            result +=1  
        else:
            print(-1)
            check = 1
            break
if check !=1:
    print(result)