
n=int(input())


def backtrack(target, length, cnt, before):
    print(target, length, cnt, before)
    if before==-1 and length>1:
        print('go1')
        return backtrack(target, length, cnt+1, target[cnt])
    elif before==-1 and length==1:
        return True
    elif before != -1:   
        if length>cnt:
            if before > target[cnt]:
                print('go2')
                if cnt+1==length:
                    return True
                else:
                    return backtrack(target, length, cnt+1, target[cnt])
            else:
                return False
    
num = 0
check=0
while 1:
    print('check', check)

    if backtrack(list(str(num)), len(list(str(num))), 0, -1):
        if n==0:
            print(0)
            break
        else:
            if num >0:
                check+=1
    
    if check == n:
        print(num)
        break
    num+=1

    # if num==638:
    #     print(-1)
    #     break

